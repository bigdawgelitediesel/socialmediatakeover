#!/usr/bin/env python
"""
coyote.py: the El Coyote command center for @elcoyotediesel (data side, stdlib only).

  python -I tools/coyote.py status                       what is due today (calendar day, slots, 48 h reads, weekly tasks, inbox)
  python -I tools/coyote.py plan [--date 2026-11-23] [--week]
                                                         today's two posts from the 30-day calendar with the full idea rows
  python -I tools/coyote.py idea <N | cell words | --list>
                                                         one idea row by number, or every idea in a cell ("shop meme")
  python -I tools/coyote.py hooks <A|B|C>                the 10 pre-written hook variants for a predicted winning cell
  python -I tools/coyote.py lint hook "<text>"           hook / lockup lint (length, opener, dealbreakers, AI tells, brand)
  python -I tools/coyote.py lint caption <file|"text">   caption lint (line 1 names a person type, tells, tags, brand)
  python -I tools/coyote.py grade <insights.json> [--log] [--durations d.json]
                                                         48 h read from a saved Composio INSTAGRAM_GET_IG_USER_MEDIA response
  python -I tools/coyote.py pending [add <media_id> "<label>" <posted_iso> | done <media_id>]
                                                         the list of reels waiting for their 48 h read
  python -I tools/coyote.py week                         the Monday checklist with the exact pull call
  python -I tools/coyote.py dashboard                    writes site/command-center.html from all of the above

Sources it reads (never edits): research/2026-11-21-OUTLIER-MATRIX.md (sections 4, 5, 6),
playbook/09-measurement-protocol.md (the thresholds below), data/instagram/posts.tsv.
Files it writes: data/instagram/plan-log.tsv, data/instagram/pending-reads.tsv, data/instagram/reads-48h.tsv,
site/command-center.html.
"""
from __future__ import annotations
import argparse, csv, datetime as dt, json, os, re, sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "research" / "2026-11-21-OUTLIER-MATRIX.md"
MILLION = ROOT / "research" / "2026-11-21-MILLION-VIEW-RULE.md"   # 2026-11-21: the objective is a million views per video; its calendar and ideas 31+ win
POSTS = ROOT / "data" / "instagram" / "posts.tsv"
PLAN_LOG = ROOT / "data" / "instagram" / "plan-log.tsv"
PENDING = ROOT / "data" / "instagram" / "pending-reads.tsv"
READS = ROOT / "data" / "instagram" / "reads-48h.tsv"
SITE = ROOT / "site" / "command-center.html"
INBOX = Path(r"C:\Users\Parts\My Drive\VIDEO\inbox")
WATCHLIST = Path(r"C:\Users\Parts\OneDrive - Elite Diesel Service\Desktop\VIDEO\tools\watchlist")
YEAR = 2026
MT = dt.timezone(dt.timedelta(hours=-7))   # Mountain Standard Time (Nov to Mar)

# playbook/09-measurement-protocol.md thresholds
FLOORS = {"sends": (1.0, 2.0), "skip": (45.0, 35.0), "watch": (50.0, 60.0), "likes": (3.0, 6.0)}

# ---------------------------------------------------------------- matrix parsing
def _matrix_text() -> str:
    return MATRIX.read_text(encoding="utf-8")

def ideas() -> dict[int, dict]:
    """Section 4: **N. Cell (...): "Title"** followed by the row paragraph."""
    txt = _matrix_text()
    s = txt.index("## 4. The 30 ideas"); e = txt.index("## 5. The 30-day calendar")
    block = txt[s:e]
    if MILLION.exists():
        mt = MILLION.read_text(encoding="utf-8")
        if "### Ten new ideas" in mt:
            block += "\n" + mt[mt.index("### Ten new ideas"):mt.index("## 5. The calendar")]
    out = {}
    pat = re.compile(r'^\*\*(\d+)\. (.+?): "(.+?)"\*\*\s*\n(.*?)(?=^\*\*\d+\. |^### |^## |\Z)', re.M | re.S)
    for m in pat.finditer(block):
        n = int(m.group(1)); head = m.group(2); title = m.group(3); body = m.group(4).strip()
        cell = head.split(" (")[0].strip()
        out[n] = {"n": n, "cell": cell, "evidence": head[len(cell):].strip(" ()"), "title": title, "body": body}
    return out

