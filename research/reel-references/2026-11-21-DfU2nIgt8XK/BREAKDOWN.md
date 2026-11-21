# @ai.nxtlvl "Stop paying for these 9 apps" (DfU2nIgt8XK)

Studied 2026-11-21 at Jacob's request ("study this"). Files here: reel.mp4 (1080x1920, 30 fps, 52.5 s, VP9 from IG dash), reel.info.json, reel.description, scenes.csv, sheet-01..03.jpg, shots/, transcript.txt, words.json, frames/ (hook, card entry and CTA tiles at 5 to 10 fps).

## Stats (from the IG metadata at download time)

| | |
|---|---|
| Posted | 2026-11-04 |
| Likes | 7,259 |
| Comments | 9,185 (more comments than likes: the comment gate is doing the work) |
| Length | 52.5 s |
| Caption | "Comment REPO and I'll DM you all 9 links", then the 9 paid-to-free pairs as a list, "Save this before you renew", a question, 5 hashtags |

## What it is

A 100 percent motion-graphics reel. No face, no footage, no b-roll. One continuous "scene" (PySceneDetect found a single shot) because nothing ever hard-cuts: every change is an element animating on or off over a fixed cream background. A voiceover (clean, close-mic, 152 words per minute, longest pause 0.54 s, mastered to -14.3 LUFS, -0.3 dBTP, LRA 2.2) drives everything. The video is a visualisation of the script, word by word.

## Layout (fixed for the whole reel)

