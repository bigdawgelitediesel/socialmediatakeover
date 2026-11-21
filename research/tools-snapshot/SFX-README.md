# SFX layer for the reel pipeline (2026-11-21)

Closes the open item from 2026-11-20: the synthesised kit in tools/sfx was judged not shippable, and UI card
sounds had nothing behind them. Everything here is CC0 or MIT-output, measured, and placed by frame.

Paths are under `C:\Users\Parts\OneDrive - Elite Diesel Service\Desktop\VIDEO\tools\`.
Python is always `"%LOCALAPPDATA%\Programs\Python\Python312\python.exe" -I` (never bare python), numpy only.
ffmpeg is the Gyan 9.0.2 build under `%LOCALAPPDATA%\Microsoft\WinGet\Packages\...\bin\ffmpeg.exe`.

## What exists

| path | what |
|---|---|
| `sfx-kit\` | the kit: 16 CC0 wavs, 48 kHz stereo 24-bit, peak-normalised per kind. `KIT.md` is the human table (file, source URL, licence, peak, moment), `kit.json` the machine table (onset, peak, end per file) that `sfx_place.py` reads |
| `sfx-kit\earshot\` | four Earshot renders normalised the same way (`es_thud_diesel`, `es_clack`, `es_riser_1s`, `es_whoosh_paper`), raw takes in `raw\`, the exact commands in `COMMANDS.md` |
| `sfx-kit\build_kit.py` | rebuilds the kit from `downloads\` and `earshot\raw\`; edit the SLOTS table to swap a sound |
| `sfx-kit\downloads\` | data only, never run anything from here: Kenney Interface Sounds (GitHub mirror, 5.2 MB), Kenney UI Audio (`UI_SFX_Set.zip`, 1.4 MB, from OpenGameArt), the Clipwing real-sfx skill clone (26 MB, we use only its vendored uisfx CC0 mp3s), `openverse\` (7 Freesound CC0 previews, 174 KB, `credits.txt`) |
| `sfx-kit\test\` | the 6-event test: `events_test.json`, `sfx_track.wav`, `placement.txt` |
| `sfx_place.py` | events JSON + kit folder in, one placed 48 kHz stereo wav + `placement.txt` out |
| `sfx_lint.py` | independent re-measure of a rendered track against the events, deltas in frames, exit 1 if any is off by more than half a frame |
| `earshot\` | clone of github.com/Leonxlnx/earshot (v1.0.0, MIT, 82 MB). Do not run from inside it; the installed package lives in the venv |
| `venv-sfx\` | Python 3.12 venv with the Earshot base extra (about 400 MB). `venv-sfx\Scripts\python.exe -I -m earshot ...` |
| `sfx\` | the OLD synthesised kit (click, impact, riser, sub, whoosh). Not shippable, kept for reference only |

## Events JSON (the contract for words_to_props.py)

`tools\words_to_props.py` does not exist yet. When it does, it emits this list and `sfx_place.py` consumes it:

```json
[
  {"at": 0.5, "kind": "whoosh"},
  {"at": 0.9, "kind": "pop", "gain_db": -3},
  {"at": 3.0, "kind": "riser", "file": "riser_energy.wav"},
  {"at": 3.0, "kind": "hit"}
]
```

`at` is seconds on the reel timeline, `kind` is one of whoosh, pop, stamp, tick, click, notify, hit, riser.
Optional: `gain_db` (trim on top of the house peak), `file` (a kit file instead of the rotation), `variant` (n-th
candidate of that kind). `t`/`time` and `type` are accepted as aliases; a `{"events": [...]}` wrapper too.

## Use

```bat
set PY="%LOCALAPPDATA%\Programs\Python\Python312\python.exe" -I
cd /d "C:\Users\Parts\OneDrive - Elite Diesel Service\Desktop\VIDEO\tools"

:: place
%PY% sfx_place.py events.json --kit sfx-kit --out work\sfx_track.wav --cuts 12 --duration 32.0 --voice work\voice.wav