def calendar() -> list[dict]:
    """Section 5 table rows: Day | Date | Slot | Idea | Cell | ... """
    txt = _matrix_text(); s = txt.index("## 5. The 30-day calendar"); e = txt.index("### The ranking rule")
    if MILLION.exists():
        mt = MILLION.read_text(encoding="utf-8")
        if "## 5. The calendar" in mt:
            txt = mt; s = txt.index("## 5. The calendar"); e = txt.index("## 6. Ranking")
    rows = []
    for line in txt[s:e].splitlines():
        if not line.startswith("|"): continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if not cells or not cells[0].isdigit(): continue
        day = int(cells[0]); date_s = cells[1]; slot = cells[2]; idea = cells[3]; cell = cells[4]
        m = re.match(r"(\d+)\s+(.*)", idea)
        n = int(m.group(1)) if m else None
        d = dt.datetime.strptime(f"{date_s} {YEAR}", "%a %b %d %Y").date()
        rows.append({"day": day, "date": d, "slot": slot, "idea_n": n, "idea": m.group(2) if m else idea, "cell": cell})
    return rows

def hook_variants() -> dict[str, dict]:
    txt = _matrix_text()
    s = txt.index("## 6. Hook variants"); e = txt.index("## 7. What to carry forward")
    block = txt[s:e]
    out = {}
    for m in re.finditer(r"^### ([ABC])\. (.+?)\n(.*?)(?=^### |\Z)", block, re.M | re.S):
        items = re.findall(r"^\d+\. (.+)$", m.group(3), re.M)
        out[m.group(1)] = {"cell": m.group(2), "hooks": items}
    return out

# ---------------------------------------------------------------- tsv helpers
def read_tsv(p: Path) -> list[dict]:
    if not p.exists(): return []
    with p.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))

def write_tsv(p: Path, rows: list[dict], cols: list[str]):
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, delimiter="\t", extrasaction="ignore")
        w.writeheader(); w.writerows(rows)

PENDING_COLS = ["media_id", "label", "posted_iso", "due_iso", "status"]
PLAN_COLS = ["day", "date", "slot", "idea_n", "media_id", "reach_48h", "sends", "sends_per_reach_pct", "skip_pct", "saves_per_reach_pct", "note"]
READ_COLS = ["read_at", "media_id", "label", "posted", "age_h", "views", "reach", "likes", "comments", "shares", "saves", "sends_per_reach_pct", "likes_per_reach_pct", "saves_per_reach_pct", "skip_pct", "avg_watch_s", "watch_pct", "grade", "tier", "verdict"]

# ---------------------------------------------------------------- commands
def today(args) -> dt.date:
    return dt.date.fromisoformat(args.date) if getattr(args, "date", None) else dt.datetime.now(MT).date()

def cmd_plan(args):
    cal = calendar(); ids = ideas(); log = {(r["day"], r["slot"]): r for r in read_tsv(PLAN_LOG)}
    d0 = today(args)
    days = [d0 + dt.timedelta(days=i) for i in range(7)] if args.week else [d0]
    first = cal[0]["date"]; last = cal[-1]["date"]
    for d in days:
        rows = [r for r in cal if r["date"] == d]
        if not rows:
            if d < first: print(f"{d}: before day 1 ({first}). Shoot and bank: skits 10, 4, 16, 22, 28 in one lunch break; memes 9, 3, 15, 21, 27 in one cutout session."); continue
            n = (d - first).days + 1
            print(f"{d}: day {n} of the plan, winners-only stretch (days 16 to 30). Morning = the send cell, afternoon = the build cell, a NEW hook each (coyote.py hooks A|B|C). Rank first with the day-15 rule in section 5 of the matrix.")
            continue
        print(f"\n=== {d:%a %b %d} · day {rows[0]['day']} of 30 ===")
        for r in rows:
            win = "09:00 to 11:00 MT" if r["slot"] == "AM" else "16:00 to 19:00 MT"
            print(f"\n[{r['slot']} {win}]  idea {r['idea_n']}  ·  {r['cell']}")
            idea = ids.get(r["idea_n"])
            if idea:
                print(f'  "{idea["title"]}"')
                if args.full or not args.week:
                    for para in idea["body"].split("\n"):
                        if para.strip(): print("  " + para.strip())
            lg = log.get((r["day"], r["slot"]))
            if lg and lg.get("media_id"):
                print(f"  LOGGED: media {lg['media_id']} reach {lg['reach_48h']} sends/reach {lg['sends_per_reach_pct']}% skip {lg['skip_pct']}%")
    print("\nEvery post is built for a million (research/2026-11-21-MILLION-VIEW-RULE.md section 3): stranger test, one universal emotion, a number in the title, the answer held to the end, story 60 to 120 s / skit 55 to 70 s / loop 6 to 12 s, a question that splits the comments, TikTok and Shorts the same day. Craft rules unchanged: one lockup at most, no on-screen ask, caption line 1 names a person type, song in-app, 48 h and 7-day reads logged.")

