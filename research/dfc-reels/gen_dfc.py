"""gen_dfc.py - batch: landscape interview -> N vertical DFC reels.
usage: python -I out/dfc/gen_dfc.py out/dfc/reels.json [slug ...]   (run from the VIDEO folder)

reels.json:
{
 "source": "C:/Users/Parts/My Drive/VIDEO/DFC/C8429.MP4", "track": "out/dfc/track.json", "fps": 24,
 "deliver_dir": "C:/Users/Parts/My Drive/VIDEO/DFC", "date": "2026-11-21",
 "people": {"left": {"name": "...", "title": "..."}, "right": {"name": "...", "title": "..."}},
 "reels": [ {"n": 1, "slug": "...", "folder": "...", "hook": ["WORD", "WORD"], "accent": "WORD",
             "keep": [[t0, t1], ...], "quote": {"text": "...", "at": 12.0, "dur": 4.0}, "caption": "...", "notes": "..."} ]
}
Per reel: EDL (crop follows the active speaker, cut on speaker change) -> build_reel3 plate (24 fps) -> Whisper on the plate ->
face track -> props (badge, hook, lower thirds, plain captions, optional quote) -> Remotion (REMOTION_BRAND=dfc) -> mux -> QA -> DFC folder."""
import json, os, subprocess, sys, shutil, glob
V = os.getcwd()
PY = sys.executable
BIN = os.path.join(os.environ["LOCALAPPDATA"], r"Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin")
FF, FP = os.path.join(BIN, "ffmpeg.exe"), os.path.join(BIN, "ffprobe.exe")
RR = os.path.join(V, "tools", "rival-reels")
sys.path.insert(0, os.path.join(V, "tools")); import layout

spec = json.load(open(sys.argv[1], encoding="utf-8"))
only = set(a for a in sys.argv[2:] if not a.startswith("--"))
SRC, FPS, DATE = spec["source"], int(spec.get("fps", 24)), spec["date"]
PW, PH = 1080, int(spec.get("plate_h", 1920)); BAND = 1920 - PH          # title band on top, plate below it
SCALE_P = PH / 1080                                                       # plate pixels per source pixel
track = json.load(open(spec["track"]))
TW, TH = track["w"], track["h"]
SCALE = PH / TH; CROP_RANGE = TW * SCALE - 1080          # x travel of the 9:16 window over the scaled frame
samples = track["samples"]

def sh(cmd, cwd=None, env=None, quiet=True):
    r = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace", shell=isinstance(cmd, str))
    if r.returncode != 0:
        print(r.stdout[-3000:]); print(r.stderr[-3000:]); raise SystemExit(f"FAILED: {cmd if isinstance(cmd, str) else ' '.join(cmd)}")
    return r.stdout

import bisect
_sample_t = [s["t"] for s in samples]
MIN_FACE_W = 100
def faces_at(t):
    """faces at source time t: look the sample up by its own timestamp (the file's "hz" was wrong once: the tracker
    steps whole frames, so 23.976/2 = 11.99 Hz was labelled 10 Hz and every crop read a face from the wrong moment)."""
    if not samples: return []
    i = bisect.bisect_left(_sample_t, t)
    if i >= len(samples): i = len(samples) - 1
    elif i > 0 and abs(_sample_t[i - 1] - t) < abs(_sample_t[i] - t): i -= 1
    # drop the bystanders: the two speakers are 150-300 px wide at 1920, passers-by in the aisle are 40-70 px and once
    # pulled the "left" crop onto the crowd (reel 19, 2026-11-21)
    return sorted((f for f in samples[i]["faces"] if f[2] >= MIN_FACE_W), key=lambda f: f[0])

LAST = {}   # last accepted face centre per side inside the current keep window (reset by sub_slots)
def face_cx_at(t, side):
    """centre x of the declared speaker's face at source time t. The two speakers are the two LARGEST faces (a bystander
    walking up the aisle is third); left/right by position among those two. With one face only, accept it when it sits
    near the side's last known position, otherwise treat it as a tracker drop-out (YuNet loses Troy for a frame or two
    and the single face is the other man; reel 8 at 40 s swung onto the interviewer's chest, 2026-11-21)."""
    fs = faces_at(t)
    if not fs: return None
    if len(fs) >= 2:
        two = sorted(sorted(fs, key=lambda f: -f[2])[:2], key=lambda f: f[0])
        f = two[0] if side == "left" else two[1]
    else:
        f = fs[0]
        cx = f[0] + f[2] / 2
        if LAST.get(side) is not None and abs(cx - LAST[side]) > 350: return None
    cx = f[0] + f[2] / 2; LAST[side] = cx
    return cx