:: lint (reads the track, not placement.txt)
%PY% sfx_lint.py events.json work\sfx_track.wav
```

What `sfx_place.py` does with each kind (30 fps unless `--fps`):

- whoosh: loudest 5 ms lands 2 frames before `at` (the cut).
- hit, stamp: loudest 5 ms lands exactly on `at`.
- riser: last audible millisecond lands 2 frames before `at`, those 2 frames stay silent, the hit on `at` is its own event. It warns when the hit's own attack starts inside the gap (hit_deep_drop has a 72 ms build; `earshot/es_thud_diesel.wav` has 21 ms).
- pop, tick, click, notify: the onset starts on `at`.
- Repeated kinds rotate through the kit's takes so the same sound never plays twice in a row.
- Peaks are the kit's (whoosh -10, pop -12, stamp/hit -7, tick/click -17, notify -12, riser -12 dBFS) plus `gain_db`.
- One-style guard: gritty (recordings) and clean (bright digital UI) in one list is refused unless `--mixed`; neutral goes with either. `--style gritty` is the default pick order.
- Density guard: warns above one whoosh per 4 cuts (`--cuts N`) and above 3 sounds starting in any 1 s.
- Clip guard: if the sum would pass -1 dBFS the track is scaled and it says by how much.
- `placement.txt`: kind, file, requested time, anchor time, measured anchor on the rendered track, delta in frames, style, gain, rule. Warnings at the bottom.

### Mix under the voice (no sidechain, fixed -6 dB, loudnorm last)

`--voice voice.wav` prints this with the right numbers. The SFX bus is set so the hottest kit sound (-7 dBFS stamp or
hit) sits 6 dB under the voice stem's sample peak; with a voice stem at -16 LUFS the peak is usually near -3 dBFS, so
the bus trim lands around -2 dB. Then the sum is normalised once, at the end:

```bat
"%LOCALAPPDATA%\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin\ffmpeg.exe" ^
  -i voice.wav -i sfx_track.wav ^
  -filter_complex "[1:a]volume=-2.0dB[s];[0:a][s]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo" ^
  -c:a pcm_s24le voice_plus_sfx.wav
