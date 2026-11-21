#!/usr/bin/env python3
"""
words_to_props.py: the generator layer for rival-reels menu compositions.

  spoken script word timestamps (words.json from Whisper)  +  a reel spec (items, cues, hook, gate)
      ->  <out>.props.json   for `npx remotion render src/index.ts CardReel|RivalReel ... --props=<out>`
      ->  <out>.sfx.json     sfx events for build_reel3.py's "sfx" audio block

Every visual event lands on the START of a spoken word (the @ai.nxtlvl pattern: picture generated to the words,
not footage-first). See research/reel-references/2026-11-21-nxtlvl-repo/PIPELINE-STUDY.md sections 1.5 and 5/12.

Usage (never bare python; run isolated):
  "%LOCALAPPDATA%\\Programs\\Python\\Python312\\python.exe" -I words_to_props.py spec.json words.json out.props.json

Timing rules (seconds unless stated):
  LEAD       0.12   a card appears this much before its cue word starts
  OLD_GAP    0.50   when `old` is set: strikestamp at the cue, item card this much later
  HOLD       1.60   durationSec = last word end + HOLD
  IRIS_LEAD  0.40   iris wipe starts this much before the gate
  CAPTION_GAP 0.55  caption groups split on silences longer than this, and on . ! ?
  caption groups are 2 to 5 words (single words merge into the previous group), max CAP_CHARS so they stay one line

Lint (refuses to write):
  cue word not found (searched forward from the previous item), cards overlapping > 0.3 s, hook > 7 words,
  any text estimated below y 1440, an item window shorter than 1.2 s.
Nothing here edits the TSX. If a component lacks a prop the generator needs, it is listed in WORDS-TO-PROPS-README.md.
"""
import json
import math
import os
import re
import sys

FPS_DEFAULT = 30
LEAD = 0.12
OLD_GAP = 0.50
HOLD = 1.60
IRIS_LEAD = 0.40
IRIS_DUR = 0.70
CAPTION_GAP = 0.55
CAP_MIN, CAP_MAX, CAP_CHARS = 2, 5, 28
MIN_WINDOW = 1.2
MAX_OVERLAP = 0.3
HOOK_MAX_WORDS = 7
TEXT_FLOOR = 1440           # nothing with text below this y (IG UI covers the bottom)
SIDEBAR_BOTTOM = 1430

# layout (1080 x 1920). hud/headline/strike/card are the kit defaults from Menu.tsx unless noted
Y_HUD = 300
Y_HEADLINE = 400
Y_STRIKE = 540
Y_CARD = 560                # card alone
Y_CARD_UNDER_STRIKE = 700   # card when a strikestamp sits above it
Y_GATE = 620
Y_GHOST = 1000
CAPTION_LINE_H = 72         # PlainCaption 60 px * 1.2
CAPTION_CHAR_W = 31         # Poppins SemiBold 60 px, rough average

# sfx: the study's peaks (dBFS) and the nearest sound build_reel3's synthesized kit already has
SFX_GAIN = {"whoosh": -10, "pop": -12, "stamp": -7, "tick": -17, "notify": -12}
SFX_KIT_FALLBACK = {"whoosh": "whoosh", "pop": "click", "stamp": "impact", "tick": "click", "notify": None}


class LintError(Exception):
    pass


# ---------------------------------------------------------------- words
def norm(w):
    return re.sub(r"[^a-z0-9]", "", w.lower())


def load_words(path):
    with open(path, encoding="utf-8") as f:
        raw = json.load(f)
    words = []
    for i, w in enumerate(raw):
        words.append({"i": i, "w": w["w"].strip(), "n": norm(w["w"]), "s": float(w["s"]), "e": float(w["e"])})
    if not words:
        raise LintError("words.json is empty")
    return words


def parse_cue(cue):
    """'driven' | 'driven#2' | 'eleven labs' | {'word': 'driven', 'nth': 2} -> (tokens, nth)"""
    nth = 1
    if isinstance(cue, dict):
        text = cue.get("word", "")
        nth = int(cue.get("nth", 1))
    else:
        text = str(cue)
        if "#" in text:
            text, n = text.rsplit("#", 1)
            nth = int(n)
    tokens = [norm(t) for t in text.split() if norm(t)]
    if not tokens:
        raise LintError(f"empty cue {cue!r}")
    return tokens, nth


