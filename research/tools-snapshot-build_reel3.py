"""build_reel3.py - El Coyote reel renderer, playbook edition (2026-11-20).

Implements research/2026-11-20-EDITING-MASTER-PLAYBOOK.md:
  color   : per-clip HDR probe, HLG -> BT.709 tone map, bt709 tags, restrained "natural" grade
  motion  : eased punch-ins (scale eval=frame), speed ramps (smoothstep integral), whip pans (dblur+sendcmd),
            beat shake, shutter flash, vidstab
  text    : two-layer soft-shadow captions (Oswald Bold hook, Montserrat SemiBold per-word captions,
            tan accent, labels, tags, band under bright shots)
  sound   : dialogue cleanup chain, ambience bed ducked under voice, SFX kit (synthesized, license free),
            J-cut beds, loudnorm -14
  export  : 1080x1920 30fps H.264 High 4.2 crf17 maxrate16M closed 1s GOP aq-mode3 deband+grain unsharp
  lint    : hook on by frame 4 and <= 7 words, no static slot > 4 s, end line present, tags verified

usage: python -I build_reel3.py edl.json [--captions-only]

EDL JSON:
{
 "name": "...", "out_dir": "...", "fontsdir": "...", "sfxdir": "...",
 "ambience": {"clip": "...", "in": 2.0, "gain_db": -28},          # optional room-tone bed (looped)
 "slots": [ {"clip","in","dur",
             "speed": 0.5 | "ramp": [[t_in, speed], ...],         # ramp = knots in SOURCE seconds, smoothstep between
             "zoom": [1.0, 1.08], "zoom_anchor": 0.5, "zoom_ease": "inout"|"out",
             "stab": true, "shake": [0.4, 1.2], "flash": [1.0],
             "xfade": {"type": "fade"|"whip_left"|"whip_right"|"wipe_left", "dur": 0.3},
             "grade": "natural"|"none"} ],
 "audio": [ {"clip","in","dur","at","gain_db":0,"clean":true} ],
 "sfx":   [ {"kind": "whoosh"|"impact"|"riser"|"sub"|"click"|"gap", "at": 2.6, "gain_db": -8} ],
 "captions": [
   {"type":"hook","text":"HOW MUCH YOU PAY\\nFOR THAT TRUCK?","accent":"TRUCK","start":0,"end":2.6},
   {"type":"words","words":[["What?",2.9],["I",3.3]],"end":4.4,"band":false},
   {"type":"cap","text":"...","start":5,"end":7},
   {"type":"label","title":"PROJECT RIVAL","sub":"1959 F600 · 7.3 Powerstroke","start":12,"end":15},
   {"type":"tag","text":"DRIVEN DIESEL","start":6,"end":9},
   {"type":"small","text":"PART 2","start":15,"end":18,"pos":[540,1400]}
 ]
}
"""
import json, os, subprocess, sys, tempfile, shutil, math

BIN = os.path.join(os.environ["LOCALAPPDATA"], r"Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin")
FF = os.path.join(BIN, "ffmpeg.exe"); FP = os.path.join(BIN, "ffprobe.exe")
W, H, FPS = 1080, 1920, 30
TAN = "&H008CB3C9"      # #c9b38c  (ASS is &HAABBGGRR)
WHITE = "&H00FFFFFF"; OFFWHITE = "&H00F2F2F2"; BLACK = "&H00000000"; INK = "&H00141414"

TONEMAP = "libplacebo=tonemapping=spline:colorspace=bt709:color_primaries=bt709:color_trc=bt709:range=tv:format=yuv420p"
TONEMAP_FALLBACK = "zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=tonemap=mobius:desat=0,zscale=t=bt709:m=bt709:r=tv:dither=error_diffusion,format=yuv420p"
GRADES = {"natural": "curves=master='0/0.012 0.25/0.235 0.5/0.5 0.75/0.765 1/0.985',eq=saturation=0.95", "none": None}
COLOR_TAGS = ["-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-color_range", "tv"]
X264 = ["-c:v", "libx264", "-preset", "slow", "-crf", "17", "-maxrate", "16M", "-bufsize", "32M", "-profile:v", "high", "-level", "4.2",
        "-pix_fmt", "yuv420p", "-g", "30", "-keyint_min", "30", "-sc_threshold", "0", "-bf", "2",
        "-x264-params", "aq-mode=3:aq-strength=0.9:psy-rd=1.0,0.15:deblock=-1,-1:no-open-gop=1"]
