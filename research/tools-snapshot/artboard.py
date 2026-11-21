"""artboard.py - the "artboard before render" step from the El Coyote playbook.

Reads a Remotion props JSON (CardReel or RivalReel), picks the PLANNED frames (hook frame 4,
every overlay's start plus --extra seconds, the last frame), renders just those frames in one
Remotion image-sequence pass, draws a label strip + the IG safe lines on every tile and tiles
them into one contact sheet so Jacob can approve or redline the layout in one look.

Writes next to the props file (or --out):
  <name>-artboard.png   the sheet (6 columns, 320 px tiles)
  <name>-artboard.md    every tile with its planned content + lint warnings

Usage:
  artboard.py <props.json> [--comp CardReel|RivalReel] [--out dir] [--cols 6] [--max 24] [--extra 0.5]
              [--tile 320] [--kit dir] [--keep] [--no-pil]

Run with any Python; if Pillow is missing it re-launches itself in tools\\venv-artboard
(falls back to ffmpeg drawtext + tile when neither has Pillow, labels are plainer).
"""
import argparse, glob, json, math, os, re, shutil, subprocess, sys, tempfile, time

HERE = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.join(HERE, "rival-reels")
VENV_PY = os.path.join(HERE, "venv-artboard", "Scripts", "python.exe")
FFBIN = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Microsoft", "WinGet", "Packages",
                     "Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe", "ffmpeg-9.0.2-full_build", "bin")
FFMPEG = os.path.join(FFBIN, "ffmpeg.exe") if os.path.exists(os.path.join(FFBIN, "ffmpeg.exe")) else "ffmpeg"
FFPROBE = os.path.join(FFBIN, "ffprobe.exe") if os.path.exists(os.path.join(FFBIN, "ffprobe.exe")) else "ffprobe"
FONTS = os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts")

W, H = 1080, 1920
TEXT_FLOOR = 1440          # nothing with text below this (IG caption block starts ~1520)
GRID_TOP, GRID_BOT = 480, 1440   # grid-safe band: what survives the 4:5 feed crop with the UI on top
DEDUPE_FRAMES = 10
HOOK_FRAME = 4
RED = (226, 44, 44)

# ---------- overlay knowledge (mirrors src/components defaults; estimates, not pixel truth) ----------
# default y when the props do not set one
DEFAULT_Y = {
    "badge": 300, "lowerthird": 1300, "quote": 330, "logo": 330, "photo": 300, "spec": 320, "strike": 340,
    "browser": 300, "prompt": 330, "comment": 360, "count": 320, "plaincap": 1150, "tooltag": 120, "outline": 400,
    "params": 330, "storyboard": 300, "masthead": 240, "chart": 1180, "blurword": 1000, "hud": 300,
    "sidebar": 420, "phone": 300, "countup": 700, "strikestamp": 620, "item": 780, "headline": 420,
    "ghost": 500, "gate": 660, "checklist": 420, "kinetic": 700, "scriptblock": 520, "stamp": 760,
    "numeral": 300,
}
# which prop carries the words, in label priority order
TEXT_KEYS = ["text", "title", "name", "word", "script", "block", "words", "label", "handle", "url", "n", "to", "reply"]
# chrome that is NOT a hook element even when it is on screen at frame 4
CHROME = {"hud", "ghost", "sidebar", "corners", "badge", "wall", "bgreplace", "vertigo", "iris", "negflash",
          "zoomthrough", "hudzoom", "slider", "grid", "orbit", "quad", "framebreak", "pullback", "beforeafter", "pip", "phone"}
# boxes that must not sit on top of one another
CARDS = {"item", "strikestamp", "spec", "logo", "photo", "browser", "params", "storyboard", "strike", "checklist",
         "count", "lowerthird", "gate", "prompt", "comment", "chart", "sidebar", "phone"}
DEFAULT_X = {"item": 72, "strikestamp": 72, "spec": 90, "logo": 120, "photo": 140, "browser": 60, "params": 60,
             "storyboard": 50, "strike": 110, "checklist": 72, "count": 90, "lowerthird": 72, "gate": 100,
             "prompt": 60, "comment": 60, "chart": 72, "sidebar": 72, "phone": 240}