def cmd_idea(args):
    ids = ideas()
    if args.list:
        for n, i in ids.items(): print(f'{n:>2}. {i["cell"]:<34} "{i["title"]}"')
        return
    q = " ".join(args.query).strip().lower()
    if q.isdigit():
        i = ids.get(int(q))
        if not i: sys.exit("no such idea")
        print(f'{i["n"]}. {i["cell"]} ({i["evidence"]}): "{i["title"]}"\n{i["body"]}')
        return
    words = [w for w in re.split(r"\W+", q) if w]
    hits = [i for i in ids.values() if all(w in i["cell"].lower() for w in words)]
    for i in hits: print(f'{i["n"]}. {i["cell"]}: "{i["title"]}"\n{i["body"]}\n')
    if not hits: print("no idea matches; try: coyote.py idea --list")

def cmd_hooks(args):
    hv = hook_variants()
    k = args.cell.upper()
    if k not in hv: sys.exit("use A (Shop x Meme), B (Shop x Skit) or C (Numbers x Named-tribe news)")
    print(f"{k}. {hv[k]['cell']}")
    used = {r.get("note", "") for r in read_tsv(PLAN_LOG)}
    for i, h in enumerate(hv[k]["hooks"], 1):
        flag = "  (used)" if any(f"hook {k}{i}" in u for u in used) else ""
        print(f"{i:>2}. {h}{flag}")

# ---------------------------------------------------------------- lint
STOCK = ["say goodbye to", "reimagined", "unlock the power", "take it to the next level", "here's the thing", "game-changer", "game changer",
         "delve", "tapestry", "testament to", "leverage", "supercharge", "elevate your", "journey", "seamless", "empower", "read that again",
         "let that sink in", "agree?", "thoughts?", "stop scrolling", "wait for it", "you won't believe", "in this video", "welcome back"]
OPENERS = ["hey guys", "hey everyone", "what's up guys", "so today", "today we", "today i", "in this video", "welcome", "hi guys", "yo guys", "alright guys", "okay so"]
CTA = ["follow for", "follow me", "hit follow", "like and", "link in bio", "subscribe", "comment below", "drop a", "tap the", "share this", "double tap", "turn on notifications"]
BRAND_NEVER = [("elite diesel", "shop name on Rival content"), ("307", "shop brand on Rival content (if this is the shop number, fine; if the shop, no)"),
               ("delete", "delete content is banned"), ("rolling coal", "coal content is banned"), ("roll coal", "coal content is banned"),
               ("defeat device", "defeat-device content is banned"), ("cp3 conversion", "he disabled the CP4 and runs a FASS; no CP3/DCR story"), ("dcr", "no CP3/DCR story")]
PRIVATE = [("transmission", "trans builder/pricing stays off public; 'built' is the most you say"), ("4r100", "trans detail is private"), ("e4od", "trans detail is private"), ("torque converter", "trans detail is private")]
PERSON = [r"\bsend (this|it) to\b", r"\bfor (the|whoever|everyone|anyone|every)\b", r"\btag (the|your|a)\b", r"\bto the (guy|one|owner|tech|kid|man)\b",
          r"\b(7\.3|6\.7|obs|cummins|powerstroke|duramax|f-?600|f-?250|f-?350|parts) (guys|owners|people|crowd)\b", r"\bguys,", r"\bowner-?ops?\b", r"\bbrother\b", r"\bdad\b", r"\bcoworker\b", r"\bbuddy\b"]

def _tells(text: str) -> list[str]:
    t = text; low = t.lower(); out = []
    if "—" in t or "–" in t: out.append("em/en dash (use a period or comma)")
    if re.search(r"\b(it'?s|this is|that'?s) not .{2,40}?,? (it'?s|this is|that'?s)\b", low): out.append('contrast reveal "it\'s not X, it\'s Y"')
    if re.search(r"\bno \w+(,| and) no \w+(,| and) no \w+", low): out.append("negation list (no X, no Y, no Z)")
    if re.search(r"\b(the (result|catch|best part|fix|problem|answer))\s*[?:]", low): out.append("self-answered question / colon reveal")
    if re.search(r"(^|\n)\s*[\U0001F300-\U0001FAFF✅🚀💡]", t): out.append("emoji bullets")
    for s in STOCK:
        if s in low: out.append(f'stock phrase "{s}"')
    lines = [l for l in t.splitlines() if l.strip()]
    if len(lines) >= 6 and all(len(l.split()) <= 7 for l in lines): out.append("broetry (every line one short sentence)")
    return out

def _brand(text: str) -> list[str]:
    low = text.lower(); out = []
    for k, why in BRAND_NEVER:
        if re.search(rf"\b{re.escape(k)}\b", low): out.append(f'"{k}": {why}')
    for k, why in PRIVATE:
        if k in low: out.append(f'"{k}": {why}')
    if re.search(r"sema", low) and re.search(r"\b(2026|2028)\b", low): out.append("SEMA year wrong: the target is November 2 to 5, 2027")
    m = re.search(r"\b(\d{3,4})\s*(crank\s*)?hp\b", low)
    if m and not (500 <= int(m.group(1)) <= 650) and "6.7" not in low: out.append(f"{m.group(1)} hp: the Rival 7.3 target is 550 to 600 crank")
    return out