- Background: warm cream (#EDE8E0 range) with a soft vignette, zero texture. Reads like paper.
- Top HUD row at y about 100: a `0/9` counter pill on the left followed by 9 progress dots that fill one at a time in coral, and the handle `@ai.nxtlvl` on the right in small mono. The HUD is the retention device: you can always see how far along you are, which answers "how long is this" without a progress bar.
- Caption line at y about 220: one short phrase, grey sans, per-word reveal, with ONE accent word per phrase set in italic serif on a coral highlight pill ("Open Generative AI.", "cinematic", "fully local,", "own server.", "one click.", "REPO", "links."). The accent word is always the payoff noun of the phrase.
- A pixel mascot (coral robot with a thought bubble) parks on the top-right corner of whichever card is current. It gives the eye a fixed anchor and makes the brand recognisable at thumbnail size.
- Content zone y 320 to 1250: the cards. Everything sits in the middle 60 percent of the frame, clear of the IG UI on the right and the caption at the bottom.
- Everything is centred on a single column, 760 to 940 px wide.

## Structure with timestamps

| Time | Beat | What you see |
|---|---|---|
| 0.0 to 2.0 | Hook: "Stop paying for these nine apps." | 3x3 grid of real app logos, each in a white card with a red `PAID` tag. The viewer recognises the apps they pay for in under a second. The word "9" and "apps." pop into the caption as they are spoken. |
| 2.3 to 5.1 | Promise: "GitHub has a free version of every single one." | Every logo gets struck through and a green `FREE` tag stamps on, one card at a time, left to right, top to bottom (9 stamps in 2 s). Then a green ribbon "ALL FREE ON GITHUB" slides in under the grid. This is the contrast beat before the payoff. |
| 5.2 | Item 1 setup: "Higgsfield?" | Grid is gone. A thin `PAID  logo  Higgsfield  $ / month` bar at the top of the content zone. The name gets struck through 0.5 s later. |
| 6.1 to 11.7 | Item 1 payoff | A big white card drops in from below with a soft shadow: icon tile (coral), repo name in bold, `owner/repo` in mono under it, a `★ 4.4K stars` counter that counts UP to 32.2K over about 0.6 s, an `OPEN SOURCE` green tag, then feature chips ("AI images", "Cinematic video", "600+ models") that pop in ON the spoken word, a footnote line, and a green `FREE` sticker that slaps onto the bottom-right corner. |
| 12.1 to 16.5 | Item 2 (ElevenLabs to VoiceStudio) | Same template. Each item: name question (0.5 s), replacement name with accent pill, card drop, 2 to 3 feature chips on the words. |
| 16.9 to 21.2 | Item 3 Semrush to OpenSEO | Same. The card first appears ghosted (low opacity) for about 0.3 s then resolves: the "loading" state is the entrance animation. |
| 21.6 to 26.1 | Item 4 Notion to AppFlowy | Same. |
| 26.6 to 30.4 | Item 5 Wispr Flow to OpenWhispr | Same. Note "even offline." gets the accent pill. |
| 30.9 to 34.3 | Item 6 Asana to OpenProject | Same. |
| 34.9 to 39.0 | Item 7 Calendly to Cal.diy | Same. |
| 39.3 to 43.4 | Item 8 Intercom to Chatwoot | Same. |
| 43.9 to 46.9 | Item 9 Loom to Cap | Same. HUD now reads 9/9, all dots filled. |
| 47.0 to 47.6 | CTA transition | A coral circle grows from a dot to fill the frame, then shrinks back: a 0.6 s iris wipe that is the ONLY full-frame transition in the reel. It resets the eye for the ask. |
| 47.6 to 49.9 | CTA: "Comment REPO and I'll send you all nine links." | A fake IG comment box: avatar, "you · just now", the word REPO typed in, a heart appears on it. Then a fake DM notification card slides up under it: "Messages · now, Your 9 free repos" with 9 numbered chips filling in 2 per beat. The viewer watches the exact outcome of commenting before they comment. |
| 49.9 to 52.5 | Hold | 2.6 s of the final frame with no audio. Long enough to read the list of 9, which doubles as a screenshot/save target. |

## Timing grammar measured from the frames

- One new visual element every 0.9 to 1.3 s for the full 52 s. Never a static second.
- Each list item is 3.7 to 5.6 s: 0.5 s question, 0.5 s strike, 0.5 s card drop, 2 to 3 s of chips, overlap into the next question. Nine items in 42 s.
- Card entrance: translate up about 40 px + fade + slight overshoot, roughly 12 frames. Chips: scale from 0.8 with a 6 frame pop. Stars: counter tween over about 18 frames. Strike-through: wipes left to right over about 8 frames. All eased, nothing linear.
- Spoken word and the matching chip land on the same frame. The caption word reveal is also frame-locked to the voice (per-word timing, then the accent word pill lands with the word).
- No sound effects were detectable as separate hits; the voice carries it. (If there are UI ticks they are below the voice bed.)
- The whole thing is a three-part arc the playbook already uses: hook (grid you recognise), contrast (PAID to FREE stamps), payoff loop x9, then the ask.

## Why it travelled (9,185 comments on 7,259 likes)

1. The hook frame is a wall of logos the viewer pays for. Instant self-identification, zero reading needed.
2. "9 free versions" is a list promise with a visible counter, so people stay to the end to get all nine, and the end frame is a screenshot-able list (saves).
3. The payoff per item is a concrete, visible proof object (a repo card with a star count), not a claim. Numbers counting up read as evidence.
4. The ask is demonstrated, not stated: a fake comment and a fake DM reply show the mechanic, which lowers the friction to comment. The comment gate ("REPO") turns intent into a ranking signal and feeds a DM list.
5. Template discipline: once the viewer learns the card layout at item 1, items 2 to 9 cost zero cognitive load, so retention holds across a 52 s video with no face.

## What is portable to El Coyote / Project Rival (concrete)

The content is unrelated to trucks, but the format is a "swap list" and Rival is literally a list of parts being swapped. Direct translations:

1. **"Stop running these 9 stock parts" / "Every part leaving the F600":** 3x3 grid of the stock parts (photos in white cards, red `STOCK` tag), stamp `RIVAL` or the partner logo on each, then one card per part: partner logo tile, part name, a counter (hp, psi, lbs, dollars saved), 2 to 3 spec chips on the spoken words, `SPONSORED` or `BOUGHT` sticker. Nine items in 45 s. Ends with "comment RIVAL and I'll DM you the full parts list" which is also a sponsor-pitch asset (DM list = audience you own).
2. **HUD counter `3/9` + dots at the top** of every list reel. Cheap, keeps people to the end, brands the series. Add to the Remotion kit as `ProgressHud`.
3. **Accent pill = payoff noun.** Our caption rule already has one tan accent word; the discipline here is that the accent is always the noun the card proves. Keep it a serif italic on a filled pill, not a colour change.
4. **Strike-through wipe + stamp** (`StrikeStamp` component): wipe a line through the old thing, slap a tag on it. We have StrikeList; this is the single-item version with a stamp.
5. **Counter tween** (`CountUp` on SpecCard): any number on a card should count up over 15 to 20 frames. Star counts, horsepower, dollars, miles.
6. **Ghost-then-resolve card entrance** for "loading a part": 0.3 s at 30 percent opacity then snap to full. Reads as "fetching".
7. **Demonstrate the CTA**: a fake comment box with the keyword typed and a fake DM card listing what they get. Build `CommentGate` (comment box + DM preview) in Remotion. Use it on every comment-gated reel.
8. **Iris wipe (coral circle) as the one full-frame transition** between the list and the ask. One per reel, 0.6 s.
9. **2.5 s silent hold on the final list frame**, no music, no fade. Gives the save and the screenshot.
10. **Caption copy repeats the list in text** so it is searchable and save-worthy on its own, then one question to farm replies.

## What NOT to copy

- No face at all works for a software account; for Jacob the face and the truck are the asset. Use this grammar as the overlay layer on top of his footage or as a card-only series (one per week max), not as the default.
- The cream-and-coral palette is theirs. Ours is black, El Coyote tan and flat 307 red, Anton/Oswald/Inter per the brand rules, with the Kaushan/Archivo lockups for titles.
- The mascot: skip unless we draw a coyote mark; a bad mascot is worse than none.

## Render notes for our stack

All of this is Remotion-native: fixed background composition, `<Sequence>` per item driven by words.json timings, spring() for card drops, interpolate() for counters and strike wipes, a `<ProgressHud count total>` that reads the current item index. No plate video needed (or a blurred still of the truck as the paper). Audio: voice bed only, -14 LUFS, optional UI ticks at -22 dB on chip pops. Export per the house recipe (H.264 High, crf 17, bt709 tags).
