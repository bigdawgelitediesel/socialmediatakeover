"""gen_bumpers.py - props for the Move Bumpers giveaway reel (IMG_4259, 2026-11-20).
Run after: plate rendered -> copied to tools/rival-reels/public/plate.mp4 -> watch.py on the plate -> facetrack.py.
Plain shadow captions (the @chandlerintelligence rule), words behind the head in the empty sky, cards placed off the face."""
import json, sys
sys.path.insert(0, "tools"); import layout
WATCH = "out/bumpers-watch/bumpers-plate-NOCAP/words.json"
FACE = "tools/rival-reels/out/bumpers.face.json"
words = json.load(open(WATCH, encoding="utf-8"))
tr = layout.load(FACE)

# captions: 4-6 word phrases, break on sentence ends, pauses > 0.35 s and clause commas; never end on a dangling function word
caps, cur = [], []
FUNC = {"the", "a", "an", "of", "and", "to", "in", "on", "at", "for", "with", "that", "my", "our", "your", "his", "i", "we", "you", "they", "it", "is", "was", "or", "but", "so", "are"}
def flush(nxt=None):
    global cur
    if not cur: return
    s0 = cur[0]["s"]; e0 = cur[-1]["e"] + 0.25
    if nxt is not None: e0 = nxt
    caps.append({"text": " ".join(w["w"].strip() for w in cur), "start": round(s0, 2), "end": round(max(e0, s0 + 0.35), 2)}); cur = []
for i, w in enumerate(words):
    cur.append(w)
    tok = w["w"].strip(); nxt_w = words[i + 1] if i + 1 < len(words) else None
    gap = (nxt_w["s"] - w["e"]) if nxt_w else 9
    dangling = tok.strip(".,?!").lower() in FUNC
    if tok.endswith((".", "?", "!")) or gap > 0.35 or (len(cur) >= 4 and not dangling) or len(cur) >= 6 or (tok.endswith(",") and len(cur) >= 2):
        flush(nxt_w["s"] if (nxt_w and gap <= 0.35) else None)
flush()
merged = []
for c in caps:
    if merged and len(c["text"].split()) == 1 and (c["end"] - c["start"]) < 0.6 and len(merged[-1]["text"].split()) < 5 and abs(merged[-1]["end"] - c["start"]) < 0.05:
        merged[-1]["text"] += " " + c["text"]; merged[-1]["end"] = c["end"]
    else: merged.append(c)
caps = merged
# accent words (one coral box max per caption)
ACC = {"free": None, "steel": "steel", "box": "box", "dm": "DM", "front": "front", "rear": "rear", "shipping": "shipping"}
for c in caps:
    for k, v in ACC.items():
        if v and k in c["text"].lower().split() or (v and any(t.strip(".,").lower() == k for t in c["text"].split())):
            c["accent"] = v; break
raw = []
for c in caps:
    fx, fy, fw, fh = layout.face_box(tr, c["start"], c["end"])
    chin = fy + fh + 55
    raw.append(int(min(1280, max(1150, chin))))   # cards live at 1340+, captions stay above them
for i, c in enumerate(caps):
    win = sorted(raw[max(0, i - 1): i + 2]); c["y"] = win[len(win) // 2]

# segment map (plate_at of each kept segment) to place cards on the spoken beats
seg = json.load(open("out/bumpers-segmap.json"))
at = {i: s["plate_at"] for i, s in enumerate(seg)}
def fy(t0, t1, h): return layout.card_zone(tr, t0, t1, card_h=h)[0]

overlays = [
    {"type": "kinetic", "at": 0.15, "dur": 3.4, "behind": True, "props": {"words": ["FREE", "BUMPERS"], "y": 260, "size": 190, "align": "right", "pad": 40, "accent": "FREE"}},
    {"type": "tooltag", "at": at[1] + 0.05, "dur": 3.2, "props": {"icon": "cards/movebumpers-logo.png", "iconW": 400, "iconH": 36, "pill": True, "name": "Bumpers", "y": fy(at[1], at[1] + 3.2, 140), "size": 64}},
    {"type": "stamp", "at": at[2] + 1.5, "dur": 2.4, "behind": True, "props": {"text": "WELD-TOGETHER", "y": 300, "size": 130}},
    {"type": "spec", "at": at[3] + 0.3, "dur": 7.2, "props": {"title": "The deal", "rows": ["Move front + rear kit", "Steel-body trucks", "Still in the box", "Free: pick up or pay shipping"], "y": max(1340, fy(at[3], at[3] + 7.2, 440)), "x": 90, "w": 900}},
    {"type": "stamp", "at": at[5] + 0.1, "dur": 3.0, "behind": True, "props": {"text": "FREE.", "y": 280, "size": 260}},
    {"type": "comment", "at": at[8] + 0.2, "dur": 3.1, "props": {"word": "BUMPERS", "handle": "you", "y": max(1340, fy(at[8], at[8] + 3.1, 140))}},
]
props = {"plate": "plate.mp4", "cutout": "cutout.webm", "captionStyle": "plain", "captions": caps, "overlays": overlays}
json.dump(props, open("tools/rival-reels/out/bumpers.props.json", "w", encoding="utf-8"), indent=1)
print(len(caps), "captions; y values", sorted(set(c["y"] for c in caps)))
print([(o["type"], round(o["at"], 2), o["props"].get("y")) for o in overlays])
