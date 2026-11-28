#!/usr/bin/env python
"""
vofit.py: finish an ElevenLabs take for the reels. Trim the ends, set the pace, hit the house loudness.

  python -I tools/vofit.py take.mp3 --out "Name - VO take 1"            -> Name - VO take 1.mp3 and .wav at 1.20x
  python -I tools/vofit.py take.mp3 --out name --tempo 1.0               -> pace as generated
  python -I tools/vofit.py take.mp3 --out name --pauses 0.5              -> also halve every pause over 0.3 s
  python -I tools/vofit.py take.mp3 --out name --cap 44                  -> warn if the result is over 44 s

House pace since 2026-11-28: 1.20x (Jacob: "I like the 1.20 speed"). Pitch is untouched (ffmpeg atempo).
Loudness: two-pass loudnorm to -14 LUFS, -1.5 dBTP, mono, 48 kHz; 320 kbps MP3 plus a 24-bit WAV master.
Needs ffmpeg and ffprobe on the PATH. Spends no credits.
"""
from __future__ import annotations
import argparse, json, re, subprocess, sys
from pathlib import Path


def run(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True)


def dur(p: str) -> float:
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p]).stdout.strip())


def silences(src: str, thr: str = "-35dB", d: float = 0.3) -> list[tuple[float, float]]:
    r = run(["ffmpeg", "-hide_banner", "-nostats", "-i", src, "-af", f"silencedetect=noise={thr}:d={d}", "-f", "null", "-"])
    starts = [float(x) for x in re.findall(r"silence_start: ([0-9.]+)", r.stderr)]
    ends = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", r.stderr)]
    return list(zip(starts, ends))


def scale_pauses(src: str, out: str, scale: float, min_gap: float = 0.16) -> int:
    """Keep every word, shorten every detected pause to `scale` of its length (never under min_gap)."""
    total = dur(src); gaps = silences(src); segs = []; cursor = 0.0
    for s, e in gaps:
        keep = max(min_gap, (e - s) * scale)
        if s > cursor: segs.append((cursor, s))
        mid = (s + e) / 2; segs.append((mid - keep / 2, mid + keep / 2)); cursor = e
    if cursor < total: segs.append((cursor, total))
    parts = [f"[0:a]atrim=start={a:.3f}:end={b:.3f},asetpts=PTS-STARTPTS[s{i}]" for i, (a, b) in enumerate(segs)]
    fc = ";".join(parts) + ";" + "".join(f"[s{i}]" for i in range(len(segs))) + f"concat=n={len(segs)}:v=0:a=1[cat]"
    r = run(["ffmpeg", "-y", "-hide_banner", "-nostats", "-i", src, "-filter_complex", fc, "-map", "[cat]", "-ar", "48000", "-ac", "1", "-c:a", "pcm_s24le", out])
    if r.returncode: sys.exit(r.stderr[-800:])
    return len(gaps)


def main() -> None:
    ap = argparse.ArgumentParser(description="finish an ElevenLabs take: trim, pace, loudness")
    ap.add_argument("take"); ap.add_argument("--out", required=True, help="output base name, no extension")
    ap.add_argument("--tempo", type=float, default=1.20, help="pace multiplier, pitch untouched (house 1.20)")
    ap.add_argument("--pauses", type=float, default=1.0, help="scale every pause over 0.3 s by this (1.0 = leave them)")
    ap.add_argument("--cap", type=float, default=None, help="warn if the finished length is over this many seconds")
    ap.add_argument("--lufs", type=float, default=-14.0); ap.add_argument("--tp", type=float, default=-1.5)
    a = ap.parse_args()
    base = str(a.out); work = Path(base + ".work.wav"); raw_len = dur(a.take)
    src = a.take; gaps = 0
    if a.pauses != 1.0:
        gaps = scale_pauses(a.take, str(work), a.pauses); src = str(work)
    # trim head and tail silence, then set the pace
    tempo = f"atempo={a.tempo}," if abs(a.tempo - 1.0) > 1e-3 else ""
    trim = "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.12,areverse,silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.35,areverse"
    pre = Path(base + ".pre.wav")
    r = run(["ffmpeg", "-y", "-hide_banner", "-nostats", "-i", src, "-af", f"{trim},{tempo}aresample=48000", "-ac", "1", "-c:a", "pcm_s24le", str(pre)])
    if r.returncode: sys.exit(r.stderr[-800:])
    # two-pass loudnorm
    m = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(pre), "-af", f"loudnorm=I={a.lufs}:TP={a.tp}:LRA=9:print_format=json", "-f", "null", "-"]).stderr
    j = json.loads(m[m.rindex("{"):m.rindex("}") + 1])
    ln = (f"loudnorm=I={a.lufs}:TP={a.tp}:LRA=9:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}"
          f":measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true")
    wav = Path(base + ".wav"); mp3 = Path(base + ".mp3")
    run(["ffmpeg", "-y", "-hide_banner", "-nostats", "-i", str(pre), "-af", ln + ",aresample=48000", "-ac", "1", "-c:a", "pcm_s24le", str(wav)])
    run(["ffmpeg", "-y", "-hide_banner", "-nostats", "-i", str(wav), "-c:a", "libmp3lame", "-b:a", "320k", "-ar", "48000", str(mp3)])
    for t in (work, pre):
        if t.exists(): t.unlink()
    meas = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(mp3), "-af", "loudnorm=print_format=summary", "-f", "null", "-"]).stderr
    li = re.search(r"Input Integrated:\s*([-0-9.]+)", meas).group(1); tp = re.search(r"Input True Peak:\s*([-0-9.]+)", meas).group(1)
    final = dur(str(mp3))
    flag = "" if a.cap is None else ("  OK" if final <= a.cap else f"  OVER the {a.cap} s cap")
    print(f"{a.take}: {raw_len:.2f} s -> {final:.2f} s at {a.tempo:.2f}x" + (f", pauses x{a.pauses} ({gaps} gaps)" if gaps else "") + f", {li} LUFS, {tp} dBTP{flag}")
    print(f"wrote {mp3} and {wav}")


if __name__ == "__main__":
    main()