EASE_INOUT = "if(lt({u},0.5),4*{u}^3,1-(-2*{u}+2)^3/2)"
EASE_OUT = "(1-(1-{u})^3)"


def run(cmd, cwd=None, check=True):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=cwd)
    if check and r.returncode != 0:
        print(" ".join(str(c) for c in cmd)); print(r.stderr[-3000:]); sys.exit(1)
    return r


def probe_dur(p):
    return float(run([FP, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p]).stdout.strip() or 0)


_HDR = {}
def is_hdr(clip):
    if clip not in _HDR:
        out = run([FP, "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=color_transfer,color_primaries", "-of", "csv=p=0", clip]).stdout.lower()
        _HDR[clip] = ("arib-std-b67" in out) or ("smpte2084" in out) or ("bt2020" in out)
    return _HDR[clip]


# ---------------------------------------------------------------- SFX kit (synthesized, no licensing)
def ensure_sfx(sfxdir):
    os.makedirs(sfxdir, exist_ok=True)
    kit = {
        "whoosh": ["-f", "lavfi", "-i", "anoisesrc=color=pink:r=48000:d=0.5:a=0.8", "-af",
                   "highpass=f=250,lowpass=f=5000,afade=t=in:d=0.22:curve=qsin,afade=t=out:st=0.25:d=0.25:curve=qsin,volume=0.9"],
        "riser": ["-f", "lavfi", "-i", "anoisesrc=color=white:r=48000:d=1.0:a=0.7", "-af",
                  "highpass=f=400,lowpass=f=9000,afade=t=in:d=1.0:curve=exp,volume=0.9"],
        "impact": ["-f", "lavfi", "-i", "sine=f=52:r=48000:d=0.7", "-f", "lavfi", "-i", "anoisesrc=color=brown:r=48000:d=0.12:a=0.9",
                   "-filter_complex", "[0:a]afade=t=out:st=0.05:d=0.65:curve=exp,volume=1.0[s];[1:a]lowpass=f=1800,afade=t=out:st=0.01:d=0.11[n];[s][n]amix=inputs=2:duration=longest:normalize=0,alimiter=limit=-1dB"],
        "sub": ["-f", "lavfi", "-i", "aevalsrc=0.9*sin(2*PI*(85-55*t)*t):s=48000:d=0.8", "-af", "afade=t=out:st=0.2:d=0.6:curve=exp"],
        "click": ["-f", "lavfi", "-i", "anoisesrc=color=white:r=48000:d=0.04:a=0.8", "-af", "highpass=f=1800,afade=t=out:st=0.005:d=0.035"],
    }
    for name, args in kit.items():
        p = os.path.join(sfxdir, f"{name}.wav")
        if not os.path.exists(p):
            run([FF, "-y", "-v", "error", *args, "-ac", "2", "-ar", "48000", p])
    return {k: os.path.join(sfxdir, f"{k}.wav") for k in kit}


# ---------------------------------------------------------------- captions (ASS)
def ass_time(t):
    t = max(0.0, t); return f"{int(t//3600)}:{int(t%3600//60):02d}:{t%60:05.2f}"

def esc(t):
    return t.replace("\\", "\\\\").replace("{", "\\{").replace("}", "\\}").replace("\n", "\\N")

STYLES = f"""Style: Hook,Oswald Bold,112,{OFFWHITE},{OFFWHITE},{BLACK},{BLACK},0,0,0,0,100,100,2,0,1,0,0,5,90,90,0,1
Style: HookShadow,Oswald Bold,112,{BLACK},{BLACK},{BLACK},{BLACK},0,0,0,0,100,100,2,0,1,0,0,5,90,90,0,1
Style: Cap,Montserrat SemiBold,66,{WHITE},{WHITE},{BLACK},{BLACK},0,0,0,0,100,100,-1,0,1,0,0,2,90,90,680,1
Style: CapShadow,Montserrat SemiBold,66,{BLACK},{BLACK},{BLACK},{BLACK},0,0,0,0,100,100,-1,0,1,0,0,2,90,90,680,1
Style: Label,Oswald Medium,40,{TAN},{TAN},{BLACK},{BLACK},0,0,0,0,100,100,5,0,1,0,0,1,72,72,0,1
Style: LabelSub,Montserrat SemiBold,34,&H00E6E6E6,&H00E6E6E6,{BLACK},{BLACK},0,0,0,0,100,100,0,0,1,0,0,1,72,72,0,1
Style: Tag,Oswald Medium,38,{INK},{INK},{TAN},{TAN},0,0,0,0,100,100,4,0,3,14,0,1,72,72,0,1
Style: Small,Montserrat SemiBold,36,&H00E6E6E6,&H00E6E6E6,{BLACK},{BLACK},0,0,0,0,100,100,1,0,1,0,0,5,90,90,0,1
Style: SmallShadow,Montserrat SemiBold,36,{BLACK},{BLACK},{BLACK},{BLACK},0,0,0,0,100,100,1,0,1,0,0,5,90,90,0,1
Style: Serif,Instrument Serif,120,{TAN},{TAN},{BLACK},{BLACK},0,-1,0,0,100,100,0,0,1,0,0,5,90,90,0,1
Style: Band,Arial,20,{BLACK},{BLACK},{BLACK},{BLACK},0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1"""