def lint_hook(text: str) -> tuple[int, list[str]]:
    notes = []; score = 100
    words = re.findall(r"[\w'’.]+", text)
    n = len(words)
    if n > 12: notes.append(f"{n} words: a hook is under 12 (a lockup 3 to 7)"); score -= 25
    elif n > 7: notes.append(f"{n} words: fine spoken, too long as a burned-in lockup (3 to 7)"); score -= 5
    low = text.lower().strip()
    for o in OPENERS:
        if low.startswith(o): notes.append(f'opens with "{o}": first noun must land by 0.9 s'); score -= 40; break
    if not re.search(r"\d|7\.3|6\.7|f600|f-600|'59|1959|sema|cummins|powerstroke|obs|frame|turbo|hp|miles|\$", low):
        notes.append("no concrete noun or number in the hook (specificity)"); score -= 15
    for c in CTA:
        if c in low: notes.append(f'ask inside the hook ("{c}"): asks live in caption line 1, never burned in'); score -= 30
    if "#" in text: notes.append("hashtag in a hook"); score -= 20
    if re.search(r"[\U0001F300-\U0001FAFF]", text): notes.append("emoji in a hook"); score -= 10
    for t in _tells(text): notes.append("AI tell: " + t); score -= 15
    for b in _brand(text): notes.append("brand: " + b); score -= 30
    if re.search(r"\b(you|your|guys)\b", low) or re.search(r"\b(7\.3|obs|cummins|owner)", low): pass
    else: notes.append("nobody is addressed: name the tribe or the viewer's person (sends rule)"); score -= 5
    return max(0, score), notes

def lint_caption(text: str) -> tuple[int, list[str]]:
    notes = []; score = 100
    lines = [l for l in text.strip().splitlines() if l.strip()]
    if not lines: return 0, ["empty"]
    l1 = lines[0].lower()
    if not any(re.search(p, l1) for p in PERSON):
        notes.append('line 1 does not name a person type ("Send this to your 7.3 brother", "For whoever is pulling a cab this weekend")'); score -= 35
    tags = re.findall(r"#\w+", text)
    if len(tags) > 5: notes.append(f"{len(tags)} hashtags: Instagram caps at 5 (Dec 2025)"); score -= 20
    if tags and len(lines) > 1 and "#" in lines[0]: notes.append("hashtags in line 1: keep line 1 for the person type"); score -= 10
    for c in ["follow for more", "follow me", "hit follow", "like and share", "link in bio", "subscribe"]:
        if c in text.lower(): notes.append(f'"{c}": no follow asks; a comment gate with a real deliverable is the only ask allowed, one post in four'); score -= 25
    if re.search(r"\bcomment\s+[\"“]?\w+[\"”]?\b", text.lower()):
        notes.append("comment gate present: confirm a real deliverable exists and this is not more than one post in four"); score -= 0
    for t in _tells(text): notes.append("AI tell: " + t); score -= 15
    for b in _brand(text): notes.append("brand: " + b); score -= 30
    if len(text) > 600: notes.append(f"{len(text)} characters: long captions are fine only when line 1 already did the job"); score -= 5
    return max(0, score), notes

def cmd_lint(args):
    text = " ".join(args.text)
    p = Path(text)
    if p.exists() and p.is_file(): text = p.read_text(encoding="utf-8")
    score, notes = (lint_hook if args.kind == "hook" else lint_caption)(text)
    verdict = "SHIP" if score >= 85 else "FIX" if score >= 60 else "REWRITE"
    print(f"{args.kind.upper()} {score}/100 {verdict}")
    for n in notes: print(" - " + n)
    if not notes: print(" - clean")

# ---------------------------------------------------------------- grade (48 h read)
def _posts_from_json(obj) -> list[dict]:
    """Accepts the raw Composio response, {data:[...]}, a list of posts, or {"results": {...}} wrappers."""
    if isinstance(obj, list): return obj
    if isinstance(obj, dict):
        for k in ("data", "posts", "items"):
            if isinstance(obj.get(k), list): return obj[k]
        for k in ("response_data", "data", "result", "results"):
            if isinstance(obj.get(k), dict):
                r = _posts_from_json(obj[k])
                if r: return r
        if "id" in obj and "timestamp" in obj: return [obj]
    return []

def _metrics(post: dict) -> dict:
    m = {}
    ins = post.get("insights")
    if isinstance(ins, dict): ins = ins.get("data", [])
    for d in ins or []:
        vals = d.get("values") or [{}]
        m[d.get("name")] = vals[0].get("value")
    for k in ("like_count", "comments_count"): m[k] = post.get(k)
    return m

