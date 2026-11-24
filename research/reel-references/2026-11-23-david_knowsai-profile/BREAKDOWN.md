# @david_knowsai, the profile (studied 2026-11-23)

David Ho. Instagram: 203K followers, 15 following, 130 posts (logged-out page, 2026-11-23).
Jacob, 2026-11-23: "Study this profile and apply what he teaches to help you edit correctly. You need to learn how to properly pair text so it looks good."

## What could and could not be seen

- Instagram does not list a profile's posts without a login, and the house rule is public sources only. His reels are mirrored
  on a public YouTube Shorts channel (`youtube.com/@david_knowsai`, 92 Shorts listed in `shorts.txt`).
- 8 of the 92 were downloaded and run through watch.py: the two about editing, three about content, three recent ones.
  Frame sheets were read for 3, full-size frames for 5, transcripts for 5. The other 84 were read by title only.
- The YouTube titles do not always match the video (the one titled "19 effects for Claude motion" is the Wi-Fi reel),
  so there may be an effects reel that was not found. YouTube view counts are tiny (4 to 2,300) and say nothing about how the reels do on Instagram.
- He does not teach text pairing in words in anything seen here. What follows on text is read off how his own reels are built.

## What he teaches (his words, from the transcripts)

1. **Captions stay off the face.** "It picks the best takes, adds captions that stay off your face, and puts in graphics and sound effects." (5 editing skills)
2. **Loudness has a target.** His editing reel shows a meter moving from -36 to -14 LUFS. We already mix to -14.
3. **Take a reel you like apart before you build.** "Give it a reel you like and it breaks down the hook, the pacing and the editing. Then it uses that structure to build a video around your own topic." Also: "break down each video's hook, storytelling structure, and visuals. Find the patterns they have in common."
4. **Edit from the retention graph.** After about 48 hours give the retention graph and the timestamped transcript: "find the biggest drop-offs. Show me what I was saying at those moments and suggest one change to test for each clip... make new versions with those changes. Keep the originals so I can compare them." The changes he names: "a shorter opening, a faster explanation, or an earlier reveal."
5. **Audit the script before filming.** "Identify the weakest part of the hook, vague claims, and repeated points. Then rewrite it without changing my message or voice." And: "show me the original line, your replacement, and why you changed it."
6. **Change requests are plain and specific.** "Make the opening faster and hold the product close up longer."

## How his text is built (read off the frames; the same in every reel seen)

- The frame is split in half: a screen recording or graphic on top, his face on the bottom. Neither half ever has text laid over it at random.
- **Exactly two text objects, and they are opposites of each other:**
  - a **title pill**: white pill, dark semi-bold sans, sentence case, one emoji, about 34 px on a 1080 frame. It sits on the seam between the two halves and stays up for the first few seconds.
  - a **word pill**: dark pill, white caps, one word (two or three in his October reels), about 28 px. It sits just above the seam and changes with every word.
- One font family for both. The contrast comes from polarity (white pill against dark pill), case (sentence against caps) and job (stays against changes), not from a second typeface.
- Both are centred on the same vertical line. Both are small. Neither ever touches his face: the seam is the dead space between the graphic and his head.
- The position never moves from reel to reel, so a viewer knows where to look.

## The pairing rules taken from it (rule 123)

Written for Jacob's main fonts (Impact, round hand, brush). This is my reading of why his text and Kalyl's look right, not a quote.

1. **One loud, one quiet.** Never two loud things. Impact is the loud one; the partner is at most about half its height.
2. **The partner never covers the loud word's letters.** It sits on the seam between two lines, or in clear space above.
3. **One axis.** Everything is centred on the same line.
4. **The contrast is obvious or it is not there.** Big against small, block against script, yellow against white. Nothing "a little" different.
5. **Three colours, always the same three:** yellow, red, white.
6. **Same place every reel:** the top third.
7. **Text lives in dead space.** If his head or body is in that space, the text goes behind him (rule 124).

## What was changed in the editor

- `mainlock` (Main.tsx) was rebuilt on these rules: the brush word now rides the seam between the two Impact lines at about half their height
  instead of lying across the letters; everything shares one centre; the round-hand line scales with the block.
- `part: "block"` with `behind: true` draws the Impact lines under the person cutout; `part: "partners"` keeps the small line in front in clear space.
- Test frames on the F600 cab clip: `kit-test-behind.jpg`. First attempt on a tight selfie failed (his head hid most of the word); second attempt
  hid the second line behind his head and was fixed by putting the title on one line. So the check "can it still be read" is part of the rule.

## Not taken

Comment gates on every reel, the split-screen screen-recording layout (he is showing software; Jacob is not), pills as the caption style (Jacob's captions stay plain).
His retention-graph loop is worth doing once Jacob can send a retention screenshot from Insights; nothing was built for it here.
