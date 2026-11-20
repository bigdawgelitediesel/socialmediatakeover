"""
watch.py  -  turn a video into things Claude can take in.

usage:  python -I watch.py <video> [--out DIR] [--model small|medium] [--no-whisper] [--fps N]

Produces, in <out>/<clipname>/:
  info.txt           duration, resolution, fps, audio
  scenes.csv         every shot change with timecodes (PySceneDetect)
  shots/shot-NNN.jpg one frame per detected shot
  sheet-NN.jpg       contact sheets (tiles with burned-in timestamps) for a timeline scan
  transcript.txt     [mm:ss.s -> mm:ss.s] text   (faster-whisper, word timestamps kept in words.json)
  words.json         word-level timestamps for captioning
"""
import sys, os, json, subprocess, csv, math, argparse, time

FF = os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin")
FFMPEG, FFPROBE = os.path.join(FF, "ffmpeg.exe"), os.path.join(FF, "ffprobe.exe")
SCENEDETECT = os.path.expandvars(r"%LOCALAPPDATA%\Programs\Python\Python312\Scripts\scenedetect.exe")
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", **kw)

def probe(video):
    r = run([FFPROBE, "-v", "error", "-print_format", "json", "-show_format", "-show_streams", video])
    j = json.loads(r.stdout)
    v = next((s for s in j["streams"] if s["codec_type"] == "video"), None)
    a = next((s for s in j["streams"] if s["codec_type"] == "audio"), None)
    dur = float(j["format"].get("duration", 0))
    num, den = (v["r_frame_rate"].split("/") + ["1"])[:2]
    fps = float(num) / float(den) if float(den) else 0
    rot = 0
    for sd in v.get("side_data_list", []) or []:
        if "rotation" in sd: rot = sd["rotation"]
    w, h = v["width"], v["height"]
    if abs(rot) in (90, 270): w, h = h, w
    return dict(duration=dur, width=w, height=h, fps=round(fps, 2), vcodec=v["codec_name"],
                audio=(a["codec_name"] if a else None), orientation=("vertical" if h > w else "horizontal" if w > h else "square"))

def ts(s):
    m, s = divmod(s, 60); return "%02d:%04.1f" % (m, s)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video"); ap.add_argument("--out", default=None)
    ap.add_argument("--model", default="small"); ap.add_argument("--no-whisper", action="store_true")
    ap.add_argument("--fps", type=float, default=None, help="contact-sheet sampling rate (default auto)")
    a = ap.parse_args()
    video = os.path.abspath(a.video)
    name = os.path.splitext(os.path.basename(video))[0]
    out = os.path.join(a.out or os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "out"), name)
    os.makedirs(os.path.join(out, "shots"), exist_ok=True)

    info = probe(video)
    with open(os.path.join(out, "info.txt"), "w") as f:
        for k, v in info.items(): f.write(f"{k}: {v}\n")
    print("INFO", info)

    # 1. scenes + one frame per shot
    t0 = time.time()
    r = run([SCENEDETECT, "-i", video, "-o", out, "detect-adaptive", "list-scenes", "-f", "scenes.csv", "-q",
             "save-images", "-n", "1", "-o", os.path.join(out, "shots"), "-f", "shot-$SCENE_NUMBER", "-W", "960"])
    scenes = []
    p = os.path.join(out, "scenes.csv")
    if os.path.exists(p):
        with open(p) as f:
            rows = list(csv.reader(f))
        hdr = next(i for i, row in enumerate(rows) if row and row[0] == "Scene Number")
        for row in rows[hdr + 1:]:
            if len(row) >= 7: scenes.append((int(row[0]), float(row[3]), float(row[6])))
    print(f"SCENES {len(scenes)} shots in {time.time()-t0:.1f}s")
    for n, s, e in scenes: print(f"  shot {n:03d}  {ts(s)} -> {ts(e)}  ({e-s:.1f}s)")

    # 2. contact sheets: one tile every N seconds, 5x4 per sheet, timestamp burned in
    dur = info["duration"]
    step = a.fps and (1 / a.fps) or max(1.0, round(dur / 60, 1))   # ~60 tiles max by default
    tiles = int(math.ceil(dur / step))
    sheets = int(math.ceil(tiles / 20))
    tw = 384 if info["orientation"] != "vertical" else 216
    vf = (f"fps=1/{step},scale={tw}:-2,"
          f"drawtext=fontfile='C\:/Windows/Fonts/arial.ttf':text='%{{pts\:hms}}':x=6:y=6:fontsize=20:fontcolor=white:box=1:boxcolor=black@0.6:boxborderw=4,"
          f"tile=5x4")
    r = run([FFMPEG, "-y", "-loglevel", "error", "-i", video, "-vf", vf, "-q:v", "3",
             os.path.join(out, "sheet-%02d.jpg")])
    if r.returncode: print("sheet error:", r.stderr[-400:])
    print(f"SHEETS {sheets} sheet(s), one tile every {step}s")

    # 3. transcript
    if not a.no_whisper and info["audio"]:
        t0 = time.time()
        from faster_whisper import WhisperModel
        m = WhisperModel(a.model, device="cpu", compute_type="int8")
        segs, _ = m.transcribe(video, word_timestamps=True, vad_filter=True)
        words, lines = [], []
        for s in segs:
            lines.append(f"[{ts(s.start)} -> {ts(s.end)}] {s.text.strip()}")
            for w in (s.words or []): words.append(dict(w=w.word, s=round(w.start, 2), e=round(w.end, 2)))
        open(os.path.join(out, "transcript.txt"), "w", encoding="utf-8").write("\n".join(lines) or "(no speech detected)")
        json.dump(words, open(os.path.join(out, "words.json"), "w"))
        print(f"TRANSCRIPT {len(lines)} segments in {time.time()-t0:.1f}s")
        for l in lines[:40]: print("  " + l)
        if len(lines) > 40: print(f"  ... {len(lines)-40} more in transcript.txt")
    print("OUT", out)

if __name__ == "__main__":
    main()