def accent(text, word):
    if not word: return esc(text)
    parts = text.split(word, 1)
    if len(parts) == 1: return esc(text)
    return esc(parts[0]) + "{\\1c" + TAN[4:] + "&}" + esc(word) + "{\\1c&HFFFFFF&}" + esc(parts[1]) if False else \
        esc(parts[0]) + "{\\1c" + TAN[4:] + "&}" + esc(word) + "{\\r}" + esc(parts[1])


def band_event(start, end, y=1060, h=420):
    return (f"Dialogue: 0,{ass_time(start)},{ass_time(end)},Band,,0,0,0,,"
            f"{{\\pos(0,{y})\\bord0\\shad0\\blur50\\1a&H66&\\p1}}m -300 0 l 1380 0 l 1380 {h} l -300 {h}{{\\p0}}")


def two_layer(style, start, end, text, pos, tags="", shadow_blur=12, shadow_alpha="&H78&", dx=3, dy=6, fade=(120, 120)):
    x, y = pos
    fad = f"\\fad({fade[0]},{fade[1]})"
    sh = f"Dialogue: 0,{ass_time(start)},{ass_time(end)},{style}Shadow,,0,0,0,,{{\\pos({x+dx},{y+dy})\\blur{shadow_blur}\\alpha{shadow_alpha}{fad}{tags}}}{text}"
    fg = f"Dialogue: 1,{ass_time(start)},{ass_time(end)},{style},,0,0,0,,{{\\pos({x},{y}){fad}{tags}}}{text}"
    return [sh, fg]


def group_words(words, max_words=4, max_chars=28, gap=0.35):
    groups, cur = [], []
    for w, t in words:
        if cur:
            last_t = cur[-1][1]; n = len(cur); chars = len(" ".join(x[0] for x in cur)) + 1 + len(w)
            if (t - last_t > gap) or n >= max_words or chars > max_chars:
                groups.append(cur); cur = []
        cur.append((w, t))
    if cur: groups.append(cur)
    # merge a trailing one-word group into the previous
    if len(groups) > 1 and len(groups[-1]) == 1:
        groups[-2].extend(groups[-1]); groups.pop()
    return groups


