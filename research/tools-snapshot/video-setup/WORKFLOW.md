# The editing workflow (saved 2026-11-23)

Source: Austin Myers (@itsaustinmyers) reel DfKl-EPM0oI, his "Workflow prompt", read off the screen and fitted to this shop PC.
Jacob, 2026-11-23: "Study this and do what it asks."

This order is followed for every reel, even if a skill suggests another order. The tools' own technical rules still apply.
Every step is recorded with `python -I tools/reel.py`, so a new chat can pick up where the last one stopped.

## The seven steps

1. **Project and transcript.** `reel.py new "<name>" <clip> [<clip> ...]`. The reel gets its own folder in `Projects/`.
   The original recording is never moved, renamed or changed (the project only stores its path). It is transcribed with
   word timings (`work/<clip>/words.json`). Captions are always timed from the edited footage, not the raw clip.
2. **Rough cut. STOP.** Mistakes, repeated takes and pauses that drag come out. His meaning and natural delivery stay
   (rule 115: cut filler, never meaning). No titles, no graphics. He watches it WITH SOUND and approves before anything is dressed up.
3. **Creative direction.** After the rough cut is approved, ask him how the reel should feel and whether he has extra clips,
   pictures or music. He owns the direction. Offer ideas only if he says he is unsure. One question at a time.
4. **Beat plan. STOP.** Turn his direction into a beat-by-beat plan for the whole reel: captions, cutaways, graphics,
   camera moves, pacing, sound, transitions. Offer a picture storyboard of the same plan (`tools/artboard.py`).
   He approves before the opening is built.
5. **Opening. STOP.** Build the first 10 to 15 seconds from the approved plan and show it with sound. If the whole reel
   is shorter than that, show the whole reel. He gives feedback before the rest is built. Update the plan if his feedback changes it.
6. **Full video.** When the opening and any plan changes are approved, build the whole thing. Check it (below), show it,
   and take changes the way he gives them: "at 6 seconds, change this."
7. **Final approval. STOP.** Wait until he clearly approves one specific video. Then `reel.py finish` saves that exact
   file, updates the notes and cleans up. A preview, or "keep going", is not final approval.

## Standing rules

- Final exports keep the original quality and frame rate unless he asks otherwise. Smaller previews are fine.
- Clear mistakes and how they were fixed go in `Setup/LEARNINGS.md` (`reel.py learn "..."`). A lasting style change is
  saved to `Signature Style/SIGNATURE-STYLE.md` only when he asks. One video's special request does not become a rule for every video.
- Cleanup removes only `work/tmp` inside the project. Originals, the final, approved examples, editable work,
  tools, speech models and notes are kept. Unknown files are left alone.
- Before step 2: `tools/lightcheck.py` on the raw clip (Setup/LIGHTING.md). If the light fails, say so before cutting.
- Checks before he sees a full video: a full-size first and middle frame (look guide), `tools/safezone.py`,
  `tools/smooth_check.py`, caption timing against the cut, loudness.
- Claude cannot hear. Every time something is shown, say plainly that the sound was checked by levels and transcript only,
  and ask him to listen. Never claim a review that was not done.
- A fast job he asks for outright ("make 20 versions of this") can skip the stops. The stops are for a reel being built from a new recording.

## Where things live

| His folder | Here |
|---|---|
| Raw | `My Drive\VIDEO\raw` and `My Drive\VIDEO\inbox` (phone uploads) |
| Projects | `VIDEO\Projects\<date> <name>\` (work, exports, notes); finals also go to `My Drive\VIDEO\finished` |
| Signature Style | `VIDEO\Signature Style\` |
| Setup | `VIDEO\Setup\` (this file, MOTION-BRIEF.md, TOOLS.md, LEARNINGS.md) and `VIDEO\tools\` |
