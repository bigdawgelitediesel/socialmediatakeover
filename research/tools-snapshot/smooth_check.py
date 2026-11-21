"""smooth_check.py - frame-pacing QA for a finished reel (answers "is it choppy?").
usage: python -I tools/smooth_check.py <reel.mp4> [more.mp4 ...]
Reports: constant frame rate, held/duplicated frames away from cuts (judder), skipped-frame spikes, cut list,
and a strobe score per shot (mean motion per frame with no blur = fast-shutter strobing -> use "mblur": true on that slot).
Method: per-frame mean absolute difference at 90x160 (grain averaged out), windows that straddle a cut are ignored."""
import os, re, subprocess, sys, statistics, tempfile
BIN = os.path.join(os.environ["LOCALAPPDATA"], r"Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin")
FF, FP = os.path.join(BIN, "ffmpeg.exe"), os.path.join(BIN, "ffprobe.exe")

def curve(path):
    with tempfile.TemporaryDirectory() as td:   # metadata=print:file= cannot take a drive-colon path, so run inside td
        subprocess.run([FF, "-v", "error", "-i", os.path.abspath(path), "-vf",
                        "scale=90:160:flags=area,gblur=sigma=1.5,format=gray,tblend=all_mode=difference,signalstats,metadata=print:key=lavfi.signalstats.YAVG:file=c.txt",
                        "-an", "-f", "null", "-"], cwd=td, check=True)
        txt = open(os.path.join(td, "c.txt")).read()
    return [(float(a), float(b)) for a, b in re.findall(r"pts_time:([0-9.]+)\s+lavfi.signalstats.YAVG=([0-9.]+)", txt)]

def check(path):
    fr = subprocess.run([FP, "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=r_frame_rate,avg_frame_rate",
                         "-of", "csv=p=0", path], capture_output=True, text=True).stdout.strip()
    d = curve(path); cuts = [t for t, v in d if v > 22]
    held, spikes = [], []
    for i in range(3, len(d) - 3):
        t, v = d[i]; nb = [d[j][1] for j in range(i - 3, i + 4) if j != i]
        if max(nb) > 18 or v > 18: continue      # cut frames and windows touching a cut
        m = statistics.median(nb)
        if m > 0.5 and v < 0.22 * m: held.append(round(t, 2))   # a real duplicate sits at the grain floor (ratio ~0.1); 0.3 is a natural pause
        if m > 0.6 and v > 3.2 * m: spikes.append(round(t, 2))
    # strobe score per shot: mean motion between cuts; > 3.5 with sharp edges reads as strobing on a phone
    bounds = [0.0] + cuts + [d[-1][0]]; shots = []
    for a, b in zip(bounds, bounds[1:]):
        seg = [v for t, v in d if a < t < b and v < 18]
        if len(seg) > 6: shots.append((a, b, statistics.mean(seg)))
    print(f"\n== {os.path.basename(path)}  fps {fr}  frames {len(d) + 1}")
    print(f"   held frames (judder): {held or 'none'}")
    print(f"   skipped-frame spikes: {spikes or 'none'}")
    print("   cuts at: " + " ".join(f"{c:.2f}" for c in cuts))
    for a, b, m in shots:
        flag = "  <- fast motion: use mblur on this slot" if m > 3.5 else ""
        print(f"   shot {a:6.2f}-{b:6.2f}  motion/frame {m:5.2f}{flag}")

for p in sys.argv[1:]: check(p)
