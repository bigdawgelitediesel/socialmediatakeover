#!/usr/bin/env python
"""
build_portal.py: writes portal/data.json for the El Coyote portal (portal/index.html).

  python -I tools/build_portal.py

Reads the same sources as coyote.py and never edits them:
  research/2026-11-21-MILLION-VIEW-RULE.md   the live calendar (days 1 to 15) and ideas 31 to 40
  research/2026-11-21-OUTLIER-MATRIX.md      ideas 1 to 30, hook variants A/B/C
  data/instagram/pending-reads.tsv           reads that are due
  data/instagram/reads-48h.tsv               the last graded pulls
  data/instagram/posts.tsv                   the post history

Vercel runs this as the build command (see vercel.json) and serves portal/ as a static site.
Everything in data.json is derived; edit the markdown and tsv files, not the JSON.
"""
from __future__ import annotations
import datetime as dt, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import coyote  # noqa: E402

OUT = ROOT / "portal" / "data.json"
SEMA = "2027-11-02"

SHAPES = {
    "loop": {"name": "Loop", "length": "6 to 12 s", "when": "AM 09:00 to 11:00 MT",
             "how": ["Closed loop: the last frame leads back into the first.",
                     "A joke a stranger gets: money, pride, the wife, the boss, the thing that should not run.",
                     "No talking. Your own cutout or your own footage, never a borrowed clip.",
                     "One LOUDER lockup on the hook, nothing else burned in. Sound added inside Instagram."]},
    "skit": {"name": "Skit", "length": "55 to 70 s", "when": "AM 09:00 to 11:00 MT",
             "how": ["One shot, one coworker, played straight. The turn lands on the last line and you cut on it.",
                     "A universal work situation: the backorder, the core charge, 'it just started doing that today'.",
                     "Bank five in one lunch break. Phone or Pocket 3 locked off, no music, no text.",
                     "The ask is spoken once at the end or lives in caption line 1. Never burned in."]},
    "story": {"name": "Story", "length": "60 to 120 s", "when": "PM 16:00 to 19:00 MT",
              "how": ["Sentence one is trouble a stranger understands. A number or a regret in the title.",
                      "Your face not before 20 s. Pocket 3 on a magnet mount, voice recorded after in the cab.",
                      "Every problem in order, the fix for each, cut every 2 to 4 s. Re-hook a third and two thirds in.",
                      "Hold the answer for the last ten seconds. End within 1.5 s of the payoff. No outro."]},
    "talk": {"name": "Talking head, in the truck", "length": "60 to 120 s", "when": "PM 16:00 to 19:00 MT, every day",
             "how": ["Same seat, same mount, Pocket 3 on the dash at eye height, Face Auto-Detect on, engine off, windows up, DJI Mic 3 to 5 inches off.",
                     "Never a static face on frame 1: door shuts mid-sentence, turn from the windshield on the first word, or the part comes up first. First noun by 0.9 s.",
                     "Title sentence with a number in the upper third for the first 3 s. Pilot line once around 15 s, spoken. One idea per breath, 150 to 165 wpm, say the acronyms.",
                     "Re-hook at a third and two thirds. Answer in the last ten seconds, one question that splits the comments, your fixed sign-off, cliffhanger to tomorrow. No outro, no ask.",
                     "Five takes straight through, teleprompter allowed, pick the best. Rotation: Rival, Rival, Counter, Chief, People. Full page: playbook/12-talking-head-in-the-truck.md"]},
    "question": {"name": "Question clip", "length": "9 to 25 s", "when": "AM 09:00 to 11:00 MT",
                 "how": ["A real clip from your own world with something going wrong or a hack happening.",
                         "One white pill top centre with the question. You keyed lower left reacting, or silent.",
                         "The question is the comment splitter: it has two honest answers.",
                         "Your footage or clearly credited. No shop signage."]},
}

