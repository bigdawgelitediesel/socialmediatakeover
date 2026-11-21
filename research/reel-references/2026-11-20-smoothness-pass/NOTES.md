# Smoothness pass, 2026-11-20 night
Jacob: "Make sure the reels aren't too choppy... They have to still feel smooth... I'm teaching you, it would suck if you don't remember in the future."

Measured (tools/smooth_check.py, per-frame motion curves at 90x160 with grain averaged out): Harley Trade, Dougie Shop Tour and Driven Diesel v3 are all constant 30 fps, zero duplicated or dropped frames, all sources true 30 fps, Remotion frame-accurate to its plate (motion-curve correlation 0.99 at lag 0, 0.14 at a one-frame shift), slow-mo interpolated smoothly.

What actually reads as choppy: shutter strobe. The phone exposed the dance at a fast shutter, so arms are tack sharp while they jump 40 px between frames. Fix: `"mblur": true` on the slot (minterpolate 120 fps, tmix 3, back to 30; about 1 s of render per output frame at 1080x1920; RIFE on the Intel UHD 770 is no faster). Applied to the five Dougie dance shots and re-delivered; the two PNGs here show before (top row) and after (bottom row): moving limbs blur, toolbox and truck stay sharp.

Not choppy: handheld selfie drift on the Driven talking head (vidstab took it from 4.7 to 4.5 motion per frame; left alone, no mblur on faces).
Lint fix in the same pass: `lockup` captions have script + block instead of text; the hook word count now reads either.