def find_cue(words, cue, start=0.0, end=None, label=""):
    """Prefix match on normalized words, consecutive tokens for multi-word cues, nth hit at or after `start`."""
    tokens, nth = parse_cue(cue)
    hits = []
    for k in range(len(words) - len(tokens) + 1):
        w = words[k]
        if w["s"] < start - 1e-6:
            continue
        if end is not None and w["s"] > end + 1e-6:
            break
        if all(words[k + j]["n"].startswith(tokens[j]) for j in range(len(tokens))):
            hits.append(w)
    if len(hits) < nth:
        rng = f"after {start:.2f}s" + (f" and before {end:.2f}s" if end is not None else "")
        raise LintError(f"cue {cue!r} ({label}) not found {rng}; need hit #{nth}, got {len(hits)}")
    return hits[nth - 1]


# ---------------------------------------------------------------- captions
def _group_segment(sel):
    """One segment (no item boundary inside): split on gaps > CAPTION_GAP, sentence punctuation, CAP_MAX words,
    CAP_CHARS chars. Singles merge forward when they open the segment, backward otherwise."""
    groups, cur = [], []

    def flush():
        nonlocal cur
        if cur:
            groups.append(cur)
            cur = []

    for w in sel:
        if cur:
            prev = cur[-1]
            gap = w["s"] - prev["e"]
            chars = sum(len(x["w"]) for x in cur) + len(cur) + len(w["w"])
            if gap > CAPTION_GAP or re.search(r"[.!?]$", prev["w"]) or len(cur) >= CAP_MAX or chars > CAP_CHARS:
                flush()
        cur.append(w)
    flush()
    merged = []
    for g in groups:
        if len(g) < CAP_MIN and merged:
            merged[-1] = merged[-1] + g
        else:
            merged.append(g)
    if len(merged) >= 2 and len(merged[0]) < CAP_MIN:
        merged[1] = merged[0] + merged[1]
        merged = merged[1:]
    return merged


def group_captions(words, t0, t1, fps, boundaries=()):
    """Caption groups for words with t0 <= s < t1. Item start times are hard boundaries: a caption never
    spans two item windows, so the caption changes with the card. Returns [{text,start,end,words}]."""
    sel = [w for w in words if t0 - 1e-6 <= w["s"] < t1 - 1e-6]
    cuts = sorted(b for b in boundaries if t0 < b < t1)
    merged = []
    seg, ci = [], 0
    for w in sel:
        while ci < len(cuts) and w["s"] >= cuts[ci] - 1e-6:
            merged += _group_segment(seg)
            seg = []
            ci += 1
        seg.append(w)
    merged += _group_segment(seg)
    out = []
    for k, g in enumerate(merged):
        start = g[0]["s"]
        last_e = g[-1]["e"]
        if k + 1 < len(merged):
            nxt = merged[k + 1][0]["s"]
            end = nxt if nxt - last_e < 0.8 else last_e + 0.4
        else:
            end = min(last_e + 0.5, t1)
        end = min(end, t1)
        if end - start < 2 / fps:
            continue
        text = " ".join(x["w"] for x in g)
        out.append({"text": text, "start": round(start, 3), "end": round(end, 3), "words": g})
    return out


# ---------------------------------------------------------------- estimates for the text floor lint
def card_height(item):
    h = 60 + 6                                     # padding + border
    row = 110 if item.get("icon") else 64 + (32 if item.get("sub") else 0)
    h += row
    if item.get("count") or item.get("tag"):
        h += 22 + 48
    if item.get("chips"):
        h += 22 + 52
    if item.get("foot"):
        h += 20 + 24
    return h


def caption_lines(text):
    return max(1, math.ceil(len(text) * CAPTION_CHAR_W / 900))


