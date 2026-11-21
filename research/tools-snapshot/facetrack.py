"""facetrack.py - face track for a talking-head plate (YuNet, OpenCV), 10 samples a second.
usage: python -I tools/facetrack.py <plate.mp4> <out.face.json> [--hz 10]
Writes [[t, x, y, w, h], ...] in plate pixels (null box when no face), the format tools/layout.py reads."""
import sys, os, json, cv2
HERE = os.path.dirname(os.path.abspath(__file__))
src, out = sys.argv[1], sys.argv[2]
hz = float(sys.argv[sys.argv.index("--hz") + 1]) if "--hz" in sys.argv else 10.0
cap = cv2.VideoCapture(src); fps = cap.get(cv2.CAP_PROP_FPS) or 30; W = int(cap.get(3)); H = int(cap.get(4)); N = int(cap.get(7))
det = cv2.FaceDetectorYN.create(os.path.join(HERE, "models", "face_detection_yunet_2023mar.onnx"), "", (W // 2, H // 2), 0.6, 0.3, 5000)
step = max(1, int(round(fps / hz))); rows = []; i = 0
while True:
    ok, fr = cap.read()
    if not ok: break
    if i % step == 0:
        small = cv2.resize(fr, (W // 2, H // 2)); _, faces = det.detect(small)
        t = round(i / fps, 2)
        if faces is not None and len(faces):
            f = max(faces, key=lambda r: r[2] * r[3])   # biggest face = Jacob
            rows.append([t, int(f[0] * 2), int(f[1] * 2), int(f[2] * 2), int(f[3] * 2)])
        else:
            rows.append([t, None, None, None, None])
    i += 1
json.dump(rows, open(out, "w"))
hit = sum(1 for r in rows if r[1] is not None)
print(f"wrote {out}: {len(rows)} samples, face found in {hit} ({100 * hit // max(1, len(rows))}%)")
