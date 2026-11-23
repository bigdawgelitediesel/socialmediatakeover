#!/usr/bin/env python3
"""
streamline.py: the El Coyote streamline editor (2026-11-23).

Thinking, not steps. It plans a cut from word timings, challenges its own plan against the doctrine
and against the last episodes so nothing looks the same, renders, and lints the result.

  python -I tools/streamline.py plan      --words words.json --src IN.MOV --job talk [--open-on TEXT] [--end-on TEXT] [--drop TEXT ...] -o plan.json
  python -I tools/streamline.py challenge plan.json [--set "Chief cab"] [--device pad] [--tone relatable]
  python -I tools/streamline.py render    plan.json --lockup "find the gratitude" -o post.mp4 [--no-captions] [--fonts research/fonts]
  python -I tools/streamline.py lint      plan.json [--video post.mp4] [--ass post.ass]
  python -I tools/streamline.py ledger    add plan.json --label "..." [--set ...] [--device ...] [--tone ...]
  python -I tools/streamline.py ledger    show

Doctrine: research/2026-11-22-REEL-EDITOR-DOCTRINE.md. Jobs and length bands come from section 10.
Cut points are breaths (gaps between words), never clocks. Captions never sit under the lockup.
"""
from __future__ import annotations
import argparse, csv, datetime as dt, json, os, re, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "data" / "edits" / "ledger.tsv"
FONTS = ROOT / "research" / "fonts"

JOBS = {  # doctrine section 10
    "loop": (6, 20), "skit": (45, 70), "talk": (40, 60), "talk-long": (60, 120), "story": (60, 120),
}
BREATH = 0.45        # a gap this long is a legal cut point
SENTENCE = 0.90      # a gap this long ends a sentence
FILLER = {"um", "uh", "like", "literally", "basically", "honestly", "kinda", "sorta"}
FILLER_PHRASES = ["you know", "kind of", "sort of", "i mean", "i wanted to make a post", "i don't know i just",
                  "so today", "hey guys", "what's up guys", "welcome back"]
STAKES = {"money", "dollar", "dollars", "paid", "pay", "cost", "costs", "broke", "bill", "hours", "saturday", "weekend",
          "wife", "kid", "kids", "boss", "job", "shop", "cold", "pride", "stressful", "stress", "hard", "failed", "fail",
          "wrong", "mistake", "truck", "trucks", "family", "friend", "friends", "blessing", "grateful", "tired", "late", "overtime"}
STOP = {"the", "a", "an", "and", "or", "to", "of", "in", "on", "with", "for", "at", "but", "that", "like", "is", "are",
        "was", "were", "be", "been", "this", "my", "your", "it", "i", "i'm", "you", "just", "so", "we", "he", "she",
        "they", "them", "me", "us", "our", "his", "her", "its", "if", "as", "than", "then", "there", "here", "when",
        "what", "which", "who", "how", "why", "not", "no", "do", "does", "did", "have", "has", "had", "can", "could",
        "would", "should", "will", "really", "very", "also", "even", "still", "about", "into", "out", "up", "down",
        "all", "some", "any", "lot", "one", "get", "got", "go", "going", "come", "coming", "make", "made", "want",
        "wanted", "know", "think", "thought", "say", "said", "feel", "feels", "felt", "being", "am", "because",
        "right", "good", "best", "big", "little", "new", "old", "long", "such", "much", "many", "more", "most", "other", "own",
        "same", "different", "next", "last", "first", "whole", "every", "each"}
PRONOUN_OPEN = {"you", "your", "you're", "yours"}
BAD_OPENERS = ["so ", "hey", "today", "one of the", "i wanted", "welcome", "what's up", "okay so", "alright"]

OPENER_TYPES = ["you-line", "number", "cold-line", "sound-first", "prop-first", "question-to-self"]
SETS = ["Chief cab", "F600 bay", "counter after close", "parts room", "porch", "walking the bay", "Class 8 cab"]
DEVICES = ["pad", "part in hand", "phone with the comment", "card", "none"]
LOCKUPS = ["name-call", "number claim", "flat contrarian"]
TONES = ["relatable", "trust", "funny", "grievance held lightly", "gratitude", "curiosity"]
CAMERAS = ["dash locked", "ActiveTrack headrest", "handheld walk", "top-down pad", "passenger angle"]
PAYOFFS = ["a number", "a rule", "a question", "open loop to a named episode", "a callback"]
FORMATS = ["talking head", "story over footage", "one-take walk", "Q&A from comments", "honest check-in"]


