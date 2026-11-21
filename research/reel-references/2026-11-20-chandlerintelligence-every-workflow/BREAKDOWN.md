# Breakdown: @chandlerintelligence "Giving away EVERY WORKFLOW" (reel De8SPjEAuV0, 85 s, 19.1k likes / 21.9k comments, posted 2026-10-25)

Jacob sent it 2026-11-20: "Check out this post and this guys IG study it deeply." Video, nine 3 fps sheets, Whisper transcript with word timings, scene list and full-res key frames are in this folder. The reel is a reaction/breakdown: Chandler sits at his desk and takes apart @justyn.ai's "Claude edited this" reel (the one Jacob set as the bar), re-creating each effect on justyn's own footage and saying how it is done. He is the third creator in the same Claude-Code-editing niche after justyn.ai and viashaan.

## Who he is (profile sweep, 2026-11-20)
- Chanyoung Ryu, Seoul. KAIST computer science, software engineer, product at a Korean influencer-marketing platform, then Higgsfield (generative video), now CEO and co-founder of Feed Media (feedmedia.io), the global arm of a large Korean social agency. Verified badge. Bio: "master claude & ai / founder, engineer, pm".
- 105K followers, 60 following, 23 posts, all reels, no carousels. Grew from zero to about 90K in three months with 16 videos; bursty cadence of 3 to 4 reels a month.
- A third-party tracker (oleg.ae, 17 reels) had him averaging about 669K views per reel, median 105K, average 20.7K likes.
- The engine is the comment-to-DM funnel: 15 of the 23 captions open with "Comment JARVIS / EDIT / SLASH / STYLES / PLUGIN" for a free guide. That is why this reel has more comments than likes (21.9k vs 19.1k). His two biggest reels (6.7M and 2M views) are remixes of other creators' content, not his own editing demos; his own-workflow reels run 250 to 20K likes.
- Roughly half his reels are paid (#HiggsfieldPartner, #SpaceXAIPartner, CREAO, Typeless). The account is partly a showcase for his agency. Nothing published on GitHub or anywhere else; the "free workflow" only comes by DM. No link to justyn.ai or viashaan in either direction.

What this means for us: he is a marketer with an engineering background using a polished, cheap-to-make format. The format is the lesson, the funnel is a separate question for Jacob.

## What is on screen (85 s, 21 hard cuts, a new graphic every 1 to 2 s)
Framing: one room, him at a laptop with a Shure mic, medium and close framings, a dark warm grade. The reel he is reacting to lives in a picture-in-picture card that has two states: hero (about 560 px wide, top-left, with its own captions readable) when the referenced clip is the subject, and thumbnail (about 250 px wide, bottom-left above the laptop) when he talks. The card moves between the states with a motion-blurred slide, not a cut. That card is the backbone of the whole reel.

Beats:
1. 0.0 to 2.5 s, hook: "I didn't edit a single second of this video. Claude did." On screen the justyn footage re-cut with big sans caps on forest green ("I DIDN'T EDIT / A SINGLE / SECOND / OF THIS VIDEO.") then "Claude did." in serif with "did." in gold. He re-created the paid look on the seller's own footage.
2. 3.0 to 6.0 s: "This guy's selling this for 97 bucks. I'm giving it away for free." A $97 checkout card drops onto the PiP. Claim plus a villain plus a price in six seconds.
3. 6.2 to 12 s, text behind head: "cut you out with a person segmentation model" while his own frame shows the alpha matte on a checkerboard (he literally shows the mechanism), then "Text behind your head" in a typewriter mono sits behind him, then his name lockup "Chandler Intelligence" (yellow-green over white, mono) at the top. Brand stamp at 10 s, not at the end.
4. 12 to 14 s: CapCut and Edits app icons with a red cross. 14 to 22 s: captions. A GitHub repo card for openai/whisper (dark card, star and fork counts) at the top, then his direct critique of justyn: "I'd lose the green box though. Plain text with shadow looks way cleaner." His captions are exactly that: white bold sans, drop shadow, no box, one to three words, centered at about y 1180, occasionally one word in a coral highlight box ("timing", "every word").
5. 22 to 24.5 s: "One sentence and the whole video is edited. Watch." then a whip-blurred slide of the PiP card to full and a hard cut.
6. 24.5 to 31.5 s: "Ask Claude to draw these for you as vector graphics" with a prompt bar typing "make it more aesthetic" (dark rounded chat input, orange send button, caret blink). "The whole thing warms up": a slider reveal, a vertical white line with a <> handle sweeping across to show the warm grade, FFmpeg icon plus name at the top as he says it, Remotion named for the slider.
7. 31.5 to 37.7 s: magazine cover "CLAUDE" masthead behind justyn's head with cover lines and a barcode sticker; then the prompt that made it typed into the bar ("Make this a magazine cover: CLAUDE masthead behind my head, cover lines, a barcode and a sticker, one per beat").
8. 37.7 to 43.6 s: "You could create a mock-up of your editor timeline, but a real screenshot would look much better" with a timeline screenshot card sliding in from the top.
9. 43.6 to 49.7 s: the nested "picture of itself three levels deep" zoom on the word "this", then "These zooms are a bit too much in my opinion" with the frame going blurry on "opinion". The prompt for it is typed anyway.
10. 49.7 to 58.6 s: "Make it moody": a tone-curve panel at the top with sliders that move as he speaks the numbers: Highlights -35, Blacks +12, Saturation -15, Vignette -40. The footage under it darkens in step.
11. 58.6 to 68.7 s: his frame shrinks into the center tile of a 3x3 grid and eight reels pop in around it one per frame, then a yt-dlp repo card ("a free tool that grabs videos from Instagram, TikTok, YouTube").
12. 68.7 to 82 s: "before rendering it gives me a complete storyboard": a white Notion-style table "020 · Claude Edited This / Storyboard" with columns number, what he says, on screen, tool, rows animating in. "Have it write a storyboard so that you both agree on what the video looks like first. I always do this before I shoot."
13. 82 to 85 s: "Comment EDIT" with a giant hollow-outline EDIT behind his head. The CTA is one spoken line and one word behind him, no card.

Measured: constant 30 fps, 2545 frames; cuts land on sentence ends; motion per frame 0.6 to 1.9 on talking shots, 3.6 on the grid pop (deliberate). Audio -14.2 LUFS integrated, loudness range 2.4 LU (heavily leveled voice), true peak -0.4 dBFS, no gaps below -40 dB (a quiet bed under the voice the whole way). Color is dark and desaturated, warm practicals, nothing pushed.

## What this adds to the El Coyote kit (built the same night, tools/rival-reels/src/components/Chandler.tsx)
1. **PiP reaction card** (`pip`): a second video in a rounded card with keyframed hero and thumbnail states and speed-based blur on the move. This is the format for Jacob reacting to anything: a sponsor's product video, a competitor's build, a diesel meme, a comment, a parts listing, a Fullbay invoice, his own older reel. Cheap to make, one talking-head take plus one downloaded clip (yt-dlp works here).
2. **Plain captions** (`captionStyle: "plain"` or per caption `style`): white Poppins SemiBold 60 with a two-layer shadow, no pill, one to three words, y 1150, optional one-word coral highlight. This is his critique of justyn's pill and it matches Jacob's own rule (light, clean, no heavy boxes). Default for talking heads from now on; the oxblood pill stays as an option for loud comedic beats.
3. **Tool tag** (`tooltag`): icon plus name at the top center the moment a brand is named. For us that is the partner logo plus name when Jacob says Driven Diesel, ISSPRO, Power Hungry, Axiom.
4. **Slider reveal** (`slider`): vertical white line with a <> handle that reveals a CSS-filtered copy of the plate (warm look) or an image. For Rival this is the before/after device: rust to paint, F600 frame to Super Duty frame, stock to compound turbos. Stays in sync with the plate via the sequence start frame.
5. **Grid wall** (`grid`): the plate shrinks into the center tile of a 3x3 and eight images pop in around it one per few frames. Proof wall: past reels, partner logos, or every part on the bench.
6. **Param panel** (`params`): dark panel with labeled sliders that animate to values as he says the numbers. Tune values, boost and EGT targets, torque specs, the moody-grade recipe itself.
7. **Storyboard card** (`storyboard`): the four-column table (number, he says, on screen, tool) animating in. Also the format of the artboard we now hand Jacob before rendering, and before he shoots.
8. **Outline word** (`outline`): huge hollow caps meant for `behind: true`. His one-word CTA. For Jacob only when there is a real thing to give away (the Rival build list, the partner list, a parts spreadsheet); he has said on-screen CTA cards are lame, this is the quiet version.

Process rules confirmed by a second creator: storyboard before render and before the shoot; show the mechanism (the alpha matte on checkerboard, the sliders moving) instead of describing it; name the tool with an icon when you say it; a real screenshot beats a mock-up; skip recursive zooms ("a bit too much"), use whip-blurred moves on cards instead; brand stamp early (10 s), not at the end.

## Rules to carry forward
- Reaction format is now in the kit; it needs one clean talking-head take from Jacob and one clip to react to.
- Captions on talking heads: plain white with shadow, one to three words, no pill unless the beat is a joke.
- Every named partner gets a tool tag. Every before/after gets the slider. Every list of numbers gets the param panel.
- Storyboard table to Jacob before the render; shot list to Jacob before he films.
- Moody grade (highlights -35, blacks +12, saturation -15, vignette -40) is an opt-in look for dark talking heads only. Jacob's rule stays: no grade on his daylight shop footage without a before/after shown first.
- The funnel (comment a word for a DM) is his growth engine; it is a Jacob decision, not an editing default.