def caption_events(caps):
    ev = []
    for c in caps:
        kind = c.get("type", "cap")
        if kind == "hook":
            pos = tuple(c.get("pos", (540, 760)))
            text = accent(c["text"].upper() if c.get("caps", True) else c["text"], (c.get("accent") or "").upper() if c.get("caps", True) else c.get("accent"))
            pop = "\\fscx94\\fscy94\\t(0,140,0.6,\\fscx100\\fscy100)"
            ev += two_layer("Hook", c["start"], c["end"], text, pos, tags=pop + "\\blur6\\t(0,160,\\blur0)", shadow_blur=14, shadow_alpha="&H70&")
            # the shadow line got the blur-in tag too; harmless
        elif kind == "words":
            words = [(w, float(t)) for w, t in c["words"]]
            end = float(c["end"]); pos = tuple(c.get("pos", (540, 1240)))
            groups = group_words(words)
            for gi, g in enumerate(groups):
                g_start = max(0.0, g[0][1] - 0.04)
                g_end = (groups[gi + 1][0][1] - 0.04) if gi + 1 < len(groups) else end
                g_end = max(g_end, g_start + 0.7)
                full = " ".join(w for w, _ in g)
                if c.get("band"): ev.append(band_event(g_start, g_end))
                ev.append(f"Dialogue: 0,{ass_time(g_start)},{ass_time(g_end)},CapShadow,,0,0,0,,{{\\pos({pos[0]+3},{pos[1]+6})\\blur10\\alpha&H80&\\fad(50,80)}}{esc(full)}")
                for wi, (w, t) in enumerate(g):
                    s = max(g_start, t - 0.04)
                    e = (g[wi + 1][1] - 0.04) if wi + 1 < len(g) else g_end
                    before = " ".join(x for x, _ in g[:wi]); after = " ".join(x for x, _ in g[wi + 1:])
                    shown = (esc(before) + " " if before else "") + "{\\1c" + TAN[4:] + "&}" + esc(w) + "{\\r}" + (" " + esc(after) if after and c.get("show_ahead") else "")
                    tags = "\\fad(50,0)\\fscx92\\fscy92\\t(0,120,0.5,\\fscx100\\fscy100)" if wi == 0 else ""
                    if wi == len(g) - 1: tags += "\\fad(0,80)"
                    ev.append(f"Dialogue: 1,{ass_time(s)},{ass_time(e)},Cap,,0,0,0,,{{\\pos({pos[0]},{pos[1]}){tags}}}{shown}")
        elif kind == "cap":
            pos = tuple(c.get("pos", (540, 1240)))
            if c.get("band"): ev.append(band_event(c["start"], c["end"]))
            text = accent(c["text"], c.get("accent"))
            pop = "\\fscx94\\fscy94\\t(0,120,0.5,\\fscx100\\fscy100)" if c.get("pop", True) else ""
            ev += two_layer("Cap", c["start"], c["end"], text, pos, tags=pop, shadow_blur=10, shadow_alpha="&H80&", fade=(80, 80))
        elif kind == "label":
            x, y = c.get("pos", (72, 1400))
            ev.append(f"Dialogue: 1,{ass_time(c['start'])},{ass_time(c['end'])},Label,,0,0,0,,{{\\pos({x},{y})\\fad(120,120)}}{esc(c['title'])}")
            ev.append(f"Dialogue: 1,{ass_time(c['start'])},{ass_time(c['end'])},Band,,0,0,0,,{{\\pos({x},{y+12})\\bord0\\shad0\\1c{TAN[4:]}&\\1a&H00&\\p1\\fad(120,120)}}m 0 0 l 56 0 l 56 4 l 0 4{{\\p0}}")
            if c.get("sub"):
                ev.append(f"Dialogue: 1,{ass_time(c['start'])},{ass_time(c['end'])},LabelSub,,0,0,0,,{{\\pos({x},{y+60})\\fad(120,120)}}{esc(c['sub'])}")
        elif kind == "tag":
            x, y = c.get("pos", (72, 1380))
            ev.append(f"Dialogue: 1,{ass_time(c['start'])},{ass_time(c['end'])},Tag,,0,0,0,,{{\\pos({x},{y})\\fad(120,120)}}{esc(c['text'])}")
        elif kind == "small":
            pos = tuple(c.get("pos", (540, 1400)))
            ev += two_layer("Small", c["start"], c["end"], esc(c["text"]), pos, shadow_blur=8, shadow_alpha="&H80&", dx=2, dy=4, fade=(120, 120))
        elif kind == "serif":
            x, y = c.get("pos", (540, 700))
            ev.append(f"Dialogue: 1,{ass_time(c['start'])},{ass_time(c['end'])},Serif,,0,0,0,,{{\\pos({x},{y})\\fad(200,200)\\blur0.4}}{esc(c['text'])}")
    return ev


def write_ass(path, caps):
    head = ("[Script Info]\nScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\nLayoutResX: 1080\nLayoutResY: 1920\nWrapStyle: 0\n"
            "ScaledBorderAndShadow: yes\nKerning: yes\n\n[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n"
            + STYLES + "\n\n[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n")
    with open(path, "w", encoding="utf-8-sig") as f:
        f.write(head + "\n".join(caption_events(caps)) + "\n")


# ---------------------------------------------------------------- motion helpers
def zoom_filters(z, dur, anchor=0.5, ease="inout"):
    a, b = float(z[0]), float(z[1])
    u = f"clip(t/{dur:.3f},0,1)"
    E = (EASE_INOUT if ease == "inout" else EASE_OUT).format(u=u)
    zf = f"({a}+({b}-{a})*({E}))"
    return [f"scale=w='{W}*{zf}':h='{H}*{zf}':eval=frame:flags=bicubic", f"crop={W}:{H}:x='(iw-ow)/2':y='(ih-oh)*{anchor}'", "setsar=1"]


