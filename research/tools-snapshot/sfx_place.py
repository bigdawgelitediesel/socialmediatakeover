#!/usr/bin/env python
"""sfx_place.py: place kit sounds on a reel timeline, frame-accurately, into one 48 kHz stereo wav.

    "%LOCALAPPDATA%\\Programs\\Python\\Python312\\python.exe" -I sfx_place.py events.json --kit sfx-kit --out sfx_track.wav
        [--fps 30] [--duration S] [--cuts N] [--style gritty|neutral|clean|any] [--mixed]
        [--placement placement.txt] [--seed 0] [--voice voice.wav]

EVENTS JSON (the format tools/words_to_props.py will emit; it does not exist yet, so this file defines it):
    [
      {"at": 0.5, "kind": "whoosh"},                       # seconds on the reel timeline, kind in KINDS
      {"at": 1.6, "kind": "stamp", "gain_db": -2},         # optional trim on top of the house peak
      {"at": 3.0, "kind": "riser", "file": "riser_long.wav"},   # optional: name a kit file instead of rotating
      {"at": 4.2, "kind": "pop", "variant": 1}             # optional: pick the n-th candidate of that kind
    ]
    Also accepted: {"events": [...]} or {"sfx": [...]} wrappers, and "t"/"time" for "at", "type" for "kind".

TIMING RULES (fps default 30, one frame = 33.33 ms):
    whoosh        its loudest 5 ms lands 2 frames BEFORE `at` (the cut), so the air is moving when the picture changes
    hit, stamp    its loudest 5 ms lands exactly ON `at`
    riser         its END lands 2 frames before `at`; those 2 frames are silence; the hit on `at` is a separate event
    pop, tick, click, notify   its onset (first 1 ms within 30 dB of the peak) STARTS at `at`

PEAKS (dBFS, sample peak, from the kit build): whoosh -10, pop -12, stamp/hit -7, tick/click -17, notify -12, riser -12.
    gain_db adds to that per event. The kit files are already at these peaks; this script only applies gain_db.

GUARDS:
    one style   the files used must not mix "gritty" (recordings) with "clean" (bright digital UI). "neutral" goes with
                either. Refuses unless --mixed.
    density     warns when more than one whoosh per 4 cuts (--cuts N; without it each whoosh is assumed to be a cut,
                so the check is skipped with a note) or more than 3 sounds start inside any 1 s window.
    clipping    if the summed track would pass -1 dBFS it is scaled down and a warning says by how much.

OUTPUT: the wav (48 kHz stereo 24-bit) and placement.txt: kind, file, requested time, anchor rule, actual anchor time
    measured on the rendered track, delta in frames. Feed placement.txt to sfx_lint.py (or read it) for the lint pass.

MIXING UNDER VOICE (documented command; no sidechain, a fixed -6 dB under voice, loudnorm to -14 at the end):
    --voice voice.wav prints the exact ffmpeg line for your files. Idea: measure the voice peak, put the SFX bus so the
    hottest kit sound (stamp/hit at -7 dBFS) sits 6 dB under the voice peak, then loudnorm the sum.
"""
import argparse
import json
import math
import os
import struct
import subprocess
import sys
from pathlib import Path

import numpy as np

SR = 48000
KINDS = ("whoosh", "pop", "stamp", "tick", "notify", "hit", "riser", "click")
ANCHOR = {"whoosh": "peak_before", "hit": "peak_on", "stamp": "peak_on", "riser": "end_before",
          "pop": "onset_on", "tick": "onset_on", "click": "onset_on", "notify": "onset_on"}
HOUSE_PEAK = {"whoosh": -10.0, "pop": -12.0, "stamp": -7.0, "hit": -7.0, "tick": -17.0, "notify": -12.0,
              "riser": -12.0, "click": -17.0}
FFMPEG = os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe"
                            r"\ffmpeg-9.0.2-full_build\bin\ffmpeg.exe")


