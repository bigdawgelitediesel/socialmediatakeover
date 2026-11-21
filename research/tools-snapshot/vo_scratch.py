"""
vo_scratch.py  -  scratch voice for timing a reel script (Kokoro TTS + faster-whisper)

usage:  python vo_scratch.py script.txt out_dir [--voice am_michael] [--speed 1.1] [--takes 2]
                                               [--whisper-model small] [--keep-takes]

  script.txt   one line per spoken beat (blank lines ignored, lines starting with # ignored)
  out_dir      vo.wav (48 kHz stereo, polished), words.json (watch.py format),
               lines.json (per line: text, chosen speed, start, end, wer), report.txt,
               takes/ (every raw take, kept by default so you can listen)

THIS IS A TIMING AND PREVIEW TOOL ONLY. The synthetic voice is never shipped; Jacob's own
voice is always the final. Use the output to hear pacing, trim words, and prototype captions.

How it runs: this file is launched with the system Python (faster-whisper lives there) and
re-launches itself inside tools\\venv-voice for the Kokoro step (kokoro-onnx lives there).
Neither environment is touched by the other. Launching it with either interpreter works.
"""
import argparse, json, os, re, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
LOCAL = os.environ.get("LOCALAPPDATA", os.path.expanduser(r"~\AppData\Local"))
SYS_PY = os.path.join(LOCAL, r"Programs\Python\Python312\python.exe")
VENV_PY = os.path.join(HERE, r"venv-voice\Scripts\python.exe")
FFMPEG = os.path.join(LOCAL, r"Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe"
                              r"\ffmpeg-9.0.2-full_build\bin\ffmpeg.exe")
MODEL_DIR = os.path.join(HERE, "models", "kokoro")
KOKORO_ONNX = os.path.join(MODEL_DIR, "kokoro-v1.0.onnx")
KOKORO_VOICES = os.path.join(MODEL_DIR, "voices-v1.0.bin")

SR = 24000
TRIM_BEFORE = 0.04      # s before the first word
TRIM_AFTER = 0.12       # s after the last word
FADE = 0.012            # s, linear in and out on every trimmed take
GAP_HOOK = 0.20         # pause after line 1
GAP_BODY = 0.30         # pause after every middle line
GAP_LAST = 0.00         # nothing after the last line
POLISH = ("highpass=f=80,"
          "acompressor=threshold=-20dB:ratio=3:attack=5:release=80:makeup=2,"
          "loudnorm=I=-16:TP=-2:LRA=9")

# pacing targets from research/2026-11-21-audio-trends-and-voice.md
WPM_LO, WPM_HI = 150, 165
HOOK_WORDS, HOOK_SECS = 15, 5.0
MAX_REEL_SECS, MIN_WPM = 18.0, 140


# ----------------------------------------------------------------------------- kokoro side
def gen_main(jobs_path):
    """Runs inside venv-voice. Reads a jobs json, writes one wav per take, returns a manifest."""
    import numpy as np
    import soundfile as sf
    from kokoro_onnx import Kokoro
    jobs = json.load(open(jobs_path, encoding="utf-8"))
    t0 = time.time()
    k = Kokoro(KOKORO_ONNX, KOKORO_VOICES)
    load_s = time.time() - t0
    out = []
    for j in jobs["takes"]:
        t1 = time.time()
        audio, sr = k.create(j["text"], voice=jobs["voice"], speed=j["speed"], lang="en-us")
        audio = np.asarray(audio, dtype=np.float32)
        if sr != SR:
            raise SystemExit(f"kokoro returned {sr} Hz, expected {SR}")
        sf.write(j["wav"], audio, SR, subtype="PCM_16")
        out.append(dict(j, dur=len(audio) / SR, gen_s=time.time() - t1))
    json.dump(dict(load_s=load_s, takes=out), open(jobs["manifest"], "w", encoding="utf-8"), indent=1)


# ----------------------------------------------------------------------------- text normalising
_ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
_TENS = "x x twenty thirty forty fifty sixty seventy eighty ninety".split()


