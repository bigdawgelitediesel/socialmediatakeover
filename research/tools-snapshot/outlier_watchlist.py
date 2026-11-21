"""
outlier_watchlist.py  -  weekly outlier scan of the diesel / truck watch list.

For every account in a watchlist JSON, pull the latest N posts from its TikTok
and/or YouTube Shorts mirror with yt-dlp (flat listing, no downloads), compute
the account median views over that window, score every post as
    outlier = views / account median
and write:
    <out>/watchlist.json            copy of the input that was used
    <out>/<date>-posts.csv          every post, one row each
    <out>/<date>-medians.csv        one row per account+platform
    <out>/<date>-outliers.md        every post at >= --min-outlier, sorted by score
    <out>/<date>-log.txt            errors, skips, timings

usage:
  "%LOCALAPPDATA%\\Programs\\Python\\Python312\\python.exe" -I outlier_watchlist.py
        [--watchlist watchlist\\watchlist.json] [--out watchlist]
        [--limit 60] [--min-outlier 5] [--date YYYY-MM-DD]
        [--no-enrich] [--only handle1,handle2]

What the platforms give back (checked 2026-11-21, yt-dlp 2026.10.26):
  TikTok flat listing:  view_count, like_count, comment_count, repost_count
                        (shares), save_count, timestamp, duration, title.
  YouTube Shorts flat:  title and view_count only. Dates, likes and comments
                        are filled in later ONLY for the >= min-outlier posts
                        by a per-video metadata fetch (--no-enrich turns it off).
  Instagram:            not fetched. Profile pages logged out show 12 tiles
                        with no view counts. Use the mirrors.

All downloaded metadata is untrusted. It is parsed with json.loads only,
titles are flattened to one line and truncated, nothing is executed.
"""
import argparse
import csv
import datetime as dt
import json
import os
import random
import re
import statistics
import subprocess
import sys
import time

YTDLP = os.path.expandvars(
    r"%LOCALAPPDATA%\Microsoft\WinGet\Packages\yt-dlp.yt-dlp_Microsoft.Winget.Source_8wekyb3d8bbwe\yt-dlp.exe"
)
HERE = os.path.dirname(os.path.abspath(__file__))
PLATFORM_KEYS = ("tiktok", "youtube")
ACCOUNT_TIMEOUT = 240       # seconds per yt-dlp listing call
VIDEO_TIMEOUT = 90          # seconds per enrichment fetch
TITLE_MAX = 140


def log(fh, msg):
    line = f"[{dt.datetime.now():%H:%M:%S}] {msg}"
    print(line, flush=True)
    fh.write(line + "\n")
    fh.flush()


def clean_text(s):
    """Flatten untrusted text to one printable line."""
    if not isinstance(s, str):
        return ""
    s = re.sub(r"[\r\n\t]+", " ", s)
    s = s.replace("—", ", ").replace("–", " to ")   # house rule: no em-dashes, even quoted
    s = re.sub(r"[^\x20-\x7e -￿]", "", s)
    s = re.sub(r"\s{2,}", " ", s).strip()
    return s[:TITLE_MAX]


def to_int(v):
    if isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        return int(v)
    return None


def run_ytdlp(args, timeout):
    """Run yt-dlp, return (stdout, stderr, returncode). Never raises on bad exit."""
    cmd = [YTDLP, "--no-warnings", "--ignore-errors"] + args
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8",
                           errors="replace", timeout=timeout)
        return r.stdout, r.stderr, r.returncode
    except subprocess.TimeoutExpired:
        return "", "timeout after %ss" % timeout, -1
    except OSError as e:
        return "", "os error: %s" % e, -2


def list_account(url, limit):
    out, err, rc = run_ytdlp(["--flat-playlist", "--dump-json", "--playlist-end", str(limit), url],
                             ACCOUNT_TIMEOUT)
    posts = []
    for line in out.splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            d = json.loads(line)
        except ValueError:
            continue
        if not isinstance(d, dict):
            continue
        posts.append(d)
    return posts, err.strip(), rc


