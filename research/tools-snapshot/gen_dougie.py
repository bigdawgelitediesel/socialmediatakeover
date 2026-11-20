import json
IB = "C:/Users/Parts/My Drive/VIDEO/inbox"; C = f"{IB}/A263E7B4-BD41-4CBA-864A-648B9647E806.mp4"
words = json.load(open("out/rival-raw2/A263E7B4-BD41-4CBA-864A-648B9647E806/words.json"))
V0 = 0.30                      # voice bed starts at out 0.30 (J-cut under the flash-forward)
ws = [[w["w"].strip(), round(w["s"] + V0, 2)] for w in words]
B2 = 1.395                     # two beats at 86 BPM (Teach Me How to Dougie)
t_dance = 4.9
slots = [
    {"clip": C, "in": 13.55, "dur": 0.5, "zoom": [1.0, 1.06], "zoom_ease": "out"},                 # 0.0-0.5 flash-forward: the shimmy
    {"clip": C, "in": 0.0, "dur": 4.4, "zoom": [1.10, 1.34], "zoom_anchor": 0.42},                 # 0.5-4.9 the line, pushing in on him
    {"clip": C, "in": 5.5, "dur": B2, "zoom": [1.0, 1.05], "shake": [0.0]},                         # cart dance, hit on the first beat
    {"clip": C, "in": 7.95, "dur": B2, "zoom": [1.0, 1.08], "xfade": {"type": "whip_left", "dur": 0.2}},   # the Pete
    {"clip": C, "in": 10.75, "dur": B2, "zoom": [1.0, 1.06], "xfade": {"type": "whip_right", "dur": 0.2}}, # toolboxes
    {"clip": C, "in": 13.40, "dur": 1.4, "speed": 0.5, "flash": [0.05]},                             # shimmy in half speed, shutter flash
    {"clip": C, "in": 15.80, "dur": 1.3, "zoom": [1.0, 1.10], "xfade": {"type": "whip_left", "dur": 0.2}},  # hood, far
    {"clip": C, "in": 17.20, "dur": 1.2, "zoom": [1.0, 1.06]},                                      # chains
    {"clip": C, "in": 14.30, "dur": 2.6, "zoom": [1.0, 1.07], "xfade": {"type": "fade", "dur": 0.25}},  # thumbs up, holds for the send line
]
# output timeline for captions/sfx
t = [0.0]
for i, s in enumerate(slots):
    xd = float(s.get("xfade", {}).get("dur", 0) or 0) if i else 0
    t.append(t[-1] + s["dur"] - xd)
cuts = t[1:]
print("cuts at", [round(x, 2) for x in cuts])
caps = [
    {"type": "hook", "text": "SAW A GUY HIT\nTHE DOUGIE", "accent": "DOUGIE", "start": 0.0, "end": 2.4, "pos": [540, 450]},
    {"type": "words", "words": ws, "end": round(4.6 + V0, 2), "band": True},
    {"type": "tag", "text": "BAY 2", "start": cuts[1] + 0.1, "end": cuts[2], "pos": [72, 1390]},
    {"type": "tag", "text": "THE PETE", "start": cuts[2] + 0.1, "end": cuts[3], "pos": [72, 1390]},
    {"type": "tag", "text": "TOOLBOXES", "start": cuts[3] + 0.1, "end": cuts[4], "pos": [72, 1390]},
    {"type": "tag", "text": "PARTS COUNTER", "start": cuts[4] + 0.1, "end": cuts[5], "pos": [72, 1390]},
    {"type": "tag", "text": "THE CHAINS", "start": cuts[6] + 0.1, "end": cuts[7], "pos": [72, 1390]},
    {"type": "cap", "text": "send this to the guy\nwho dances at work", "start": cuts[7] + 0.15, "end": cuts[8], "pos": [540, 1240], "band": True, "accent": "dances at work"},
    {"type": "small", "text": "@elcoyotediesel", "start": cuts[7] + 0.15, "end": cuts[8], "pos": [540, 1395]},
]
sfx = [{"kind": "click", "at": 0.13, "gain_db": -14}, {"kind": "riser", "at": cuts[1], "gain_db": -15}, {"kind": "impact", "at": cuts[1], "gain_db": -8},
       {"kind": "whoosh", "at": cuts[2], "gain_db": -11}, {"kind": "whoosh", "at": cuts[3], "gain_db": -11}, {"kind": "sub", "at": cuts[4], "gain_db": -9},
       {"kind": "whoosh", "at": cuts[5], "gain_db": -11}, {"kind": "click", "at": cuts[6], "gain_db": -12}, {"kind": "impact", "at": cuts[7], "gain_db": -12}]
e = {"name": "dougie-shop-tour", "out_dir": "C:/Users/Parts/OneDrive - Elite Diesel Service/Desktop/VIDEO/out/renders",
     "fontsdir": "C:/Users/Parts/OneDrive - Elite Diesel Service/Desktop/VIDEO/tools/fonts",
     "ambience": {"clip": C, "in": 6.0, "gain_db": -26},
     "slots": slots, "audio": [{"clip": C, "in": 0.0, "dur": 4.65, "at": V0, "clean": True, "fade": 0.06}],
     "sfx": sfx, "captions": caps}
json.dump(e, open("out/dougie-shop-tour.json", "w", encoding="utf-8"), indent=1)
print("total", round(cuts[-1], 2))