# ---------------------------------------------------------------- main build
def build(spec, words):
    fps = int(spec.get("fps", FPS_DEFAULT))
    comp = spec.get("composition", "CardReel")
    if comp not in ("CardReel", "RivalReel"):
        raise LintError(f"composition must be CardReel or RivalReel, got {comp!r}")
    items = spec.get("items") or []
    if not items:
        raise LintError("spec has no items")
    n = len(items)
    f2 = lambda s: round(s, 3)
    to_f = lambda s: int(round(s * fps))

    last_end = words[-1]["e"]
    duration = f2(last_end + HOLD)
    floor_notes = []      # (label, bottom_y)

    # ---- gate (optional) decides where the last window ends
    gate = spec.get("gate")
    gate_at = iris_at = None
    if gate:
        gw = find_cue(words, gate.get("cue", "comment"), label="gate")
        gate_at = f2(gw["s"] - LEAD)
        iris_at = f2(gate_at - IRIS_LEAD)

    # ---- resolve item cues in order, searching forward from the previous item
    plan = []
    cursor = 0.0
    for idx, it in enumerate(items):
        if "cue" not in it:
            raise LintError(f"item {idx + 1} ({it.get('name')}) has no cue")
        if "at" in it:                                  # explicit override, seconds
            start = float(it["at"])
            cue_w = {"w": "(explicit)", "s": start + LEAD}
        else:
            cue_w = find_cue(words, it["cue"], start=cursor, label=f"item {idx + 1} {it.get('name')}")
            start = f2(cue_w["s"] - LEAD)
        start = max(0.0, start)
        if plan and start <= plan[-1]["start"]:
            raise LintError(f"item {idx + 1} cue {it['cue']!r} at {start:.2f}s is not after item {idx} ({plan[-1]['start']:.2f}s)")
        plan.append({"idx": idx, "item": it, "cue_word": cue_w["w"], "cue_s": cue_w["s"], "start": start})
        cursor = cue_w["s"] + 0.01

    # window ends
    tail_end = f2(iris_at + IRIS_DUR * 0.43) if gate else duration     # iris covers the frame ~0.3 s in
    for k, p in enumerate(plan):
        p["end"] = plan[k + 1]["start"] if k + 1 < n else tail_end
        p["win"] = f2(p["end"] - p["start"])
        if p["win"] < MIN_WINDOW:
            raise LintError(f"item {k + 1} ({p['item'].get('name')}) window {p['win']:.2f}s < {MIN_WINDOW}s")

    # ---- hook
    hook = spec.get("hook") or {}
    hook_text = hook.get("text", "")
    if hook_text and len(hook_text.split()) > HOOK_MAX_WORDS:
        raise LintError(f"hook has {len(hook_text.split())} words, max {HOOK_MAX_WORDS}: {hook_text!r}")
    hook_end = plan[0]["start"]

    overlays, sfx, captions = [], [], []

    # ---- sidebar geometry (anchored above the IG UI)
    sidebar = bool(spec.get("sidebar"))
    side_names = [it.get("short") or it.get("name", f"Item {i + 1}") for i, it in enumerate(items)]
    sb_cols = 2 if n > 5 else 1
    sb_size = int(spec.get("sidebarSize", 22))
    sb_rows = math.ceil(n / sb_cols)
    sb_line = sb_size * 1.55
    sb_y = int(SIDEBAR_BOTTOM - sb_rows * sb_line) if sidebar else None
    cap_y = (sb_y - 130) if sidebar else 1150
    cap_y = int(spec.get("captionY", cap_y))

    # ---- ghost word (decoration, lowest z: first in the array)
    if spec.get("ghost"):
        overlays.append({"type": "ghost", "at": 0, "dur": duration, "props": {"text": spec["ghost"], "y": Y_GHOST}})

    # ---- hud variant
    hud = spec.get("hud", "dots")
    hud_props = lambda count: {"count": count, "total": n, "y": Y_HUD, "variant": hud, **({"handle": spec["handle"]} if spec.get("handle") else {})}
    if hud and hook_end > 0:
        overlays.append({"type": "hud", "at": 0, "dur": f2(hook_end), "props": hud_props(0)})
    floor_notes.append(("hud", Y_HUD + 50))

    # ---- headline on the hook
    if hook_text and hook_end > 2 / fps:
        hp = {"text": hook_text, "y": Y_HEADLINE}
        if hook.get("accent"):
            hp["accent"] = hook["accent"]
        overlays.append({"type": "headline", "at": 0, "dur": f2(hook_end), "props": hp})
        size = 60 * max(0.68, min(1, 24 / max(1, len(hook_text))))
        lines = max(1, math.ceil(len(hook_text) * size * 0.55 / 878))
        floor_notes.append(("headline", Y_HEADLINE + lines * size * 1.5))

    # ---- items
    card_spans = []
    for k, p in enumerate(plan):
        it = p["item"]
        start, end = p["start"], p["end"]
        if hud:
            overlays.append({"type": "hud", "at": start, "dur": f2(end - start), "props": hud_props(k + 1)})
        if sidebar:
            overlays.append({"type": "sidebar", "at": start, "dur": f2(end - start),
                             "props": {"items": side_names, "current": k + 1, "y": sb_y, "cols": sb_cols, "size": sb_size}})
            floor_notes.append((f"sidebar {k + 1}", sb_y + sb_rows * sb_line))

        has_old = bool(it.get("old"))
        card_at = f2(start + OLD_GAP) if has_old else start
        if has_old:
            sp = {"name": it["old"], "tag": it.get("oldTag", "STOCK"), "stamp": it.get("stamp", "RIVAL"), "y": Y_STRIKE}
            if it.get("oldMeta"):
                sp["meta"] = it["oldMeta"]
            if it.get("oldIcon"):
                sp["icon"] = it["oldIcon"]
            overlays.append({"type": "strikestamp", "at": start, "dur": f2(end - start), "props": sp})
            sfx.append({"at": f2(start + 16 / fps), "kind": "stamp"})
            floor_notes.append((f"strike {k + 1}", Y_STRIKE + 120))

        card_y = Y_CARD_UNDER_STRIKE if has_old else Y_CARD
        card_dur = f2(end - card_at)
        if card_dur < 0.6:
            raise LintError(f"item {k + 1} card would show for only {card_dur:.2f}s")
        cp = {"title": it.get("name", f"Item {k + 1}"), "y": card_y}
        for key in ("sub", "icon", "count", "tag", "foot", "sticker", "shadow", "ghost"):
            if it.get(key) is not None:
                cp[key] = it[key]

        chips = []
        chip_cursor = card_at
        for c in it.get("chips") or []:
            if "cue" in c:
                cw = find_cue(words, c["cue"], start=chip_cursor, end=end, label=f"chip {c.get('text')!r} of item {k + 1}")
                chip_t = cw["s"]
                chip_cursor = cw["s"] + 0.01
            else:
                chip_t = card_at + float(c.get("after", 0.5))
            at_frames = max(0, to_f(chip_t - card_at))
            chips.append({"text": c["text"], "at": at_frames})
            sfx.append({"at": f2(card_at + at_frames / fps), "kind": "pop"})
        if chips:
            cp["chips"] = chips
        if it.get("sticker"):
            if it.get("stickerCue"):
                sw = find_cue(words, it["stickerCue"], start=card_at, end=end, label=f"sticker of item {k + 1}")
                cp["stickerAt"] = max(0, to_f(sw["s"] - card_at))
            else:
                cp["stickerAt"] = (max(c["at"] for c in chips) + 10) if chips else 24
            sfx.append({"at": f2(card_at + cp["stickerAt"] / fps), "kind": "stamp"})
        overlays.append({"type": "item", "at": card_at, "dur": card_dur, "props": cp})
        sfx.append({"at": card_at, "kind": "whoosh"})
        card_bottom = card_y + card_height(it)
        floor_notes.append((f"card {k + 1}", card_bottom))
        if card_bottom + 24 > cap_y and spec.get("captions", "auto") != "none":
            raise LintError(f"item {k + 1} card bottom {card_bottom} collides with captions at y {cap_y}; drop foot/chips or move the sidebar")
        card_spans.append((card_at, card_at + card_dur, k + 1))
        p["card_at"] = card_at
        p["card_dur"] = card_dur

    # ---- card overlap lint
    for a in range(len(card_spans)):
        for b in range(a + 1, len(card_spans)):
            ov = min(card_spans[a][1], card_spans[b][1]) - max(card_spans[a][0], card_spans[b][0])
            if ov > MAX_OVERLAP:
                raise LintError(f"cards {card_spans[a][2]} and {card_spans[b][2]} overlap by {ov:.2f}s")

    # ---- gate + iris
    if gate:
        overlays.append({"type": "iris", "at": iris_at, "dur": IRIS_DUR, "props": {"color": gate.get("irisColor", "#7a1f1f")}})
        word = gate.get("word", "RIVAL")
        type_at = 6
        dm_at = max(36, type_at + len(word) * 3 + 14)
        gp = {"word": word, "reply": gate.get("reply", ""), "items": gate.get("items") or side_names, "y": Y_GATE, "typeAt": type_at, "dmAt": dm_at}
        if gate.get("handle"):
            gp["handle"] = gate["handle"]
        overlays.append({"type": "gate", "at": gate_at, "dur": f2(duration - gate_at), "props": gp})
        for ch in range(len(word)):
            sfx.append({"at": f2(gate_at + (type_at + ch * 3) / fps), "kind": "tick"})
        sfx.append({"at": f2(gate_at + dm_at / fps), "kind": "notify"})
        sfx.append({"at": iris_at, "kind": "whoosh"})
        rows = math.ceil(len(gp["items"]) / 2)
        floor_notes.append(("gate dm", Y_GATE + 250 + 110 + rows * 50))

    # ---- captions (none on the hook, none during the gate)
    if spec.get("captions", "auto") != "none":
        cap_end = gate_at if gate else duration
        for g in group_captions(words, hook_end, cap_end, fps, boundaries=[p["cue_s"] for p in plan]):
            c = {"text": g["text"], "start": g["start"], "end": g["end"], "y": cap_y}
            # accent = item name's first word when the caption sits inside that item's window and the word is spoken
            for p in plan:
                if p["start"] <= g["start"] < p["end"]:
                    first = (p["item"].get("accent") or p["item"].get("name", "").split(" ")[0]).strip(".,")
                    if first and any(norm(w["w"]) == norm(first) for w in g["words"]):
                        c["accent"] = first
                    break
            captions.append(c)
            floor_notes.append((f"caption {g['text'][:18]!r}", cap_y + caption_lines(g["text"]) * CAPTION_LINE_H))

    # ---- text floor lint
    low = [(lbl, y) for lbl, y in floor_notes if y > TEXT_FLOOR]
    if low:
        shown = ", ".join(f"{l} (bottom ~{int(y)})" for l, y in low[:5])
        more = f" and {len(low) - 5} more" if len(low) > 5 else ""
        raise LintError(f"text below y {TEXT_FLOOR}: {shown}{more}")

    # ---- assemble props
    overlays.sort(key=lambda o: (o["at"], 0 if o["type"] in ("ghost", "hud", "sidebar") else 1))
    if comp == "CardReel":
        props = {"bg": spec.get("bg", "#0b0b0c"), "durationSec": duration, "fps": fps,
                 "captionStyle": spec.get("captionStyle", "plain"), "overlays": overlays, "captions": captions}
        if "grain" in spec:
            props["grain"] = bool(spec["grain"])
    else:
        if not spec.get("plate"):
            raise LintError("RivalReel needs a plate")
        props = {"plate": spec["plate"], "captionStyle": spec.get("captionStyle", "plain"), "muted": spec.get("muted", True),
                 "fps": fps, "overlays": overlays, "captions": captions}
        if spec.get("cutout"):
            props["cutout"] = spec["cutout"]

    for s in sfx:
        s["gain_db"] = SFX_GAIN[s["kind"]]
        fb = SFX_KIT_FALLBACK[s["kind"]]
        s["kit"] = fb
        if fb:
            pass  # 2026-11-21: no hard file path; sfx_place.py rotates tools/sfx-kit by kind (the old tools/sfx synth kit is not shippable)
    sfx.sort(key=lambda s: s["at"])
    return props, sfx, plan, duration, hook_end