def read_wav(path):
    """Reads PCM wav (16/24/32-bit int or 32-bit float) into float64 stereo at 48 kHz; falls back to ffmpeg."""
    data = Path(path).read_bytes()
    if data[:4] != b"RIFF" or data[8:12] != b"WAVE":
        return ffmpeg_decode(path)
    pos, fmt, raw = 12, None, None
    while pos + 8 <= len(data):
        cid, size = data[pos:pos + 4], struct.unpack("<I", data[pos + 4:pos + 8])[0]
        body = data[pos + 8:pos + 8 + size]
        if cid == b"fmt ":
            fmt = struct.unpack("<HHIIHH", body[:16])
        elif cid == b"data":
            raw = body
        pos += 8 + size + (size & 1)
    if fmt is None or raw is None:
        return ffmpeg_decode(path)
    tag, ch, sr, _, _, bits = fmt
    if sr != SR or tag not in (1, 3) or bits not in (16, 24, 32):
        return ffmpeg_decode(path)
    if tag == 3:
        x = np.frombuffer(raw, dtype="<f4").astype(np.float64)
    elif bits == 16:
        x = np.frombuffer(raw, dtype="<i2").astype(np.float64) / 32768.0
    elif bits == 32:
        x = np.frombuffer(raw, dtype="<i4").astype(np.float64) / 2147483648.0
    else:
        b = np.frombuffer(raw, dtype=np.uint8).reshape(-1, 3)
        i = (b[:, 0].astype(np.int32) | (b[:, 1].astype(np.int32) << 8) | (b[:, 2].astype(np.int32) << 16))
        i = np.where(i >= 1 << 23, i - (1 << 24), i)
        x = i.astype(np.float64) / 8388608.0
    x = x.reshape(-1, ch)
    if ch == 1:
        x = np.repeat(x, 2, axis=1)
    return x[:, :2]