DEFAULT_W = {"item": 936, "strikestamp": 936, "spec": 900, "logo": 840, "photo": 800, "browser": 960, "params": 960,
             "storyboard": 980, "strike": 860, "checklist": 936, "count": 420, "lowerthird": 700, "gate": 880,
             "prompt": 960, "comment": 960, "chart": 936, "sidebar": 936, "phone": 600}


def est_height(o):
    """Rough rendered height of an overlay from its type + props (good enough for a floor warning)."""
    t, p = o["type"], o.get("props") or {}
    n_items = len(p.get("items") or [])
    n_rows = len(p.get("rows") or [])
    size = p.get("size")
    if t == "sidebar":
        cols = p.get("cols", 2); s = size or 24
        return math.ceil(max(1, n_items) / cols) * s * 1.55
    if t == "item":
        return 230 + (60 if p.get("chips") else 0) + (40 if p.get("foot") else 0) + (20 if p.get("count") else 0)
    if t == "strikestamp": return 110
    if t == "gate": return 250 + 210
    if t == "lowerthird": return 120 if p.get("title") else 90
    if t in ("headline", "plaincap"): return (size or (60 if t == "headline" else 60)) * 1.2 * 2
    if t == "quote": return (size or 76) * 1.3 * 2
    if t == "chart": return p.get("h", 300) + 60
    if t == "checklist": return 70 + max(1, n_rows) * 60
    if t in ("spec", "storyboard", "params"): return 90 + max(1, n_rows) * 56
    if t == "strike": return 90 + max(1, n_items) * 56
    if t in ("masthead", "ghost", "outline", "blurword", "stamp"):
        base = {"masthead": 320, "ghost": 330, "outline": 360, "blurword": 110, "stamp": 160}[t]
        return (size or base) * 1.05 + (len(p.get("lines") or []) * 40 if t == "masthead" else 0)
    if t == "kinetic": return (size or 120) * 1.15
    if t in ("count", "numeral", "countup"): return 220
    if t in ("logo", "photo"): return p.get("w", 800) * 0.72
    if t == "browser": return p.get("w", 960) * 0.62
    if t == "hud": return 44
    if t == "scriptblock": return 260
    if t in ("prompt", "comment"): return 130
    if t == "phone": return p.get("w", 600) * 16 / 9
    return 120


def overlay_box(o):
    """(x, top, w, bottom) or None for full-frame effects with no y of their own."""
    t, p = o["type"], o.get("props") or {}
    if "y" not in p and t not in DEFAULT_Y: return None
    y = p.get("y", DEFAULT_Y.get(t, 0)); x = p.get("x", DEFAULT_X.get(t, 0)); w = p.get("w", DEFAULT_W.get(t, W))
    return x, y, w, y + est_height(o)


def has_text(o):
    p = o.get("props") or {}
    return any(k in p for k in TEXT_KEYS) or bool(p.get("items")) or bool(p.get("rows"))


def short_prop(o, n=34):
    p = o.get("props") or {}
    for k in TEXT_KEYS:
        if k in p and p[k] not in (None, ""):
            v = p[k]
            if isinstance(v, list): v = " ".join(str(x) for x in v)
            s = f"{k}={v}" if k not in ("text", "title", "name", "word") else str(v)
            break
    else:
        if "count" in p and "total" in p: s = f"{p['count']}/{p['total']}"
        elif p.get("items"): s = f"{len(p['items'])} items, #{p.get('current', '?')}"
        elif p.get("rows"): s = f"{len(p['rows'])} rows"
        elif p.get("tiles"): s = f"{len(p['tiles'])} tiles"
        elif p.get("values"): s = f"{len(p['values'])} values"
        elif p.get("src"): s = os.path.basename(str(p["src"]))
        elif p.get("bg"): s = f"bg={os.path.basename(str(p['bg']))}"
        elif "to" in p: s = f"to={p['to']}"
        else: s = ""
    s = " ".join(str(s).split())
    return s if len(s) <= n else s[: n - 1] + "~"