def _n2w(n):
    if n < 20: return _ONES[n]
    if n < 100: return _TENS[n // 10] + ("" if n % 10 == 0 else " " + _ONES[n % 10])
    if n < 1000: return _ONES[n // 100] + " hundred" + ("" if n % 100 == 0 else " " + _n2w(n % 100))
    if 1100 <= n <= 1999 and n % 100 != 0: return _n2w(n // 100) + " " + _n2w(n % 100)   # years: nineteen fifty nine
    if n < 1_000_000: return _n2w(n // 1000) + " thousand" + ("" if n % 1000 == 0 else " " + _n2w(n % 1000))
    return str(n)


def _num_token(m):
    s = m.group(0)
    if "." in s:
        a, b = s.split(".", 1)
        return (_n2w(int(a)) if a else "") + " point " + " ".join(_ONES[int(c)] for c in b)
    return _n2w(int(s))


def norm_words(text):
    """Lowercase, drop punctuation, spell out numbers so '1959' and 'nineteen fifty nine' agree.
    Applied to both the script line and the Whisper transcript before scoring."""
    t = text.lower().replace("-", " ").replace("/", " ")
    t = re.sub(r"(\d),(\d)", r"\1\2", t)                       # 1,000 -> 1000
    t = re.sub(r"([a-z])(\d)", r"\1 \2", t)                      # f600 -> f 600
    t = re.sub(r"(\d)([a-z])", r"\1 \2", t)                      # 600hp -> 600 hp
    t = re.sub(r"\d+\.\d+|\d+", _num_token, t)
    t = re.sub(r"[^a-z' ]+", " ", t)
    t = t.replace("'", "")
    return t.split()


def merge_compounds(ref, hyp):
    """'power stroke' heard for 'powerstroke' is not an error: glue adjacent hyp tokens when their
    concatenation is a ref token (and the reverse, split ref tokens Whisper glued together)."""
    refset = set(ref)
    out, i = [], 0
    while i < len(hyp):
        merged = False
        for n in (3, 2):
            if i + n <= len(hyp) and "".join(hyp[i:i + n]) in refset:
                out.append("".join(hyp[i:i + n])); i += n; merged = True; break
        if not merged: out.append(hyp[i]); i += 1
    hypset = set(out)
    ref2, i = [], 0
    while i < len(ref):
        merged = False
        for n in (3, 2):
            if i + n <= len(ref) and "".join(ref[i:i + n]) in hypset:
                ref2.append("".join(ref[i:i + n])); i += n; merged = True; break
        if not merged: ref2.append(ref[i]); i += 1
    return ref2, out


def wer(ref, hyp):
    """Classic word error rate: edits / len(ref). Both are token lists."""
    if not ref: return 0.0 if not hyp else 1.0
    ref, hyp = merge_compounds(ref, hyp)
    d = list(range(len(hyp) + 1))
    for i in range(1, len(ref) + 1):
        prev, d[0] = d[0], i
        for j in range(1, len(hyp) + 1):
            cur = d[j]
            d[j] = min(d[j] + 1, d[j - 1] + 1, prev + (ref[i - 1] != hyp[j - 1]))
            prev = cur
    return d[len(hyp)] / len(ref)


def align_words(script_tokens, whisper_words):
    """Give every script token a time span from the Whisper words, whatever Whisper's spelling or
    tokenisation ("1,959" for "1959,", "two-wheel" for "Two wheel", "power stroke" for "Powerstroke").
    Both sides are broken into normalised sub-tokens, aligned by edit distance, and each script
    token takes the span of the Whisper words its sub-tokens landed on. A Whisper word shared by
    several script tokens is split by character count. Unmatched script tokens get a zero-length
    slot at the previous word's end so the list stays complete and monotonic."""
    A = [(t, si) for si, tok in enumerate(script_tokens) for t in norm_words(tok)]
    B = [(t, wi) for wi, w in enumerate(whisper_words) for t in norm_words(w["w"])]
    n, m = len(A), len(B)
    D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): D[i][0] = i
    for j in range(1, m + 1): D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(D[i - 1][j] + 1, D[i][j - 1] + 1, D[i - 1][j - 1] + (A[i - 1][0] != B[j - 1][0]))
    i, j, pairs = n, m, []           # (script idx, whisper idx) for matched or substituted sub-tokens
    while i > 0 and j > 0:
        if D[i][j] == D[i - 1][j - 1] + (A[i - 1][0] != B[j - 1][0]):
            pairs.append((A[i - 1][1], B[j - 1][1])); i -= 1; j -= 1
        elif D[i][j] == D[i - 1][j] + 1: i -= 1
        else: j -= 1
    by_script = {}
    for si, wi in pairs: by_script.setdefault(si, set()).add(wi)
    by_whisper = {}
    for si, wi in pairs: by_whisper.setdefault(wi, set()).add(si)
    out, prev_end = [], 0.0
    for si, tok in enumerate(script_tokens):
        wis = sorted(by_script.get(si, ()))
        if not wis:
            out.append([tok, prev_end, prev_end]); continue
        s0 = min(whisper_words[w]["s"] for w in wis); e0 = max(whisper_words[w]["e"] for w in wis)
        if len(wis) == 1 and len(by_whisper[wis[0]]) > 1:          # one Whisper word, several script tokens
            group = sorted(by_whisper[wis[0]])
            lens = [max(1, len(script_tokens[g].strip(",.!?;:"))) for g in group]
            k = group.index(si); tot = sum(lens)
            s0, e0 = s0 + (e0 - s0) * sum(lens[:k]) / tot, s0 + (e0 - s0) * sum(lens[:k + 1]) / tot
        s0 = max(s0, prev_end)
        e0 = max(e0, s0)
        out.append([tok, s0, e0]); prev_end = e0
    return out


# ----------------------------------------------------------------------------- orchestrator
def take_speeds(base, takes):
    """takes=2 at base 1.10 -> 1.06 and 1.18 (the two-takes-two-speeds rule). More takes fan out
    evenly between base-0.04 and base+0.08. One take = the base speed itself."""
    if takes <= 1: return [round(base, 3)]
    lo, hi = base - 0.04, base + 0.08
    return [round(lo + (hi - lo) * i / (takes - 1), 3) for i in range(takes)]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("script"); ap.add_argument("out_dir")
    ap.add_argument("--voice", default="am_michael")
    ap.add_argument("--speed", type=float, default=1.1)
    ap.add_argument("--takes", type=int, default=2)
    ap.add_argument("--whisper-model", default="small")
    ap.add_argument("--keep-takes", action="store_true", default=True)
    a = ap.parse_args()

    for p, what in [(SYS_PY, "system Python 3.12"), (VENV_PY, "venv-voice (see VOICE-README.md)"),
                    (FFMPEG, "ffmpeg"), (KOKORO_ONNX, "kokoro-v1.0.onnx"), (KOKORO_VOICES, "voices-v1.0.bin")]:
        if not os.path.exists(p): sys.exit(f"missing {what}: {p}")

    import numpy as np
    import soundfile as sf

    out = os.path.abspath(a.out_dir)
    takes_dir = os.path.join(out, "takes")
    os.makedirs(takes_dir, exist_ok=True)
    lines = [l.strip() for l in open(a.script, encoding="utf-8") if l.strip() and not l.lstrip().startswith("#")]
    if not lines: sys.exit("script has no lines")
    T0 = time.time()

    # 1. generate every take in one venv process (model loads once)
    jobs = dict(voice=a.voice, manifest=os.path.join(takes_dir, "manifest.json"), takes=[])
    for li, text in enumerate(lines):
        for ti, sp in enumerate(take_speeds(a.speed, a.takes)):
            jobs["takes"].append(dict(line=li, take=ti, speed=sp, text=text,
                                      wav=os.path.join(takes_dir, f"line{li+1:02d}_t{ti}_x{sp:.2f}.wav")))
    jobs_path = os.path.join(takes_dir, "jobs.json")
    json.dump(jobs, open(jobs_path, "w", encoding="utf-8"), indent=1)
    t = time.time()
    r = subprocess.run([VENV_PY, "-I", os.path.abspath(__file__), "--_gen", jobs_path], capture_output=True, text=True)
    if r.returncode:
        sys.exit("kokoro step failed:\n" + r.stdout[-2000:] + r.stderr[-2000:])
    man = json.load(open(jobs["manifest"], encoding="utf-8"))
    gen_s = time.time() - t
    audio_s = sum(x["dur"] for x in man["takes"])
    print(f"KOKORO  {len(man['takes'])} takes, {audio_s:.1f} s of audio in {gen_s:.1f} s "
          f"(model load {man['load_s']:.1f} s, RTF {(gen_s - man['load_s']) / max(audio_s, 1e-6):.2f})")

    # 2. transcribe each take, score against the script line
    t = time.time()
    from faster_whisper import WhisperModel
    wm = WhisperModel(a.whisper_model, device="cpu", compute_type="int8")
    for x in man["takes"]:
        segs, _ = wm.transcribe(x["wav"], word_timestamps=True, beam_size=5, language="en",
                                condition_on_previous_text=False, vad_filter=False)
        words = []
        for s in segs:
            for w in (s.words or []):
                # tokens without a leading space are continuations ("1" + ",959", "7" + ".3"): merge them
                if words and not w.word.startswith(" "):
                    words[-1]["w"] += w.word; words[-1]["e"] = float(w.end)
                else:
                    words.append(dict(w=w.word, s=float(w.start), e=float(w.end)))
        hyp = "".join(w["w"] for w in words)
        x["words"] = words
        x["transcript"] = hyp.strip()
        x["wer"] = round(wer(norm_words(x["text"]), norm_words(hyp)), 3)
    print(f"WHISPER {len(man['takes'])} takes in {time.time() - t:.1f} s")

    # 3. pick, trim, fade, join
    pieces, cursor, picked, all_words = [], 0.0, [], []
    by_line = {}
    for x in man["takes"]: by_line.setdefault(x["line"], []).append(x)
    n_fade = int(FADE * SR)
    for li, text in enumerate(lines):
        cands = by_line[li]
        # lowest WER wins; on a tie prefer the take whose speed is closest to the requested base
        best = sorted(cands, key=lambda x: (x["wer"], abs(x["speed"] - a.speed)))[0]
        audio, sr = sf.read(best["wav"], dtype="float32")
        if audio.ndim > 1: audio = audio.mean(axis=1)
        words = best["words"]
        if words:
            s0 = max(0.0, words[0]["s"] - TRIM_BEFORE)
            e0 = min(len(audio) / SR, words[-1]["e"] + TRIM_AFTER)
        else:                                  # whisper heard nothing: keep the take whole
            s0, e0 = 0.0, len(audio) / SR
        seg = audio[int(s0 * SR):int(e0 * SR)].copy()
        if len(seg) > 2 * n_fade:
            ramp = np.linspace(0, 1, n_fade, dtype=np.float32)
            seg[:n_fade] *= ramp; seg[-n_fade:] *= ramp[::-1]
        # word timing: shift to the trimmed take, then onto the timeline
        script_tokens = text.split()
        line_words = [dict(w=" " + tok, s=round(cursor + ws - s0, 2), e=round(cursor + we - s0, 2))
                      for tok, ws, we in align_words(script_tokens, words)] if words else []
        all_words.extend(line_words)
        start = cursor
        cursor += len(seg) / SR
        picked.append(dict(line=li + 1, text=text, speed=best["speed"], start=round(start, 2), end=round(cursor, 2),
                           dur=round(cursor - start, 2), wer=best["wer"], transcript=best["transcript"],
                           words=len(script_tokens), take=os.path.basename(best["wav"]),
                           takes=[dict(speed=c["speed"], wer=c["wer"], raw_dur=round(c["dur"], 2)) for c in cands]))
        gap = GAP_LAST if li == len(lines) - 1 else (GAP_HOOK if li == 0 else GAP_BODY)
        pieces.append(seg)
        if gap > 0:
            pieces.append(np.zeros(int(gap * SR), dtype=np.float32)); cursor += gap
    raw = np.concatenate(pieces)
    raw_path = os.path.join(out, "vo_raw_24k.wav")
    sf.write(raw_path, raw, SR, subtype="PCM_16")
    total = len(raw) / SR

    # 4. polish: no atempo anywhere, so word times stay valid against vo.wav
    vo_path = os.path.join(out, "vo.wav")
    r = subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-i", raw_path, "-af", POLISH,
                        "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le", vo_path], capture_output=True, text=True)
    if r.returncode: sys.exit("ffmpeg polish failed: " + r.stderr[-1500:])

    # 5. outputs
    json.dump(all_words, open(os.path.join(out, "words.json"), "w"))
    json.dump(dict(voice=a.voice, base_speed=a.speed, takes=a.takes, whisper_model=a.whisper_model,
                   total_s=round(total, 2), lines=picked),
              open(os.path.join(out, "lines.json"), "w", encoding="utf-8"), indent=1)

    n_words = sum(p["words"] for p in picked)
    spoken = sum(p["dur"] for p in picked)
    wpm_total = n_words / total * 60 if total else 0
    wpm_spoken = n_words / spoken * 60 if spoken else 0
    hook = picked[0]
    hook_ok = hook["words"] <= HOOK_WORDS and hook["end"] <= HOOK_SECS
    mean_wer = sum(p["wer"] for p in picked) / len(picked)
    elapsed = time.time() - T0
    rep = []
    rep.append(f"vo_scratch report  {time.strftime('%Y-%m-%d %H:%M')}")
    rep.append(f"script: {os.path.abspath(a.script)}")
    rep.append(f"voice {a.voice}  base speed {a.speed}  takes/line {a.takes}  whisper {a.whisper_model}")
    rep.append("SCRATCH VOICE ONLY. Timing and preview. Jacob records the real VO.")
    rep.append("")
    rep.append(f"total duration   {total:.2f} s   ({spoken:.2f} s spoken + {total - spoken:.2f} s gaps)")
    rep.append(f"words            {n_words}")
    rep.append(f"words per minute {wpm_total:.0f} overall, {wpm_spoken:.0f} while speaking   target {WPM_LO} to {WPM_HI}")
    rep.append(f"hook             {hook['words']} words, ends at {hook['end']:.2f} s   target {HOOK_WORDS} words inside {HOOK_SECS:.0f} s   "
               f"{'OK' if hook_ok else 'OVER'}")
    rep.append(f"mean WER         {mean_wer:.3f}  (0 = Whisper read back every word of the script)")
    flags = []
    if total > MAX_REEL_SECS: flags.append(f"runs {total:.1f} s, over the {MAX_REEL_SECS:.0f} s ceiling: cut words")
    if wpm_total < MIN_WPM: flags.append(f"{wpm_total:.0f} wpm is under {MIN_WPM}: tighten the lines or raise --speed")
    if wpm_total > WPM_HI + 15: flags.append(f"{wpm_total:.0f} wpm is well over target: Jacob will not talk this fast, expect a longer real take")
    if not hook_ok: flags.append("hook misses the 15 words in 5 s target")
    high = [p for p in picked if p["wer"] > 0.15]
    if high: flags.append("lines Whisper misheard (" + ", ".join(str(p["line"]) for p in high) + "): check wording or respell a word")
    rep.append("flags            " + ("; ".join(flags) if flags else "none"))
    rep.append("")
    rep.append(f"{'line':>4} {'start':>6} {'end':>6} {'dur':>5} {'wds':>3} {'wpm':>4} {'speed':>5} {'wer':>5}  text")
    for p in picked:
        rep.append(f"{p['line']:>4} {p['start']:>6.2f} {p['end']:>6.2f} {p['dur']:>5.2f} {p['words']:>3} "
                   f"{p['words'] / p['dur'] * 60 if p['dur'] else 0:>4.0f} {p['speed']:>5.2f} {p['wer']:>5.3f}  {p['text']}")
        others = [c for c in p["takes"] if c["speed"] != p["speed"]]
        if others:
            rep.append("     " + "  ".join(f"(not picked x{c['speed']:.2f} wer {c['wer']:.3f} {c['raw_dur']:.2f}s)" for c in others))
        if p["wer"] > 0:
            rep.append(f"     whisper heard: {p['transcript']}")
    rep.append("")
    rep.append(f"timing           kokoro {gen_s:.1f} s for {audio_s:.1f} s of raw takes, whole run {elapsed:.1f} s")
    rep.append(f"files            vo.wav (48k stereo polished), vo_raw_24k.wav, words.json, lines.json, takes/")
    txt = "\n".join(rep)
    open(os.path.join(out, "report.txt"), "w", encoding="utf-8").write(txt + "\n")
    print(txt)


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "--_gen":
        gen_main(sys.argv[2])
    elif os.path.normcase(sys.executable) == os.path.normcase(VENV_PY):
        # launched from the venv by mistake: hop to the system Python, which has faster-whisper
        sys.exit(subprocess.call([SYS_PY, "-I", os.path.abspath(__file__)] + sys.argv[1:]))
    else:
        main()