def grade_post(post: dict, durations: dict, now: dt.datetime) -> dict:
    m = _metrics(post)
    reach = m.get("reach") or 0; shares = m.get("shares") or 0; saves = m.get("saved") or 0
    likes = m.get("like_count") or 0; comments = m.get("comments_count") or 0; views = m.get("views") or 0
    skip = m.get("reels_skip_rate"); watch_ms = m.get("ig_reels_avg_watch_time")
    ts = post.get("timestamp", "")
    try: posted = dt.datetime.fromisoformat(ts.replace("+0000", "+00:00"))
    except Exception: posted = None
    age_h = round((now - posted).total_seconds() / 3600, 1) if posted else None
    spr = round(100 * shares / reach, 2) if reach else None
    lpr = round(100 * likes / reach, 2) if reach else None
    svr = round(100 * saves / reach, 2) if reach else None
    dur = durations.get(post.get("id")) or durations.get(post.get("permalink", ""))
    watch_s = round(watch_ms / 1000, 1) if watch_ms else None
    watch_pct = round(100 * watch_s / dur, 0) if (watch_s and dur) else None
    verdicts = []; grade = "no read"
    tier = "MILLION" if views >= 1_000_000 else "CANDIDATE" if views >= 100_000 else "building" if views >= 10_000 else "-"
    if reach and reach < 500: verdicts.append("under 500 reach: no read, does not rank")
    elif reach:
        if spr is not None:
            if spr >= FLOORS["sends"][1]: grade = "GOAL"
            elif spr >= FLOORS["sends"][0]: grade = "FLOOR"
            else: grade = "MISS"; verdicts.append("sends under 1%: the format failed (who it is for), change the person type and caption line 1, not the footage")
        if skip is not None and skip > FLOORS["skip"][0]: verdicts.append(f"skip {skip:.0f}%: first 2 s opened on a product or a thank-you; open on a person or a move")
        if watch_pct is not None and watch_pct < FLOORS["watch"][0]: verdicts.append(f"watch {watch_pct:.0f}%: second promise missing, re-hook at 9 to 10 s or cut length")
        if lpr is not None and lpr < FLOORS["likes"][0] and (spr or 0) < 1: verdicts.append("likes and sends both low: vanilla")
        if svr and spr is not None and svr > spr: verdicts.append("saves above sends: education; wrap the tip in a tribe or argument frame")
        if comments and likes and comments > likes: verdicts.append("comments above likes: gated or argument reel, read it as that lane")
    if age_h is not None and age_h < 44: verdicts.insert(0, f"only {age_h} h old: early read, re-pull at 48 h")
    cap = (post.get("caption") or "").strip().replace("\n", " ")
    return {"read_at": now.isoformat(timespec="minutes"), "media_id": post.get("id"), "label": cap[:60], "posted": ts, "age_h": age_h,
            "views": views, "reach": reach, "likes": likes, "comments": comments, "shares": shares, "saves": saves,
            "sends_per_reach_pct": spr, "likes_per_reach_pct": lpr, "saves_per_reach_pct": svr, "skip_pct": skip,
            "avg_watch_s": watch_s, "watch_pct": watch_pct, "grade": grade, "tier": tier, "verdict": "; ".join(verdicts), "permalink": post.get("permalink", ""),
            "media_product_type": post.get("media_product_type", "")}

