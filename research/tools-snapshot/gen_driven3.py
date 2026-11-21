import json, sys
sys.path.insert(0, "tools"); import layout
tr = layout.load("tools/rival-reels/out/driven-v2.face.json")
e = json.load(open("tools/rival-reels/out/driven-v2.props.json", encoding="utf-8"))
e["cutout"] = "cutout.webm"
ys = layout.caption_ys(tr, [(c["start"], c["end"]) for c in e["captions"]])
for c, y in zip(e["captions"], ys): c["y"] = y
for o in e["overlays"]:
    if o["type"] == "kinetic":
        o["behind"] = True; o["props"].update({"y": 300, "size": 168, "align": "center", "pad": 40})
    elif o["type"] in ("logo", "photo", "strike", "comment"):
        y, zone = layout.card_zone(tr, o["at"], o["at"] + o["dur"], card_h=420 if o["type"] != "photo" else 560)
        o["props"]["y"] = y
    elif o["type"] == "stamp":
        o["behind"] = True; o["props"].update({"y": 330, "size": 150})
json.dump(e, open("tools/rival-reels/out/driven-v3.props.json", "w", encoding="utf-8"), indent=1)
print("caption y values:", sorted(set(c["y"] for c in e["captions"])))
print([(o["type"], o["props"].get("y"), o.get("behind", False)) for o in e["overlays"]])
