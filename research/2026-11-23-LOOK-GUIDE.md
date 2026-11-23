# The look guide: what the reels actually look like (2026-11-23, written on the laptop)

Why this file exists. On 2026-11-22 the laptop session edited "Find the gratitude" five times from the written rules, passed every lint, and Jacob took the post down the same night: "the edit sucks, like the lighting ... the first shot is all washed out", then "I gave so much info and reels to look at and you've only got worse". The rules were read; the reels were never looked at. This file is the result of looking: Jacob's five finished reels at full size, and about 75 contact sheets across the 61 folders in `research/reel-references` (talking heads, motion-graphics, diesel and truck). It records what is on screen, not why it performs. Where it disagrees with a rule file, look at the reel again before trusting either.

Limits: contact sheets are one or two frames a second, so entry animations, exact cut timing, sharpness and sound were not judged. `jessicacarter-profile` has no sheets. Sizes are fractions of the frame, read off thumbnails, good to about 0.03.

## 1. Picture first. Nothing ships washed out.

- Every winner in all three sets has real contrast: blacks stay black, sky is deep blue, paint and skin are saturated and a little warm. None is flat or lifted. This holds for ungraded phone footage (most diesel winners) as much as graded reels (Caleb Ralston warm golden hour, Jacob Kitton cool and moody in a vehicle, justyn and chandler dark rooms with a warm lamp).
- Jacob's own Driven Diesel and Move Bumpers reels look like this: deep blue Wyoming sky, natural skin, shadow under the cap brim.
- What went wrong on the laptop: `tools/streamline.py` tone-mapped iPhone HLG with `npl=100` and mobius, which lifted a direct-sun selfie until the face was red and shiny and the wall was white. Fixed to `npl=203` with hable (HLG reference white). `light-options.jpg` from that night is the before and after.
- "No color grade" means do not add a look. It does not mean ship a bad conversion. Correct exposure and contrast so skin reads natural and blacks are black.
- Check before anything is delivered: open one full-size frame of the first shot and one from the middle. Skin natural? Blacks black? Sky or wall not blown? If not, fix the conversion before any text goes on.
- Shooting side, from the references: soft light from the front or side (window, shade, low sun), camera at eye level, not from below, depth behind the shoulder. A hard-sun selfie from below (the gratitude clip) starts behind and the edit can only recover part of it.

## 2. The hook: big, high, and off the face

- Jacob's liked reels: tan and cream Anton block caps, three short lines, about half the frame wide, upper right, partly behind his head (needs the matte), on from frame one.
- Motion-graphics references agree: justyn's cream serif caps at 0.85 of frame width from 0.15 to 0.45 of height with the cap brim over the letters; chandler's hollow outline word behind the head; ultraskills pushes the face down to make room.
- Talking-head references: the title sits in the top 10 to 20 percent, above the head, 70 to 85 percent of width, one or two lines. Each creator has one title look and keeps it.
- Diesel and truck: one small line in the upper third in a pill or with a thin outline, or no text at all.
- Nobody puts the hook low on the chest. The laptop cut did, because the face filled the upper third and the matte model was missing. The fix is the matte (behind the head) or a frame with room above the head, not a lower hook.
- White or cream reads; tan on bright footage does not.

## 3. Captions: small, plain, chest height

- Across all three sets captions are small (text height about 0.03 to 0.04 of frame height), 2 to 4 words, one line, about half the frame wide, at 0.60 to 0.70 of height, which is the chest. Soft shadow, no stroke.
- Jacob's two liked treatments: the oxblood pill with one tan italic word (Driven Diesel) and plain white with one coral-boxed word (Move Bumpers). Both sit at about 0.66 of height with the card directly under them.
- One highlighted word per phrase at most, and it needs contrast against the footage behind it.

## 4. Something new every 2 to 4 seconds, and it is not a cut in the talking

- Driven Diesel: eight cards and two full-screen cutaways in 31 s. Move Bumpers: hook, tool tag, a list card twice, a comment card, plus he moves the camera. Harley Trade: a new shot every 2 to 3 s.
- Motion-graphics references: a new card every 1.5 to 3 s, holding 1.5 to 3 s.
- Talking-head references hold the talking shot 5 to 20 s uncut and make the change with overlays in clean space, a notebook insert every 4 to 6 s (Mariah), image tiles every 2 to 6 s (Jun Yuh, Caleb), a counter or countdown ring.
- The laptop cut had two extras in 58 s and long stretches of one shot. That is the "plain" Jacob saw.

## 5. Cards: brand-coloured objects, in one of two places

- Jacob's cards are cream with rounded corners, oxblood and tan type, a soft shadow, about 0.7 of frame width, and they sit directly under the caption on his chest. Never on the face.
- The motion-graphics references put cards above the head (0.10 to 0.40 of height, 0.75 to 0.9 of width). Either zone works; pick one per reel.
- Cards look like real things: a logo, a photo, a list, a comment box, a chart, a screenshot.
- The laptop's dark `checklist` box did not match the cream card family. Use the cream family (`logo`, `photo`, `spec`, `strike`, `comment`) or restyle before using a dark one.
- Two or three colours and two fonts per reel, carried through hook, captions and cards.

## 6. Cutaways are full frame

- When he names the truck, the whole frame goes to the truck and the caption and card keep running over it (Driven Diesel: the F600, then pressure-washing the block).
- Truck b-roll is close and low: the truck fills 60 to 90 percent of the frame, cropped by the edges, from wheel or bumper height, with the camera moving. Details are extreme close: a badge, a wheel, a hand on a switch.
- A small picture-in-picture window is the weaker version. Use `G:\My Drive\VIDEO\raw` for clean footage; the finished lyric reel has burned-in text and cannot be reused.

## 7. The first frame

- Title already on, and something already happening: mid-gesture, smoke, a key turning, a proof image up.
- Jacob's ask is the same thing in his words: "grab attention right off the bat".

## 8. What reads as cheap

Flat or bright plates; outlined or neon text effects; more than three colours; a hook low in the frame; captions too big; long stretches with nothing new; a dark card on a cream system; letterbox bars or mixed aspect ratios; a truck lost in a wide shot.

## 9. The look check (run it before Jacob sees anything)

1. First frame, full size: exposure, skin, blacks. Compare side by side with a frame from Driven Diesel.
2. Hook: upper part of the frame, off the face, white or cream, readable at thumbnail size.
3. Count the new things: one every 2 to 4 s across the whole reel. List the gaps over 5 s.
4. Every card: cream family, under the caption or above the head, never on the face.
5. Every time he names something that exists as footage, the frame goes there.
6. Captions: small, chest height, one accent word that can be read.
7. Send Jacob one still of the first frame before any render over two minutes, and never post without his go.

## 10. What Jacob asks for, in his words (2026-11-22)

"I want the whole message in there." "I do still need it under a minute." "Let's just keep it creative." "I want this to grab attention right off the bat." "Look at the other videos you made me as well, those are better."

## Sources

Jacob's finished reels in `My Drive\VIDEO\finished` (Dougie, Driven Diesel, Harley Trade, Move Bumpers, Rival Lyric); `research/reel-references` (all 61 folders, about 75 sheets viewed); `research/reel-references/2026-11-21-caption-audit/CAPTION-AUDIT.md` for measured caption sizes; `research/reel-references/2026-11-20-smoothness-pass/NOTES.md`.