def cmd_grade(args):
    obj = json.loads(Path(args.file).read_text(encoding="utf-8"))
    posts = _posts_from_json(obj)
    if not posts: sys.exit("no posts found in that JSON (expected the INSTAGRAM_GET_IG_USER_MEDIA response with nested insights)")
    durations = json.loads(Path(args.durations).read_text(encoding="utf-8")) if args.durations else {}
    now = dt.datetime.now(dt.timezone.utc)
    rows = [grade_post(p, durations, now) for p in posts]
    rows = [r for r in rows if (r["media_product_type"] or "REELS") == "REELS"] or rows
    print(f"{'posted':<16} {'age':>5} {'views':>9} {'tier':<9} {'reach':>7} {'sends':>5} {'s/r%':>5} {'skip':>5} {'watch':>5} {'48h':<6} caption")
    for r in rows:
        print(f"{(r['posted'] or '')[:16]:<16} {str(r['age_h'] or ''):>5} {r['views']:>9,} {r['tier']:<9} {r['reach']:>7} {r['shares']:>5} {str(r['sends_per_reach_pct'] or ''):>5} {str(r['skip_pct'] or '')[:5]:>5} {str(r['watch_pct'] or '')[:5]:>5} {r['grade']:<6} {r['label'][:44]}")
        if r["verdict"] and args.verbose: print(f"{'':>16} -> {r['verdict']}")
    byv = sorted(rows, key=lambda r: -(r["views"] or 0))
    print("\nRanked by views (goal 1,000,000; 100,000 is a candidate):")
    for r in byv[:5]: print(f"  {r['views']:>9,}  {r['tier']:<9} sends/reach {str(r['sends_per_reach_pct'] or '-'):>5}%  watch {str(r['watch_pct'] or '-'):>4}%  {r['label'][:50]}")
    good = [r for r in rows if r["reach"] and r["reach"] >= 500 and r["sends_per_reach_pct"] is not None]
    if good:
        good.sort(key=lambda r: (-(r["sends_per_reach_pct"] or 0), r["skip_pct"] or 99))
        print("\nEarly warning at 48 h, sends per reach (reach 500+):")
        for r in good[:5]: print(f"  {r['sends_per_reach_pct']:>5}%  skip {str(r['skip_pct'])[:4]:>4}  {r['label'][:60]}")
    if args.log:
        old = read_tsv(READS); old += rows; write_tsv(READS, old, READ_COLS)
        pend = read_tsv(PENDING)
        ages = {r["media_id"]: (r["age_h"] or 0) for r in rows}
        for p in pend:
            a = ages.get(p["media_id"])
            if a is None: continue
            if "7-day" in p["label"] and a >= 164: p["status"] = "read"
            elif "7-day" not in p["label"] and a >= 44: p["status"] = "read"
        write_tsv(PENDING, pend, PENDING_COLS)
        # posts.tsv: add rows that are not there yet
        posts_rows = read_tsv(POSTS); have = {p["media_id"] for p in posts_rows}
        cols = list(posts_rows[0].keys()) if posts_rows else ["media_id", "timestamp_utc", "format", "views", "reach", "likes", "comments", "shares", "saves", "interactions", "avg_watch_ms", "caption_summary", "skip_rate_pct"]
        added = 0
        for r, p in zip(rows, posts):
            if r["media_id"] in have: continue
            m = _metrics(p)
            posts_rows.append({"media_id": r["media_id"], "timestamp_utc": (r["posted"] or "")[:19], "format": p.get("media_product_type") or p.get("media_type", ""),
                               "views": r["views"], "reach": r["reach"], "likes": r["likes"], "comments": r["comments"], "shares": r["shares"], "saves": r["saves"],
                               "interactions": m.get("total_interactions") or "", "avg_watch_ms": m.get("ig_reels_avg_watch_time") or 0,
                               "caption_summary": r["label"], "skip_rate_pct": r["skip_pct"] if r["skip_pct"] is not None else ""})
            added += 1
        posts_rows.sort(key=lambda x: x.get("timestamp_utc", ""), reverse=True)
        write_tsv(POSTS, posts_rows, cols)
        print(f"\nlogged {len(rows)} reads to {READS.relative_to(ROOT)}, {added} new rows in posts.tsv, pending list updated")

# ---------------------------------------------------------------- pending
def cmd_pending(args):
    pend = read_tsv(PENDING)
    if args.action == "add":
        posted = dt.datetime.fromisoformat(args.posted)
        due = posted + dt.timedelta(hours=48)
        pend.append({"media_id": args.media_id, "label": args.label, "posted_iso": posted.isoformat(timespec="minutes"), "due_iso": due.isoformat(timespec="minutes"), "status": "due"})
        pend.append({"media_id": args.media_id, "label": args.label + " (7-day views read)", "posted_iso": posted.isoformat(timespec="minutes"), "due_iso": (posted + dt.timedelta(days=7)).isoformat(timespec="minutes"), "status": "due"})
        write_tsv(PENDING, pend, PENDING_COLS); print("added")
    elif args.action == "done":
        for p in pend:
            if p["media_id"] == args.media_id: p["status"] = "read"
        write_tsv(PENDING, pend, PENDING_COLS); print("marked read")
    now = dt.datetime.now(MT)
    for p in pend:
        if p["status"] != "due": continue
        due = dt.datetime.fromisoformat(p["due_iso"])
        if due.tzinfo is None: due = due.replace(tzinfo=MT)
        state = "READ NOW" if now >= due else f"due {due:%a %b %d %H:%M} MT"
        print(f"  {p['media_id']:<20} {p['label'][:40]:<40} {state}")
    if not any(p["status"] == "due" for p in pend): print("  nothing waiting for a 48 h read")

