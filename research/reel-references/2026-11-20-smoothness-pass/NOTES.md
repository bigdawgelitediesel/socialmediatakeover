# Smoothness pass, 2026-11-20 night
Jacob: "Make sure the reels aren't too choppy... They have to still feel smooth... I'm teaching you, it would suck if you don't remember in the future."

Measured (tools/smooth_check.py, per-frame motion curves at 90x160 with grain averaged out): Harley Trade, Dougie Shop Tour and Driven Diesel v3 are all constant 30 fps, zero duplicated or dropped frames, all sources true 30 fps, Remotion frame-accurate to its plate (motion-curve correlation 0.99 at lag 0, 0.14 at a one-frame shift), slow-mo interpolated smoothly.

What actually reads as choppy: shutter strobe. The phone exposed the dance at a fast shutter, so arms are tack sharp while they jump 40 px between frames. Fix: `"mblur": true` on the slot (minterpolate 120 fps, tmix 3, back to 30; about 1 s of render per output frame at 1080x1920; RIFE on the Intel UHD 770 is no faster). Applied to the five Dougie dance shots and re-delivered; the two PNGs here show before (top row) and after (bottom row): moving limbs blur, toolbox and truck stay sharp.

Not choppy: handheld selfie drift on the Driven talking head (vidstab took it from 4.7 to 4.5 motion per frame; left alone, no mblur on faces).
Lint fix in the same pass: `lockup` captions have script + block instead of text; the hook word count now reads either.

## Driven Diesel v4 (same night, Jacob: "Now apply these to the driven diesel reel")
Plate rebuilt from out/driven-v2-plate.json with `stab: true` + `mblur: 2` (180-degree shutter) on the ten IMG_4252 handheld slots and `mblur: 2` on the DJI slot; the IMG_3856 static shot untouched. `mblur` now takes a number (3 = dance, 2 = talking head/handheld). Measured motion per frame dropped on every handheld shot (for example 4.94 -> 4.66, 5.18 -> 4.15, 3.97 -> 3.38) with the face still sharp. Then the full chain again on the new plate: tools/matte.py cutout, tools/facetrack.py (new tool, replaces the inline YuNet snippet), out/gen_driven4.py props (hook now `align: right` so it clears his head), Remotion render, ffmpeg mux. tools-snapshot/driven_v4_pipeline.sh is the one-shot chain. Delivered as POST THIS (v4 smooth, text behind head); v3 kept as alt.
Plate note: the NOCAP plate reports transfer/primaries unknown after stab+mblur (BAD TAGS from the tool's own check); the final mux re-tags bt709 explicitly, verified. Worth fixing at the slot level later.