```

Replace `-2.0dB` with the number `--voice` prints (voice peak minus 6, minus the kit's -7). With a room-tone bed as well, use graph 5b in `research\2026-11-20-editing-sound-design.md` and feed this sfx_track as its third input. Mux into the reel with `-c:v copy -c:a aac -b:a 192k`, then verify with `-af ebur128=peak=true -f null -` (I near -14, true peak under -1.5 after AAC).

Single-pass loudnorm undershoots on short material (a 5 s synthetic test landed at -16.0 LUFS). For the final
render do it in two passes: run the same graph once with `loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null -`,
then rerun with `measured_I`, `measured_TP`, `measured_LRA`, `measured_thresh` and `offset` from that JSON plus
`linear=true` (the two-pass recipe in the 2026-11-20 sound doc). The same 5 s test landed at -15.1 LUFS two-pass,
limited by its own true peak; a real 30 s voice stem sits closer. Always read ebur128 after the encode.

## Test result (2026-11-21)

`sfx-kit\test\events_test.json`: whoosh 0.5, pop 0.9, pop 1.2, stamp 1.6, riser ending 3.0, hit 3.0, `--cuts 4`.
Picked: whoosh_air_short, pop_chip, pop_select, stamp_rubber, riser_long, hit_deep_drop (gritty + neutral, guard passed).
`sfx_place.py` measured each sound on its own placed segment: whoosh peak 0.4334 s (+0.00 frames against 0.4333),
pop onsets +0.00 and +0.00, stamp peak +0.00, riser end 2.9340 s (+0.02 frames against 2.9333), hit peak +0.00.
ffmpeg astats on the track agrees on levels: -7.00 dBFS in the stamp and hit windows, -10.00 in the whoosh window.

`sfx_lint.py` (independent scan of the mixed track): whoosh +0.00, pops +0.03 and -0.01, stamp +0.00, hit +0.00,
riser end +0.75 frames. That last one is real and is the warning sfx_place prints: hit_deep_drop builds for 72 ms
before its peak, so it starts sounding at 2.928 s, inside the 2-frame gap, and the lint sees the riser's fall later.
`events_test_fasthit.json` is the same list with `"file": "earshot/es_thud_diesel.wav"` on the hit: lint gives
whoosh +0.00, pops +0.03 and -0.01, stamp +0.00, riser end +0.01, hit +0.00, worst 0.03 frames (1 ms), exit 0.
Lesson: a riser-into-hit wants a hit whose attack is under 2 frames; es_thud_diesel (21 ms) or hit_bong_low (4 ms).

## House sound rules (restated from the 2026-11-20 playbook and the 2026-11-21 card-style notes)

- SFX are OFF by default when a song is added inside Instagram. The song carries the cuts; whooshes fight it. Only a real sound on a real reveal in a reel with no music, or UI ticks on card-only reels.
- Whoosh starts 2 to 3 frames before a cut and peaks on it; one cut in four at most. Impact on the exact frame of a hook text hit or reveal. Riser 1 s ahead with a hard stop and 2 frames of silence before the hit.
- SFX 6 dB under the voice. UI ticks lower still: chip pops, HUD fills and stamp slaps felt not heard (18 to 24 dB under the voice peak), typewriter keys on every other character only, one soft airy whoosh on the iris, nothing on caption words, the final 2.5 s hold silent.
- One SFX style per reel. Gritty mechanical, not clean dings. Rotate takes of any repeated sound.
- Never CapCut's library for Instagram use. Loudness -14 LUFS, true peak -1.5 after AAC, loudnorm last.
- Dialogue first (highpass 90, denoise, de-ess, 3:1, limiter, voice stem to -16 LUFS), then a room-tone or diesel-idle bed 26 to 30 dB under voice, then SFX.

## When a specific sound is needed: Openverse (Freesound CC0 through a key-free API)

Anonymous limits: 20 requests per minute, 200 per day, top results only (no deep paging). CC0 needs no credit, but
Openverse does not verify licences: open `foreign_landing_url` and check the Freesound page before a sponsor reel.
The `url` field is a 128 kbps mp3 preview (fine under a voice or a song, not for a sting that plays alone; the
original wav needs a Freesound login).

```bat
curl -s -A "elcoyote-sfx-kit/0.1" "https://api.openverse.org/v1/audio/?q=air%%20ratchet&license=cc0&page_size=20" -o hits.json
"%LOCALAPPDATA%\Programs\Python\Python312\python.exe" -I -c "import json;[print(r['duration'],'ms |',r['title'][:40],'|',r['creator'],'|',r['url'],'|',r['foreign_landing_url']) for r in json.load(open('hits.json'))['results'] if r['source']=='freesound']"
```

Useful params: `q`, `license=cc0`, `source=freesound`, `tags`, `extension`, `page_size` (max 20 anonymous).
`category=sound_effect` and `length=shortest` returned nothing for our queries on 2026-11-21; filter by `duration`
in the JSON instead. Drop the preview into `sfx-kit\downloads\openverse\`, add a line to `credits.txt`, add a SLOT in
`build_kit.py`, rerun it. For whooshes built to a move, Earshot can also make one to spec:
`venv-sfx\Scripts\python.exe -I -m earshot sfx render whoosh_fast/crisp -o w.wav --dur 0.8 --apex 0.32`.

## Not done, on purpose

- Earshot's listen extra (torch, 1.1 GB of models, 20 to 40 s per call) and its `timeline` sync audit. `sfx_lint.py` covers the timing check without models.
- The real-sfx agent loop, picture scan, beat snapping and masking critique. We use only its CC0 uisfx sounds; `from_cues.py` / `mix.py` stay in `downloads\` unexecuted.
- The official kenney.nl zips: the download button is JavaScript-gated, so the CC0 GitHub mirror and the OpenGameArt upload (same author, same licence) were used. Fetch from kenney.nl in a browser if a byte-identical copy matters.
- sfxmint could not be verified in the dossier and was not used.
