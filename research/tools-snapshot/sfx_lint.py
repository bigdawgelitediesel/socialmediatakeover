#!/usr/bin/env python
"""sfx_lint.py: independent timing check of an sfx track against the events that made it.

    "%LOCALAPPDATA%\\Programs\\Python\\Python312\\python.exe" -I sfx_lint.py events.json sfx_track.wav [--fps 30] [--tol 0.5]

Does not read placement.txt or kit.json. For each event it scans the rendered track itself around the expected anchor
(whoosh: loudest 5 ms at -2 frames; hit/stamp: loudest 5 ms on `at`; riser: last audible 1 ms at -2 frames;
pop/tick/click/notify: first audible 1 ms on `at`) inside a window of +-6 frames and reports the delta in frames.
Exit code 1 if any |delta| > --tol frames. Also reports the track's sample peak and the loudest 1 s window count.
"""
import argparse
import math
import struct
import sys
from pathlib import Path

import numpy as np

SR = 48000
RULE = {"whoosh": ("peak", -2), "hit": ("peak", 0), "stamp": ("peak", 0), "riser": ("end", -2),
        "pop": ("onset", 0), "tick": ("onset", 0), "click": ("onset", 0), "notify": ("onset", 0)}


def read_wav(path):
    data = Path(path).read_bytes()
    pos, fmt, raw = 12, None, None
    while pos + 8 <= len(data):
        cid, size = data[pos:pos + 4], struct.unpack("<I", data[pos + 4:pos + 8])[0]
        if cid == b"fmt ":
            fmt = struct.unpack("<HHIIHH", data[pos + 8:pos + 24])
        elif cid == b"data":
            raw = data[pos + 8:pos + 8 + size]
        pos += 8 + size + (size & 1)
    tag, ch, sr, _, _, bits = fmt
    assert sr == SR, f"expected 48 kHz, got {sr}"
    if tag == 3:
        x = np.frombuffer(raw, dtype="<f4").astype(np.float64)
    elif bits == 16:
        x = np.frombuffer(raw, dtype="<i2").astype(np.float64) / 32768.0
    elif bits == 24:
        b = np.frombuffer(raw, dtype=np.uint8).reshape(-1, 3)
        i = b[:, 0].astype(np.int32) | (b[:, 1].astype(np.int32) << 8) | (b[:, 2].astype(np.int32) << 16)
        x = np.where(i >= 1 << 23, i - (1 << 24), i).astype(np.float64) / 8388608.0
    else:
        x = np.frombuffer(raw, dtype="<i4").astype(np.float64) / 2147483648.0
    return x.reshape(-1, ch).mean(axis=1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("events")
    ap.add_argument("track")
    ap.add_argument("--fps", type=float, default=30.0)
    ap.add_argument("--tol", type=float, default=0.5, help="max |delta| in frames before failing")
    ap.add_argument("--window", type=float, default=6, help="search window, frames either side of the anchor")
    a = ap.parse_args()
    import json
    ev = json.loads(Path(a.events).read_text(encoding="utf-8"))
    if isinstance(ev, dict):
        ev = ev.get("events") or ev.get("sfx") or ev.get("cues")
    mono = read_wav(a.track)
    fr = 1.0 / a.fps
    w5, w1 = int(0.005 * SR), int(0.001 * SR)
    env5 = np.sqrt(np.convolve(mono ** 2, np.ones(w5) / w5, mode="same"))
    env1 = np.sqrt(np.convolve(mono ** 2, np.ones(w1) / w1, mode="same"))
    win = int(a.window * fr * SR)
    bad = 0
    print(f"{'kind':8} {'at':>8} {'expect':>8} {'found':>8} {'delta_f':>8}  how")
    for e in sorted(ev, key=lambda e: float(e.get("at", e.get("t", 0)))):
        at = float(e.get("at", e.get("t")))
        kind = (e.get("kind") or e.get("type")).lower()
        what, off = RULE[kind]
        exp = at + off * fr
        c = int(round(exp * SR))
        lo, hi = max(0, c - win), min(len(mono), c + win)
        if what == "peak":
            i = lo + int(env5[lo:hi].argmax())
            how = "loudest 5 ms in window"
        else:
            # an onset is the steepest rise of the 1 ms envelope, an end (hard stop) the steepest fall; a step
            # measure is blind to a neighbour's tail sitting inside the window, which a plain threshold is not
            db = 20 * np.log10(env1 + 1e-7)
            k = int(0.002 * SR)
            step = db[lo + k:hi + k] - db[lo - k:hi - k] if lo >= k and hi + k <= len(db) else np.zeros(hi - lo)
            if what == "onset":
                i = lo + int(step.argmax()) + 1  # the sample after the steepest 4 ms rise
                how = "steepest 1 ms envelope rise"
            else:
                i = lo + int(step.argmin()) - 1
                how = "steepest 1 ms envelope fall"
        found = i / SR
        d = (found - exp) * a.fps
        flag = "" if abs(d) <= a.tol else "  <-- off"
        bad += abs(d) > a.tol
        print(f"{kind:8} {at:8.3f} {exp:8.4f} {found:8.4f} {d:+8.2f}  {how}{flag}")
    pk = 20 * math.log10(max(float(np.abs(mono).max()), 1e-9))
    print(f"track peak (mono sum) {pk:+.1f} dBFS, length {len(mono) / SR:.2f} s, {bad} event(s) outside +-{a.tol} frames")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
