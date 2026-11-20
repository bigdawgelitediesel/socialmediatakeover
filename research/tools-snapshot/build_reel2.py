"""build_reel2.py - render a 9:16 reel from an EDL with transitions, slow motion,
punch-ins, stabilization, word-timed (karaoke) captions and real audio.

usage: python -I build_reel2.py edl.json

EDL JSON (all times in seconds):
{
  "name": "harley-trade", "out_dir": "C:/.../out",
  "size": [1080, 1920], "fps": 30,
  "fontsdir": "C:/.../tools/fonts",
  "styles": { "Hook": {...}, "Cap": {...} },        # optional overrides of the ASS styles below
  "slots": [
    { "clip": "...", "in": 1.0, "dur": 2.5,
      "speed": 0.5,                 # <1 slow motion (optical-flow minterpolate), >1 fast. dur = OUTPUT seconds
      "zoom": [1.0, 1.12],          # punch-in from scale a to b across the slot (crop-expression keyframe)
      "stab": true,                 # two-pass vidstab stabilization
      "xfade": {"type": "fade", "dur": 0.4},   # transition INTO this slot (default hard cut)
      "grade": "warm"               # optional named grade (see GRADES)
    }, ...
  ],
  "audio": [ {"clip": "...", "in": 51.6, "dur": 2.0, "at": 0.4, "gain_db": 0} ],   # source-audio beds on the output timeline; empty = silent
  "loudnorm": true,
  "captions": [
    {"style": "Hook", "text": "what'd you pay for that truck?", "start": 0.0, "end": 2.6},
    {"style": "Cap",  "text": "...", "start": 4.0, "end": 6.0, "pos": [540, 1250]},
    {"style": "Sub",  "words": [["I", 3.0], ["traded", 3.3], ...], "end": 6.1}   # karaoke, each word = [text, start]
  ]
}
Outputs <name>.mp4 (+ -NOCAP.mp4 without captions, for CapCut) and <name>-sheet.jpg.
"""
import json, os, subprocess, sys, tempfile, shutil

BIN = os.path.join(os.environ["LOCALAPPDATA"], r"Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin")
FF = os.path.join(BIN, "ffmpeg.exe")
FP = os.path.join(BIN, "ffprobe.exe")

GRADES = {
    # mild contrast + warmth; keep it subtle so it still looks like a phone video
    "warm": "eq=contrast=1.06:saturation=1.08,colorbalance=rs=0.03:bs=-0.03",
    "punch": "eq=contrast=1.10:saturation=1.12",
    "none": "null",
}

DEFAULT_STYLES = {
    # name: font, size, primary, secondary, outline_colour, back (shadow), outline px, shadow px, bold, align, marginV
    # ASS colours are &HAABBGGRR (AA = 00 opaque .. FF transparent). Clean look: thin semi-transparent outline + soft shadow.
    "Hook": dict(font="Montserrat ExtraBold", size=84, primary="&H00FFFFFF", secondary="&H00FFFFFF",
                 outline_colour="&H5A000000", back="&H8C000000", outline=2.5, shadow=1.5, bold=0, align=5, marginv=0),
    "Cap":  dict(font="Montserrat SemiBold", size=64, primary="&H00FFFFFF", secondary="&H00FFFFFF",
                 outline_colour="&H5A000000", back="&H8C000000", outline=2.2, shadow=1.5, bold=0, align=2, marginv=600),
    "Sub":  dict(font="Montserrat SemiBold", size=62, primary="&H00FFFFFF", secondary="&H00C8C8C8",
                 outline_colour="&H5A000000", back="&H8C000000", outline=2.2, shadow=1.5, bold=0, align=2, marginv=600),
    "Small": dict(font="Montserrat SemiBold", size=36, primary="&H00E6E6E6", secondary="&H00E6E6E6",
                 outline_colour="&H5A000000", back="&H8C000000", outline=1.5, shadow=1, bold=0, align=2, marginv=470),
}


def run(cmd, quiet=True, cwd=None):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=cwd)
    if r.returncode != 0:
        print(" ".join(cmd)); print(r.stderr[-4000:]); sys.exit(1)
    return r


