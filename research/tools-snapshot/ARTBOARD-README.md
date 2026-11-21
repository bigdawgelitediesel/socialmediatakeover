# artboard.py: approve the layout before the render

## Purpose

The playbook (2026-11-20) says: artboard before render. This is the tool for that step.
Give it a Remotion props JSON and it renders only the frames that matter, the planned ones:

- frame 4 (the hook check)
- every overlay's `at` plus half a second (the element is landed, the animation has settled)
- the last frame

It labels each still with the time, the overlay that owns it and what else is on screen, draws the IG
safe lines on every tile (solid red at y 1440, the text floor; dashed red at y 480, the top of the
grid-safe band) and tiles everything into one contact sheet. Jacob looks at one PNG, not a 45 s render,
and says yes or redlines it. A 23-tile sheet costs about 20 s; the full render costs minutes and a re-render
after a layout note costs minutes again.

Alongside the PNG it writes a markdown file with every tile, its planned content and lint warnings:

- any overlay or caption whose text would sit below the 1440 floor
- more than one hook element on frame 4
- two cards overlapping each other
- an overlay type that is not in REG (it would render nothing)
- an overlay that runs past the end of a CardReel

The lint heights are estimates from the component defaults, not measured pixels. The sheet is the truth;
the lint only says where to look first.

## Usage

```
cd "C:\Users\Parts\OneDrive - Elite Diesel Service\Desktop\VIDEO\tools"
python -I artboard.py rival-reels\out\stock-parts\stock-parts.props.json
python -I artboard.py rival-reels\out\fx-test.props.json
```

Any Python works. If Pillow is missing the script re-launches itself in `tools\venv-artboard`
(Pillow lives there, nothing was installed into the system Python). With no Pillow anywhere it falls
back to ffmpeg drawtext + tile, which gives plainer labels and no tile-number badges.

Options:

| flag | default | meaning |
|---|---|---|
| `--comp CardReel\|RivalReel` | auto | auto picks RivalReel when the props have a `plate`, else CardReel |
| `--out dir` | next to the props file | where the PNG and MD land |
| `--cols 6` | 6 | columns on the sheet |
| `--max 24` | 24 | tile cap; over the cap the tool keeps the most spread-out frames (hook and last always stay) |
| `--extra 0.5` | 0.5 | seconds after each overlay's `at` to sample |
| `--tile 320` | 320 | tile width in px |
| `--keep` | off | keep the rendered frames folder (path is printed) |
| `--no-pil` | off | force the ffmpeg labelling path |

Outputs: `<name>-artboard.png` and `<name>-artboard.md`, where `<name>` is the props file name without
`.props.json` (so `stock-parts.props.json` gives `stock-parts-artboard.png`).

Duration comes from `durationSec` for CardReel and from ffprobe on `public/<plate>` for RivalReel.
Frames closer than 10 frames to one already chosen are folded into it, so a hud + sidebar + card that all
start together make one tile, not three. Rendering goes through one `remotion render --image-sequence
--frames=a,b,c` pass, which is roughly five times faster per frame than one `remotion still` per frame
because fonts and the bundle load once.

## Reading the sheet

- yellow badge = tile number; a red badge means the lint has a note on that tile
- line 1 of the strip: tile number, time in seconds, frame, HOOK or LAST
- line 2: the overlay that owns the tile (type: title/text), `[behind]` when it sits behind the cutout
- line 3: everything else on screen (`*` = behind) and the live caption
- solid red line = 1440, nothing with text below it (IG caption block starts about 1520)
- dashed red line = 480, with 1440 it bounds the band that survives the 4:5 feed crop and the UI

## How Jacob redlines

Reply with the tile number and the change, one note per tile. Examples:

```
07: drop the item card to y 820, it is kissing the strikestamp
12: kill the caption, the card already says it
01: hook too small, headline size 72
19: fine
```

The editor applies the notes to the props JSON, runs artboard.py again, and only when the sheet comes back
clean does the full render start. "Approved" on the sheet is the green light for the render.

## Files

- `tools\artboard.py` the tool
- `tools\venv-artboard` Pillow venv it uses for labels
- `tools\rival-reels` the Remotion kit it renders from (`--kit` to point elsewhere)