# ---------- props, duration, frame picking ----------
def probe_duration(path):
    out = subprocess.run([FFPROBE, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                         capture_output=True, text=True, check=True).stdout.strip()
    return float(out)


def load_props(path, comp):
    d = json.load(open(path, encoding="utf-8"))
    if not comp: comp = "RivalReel" if d.get("plate") else "CardReel"
    fps = d.get("fps", 30)
    if comp == "CardReel":
        dur = float(d["durationSec"]); total = math.ceil(dur * fps); last = total - 1
    else:
        plate = os.path.join(KIT, "public", d["plate"])
        dur = probe_duration(plate); total = math.ceil(dur * fps)
        # the composition takes its length from the browser's idea of the plate duration, which can land one frame
        # short of ffprobe's, so the "last" tile sits two frames back to never ask for a frame that is not there
        last = max(0, int(dur * fps) - 2)
    return d, comp, fps, dur, total, last


def pick_frames(d, fps, total, last, extra, max_tiles):
    """Returns ordered list of dicts {frame, why} after dedupe (10 f) and thinning to max_tiles."""
    cands = [(HOOK_FRAME, "hook"), (last, "last")]
    for i, o in enumerate(d.get("overlays") or []):
        fr = int(round((o["at"] + extra) * fps))
        if fr >= total: fr = last
        cands.append((fr, f"ov{i}"))
    cands.sort(key=lambda c: (c[0], 0 if c[1] in ("hook", "last") else 1))
    kept = []   # [frame, [whys]]
    for fr, why in cands:
        if kept and abs(fr - kept[-1][0]) < DEDUPE_FRAMES and why not in ("hook", "last"):
            kept[-1][1].append(why); continue
        if kept and why in ("hook", "last") and abs(fr - kept[-1][0]) < DEDUPE_FRAMES and kept[-1][1][0] not in ("hook", "last"):
            # the hook or last frame wins the slot, the overlay start is folded into it
            kept[-1] = [fr, [why] + kept[-1][1]]; continue
        if kept and abs(fr - kept[-1][0]) < DEDUPE_FRAMES: kept[-1][1].append(why); continue
        kept.append([fr, [why]])
    # thin to max by dropping whichever tile has the nearest neighbour (hook + last are pinned)
    def pinned(k): return any(w in ("hook", "last") for w in k[1])
    while len(kept) > max_tiles:
        best, bi = None, None
        for i, k in enumerate(kept):
            if pinned(k): continue
            gap = min(abs(k[0] - kept[j][0]) for j in (i - 1, i + 1) if 0 <= j < len(kept))
            if best is None or gap < best: best, bi = gap, i
        if bi is None: break
        kept[bi - 1][1].extend(kept[bi][1]); del kept[bi]
    return [{"frame": k[0], "whys": k[1]} for k in kept]


def active(d, fps, frame):
    t = frame / fps
    ovs = [(i, o) for i, o in enumerate(d.get("overlays") or []) if o["at"] <= t < o["at"] + o["dur"]]
    caps = [c for c in d.get("captions") or [] if c["start"] <= t < c["end"]]
    return ovs, caps


# ---------- lint ----------
def lint(d, fps, tiles, reg):
    warns = []   # (tile_no or None, text)
    ovs = d.get("overlays") or []
    def tile_for(o):
        for n, tl in enumerate(tiles, 1):
            if o["at"] <= tl["frame"] / fps < o["at"] + o["dur"]: return n
        return None
    # unknown types render nothing
    for i, o in enumerate(ovs):
        if reg and o["type"] not in reg:
            warns.append((tile_for(o), f"ov{i} type '{o['type']}' is not in REG, it will render nothing"))
    # text below the floor
    for i, o in enumerate(ovs):
        box = overlay_box(o)
        if not box or not has_text(o) or o["type"] == "ghost": continue
        x, top, w, bottom = box
        if bottom > TEXT_FLOOR:
            warns.append((tile_for(o), f"ov{i} {o['type']} '{short_prop(o)}' y={int(top)} est. bottom {int(bottom)} is below the {TEXT_FLOOR} text floor"))
    for j, c in enumerate(d.get("captions") or []):
        style = c.get("style") or d.get("captionStyle") or ("plain" if not d.get("plate") else "pill")
        y = c.get("y", 1150 if style == "plain" else 1230)
        bottom = y + (150 if style == "plain" else 90)
        if bottom > TEXT_FLOOR:
            warns.append((None, f"caption {j} '{c['text']}' y={y} est. bottom {int(bottom)} is below the {TEXT_FLOOR} text floor"))
    # hook frame: one element only
    hook_ovs, hook_caps = active(d, fps, HOOK_FRAME)
    hook = [f"{o['type']} '{short_prop(o)}'" for i, o in hook_ovs if o["type"] not in CHROME and not o.get("behind") and has_text(o)]
    hook += [f"caption '{c['text']}'" for c in hook_caps]
    if len(hook) > 1:
        warns.append((1, f"frame {HOOK_FRAME} carries {len(hook)} hook elements, the playbook wants one: " + "; ".join(hook)))
    if not hook and not hook_ovs:
        warns.append((1, f"frame {HOOK_FRAME} has nothing on it, the hook lands late"))
    # cards overlapping, checked at every overlay start
    seen = set()
    for o in ovs:
        t = o["at"] + 0.01
        live = [(i, p) for i, p in enumerate(ovs) if p["at"] <= t < p["at"] + p["dur"] and p["type"] in CARDS]
        for a in range(len(live)):
            for b in range(a + 1, len(live)):
                ia, pa = live[a]; ib, pb = live[b]
                if (ia, ib) in seen: continue
                A, B = overlay_box(pa), overlay_box(pb)
                if not A or not B: continue
                ox = min(A[0] + A[2], B[0] + B[2]) - max(A[0], B[0])
                oy = min(A[3], B[3]) - max(A[1], B[1])
                if ox > 12 and oy > 12:
                    seen.add((ia, ib))
                    warns.append((tile_for(pa), f"ov{ia} {pa['type']} '{short_prop(pa)}' and ov{ib} {pb['type']} '{short_prop(pb)}' overlap by ~{int(oy)} px from t={pa['at']}s"))
    # overlays running past the end
    total_s = (d.get("durationSec") if "durationSec" in d else None)
    if total_s:
        for i, o in enumerate(ovs):
            if o["at"] + o["dur"] > total_s + 0.05:
                warns.append((tile_for(o), f"ov{i} {o['type']} ends at {o['at'] + o['dur']:.2f}s, past the {total_s}s reel"))
    return warns


def read_reg():
    try:
        src = open(os.path.join(KIT, "src", "RivalReel.tsx"), encoding="utf-8").read()
        body = re.search(r"REG: Record<string, React\.FC<any>> = \{(.*?)\n\};", src, re.S).group(1)
        return set(re.findall(r"(?:^|[,{\s])([a-z]+):\s*[A-Z]", body, re.M))
    except Exception:
        return set()


# ---------- render ----------
def render_frames(comp, props_path, frames, workdir, log):
    npx = shutil.which("npx") or "npx"
    cmd = [npx, "remotion", "render", "src/index.ts", comp, workdir, f"--props={props_path}", "--image-sequence",
           "--image-format=png", f"--frames={','.join(str(f) for f in frames)}", "--log=error"]
    t0 = time.time()
    r = subprocess.run(cmd, cwd=KIT, capture_output=True, text=True)
    dt = time.time() - t0
    if r.returncode != 0:
        sys.stderr.write(r.stdout + r.stderr); raise SystemExit(f"remotion render failed ({r.returncode})")
    got = {}
    for f in glob.glob(os.path.join(workdir, "element-*.png")):
        m = re.search(r"element-(\d+)\.png$", f)
        if m: got[int(m.group(1))] = f
    missing = [f for f in frames if f not in got]
    if missing: raise SystemExit(f"remotion did not write frames {missing}; files: {sorted(got)}")
    log(f"rendered {len(frames)} frames in {dt:.1f}s ({dt / len(frames):.2f}s per frame)")
    return got, dt


# ---------- tiles + sheet (Pillow) ----------
def tile_info(d, fps, tl, n):
    ovs, caps = active(d, fps, tl["frame"])
    starters = [int(w[2:]) for w in tl["whys"] if w.startswith("ov")]
    why = []
    if "hook" in tl["whys"]: why.append("HOOK")
    if "last" in tl["whys"]: why.append("LAST")
    allov = d.get("overlays") or []
    lead = None
    for i in starters:
        o = allov[i]
        if o["type"] not in CHROME: lead = o; break
    if lead is None and starters: lead = allov[starters[0]]
    if lead is None:
        # prefer a front, non-chrome overlay; then anything behind; then whatever is on screen
        for pick in (lambda o: o["type"] not in CHROME and not o.get("behind"), lambda o: o["type"] not in CHROME, lambda o: True):
            for i, o in ovs:
                if pick(o): lead = o; break
            if lead: break
    return {"n": n, "frame": tl["frame"], "t": tl["frame"] / fps, "why": why, "starters": starters, "lead": lead,
            "active": ovs, "caps": caps}


def label_lines(info):
    l1 = f"#{info['n']}  {info['t']:.2f}s  f{info['frame']}" + (("  " + " ".join(info["why"])) if info["why"] else "")
    if info["lead"]:
        o = info["lead"]; l2 = f"{o['type']}: {short_prop(o, 30)}" + ("  [behind]" if o.get("behind") else "")
    else:
        l2 = "(no overlay)"
    others = [o["type"] + ("*" if o.get("behind") else "") for i, o in info["active"] if o is not info["lead"]]
    l3 = ("+ " + ", ".join(others)) if others else ""
    if info["caps"]: l3 = (l3 + "  " if l3 else "") + "cap: " + short_prop({"props": {"text": info["caps"][0]["text"]}}, 22)
    return l1, l2, l3


def build_sheet_pil(d, fps, tiles, files, out_png, cols, tile_w, title, warns):
    from PIL import Image, ImageDraw, ImageFont
    def font(name, size):
        try: return ImageFont.truetype(os.path.join(FONTS, name), size)
        except Exception: return ImageFont.load_default()
    fb, fr, fm = font("arialbd.ttf", 15), font("arial.ttf", 13), font("consola.ttf", 12)
    fh, fhs = font("arialbd.ttf", 22), font("arial.ttf", 14)
    th = round(tile_w * H / W); strip = 66; gap = 10; head = 64
    def fit(s, f, maxw):
        """Truncate s with a trailing ~ so it fits in maxw px of font f (the strip must not run into the next tile)."""
        if f.getlength(s) <= maxw: return s
        while s and f.getlength(s + "~") > maxw: s = s[:-1]
        return s.rstrip() + "~"
    rows = math.ceil(len(tiles) / cols)
    sw = cols * tile_w + (cols + 1) * gap
    sh = head + rows * (th + strip + gap) + gap
    sheet = Image.new("RGB", (sw, sh), (24, 24, 26)); dr = ImageDraw.Draw(sheet)
    dr.text((gap, 12), title, font=fh, fill=(240, 236, 226))
    legend = f"solid red = {TEXT_FLOOR} text floor    dashed red = {GRID_TOP} top of grid-safe band    * = behind the cutout    {len(warns)} lint warning(s), see the .md"
    dr.text((gap, 42), legend, font=fhs, fill=(170, 170, 175))
    warned_tiles = {w[0] for w in warns if w[0]}
    for idx, tl in enumerate(tiles):
        info = tile_info(d, fps, tl, idx + 1)
        r, c = divmod(idx, cols)
        x0 = gap + c * (tile_w + gap); y0 = head + r * (th + strip + gap)
        im = Image.open(files[tl["frame"]]).convert("RGB").resize((tile_w, th), Image.LANCZOS)
        sheet.paste(im, (x0, y0))
        # safe lines
        yf = y0 + round(TEXT_FLOOR * th / H); yg = y0 + round(GRID_TOP * th / H)
        dr.line([(x0, yf), (x0 + tile_w, yf)], fill=RED, width=2)
        for xx in range(x0, x0 + tile_w, 8): dr.line([(xx, yg), (min(xx + 4, x0 + tile_w), yg)], fill=RED, width=1)
        dr.text((x0 + tile_w - 30, yf - 14), "1440", font=fm, fill=RED)
        dr.text((x0 + tile_w - 24, yg + 2), "480", font=fm, fill=RED)
        # tile number badge
        dr.rectangle([x0, y0, x0 + 34, y0 + 22], fill=(255, 221, 51) if idx + 1 not in warned_tiles else RED)
        dr.text((x0 + 4, y0 + 3), f"{idx + 1:02d}", font=fb, fill=(0, 0, 0))
        # label strip
        dr.rectangle([x0, y0 + th, x0 + tile_w, y0 + th + strip], fill=(38, 38, 42))
        l1, l2, l3 = label_lines(info); maxw = tile_w - 12
        dr.text((x0 + 6, y0 + th + 4), fit(l1, fb, maxw), font=fb, fill=(240, 236, 226))
        dr.text((x0 + 6, y0 + th + 24), fit(l2, fr, maxw), font=fr, fill=(255, 221, 51) if info["lead"] else (150, 150, 155))
        dr.text((x0 + 6, y0 + th + 43), fit(l3, fm, maxw), font=fm, fill=(170, 170, 175))
        dr.rectangle([x0, y0, x0 + tile_w - 1, y0 + th + strip - 1], outline=(70, 70, 75))
    sheet.save(out_png, optimize=True)


# ---------- tiles + sheet (ffmpeg fallback, no Pillow) ----------
def _ff_esc(s):
    return str(s).replace("\\", "\\\\").replace(":", "\\:").replace("'", "\u2019").replace("%", "%%").replace(",", "\\,")


def build_sheet_ffmpeg(d, fps, tiles, files, out_png, cols, tile_w, title, warns, workdir):
    th = round(tile_w * H / W); strip = 66
    font = (FONTS + "/arial.ttf").replace("\\", "/").replace(":", "\\:")
    yf = round(TEXT_FLOOR * th / H); yg = round(GRID_TOP * th / H)
    for idx, tl in enumerate(tiles):
        info = tile_info(d, fps, tl, idx + 1); l1, l2, l3 = label_lines(info)
        vf = (f"scale={tile_w}:{th},pad={tile_w}:{th + strip}:0:0:0x262628,"
              f"drawbox=x=0:y={yf}:w={tile_w}:h=2:color=0xE22C2C@1:t=fill,"
              f"drawbox=x=0:y={yg}:w={tile_w}:h=1:color=0xE22C2C@0.8:t=fill,"
              f"drawtext=fontfile='{font}':text='{_ff_esc(l1)}':x=6:y={th + 4}:fontsize=15:fontcolor=white,"
              f"drawtext=fontfile='{font}':text='{_ff_esc(l2)}':x=6:y={th + 24}:fontsize=13:fontcolor=0xFFDD33,"
              f"drawtext=fontfile='{font}':text='{_ff_esc(l3)}':x=6:y={th + 43}:fontsize=12:fontcolor=0xAAAAAF")
        subprocess.run([FFMPEG, "-y", "-v", "error", "-i", files[tl["frame"]], "-vf", vf,
                        os.path.join(workdir, f"tile-{idx:03d}.png")], check=True)
    rows = math.ceil(len(tiles) / cols)
    subprocess.run([FFMPEG, "-y", "-v", "error", "-framerate", "1", "-i", os.path.join(workdir, "tile-%03d.png"),
                    "-vf", f"tile={cols}x{rows}:padding=10:margin=10:color=0x18181A,"
                           f"pad=iw:ih+40:0:40:0x18181A,drawtext=fontfile='{font}':text='{_ff_esc(title)}':x=10:y=10:fontsize=22:fontcolor=white",
                    "-frames:v", "1", out_png], check=True)


# ---------- markdown ----------
def write_md(path, d, comp, fps, dur, tiles, warns, render_s, sheet_png, props_path):
    L = [f"# Artboard: {os.path.basename(sheet_png)}", "",
         f"props: `{props_path}`  ", f"composition: {comp}, {dur:.2f}s at {fps} fps ({math.ceil(dur * fps)} frames), "
         f"{len(d.get('overlays') or [])} overlays, {len(d.get('captions') or [])} captions  ",
         f"tiles: {len(tiles)} rendered in {render_s:.1f}s  ", f"sheet: `{sheet_png}`", "",
         "Redline by tile number: reply with the number and the change (\"07: drop the item card to y 820\", \"12: kill the caption\").", "",
         "## Tiles", "", "| # | time | frame | why | lead overlay | also on screen | caption |", "|---|---|---|---|---|---|---|"]
    allov = d.get("overlays") or []
    for idx, tl in enumerate(tiles):
        info = tile_info(d, fps, tl, idx + 1)
        why = " ".join(info["why"] + [f"ov{i} {allov[i]['type']} starts" for i in info["starters"]]) or "overlay start"
        lead = f"{info['lead']['type']}: {short_prop(info['lead'], 48)}" + (" (behind)" if info["lead"] and info["lead"].get("behind") else "") if info["lead"] else ""
        also = ", ".join(f"{o['type']}" + ("*" if o.get("behind") else "") + (f" ({short_prop(o, 20)})" if short_prop(o, 20) else "")
                         for i, o in info["active"] if o is not info["lead"])
        cap = "; ".join(c["text"] for c in info["caps"])
        L.append(f"| {idx + 1:02d} | {info['t']:.2f}s | {info['frame']} | {why} | {lead} | {also} | {cap} |")
    L += ["", "\\* = behind the cutout (RivalReel only)", "", "## Lint", ""]
    if not warns: L.append("clean: no text below 1440, one hook element at frame 4, no card overlaps")
    for t, w in warns: L.append(f"- {'tile ' + f'{t:02d}' if t else 'timeline'}: {w}")
    L += ["", "Heights in the lint are estimates from the component defaults, not measured pixels. The sheet is the truth; the lint just points at what to look at first.", ""]
    open(path, "w", encoding="utf-8").write("\n".join(L))


# ---------- main ----------
def main():
    global KIT
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("props"); ap.add_argument("--comp", choices=["CardReel", "RivalReel"])
    ap.add_argument("--out"); ap.add_argument("--cols", type=int, default=6); ap.add_argument("--max", type=int, default=24)
    ap.add_argument("--extra", type=float, default=0.5); ap.add_argument("--tile", type=int, default=320)
    ap.add_argument("--kit", default=KIT); ap.add_argument("--keep", action="store_true", help="keep the rendered frames folder")
    ap.add_argument("--no-pil", action="store_true", help="force the ffmpeg labelling path")
    a = ap.parse_args()
    KIT = os.path.abspath(a.kit)

    use_pil = not a.no_pil
    if use_pil:
        try: import PIL  # noqa
        except ImportError:
            if os.path.exists(VENV_PY) and os.path.abspath(sys.executable).lower() != os.path.abspath(VENV_PY).lower():
                # os.execv does not block on Windows, so hand off and wait
                raise SystemExit(subprocess.run([VENV_PY, "-I", os.path.abspath(__file__)] + sys.argv[1:]).returncode)
            use_pil = False; print("Pillow not found, using ffmpeg labels")

    props_path = os.path.abspath(a.props)
    name = re.sub(r"\.props$", "", os.path.splitext(os.path.basename(props_path))[0])
    out_dir = os.path.abspath(a.out) if a.out else os.path.dirname(props_path); os.makedirs(out_dir, exist_ok=True)
    out_png = os.path.join(out_dir, f"{name}-artboard.png"); out_md = os.path.join(out_dir, f"{name}-artboard.md")
    log = lambda s: print(s, flush=True)

    d, comp, fps, dur, total, last = load_props(props_path, a.comp)
    tiles = pick_frames(d, fps, total, last, a.extra, a.max)
    log(f"{name}: {comp} {dur:.2f}s @ {fps} fps, {len(d.get('overlays') or [])} overlays -> {len(tiles)} tiles: "
        + ",".join(str(t['frame']) for t in tiles))
    warns = lint(d, fps, tiles, read_reg())

    workdir = tempfile.mkdtemp(prefix="artboard-")
    try:
        files, render_s = render_frames(comp, props_path, [t["frame"] for t in tiles], workdir, log)
        t0 = time.time()
        title = f"{name}  |  {comp}  {dur:.2f}s  |  {len(tiles)} planned frames  |  {time.strftime('%Y-%m-%d %H:%M')}"
        if use_pil: build_sheet_pil(d, fps, tiles, files, out_png, a.cols, a.tile, title, warns)
        else: build_sheet_ffmpeg(d, fps, tiles, files, out_png, a.cols, a.tile, title, warns, workdir)
        log(f"sheet built in {time.time() - t0:.1f}s")
    finally:
        if a.keep: log(f"frames kept in {workdir}")
        else: shutil.rmtree(workdir, ignore_errors=True)
    write_md(out_md, d, comp, fps, dur, tiles, warns, render_s, out_png, props_path)
    for t, w in warns: log(f"  lint {'tile %02d' % t if t else 'timeline'}: {w}")
    log(f"wrote {out_png}\nwrote {out_md}")


if __name__ == "__main__":
    main()