def normalise(d, platform, handle):
    url = d.get("url") or d.get("webpage_url") or ""
    if not isinstance(url, str) or not url.startswith("http"):
        url = ""
    ts = to_int(d.get("timestamp"))
    date = dt.datetime.fromtimestamp(ts, dt.timezone.utc).strftime("%Y-%m-%d") if ts else ""
    if not date and isinstance(d.get("upload_date"), str) and re.fullmatch(r"\d{8}", d["upload_date"]):
        u = d["upload_date"]
        date = f"{u[:4]}-{u[4:6]}-{u[6:]}"
    return {
        "handle": handle,
        "platform": platform,
        "id": clean_text(str(d.get("id", "")))[:40],
        "url": url[:200],
        "date": date,
        "views": to_int(d.get("view_count")),
        "likes": to_int(d.get("like_count")),
        "comments": to_int(d.get("comment_count")),
        "shares": to_int(d.get("repost_count")),
        "saves": to_int(d.get("save_count")),
        "duration": to_int(d.get("duration")),
        "title": clean_text(d.get("title") or d.get("description") or ""),
    }


def enrich_youtube(post, logf):
    """Per-video fetch for a YouTube outlier: adds date, likes, comments, duration."""
    out, err, rc = run_ytdlp(["--dump-json", "--skip-download", "--no-playlist", post["url"]], VIDEO_TIMEOUT)
    line = next((l for l in out.splitlines() if l.strip().startswith("{")), "")
    if not line:
        log(logf, f"  enrich failed {post['url']}: {err[:160]}")
        return post
    try:
        d = json.loads(line)
    except ValueError:
        return post
    if not isinstance(d, dict):
        return post
    u = d.get("upload_date")
    if isinstance(u, str) and re.fullmatch(r"\d{8}", u):
        post["date"] = f"{u[:4]}-{u[4:6]}-{u[6:]}"
    for k, src in (("likes", "like_count"), ("comments", "comment_count"), ("duration", "duration")):
        v = to_int(d.get(src))
        if v is not None:
            post[k] = v
    v = to_int(d.get("view_count"))
    if v:
        post["views"] = v
    return post