_HDR_CACHE = {}
def is_hdr(clip):
    """True for HLG / PQ sources (iPhone Dolby Vision 8.4 records HLG, arib-std-b67)."""
    if clip in _HDR_CACHE: return _HDR_CACHE[clip]
    r = subprocess.run([FP, "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=color_transfer,color_primaries",
                        "-of", "csv=p=0", clip], capture_output=True, text=True)
    out = (r.stdout or "").lower()
    hdr = ("arib-std-b67" in out) or ("smpte2084" in out) or ("bt2020" in out)
    _HDR_CACHE[clip] = hdr
    return hdr

# libplacebo spline tone map (HLG/PQ BT.2020 -> BT.709 SDR). Tested 2026-11-20 on the iPhone HLG clips:
# naive yuv420p conversion = washed out and wrong hue; spline = natural. Runs faster than realtime on the UHD 770.
TONEMAP = "libplacebo=tonemapping=spline:colorspace=bt709:color_primaries=bt709:color_trc=bt709:range=tv:format=yuv420p"


def ass_time(t):
    t = max(0.0, t); h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def ass_escape(t):
    return t.replace("\\", "\\\\").replace("{", "\\{").replace("}", "\\}").replace("\n", "\\N")


def write_ass(path, W, H, styles, captions):
    lines = ["[Script Info]", "ScriptType: v4.00+", f"PlayResX: {W}", f"PlayResY: {H}", "WrapStyle: 0",
             "ScaledBorderAndShadow: yes", "", "[V4+ Styles]",
             "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, "
             "Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding"]
    for name, s in styles.items():
        lines.append(f"Style: {name},{s['font']},{s['size']},{s['primary']},{s['secondary']},{s['outline_colour']},{s['back']},"
                     f"{s['bold']},0,0,0,100,100,0,0,1,{s['outline']},{s['shadow']},{s['align']},80,80,{s['marginv']},1")
    lines += ["", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
    for c in captions:
        st = c.get("style", "Cap")
        tags = ""
        if "pos" in c:
            tags += "\\pos(%d,%d)" % tuple(c["pos"])
        fade_in = int(c.get("fade_in", 0) * 1000); fade_out = int(c.get("fade_out", 0) * 1000)
        if fade_in or fade_out:
            tags += f"\\fad({fade_in},{fade_out})"
        if c.get("pop"):
            # scale pop-in: 80% -> 100% over 120 ms
            tags += "\\fscx84\\fscy84\\t(0,120,\\fscx100\\fscy100)"
        if "words" in c:
            words = c["words"]; start = words[0][1]; end = c["end"]
            parts = []
            for i, (w, s0) in enumerate(words):
                s1 = words[i + 1][1] if i + 1 < len(words) else end
                parts.append("{\\k%d}%s" % (max(1, round((s1 - s0) * 100)), ass_escape(w)))
            text = " ".join(parts)
        else:
            start, end, text = c["start"], c["end"], ass_escape(c["text"])
        text = ("{" + tags + "}" if tags else "") + text
        lines.append(f"Dialogue: 0,{ass_time(start)},{ass_time(end)},{st},,0,0,0,,{text}")
    with open(path, "w", encoding="utf-8-sig") as f:
        f.write("\n".join(lines) + "\n")


def render_slot(i, s, W, H, fps, tmp):
    """Normalise one slot to a WxH, fps, yuv420p intermediate of exactly s['dur'] output seconds."""
    out = os.path.join(tmp, f"slot{i:02d}.mp4")
    speed = float(s.get("speed", 1.0))
    dur_out = float(s["dur"])
    dur_src = dur_out * speed
    vf = [f"scale={W}:{H}:force_original_aspect_ratio=increase", f"crop={W}:{H}", "setsar=1"]
    if is_hdr(s["clip"]):
        vf.insert(0, TONEMAP)
        print("   HDR source -> tone mapped to BT.709")
    src_in = float(s["in"])
    stab = s.get("stab")
    if stab:
        # pass 1: analyse the exact segment
        trf = f"slot{i:02d}.trf"   # relative; ffmpeg runs with cwd=tmp so no drive-colon escaping
        run([FF, "-y", "-v", "error", "-ss", f"{src_in:.3f}", "-t", f"{dur_src + 0.5:.3f}", "-i", s["clip"],
             "-vf", f"vidstabdetect=shakiness=5:accuracy=15:result={trf}",
             "-f", "null", "-"], cwd=tmp)
        vf.insert(0, f"vidstabtransform=input={trf}:zoom=3:smoothing=20:interpol=bicubic,unsharp=5:5:0.4:3:3:0.0")
    z = s.get("zoom")
    if z:
        a, b = float(z[0]), float(z[1])
        # linear keyframe from scale a to b over the slot; crop expression uses output time t
        expr = f"({a}+({b}-{a})*min(t/{dur_out:.3f},1))"
        vf += [f"crop=w='iw/{expr}':h='ih/{expr}':x='(iw-ow)/2':y='(ih-oh)/2'", f"scale={W}:{H}", "setsar=1"]
    grade = GRADES.get(s.get("grade", "none"), "null")
    if grade != "null":
        vf.append(grade)
    if abs(speed - 1.0) > 1e-3:
        if speed < 1.0:
            # optical-flow interpolation: synthesise the in-between frames, then stretch
            target_fps = fps / speed
            vf += [f"minterpolate=fps={target_fps:.3f}:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1",
                   f"setpts={1/speed:.4f}*PTS"]
        else:
            vf += [f"setpts={1/speed:.4f}*PTS"]
    vf += [f"fps={fps}", "format=yuv420p", f"trim=duration={dur_out:.3f}", "setpts=PTS-STARTPTS"]
    cmd = [FF, "-y", "-v", "error", "-ss", f"{src_in:.3f}", "-t", f"{dur_src + 0.6:.3f}", "-i", s["clip"],
           "-an", "-vf", ",".join(vf), "-r", str(fps), "-c:v", "libx264", "-preset", "medium", "-crf", "16",
           "-pix_fmt", "yuv420p", "-t", f"{dur_out:.3f}", out]
    run(cmd, cwd=tmp)
    # verify length; pad with the last frame if the source ran out
    d = float(run([FP, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", out]).stdout.strip() or 0)
    if d < dur_out - 0.05:
        padded = os.path.join(tmp, f"slot{i:02d}p.mp4")
        run([FF, "-y", "-v", "error", "-i", out, "-vf", f"tpad=stop_mode=clone:stop_duration={dur_out - d + 0.1:.3f},trim=duration={dur_out:.3f}",
             "-c:v", "libx264", "-preset", "medium", "-crf", "16", "-pix_fmt", "yuv420p", padded])
        out = padded
    return out


def main(edl_path):
    e = json.load(open(edl_path, encoding="utf-8"))
    W, H = e.get("size", [1080, 1920]); fps = int(e.get("fps", 30))
    name = e["name"]; out_dir = e["out_dir"]; os.makedirs(out_dir, exist_ok=True)
    fontsdir = e.get("fontsdir")
    styles = {k: dict(v) for k, v in DEFAULT_STYLES.items()}
    for k, v in e.get("styles", {}).items():
        styles.setdefault(k, dict(DEFAULT_STYLES["Cap"])).update(v)
    slots = e["slots"]
    tmp = tempfile.mkdtemp(prefix="reel2_")
    captions_only = "--captions-only" in sys.argv and os.path.exists(os.path.join(out_dir, f"{name}-NOCAP.mp4"))
    try:
        parts = []
        if captions_only:
            slots = []
        for i, s in enumerate(slots):
            print(f"slot {i+1}/{len(slots)}: {os.path.basename(s['clip'])} in={s['in']} dur={s['dur']}"
                  + (f" speed={s['speed']}" if 'speed' in s else "") + (" stab" if s.get('stab') else "") + (" zoom" if s.get('zoom') else ""))
            parts.append(render_slot(i, s, W, H, fps, tmp))

        # ---- video: chain of xfade transitions (hard cut = xfade of 0 -> use concat for those) ----
        inputs = []
        for p in parts:
            inputs += ["-i", p]
        fc = [f"[{i}:v]setsar=1,format=yuv420p,fps={fps},settb=AVTB[s{i}]" for i in range(len(parts))]
        cur = "[s0]"; cur_len = float(slots[0]["dur"]) if slots else 0.0
        for i in range(1, len(slots)):
            x = slots[i].get("xfade")
            d = float(slots[i]["dur"])
            if x and float(x.get("dur", 0)) > 0:
                xd = float(x["dur"]); off = cur_len - xd
                fc.append(f"{cur}[s{i}]xfade=transition={x.get('type','fade')}:duration={xd:.3f}:offset={off:.3f},settb=AVTB[x{i}]")
                cur_len = cur_len + d - xd
            else:
                fc.append(f"{cur}[s{i}]concat=n=2:v=1:a=0,settb=AVTB[x{i}]")
                cur_len = cur_len + d
            cur = f"[x{i}]"
        total = cur_len
        fc.append(f"{cur}format=yuv420p[vout]")

        # ---- audio: beds placed on the timeline over a silent base (amix duration=first) ----
        beds = e.get("audio", [])
        n_v = len(parts)
        fc.append(f"anullsrc=r=48000:cl=stereo,atrim=duration={total:.3f}[abase]")
        amix_in = ["[abase]"]
        for j, b in enumerate(beds):
            inputs += ["-ss", f"{float(b['in']):.3f}", "-t", f"{float(b['dur']):.3f}", "-i", b["clip"]]
            idx = n_v + j
            gain = float(b.get("gain_db", 0))
            fade = float(b.get("fade", 0.08))
            ms = int(float(b["at"]) * 1000)
            fc.append(f"[{idx}:a:0]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,asetpts=PTS-STARTPTS,"
                      f"volume={gain}dB,afade=t=in:d={fade},afade=t=out:st={float(b['dur'])-fade:.3f}:d={fade},"
                      f"adelay={ms}|{ms}[a{j}]")
            amix_in.append(f"[a{j}]")
        fc.append("".join(amix_in) + f"amix=inputs={len(amix_in)}:duration=first:normalize=0"
                  + (",loudnorm=I=-14:TP=-1.5:LRA=11" if (beds and e.get("loudnorm", True)) else "")
                  + ",aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo[aout]")

        nocap = os.path.join(out_dir, f"{name}-NOCAP.mp4")
        if captions_only:
            total = float(run([FP, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", nocap]).stdout.strip())
            print(f"captions-only: reusing {nocap} ({total:.2f}s)")
        else:
          run([FF, "-y", "-v", "error", *inputs, "-filter_complex", ";".join(fc), "-map", "[vout]", "-map", "[aout]",
             "-r", str(fps), "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-pix_fmt", "yuv420p", "-profile:v", "high",
             "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-color_range", "tv",
             "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", nocap])
          print(f"wrote {nocap} ({total:.2f}s)")

        # ---- captions: burn an ASS subtitle track ----
        caps = e.get("captions", [])
        final = os.path.join(out_dir, f"{name}.mp4")
        if caps:
            ass_path = os.path.join(out_dir, f"{name}.ass")
            write_ass(ass_path, W, H, styles, caps)
            sub = ass_path.replace("\\", "/").replace(":", "\\:")
            vf = f"ass='{sub}'" + (f":fontsdir='{fontsdir.replace(chr(92), '/').replace(':', chr(92)+':')}'" if fontsdir else "")
            run([FF, "-y", "-v", "error", "-i", nocap, "-vf", vf, "-c:v", "libx264", "-preset", "slow", "-crf", "17",
                 "-pix_fmt", "yuv420p", "-profile:v", "high",
                 "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-color_range", "tv",
                 "-c:a", "copy", "-movflags", "+faststart", final])
        else:
            shutil.copyfile(nocap, final)
        print(f"wrote {final}")

        # ---- contact sheet ----
        sheet = os.path.join(out_dir, f"{name}-sheet.jpg")
        n = max(1, int(round(total / 1.0)))
        cols = 5; rows = (n + cols - 1) // cols
        run([FF, "-y", "-v", "error", "-i", final, "-vf", f"fps=1,scale=216:384,tile={cols}x{rows}", "-frames:v", "1", "-q:v", "3", sheet])
        print(f"wrote {sheet}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main(sys.argv[1])