def shake_filters(beats, amp=28, freq=12.0, decay=10.0):
    if not beats: return []
    sx = "+".join(f"gte(t,{b})*exp(-{decay}*(t-{b}))*sin(2*PI*{freq}*(t-{b}))" for b in beats)
    sy = "+".join(f"gte(t,{b})*exp(-{decay}*(t-{b}))*cos(2*PI*{freq*0.75:.2f}*(t-{b}))" for b in beats)
    return [f"scale=iw*1.06:ih*1.06:flags=bicubic", f"crop={W}:{H}:x='(iw-ow)/2+{amp}*({sx})':y='(ih-oh)/2+{int(amp*0.6)}*({sy})'", "setsar=1"]


def ramp_setpts(knots, dur_src):
    """knots: [[t_in, speed], ...] in source seconds (relative to slot start). Smoothstep between knots.
    Returns (setpts_expr, out_duration)."""
    pts = [(float(t), 1.0 / float(s)) for t, s in knots]           # r = output seconds per input second
    if pts[0][0] > 0: pts.insert(0, (0.0, pts[0][1]))
    pts.append((dur_src, pts[-1][1]))
    expr = None; T = 0.0; terms = []
    for i in range(len(pts) - 1):
        t0, r0 = pts[i]; t1, r1 = pts[i + 1]
        if t1 <= t0: continue
        L = t1 - t0
        seg = f"{T:.5f}+(T-{t0:.4f})*{r0:.5f}+({r1 - r0:.5f})*{L:.4f}*(st(1,(T-{t0:.4f})/{L:.4f})*0+ld(1)^3-ld(1)^4/2)"
        terms.append((t1, seg)); T += L * (r0 + r1) / 2
    # build nested if from the end
    expr = terms[-1][1]
    for t1, seg in reversed(terms[:-1]):
        expr = f"if(lt(T,{t1:.4f}),{seg},{expr})"
    return f"({expr})/TB", T