def print_plan(plan, duration, hook_end, spec):
    hook = (spec.get("hook") or {}).get("text", "")
    print(f"\nPLAN  {spec.get('composition', 'CardReel')}  duration {duration:.2f}s  hook 0.00 -> {hook_end:.2f}s  {hook!r}")
    print(f"{'#':>2}  {'item':<30} {'cue':<12} {'cue@':>6} {'start':>6} {'card':>6} {'win':>5}  chips")
    for p in plan:
        it = p["item"]
        chips = ", ".join(c["text"] for c in it.get("chips") or [])
        name = it.get("name", "")[:30]
        print(f"{p['idx'] + 1:>2}  {name:<30} {p['cue_word'][:12]:<12} {p['cue_s']:>6.2f} {p['start']:>6.2f} {p['card_at']:>6.2f} {p['win']:>5.2f}  {chips}")
    print()


def main(argv):
    if len(argv) < 4:
        print(__doc__)
        return 2
    spec_path, words_path, out_path = argv[1], argv[2], argv[3]
    with open(spec_path, encoding="utf-8") as f:
        spec = json.load(f)
    words = load_words(words_path)
    try:
        props, sfx, plan, duration, hook_end = build(spec, words)
    except LintError as e:
        print(f"LINT: {e}\nnothing written.")
        return 1
    print_plan(plan, duration, hook_end, spec)
    os.makedirs(os.path.dirname(os.path.abspath(out_path)) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(props, f, indent=1)
    sfx_path = re.sub(r"\.props\.json$", "", out_path)
    sfx_path = re.sub(r"\.json$", "", sfx_path) + ".sfx.json"
    with open(sfx_path, "w", encoding="utf-8") as f:
        json.dump(sfx, f, indent=1)
    print(f"wrote {out_path}  ({len(props['overlays'])} overlays, {len(props['captions'])} captions)")
    print(f"wrote {sfx_path}  ({len(sfx)} sfx events)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
