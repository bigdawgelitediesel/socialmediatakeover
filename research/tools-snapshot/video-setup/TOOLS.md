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

## Added 2026-11-24: four open editing kits, cloned and read

From the "4 free GitHub repos" reel (DfmlI5sNFVa). Clones (about 1.5 GB) are on this PC only:
`Desktop/socialmediatakeover/research/reel-references/2026-11-24-DfmlI5sNFVa/clone/`. None of them is installed.

| Kit | Licence | What was taken | What was left |
|---|---|---|---|
| Herk Edit Kit (nateherkai) | MIT | The three cutting scripts, copied to `tools/herk/` with the licence and wrapped by `tools/cutfind.py`. The editing playbook's rules (MOTION-BRIEF). | Its ElevenLabs transcriber, AI b-roll, music and sound effects. The AIS brand files are not licensed for reuse. |
| HyperFrames (heygen-com) | Apache 2.0 | Motion and caption numbers (MOTION-BRIEF). | Not installed: telemetry is on by default, the skill fetches a CLI at run time, and Remotion already does titles behind the cutout. If it is ever tried, set `HYPERFRAMES_NO_TELEMETRY=1`. |
| OpenFilm (openfilm) | MIT | Caption break rules, the post-render check idea. | Not installed: its skill runs the newest npm version every time, library search sends queries to their server, Windows transcription is one thread. |
| OpenMontage (OpenMontageInc) | AGPL 3.0 | Ideas only, rewritten: the "does this clip stand alone" test, review rules. | No code copied (AGPL). Most pipelines use AI pictures, voices and music. |

`tools/cutfind.py <words.json> [--gap 0.55]`: tested 2026-11-24 on a 21 minute interview transcript (133 pauses, 127 s of dead air, 30 stutter candidates) and a short clip. Needs only node.

New overlays in `tools/rival-reels` (`src/components/Code.tsx`): `backdrop`, `objection`, `stattiles`, for beats drawn from code with no footage under them. Sample: `out/code-sample.props.json`.

