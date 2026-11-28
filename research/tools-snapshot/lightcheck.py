"""lightcheck.py - read the light on Jacob's face in a clip or a still, in numbers, before anything is cut.
Built 2026-11-23 from the @dash.directed "34 lighting styles" reel (Dfp6L7lol4F): the names are in Setup/LIGHTING.md.

usage: python -I tools/lightcheck.py <video-or-image> [t1 t2 ...]     (no times on a video = 5 evenly spaced frames)

Per frame it prints:
  face      mean brightness of the face, 0 to 255 (skin wants about 95 to 175)
  side      brighter side of the face and the ratio lit side : shadow side
  vert      forehead against chin (top light or under light)
  clip      percent of face pixels blown out (over 245) and crushed (under 12)
  bg        background brightness against the face (high key, low key, silhouette)
  cast      warm or cool tint on the skin
  name      the closest name from the lighting list, and a verdict for a talking head
It only measures. It never changes the picture (house rule: no colour grade)."""
import sys, os, subprocess, tempfile
os.environ.setdefault("OPENCV_LOG_LEVEL", "ERROR")
import numpy as np, cv2
HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.join(HERE, "models", "face_detection_yunet_2023mar.onnx")

def frames(src, times):
    if src.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
        return [("still", cv2.imread(src))]
    if not times:
        d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", src], capture_output=True, text=True).stdout.strip())
        times = [round(d * k / 6, 2) for k in range(1, 6)]
    out = []
    for t in times:
        p = os.path.join(tempfile.gettempdir(), "lc-%s.png" % str(t).replace(".", "_"))
        # tonemap HDR phone clips the same way the editor does, so the numbers match what gets posted
        probe = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=color_transfer", "-of", "csv=p=0", src], capture_output=True, text=True).stdout
        vf = "libplacebo=tonemapping=spline:colorspace=bt709:color_primaries=bt709:color_trc=bt709:range=tv:format=yuv420p," if ("b67" in probe or "2084" in probe) else ""
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", src, "-frames:v", "1", "-vf", vf + "scale=-2:1280", p], check=True)
        out.append((str(t), cv2.imread(p)))
    return out

def luma(bgr): return 0.0722 * bgr[..., 0] + 0.7152 * bgr[..., 1] + 0.2126 * bgr[..., 2]

def check(img):
    H, W = img.shape[:2]
    det = cv2.FaceDetectorYN.create(MODEL, "", (W, H), 0.6, 0.3, 5000)
    _, faces = det.detect(img)
    if faces is None or not len(faces): return None
    f = max(faces, key=lambda r: r[2] * r[3]); x, y, w, h = [int(v) for v in f[:4]]
    x, y = max(0, x), max(0, y); w, h = min(w, W - x), min(h, H - y)
    # the skin part of the box: drop the outer 12 percent each side (hair, ears, background)
    ix, iy, iw, ih = x + int(w * 0.12), y + int(h * 0.10), int(w * 0.76), int(h * 0.80)
    face = img[iy:iy + ih, ix:ix + iw].astype(np.float32); L = luma(face)
    left, right = L[:, : iw // 2].mean(), L[:, iw // 2:].mean()          # image left / right
    top, bot = L[: ih // 3].mean(), L[2 * ih // 3:].mean()
    hi, lo = max(left, right), max(1.0, min(left, right))
    mask = np.ones((H, W), bool); mask[max(0, y - h // 4): min(H, y + h + h // 2), max(0, x - w // 4): min(W, x + w + w // 4)] = False
    bg = luma(img.astype(np.float32))[mask].mean()
    b, g, r = [face[..., k].mean() for k in range(3)]
    r_ = {"face": L.mean(), "ratio": hi / lo, "side": "left of frame" if left > right else "right of frame", "vert": top / max(1.0, bot),
          "blown": 100.0 * (L > 245).mean(), "crushed": 100.0 * (L < 12).mean(), "bg": bg / max(1.0, L.mean()), "rb": r / max(1.0, b), "box": (x, y, w, h)}
    # names, from Setup/LIGHTING.md
    n = []
    if r_["bg"] > 1.8 and r_["face"] < 70: n.append("silhouette")
    elif r_["ratio"] >= 4.0: n.append("split light")
    elif r_["ratio"] >= 2.2: n.append("Rembrandt / short-light range (strong side light)")
    elif r_["ratio"] >= 1.35: n.append("loop light range (soft side light)")
    else: n.append("flat or butterfly (light from the front)")
    if r_["vert"] > 1.6: n.append("top light (forehead much brighter than chin)")
    if r_["vert"] < 0.45: n.append("forehead much darker than chin (cap brim shadow, or light from below)")
    if r_["bg"] > 1.25 and "silhouette" not in n: n.append("bright background (high key or backlit)")
    if r_["bg"] < 0.45: n.append("dark background (low key)")
    # verdict for a talking head
    v = []
    if r_["blown"] > 2.0: v.append("FACE BLOWN OUT (%.1f%% of skin is pure white): turn away from the sun or step into shade" % r_["blown"])
    if r_["face"] > 185: v.append("face too bright")
    if r_["face"] < 75: v.append("face too dark: turn toward the light")
    if r_["crushed"] > 8.0: v.append("part of the face is pure black")
    if r_["bg"] > 1.6 and r_["face"] < 110: v.append("backlit: the window or sky behind him is brighter than his face")
    if r_["vert"] > 1.6: v.append("overhead light: raccoon eyes risk, tip the face up or move out from under it")
    if r_["vert"] < 0.45 and r_["face"] < 110: v.append("eyes are in the cap shadow: tip the brim up or face the light")
    if r_["ratio"] > 3.2: v.append("half the face is lost: fine for a moody beat, wrong for a whole talking head")
    r_["name"] = "; ".join(n); r_["verdict"] = "; ".join(v) if v else "OK for a talking head"
    return r_

if __name__ == "__main__":
    src, times = sys.argv[1], sys.argv[2:]
    for t, img in frames(src, times):
        r = check(img)
        if r is None: print("%6s  no face found (silhouette, turned away, or too dark to see a face)" % t); continue
        cast = "warm" if r["rb"] > 1.75 else ("cool" if r["rb"] < 1.15 else "neutral")
        print("%6s  face %3.0f | brighter %s, %.1f : 1 | forehead/chin %.2f | blown %.1f%% crushed %.1f%% | bg/face %.2f | %s (R/B %.2f)"
              % (t, r["face"], r["side"], r["ratio"], r["vert"], r["blown"], r["crushed"], r["bg"], cast, r["rb"]))
        print("        looks like: %s" % r["name"]); print("        verdict:    %s" % r["verdict"])
