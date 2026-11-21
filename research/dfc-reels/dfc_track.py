"""dfc_track.py - multi-face track + active-speaker guess for a landscape interview, for 9:16 reframing.
usage: python -I dfc_track.py <video> <out.json> [--hz 10] [--t0 S] [--t1 S]
Writes {"hz":10, "w":W, "h":H, "samples":[{"t":..,"faces":[[x,y,w,h,mouth_motion],...],"speaker":i|null}, ...]}
Speaker = the face whose mouth region changed most since the previous sample (smoothed over ~1 s)."""
import sys, os, json, cv2, numpy as np
src, out = sys.argv[1], sys.argv[2]
hz = float(sys.argv[sys.argv.index("--hz") + 1]) if "--hz" in sys.argv else 10.0
t0 = float(sys.argv[sys.argv.index("--t0") + 1]) if "--t0" in sys.argv else 0.0
t1 = float(sys.argv[sys.argv.index("--t1") + 1]) if "--t1" in sys.argv else 1e9
HERE = os.path.dirname(os.path.abspath(__file__))
model = os.path.join(HERE, "models", "face_detection_yunet_2023mar.onnx")
cap = cv2.VideoCapture(src); fps = cap.get(cv2.CAP_PROP_FPS); W = int(cap.get(3)); H = int(cap.get(4)); N = int(cap.get(7))
step = max(1, int(round(fps / hz)))
DS = 0.5
det = cv2.FaceDetectorYN.create(model, "", (int(W * DS), int(H * DS)), 0.7, 0.3, 50)
samples, prev_mouths, i = [], {}, 0
cap.set(cv2.CAP_PROP_POS_FRAMES, int(t0 * fps)); i = int(t0 * fps)
while True:
    ok = cap.grab()
    if not ok or i / fps > t1: break
    if i % step == 0:
        ok, fr = cap.retrieve()
        if not ok: break
        small = cv2.resize(fr, (int(W * DS), int(H * DS)))
        _, faces = det.detect(small)
        faces = [] if faces is None else faces
        gray = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
        rows, mouths = [], {}
        for f in sorted(faces, key=lambda f: f[0])[:3]:
            x, y, w, h = [int(v / DS) for v in f[:4]]
            if w < 40: continue
            # mouth region: lower third of the box; compare with the previous sample's mouth for the nearest face
            mx0, mx1, my0, my1 = x + int(w * 0.2), x + int(w * 0.8), y + int(h * 0.62), y + int(h * 0.95)
            m = cv2.resize(gray[max(0, my0):my1, max(0, mx0):mx1], (32, 16)).astype(np.float32) if my1 > my0 and mx1 > mx0 else None
            key = round((x + w / 2) / 200)   # coarse x bucket to match faces between samples
            motion = 0.0
            if m is not None:
                pm = prev_mouths.get(key)
                if pm is not None: motion = float(np.mean(np.abs(m - pm)))
                mouths[key] = m
            rows.append([x, y, w, h, round(motion, 2)])
        prev_mouths = mouths
        samples.append({"t": round(i / fps, 2), "faces": rows})
        if len(samples) % 500 == 0: print(f"  {len(samples)} samples, t={i / fps:.0f}s", flush=True)
    i += 1
# smooth the speaker guess: for each sample, pick the face with the highest mouth motion summed over +-5 samples (about 1 s)
K = 5
for idx, s in enumerate(samples):
    if not s["faces"]: s["speaker"] = None; continue
    best, best_v = None, -1
    for fi, f in enumerate(s["faces"]):
        cx = f[0] + f[2] / 2; v = 0.0
        for j in range(max(0, idx - K), min(len(samples), idx + K + 1)):
            for g in samples[j]["faces"]:
                if abs((g[0] + g[2] / 2) - cx) < 160: v += g[4]
        if v > best_v: best, best_v = fi, v
    s["speaker"] = best
json.dump({"hz": hz, "w": W, "h": H, "samples": samples}, open(out, "w"))
print(f"wrote {out}: {len(samples)} samples, {sum(1 for s in samples if len(s['faces']) >= 2)} with 2+ faces")
