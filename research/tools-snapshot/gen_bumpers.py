"""gen_bumpers.py - props for the Move Bumpers giveaway reel (IMG_4259, 2026-11-20).
Run after: plate rendered -> copied to tools/rival-reels/public/plate.mp4 -> watch.py on the plate -> facetrack.py.
Plain shadow captions (the @chandlerintelligence rule), words behind the head in the empty sky, cards placed off the face."""
import json, sys
sys.path.insert(0, "tools"); import layout
WATCH = "out/bumpers-watch/bumpers-plate-NOCAP/words.json"
FACE = "tools/rival-reels/out/bumpers.face.json"
words = json.load(open(WATCH, encoding="utf-8"))
tr = layout.load(FACE)

# captions: 1-3 words, break on punctuation, on gaps > 0.4 s and at 3 words; zero gaps between consecutive captions
caps, cur = [], []
def flush(nxt_start=None):
    global cur
    if not cur: return
    s = cur[0]["s"]; e = cur[-1]["e"] + 0.25
    if nxt_start is not None: e = min(max(e, nxt_start), nxt_start)
    caps.append({"text": " ".join(w["w"].strip() for w in cur), "start": round(s, 2), "end": round(e, 2)})
    cur = []
for i, w in enumerate(words):
    cur.append(w)
    txt = w["w"].strip()
    gap = (words[i + 1]["s"] - w["e"]) if i + 1 < len(words) else 9
    if txt.endswith((".", ",", "?", "!")) or gap > 0.4 or len(cur) == 3:
        flush(words[i + 1]["s"] if (i + 1 < len(words) and gap <= 0.4) else None)
flush()
# accent words (one coral box max per caption)
ACC = {"free": None, "steel": "steel", "box": "box", "dm": "DM", "front": "front", "rear": "rear", "shipping": "shipping"}
for c in caps:
    for k, v in ACC.items():
        if v and k in c["text"].lower().split() or (v and any(t.strip(".,").lower() == k for t in c["text"].split())):
            c["accent"] = v; break
ys = layout.caption_ys(tr, [(c["start"], c["end"]) for c in caps])
for c, y in zip(caps, ys): c["y"] = 1150 if y == layout.BELOW_Y else 400

# segment map (plate_at of each kept segment) to place cards on the spoken beats
seg = json.load(open("out/bumpers-segmap.json"))
at = {i: s["plate_at"] for i, s in enumerate(seg)}
def fy(t0, t1, h): return layout.card_zone(tr, t0, t1, card_h=h)[0]

overlays = [
    {"type": "kinetic", "at": 0.15, "dur": 3.4, "behind": True, "props": {"words": ["FREE", "BUMPERS"], "y": 260, "size": 190, "align": "right", "pad": 40, "accent": "FREE"}},
    {"type": "tooltag", "at": at[1] + 0.05, "dur": 3.2, "props": {"icon": "cards/movebumpers-logo.png", "iconW": 400, "iconH": 36, "pill": True, "name": "Bumpers", "y": fy(at[1], at[1] + 3.2, 140), "size": 64}},
    {"type": "stamp", "at": at[2] + 1.5, "dur": 2.4, "behind": True, "props": {"text": "WELD-TOGETHER", "y": 300, "size": 130}},
    {"type": "spec", "at": at[3] + 0.3, "dur": 7.2, "props": {"title": "The deal", "rows": ["Move front + rear kit", "Steel-body trucks", "Still in the box", "Free: pick up or pay shipping"], "y": fy(at[3], at[3] + 7.2, 440), "x": 90, "w": 900}},
    {"type": "stamp", "at": at[5] + 0.1, "dur": 3.0, "behind": True, "props": {"text": "FREE.", "y": 280, "size": 260}},
    {"type": "comment", "at": at[8] + 0.2, "dur": 3.1, "props": {"word": "BUMPERS", "handle": "you", "y": fy(at[8], at[8] + 3.1, 140)}},
]
props = {"plate": "plate.mp4", "cutout": "cutout.webm", "captionStyle": "plain", "captions": caps, "overlays": overlays}
json.dump(props, open("tools/rival-reels/out/bumpers.props.json", "w", encoding="utf-8"), indent=1)
print(len(caps), "captions; y values", sorted(set(c["y"] for c in caps)))
print([(o["type"], round(o["at"], 2), o["props"].get("y")) for o in overlays])