# ---------------------------------------------------------------- slot render
def render_slot(i, s, tmp, prev_whip=None, next_whip=None):
    out = os.path.join(tmp, f"slot{i:02d}.mp4")
    dur_out = float(s["dur"]); src_in = float(s["in"])
    ramp = s.get("ramp"); speed = float(s.get("speed", 1.0))
    vf = []
    if is_hdr(s["clip"]): vf.append(TONEMAP)
    if s.get("stab"):
        trf = f"slot{i:02d}.trf"
        run([FF, "-y", "-v", "error", "-ss", f"{src_in:.3f}", "-t", f"{dur_out * (speed if not ramp else 1) + 1.0:.3f}", "-i", s["clip"],
             "-vf", (TONEMAP + "," if is_hdr(s["clip"]) else "") + f"vidstabdetect=shakiness=5:accuracy=15:result={trf}", "-f", "null", "-"], cwd=tmp)
        vf.append(f"vidstabtransform=input={trf}:zoom=3:smoothing=20:interpol=bicubic,unsharp=5:5:0.4:3:3:0.0")
    vf += [f"scale={W}:{H}:force_original_aspect_ratio=increase", f"crop={W}:{H}", "setsar=1"]
    g = GRADES.get(s.get("grade", "natural"))
    if g: vf.append(g)
    # time remap
    if ramp:
        src_len = float(ramp[-1][0]) if ramp[-1][0] else dur_out
        # the knots describe the whole source window; its output length defines dur
        expr, T = ramp_setpts(ramp, src_len)
        min_speed = min(float(k[1]) for k in ramp)
        if min_speed < 1.0:
            vf.append("minterpolate=fps=120:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1")
        vf += [f"setpts='{expr}'", "tmix=frames=2", f"fps={FPS}"]
        dur_src = src_len; dur_out = T; s["dur"] = round(T, 3)
    elif abs(speed - 1.0) > 1e-3:
        dur_src = dur_out * speed
        if speed < 1.0:
            vf += [f"minterpolate=fps={FPS/speed:.3f}:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1", f"setpts={1/speed:.4f}*PTS"]
        else:
            vf += [f"setpts={1/speed:.4f}*PTS"]
        vf.append(f"fps={FPS}")
    else:
        dur_src = dur_out; vf.append(f"fps={FPS}")
    if s.get("zoom"): vf += zoom_filters(s["zoom"], dur_out, s.get("zoom_anchor", 0.5), s.get("zoom_ease", "inout"))
    if s.get("shake"): vf += shake_filters(s["shake"])
    for ft in s.get("flash", []):
        vf.append(f"drawbox=c=white@0.75:t=fill:enable='between(t,{ft:.3f},{ft + 0.07:.3f})'")
    # whip blur at the edges (keyframed with sendcmd, slot-local times)
    cmds = []
    if prev_whip:   # this slot is entered by a whip: blur-in over its first 0.25 s
        cmds.append(f"0.00-0.25 [expr] dblur@w radius '(1-TI)*(1-TI)*70';")
    if next_whip:   # this slot exits with a whip: blur-out over its last 0.25 s
        cmds.append(f"{max(0, dur_out - 0.25):.2f}-{dur_out:.2f} [expr] dblur@w radius 'TI*TI*70';")
    if cmds:
        cf = f"slot{i:02d}.cmd"; open(os.path.join(tmp, cf), "w").write("\n".join(cmds) + "\n")
        ang = 0 if (prev_whip or next_whip) in ("whip_left", "whip_right") else 90
        vf += ["settb=AVTB", f"sendcmd=f={cf}", f"dblur@w=angle={ang}:radius=0"]
    vf += ["format=yuv420p", f"trim=duration={dur_out:.3f}", "setpts=PTS-STARTPTS"]
    run([FF, "-y", "-v", "error", "-ss", f"{src_in:.3f}", "-t", f"{dur_src + 0.6:.3f}", "-i", s["clip"], "-an",
         "-vf", ",".join(vf), "-r", str(FPS), "-c:v", "libx264", "-preset", "medium", "-crf", "15", "-pix_fmt", "yuv420p",
         *COLOR_TAGS, "-t", f"{dur_out:.3f}", out], cwd=tmp)
    d = probe_dur(out)
    if d < dur_out - 0.05:
        padded = os.path.join(tmp, f"slot{i:02d}p.mp4")
        run([FF, "-y", "-v", "error", "-i", out, "-vf", f"tpad=stop_mode=clone:stop_duration={dur_out - d + 0.1:.3f},trim=duration={dur_out:.3f}",
             "-c:v", "libx264", "-preset", "medium", "-crf", "15", "-pix_fmt", "yuv420p", *COLOR_TAGS, padded])
        out = padded
    return out, dur_out


# ---------------------------------------------------------------- lint
def lint(e, total):
    problems, warns = [], []
    hooks = [c for c in e.get("captions", []) if c.get("type") == "hook"]
    if not hooks: problems.append("no hook caption")
    for h in hooks:
        n = len(h["text"].replace("\n", " ").split())
        if n > 7: problems.append(f"hook has {n} words (max 7): {h['text']!r}")
        if h["start"] > 0.14: problems.append(f"hook starts at {h['start']} s, must be on by frame 4 (0.13 s)")
    t = 0.0
    for i, s in enumerate(e["slots"]):
        if s["dur"] > 4.0 and not (s.get("zoom") or s.get("ramp") or s.get("shake")):
            warns.append(f"slot {i} holds {s['dur']} s with no zoom/ramp (max 4 s static)")
        if s["dur"] > 3.0 and not (s.get("zoom") or s.get("ramp") or s.get("speed")):
            warns.append(f"slot {i} is {s['dur']} s with no motion treatment (3 s rule)")
        t += s["dur"]
    last = [c for c in e.get("captions", []) if c.get("type") in ("cap", "small", "serif") and c["end"] >= total - 0.6]
    if not last: warns.append("no end line in the last 0.6 s (send/loop line expected)")
    if total > 60: warns.append(f"{total:.1f} s is long for cold reach")
    for p in problems: print("LINT FAIL:", p)
    for w in warns: print("LINT WARN:", w)
    if problems: sys.exit(2)


