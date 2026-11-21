import json
IB = "C:/Users/Parts/My Drive/VIDEO/inbox"; J = f"{IB}/IMG_4252.MOV"
D33 = f"{IB}/Video_262672_DJI_20261115132016_0033_D_MP4_141790265_34000_20261115132856_video_original.mp4"
words = json.load(open("out/rival-raw2/IMG_4252/words.json"))
segs = [("A", 0.56, 5.90, 0.00), ("B", 6.78, 11.00, 5.40), ("C", 12.52, 13.35, 9.70), ("D", 16.86, 17.74, 10.60),
        ("E", 24.18, 29.50, 11.60), ("F1", 34.18, 36.60, 17.00), ("F2", 38.88, 42.86, 19.50), ("G", 43.44, 47.30, 23.55), ("H", 57.30, 60.10, 27.50)]
beds = [{"clip": J, "in": s0, "dur": round(s1 - s0, 3), "at": o0, "clean": "light", "fade": 0.06} for _, s0, s1, o0 in segs]
allwords = []
for name, s0, s1, o0 in segs:
    for w in words:
        if s0 - 0.05 <= w["s"] < s1 - 0.02:
            t = round(w["s"] - s0 + o0, 2)
            if name == "A" and t < 0.05: continue
            if name == "B" and w["w"].strip().lower() == "aka": continue
            allwords.append([w["w"].strip(), t])
# talking head only, alternating framings on every sentence; two b-roll inserts
slots = [
    {"clip": J, "in": 0.56, "dur": 2.7, "zoom": [1.0, 1.04], "zoom_anchor": 0.3},
    {"clip": J, "in": 3.26, "dur": 2.7, "zoom": [1.16, 1.18], "zoom_anchor": 0.3},
    {"clip": J, "in": 6.78, "dur": 2.3, "zoom": [1.0, 1.03], "zoom_anchor": 0.3},
    {"clip": f"{IB}/IMG_3856.MOV", "in": 0.3, "dur": 2.0, "zoom": [1.0, 1.08]},                # "Project Rival" -> the truck
    {"clip": J, "in": 12.52, "dur": 0.9, "zoom": [1.16, 1.18], "zoom_anchor": 0.3},
    {"clip": J, "in": 16.86, "dur": 1.0, "zoom": [1.0, 1.03], "zoom_anchor": 0.3},
    {"clip": J, "in": 24.18, "dur": 3.3, "zoom": [1.16, 1.19], "zoom_anchor": 0.3},
    {"clip": D33, "in": 12.2, "dur": 2.1, "zoom": [1.0, 1.06]},                                  # "fuel system" -> steam
    {"clip": J, "in": 34.18, "dur": 2.5, "zoom": [1.0, 1.04], "zoom_anchor": 0.3},
    {"clip": J, "in": 38.88, "dur": 4.05, "zoom": [1.16, 1.19], "zoom_anchor": 0.3},
    {"clip": J, "in": 43.44, "dur": 3.95, "zoom": [1.0, 1.04], "zoom_anchor": 0.3},
    {"clip": J, "in": 57.30, "dur": 3.4, "zoom": [1.16, 1.2], "zoom_anchor": 0.3},
]
e = {"name": "driven-v2-plate", "out_dir": "C:/Users/Parts/OneDrive - Elite Diesel Service/Desktop/VIDEO/out/renders",
     "fontsdir": "C:/Users/Parts/OneDrive - Elite Diesel Service/Desktop/VIDEO/tools/fonts",
     "ambience": {"clip": f"{IB}/IMG_3773.MOV", "in": 20.0, "gain_db": -30},
     "slots": slots, "audio": beds, "sfx": [], "captions": []}
json.dump(e, open("out/driven-v2-plate.json", "w", encoding="utf-8"), indent=1)
json.dump({"words": allwords, "total": round(sum(s["dur"] for s in slots), 2)}, open("out/driven-v2-words.json", "w"), indent=0)
print("total", round(sum(s["dur"] for s in slots), 2), "words", len(allwords))
