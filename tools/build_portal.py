#!/usr/bin/env python
"""
build_portal.py: writes portal/data.json for the El Coyote portal (portal/index.html).

  python -I tools/build_portal.py

Reads the same sources as coyote.py and never edits them:
  playbook/13-two-a-day-30-day-plan.md       the live calendar (30 days, two talking heads a day) and ideas 101 to 166
  research/2026-11-21-MILLION-VIEW-RULE.md   the older calendar and ideas 31 to 59 (the bank)
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
                      "Every problem in order, the fix for each; each clause cuts to the thing it names and holds until the next sentence names something else. One loop, one turn, the answer last.",
                      "Hold the answer for the last ten seconds. End within 1.5 s of the payoff. No outro."]},
    "talk": {"name": "Talking head, in the truck", "length": "AM 20 to 45 s, PM 40 to 60 s", "when": "twice a day: AM 09:00 to 11:00 MT (the send episode), PM 16:00 to 19:00 MT (the hold episode)",
             "how": ["Two a day, two jobs (2026-11-23). AM is built to be sent: one joke or one list, 20 to 45 s, the turn on the last line, graded on sends per reach. PM is built to be held: the story, the trust, the check-in, 40 to 60 s, the whole message under a minute, graded on watch share and likes per reach.",
                     "One sit at 16:30 films both of tomorrow's: PM first while the voice is fresh, AM second. Three to five takes each, straight through. Bring the device the brief names (the part, the sticky note, the two parts, the phone with the comment up). Never shoot the morning of.",
                     "Same seat, same mount, Pocket 3 on the dash at eye height, 70 to 90 cm from the face, passenger window as the key, Face Auto-Detect on, engine off, windows up, DJI Mic 3 to 5 inches off. Leave the cab at least twice a week: parts room, counter after hours, the bay, the driveway, the yard. Say 'I work there' when the shop is in frame.",
                     "The sentence is the opener: voice before the picture settles, first noun by 0.9 s, the device or the lockup is the move on frame 1. Lockup 3 to 7 words with the number, upper third, gone by 3 s. Plain captions at the chest, beat words by the face (rule 118). Opener type never repeats two episodes running.",
                     "One loop in sentence one, one turn in the middle, the answer last, then the question that splits the comments. Change, not cut: the pad, the part, a turn; cut only to remove, on a breath. No outro, no ask, no grade. Look check (LOOK-GUIDE section 9) before it goes anywhere. Plan: playbook/13-two-a-day-30-day-plan.md. Format: playbook/12-talking-head-in-the-truck.md"]},
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
    "Two talking heads a day (Jacob, 2026-11-23). AM 09:00 to 11:00 is the send episode (funny or a list, 20 to 45 s, graded on sends per reach); PM 16:00 to 19:00 is the hold episode (story, trust, check-in, 40 to 60 s, graded on watch share and likes per reach). Film both of tomorrow's in one sit tonight. If a day breaks, the PM goes out and the AM is skipped, never the reverse. The plan: playbook/13-two-a-day-30-day-plan.md.",
    "Change, not cut (doctrine 2026-11-22): something the viewer cares about changes every five to eight seconds; a cut is the most expensive way to make it. One physical device per talking head, cut only to remove, on a breath. Full text: research/2026-11-22-REEL-EDITOR-DOCTRINE.md.",
    "The 10K plan (2026-11-23): two engines, the morning send post and the afternoon talking head; profile fixed before Tuesday; replies inside the hour; one peer Collab a week; Trial twins on every talking head if the toggle is there; day-30 checkpoint 1,500 to 2,500, 10K by day 90, run as if 30 were possible. Full text: research/2026-11-23-GROWTH-PLAN-10K.md. Principles, not steps: skill/el-coyote/PRINCIPLES.md.",
    "Community first. The more relatable the better. A stranger with any truck, or no truck, has to see themselves in it before the F600, the 7.3 or the shop matter. They are the backdrop and the credential, not the subject.",
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


TH_FIELDS = {"open": "Open", "turn": "Turn", "last": "Last", "device": "Device", "where": "Where", "length_note": "Length",
             "lockup": "Lockup", "splits": "Splits"}


def th_field(body: str, label: str) -> str:
    """One labelled field of a talking-head brief. Open, Turn, Last, Lockup, Caption line 1 and Splits are lines of their
    own; Device, Where and Length share one line ('Device: the part. Where: cab. Length: 45 to 60 s.')."""
    labels = "|".join(re.escape(x) for x in TH_FIELDS.values())
    m = re.search(r'(?:^|\s)' + re.escape(label) + r':\s*(.+?)(?=\s(?:' + labels + r'):\s|$)', body, re.M)
    if not m: return ""
    v = m.group(1).strip()
    return v.rstrip(".") if label in ("Device", "Where", "Length") else v


def parse_idea(i: dict) -> dict:
    body = i["body"]
    cap = re.search(r'Caption line 1:\s*"(.+?)"', body)
    frame = re.search(r'Frame 1:\s*(.+?)(?:\.\s|$)', body)
    shape = shape_of(i["cell"])
    lane = i["cell"].split(" x ")[0].replace(" check-in", "") if " x " in i["cell"] else ""
    out = {
        "n": i["n"], "cell": i["cell"], "title": i["title"], "evidence": i["evidence"], "body": body,
        "shape": shape, "length": SHAPES[shape]["length"],
        "caption_line1": cap.group(1) if cap else "",
        "frame1": (frame.group(1).strip() + ".") if frame else "",
    }
    if i["n"] >= 101:   # the two-a-day talking heads carry labelled lines
        for k, label in TH_FIELDS.items(): out[k] = th_field(body, label)
        out["lane"] = lane
        if not out["frame1"] and out["open"]: out["frame1"] = out["open"]
        out["spare"] = i["n"] >= 161
    return out


def main():
    cal = coyote.calendar()
    ideas = {n: parse_idea(i) for n, i in coyote.ideas().items()}
    # every afternoon slot is the talking head in the truck (2026-11-22), whatever cell the idea came from
    for r in cal:
        if r["slot"] == "PM" and r["idea_n"] in ideas:
            ideas[r["idea_n"]]["shape"] = "talk"; ideas[r["idea_n"]]["length"] = SHAPES["talk"]["length"]
    hooks = coyote.hook_variants()
    reads = coyote.read_tsv(coyote.READS)
    posts = coyote.read_tsv(coyote.POSTS)
    pend = coyote.read_tsv(coyote.PENDING)
    data = {
        "generated_at": dt.datetime.now(coyote.MT).isoformat(timespec="minutes"),
        "plan_name": "Two talking heads a day",
        "plan_doc": "playbook/13-two-a-day-30-day-plan.md",
        "plan_first_date": cal[0]["date"].isoformat(),
        "plan_last_date": cal[-1]["date"].isoformat(),
        "ranking_date": "2026-12-08",
        "sema_date": SEMA,
        "slots": {"AM": "09:00 to 11:00 MT", "PM": "16:00 to 19:00 MT"},
        "jobs": {"AM": {"job": "send", "length": "20 to 45 s", "grade": "sends per reach (floor 1%, goal 2), skip under 40",
                        "what": "One joke or one list a person forwards. The turn on the last line, cut on it."},
                 "PM": {"job": "hold", "length": "40 to 60 s", "grade": "watch share (floor 50%) and likes per reach (floor 4%)",
                        "what": "The story, the trust, the check-in. The whole message, under a minute."}},
        "spares": [n for n in sorted(ideas) if n >= 161],
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