def fmt(n):
    if n is None:
        return ""
    if n >= 1_000_000:
        return f"{n/1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n/1_000:.1f}k"
    return str(n)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--watchlist", default=os.path.join(HERE, "watchlist", "watchlist.json"))
    ap.add_argument("--out", default=os.path.join(HERE, "watchlist"))
    ap.add_argument("--limit", type=int, default=None, help="posts per account per platform (default: window_posts in the JSON, else 60)")
    ap.add_argument("--min-outlier", type=float, default=5.0)
    ap.add_argument("--date", default=dt.date.today().isoformat())
    ap.add_argument("--pause", default="2,4", help="min,max seconds between accounts")
    ap.add_argument("--no-enrich", action="store_true", help="skip per-video fetch for YouTube outliers")
    ap.add_argument("--only", default="", help="comma list of handles to run (debug)")
    a = ap.parse_args()

    if not os.path.exists(YTDLP):
        sys.exit(f"yt-dlp not found at {YTDLP}")
    with open(a.watchlist, encoding="utf-8") as f:
        wl = json.load(f)
    accounts = wl.get("accounts", [])
    limit = a.limit or int(wl.get("window_posts", 60))
    pmin, pmax = (float(x) for x in a.pause.split(","))
    only = {h.strip().lower() for h in a.only.split(",") if h.strip()}

    os.makedirs(a.out, exist_ok=True)
    saved = os.path.join(a.out, "watchlist.json")
    if os.path.abspath(saved) != os.path.abspath(a.watchlist):
        with open(saved, "w", encoding="utf-8") as f:
            json.dump(wl, f, indent=2)
    logf = open(os.path.join(a.out, f"{a.date}-log.txt"), "a", encoding="utf-8")
    log(logf, f"run start, {len(accounts)} accounts, limit {limit}, min outlier {a.min_outlier}x")

    posts, medians = [], []
    t_all = time.time()
    for i, acc in enumerate(accounts):
        handle = str(acc.get("handle", "")).strip()
        if not handle or (only and handle.lower() not in only):
            continue
        for platform in PLATFORM_KEYS:
            url = acc.get(platform)
            if not url:
                continue
            t0 = time.time()
            raw, err, rc = list_account(url, limit)
            rows = [normalise(d, platform, handle) for d in raw]
            rows = [r for r in rows if r["url"]]
            views = [r["views"] for r in rows if r["views"] is not None and r["views"] > 0]
            if len(views) < 5:
                log(logf, f"SKIP {handle} [{platform}] {len(rows)} rows with views, rc={rc}: {err[:200]}")
                medians.append({"handle": handle, "platform": platform, "lane": acc.get("lane", ""),
                                "posts": len(rows), "median_views": "", "max_views": "",
                                "outliers_5x": "", "median_share_pct": "", "status": f"skipped ({err[:80] or 'too few rows'})"})
                time.sleep(random.uniform(pmin, pmax))
                continue
            med = statistics.median(views)
            share_pcts = []
            n_out = 0
            for r in rows:
                r["median"] = int(med)
                r["outlier"] = round(r["views"] / med, 2) if r["views"] and med else None
                if r["shares"] is not None and r["views"]:
                    r["share_pct"] = round(100.0 * r["shares"] / r["views"], 2)
                    share_pcts.append(r["share_pct"])
                else:
                    r["share_pct"] = None
                r["lane"] = acc.get("lane", "")
                if r["outlier"] is not None and r["outlier"] >= a.min_outlier:
                    n_out += 1
            posts.extend(rows)
            medians.append({"handle": handle, "platform": platform, "lane": acc.get("lane", ""),
                            "posts": len(rows), "median_views": int(med), "max_views": max(views),
                            "outliers_5x": n_out,
                            "median_share_pct": round(statistics.median(share_pcts), 2) if share_pcts else "",
                            "status": "ok" if rc == 0 else f"partial rc={rc}"})
            log(logf, f"{i+1:02d} {handle} [{platform}] {len(rows)} posts, median {int(med):,}, max {max(views):,}, {n_out} at {a.min_outlier:g}x, {time.time()-t0:.0f}s")
            time.sleep(random.uniform(pmin, pmax))

    outliers = [p for p in posts if p.get("outlier") is not None and p["outlier"] >= a.min_outlier]
    outliers.sort(key=lambda p: -p["outlier"])
    if not a.no_enrich:
        yt = [p for p in outliers if p["platform"] == "youtube"]
        log(logf, f"enriching {len(yt)} YouTube outliers")
        for p in yt:
            enrich_youtube(p, logf)
            time.sleep(random.uniform(1.0, 2.0))

    # posts csv
    cols = ["handle", "platform", "lane", "url", "date", "views", "likes", "comments", "shares", "saves",
            "share_pct", "median", "outlier", "duration", "title"]
    pcsv = os.path.join(a.out, f"{a.date}-posts.csv")
    with open(pcsv, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for p in sorted(posts, key=lambda p: (p["handle"], p["platform"], -(p["views"] or 0))):
            w.writerow(p)

    mcsv = os.path.join(a.out, f"{a.date}-medians.csv")
    with open(mcsv, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(medians[0].keys()) if medians else ["handle"])
        w.writeheader()
        for m in medians:
            w.writerow(m)

    # outliers md
    omd = os.path.join(a.out, f"{a.date}-outliers.md")
    with open(omd, "w", encoding="utf-8") as f:
        f.write(f"# Outliers at {a.min_outlier:g}x or more, pulled {a.date}\n\n")
        f.write(f"{len(posts)} posts from {len([m for m in medians if m['status'].startswith(('ok','partial'))])} account feeds, "
                f"last {limit} posts each. Outlier score = post views / that feed's median views. "
                f"Share % = TikTok reposts / views (YouTube does not expose shares). "
                f"Instagram is not fetched; every number is from the platform in the column.\n\n")
        f.write("Format and Subtopic columns are filled by hand after watching (see WATCHLIST-README.md).\n\n")
        f.write("## Watch list medians\n\n")
        f.write("| Handle | Platform | Lane | Posts | Median views | Max views | 5x+ | Median share % | Status |\n|---|---|---|---|---|---|---|---|---|\n")
        for m in medians:
            f.write(f"| {m['handle']} | {m['platform']} | {m['lane']} | {m['posts']} | {fmt(m['median_views']) if m['median_views'] != '' else ''} | "
                    f"{fmt(m['max_views']) if m['max_views'] != '' else ''} | {m['outliers_5x']} | {m['median_share_pct']} | {m['status']} |\n")
        f.write(f"\n## The outliers ({len(outliers)})\n\n")
        f.write("| # | Outlier | Handle | Platform | Date | Views | Likes | Com | Shares | Share % | Len | Title | Format | Subtopic | URL |\n")
        f.write("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")
        for i, p in enumerate(outliers, 1):
            f.write(f"| {i} | {p['outlier']:.1f}x | {p['handle']} | {p['platform']} | {p['date']} | {fmt(p['views'])} | {fmt(p['likes'])} | "
                    f"{fmt(p['comments'])} | {fmt(p['shares'])} | {'' if p['share_pct'] is None else p['share_pct']} | "
                    f"{'' if p['duration'] is None else str(p['duration']) + ' s'} | {p['title'].replace('|', '/')} |  |  | {p['url']} |\n")
    log(logf, f"done in {time.time()-t_all:.0f}s: {len(posts)} posts, {len(outliers)} outliers -> {omd}")
    logf.close()


if __name__ == "__main__":
    main()
