# Breakdown: @viashaan "captions behind my head" (reel DfSrDF-Riau, 9.3 s, 21.7k likes, 25k comments)

Shaan Johari, creative director at AI Makeover (Liam Ottley's channels). Caption: "What I filmed vs what Claude Code turned it into. Same take, every layer added by AI." Jacob sent it 2026-11-20: "Study this reel in this guy's account." His profile and TikTok are private, so this is the one video; the reel, a 6 fps sheet and the transcript are in this folder.

## What is on screen (9 seconds, studied at 6 fps)
Format: a split-screen "RAW | EDITED BY AI" presentation on a warm brown grain background with a date and a title ("HOW CLAUDE EDITS MY VIDEOS"). The right pane is the finished reel; the left is the untouched phone take. The presentation itself is a reusable device (before/after proof).

The edited pane, beat by beat:
1. 0.0 to 1.6 s "Wait, how are these words going behind my head?": color grade from flat kitchen to warm amber with a curtain backdrop (the background is replaced or heavily graded, the subject keeps his real lighting); words appear one at a time in a mixed serif italic ("Wait,") and white sans ("how are these words") and they sit BEHIND his head and shoulder. That needs a per-frame person matte: text layer under a cutout of him.
2. 1.6 to 3.3 s: a hard cut to a stylized frame, his silhouette in black on a cream card, "behind my head?" in big serif italic, a thick brown looping stroke drawn through the frame, then a flash of his inverted silhouette (negative) on black for two frames. Pure matte work again: silhouette = alpha filled black.
3. 3.3 to 4.6 s "It's tracking my face": a tracking HUD, "tracking my FACE" in serif + heavy caps with a yellow cursor block, small monospace readout "FACE 0.929  X 0605 Y 0971" and yellow corner brackets that follow his head.
4. 4.6 to 5.8 s "10 times a second": a giant yellow "10x" with "a second" small, the readout updates (0.933, 0.924) with each sample.
5. 5.8 to 9.2 s "and it knows where all of Instagram's buttons are so my captions never end up underneath them": white sans captions that drift to wherever there is room, up and left of his face, away from the right-hand button column; "underneath them." lands bottom-left.

Craft notes: every text layer has subtle motion (drift, scale pop), two type voices (editorial serif italic + plain bold sans) plus a monospace for the HUD, a single accent yellow, dark warm grade, zero stock effects. The hook is a question answered by the visual within two seconds.

## What this adds to the El Coyote kit (verified on this PC tonight)
1. **Text behind the subject.** Robust Video Matting (ONNX, MobileNetV3) runs on this CPU at about 11 frames a second at 1080x1920 (a 31 s reel mattes in about 90 s). `tools/matte.py` writes a VP9 WebM with alpha; the Remotion composition now has a `cutout` layer, and any overlay flagged `behind: true` renders under it. The hook can sit behind Jacob's head the way his does. The same alpha gives silhouettes, knockouts and the negative flash.
2. **Face-aware layout.** OpenCV's YuNet detector tracks the face at 215 frames a second (10 samples a second costs nothing). `tools/layout.py` returns a caption y below the chin when there is room, above the forehead otherwise, never below y 1248 where the Instagram caption block lives, and a card zone that avoids the face. This fixes the exact problem the Driven cut had (cards on his face).
3. **The HUD** (FACE 0.93, X/Y readout, corner brackets) is a cheap component and a good "look what it does" beat if Jacob ever wants a behind-the-scenes reel; not for diesel content by default.
4. **Before/after split presentation** as a reusable frame for "what I filmed vs the edit" or for build before/afters.

## Rules to carry forward
Track the face on every talking-head plate and feed captions and cards through the layout helper. Keep two type voices per reel at most. One accent color. When text goes behind the subject, keep it big and short (one to four words) so partial occlusion still reads.