# ---------------------------------------------------------------- status / week
def cmd_week(args):
    print("""MONDAY READ (playbook/09-measurement-protocol.md)
1. Pull the last 20 posts, one call, then `coyote.py grade <saved.json> --log`:
   INSTAGRAM_GET_IG_USER_MEDIA  ig_user_id "me", limit 20,
   fields "id,caption,media_type,media_product_type,permalink,timestamp,like_count,comments_count,insights.metric(views,reach,saved,shares,total_interactions,ig_reels_avg_watch_time,reels_skip_rate)"
   (never request reposts or profile_visits on reels; connection instagram_metic-mutule)
2. Account: followers, 30-day reach, profile visits per 1,000 reach, follows per 1,000 reach (INSTAGRAM_GET_USER_INSIGHTS period=day, 30-day windows; follows_and_unfollows breakdown=follow_type).
3. Top 3 and bottom 3 reels of the week by sends per reach, one sentence each on why.
4. Trending audio: Professional dashboard Trending audio, then Ignix weekly list, then CreatorDB (research/2026-11-21-audio-trends-and-voice.md).
5. THE BAR weekly re-pull (research/reel-references/2026-11-21-the-bar-weekly/WEEKLY.md).
6. Outlier watch list: `python -I "<VIDEO>/tools/outlier_watchlist.py"` (about 10 minutes), file the new outliers into the matrix cells.
7. Trial Reels: if the composer shows the toggle, every build reel goes out as a Trial with two caption first lines.
8. Partners: who got a Story thank-you, who owes a reply (Strictly Diesel), what is due at SEMA pitch stage.""")

def _inbox():
    if not INBOX.exists(): return [], []
    raw, done = [], []
    for p in INBOX.iterdir():
        if p.is_dir() and "completed" in p.name.lower(): done.append(p.name)
        elif p.suffix.lower() in (".mov", ".mp4", ".m4v"): raw.append((p.name, dt.datetime.fromtimestamp(p.stat().st_mtime)))
    raw.sort(key=lambda x: x[1], reverse=True)
    return raw, sorted(done)

def cmd_status(args):
    now = dt.datetime.now(MT); d = now.date()
    cal = calendar(); first = cal[0]["date"]
    dayn = (d - first).days + 1
    print(f"El Coyote status · {now:%a %b %d %H:%M} MT")
    if dayn < 1: print(f"  30-day plan starts {first:%a %b %d} (in {1 - dayn} days). Bank the skits and memes now.")
    elif dayn <= 15: print(f"  Day {dayn} of 30 (built for a million: story PM, skit or loop AM). Day 15 ranking by 7-day views on Sun Dec 7.")
    elif dayn <= 30: print(f"  Day {dayn} of 30 (winners-only phase).")
    else: print("  The 30-day plan is over; rank, keep the winning cells, write the next matrix.")
    rows = [r for r in cal if r["date"] == d]
    for r in rows:
        print(f"  {r['slot']}  idea {r['idea_n']} {r['idea']}  ·  {r['cell']}" + ("  (post 09:00 to 11:00)" if r["slot"] == "AM" else "  (post 16:00 to 19:00)"))
    print("\n48 h reads:")
    cmd_pending(argparse.Namespace(action=None))
    posts = read_tsv(POSTS)
    if posts: print(f"\nposts.tsv: {len(posts)} rows, newest {posts[0].get('timestamp_utc','')[:10]}")
    if WATCHLIST.exists():
        newest = max((p.stat().st_mtime for p in WATCHLIST.iterdir()), default=0)
        age = (dt.datetime.now().timestamp() - newest) / 86400
        print(f"outlier watch list: last run {age:.1f} days ago" + ("  (RE-RUN, weekly)" if age > 7 else ""))
    if now.weekday() == 0: print("Monday: run `coyote.py week`.")
    raw, done = _inbox()
    print(f"\nDrive inbox: {len(raw)} raw clips, {len(done)} completed folders")
    for n, t in raw[:6]: print(f"  {t:%m-%d %H:%M}  {n}")
    for n in done[-3:]: print(f"  done: {n}")
    print("\nAlways before cutting: pull the last 12 posts (he posts 2 to 4 a day).")

