"""layout.py - face-aware placement for captions and cards (the @viashaan rule: track the face, know the IG UI).
Reads a face track [[t,x,y,w,h],...] (YuNet, 10 samples/s) and returns safe y positions."""
import json
IG_TOP, IG_BOTTOM_TEXT, PILL_H = 290, 1440, 90   # nothing above 290; caption pills must end above 1440 (IG caption block starts ~1520)

def load(path): return [r for r in json.load(open(path)) if r[1] is not None]

def face_box(track, t0, t1):
    rows = [r for r in track if t0 <= r[0] <= t1] or track[:1]
    xs = sorted(r[1] for r in rows); ys = sorted(r[2] for r in rows); ws = sorted(r[3] for r in rows); hs = sorted(r[4] for r in rows)
    m = len(rows) // 2
    return xs[m], ys[m], ws[m], hs[m]

BELOW_Y, ABOVE_Y = 1230, 400   # two fixed bands so captions do not wander frame to frame

def caption_band(track, t0, t1, margin=70):
    """'below' when the chin leaves room for a pill above the IG caption block, else 'above'."""
    x, y, w, h = face_box(track, t0, t1)
    return "below" if y + h + margin + PILL_H <= IG_BOTTOM_TEXT else "above"

def caption_ys(track, windows, margin=70):
    """Band per caption with hysteresis: only switch bands when the next two captions agree."""
    bands = [caption_band(track, a, b, margin) for a, b in windows]
    out, cur = [], bands[0] if bands else "below"
    for i, b in enumerate(bands):
        if b != cur and all(x == b for x in bands[i:i + 2]): cur = b
        out.append(BELOW_Y if cur == "below" else ABOVE_Y)
    return out

def caption_y(track, t0, t1, default=1230, margin=70):
    return BELOW_Y if caption_band(track, t0, t1, margin) == "below" else ABOVE_Y

def card_zone(track, t0, t1, card_h=420):
    """Return (y, zone) for a card: 'below' the chin if it fits above 1700, else 'above' the hat, else 'low' (y=1330)."""
    x, y, w, h = face_box(track, t0, t1)
    if y + h + 60 + card_h <= 1700: return int(y + h + 60), "below"
    if y - 60 - card_h >= IG_TOP: return int(y - 60 - card_h), "above"
    return 1330, "low"

if __name__ == "__main__":
    import sys
    tr = load(sys.argv[1]); print("face rows", len(tr), "example box @2s", face_box(tr, 1.8, 2.2), "caption y", caption_y(tr, 1.8, 2.2), "card", card_zone(tr, 1.8, 2.2))