MILLION_CHECK = [
    "Stranger test: would someone who never owned a diesel know what is at stake by second three?",
    "One universal emotion named out loud: money lost, pride, regret, the boss, the wife, the old man who had one.",
    "A number or a price in the title line.",
    "The answer held to the end. First ten seconds set the trouble, last ten carry the payoff.",
    "Length by shape: story 60 to 120 s, skit 55 to 70 s, loop 6 to 12 s. Nothing 20 to 40 s.",
    "A question that splits the comments, in the caption or the last spoken line.",
    "TikTok and Shorts the same day, same first line.",
    "Move on frame 1, first noun by 0.9 s, one lockup at most, no on-screen ask, no grade, song in-app.",
]

POST_CHECK = [
    "Caption line 1 names a person type and is the sentence a sender would type.",
    "Five hashtags max, none in line 1. No follow ask. No em-dashes.",
    "Song added inside Instagram. Upload at highest quality. No in-app trim, filter or added text.",
    "Share to your Story with the same one line. Pin a comment that repeats the person type.",
    "Post the same master to TikTok and Shorts today.",
    "Log it: python -I tools/coyote.py pending add <media_id> \"<label>\" <posted_iso>",
]

RULES = [
    "No on-screen call to action, no outro, no fade. The share line is caption line 1, written as a person type.",
    "One poster lockup on the hook (LOUDER, MEGANTE or TROPI). Nothing else burned in on the fast tier.",
    "No color grade. Real footage only. Your voice only; the Kokoro scratch voice never ships.",
    "The shop is part of the brand: Elite Diesel can appear, say \"I work there\" when it does. No customer names, plates or invoices, no vendor cost, no promises for the business. Transmission detail stays private.",
    "Two numbers never wrong: 550 to 600 crank hp. SEMA November 2 to 5, 2027. SEMA is 'the target'.",
    "No delete, coal or defeat-device content. No pods, bots, bought followers. No follow gates.",
    "Judge: views at 7 days (100,000 candidate, 1,000,000 goal). Early warning at 48 h: sends per reach over 1 percent, watch over 60 percent, skip under 45.",
]


def shape_of(cell: str) -> str:
    c = cell.lower()
    if "talking head" in c: return "talk"
    if c == "loop" or "meme" in c: return "loop"
    if "skit" in c: return "skit"
    if "question" in c: return "question"
    if "roller" in c: return "loop"
    return "story"


def parse_idea(i: dict) -> dict:
    body = i["body"]
    cap = re.search(r'Caption line 1:\s*"(.+?)"', body)
    frame = re.search(r'Frame 1:\s*(.+?)(?:\.\s|$)', body)
    shape = shape_of(i["cell"])
    return {
        "n": i["n"], "cell": i["cell"], "title": i["title"], "evidence": i["evidence"], "body": body,
        "shape": shape, "length": SHAPES[shape]["length"],
        "caption_line1": cap.group(1) if cap else "",
        "frame1": (frame.group(1).strip() + ".") if frame else "",
    }


def main():
    cal = coyote.calendar()
    ideas = {n: parse_idea(i) for n, i in coyote.ideas().items()}
    hooks = coyote.hook_variants()
    reads = coyote.read_tsv(coyote.READS)
    posts = coyote.read_tsv(coyote.POSTS)
    pend = coyote.read_tsv(coyote.PENDING)
    data = {
        "generated_at": dt.datetime.now(coyote.MT).isoformat(timespec="minutes"),
        "plan_first_date": cal[0]["date"].isoformat(),
        "plan_last_date": cal[-1]["date"].isoformat(),
        "sema_date": SEMA,
        "slots": {"AM": "09:00 to 11:00 MT", "PM": "16:00 to 19:00 MT"},
        "calendar": [{**r, "date": r["date"].isoformat()} for r in cal],
        "ideas": ideas,
        "shapes": SHAPES,
        "hooks": hooks,
        "million_checklist": MILLION_CHECK,
        "post_checklist": POST_CHECK,
        "rules": RULES,
        "pending": pend,
        "reads": reads[-40:],
        "posts": posts[:40],
    }
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}: {len(cal)} calendar rows, {len(ideas)} ideas, {len(reads)} reads, {len(posts)} posts")


if __name__ == "__main__":
    main()
