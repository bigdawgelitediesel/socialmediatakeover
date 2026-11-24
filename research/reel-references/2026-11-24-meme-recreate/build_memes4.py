"""build_memes4.py - four meme recreations from Drive raw footage (2026-11-24).
Each meme: a list of segments (clip, start, dur, optional label) plus one header line. Text is drawn with PIL in Impact
(system font, never copied), top zone only (rule 120), no grade, HLG tone-mapped to bt709, 1080x1920 30 fps.
usage: python -I build_memes4.py [name ...]
"""
import os, sys, subprocess, json
from PIL import Image, ImageDraw, ImageFont, ImageFilter
FF = os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin")
FFMPEG, FFPROBE = FF + r"\ffmpeg.exe", FF + r"\ffprobe.exe"
RAW = r"C:\Users\Parts\My Drive\VIDEO\raw"
HERE = os.path.dirname(os.path.abspath(__file__)); TMP = os.path.join(HERE, "tmp"); os.makedirs(TMP, exist_ok=True)
IMPACT = r"C:\Windows\Fonts\impact.ttf"
TONEMAP = "libplacebo=tonemapping=spline:colorspace=bt709:color_primaries=bt709:color_trc=bt709:range=tv:format=yuv420p"
WHITE, YELLOW, RED = (255, 255, 255), (253, 196, 58), (226, 54, 54)
DANCE = "A263E7B4-BD41-4CBA-864A-648B9647E806.mp4"
WASH = "Video_262672_DJI_20261115132016_0033_D_MP4_141790265_34000_20261115132856_video_original.mp4"
ENGINE = "Video_262624_DJI_20261115111038_0030_D_MP4_863462710_80000_20261115111158_video_original.mp4"

MEMES = {
    # 1. Shayna Laliberte "The car I spent $40k on" (YouTube Shorts QdD8M80lPRo, 3.15M): one line, her dancing in front of it.
    "1-standing-in-the-shop": dict(header=["STANDING IN THE SHOP", "WHERE THE TRUCK I'M TAKING", "TO SEMA STILL CAN'T MOVE"], size=78,
        segs=[(DANCE, 4.6, 6.4, None)]),
    # 2. Mechanical Nightmare "Customer States: my engine is knocking" (VcviAMyHTDU, 4.06M): the quote, then what was found.
    "2-customer-states": dict(header=["CUSTOMER STATES:", "\"IT RAN WHEN PARKED\""], size=92, hl=1,
        segs=[(WASH, 4.5, 9.0, None)]),
    # 3. C.Z TUNES "The Definition Of A True Project Car Budget" (agyzLfUaSMM, 14.1M): what the truck doesn't have, then where the money went.
    "3-project-truck-budget": dict(header=["THE DEFINITION OF A TRUE", "PROJECT TRUCK BUDGET"], size=78,
        segs=[("IMG_3861.MOV", 1.6, 2.0, ("PAINT", "NO")), ("IMG_3859.MOV", 2.6, 2.0, ("A/C", "NO")), ("IMG_3862.MOV", 3.6, 2.2, ("BED", "NO")),
              (ENGINE, 6.0, 3.0, ("7.3 POWERSTROKE", "YES"))]),
    # 4. Tom's Refurb "Just a little 331 stroker" (TikTok 5.0M, Shorts 6.5M): the caption undersells, the picture oversells.
    "4-little-surface-rust": dict(header=["JUST A LITTLE", "SURFACE RUST"], size=110,
        segs=[("IMG_3857.MOV", 0.3, 3.6, None), ("IMG_3861.MOV", 0.6, 4.4, None)]),
}

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode: sys.exit("FAILED: " + " ".join(cmd[:6]) + "\n" + r.stderr[-1500:])
    return r

def is_hdr(p):
    r = run([FFPROBE, "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=color_transfer", "-of", "csv=p=0", p])
    return "arib-std-b67" in r.stdout or "smpte2084" in r.stdout

def text_png(path, lines, size, y0, colors=None, align_center=True):
    """Lines of Impact with a soft shadow on a transparent 1080x1920 canvas. Returns the bottom y."""
    im = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0)); sh = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0))
    d, ds = ImageDraw.Draw(im), ImageDraw.Draw(sh); y = y0
    for i, ln in enumerate(lines):
        sz = size; f = ImageFont.truetype(IMPACT, sz)
        while d.textlength(ln, font=f) > 940: sz -= 4; f = ImageFont.truetype(IMPACT, sz)
        w = d.textlength(ln, font=f); x = (1080 - w) / 2
        ds.text((x, y + 6), ln, font=f, fill=(0, 0, 0, 200))
        d.text((x, y), ln, font=f, fill=(colors[i] if colors else WHITE) + (255,))
        y += int(sz * 1.08)
    sh = sh.filter(ImageFilter.GaussianBlur(9)); out = Image.alpha_composite(sh, im); out.save(path); return y

def build(name, m):
    parts = []
    hdr = os.path.join(TMP, name + "-hdr.png")
    cols = [WHITE] * len(m["header"])
    if "hl" in m: cols[m["hl"]] = YELLOW
    ybot = text_png(hdr, m["header"], m["size"], 190, cols)
    assert ybot < 620, (name, ybot)
    for i, (clip, ss, dur, label) in enumerate(m["segs"]):
        src = os.path.join(RAW, clip); out = os.path.join(TMP, "%s-%d.mp4" % (name, i))
        vf = ([TONEMAP] if is_hdr(src) else []) + ["scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos", "crop=1080:1920", "fps=30", "setsar=1", "format=yuv420p"]
        ins = ["-ss", "%.3f" % ss, "-t", "%.3f" % dur, "-i", src, "-i", hdr]; fc = "[0:v]" + ",".join(vf) + "[b];[b][1:v]overlay=0:0[v1]"; last = "v1"
        if label:
            lp = os.path.join(TMP, "%s-%d-label.png" % (name, i))
            text_png(lp, [label[0], label[1]], 120, 1290, [WHITE, RED if label[1] == "NO" else YELLOW])
            ins += ["-i", lp]; fc += ";[v1][2:v]overlay=0:0:enable='gte(t,0.25)'[v2]"; last = "v2"
        run([FFMPEG, "-y", "-v", "error"] + ins + ["-filter_complex", fc, "-map", "[%s]" % last, "-map", "0:a:0?", "-c:v", "libx264", "-crf", "16", "-preset", "medium",
             "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709", "-color_range", "tv", out])
        parts.append(out)
    lst = os.path.join(TMP, name + ".txt"); open(lst, "w").write("".join("file '%s'\n" % p.replace("\\", "/") for p in parts))
    final = os.path.join(HERE, name + ".mp4")
    run([FFMPEG, "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c:v", "libx264", "-crf", "17", "-preset", "slow", "-pix_fmt", "yuv420p", "-r", "30",
         "-c:a", "aac", "-b:a", "192k", "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709", "-color_range", "tv", "-movflags", "+faststart", final])
    print("built", final)

if __name__ == "__main__":
    for n, m in MEMES.items():
        if len(sys.argv) > 1 and not any(a in n for a in sys.argv[1:]): continue
        build(n, m)