def crop_x_for(cx): return max(0.0, min(1.0, (cx * SCALE - 540) / CROP_RANGE))

def sub_slots(t0, t1, side, jump=170, hold=0.6):
    """split [t0,t1] into windows with a stable crop; a new window starts (with an eased glide) when the face
    has moved more than `jump` source px for at least `hold` s. Returns [(a, b, cx_from, cx_to)]."""
    pts = []
    LAST.clear()
    t = t0
    while t < t1:
        cx = face_cx_at(t, side)
        if cx is not None: pts.append((round(t, 2), cx))
        t += 0.1
    if not pts: return [(t0, t1, TW / 2, TW / 2)]
    out, a, ref, moved_since = [], t0, pts[0][1], None
    for (t, cx) in pts:
        if abs(cx - ref) > jump:
            if moved_since is None: moved_since = t
            elif t - moved_since >= hold:
                new_ref = sorted(c for (tt, c) in pts if moved_since <= tt <= t)[len([1 for (tt, c) in pts if moved_since <= tt <= t]) // 2]
                out.append((a, moved_since, out[-1][3] if out else ref, ref)); a, ref, moved_since = moved_since, new_ref, None
        else:
            moved_since = None
    out.append((a, t1, out[-1][3] if out else ref, ref))
    # (a, b, cx_from, cx_to): the first window is static at its own median; later ones glide from the previous cx to the new one
    fixed = []
    for i, (a, b, cfrom, cto) in enumerate(out):
        med = sorted(c for (tt, c) in pts if a <= tt <= b); med = med[len(med) // 2] if med else cto
        fixed.append((a, b, (fixed[-1][3] if fixed else med), med))
    return fixed

def build_reel(r):
    slug, n = r["slug"], r["n"]; name = f"dfc-{n:02d}-{slug}"
    out_dir = os.path.join(V, "out", "renders"); os.makedirs(out_dir, exist_ok=True)
    print(f"\n===== Reel {n}: {slug}")
    # ---- EDL
    slots, beds, segmap, t = [], [], [], 0.0
    zoom_toggle = False
    for seg in r["keep"]:
        k0, k1 = seg[0], seg[1]; side = seg[2] if len(seg) > 2 else "right"
        seg_at = t
        z = [1.0, 1.03] if not zoom_toggle else [1.06, 1.09]; zoom_toggle = not zoom_toggle
        wins = sub_slots(k0, k1, side)
        for wi, (a, b, cfrom, cto) in enumerate(wins):
            d = round(b - a, 3)
            if d < 0.3: continue
            cx0, cx1 = crop_x_for(cfrom), crop_x_for(cto)
            slot = {"clip": SRC, "in": round(a, 3), "dur": d, "zoom": z, "zoom_anchor": 0.15,
                    "crop_x": round(cx1, 4) if (wi == 0 or abs(cx1 - cx0) < 0.01) else [round(cx0, 4), round(cx1, 4)], "crop_move": 0.7}
            slots.append(slot); segmap.append({"plate_at": round(t, 3), "src_in": round(a, 3), "dur": d, "side": side}); t += d
        beds.append({"clip": SRC, "in": round(k0, 3), "dur": round(k1 - k0, 3), "at": round(seg_at, 3), "clean": "light", "fade": 0.05})
    total = t
    edl = {"name": name, "fps": FPS, "size": [PW, PH], "out_dir": out_dir, "fontsdir": os.path.join(V, "tools", "fonts"),
           "ambience": {"clip": SRC, "in": float(spec.get("ambience_in", 2.0)), "gain_db": -32}, "slots": slots, "audio": beds, "sfx": [], "captions": []}
    edl_path = os.path.join(V, "out", "dfc", f"{name}.edl.json"); json.dump(edl, open(edl_path, "w"), indent=1)
    print(f"  {len(slots)} slots, {total:.1f} s")
    # ---- plate
    plate = os.path.join(out_dir, f"{name}-NOCAP.mp4")
    if not os.path.exists(plate) or "--force" in sys.argv:
        sh([PY, "-I", os.path.join(V, "tools", "build_reel3.py"), edl_path])
    pub_plate = os.path.join(RR, "public", f"{name}.mp4"); shutil.copyfile(plate, pub_plate)
    # ---- whisper + face on the plate
    wdir = os.path.join(V, "out", "dfc", "watch-" + name)
    if not glob.glob(os.path.join(wdir, "*", "words.json")):
        sh([PY, "-I", os.path.join(V, "tools", "watch.py"), pub_plate, "--out", wdir, "--model", "medium", "--fps", "1"])
    words = json.load(open(glob.glob(os.path.join(wdir, "*", "words.json"))[0], encoding="utf-8"))
    face_json = os.path.join(RR, "out", f"{name}.face.json")
    if not os.path.exists(face_json): sh([PY, "-I", os.path.join(V, "tools", "facetrack.py"), pub_plate, face_json])
    tr = layout.load(face_json)
    # ---- captions: 1-3 words, zero gaps
    caps, cur = [], []
    FUNC = {"the", "a", "an", "of", "and", "to", "in", "on", "at", "for", "with", "that", "my", "our", "your", "his", "i", "we", "you", "they", "it", "is", "was", "or", "but", "so"}
    def flush(nxt=None):
        nonlocal cur
        if not cur: return
        s0 = cur[0]["s"]; e0 = cur[-1]["e"] + 0.25
        if nxt is not None: e0 = nxt
        caps.append({"text": " ".join(w["w"].strip() for w in cur), "start": round(s0, 2), "end": round(max(e0, s0 + 0.35), 2)}); cur = []
    for i, w in enumerate(words):
        cur.append(w)
        tok = w["w"].strip(); nxt_w = words[i + 1] if i + 1 < len(words) else None
        gap = (nxt_w["s"] - w["e"]) if nxt_w else 9
        ends_sentence = tok.endswith((".", "?", "!")); ends_clause = tok.endswith(",")
        dangling = tok.strip(".,?!").lower() in FUNC
        if ends_sentence or gap > 0.35 or (len(cur) >= 4 and not dangling) or len(cur) >= 6 or (ends_clause and len(cur) >= 2):
            flush(nxt_w["s"] if (nxt_w and gap <= 0.35) else None)
    flush()
    # merge a one-word tail into the previous caption when it is short
    merged = []
    for c in caps:
        if merged and len(c["text"].split()) == 1 and (c["end"] - c["start"]) < 0.6 and len(merged[-1]["text"].split()) < 4 and abs(merged[-1]["end"] - c["start"]) < 0.05:
            merged[-1]["text"] += " " + c["text"]; merged[-1]["end"] = c["end"]
        else: merged.append(c)
    caps = merged
    acc = [a.lower() for a in r.get("accents", [])]
    for c in caps:
        for tkn in c["text"].split():
            if tkn.strip(".,?!").lower() in acc: c["accent"] = tkn.strip(".,?!"); break
    for c in caps:
        if tr:
            fx, fy, fw, fh = layout.face_box(tr, c["start"], c["end"])
            c["y"] = int(max(1180, min(1420, BAND + fy + fh + 55)))
        else: c["y"] = 1300
    # smooth caption y: one value per reel (median) so the text does not hop
    med = sorted(c["y"] for c in caps)[len(caps) // 2] if caps else 1300
    for c in caps: c["y"] = med
    # ---- overlays
    HOOK_END = float(r.get("hook_dur", 3.0))
    fx, fy, fw, fh = layout.face_box(tr, 0, HOOK_END) if tr else (300, 450, 480, 560)
    hook_y = int(max(1200, min(1340, BAND + fy + fh + 110)))
    hook_size = int(r.get("hook_size", 150)) if len(r["hook"]) < 3 else min(84, int(r.get("hook_size", 84)))
    hook_size = min(hook_size, 100)
    overlays = [{"type": "kinetic", "at": 0.1, "dur": HOOK_END, "props": {"words": r["hook"], "accent": r.get("accent"), "y": hook_y, "size": hook_size, "align": "center", "pad": 60}}]
    caps = [c for c in caps if c["end"] > HOOK_END + 0.15]
    for c in caps:
        if c["start"] < HOOK_END + 0.15: c["start"] = round(HOOK_END + 0.15, 2)
    seen = set()
    for sgm in segmap:
        side = sgm["side"]
        if side in seen or side not in spec["people"]: continue
        seen.add(side); p = spec["people"][side]
        if p.get("lowerthird") is False: continue   # Jacob 2026-11-21: no name tag on Troy, "we know it's Troy Lake"
        at = max(sgm["plate_at"], HOOK_END + 0.4) if not seen - {side} else sgm["plate_at"]
        overlays.append({"type": "lowerthird", "at": round(at, 2), "dur": 4.0, "props": {"name": p["name"], "title": p.get("title", ""), "x": 72, "y": 300}})
    # corner logos on every DFC reel (Jacob 2026-11-21): Dynamic Diesels bottom-left, DFC lockup (white) bottom-right
    for lg in spec.get("corner_logos", []):
        overlays.append({"type": "corners", "at": 0, "dur": round(total, 2), "props": dict(lg)})
    if r.get("quote"):
        q = r["quote"]; overlays.append({"type": "quote", "at": q["at"], "dur": q["dur"], "props": {"text": q["text"]}})
    props = {"plate": f"{name}.mp4", "fps": FPS, "captionStyle": "plain", "captions": caps, "overlays": overlays}
    if BAND > 0: props["frame"] = {"top": BAND, "h": PH, "bg": "blur"}
    props_path = os.path.join(RR, "out", f"{name}.props.json"); json.dump(props, open(props_path, "w", encoding="utf-8"), indent=1)
    # ---- render + mux
    video = os.path.join(RR, "out", f"{name}-video.mp4"); final = os.path.join(RR, "out", f"{name}-final.mp4")
    env = dict(os.environ, REMOTION_BRAND="dfc")
    sh(f'npx remotion render src/index.ts RivalReel "{video}" --props="{props_path}" --codec=h264 --crf=17 --concurrency=4 --log=error', cwd=RR, env=env)   # 4 browser tabs, not 14: the machine killed the batch for memory at 14
    sh([FF, "-y", "-v", "error", "-i", video, "-i", pub_plate, "-map", "0:v:0", "-map", "1:a:0",
        "-vf", "unsharp=5:5:0.4:3:3:0.0,format=yuv420p,setparams=color_primaries=bt709:color_trc=bt709:colorspace=bt709:range=tv",
        "-c:v", "libx264", "-preset", "slow", "-profile:v", "high", "-level", "4.2", "-crf", "17", "-maxrate", "16M", "-bufsize", "32M",
        "-g", str(FPS), "-keyint_min", str(FPS), "-sc_threshold", "0", "-bf", "2",
        "-x264-params", "aq-mode=3:aq-strength=0.9:psy-rd=1.0,0.15:deblock=-1,-1:no-open-gop=1:colorprim=bt709:transfer=bt709:colormatrix=bt709",
        "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-color_range", "tv",
        "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", final])
    qa = sh([PY, "-I", os.path.join(V, "tools", "smooth_check.py"), final])
    qa_lines = [l for l in qa.splitlines() if "held" in l or "spikes" in l or "fps" in l]
    tags = sh([FP, "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=r_frame_rate,color_space,color_transfer,color_primaries,duration", "-of", "csv=p=0", final]).strip()
    sheet = os.path.join(RR, "out", f"{name}-sheet.png")
    sh([FF, "-y", "-v", "error", "-i", final, "-vf", "fps=1,scale=270:480,tile=8x8:padding=2:margin=2", "-frames:v", "1", "-update", "1", sheet])
    print("  QA:", " | ".join(qa_lines)); print("  tags:", tags)
    # ---- deliver
    folder = os.path.join(spec["deliver_dir"], f"{r['folder']} - completed {DATE}")
    os.makedirs(folder, exist_ok=True)
    shutil.copyfile(final, os.path.join(folder, f"{DATE} DFC {n:02d} {r['folder']} - POST THIS.mp4"))
    shutil.copyfile(plate, os.path.join(folder, f"{DATE} DFC {n:02d} {r['folder']} - alt no captions.mp4"))
    open(os.path.join(folder, "README - posting kit.txt"), "w", encoding="utf-8").write(
        f"{DATE}  DFC REEL {n:02d}: {r['folder'].upper()}  ({total:.0f} s, 1080x1920, {FPS} fps, source C8429.MP4 {r['keep'][0][0]:.0f}s to {r['keep'][-1][1]:.0f}s)\n"
        + "=" * 90 + "\n\nWHAT IT IS\n" + r.get("notes", "") + "\n\nCAPTION\n" + r.get("caption", "") + "\n\n"
        "HOW TO POST\nUpload at highest quality, no in-app trim or filters. Song optional at 10 percent under his voice or none at all.\n"
        "Alt file has no captions or graphics if you want to run CapCut text instead.\n")
    print("  delivered:", folder)
    return {"n": n, "slug": slug, "total": round(total, 1), "folder": folder, "qa": qa_lines, "tags": tags}

results = []
for r in spec["reels"]:
    if only and r["slug"] not in only: continue
    results.append(build_reel(r))
json.dump(results, open(os.path.join(V, "out", "dfc", "results.json"), "w"), indent=1)
print("\nDONE", len(results), "reels")
