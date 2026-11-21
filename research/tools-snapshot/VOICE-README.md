# vo_scratch: scratch voice for timing a reel script

**Rule first: this is a timing and preview tool only.** The Kokoro voice is never shipped,
never posted, never put under a reel "just for now". Jacob's own voice is the credential and
is always the final VO. Use this to hear whether a script runs long, where the hook lands,
and to prototype karaoke captions against real word timestamps before he records. If a
synthetic voice ever did go out, Meta's "Add AI label" toggle would be required at share.

Built 2026-11-21 from the nxtlvl pipeline study (`socialmediatakeover/research/reel-references/
2026-11-21-nxtlvl-repo/PIPELINE-STUDY.md` section 1.7) and the audio research note
(`socialmediatakeover/research/2026-11-21-audio-trends-and-voice.md`).

## What is installed

| Piece | Where | Notes |
|---|---|---|
| Virtual env | `tools\venv-voice\` | kokoro-onnx 0.6.1, onnxruntime 1.32.0, espeakng-loader 0.2.4 (bundles espeak-ng), phonemizer 3.6.0, soundfile 0.14.0, numpy 2.5.5. Installed with pip inside the venv only. |
| Kokoro model | `tools\models\kokoro\kokoro-v1.0.onnx` (325 MB) | from github.com/thewh1teagle/kokoro-onnx releases, tag `model-files-v1.0` |
| Kokoro voices | `tools\models\kokoro\voices-v1.0.bin` (28 MB) | same release |
| faster-whisper | system Python 3.12 (`%LOCALAPPDATA%\Programs\Python\Python312\python.exe`) | already there for watch.py, `small` and `medium` cached. **Do not upgrade it, av==14.2.0 is pinned.** |
| ffmpeg | `%LOCALAPPDATA%\Microsoft\WinGet\Packages\Gyan.FFmpeg_...\ffmpeg-9.0.2-full_build\bin\ffmpeg.exe` | polish chain |

The two Pythons never mix. `vo_scratch.py` runs under the system Python and spawns
`venv-voice\Scripts\python.exe` for the Kokoro step. Launching it from the venv by mistake
re-launches it under the system Python.

### Rebuilding the venv from scratch

    cd "C:\Users\Parts\OneDrive - Elite Diesel Service\Desktop\VIDEO\tools"
    "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" -m venv venv-voice
    venv-voice\Scripts\python.exe -m pip install kokoro-onnx soundfile numpy
    curl -L -o models\kokoro\kokoro-v1.0.onnx https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
    curl -L -o models\kokoro\voices-v1.0.bin https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin

Everything resolves as pure wheels on Python 3.12, no compiler, no system espeak install.

## Usage

    "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" -I vo_scratch.py script.txt out_dir [--voice am_michael] [--speed 1.1] [--takes 2] [--whisper-model small]

- `script.txt`: one line per spoken beat. Blank lines and lines starting with `#` are skipped.
  Line 1 is treated as the hook.
- `--voice`: `am_michael` is the default (best-rated American male). `am_adam`, `af_heart`,
  `am_fenrir`, `am_puck` also exist; `k.get_voices()` lists all 54.
- `--speed`: base speed. With `--takes 2` the two takes are generated at base-0.04 and
  base+0.08 (1.06 and 1.18 at the default 1.1). More takes fan out across that range.
  Generate at the speed you want; the tool never time-stretches.
- `--whisper-model`: `small` (default) or `medium`.

### What it does per line

1. Generates every take with Kokoro at 24 kHz (one venv process, model loads once).
2. Transcribes each take with faster-whisper (`small`, CPU int8, `word_timestamps=True`, beam 5).
3. Scores each take by word error rate against the script line. Numbers are spelled out on
   both sides so "1959" and "nineteen fifty nine" agree, and split compounds ("power stroke"
   for "Powerstroke") are not counted as errors. Lowest WER wins; ties go to the take whose
   speed is closest to `--speed`.
4. Trims the winner from 0.04 s before the first word to 0.12 s after the last, 12 ms fades.
5. Joins lines with a gap after each: hook 0.2 s, body lines 0.3 s, last line 0 s.
6. Polishes with ffmpeg: `highpass=f=80, acompressor threshold -20 dB ratio 3 attack 5
   release 80 makeup 2, loudnorm I=-16 TP=-2 LRA=9`, written as 48 kHz stereo PCM.
   No atempo anywhere, so the word times line up with `vo.wav` as written.

### Outputs in `out_dir`

| File | What |
|---|---|
| `vo.wav` | polished scratch VO, 48 kHz stereo, about -16 LUFS |
| `vo_raw_24k.wav` | the un-polished join, 24 kHz mono |
| `words.json` | `[{"w": " word", "s": 0.00, "e": 0.46}, ...]`, same shape as `watch.py` writes (leading space on every word, 2-decimal seconds). Always one entry per script word in the script's own spelling: Whisper's tokens are aligned to the script ("1,959" to "1959", "power stroke" to "Powerstroke.", "two-wheel" split across "Two wheel") so caption prototypes read exactly what was written. Drops straight into the build_reel caption step. |
| `lines.json` | per line: text, chosen speed, start, end, dur, wer, Whisper transcript, word count, which take file, and the WER of every take |
| `report.txt` | words per minute, total duration, hook check, flags, a per-line table, run timing |
| `takes/` | every raw take (`line01_t0_x1.06.wav` ...), `jobs.json`, `manifest.json` |

### Reading the report

Targets, from the audio research note: **150 to 165 wpm overall; a 15-word hook inside 5 s;
whole reel under 18 s; never under 140 wpm.** The report flags each miss. Kokoro at 1.06 runs
about 155 wpm while speaking, close to a brisk human read, so if the scratch runs long, Jacob's
real take will run longer. Cut words before he records, do not plan on him talking faster.

## Measured on this machine (CPU only, 2026-11-21)

6-line, 81-word Rival script, 2 takes per line (12 takes, 62 s of audio), three runs:
Kokoro 19 to 25 s (RTF 0.33 to 0.38, about 1 s model load), Whisper small 23 to 51 s
depending on what else the machine is doing, whole run 45 to 77 s. Budget about a minute
per script, two if OneDrive is syncing.

## Limits

- CPU TTS, so about 3x faster than real time. A 20-line script with 3 takes takes a few minutes.
- Kokoro pronunciation: numbers and model names mostly come out right ("F600" as "F six
  hundred", "7.3" as "seven point three", "1959" as "nineteen fifty nine"). If a word comes
  out wrong, respell it in the script ("ISSPRO" as "iss pro") or rewrite the line; the study
  notes Kokoro dropping "-ed" endings on some words. kokoro-onnx also accepts inline IPA via
  phonemes if it ever matters, but a respelling is usually enough for a timing pass.
- The WER score picks between takes, it does not judge delivery. Listen to `takes/` if the
  chosen read sounds off and copy the other take's timings from `lines.json`.
- Whisper word timestamps are about plus or minus 50 ms. Fine for caption prototyping, and
  they get replaced by `watch.py` timings on Jacob's real recording anyway.
- Only English (`lang="en-us"`) is wired up.
- Word timing uses the Whisper words of the chosen take; if Whisper hears nothing on a take
  (empty line, pure numbers) the take is kept whole and that line has no words in `words.json`.
- The test output in `tools\voice-test\` is a sample, regenerate it any time.

## Do not

- Do not pip install anything into the system Python for this tool. kokoro-onnx pulls its
  own onnxruntime and must stay inside `venv-voice`.
- Do not post, upload, or hand off `vo.wav` as a finished voice track. Scratch only.
