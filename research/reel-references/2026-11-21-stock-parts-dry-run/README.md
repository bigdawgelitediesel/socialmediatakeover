# Dry run: "Every stock part leaving this 7.3" (2026-11-21, scratch voice, NOT for posting)

The first end-to-end run of the menu-reel pipeline built this morning. Machine time about five minutes. Files here: script.txt, words.json (from the scratch voice), report.txt (pacing), stock-parts.props.json, stock-parts.sfx.json and the cleaned event list, placement.txt (frame deltas), stock-parts-sheet.png. The renders stay local in `VIDEO/tools/rival-reels/out/stock-parts/` (stock-parts-video.mp4 silent, stock-parts-POST-scratchvoice.mp4 with the Kokoro voice and the CC0 sfx at -14 LUFS). The voice is synthetic, so nothing from this folder goes to the Drive or to Instagram; Jacob records the lines and the same spec re-runs on his words.json.

## Commands (from VIDEO/tools; PY = %LOCALAPPDATA%\Programs\Python\Python312\python.exe)

1. `PY -I vo_scratch.py rival-reels\out\stock-parts\script.txt rival-reels\out\stock-parts\vo --voice am_michael --speed 1.1 --takes 2` (132 s; report said 138 wpm, hook 9 words in 3.8 s, total 41 s)
2. `PY -I words_to_props.py specs\stock-parts.json rival-reels\out\stock-parts\vo\words.json rival-reels\out\stock-parts\stock-parts.props.json` (plan table, 9 items, 41 overlays, 19 captions, 42 sfx events)
3. `cd rival-reels && npx remotion render src/index.ts CardReel out/stock-parts/stock-parts-video.mp4 --props=out/stock-parts/stock-parts.props.json --codec=h264 --crf=18` (65 s for 42.7 s)
4. `PY -I sfx_place.py <events.json> --kit sfx-kit --out sfx_track.wav --duration 42.71 --style gritty --voice vo.wav --placement placement.txt` (all deltas 0.00 frames; one density warning at the 37.7 s gauges chips, 5 sounds in a second)
5. ffmpeg mix: voice + sfx at -6 dB, loudnorm I=-14 TP=-1.5, `aformat=sample_fmts=fltp:channel_layouts=stereo`, video copied.

## What the sheet shows (stock-parts-sheet.png)

HUD dots fill 1 to 9; each item: STOCK row strikes and takes the RIVAL stamp, the card drops 0.5 s later, chips pop on their spoken words (Forged, Billet, Roller lifters, Regulated return, Compounds, Hybrid, Boost, EGT, Fuel pressure), partner cards carry the logo tile and the PARTNER sticker, the injector card counts to 600 hp, the sidebar highlights the current item, captions are plain white with one tan-boxed accent; iris into the RIVAL comment gate with the nine-item DM preview.

## Critique for the next pass

- The content sits high: HUD 300, strike row 560, card to about 1000, captions 1130, sidebar 1320. Push the strike row to 640 and the card to 840 so the middle of the frame carries the weight (the grid crop keeps y 480 to 1440).
- Cards and chips can grow 10 to 15 percent; the nxtlvl card fills about 85 percent of the width.
- Fix words_to_props: the events list no longer carries a hard "file" path (patched after the first run); gauges chips crowd the last second (three chips in 1.5 s plus the gate iris), spread them or cut one.
- Voice: 138 wpm is under the 150 floor at speed 1.1; Jacob's real read will be faster and shorter. The script should lose four to six words per item.
- This is the one-a-week card-only format. The same spec can run on RivalReel over a talking-head plate (set composition RivalReel, plate, cutout) and then only the sidebar, HUD and cards appear with his face.
