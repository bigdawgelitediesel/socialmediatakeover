# El Coyote signature style

**STATUS: the MAIN FONTS section is approved (his pick, 2026-11-23). Everything else is still a DRAFT, not approved by Jacob yet.** Austin Myers' signature-style prompt (reel DfKl-EPM0oI) says to study
three to five of his own edited videos, say what was observed and what is being suggested, and ask for his feedback before
saving it as approved. Nothing below becomes "the style" until he says so.

Identity: Jacob Dalton, @elcoyotediesel. Project Rival, a 1959 Ford F600 on a 7.3 Powerstroke, road to SEMA Nov 2 to 5, 2027.

## Main fonts (Jacob's pick, 2026-11-23: APPROVED)

Jacob, on @kalylsfilms reel DcBwAjvoEqI: "I love these fonts and want them as my main fonts in my style guide!"

| Role | His font | On this PC | Licence |
|---|---|---|---|
| The big word | **Impact** | Impact, the real font (ships with Windows) | fine in video; never commit the file to a repo or host it on a site |
| The classy line | **Snell Roundhand** | **Pinyon Script** stand-in (SIL OFL) | real one is paid (Linotype, about $30 a style) and built into Macs and iPhones |
| The painted word | **Rocktown** (by Khurasan) | **Permanent Marker** stand-in (Apache 2.0); Knewave on disk as a second option | real one is free for personal use only; an account with partners needs the paid licence |

- **Pairing:** the big word is always Impact, caps. One of the other two rides on it, never all three at once.
  1. Impact + painted word: two stacked Impact lines, yellow then red, one white brush word riding the seam between them at about half their height.
  2. Impact + classy line: round hand in yellow on top, Impact under it. For partners, names, places.
- **Colours, measured off his example:** yellow `#FDC43A`, red `#F04625`, white `#FFFFFF`. Soft dark shadow, no outline.
- **Where:** in the top third (y 0 to 620), never on his face.
- **In the tools:** Remotion overlay `mainlock` (`rival-reels/src/components/Main.tsx`; theme names `F.impact`, `F.round`, `F.brush`).
  For ffmpeg/ASS burns the font names are `Impact`, `Pinyon Script`, `Permanent Marker` (files in `tools/fonts`).
- **Replaces** as the default title: Archivo Black lines, and the A LOUDER / B MEGANTE / C TROPI lockups (kept on file, not the default).
- **If he buys the real fonts:** drop the files in `tools/fonts` and `rival-reels/public/fonts`, change two names in `theme.ts`. Nothing else moves.
- Captions were not part of the pick. They stay small white Poppins until he says otherwise (his example uses a bold serif).

## Text pairing and the behind-the-body rule (2026-11-23: APPROVED, his rules)

Jacob: "You need to learn how to properly pair text so it looks good." and "new rule if my body is in the way of what you are
going to post you need to put the title text behind me."

Pairing (rule 123, my reading of the @david_knowsai and @kalylsfilms reels):
1. One loud, one quiet. Impact is loud; the partner is at most about half its height.
2. The partner never covers the big word's letters. The brush word rides the seam between the two Impact lines; the round hand sits in clear space above.
3. One centre axis for every line.
4. The contrast is obvious (big against small, block against script) or it is not used.
5. Yellow, red, white. Always the same three.
6. Top third, the same place every reel.

Behind the body (rule 124, his words):
- Check the frame at the title's time. If his head, hat, hands or body reach into the title, make a cutout (`tools/matte.py`) and draw the
  Impact block under it: `mainlock` with `behind: true, part: "block"`, and again in front with `part: "partners"` only if the small line is in clear space.
- It must still read behind him: first and last letters clear of his head. If not, put the title on one line or move it. Never in front of him.
- Captions and beat words stay off his face.

## Examples studied (his own finished reels, in `My Drive\VIDEO\finished`)

1. Find the gratitude, final (2026-11-22): approved at 57.9 s, whole message kept, six cuts, a checklist card, lockup at 0.0.
2. Stomper Customs Announcement (2026-11-23): cab talking head, title PARTNER NO. 6, small captions.
3. Summit 7.3 BOGO Announcement (2026-11-23): truck cab, title BUY 1 GET 1 FREE, the flyer shown as a card in the top third.
4. Six Companies trial reels (2026-11-23): two-line block title, small captions, 19 to 33 s.
5. Bro to Bro trial reels (2026-11-23): text only over b-roll, yellow serif, music.

## What was actually observed

- **Colours:** footage left natural, no grade. Text is white or cream. Yellow only on the Bro to Bro set (copied from an example he sent). Brand kit on file: black #0b0b0c, cream #efe9dc, tan #c9b38c, oxblood #7a1f1f, yellow #f7d43c.
- **Fonts:** Archivo Black caps for titles (64 px, two lines, top of frame). Poppins SemiBold for captions (62 px). His three picked lockups are on file: A LOUDER (Kaushan Script + Anton), B MEGANTE (Archivo Black), C TROPI (Shrikhand). Instrument Serif for the serif accent.
- **Caption size and place:** small, plain, a few words at a time, centred at y 1345 of 1920. Soft shadow, no outline, no box, no word-by-word highlight.
- **Title:** one lockup at 0.0, held about 3 s, top third. Nothing else burned in on a plain talking head.
- **Pacing:** talking heads keep the whole message. Cuts land on breaths. 20 to 60 s, under a minute.
- **Camera:** alternating wide and punched-in framing between sentences (1.0 and about 1.18), a slow 3 percent push inside each shot.
- **Graphics:** one device per reel when there is one (a checklist card, a flyer card, beat words).
- **Transitions:** hard cuts. No fades, no outro, no call to action on screen.
- **Sound:** his voice, light cleanup, a quiet cab ambience bed. Song added inside Instagram. Sound effects off. Music was baked in only on the Bro to Bro set, at his request.

## What is being suggested (my read, for him to accept or change)

1. Eyes on the upper third line (y 625) in every talking head. They sit 150 to 200 px low today.
2. Captions no wider than 760 px and shifted left so they clear the like, comment and share buttons.
3. Titles bigger (done by the main fonts pick above: Impact at up to 250 px).
4. Keep everything else as it is.

## Files kept for future edits

- Fonts: `VIDEO\tools\fonts` and `VIDEO\tools\rival-reels\public\fonts`
- Font spec: social repo `research/FONT-LIBRARY.md`. Look guide: `research/2026-11-23-LOOK-GUIDE.md`
- Graphics kit: `VIDEO\tools\rival-reels` (colours and fonts in `src/theme.ts`)
- Safe zones: `VIDEO\tools\safezone.py` (rule 120)
