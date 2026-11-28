# Studio-quality motion brief (saved 2026-11-23)

The quality standard for every edit. From Austin Myers' "Studio-quality Motion Brief" (reel DfKl-EPM0oI), read off the screen.
It applies to captions, graphics, footage, cutaways and sound. The look itself comes from `Signature Style/` and the reel's direction.

1. **Build around what he is saying.** Show ideas through actions: a choice gets selected, a stack builds, a number
   changes, a panel opens to show something useful. Graphics make the point clearer. No unrelated icons, no captions alone filling the screen.
2. **Make the reel feel connected.** Carry something into the next moment: a word becomes a title, a line becomes a
   divider, a panel grows into a video, a shape becomes the next scene's frame. Use these where they help the story. Let other moments hold.
3. **Give motion weight.** Decide how each object starts, speeds up, lands and settles. A heavy panel, a paper note and
   a small label move differently. Use anticipation, overlap, recoil, blur, shadow and depth when they fit. Never the same bounce or slide on everything.
4. **Object movement and camera movement are separate.** The camera holds still while a graphic builds, unless a
   reframe, zoom or reveal has a clear purpose. Use layers in front of and behind the person. Check the cutout edge in motion.
5. **Captions are designed for a phone.** They match the real words and their timing. Clear line breaks, deliberate
   placement, good contrast, room around the face and the app buttons (rule 120 zones). A strong caption can also just sit still long enough to read.
6. **Pace follows the delivery.** Fast passages get tighter cuts and denser builds. Calm passages get room. No constant
   camera movement, endless pop-ins, generic gradient backgrounds or clutter.
7. **Sound matches the action.** The hit lands on the visible contact, landing or change. Mix textures with restraint.
   Speech stays clear. Leave quiet moments. Not a sound on every word. (House rule: sound effects off unless he asks.)
8. **Study examples in motion, then frame by frame** around the key builds and handoffs. Record the timing, spacing,
   size change, overlap, settle and sound that make them work. Use the findings to build original moments in his style.
9. **Inspect the real rendered file before showing it.** Fast transitions frame by frame, caption timing, edges,
   readability, sound sync. Fix accidental jumps, overlaps, clipped words and unfinished graphics. If a part could not be
   watched or heard, say so and ask him to check it.

## Numbers to work to (added 2026-11-24)

Read out of four open editing kits (Herk Edit Kit, HyperFrames, OpenFilm, OpenMontage) and rewritten for this kit.
They are starting points measured on other people's reels, not law. Jacob's own notes beat all of them.

**Cutting speech**
- Cut BETWEEN phrases, at real silence. Never inside a phrase. A filler that runs straight into the next word stays, because cutting it clips the words around it.
- A pause under about 0.55 s is his natural rhythm and stays. A trimmed pause keeps a breath: 0.14 s, 0.20 s after a sentence, 0.24 s after a long pause.
- Keep the last clean take of a repeated line. Join two takes only where both sides are silent.
- A repeated word can be emphasis ("never, never"). Every stutter or false start is shown to him as a question, not cut on its own.
- Speech starts within about 0.1 s of frame one. The file ends right after the last word. Never fade the last word.
- `python -I tools/cutfind.py <words.json>` lists the pauses and the mistake candidates. It proposes; step 2 of the workflow approves.

**Motion**
- Arrivals ease out hard. Exits are about half as long as arrivals. Camera moves ease in and out.
- Words arrive 2 to 3 frames apart. A good plain entrance: each word from a 6 px blur to sharp in about 4 frames.
- Once a title has landed it holds dead still. Only the next thing moves.
- A line stays up about 0.5 s plus 0.3 s a word. Nothing readable under 28 px on a phone frame.
- Text behind him reads best with 30 to 55 percent of it covered. Check it against the cutout over the whole time it is up, because his head moves.

**Captions**
- Break on his own pauses. Never between a number and its unit. Hold about 0.2 s past the last word. Close gaps under 0.15 s so captions do not flicker.
- Never over his mouth or chin, least of all in the first 2.5 seconds.

**Checks on the rendered file, before he sees it**
- Transcribe the FINAL render and compare the words at every cut with the raw clip. A matching word count is not proof; a clipped word still transcribes.
- A strip of frames across every cut (10 each side) catches one-frame flashes that single stills miss.
- Read the first 2.5 seconds frame by frame.
- Loudness on the delivered file: about -14 LUFS, true peak at or under -1.5.
- Say which checks could not be done. Levels are not listening. A transcript is not hearing the edit.

**The loop**
- Every note he gives becomes a line in `LEARNINGS.md` or the skill the same day, so he never gives the same note twice.