# ---------- words, sentences, scoring ----------
def load_words(path):
    raw = json.load(open(path, encoding="utf-8"))
    out = []
    for w in raw:
        txt = (w.get("w") or w.get("word") or w.get("text") or "").strip()
        s = w.get("s", w.get("start")); e = w.get("e", w.get("end"))
        if txt and s is not None and e is not None:
            out.append({"w": txt, "s": float(s), "e": float(e)})
    return out


def sentences(words):
    sents, cur = [], []
    for i, w in enumerate(words):
        cur.append(w)
        gap = words[i + 1]["s"] - w["e"] if i + 1 < len(words) else 99
        ends = w["w"].endswith((".", "?", "!"))
        if gap >= SENTENCE or ends or len(cur) >= 28 or (gap >= BREATH and len(cur) >= 10):
            sents.append(cur); cur = []
    if cur: sents.append(cur)
    out = []
    for k, s in enumerate(sents):
        text = " ".join(x["w"] for x in s)
        out.append({"k": k, "a": s[0]["s"], "b": s[-1]["e"], "text": text, "words": s})
    return out


def first_noun(ws):
    """Heuristic: the first word that is not a stopword, pronoun, filler or an -ly adverb. Returns (word, time) or (None, None)."""
    for w in ws:
        t = re.sub(r"[^a-z0-9']", "", w["w"].lower())
        if not t or t in STOP or t in FILLER or t in PRONOUN_OPEN or t.endswith("ly"):
            continue
        return w["w"], w["s"]
    return None, None


def score_opener(sent):
    text = sent["text"].lower()
    ws = sent["words"]
    sc = 0.0; why = []
    if any(re.sub(r"[^a-z']", "", w["w"].lower()) in PRONOUN_OPEN for w in ws[:8]):
        sc += 2; why.append("you in the first eight words")
    n, t = first_noun(ws)
    if n is not None:
        rel = t - sent["a"]
        if rel <= 0.9: sc += 2; why.append(f"noun '{n}' by {rel:.1f} s")
        elif rel <= 1.5: sc += 1
    if re.search(r"\b\d+\b", text): sc += 1.5; why.append("a number")
    if any(w in STAKES for w in re.findall(r"[a-z']+", text)): sc += 1; why.append("a stake a stranger feels")
    nw = len(ws)
    if 5 <= nw <= 18: sc += 1
    if any(text.startswith(b) for b in BAD_OPENERS): sc -= 3; why.append("starts like an intro")
    fill = sum(1 for w in ws if re.sub(r"[^a-z']", "", w["w"].lower()) in FILLER)
    if fill >= 3: sc -= 1.5; why.append(f"{fill} fillers")
    if nw <= 3: sc -= 2
    return sc, why


def score_closer(sent):
    text = sent["text"].lower()
    sc = 0.0
    for cue in ("grateful", "that's why", "and that is", "and that's", "the answer", "turns out", "so now", "never again",
                "every time", "i'm done", "that's it", "for that"):
        if cue in text: sc += 2
    if any(text.rstrip().endswith(x) for x in ("you", "it", "that", "now", "me")): sc += 0.5
    sc += 0.5 if 4 <= len(sent["words"]) <= 20 else 0
    return sc


def filler_density(ws, seconds):
    f = sum(1 for w in ws if re.sub(r"[^a-z']", "", w["w"].lower()) in FILLER)
    return f, (f / seconds * 60 if seconds > 0 else 0)


# ---------- plan ----------
def snap(words, a, b):
    """Pull a span's edges to the surrounding breaths: start 0.08 s before the first word, end 0.14 s after the last."""
    return max(0.0, a - 0.08), b + 0.14


