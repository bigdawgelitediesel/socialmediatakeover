# Breakdown: @justyn.ai "Claude edited this" (reel DehbdDYssBE, 56 s, 11.5k likes / 22k comments)

Jacob sent this 2026-11-20 as the quality bar. Watched at 2 fps (six sheets in this folder). This is the "motion graphics on a talking head" tier, and it is a branded SYSTEM, not a set of effects. It also carries the three process points he says in the audio: use the strongest model at max effort, give Claude a brand style guide plus sample reels you like, and ask for a shot-by-shot artboard before rendering.

## What is actually on screen

Brand kit (every element obeys it):
- Palette: deep forest green (#1f3a2d-ish) as the dominant card and pill color, cream/off-white (#efe9dc) for type and cards, burgundy accents, a mustard yellow card once. Nothing outside this palette appears.
- Type: a high-contrast serif display (EB Garamond / Cormorant family) for titles, caps, letterspaced, built word by word or letter by letter; the same serif in italic for the accent word inside captions; a small-caps sans for micro labels ("PICK THE RIGHT", "SHOT BY", "GIVE CLAUDE YOUR STYLE"). Numerals "1 2 3" as huge serif chapter marks that stack in one by one.
- Captions: one short phrase at a time (3 to 5 words), serif, cream on a dark green pill, bottom-center, the key word in italic or in a lighter tint. Every phrase sits in a pill; no stroke, no shadow.

Composition grammar:
- Talking head alternates between three framings (wide on a stool, medium, close) and two rooms; cuts land on sentence breaks and often carry a 3 to 6 frame directional blur or a whip.
- Floating "cards" illustrate nouns the instant they are spoken: four reel thumbnails fan in when he says "this video, this video"; a HELLO name tag when he says his name; a week calendar fills with green blocks for "free up time"; a model dropdown animates to "Opus 5.5"; an effort dial turns to MAX; a swatch fan for "brand style guide"; a stack of sample reels; a "Requirements" card with lines struck through; a comments stack for testimonials; a NEXT WEEK stamp; a waitlist card writing "you" on line No.1; the word EDIT dropping in as letters; a comment box typing EDIT; a brand guide document; an artboard grid of shots; a render progress bar 21 to 100 percent; fast-forward icon.
- Big single words as punctuation: ZERO, 1, 2, 3, BETTER RESULT, built with serif letter animation and sometimes with a mirrored echo behind.
- Rhythm: a new visual element every 1.5 to 3 s without exception; the frame is never static for more than 2 s. About 25 distinct overlay moments in 56 s.
- The opening 4 s: title "CLAUDE EDITED" in the serif builds while four reel cards pop in one per spoken "this video", then a hard cut to a full-green card with the same title, then back to him. Hook, proof and brand in one move.
- Ending: "BETTER RESULT." builds letter by letter, period lands last. No CTA card (the CTA is spoken mid-reel, with the comment-box card illustrating it).

## What this means for El Coyote

1. The ceiling is motion graphics tied to the words, not transitions or captions. Every overlay is a reusable component: title build, chapter numeral, caption pill with italic accent, floating card (image or UI mock), word stamp, strike-through list, progress bar, comment stack, calendar fill, dial. That is a Remotion component library, exactly Phase 2 of the playbook. ASS captions cannot do any of the cards.
2. It needs a brand kit first. El Coyote already has colors (black #0b0b0c, Coyote tan #c9b38c, oxblood #7a1f1f) and now fonts (Combo A: Kaushan Script + Anton + Poppins Italic; Combo B: Archivo Black deep red; Combo C: Shrikhand). The equivalent of his serif-on-green is our Anton-on-oxblood or tan-on-black pill. Write the kit as a Remotion theme file.
3. The script drives the graphics: every noun that can be shown gets a card. For Rival: part photos, the build list rows, the partner logos, the portal countdown, the parts invoice, a Fullbay screenshot, the SEMA floor plan, torque spec cards. Jacob's talking-head clips (like the Driven Diesel announcement) are the raw material this treatment is built for.
4. Process change he names and we adopt: show Jacob a shot-by-shot artboard (frame grid with the planned overlays drawn in) BEFORE rendering, take feedback, then render. We did grids after; move them before.
5. Shoot-side: he uses three framings and two rooms for one script. Jacob should record each talking piece twice (wide and close) so the cut can alternate.

## Build plan (Phase 2, concrete)
- `tools/rival-reels/` Remotion project (Node 24 present, benchmarked 24 s per 5 s on this CPU). Theme: colors, fonts (static TTFs via @remotion/fonts), spacing.
- Components v1: TitleBuild (serif/Anton letter stagger), ChapterNumeral, CaptionPill (phrase + italic accent, from words.json groups), FloatingCard (image/screenshot with spring in, slight tilt, drop shadow), WordStamp, StrikeList, ProgressBar, CommentStack, Dial, LogoRow (partner logos from the portal).
- Bridge: the existing EDL JSON plus an `overlays` list ({at, dur, component, props}) generated from the transcript by Claude, reviewed on the artboard.
- Plates from ffmpeg (tone-mapped, trimmed, short GOP); final mux and loudnorm in ffmpeg; export recipe unchanged.
- First target: re-cut the Driven Diesel announcement (IMG_4252, already posted plain) as the internal A/B to prove the tier, then use it on the next partner reveal.