def ffmpeg_decode(path):
    cmd = [FFMPEG, "-v", "error", "-i", str(path), "-f", "f32le", "-ac", "2", "-ar", str(SR), "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).reshape(-1, 2).astype(np.float64)


def write_wav24(path, x):
    x = np.clip(x, -1.0, 1.0)
    ints = np.round(x * 8388607.0).astype("<i4")
    arr = np.frombuffer(ints.tobytes(), dtype=np.uint8).reshape(-1, 4)[:, :3].tobytes()
    n = len(arr)
    hdr = (b"RIFF" + struct.pack("<I", 36 + n) + b"WAVE" + b"fmt "
           + struct.pack("<IHHIIHH", 16, 1, 2, SR, SR * 6, 6, 24))
    Path(path).write_bytes(hdr + b"data" + struct.pack("<I", n) + arr)


def measure(x):
    """onset (first 1 ms within 30 dB of the loudest), peak (loudest 5 ms), end (last 1 ms within 50 dB), seconds."""
    mono = x.mean(axis=1)
    w5 = int(0.005 * SR)
    env5 = np.sqrt(np.convolve(mono ** 2, np.ones(w5) / w5, mode="same"))
    w1 = int(0.001 * SR)
    env1 = np.sqrt(np.convolve(mono ** 2, np.ones(w1) / w1, mode="same"))
    top = env1.max()
    a30 = np.nonzero(env1 >= top * 10 ** (-30 / 20))[0]
    a50 = np.nonzero(env1 >= top * 10 ** (-50 / 20))[0]
    return dict(onset_s=(int(a30[0]) if len(a30) else 0) / SR, peak_s=int(env5.argmax()) / SR,
                end_s=(int(a50[-1]) if len(a50) else len(mono) - 1) / SR)


def load_kit(kit_dir):
    kit_dir = Path(kit_dir)
    kj = kit_dir / "kit.json"
    files = []
    if kj.exists():
        for r in json.loads(kj.read_text(encoding="utf-8"))["files"]:
            files.append(dict(r, path=kit_dir / r["file"]))
    else:
        # no kit.json: take every wav whose name starts with a kind, measure it now, style unknown
        for p in sorted(kit_dir.rglob("*.wav")):
            kind = next((k for k in KINDS if p.name.lower().startswith(k)), None)
            if kind:
                m = measure(read_wav(p))
                files.append(dict(file=p.name, kind=kind, style="unknown", path=p, **m))
    if not files:
        sys.exit(f"no kit files found in {kit_dir}")
    return files


def load_events(path):
    d = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(d, dict):
        d = d.get("events") or d.get("sfx") or d.get("cues") or []
    ev = []
    for i, e in enumerate(d):
        at = e.get("at", e.get("t", e.get("time")))
        kind = (e.get("kind") or e.get("type") or "").lower()
        if at is None or kind not in KINDS:
            sys.exit(f"event {i}: needs 'at' (seconds) and 'kind' in {KINDS}: {e}")
        ev.append(dict(at=float(at), kind=kind, gain_db=float(e.get("gain_db", 0.0)), file=e.get("file"),
                       variant=e.get("variant")))
    return sorted(ev, key=lambda e: e["at"])


def pick(files, ev, style, counters, rng):
    if ev["file"]:
        for f in files:
            if f["file"].replace("\\", "/").endswith(ev["file"].replace("\\", "/")):
                return f
        sys.exit(f"{ev['file']} is not in the kit")
    cands = [f for f in files if f["kind"] == ev["kind"] and "/" not in f["file"]]  # top-level kit first
    extra = [f for f in files if f["kind"] == ev["kind"] and "/" in f["file"]]      # earshot/ as fallbacks
    if style != "any":
        pref = [f for f in cands if f["style"] == style] or [f for f in cands if f["style"] == "neutral"]
        cands = pref or cands
    if not cands:
        cands = extra
    if not cands:
        sys.exit(f"no kit sound of kind {ev['kind']}")
    if ev["variant"] is not None:
        return cands[int(ev["variant"]) % len(cands)]
    n = counters.get(ev["kind"], 0)
    counters[ev["kind"]] = n + 1
    return cands[n % len(cands)]  # rotate takes of a repeated kind (vanja.io: never the same sound twice in a row)


def anchor_start(kind, f, at, fps):
    fr = 1.0 / fps
    rule = ANCHOR[kind]
    if rule == "peak_before":
        return at - 2 * fr - f["peak_s"], f"peak at -2f ({at - 2 * fr:.4f})", at - 2 * fr, "peak"
    if rule == "peak_on":
        return at - f["peak_s"], f"peak on at ({at:.4f})", at, "peak"
    if rule == "end_before":
        return at - 2 * fr - f["end_s"], f"end at -2f ({at - 2 * fr:.4f})", at - 2 * fr, "end"
    return at - f["onset_s"], f"onset on at ({at:.4f})", at, "onset"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("events")
    ap.add_argument("--kit", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--fps", type=float, default=30.0)
    ap.add_argument("--duration", type=float, help="track length in s (default: last sound end + 1 s)")
    ap.add_argument("--cuts", type=int, help="number of picture cuts in the reel, for the whoosh density guard")
    ap.add_argument("--style", default="gritty", choices=["gritty", "neutral", "clean", "any"])
    ap.add_argument("--mixed", action="store_true", help="allow gritty and clean in one reel")
    ap.add_argument("--placement", help="placement table path (default: next to --out)")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--voice", help="voice stem: print the ffmpeg mix command for it")
    a = ap.parse_args()

    files = load_kit(a.kit)
    events = load_events(a.events)
    rng = np.random.default_rng(a.seed)
    counters, placed, warnings = {}, [], []

    for ev in events:
        f = pick(files, ev, a.style, counters, rng)
        start, rule_txt, target_t, which = anchor_start(ev["kind"], f, ev["at"], a.fps)
        if start < 0:
            warnings.append(f"{ev['kind']} at {ev['at']:.3f}: would start at {start:.3f} s, clamped to 0 (anchor misses)")
            start = 0.0
        placed.append(dict(ev=ev, f=f, start=start, rule=rule_txt, target=target_t, which=which))

    # one-style guard
    styles = {p["f"]["style"] for p in placed}
    if "gritty" in styles and "clean" in styles and not a.mixed:
        bad = [f"{p['f']['file']} ({p['f']['style']})" for p in placed if p["f"]["style"] in ("gritty", "clean")]
        sys.exit("one SFX style per reel: this list mixes gritty and clean sounds: " + ", ".join(sorted(set(bad)))
                 + ". Pick one style (--style) or pass --mixed on purpose.")

    # the 2 frames before a riser's target must be silent: a hit on the same `at` with a slow attack breaks that
    fr = 1.0 / a.fps
    for p in placed:
        if p["ev"]["kind"] != "riser":
            continue
        gap_lo = p["ev"]["at"] - 2 * fr
        for q in placed:
            if q is p:
                continue
            q_on = q["start"] + q["f"]["onset_s"]
            if gap_lo - 0.001 < q_on < p["ev"]["at"] - 0.001:
                warnings.append(f"riser at {p['ev']['at']:.3f}: {q['ev']['kind']} {q['f']['file']} starts sounding at "
                                f"{q_on:.3f} s, inside the 2-frame gap ({gap_lo:.3f} to {p['ev']['at']:.3f}); "
                                f"use a faster-attack sound there (\"file\": \"earshot/es_thud_diesel.wav\" peaks 21 ms "
                                f"after its onset) or accept the overlap")

    # density guards
    n_whoosh = sum(1 for p in placed if p["ev"]["kind"] == "whoosh")
    if a.cuts is not None:
        if n_whoosh > max(1, a.cuts // 4):
            warnings.append(f"density: {n_whoosh} whooshes for {a.cuts} cuts; house rule is one whoosh per 4 cuts at most")
    else:
        warnings.append(f"density: --cuts not given, whoosh-per-cut check skipped ({n_whoosh} whooshes placed)")
    starts = sorted(p["ev"]["at"] for p in placed)
    for i, t in enumerate(starts):
        inside = [s for s in starts if t <= s < t + 1.0]
        if len(inside) > 3:
            warnings.append(f"density: {len(inside)} sounds start between {t:.2f} and {t + 1:.2f} s (max 3 per second)")
            break

    # render
    end_t = max(p["start"] + p["f"].get("duration_s", 0) or 0 for p in placed)
    dur = a.duration if a.duration else end_t + 1.0
    n = int(math.ceil(dur * SR))
    track = np.zeros((n, 2))
    for p in placed:
        x = read_wav(p["f"]["path"])
        if p["ev"]["gain_db"]:
            x = x * 10 ** (p["ev"]["gain_db"] / 20)
        s0 = int(round(p["start"] * SR))
        seg = x[: max(0, n - s0)]
        if len(seg):
            track[s0:s0 + len(seg)] += seg
        p["s0"] = s0
        p["len"] = len(seg)
        p["x"] = x
    peak = float(np.abs(track).max()) if n else 0.0
    lim = 10 ** (-1 / 20)
    if peak > lim:
        track *= lim / peak
        warnings.append(f"clipping: sum peaked at {20 * math.log10(peak):+.1f} dBFS, whole track scaled by "
                        f"{20 * math.log10(lim / peak):+.1f} dB (thin out the overlaps instead)")
    write_wav24(a.out, track)

    # measure actual anchors on the rendered track (each sound's own window, so neighbours do not fool the measure)
    rows = []
    for p in placed:
        seg = track[p["s0"]:p["s0"] + p["len"]]
        m = measure(seg) if len(seg) else dict(onset_s=0, peak_s=0, end_s=0)
        actual = p["s0"] / SR + m[p["which"] + "_s"]
        delta_fr = (actual - p["target"]) * a.fps
        rows.append((p["ev"]["kind"], p["f"]["file"], p["ev"]["at"], p["rule"], actual, delta_fr, p["f"]["style"],
                     p["ev"]["gain_db"]))

    pl = Path(a.placement) if a.placement else Path(a.out).with_name("placement.txt")
    lines = [f"# sfx_place.py  events={a.events}  kit={a.kit}  fps={a.fps:g}  out={a.out}  style={a.style}"
             f"{' mixed' if a.mixed else ''}",
             f"# anchor rule: whoosh peak -2f, hit/stamp peak on, riser end -2f, pop/tick/click/notify onset on",
             f"{'kind':8} {'file':28} {'requested':>9} {'anchor':>9} {'actual':>9} {'delta_f':>8} {'style':8} {'gain':>5}  rule"]
    for k, fn, at, rule, actual, d, st, g in rows:
        tgt = rule.split("(")[1].rstrip(")")
        lines.append(f"{k:8} {fn:28} {at:9.4f} {float(tgt):9.4f} {actual:9.4f} {d:+8.2f} {st:8} {g:+5.1f}  {rule.split(' (')[0]}")
    for w in warnings:
        lines.append("WARN " + w)
    pl.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    print(f"wrote {a.out} ({dur:.2f} s, peak {20 * math.log10(max(float(np.abs(track).max()), 1e-9)):+.1f} dBFS) and {pl}")

    if a.voice:
        v = read_wav(a.voice)
        vpk = 20 * math.log10(max(float(np.abs(v).max()), 1e-9))
        # hottest kit sound is -7 dBFS (stamp/hit); place it 6 dB under the voice peak
        bus = (vpk - 6.0) - (-7.0)
        print("\nMix under the voice (fixed -6 dB under the voice peak, then loudnorm to -14 LUFS):")
        print(f'  voice peak {vpk:+.1f} dBFS, so the SFX bus gets volume={bus:+.1f}dB')
        print(f'  "{FFMPEG}" -i "{a.voice}" -i "{a.out}" -filter_complex '
              f'"[1:a]volume={bus:+.1f}dB[s];[0:a][s]amix=inputs=2:duration=first:normalize=0,'
              f'loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo" '
              f'-c:a pcm_s24le voice_plus_sfx.wav')


if __name__ == "__main__":
    main()