def cmd_plan(args):
    words = load_words(args.words)
    sents = sentences(words)
    if not sents: sys.exit("no words")
    for cut in (args.split_at or []):
        first = cut.lower().split()[0]; out = []
        for s in sents:
            idx = next((i for i in range(1, len(s["words"])) if " ".join(w["w"].lower() for w in s["words"][i:i + len(cut.split())]).startswith(cut.lower())), None)
            if idx is None: out.append(s); continue
            a_w, b_w = s["words"][:idx], s["words"][idx:]
            out.append(dict(s, b=a_w[-1]["e"], words=a_w, text=" ".join(w["w"] for w in a_w)))
            out.append(dict(s, a=b_w[0]["s"], words=b_w, text=" ".join(w["w"] for w in b_w)))
        sents = [dict(s, k=i) for i, s in enumerate(out)]
    lo, hi = JOBS[args.job]

    # drop phrases the editor names, plus known intro filler
    dropped = []
    drops = [d.lower() for d in (args.drop or [])] + FILLER_PHRASES
    keep = []
    keeps = [k.lower() for k in (args.keep or [])]
    def protected(s): return any(k in s["text"].lower() for k in keeps)
    for s in sents:
        t = re.sub(r"[^a-z0-9' ]", "", s["text"].lower())
        hit = next((d for d in drops if d in t and len(d) > 8), None)
        if hit and len(s["words"]) <= 24 and not protected(s):
            dropped.append({"text": s["text"], "why": f"contains '{hit}'"}); continue
        keep.append(s)
    sents = keep

    # opener
    scored = [(score_opener(s), s) for s in sents]
    if args.open_on:
        cand = [s for s in sents if args.open_on.lower() in s["text"].lower()]
        if not cand: sys.exit(f"--open-on not found: {args.open_on}")
        opener = cand[0]; op_why = ["chosen by the editor"]
    else:
        (sc, why), opener = max(scored, key=lambda x: x[0][0])
        op_why = why
    # closer
    if args.end_on:
        cand = [s for s in sents if args.end_on.lower() in s["text"].lower()]
        if not cand: sys.exit(f"--end-on not found: {args.end_on}")
        closer = cand[-1]
    else:
        tail = sents[-max(1, len(sents) // 3):]
        closer = max(tail, key=score_closer)
    # within-opener trim: start at the opener's first strong word if the editor passed --open-on
    if args.open_on:
        i = next(i for i, w in enumerate(opener["words"]) if args.open_on.lower().split()[0] in w["w"].lower())
        opener = dict(opener, a=opener["words"][i]["s"], words=opener["words"][i:], text=" ".join(w["w"] for w in opener["words"][i:]))

    # order: opener, then the rest in source order up to and including the closer
    body = [s for s in sents if s is not opener and s["a"] >= (opener["b"] if args.keep_before_opener is False else -1)]
    body = [s for s in body if s["b"] <= closer["b"] + 0.01]
    ordered = [opener] + body
    # length control: drop lowest-scoring middle sentences until under the band
    def total(seq): return sum(s["b"] - s["a"] for s in seq)
    limit = min(hi, args.target) if args.target else hi
    while total(ordered) > limit and len(ordered) > 2:
        middle = sorted((s for s in ordered[1:-1] if not protected(s)), key=lambda s: score_opener(s)[0] + score_closer(s))
        victim = next((s for s in middle if total(ordered) - (s["b"] - s["a"]) >= lo), None)
        if victim is None: break  # nothing can go without dropping under the band floor
        dropped.append({"text": victim["text"], "why": f"over {limit:g} s ({args.job} band {lo} to {hi}); lowest-value middle sentence"})
        ordered.remove(victim)
    # merge adjacent sentences into segments (a cut only where the source is not contiguous)
    segs = []
    for s in ordered:
        a, b = snap(words, s["a"], s["b"])
        if segs and a <= segs[-1]["b"] + 0.30:
            segs[-1]["b"] = b; segs[-1]["text"] += " " + s["text"]
        else:
            segs.append({"a": round(a, 2), "b": round(b, 2), "text": s["text"]})
    for s in segs: s["b"] = round(s["b"], 2)
    tot = round(sum(s["b"] - s["a"] for s in segs), 2)
    all_words = [w for s in ordered for w in s["words"]]
    fcount, fpm = filler_density(all_words, tot)
    n, t = first_noun(opener["words"])
    plan = {
        "made": dt.datetime.now().isoformat(timespec="minutes"), "src": os.path.abspath(args.src), "words": os.path.abspath(args.words),
        "job": args.job, "band_s": [lo, hi], "total_s": tot, "cuts": max(0, len(segs) - 1), "segments": segs,
        "opener": {"text": opener["text"], "why": op_why, "first_word_s": round(opener["words"][0]["s"] - segs[0]["a"], 2),
                   "first_noun": n, "first_noun_s": round(t - segs[0]["a"], 2) if t is not None else None,
                   "has_you": any(re.sub(r"[^a-z']", "", w["w"].lower()) in PRONOUN_OPEN for w in opener["words"][:8]),
                   "type": ("you-line" if any(re.sub(r"[^a-z']", "", w["w"].lower()) in PRONOUN_OPEN for w in opener["words"][:8])
                            else "number" if re.search(r"\b\d+\b", opener["text"]) else "cold-line")},
        "closer": {"text": closer["text"], "tail_s": round(segs[-1]["b"] - closer["b"], 2)},
        "dropped": dropped, "filler": {"count": fcount, "per_min": round(fpm, 1)},
        "lockup_suggestion": (n or "").lower(), "captions": {"start_s": 3.0, "policy": "chest band, 2 to 4 words, none under the lockup"},
        "challenge": [],
    }
    Path(args.out).write_text(json.dumps(plan, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"plan: {args.job} {tot} s in {len(segs)} segment(s), {plan['cuts']} cut(s); band {lo} to {hi} s")
    print(f"open on: {opener['text'][:90]}")
    print(f"  why: {'; '.join(op_why)} | first word {plan['opener']['first_word_s']} s | first noun {n} at {plan['opener']['first_noun_s']} s")
    print(f"end on:  {closer['text'][-90:]}")
    for d in dropped: print(f"dropped: {d['text'][:70]}  ({d['why']})")
    print(f"filler: {fcount} ({fpm:.1f} a minute)  lockup suggestion: {plan['lockup_suggestion']!r}")
    print(f"wrote {args.out}; next: challenge, then render")


# ---------- challenge ----------
def read_ledger():
    if not LEDGER.exists(): return []
    with open(LEDGER, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def rotate(options, recent):
    """The first option not used in the recent rows, else the least recently used."""
    for o in options:
        if o not in recent: return o
    return min(options, key=lambda o: max(i for i, r in enumerate(recent) if r == o) if o in recent else -1)


def cmd_challenge(args):
    plan = json.load(open(args.plan, encoding="utf-8"))
    led = read_ledger()[-3:]
    notes = []
    op = plan["opener"]
    # 1. the opener's own counter-arguments
    if op["first_word_s"] > 0.5:
        notes.append({"decision": "open", "flag": f"first word at {op['first_word_s']} s", "counter": "Doctrine 3.1 and Emplifi: speech inside 0.5 s is the largest measured lift.", "fix": "pull the in-point to 0.08 s before the first word"})
    if op["first_noun_s"] is None or op["first_noun_s"] > 0.9:
        notes.append({"decision": "open", "flag": f"first noun '{op['first_noun']}' at {op['first_noun_s']} s", "counter": "Doctrine 3.3: the first sentence carries the person and the noun by 0.9 s.", "fix": "start on a later word of the same sentence, or pick the sentence with the noun"})
    if not op["has_you"]:
        notes.append({"decision": "open", "flag": "no 'you' in the first eight words", "counter": "Kier's 112 and Content Labs' 14,424: 'you' lines ran 9.6x against 6.2x for 'I'. Doctrine 3.7: name-call, not topic.", "test": "Trial twin: this opener against the best you-line in the take"})
    stakes = [w for w in re.findall(r"[a-z']+", op["text"].lower()) if w in STAKES]
    if not stakes:
        notes.append({"decision": "open", "flag": "no stake a stranger feels in the opener", "counter": "Doctrine 2.5: money, hours, the wife, the boss, cold mornings, pride, in the first ten seconds.", "fix": "move the sentence with the concrete loss to second position"})
    # 2. the shape
    lo, hi = plan["band_s"]
    if not (lo <= plan["total_s"] <= hi):
        notes.append({"decision": "length", "flag": f"{plan['total_s']} s outside {lo} to {hi}", "counter": "Doctrine 10: two lengths by job, nothing padded.", "fix": "drop the lowest-value middle sentence or change --job"})
    if plan["cuts"] > max(1, round(plan["total_s"] / 30 * 3)):
        notes.append({"decision": "cuts", "flag": f"{plan['cuts']} cuts in {plan['total_s']} s", "counter": "Doctrine 6.1: at most three cuts per 30 s of face; cut only to remove.", "fix": "merge segments or drop the shortest"})
    if plan["closer"]["tail_s"] > 1.5:
        notes.append({"decision": "end", "flag": f"{plan['closer']['tail_s']} s after the last word", "counter": "Doctrine 11: cut on the last word of the payoff.", "fix": "trim the out-point"})
    if plan["filler"]["per_min"] > 8:
        notes.append({"decision": "delivery", "flag": f"{plan['filler']['per_min']} fillers a minute", "counter": "Doctrine 4.4: five a minute is free, above eight cut; damage is um and uh, not like.", "fix": "drop the worst sentence or re-shoot"})
    # 3. sameness against the ledger
    axes = {"opener_type": (op["type"], OPENER_TYPES), "set": (args.set, SETS), "device": (args.device, DEVICES),
            "lockup_style": (args.lockup_style, LOCKUPS), "tone": (args.tone, TONES), "camera": (args.camera, CAMERAS),
            "payoff": (args.payoff, PAYOFFS), "format": (args.format, FORMATS)}
    same = []
    for ax, (val, options) in axes.items():
        recent = [r.get(ax, "") for r in led]
        if val and len(led) >= 2 and all(r == val for r in recent[-2:]):
            alt = rotate(options, recent + [val])
            same.append({"axis": ax, "value": val, "repeated": len(recent[-2:]) + 1, "try": alt})
    lengths = [float(r.get("length_s", 0) or 0) for r in led]
    if lengths and all(abs(L - plan["total_s"]) < 6 for L in lengths[-2:]):
        same.append({"axis": "length", "value": plan["total_s"], "repeated": 3, "try": "a 20 s loop or the long form, not another near-identical length"})
    if same:
        notes.append({"decision": "variation", "flag": "an axis repeats three episodes running", "counter": "Doctrine 3.9 and file 01-human-not-ai: a known frame decays; rotate one axis per episode, never all.", "rotate": same})
    # 4. the thinking test (Remy's point: steps are not thinking)
    notes.append({"decision": "thinking", "questions": [
        "What is the last line, and is the first line its opposite?",
        "Which of Humm's five is in the first 20 s: where, the verb, the raw thought, the body, the exact words?",
        "Who is the one person this is for, and what do they already think that this says out loud?",
        "What changes every five to eight seconds without a cut: hand, pad, part, turn, pause?",
        "What is the one physical device, and is there only one?",
        "What would a stranger with no truck feel by second three?",
        "Which caption line would a viewer text to his buddy?",
        "What is the counter-argument to this cut, and which Trial twin would settle it?",
    ]})
    plan["challenge"] = notes
    plan["ledger_axes"] = {"set": args.set, "device": args.device, "lockup_style": args.lockup_style, "tone": args.tone,
                           "camera": args.camera, "payoff": args.payoff, "format": args.format}
    # the five-axis check from file 01: if the new episode matches more than two of five against any one of the last three, change one axis
    five = ["opener_type", "set", "device", "tone", "length_s"]
    for r in led:
        hits = [ax for ax in five if (str(r.get(ax, "")) == str({"opener_type": op["type"], "set": args.set, "device": args.device, "tone": args.tone, "length_s": None}.get(ax)))
                or (ax == "length_s" and abs(float(r.get("length_s", 0) or 0) - plan["total_s"]) < 6)]
        if len(hits) > 2:
            notes.insert(len(notes) - 1, {"decision": "variation", "flag": f"matches {len(hits)} of 5 axes against '{r.get('label','')}' ({', '.join(hits)})",
                                          "counter": "File 01, five-axis check: change one axis before it goes out.", "fix": "rotate the opener type, the set, the device or the length"})
    Path(args.plan).write_text(json.dumps(plan, indent=1, ensure_ascii=False), encoding="utf-8")
    flags = [n for n in notes if "flag" in n]
    print(f"challenge: {len(flags)} flag(s) against the doctrine, {len(same)} sameness warning(s) against the last {len(led)} episode(s)")
    for n in flags:
        print(f"- [{n['decision']}] {n['flag']}\n    counter: {n['counter']}\n    {('fix: ' + n['fix']) if 'fix' in n else ('test: ' + n['test']) if 'test' in n else ''}".rstrip())
        if "rotate" in n:
            for s in n["rotate"]: print(f"    rotate {s['axis']}: '{s['value']}' used {s['repeated']} running, try '{s['try']}'")
    print("thinking test (answer before you render):")
    for q in notes[-1]["questions"]: print(f"  - {q}")


# ---------- render ----------
def ffprobe(path, entries, stream="v"):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", stream, "-show_entries", entries, "-of", "default=nw=1:nk=1", path],
                         capture_output=True, text=True).stdout.strip().splitlines()
    return out


def build_ass(plan, words, lockup, caption_start, out_path):
    tl, t = [], 0.0
    for s in plan["segments"]:
        tl.append((s["a"], s["b"], t)); t += s["b"] - s["a"]
    def remap(x):
        for a, b, off in tl:
            if a - 0.05 <= x <= b + 0.05: return off + (x - a)
        return None
    groups, cur, prev = [], [], None
    def flush():
        nonlocal cur
        if cur: groups.append(cur); cur = []
    for w in words:
        s, e = remap(w["s"]), remap(w["e"])
        if s is None or e is None: flush(); prev = None; continue
        if s < caption_start: continue
        ww = w["w"]
        if re.sub(r"[^a-z']", "", ww.lower()) in ("like", "uh", "um") and cur and len(cur) >= 2: continue
        if prev is not None and s - prev > BREATH: flush()
        txt = " ".join(x[2] for x in cur)
        if cur and (len(cur) >= 4 or len(txt) + 1 + len(ww) > 24) and cur[-1][2].lower() not in STOP: flush()
        cur.append((s, e, ww)); prev = e
    flush()
    merged, carry = [], []
    for g in groups:
        if carry: g = carry + g; carry = []
        if len(g) == 1: carry = g; continue
        merged.append(g)
    if carry:
        if merged: merged[-1] = merged[-1] + carry
        else: merged.append(carry)
    # no group over four words or 24 characters: split long merges in half
    split = []
    for g in merged:
        while len(g) > 4 or len(" ".join(x[2] for x in g)) > 24:
            if len(g) < 2: break
            h = max(1, len(g) // 2); split.append(g[:h]); g = g[h:]
        split.append(g)
    merged = split
    def ts(x):
        h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60; return f"{h}:{m:02d}:{s:05.2f}"
    ass = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: 1080", "PlayResY: 1920", "WrapStyle: 2", "", "[V4+ Styles]",
           "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
           "Style: Cap,Poppins SemiBold,68,&H00DCE9EF,&H000000FF,&H00000000,&H96000000,0,0,0,0,100,100,0,0,1,0,3,2,72,130,735,1",
           "Style: Lock,Shrikhand,96,&H00424A5A,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,-3,1,0,0,8,72,72,110,1",
           "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
    for g in merged:
        s = g[0][0]; e = max(g[-1][1], s + 0.4)
        ass.append(f"Dialogue: 0,{ts(s)},{ts(e)},Cap,,0,0,0,,{' '.join(x[2] for x in g).replace('{','').replace('}','')}")
    if lockup:
        ass.append(f"Dialogue: 1,{ts(0.13)},{ts(3.0)},Lock,,0,0,0,,{{\\fad(110,120)}}{lockup}")
    Path(out_path).write_text("\n".join(ass), encoding="utf-8")
    return len(merged)


def ffpath(p) -> str:
    """A path quoted for an ffmpeg filter argument: a Windows drive colon would otherwise end the option."""
    return "'" + str(p).replace("\\", "/").replace(":", "\\:") + "'"


def cmd_render(args):
    plan = json.load(open(args.plan, encoding="utf-8"))
    src = plan["src"]; words = load_words(plan["words"])
    out = Path(args.out); work = out.parent / (out.stem + "_work"); work.mkdir(parents=True, exist_ok=True)
    trc = (ffprobe(src, "stream=color_transfer") or [""])[0]
    hdr = "arib-std-b67" in trc or "smpte2084" in trc
    tone = ("zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=tonemap=mobius:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p," if hdr else "")
    vf = tone + "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1"
    ENC = ["-r", "30", "-c:v", "libx264", "-preset", "medium", "-crf", "14", "-pix_fmt", "yuv420p", "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709",
           "-x264-params", "colorprim=bt709:transfer=bt709:colormatrix=bt709"]
    for i, s in enumerate(plan["segments"]):
        a, b = s["a"], s["b"]
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-threads", "2", "-ss", str(a), "-to", str(b), "-i", src, "-filter_threads", "2", "-vf", vf,
                        "-af", f"afade=t=in:d=0.02,afade=t=out:st={max(0, b - a - 0.03)}:d=0.03,aresample=48000", "-map", "0:v:0", "-map", "0:a:0"] + ENC +
                       ["-c:a", "pcm_s16le", str(work / f"seg{i}.mov")], check=True)
        print("seg", i, "ok", flush=True)
    (work / "list.txt").write_text("".join(f"file 'seg{i}.mov'\n" for i in range(len(plan["segments"]))))
    EXP = ["-r", "30", "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-maxrate", "16M", "-bufsize", "32M", "-profile:v", "high", "-level", "4.2", "-g", "30", "-keyint_min", "30",
           "-pix_fmt", "yuv420p", "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-x264-params", "colorprim=bt709:transfer=bt709:colormatrix=bt709:aq-mode=3",
           "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart"]
    pre = "highpass=f=90,afftdn=nf=-28,acompressor=threshold=-18dB:ratio=3:attack=5:release=120"
    m = subprocess.run(["ffmpeg", "-hide_banner", "-y", "-f", "concat", "-safe", "0", "-i", str(work / "list.txt"), "-vn", "-af", pre + ",loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    js = json.loads(m[m.rfind("{"):m.rfind("}") + 1])
    ln = f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={js['input_i']}:measured_TP={js['input_tp']}:measured_LRA={js['input_lra']}:measured_thresh={js['input_thresh']}:offset={js['target_offset']}:linear=true"
    nocap = out.with_name(out.stem + "_nocap.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(work / "list.txt"), "-af", pre + "," + ln + ",aresample=48000", "-vf", "setsar=1"] + EXP + [str(nocap)], check=True)
    print("nocap ok", flush=True)
    ass = out.with_suffix(".ass")
    n = build_ass(plan, words, args.lockup, plan["captions"]["start_s"], ass)
    if args.no_captions and not args.lockup:
        shutil.copyfile(nocap, out)
    else:
        if args.no_captions:  # lockup only
            txt = ass.read_text(encoding="utf-8").splitlines(); ass.write_text("\n".join(l for l in txt if not l.startswith("Dialogue: 0,")), encoding="utf-8")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(nocap), "-vf", f"ass={ffpath(ass)}:fontsdir={ffpath(args.fonts)}", "-c:a", "copy"] + EXP + [str(out)], check=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(out), "-vf", "fps=1,scale=240:-1,tile=8x6", str(out.with_name(out.stem + "_qa.jpg"))], check=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "1.0", "-i", str(out), "-frames:v", "1", str(out.with_name(out.stem + "_cover.jpg"))], check=True)
    plan["render"] = {"out": str(out), "nocap": str(nocap), "ass": str(ass), "caption_groups": n, "lockup": args.lockup}
    Path(args.plan).write_text(json.dumps(plan, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"rendered {out} ({n} caption groups); qa sheet and cover beside it. Next: lint, then ledger add")


# ---------- lint ----------
def cmd_lint(args):
    plan = json.load(open(args.plan, encoding="utf-8"))
    ok, bad = [], []
    def chk(cond, label):
        (ok if cond else bad).append(label)
    op = plan["opener"]; lo, hi = plan["band_s"]
    chk(op["first_word_s"] <= 0.5, f"first word at {op['first_word_s']} s (limit 0.5)")
    chk(op["first_noun_s"] is not None and op["first_noun_s"] <= 0.9, f"first noun '{op['first_noun']}' at {op['first_noun_s']} s (limit 0.9)")
    chk(lo <= plan["total_s"] <= hi, f"length {plan['total_s']} s in {lo} to {hi}")
    chk(plan["cuts"] <= max(1, round(plan["total_s"] / 30 * 3)), f"{plan['cuts']} cuts (limit 3 per 30 s)")
    chk(plan["closer"]["tail_s"] <= 1.5, f"ends {plan['closer']['tail_s']} s after the last word (limit 1.5)")
    chk(plan["filler"]["per_min"] <= 8, f"fillers {plan['filler']['per_min']} a minute (limit 8)")
    ass = args.ass or (plan.get("render") or {}).get("ass")
    if ass and os.path.exists(ass):
        under, long_groups = 0, 0
        for line in open(ass, encoding="utf-8"):
            if line.startswith("Dialogue: 0,"):
                parts = line.split(",", 9); start = parts[1]; text = parts[9].strip()
                h, m, s = start.split(":"); st = int(h) * 3600 + int(m) * 60 + float(s)
                if st < 3.0: under += 1
                if len(text.split()) > 4 or len(text) > 24: long_groups += 1
        chk(under == 0, f"{under} caption group(s) under the lockup (first 3 s)")
        chk(long_groups == 0, f"{long_groups} caption group(s) over 4 words or 24 characters")
    video = args.video or (plan.get("render") or {}).get("out")
    if video and os.path.exists(video):
        w, h, fr = (ffprobe(video, "stream=width,height,r_frame_rate") + ["", "", ""])[:3]
        chk(w == "1080" and h == "1920", f"frame {w}x{h}")
        chk(fr in ("30/1", "30000/1000"), f"frame rate {fr}")
        dur = float((ffprobe(video, "format=duration", "a") or ["0"])[0] or 0)
        chk(abs(dur - plan["total_s"]) < 0.6, f"duration {dur:.1f} s vs plan {plan['total_s']}")
        m = subprocess.run(["ffmpeg", "-hide_banner", "-i", video, "-af", "loudnorm=print_format=json", "-f", "null", "-"], capture_output=True, text=True).stderr
        try:
            js = json.loads(m[m.rfind("{"):m.rfind("}") + 1]); I = float(js["input_i"]); tp = float(js["input_tp"])
            chk(-16.5 <= I <= -13.0, f"loudness {I} LUFS (band -16.5 to -13)"); chk(tp <= -0.6, f"true peak {tp} dBTP (limit -0.6)")
        except Exception: bad.append("loudness could not be measured")
    for l in ok: print("  ok  ", l)
    for l in bad: print("  FIX ", l)
    print(f"lint: {len(ok)} ok, {len(bad)} to fix")
    return 1 if bad else 0


# ---------- ledger ----------
def cmd_ledger(args):
    cols = ["date", "label", "job", "opener_type", "first_noun", "set", "device", "lockup_style", "tone", "camera", "payoff", "format", "length_s", "cuts", "captions", "lockup", "plan"]
    if args.action == "show":
        rows = read_ledger()
        if not rows: print("ledger empty:", LEDGER); return
        for r in rows[-12:]: print("  ".join(str(r.get(c, "")) for c in cols[:12]))
        return
    plan = json.load(open(args.plan, encoding="utf-8"))
    axes = plan.get("ledger_axes", {})
    row = {"date": dt.date.today().isoformat(), "label": args.label, "job": plan["job"], "opener_type": plan["opener"]["type"], "first_noun": plan["opener"]["first_noun"] or "",
           "set": args.set or axes.get("set") or "", "device": args.device or axes.get("device") or "", "lockup_style": args.lockup_style or axes.get("lockup_style") or "",
           "tone": args.tone or axes.get("tone") or "", "camera": axes.get("camera") or "", "payoff": axes.get("payoff") or "", "format": axes.get("format") or "", "length_s": plan["total_s"], "cuts": plan["cuts"], "captions": "no" if args.no_captions else "yes",
           "lockup": (plan.get("render") or {}).get("lockup") or "", "plan": os.path.relpath(args.plan, ROOT) if str(ROOT) in os.path.abspath(args.plan) else args.plan}
    new = not LEDGER.exists()
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    with open(LEDGER, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, delimiter="\t")
        if new: w.writeheader()
        w.writerow(row)
    print("ledger +1:", LEDGER.relative_to(ROOT), "|", row["label"], row["opener_type"], row["set"], row["device"], row["tone"], row["length_s"], "s")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("plan"); p.add_argument("--words", required=True); p.add_argument("--src", required=True); p.add_argument("--job", default="talk", choices=sorted(JOBS))
    p.add_argument("--open-on"); p.add_argument("--end-on"); p.add_argument("--drop", action="append", help="drop any sentence containing this text (repeatable)"); p.add_argument("--keep", action="append", help="never drop a sentence containing this text (repeatable)"); p.add_argument("--split-at", action="append", help="force a sentence boundary where this text begins (repeatable)"); p.add_argument("--keep-before-opener", action="store_true", default=False)
    p.add_argument("--target", type=float, help="aim at this many seconds (default: the top of the band)")
    p.add_argument("-o", "--out", default="plan.json"); p.set_defaults(fn=cmd_plan)
    c = sub.add_parser("challenge"); c.add_argument("plan"); c.add_argument("--set"); c.add_argument("--device"); c.add_argument("--lockup-style"); c.add_argument("--tone"); c.add_argument("--camera"); c.add_argument("--payoff"); c.add_argument("--format"); c.set_defaults(fn=cmd_challenge)
    r = sub.add_parser("render"); r.add_argument("plan"); r.add_argument("-o", "--out", required=True); r.add_argument("--lockup", default=""); r.add_argument("--no-captions", action="store_true"); r.add_argument("--fonts", default=str(FONTS)); r.set_defaults(fn=cmd_render)
    l = sub.add_parser("lint"); l.add_argument("plan"); l.add_argument("--video"); l.add_argument("--ass"); l.set_defaults(fn=cmd_lint)
    g = sub.add_parser("ledger"); g.add_argument("action", choices=["add", "show"]); g.add_argument("plan", nargs="?"); g.add_argument("--label", default=""); g.add_argument("--set"); g.add_argument("--device"); g.add_argument("--lockup-style"); g.add_argument("--tone"); g.add_argument("--no-captions", action="store_true"); g.set_defaults(fn=cmd_ledger)
    args = ap.parse_args()
    rc = args.fn(args)
    sys.exit(rc or 0)


if __name__ == "__main__":
    main()
