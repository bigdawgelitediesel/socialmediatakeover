# Tools check (2026-11-23, shop PC, Windows 11)

Austin Myers' setup prompt (reel DfKl-EPM0oI) lists seven tools. Each one was run on this PC, not just looked up.

| His list | Here | Status |
|---|---|---|
| FFmpeg + ffprobe | ffmpeg 9.0.2 | runs |
| Python | 3.12.10 | runs |
| Node.js | 24.18.0 | runs |
| yt-dlp | 2026.10.26 | runs |
| WhisperX (word timings) | faster-whisper 1.2.1, word timings through `tools/watch.py` | runs. Same job, so WhisperX was NOT installed (it needs a torch install of about 2 GB) |
| HyperFrames (graphics from code) | Remotion kit in `tools/rival-reels`, 75 components | runs. Same job, so HyperFrames was NOT installed. It is on npm (0.9.87) if Jacob wants a second engine |
| Playwright (browser checks) | Remotion's own headless Chrome | runs. Playwright was NOT installed, nothing needs it |

No paid voice, avatar or media service is part of this setup.

## Working helpers (code that runs, not descriptions)

| Helper | Job | Tested |
|---|---|---|
| `tools/reel.py` | project folder, step record, approval stops, finish, cleanup | 2026-11-23 with disposable files: refused out-of-order steps, refused "ok" and "keep going" as approval, saved the final, removed only `work/tmp`, left the source file and other work files alone |
| `tools/watch.py` | transcript with word timings, frame sheets, scene list | used all day 2026-11-23 |
| `tools/build_reel3.py`, social repo `tools/streamline.py` | the cut | used on every delivered reel |
| `tools/safezone.py` | draws the rule 120 zones over frames | 2026-11-23 on four reels |
| `tools/smooth_check.py` | choppy-motion check | in use |
| `tools/artboard.py` | picture storyboard | in use |
| `tools/matte.py` | person cutout for layered graphics | in use |
| `tools/rival-reels` | motion graphics (Remotion) | 2026-11-23: all 17 tenfoldmarc effects rendered in one proof, `out/all17.mp4` |

## Not tested yet

The seven-step workflow has not been run on a real recording. `reel.py new` with transcription on a real clip, and the
stops with Jacob actually answering, still need a real reel.