# ---------------------------------------------------------------- main
def main(edl_path):
    e = json.load(open(edl_path, encoding="utf-8"))
    name, out_dir = e["name"], e["out_dir"]; os.makedirs(out_dir, exist_ok=True)
    fontsdir = e.get("fontsdir"); sfxdir = e.get("sfxdir", os.path.join(os.path.dirname(os.path.abspath(__file__)), "sfx"))
    kit = ensure_sfx(sfxdir)
    captions_only = "--captions-only" in sys.argv and os.path.exists(os.path.join(out_dir, f"{name}-NOCAP.mp4"))
    nocap = os.path.join(out_dir, f"{name}-NOCAP.mp4")
    tmp = tempfile.mkdtemp(prefix="reel3_")
    try:
        slots = e["slots"]
        if not captions_only:
            parts = []
            for i, s in enumerate(slots):
                prev_whip = slots[i].get("xfade", {}).get("type") if str(slots[i].get("xfade", {}).get("type", "")).startswith("whip") else None
                next_whip = slots[i + 1].get("xfade", {}).get("type") if i + 1 < len(slots) and str(slots[i + 1].get("xfade", {}).get("type", "")).startswith("whip") else None
                print(f"slot {i+1}/{len(slots)}: {os.path.basename(s['clip'])} in={s['in']} dur={s['dur']}" + (" HDR" if is_hdr(s['clip']) else "")
                      + (" ramp" if s.get("ramp") else "") + (f" speed={s['speed']}" if s.get("speed") else "") + (" zoom" if s.get("zoom") else "") + (" stab" if s.get("stab") else ""))
                p, d = render_slot(i, s, tmp, prev_whip, next_whip)
                parts.append(p)
            total = sum(float(s["dur"]) for s in slots)
            # ---- video chain
            inputs = []
            for p in parts: inputs += ["-i", p]
            fc = [f"[{i}:v]setsar=1,format=yuv420p,fps={FPS},settb=AVTB[s{i}]" for i in range(len(parts))]
            cur, cur_len = "[s0]", float(slots[0]["dur"])
            for i in range(1, len(slots)):
                x = slots[i].get("xfade") or {}; d = float(slots[i]["dur"]); typ = x.get("type", "cut"); xd = float(x.get("dur", 0) or 0)
                if typ.startswith("whip"):
                    xd = xd or 0.2; tr = "slideleft" if typ == "whip_left" else "slideright"
                    fc.append(f"{cur}[s{i}]xfade=transition={tr}:duration={xd:.3f}:offset={cur_len - xd:.3f},settb=AVTB[x{i}]"); cur_len += d - xd
                elif typ.startswith("wipe") and xd > 0:
                    tr = {"wipe_left": "wipeleft", "wipe_right": "wiperight", "wipe_up": "wipeup", "wipe_down": "wipedown"}.get(typ, "wipeleft")
                    fc.append(f"{cur}[s{i}]xfade=transition={tr}:duration={xd:.3f}:offset={cur_len - xd:.3f},settb=AVTB[x{i}]"); cur_len += d - xd
                elif xd > 0:
                    fc.append(f"{cur}[s{i}]xfade=transition={typ if typ != 'cut' else 'fade'}:duration={xd:.3f}:offset={cur_len - xd:.3f},settb=AVTB[x{i}]"); cur_len += d - xd
                else:
                    fc.append(f"{cur}[s{i}]concat=n=2:v=1:a=0,settb=AVTB[x{i}]"); cur_len += d
                cur = f"[x{i}]"
            total = cur_len
            fc.append(f"{cur}format=yuv420p[vout]")
            # ---- audio: voice beds (cleaned), ambience bed ducked by voice, sfx, loudnorm
            n_in = len(parts); voice_in = []
            beds = e.get("audio", [])
            for j, b in enumerate(beds):
                inputs += ["-ss", f"{float(b['in']):.3f}", "-t", f"{float(b['dur']):.3f}", "-i", b["clip"]]
                ms = int(float(b["at"]) * 1000); fade = float(b.get("fade", 0.08))
                clean = ("highpass=f=90:poles=2,afftdn=nr=12:nf=-40:tn=1,deesser=i=0.3:m=0.5:f=0.6,"
                         "acompressor=threshold=-20dB:ratio=3:attack=8:release=120:makeup=3dB:knee=4,alimiter=limit=-2dB:attack=5:release=50,") if b.get("clean") else ""
                fc.append(f"[{n_in}:a:0]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,asetpts=PTS-STARTPTS,{clean}"
                          f"volume={float(b.get('gain_db', 0))}dB,afade=t=in:d={fade},afade=t=out:st={float(b['dur']) - fade:.3f}:d={fade},adelay={ms}|{ms}[b{j}]")
                voice_in.append(f"[b{j}]"); n_in += 1
            fc.append(f"anullsrc=r=48000:cl=stereo,atrim=duration={total:.3f}[abase]")
            if voice_in:
                fc.append("".join(["[abase]"] + voice_in) + f"amix=inputs={len(voice_in) + 1}:duration=first:normalize=0,asplit=2[voice][vkey]")
            else:
                fc.append("[abase]asplit=2[voice][vkey]")
            amb = e.get("ambience")
            if amb:
                inputs += ["-stream_loop", "-1", "-ss", f"{float(amb.get('in', 0)):.3f}", "-t", f"{total + 1:.3f}", "-i", amb["clip"]]
                fc.append(f"[{n_in}:a:0]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,asetpts=PTS-STARTPTS,highpass=f=60,lowpass=f=9000,"
                          f"volume={float(amb.get('gain_db', -28))}dB,afade=t=in:d=0.4,atrim=duration={total:.3f}[amb0]")
                fc.append("[amb0][vkey]sidechaincompress=threshold=0.05:ratio=4:attack=10:release=400:knee=4[amb]"); n_in += 1
                mix_in = ["[voice]", "[amb]"]
            else:
                fc.append("[vkey]anullsink"); mix_in = ["[voice]"]
            sfx = e.get("sfx", [])
            for k, sx in enumerate(sfx):
                kind = sx.get("kind"); f = sx.get("file") or kit.get(kind)
                if not f: continue
                if kind == "gap":  # 2 frames of silence before a hit: handled as a volume dip on the ambience, skip as a file
                    continue
                at = float(sx["at"]) - (0.08 if kind == "whoosh" else 1.0 if kind == "riser" else 0.0)
                at = max(0.0, at); ms = int(at * 1000)
                inputs += ["-i", f]
                fc.append(f"[{n_in}:a:0]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,volume={float(sx.get('gain_db', -10))}dB,adelay={ms}|{ms}[fx{k}]")
                mix_in.append(f"[fx{k}]"); n_in += 1
            fc.append("".join(mix_in) + f"amix=inputs={len(mix_in)}:duration=first:normalize=0,atrim=duration={total:.3f},"
                      + ("loudnorm=I=-14:TP=-1.5:LRA=11:linear=true," if voice_in else "")
                      + "aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo[aout]")
            lint(e, total)
            graph = os.path.join(tmp, "graph.txt"); open(graph, "w", encoding="utf-8").write(";\n".join(fc))
            run([FF, "-y", "-v", "error", *inputs, "/filter_complex", graph, "-map", "[vout]", "-map", "[aout]", "-r", str(FPS),
                 *X264, *COLOR_TAGS, "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", "-movflags", "+faststart", nocap])
            print(f"wrote {nocap} ({total:.2f}s)")
        else:
            total = probe_dur(nocap); print(f"captions-only: reusing {nocap} ({total:.2f}s)")
        # ---- captions + finishing filters + export recipe
        final = os.path.join(out_dir, f"{name}.mp4")
        ass_path = os.path.join(out_dir, f"{name}.ass"); write_ass(ass_path, e.get("captions", []))
        sub = ass_path.replace("\\", "/").replace(":", "\\:")
        fd = (fontsdir or "").replace("\\", "/").replace(":", "\\:")
        vf = ("unsharp=5:5:0.5:3:3:0.0,deband=1thr=0.02:2thr=0.02:3thr=0.02:range=16:blur=1,noise=alls=3:allf=t,"
              f"ass='{sub}'" + (f":fontsdir='{fd}'" if fontsdir else "") + ":shaping=complex,format=yuv420p")
        run([FF, "-y", "-v", "error", "-i", nocap, "-vf", vf, *X264, *COLOR_TAGS, "-c:a", "copy", "-movflags", "+faststart", final])
        tags = run([FP, "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=pix_fmt,color_space,color_transfer,color_primaries,color_range", "-of", "csv=p=0", final]).stdout.strip()
        print("tags:", tags, "OK" if tags.startswith("yuv420p,bt709,bt709,bt709,tv") else "BAD TAGS")
        print(f"wrote {final}")
        sheet = os.path.join(out_dir, f"{name}-sheet.jpg"); n = max(1, int(round(total))); rows = (n + 4) // 5
        run([FF, "-y", "-v", "error", "-i", final, "-vf", f"fps=1,scale=216:384,tile=5x{rows}", "-frames:v", "1", "-q:v", "3", sheet])
        print(f"wrote {sheet}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main(sys.argv[1])