# ---------------------------------------------------------------- dashboard
def cmd_dashboard(args):
    import html, io
    buf = io.StringIO(); real = sys.stdout; sys.stdout = buf
    try:
        cmd_status(argparse.Namespace()); st = buf.getvalue(); buf.seek(0); buf.truncate()
        cmd_plan(argparse.Namespace(date=None, week=True, full=False)); pl = buf.getvalue(); buf.seek(0); buf.truncate()
        cmd_week(argparse.Namespace()); wk = buf.getvalue()
    finally:
        sys.stdout = real
    reads = read_tsv(READS)[-20:]
    tbl = "".join(f"<tr><td>{html.escape(str(r['posted'])[:10])}</td><td>{html.escape(r['label'][:50])}</td><td>{r['reach']}</td><td>{r['sends_per_reach_pct']}</td><td>{r['skip_pct']}</td><td>{r['grade']}</td></tr>" for r in reversed(reads))
    rules = """<li>No on-screen call to action, no outro, no fade. The share line is caption line 1, written as a person type.</li>
<li>One poster lockup on the hook (LOUDER / MEGANTE / TROPI), nothing else burned in on the fast tier. No color grade. Song added inside Instagram.</li>
<li>Move on frame 1, first noun by 0.9 s, first payoff by 4 to 5 s, end within 1.5 s of the payoff.</li>
<li>Grade = sends per reach at 48 h: floor 1%, goal 2%. Skip under 45%. One variable per post.</li>
<li>El Coyote only on Rival content. Transmission detail private. No delete, coal or defeat-device content. No AI imagery, no shipped synthetic voice.</li>
<li>Comment gates only with a real deliverable, at most one post in four, never a follow gate. Five hashtags max.</li>
<li>Two numbers never wrong: 550 to 600 crank hp, SEMA November 2 to 5, 2027.</li>"""
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>El Coyote command center</title>
<style>
:root{{--bg:#0b0b0c;--ink:#efe9dc;--tan:#c9b38c;--ox:#7a1f1f;--hi:#e2543e;--card:#141414}}
body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.5 Poppins,system-ui,sans-serif;padding:24px 16px}}
h1{{font-family:Anton,Impact,sans-serif;font-weight:400;letter-spacing:1px;font-size:40px;margin:0 0 4px}} h1 span{{color:var(--tan)}}
.sub{{color:var(--tan);margin-bottom:24px}} .grid{{display:grid;gap:18px;grid-template-columns:repeat(auto-fit,minmax(340px,1fr))}}
.card{{background:var(--card);border:1px solid #26262a;border-radius:16px;padding:18px 20px}} .card h2{{margin:0 0 10px;font-size:14px;letter-spacing:3px;text-transform:uppercase;color:var(--tan)}}
pre{{white-space:pre-wrap;font:13px/1.45 Consolas,monospace;color:#d8d2c4;margin:0}} table{{width:100%;border-collapse:collapse;font-size:13px}} td,th{{padding:5px 6px;border-bottom:1px solid #2a2a2e;text-align:left}} th{{color:var(--tan);font-weight:600}}
ul{{margin:0;padding-left:18px}} li{{margin:4px 0}} .tag{{display:inline-block;background:var(--ox);color:#fff;border-radius:8px;padding:2px 10px;font-size:12px;margin-left:8px}}
</style></head><body>
<h1>EL COYOTE <span>command center</span></h1>
<div class="sub">@elcoyotediesel · Project Rival · generated {dt.datetime.now(MT):%a %b %d %Y %H:%M} MT by tools/coyote.py dashboard</div>
<div class="grid">
<div class="card"><h2>Status</h2><pre>{html.escape(st)}</pre></div>
<div class="card"><h2>House rules</h2><ul>{rules}</ul></div>
<div class="card" style="grid-column:1/-1"><h2>This week's plan</h2><pre>{html.escape(pl)}</pre></div>
<div class="card"><h2>Last 48 h reads</h2><table><tr><th>posted</th><th>reel</th><th>reach</th><th>sends/reach %</th><th>skip %</th><th>grade</th></tr>{tbl or '<tr><td colspan=6>none logged yet: coyote.py grade &lt;json&gt; --log</td></tr>'}</table></div>
<div class="card"><h2>Monday read</h2><pre>{html.escape(wk)}</pre></div>
</div></body></html>"""
    SITE.parent.mkdir(exist_ok=True); SITE.write_text(page, encoding="utf-8")
    print(f"wrote {SITE}")

# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("status"); s.set_defaults(fn=cmd_status)
    s = sub.add_parser("plan"); s.add_argument("--date"); s.add_argument("--week", action="store_true"); s.add_argument("--full", action="store_true"); s.set_defaults(fn=cmd_plan)
    s = sub.add_parser("idea"); s.add_argument("query", nargs="*"); s.add_argument("--list", action="store_true"); s.set_defaults(fn=cmd_idea)
    s = sub.add_parser("hooks"); s.add_argument("cell"); s.set_defaults(fn=cmd_hooks)
    s = sub.add_parser("lint"); s.add_argument("kind", choices=["hook", "caption"]); s.add_argument("text", nargs="+"); s.set_defaults(fn=cmd_lint)
    s = sub.add_parser("grade"); s.add_argument("file"); s.add_argument("--log", action="store_true"); s.add_argument("--durations"); s.add_argument("-v", "--verbose", action="store_true", default=True); s.set_defaults(fn=cmd_grade)
    s = sub.add_parser("pending"); s.add_argument("action", nargs="?", choices=["add", "done"]); s.add_argument("media_id", nargs="?"); s.add_argument("label", nargs="?"); s.add_argument("posted", nargs="?"); s.set_defaults(fn=cmd_pending)
    s = sub.add_parser("week"); s.set_defaults(fn=cmd_week)
    s = sub.add_parser("dashboard"); s.set_defaults(fn=cmd_dashboard)
    a = ap.parse_args(); a.fn(a)

if __name__ == "__main__":
    main()
