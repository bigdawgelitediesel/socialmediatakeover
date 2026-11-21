"""matte.py - person cutout of a plate as a VP9 WebM with alpha, via Robust Video Matting (ONNX, CPU).
usage: python -I matte.py <plate.mp4> <out.webm> [--ds 0.25]
The WebM layers into Remotion with <OffthreadVideo transparent>, so text can sit BEHIND the subject."""
import sys, os, subprocess, numpy as np, cv2, onnxruntime as ort
BIN = os.path.join(os.environ["LOCALAPPDATA"], r"Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin")
FF = os.path.join(BIN, "ffmpeg.exe")
HERE = os.path.dirname(os.path.abspath(__file__))
src, out = sys.argv[1], sys.argv[2]
ds = float(sys.argv[sys.argv.index("--ds") + 1]) if "--ds" in sys.argv else 0.25
sess = ort.InferenceSession(os.path.join(HERE, "models", "rvm_mobilenetv3_fp32.onnx"), providers=["CPUExecutionProvider"])
cap = cv2.VideoCapture(src); fps = cap.get(cv2.CAP_PROP_FPS) or 30; W = int(cap.get(3)); H = int(cap.get(4)); N = int(cap.get(7))
enc = subprocess.Popen([FF, "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{W}x{H}", "-r", f"{fps}", "-i", "-",
                        "-c:v", "libvpx-vp9", "-pix_fmt", "yuva420p", "-b:v", "0", "-crf", "24", "-row-mt", "1", "-deadline", "good", "-cpu-used", "4", "-auto-alt-ref", "0", out], stdin=subprocess.PIPE)
rec = [np.zeros([1, 1, 1, 1], dtype=np.float32)] * 4; dsr = np.array([ds], dtype=np.float32); i = 0
while True:
    ok, fr = cap.read()
    if not ok: break
    rgb = cv2.cvtColor(fr, cv2.COLOR_BGR2RGB)
    x = np.transpose(rgb.astype(np.float32) / 255.0, (2, 0, 1))[None]
    fgr, pha, *rec = sess.run(None, {"src": x, "r1i": rec[0], "r2i": rec[1], "r3i": rec[2], "r4i": rec[3], "downsample_ratio": dsr})
    a = pha[0, 0]
    a = cv2.GaussianBlur(a, (0, 0), 1.2)                       # soften the edge a hair
    rgba = np.dstack([rgb, (np.clip(a, 0, 1) * 255).astype(np.uint8)])
    enc.stdin.write(rgba.tobytes()); i += 1
    if i % 100 == 0: print(f"  matte {i}/{N}", flush=True)
enc.stdin.close(); enc.wait()
print(f"wrote {out} ({i} frames)")
