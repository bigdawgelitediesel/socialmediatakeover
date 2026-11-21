# Fresh short-form editing tutorials, Oct 7 to Nov 21 2026 (what is new vs. the master playbook)

Written 2026-11-21. Scope: YouTube tutorials and breakdowns on Reels, TikTok and Shorts editing uploaded in the last 45 days. Method: 30 YouTube Data API searches (publishedAfter 2026-10-07, sorted by view count, 17 query angles) plus 10 extended web searches, 60 candidates ranked by views and relevance, 22 transcripts pulled through Supadata and saved in `research/transcripts/2026-11-21-*.txt` (index in `research/transcripts/2026-11-21-INDEX.txt`). Three long videos were keyword-skimmed rather than saved. yt-dlp returned HTTP 429 on subtitle downloads all session, and the Supadata free plan (100 per month) ran out after transcript 27, so six candidates are listed but not transcribed.

Everything below is judged against `2026-11-20-EDITING-MASTER-PLAYBOOK.md` and the ten lane reports. "NEW" means it is not in those documents. "CONFIRMS" means a second independent source agrees with a rule we already have. No em-dashes.

## 0. The one-paragraph read on the month

The editing-tutorial space on YouTube flipped in the last six weeks. Of the 60 candidates that ranked for plain queries like "reels editing tutorial" or "talking head editing", 35 are about Claude editing the video (Claude Motion shipped in beta on Oct 8, 2026; Anthropic's launch video sits at 1.51M views; the Team and Enterprise-only beta pushed Pro and Max users to Claude Code + Remotion, which is exactly our stack). The craft content inside those videos is still real: Joseph (Ultimate Editors) published the two most detailed style breakdowns of the month, and every "AI edits my reel" video ends with the same critique list (text too small, first five seconds too slow, face held four seconds with nothing moving, graphics entering late relative to the word). The non-AI craft videos worth having were about speed-ramp curve logic, color node order, text animation values, audio hooks, and Meta's Edits app gaining speed curves (Nov 12). Nothing this month contradicts the playbook's core rules; several things sharpen them, and three new QA tools are worth copying.

## 1. Video table

Views are as of 2026-11-21. T = transcript saved, S = keyword-skimmed only, X = not transcribed (plan limit).

| # | Title | Channel | Uploaded | Views | Length | URL | Got |
|---|---|---|---|---|---|---|---|
| 1 | How to Edit VIRAL Talking Head Videos Using ONLY Claude! (New Minimal Style) | Joseph, Video Editing | 2026-10-31 | 290,983 | 20:57 | https://www.youtube.com/watch?v=g9xoKm5DEeU | T |
| 2 | How to Edit VIRAL Instagram Reels Using Opus 5.5! (New Style in 2026) | Joseph, Video Editing | 2026-10-11 | 190,407 | 17:17 | https://www.youtube.com/watch?v=5UnK3c-nlIs | T |
| 3 | How To Make Insane Motion Graphics With Opus 5.5 (Claude Motion) | kaye.creatives | 2026-10-14 | 723,540 | 12:24 | https://www.youtube.com/watch?v=AsvN_feasyY | T |
| 4 | How To Make Insane Video Editing With Opus 5.5 (Claude Motion) | kaye.creatives | 2026-11-07 | 294,807 | 15:21 | https://www.youtube.com/watch?v=FJZkfjM8WhI | T |
| 5 | Claude Just Dropped MOTION (Get Ahead of 95% in 11 Minutes) | Tristen O'Brien | 2026-10-14 | 596,387 | 11:23 | https://www.youtube.com/watch?v=yf2OwchM9nw | T |
| 6 | Claude Edited This Netflix-Level Documentary (Copy Me) | Zane Hoyer | 2026-11-03 | 311,200 | 5:43 | https://www.youtube.com/watch?v=e2Fykz51Nxg | T |
| 7 | Automate Your CapCut Editing With Claude (Step by Step + Free Skill) | Matt Loui | 2026-10-23 | 363,267 | 9:40 | https://www.youtube.com/watch?v=U-AdnIz1jIk | T |
| 8 | How to Edit Videos With Claude Code (From a 10-Year Editor) | Stockton Walbeck | 2026-10-28 | 39,987 | 10:01 | https://www.youtube.com/watch?v=gM40EV6Esh0 | T |
| 9 | Insane GitHub Repos To Actually 10x Claude Video Editing | AI LABS | 2026-11-02 | 144,795 | 14:57 | https://www.youtube.com/watch?v=oTWUyW_bR-g | T |
| 10 | 8 Easy Text Animations in After Effects | theRichy | 2026-10-07 | 36,432 | 15:05 | https://www.youtube.com/watch?v=F6I_zPfi0UQ | T |
| 11 | How to Make VIRAL YouTube Shorts Captions in One Click (Vizard) | Thomas Creates | 2026-11-03 | 15,410 | 9:55 | https://www.youtube.com/watch?v=8sb2R11FeVw | T |
| 12 | Dynamic Auto Captions Tutorial (Filmora) | Ka Production | 2026-10-17 | 12,131 | 3:16 | https://www.youtube.com/watch?v=3WMazrwPDkw | T |
| 13 | All 70 Graphics That Turn a Podcast Into a Show (DaVinci Resolve) | Letta Edit | 2026-10-20 | 74 | 4:06 | https://www.youtube.com/watch?v=zhjqLOKL-IU | T |
| 14 | The Retention Trick Pro Editors Never Share | GrowthalgoYT | 2026-10-21 | 3,781 | 5:03 | https://www.youtube.com/watch?v=LdajwuyD28I | T |
| 15 | How to Make SMOOTH Speed Ramps in After Effects (Beginner Tutorial) | AM Film | 2026-10-12 | 5,695 | 6:21 | https://www.youtube.com/watch?v=LLottFJnMhI | T |
| 16 | 5 Color Grading Mistakes Ruining Your Footage In DaVinci Resolve | Mehran Hadad | 2026-10-11 | 76,265 | 8:44 | https://www.youtube.com/watch?v=U1BreW0Fe6U | T |
| 17 | iPhone 18 Pro Max Camera Settings You MUST Change! | Think Media | 2026-10-21 | 59,637 | 16:17 | https://www.youtube.com/watch?v=aZ2CsOKd5XU | T |
| 18 | Trending Slow Motion Edit in Edits App (speed curves) | Creator Swift | 2026-10-28 | 62,295 | 0:48 | https://www.youtube.com/watch?v=xEtVdcmzhxk | T (Hindi, glossed) |
| 19 | CapCut Editing Tricks That Look Pro: Text Behind Your Head, Speed Ramp on a Beat, Glow Title | socialcontentking | 2026-11-07 | 20,096 | 0:18 | https://www.youtube.com/watch?v=CsY9aOy3kYw | T |
| 20 | Audio Hooks for Short-Form Video: 5 Sound Tricks That Keep Viewers Watching | socialcontentking | 2026-10-22 | 825 | 0:48 | https://www.youtube.com/watch?v=WqmKMfMkrZw | T |
| 21 | I Tried Fully Automating My Video Editing With AI (RAW RESULTS) | Ali Abdaal | 2026-10-26 | 631,397 | 46:33 | https://www.youtube.com/watch?v=C0jOKDJtK9s | S |
| 22 | How I Get Claude To Edit My Videos (Step-By-Step) | Matt Wolfe | 2026-11-04 | 116,044 | 32:45 | https://www.youtube.com/watch?v=ep4psgAFOqc | S |
| 23 | Talking Head Motion Graphics Reel Breakdown In Premiere Pro | Usman Explains | 2026-10-07 | 135,539 | 20:47 | https://www.youtube.com/watch?v=uW-8SKO8kYE | S |
| 24 | Introducing Claude Dashboards and Claude Motion | Claude (Anthropic) | 2026-10-08 | 1,513,075 | 1:22 | https://www.youtube.com/watch?v=en0GuyhieQk | context only |
| 25 | ChatGPT can now edit videos in CapCut, Full Tutorial | Matt Loui | 2026-11-13 | 174,938 | 10:07 | https://www.youtube.com/watch?v=3vcuIfG5o0E | X (partial read) |
| 26 | I Built a 1-Click Speed Ramp Plugin for DaVinci Resolve (Let's Ramp) | The Car Video Guy | 2026-10-15 | 48,872 | 12:49 | https://www.youtube.com/watch?v=pQQbSMJ3cSM | X |
| 27 | how to SPEED RAMP in Premiere Pro (Full Tutorial + SUPER Slow Motion 1%) | Foebus dela Paz | 2026-11-01 | 21,680 | 29:15 | https://www.youtube.com/watch?v=I0BjUzAlRXI | X |
| 28 | Final Cut Pro Captions Just Got Ridiculous (Magic Mode Upgrade) | Editor's League | 2026-11-07 | 1,506 | 3:13 | https://www.youtube.com/watch?v=0eTqUDW14VY | X |
| 29 | Edit 10 Videos a Day With Claude (No Editor Needed) | Aaghaz | 2026-10-14 | 1,258,715 | 10:49 | https://www.youtube.com/watch?v=RDOy_HkTWyY | X (Hindi only) |
| 30 | 3 Hook Formulas That Stop The Swipe | CORDIMITE | 2026-11-16 | 1,179 | 1:17 | https://www.youtube.com/watch?v=AG6q5fEOMdE | X |

Web sources used for facts not in a transcript: Social Media Today on the Edits app Nov 12 update (speed curves, audio auto-adjust, text animation duration controls) https://www.socialmediatoday.com/news/metas-edits-app-gets-speed-curves-and-auto-audio-balancing/874586/ ; 9to5Mac on Edits for Mac, Nov 5 (multi-track, color grading, 4K export, Apple silicon only, no Windows) https://9to5mac.com/2026/11/05/instagram-launches-edits-for-mac-with-multi-track-video-editing-and-4k-exports/ .

## 2. New techniques by lane (recipes)

Each entry: what, values, why it works, who showed it, how we build it (ffmpeg 9 or Remotion 4). Items marked DERIVED are my translation of a creator's qualitative note into a number we can test; treat the number as a starting point.

### 2.1 Hooks

**H1. Audio-first hook set (NEW, five variants).** socialcontentking, 0:48, 2026-10-22.
- Sound-first open: a shutter, a pour, a zipper (for us: a ratchet click, an air gun, a bay door chain) is heard 6 to 10 frames before the first frame shows anything legible. "The ears hook before the eye."
- Mid-sentence start: cut into the first line halfway through a thought ("...and that's why the 7.3 is still here"). The brain wants the beginning and keeps watching to reconstruct it.
- Silence drop: kill music and ambience for 0.5 s right before the key line (we already use this as the contrast beat before the payoff; new is using it inside the first 3 s).
- Room change: a texture shift from clean lav audio to raw on-camera audio (or the reverse) signals "something changed". For us: DJI Mic 2 lav line into raw iPhone shop audio when he walks to the truck.
- Off-screen voice: someone asks a question before Jacob is in frame ("Jake, is that really the whole engine?").
- Build: words.json gives word boundaries, so mid-sentence start = pick the in-point at a word boundary 40 to 60 percent into the first clause and let the caption group start there too. Silence drop = `volume=enable='between(t,A,A+0.5)':volume=0` on the bed and song stems, never on the voice stem. Sound-first = `adelay` the video-synced audio by 0 and start the picture on black for 6 to 10 frames with the SFX at -8 dBFS (`-filter_complex "[0:v]tpad=start_duration=0.3:color=black[v]"`). Off-screen voice needs a second person at the shop; log it as a shooting-brief item, not an edit.

**H2. Hook card rule: the accent word is the curiosity word, not the noun (NEW nuance).** Joseph, 2026-10-11: "the speaker is always on screen during the hook, subtitles sit in the lower half, and the captions highlight the one word that makes you keep watching." In "29 year old engine. 67 year old truck." the tan word is "67", not "truck". Build: in the EDL hook block, require `accent:` to be set explicitly; lint warns if the accent word is a noun that also appears in the frame.

**H3. Director rules as a pre-build checklist (NEW as a tool, CONFIRMS as rules).** hashu-motion (AI Labs, 2026-11-02) encodes: hook on screen in the first 3 s, strong movement in the middle, a pause right before the biggest moment, and the agent checks its own plan against those rules before building. video-director adds: text big enough to read on a phone, nothing flashes, loudness within range, every factual claim checked, then a separate reviewer agent that never saw the build scores it, up to three rounds. Build: this is Phase 1's lint pass extended with (a) a plan-stage check on the EDL before any render, (b) a render-stage check (ffprobe tags, smooth_check, loudnorm print, minimum text height), and (c) a fresh-context review pass that only sees the MP4 and the beat sheet.

**H4. Critique thresholds from real reviewers (CONFIRMS our 3 s and 4 s rules).** Karima's notes on Claude's first draft (2026-11-07): "the pacing in the first 5 seconds still feels too slow", "the headline text in the top card is sitting too small", "it stays on my face for 4 seconds straight without enough motion". Second draft: "the main typography is too small in the center" and "the glass cards enter a little too slowly so the visual energy drags behind the voice over". Translation: element entrances must land on or before the spoken word, never after it; and when in doubt the title is too small.

### 2.2 Captions and typography

**T1. Composed "cinematic line" for payoff and quote beats (NEW layout logic).** Joseph's breakdown of the Arthur Brooks minimal style, 2026-10-31. The line is five words or fewer. Pick the one or two most important words, set them large and bold (sans bold or serif italic) in the center, then place the remaining words at a smaller scale in the gaps above and below. Two fonts only: a clean sans (Inter in his case) plus a serif italic (Playfair Italic) for the special words. White plus one accent. Why: it reads as a designed title instead of a subtitle, and the eye lands on the keyword first. Build (Remotion component `cinemaLine`): keyword at 104 px Oswald Bold or 110 px Instrument Serif Italic in tan, support words at 44 px Montserrat SemiBold off-white, keyword centered at (540, 820), support words offset to y 740 and y 900 with x nudged toward the free side; 140 ms pop on the keyword, 90 ms fade on the support words, all eased. Use it once or twice per reel (payoff, end line), never for running dialogue.

**T2. Make every element 25 percent smaller, and dull the colors (NEW taste rule, with a caveat).** Joseph, 2026-10-11 (the content of the demo edit, which he endorses as his own rules): "huge icons and huge shape layers scream beginner, make every element 25 percent smaller"; "the less you use an effect the more special it is"; "harsh blacks, harsh whites and bright reds read beginner; dull blues and greens read high-end." Caveat: Karima's reviewer flagged text as too small twice in the same month, so the rule applies to icons, cards, pills and shapes, not to the caption body. Build: in the Remotion kit, default card and icon scale 0.75 of whatever looks right in the first draft; backgrounds #111111 not #000000; caption white #F2F2F2 (already our hook off-white, extend it to body captions); oxblood stays flat and desaturated (consistent with the no-sheen rule).

**T3. Dim-and-blur the plate behind any UI card (NEW).** Joseph's on-screen animation rule: "the background behind it darkens and blurs, and the animation sits in the lower half of the screen." Build (ffmpeg): `split[a][b];[b]gblur=sigma=18,eq=brightness=-0.18[bl];[a][bl]overlay=enable='between(t,S,E)'` behind the card, or in Remotion a `backdrop-filter: blur(18px) brightness(0.8)` layer under the card, both faded in over 120 ms. For talking heads the card sits in y 1000 to 1500 and the face stays sharp above it.

**T4. Text that stays alive while it holds: tracking drift (NEW).** theRichy, 2026-10-07, all eight animations end with the same move: a tracking keyframe from 0 at the first frame of the line to +6 or +7 at the last frame of the hold, plus motion blur. Why: a static title dies after a second; a 1 to 2 percent letter-spacing creep is invisible as motion but keeps the text from feeling frozen. Build: Remotion `letterSpacing: interpolate(frame, [0, holdFrames], [0, 0.06em])`; in libass there is no animated spacing, so use `\fscx100` to `\fscx102` over the hold with `\t` as the stand-in.

**T5. Eight text-in recipes with exact values (NEW values, ported from After Effects text animators).** theRichy. Rendered in Remotion per word or per character:
- Fade words with ease: opacity 0 to 100 per word, ease high 40 / ease low 40, plus a soft glow and drop shadow (our two-layer shadow already does the shadow; add a 6 px, 25 percent glow in the accent color only on the hook card).
- Random-order character reveal: opacity 0 to 100, randomize order, ease low 100, start 0 to 100 over 8 to 12 frames; out = the same reversed.
- Typewriter with slide: characters type in while the whole line slides 30 to 40 px from the left, eased; the out is the in reversed in time.
- Word rise with blur: per word, blur 5 px to 0, opacity 0 to 100, y +40 px to 0, ramp-up shape, ease low 100 / ease high 10, motion blur on. This is the closest match to the playbook's "120 to 160 ms eased pop" and is the default to port.
- Scale-up scatter: scale 0 to 100 and y -50 to 0, random order seed 30, ease low 50.
- Rotate-and-bounce: rotation +45 to 0, scale 0 to 100, tracking -105 to 0, random seed 59, then a Y bounce of +20, -22, +8, -8, 0 at 10 to 13 frame spacing, all eased. Use once per reel at most (comedic beat).
- Close-to-open: tracking -43 to 0 (letters start stacked), opacity 0 to 100, y +50 to 0, ease high -50.
- Rotate rise: rotation +45 to 0, y +40 to 0, opacity 0 to 100, random seed 15, ease low 100.
- His general warning, repeated three times: keyframes too close together look cheap; leave 8 to 12 frames between in and settle, and turn motion blur on for anything that moves more than 20 px.

**T6. Caption line-break QA (NEW lint).** Thomas Creates, 2026-11-03, the only useful minute of a Vizard ad: a caption group ended on "in the" with "summer heat" alone in the next group; the fix was to merge so the group starts when its first word is spoken. Rule: a group may not end on an article, preposition or conjunction, and a group may not consist of fewer than two words unless it is the accent word by itself. Build: a 20-word stoplist in the caption grouper; if the last word of a group is on the list, pull the next word in or push this word to the next group.

**T7. The "viral clipper" caption look is a different product, not a competitor (CONTEXT).** Vizard's presets (two lines, all caps, Montserrat Black or Inter Black 16 to 17, thick black outline, keywords auto-colored red, blue and lime, emojis inserted) and Filmora's Dynamic Captions (glow and highlight templates, a shadow PNG blob dropped under the caption layer) are the mass look of October 2026. Joseph's premium style and our rules (one accent, no stroke, mixed case, soft shadow) sit on the other side of the same split. Keep ours. The one Filmora idea worth keeping is the shadow blob: our geq bottom gradient at 45 percent already does it.

**T8. Overlay taxonomy to borrow names and behaviors from (NEW, two items worth building).** Letta Edit's 70-preset podcast kit for Resolve (2026-10-20): vertical layouts (stacked two cam, split reaction, top cam plus caption space), name plates (pill, underline, name box, speaker-switch highlight), quote cards (pull quote, quote highlight, hot take, stat quote, quote typewriter), badges (clip hook header pinned at the top of a clip, timestamp bug, topic ticker), episode cards (chapter topic, coming up). Every title has the same in and out animation, a light glass or dark theme, and a drop shadow. Two we do not have: `hookHeader` (the hook line pinned in the top safe band for the whole clip, 44 px Oswald Medium caps on a 60 percent dark glass strip, used when the hook is a question the whole reel answers) and `statCard` (one number large, unit and context small, for price and count reels).

### 2.3 Motion and transitions

**M1. Speed-ramp curve logic, stated as two controls (CONFIRMS, with one new step).** AM Film, 2026-10-12: on a time-remap curve the vertical handle is speed and the horizontal handle is how gradually that speed is reached; pull handles far horizontally for a smooth ramp, short handles snap. Stabilize first (track one feature, scale up to hide borders), then the new step: move the tracked feature to the exact center of the frame before ramping so the eye has an anchor through the speed change. Motion blur and frame blending are mandatory on every ramp. Build: our ramp block already does minterpolate plus tmix; add `anchor: "auto"` which runs the YOLO or vidstab track and recenters the crop on the tracked point for the ramped shot.

**M2. Graphics straddle the cut (NEW rule).** Matt Loui, 2026-10-23, fixing Claude's CapCut timeline: "we see a jump cut and then the motion graphic kicks in, which just isn't professional", so he slid the graphic earlier to cover the cut. Rule: any card, tag or PiP that appears within 10 frames after a jump cut starts 4 to 6 frames before the cut instead, so the cut lands inside the motion. Build: in the EDL compiler, if `graphic.start - cut.time < 10 frames`, set `graphic.start = cut.time - 5 frames`.

**M3. Readability floor for on-screen words (DERIVED from Zane Hoyer, 2026-11-03).** His first drafts failed because "it was rushing too fast so I couldn't read any of the words" and phrases repeated where not needed; the fix was "slow down, smooth camera movement, readability". Floor: hold = 0.3 s per word + 0.6 s, minimum 1.0 s for any text block that is not a karaoke caption; no phrase may appear twice in a reel unless it is the hook called back at the end. Lint it.

**M4. Edits app speed curves for phone finishing (NEW platform fact).** Creator Swift, 2026-10-28 (Hindi) and Social Media Today, 2026-11-12: Edits now has Speed > Curve with presets and a Custom editor; add a point between each pair, pull points down for slow and up for fast, alternate for slow-fast-slow, leave the first and last points at normal. The same update added audio auto-adjust and text animation duration controls. For us: when Jacob finishes on the phone, the slow-fast beat can be done in Edits rather than CapCut, and our render should ship the ramped shot at constant speed with `rampable: true` metadata so the ramp can be redone in-app without double interpolation.

**M5. Glow title = duplicate and blur the bottom copy (CONFIRMS our two-layer text, new variant).** socialcontentking, 2026-11-07. Build: second ASS layer or Remotion layer, same text in the accent color, blur 16 to 22 px, 50 to 60 percent opacity, zero offset. Hook card only, and only on dark plates.

**M6. Natural push-in tied to the voice (DERIVED).** Karima on the human editor's edge over Claude: "the camera pushes in naturally with my voice." Our eased 1.00 to 1.08 punch is time-based; drive it from the voice instead: librosa RMS per frame, smooth over 12 frames, map the top 20 percent of loudness in each sentence to a 1.02 to 1.04 micro-push and the sentence end to a settle. One continuous eased curve, never steps.

**M7. Subtle pendulum on stills (NEW, from CapCut's "play pendulum" effect that Matt Loui applies over whole timelines of generated images, 2026-11-13).** ffmpeg: `rotate='0.006*sin(2*PI*t/6)':ow=iw:oh=ih:c=none,scale=1.03*iw:-2,crop=1080:1920` on any still or screenshot longer than 2 s. Keeps a still from reading as a freeze. Not for footage.

### 2.4 Sound

**S1. The 16-file starter SFX kit and its three families (NEW spec).** Joseph, 2026-10-11: five whooshes (long, short, textured), two or three mechanical clicks (short, metallic, retro), two or three sci-fi hits (impact, click, shot), two or three UI sounds (click, success, fail), two risers (bass, metallic), two hits (bass, heavy). The mapping: whooshes for movement, textures (clicks, pops, UI) for things appearing, risers and hits for build and drop. His edit-to-sound pairings: clicks on text appearing, a highlighter sweep on graphs, whooshes on transitions, song at -20 dB under the voice. Our sound lane has the timing rules and sources; it does not have the kit spec or the "clicks on text" pairing. Build: `VIDEO/tools/sfx/` with those 16 slots named by family, picked from Pixabay, Mixkit, Freesound CC0 and Soundly Free, gritty mechanical versions for El Coyote (no clean UI dings on footage; UI sounds only inside the `params` and `grid` components).

**S2. Sound-to-frame alignment sheet as a QA step (NEW tool idea, from earshot, AI Labs 2026-11-02).** The agent cannot hear, so earshot describes each sound and lines it up against frames so the agent can see whether a hit lands on a cut. Our version without installing anything: `librosa.onset.onset_detect` on the SFX stem, compare to the cut list from `smooth_check.py`, assert every whoosh peak is within 2 frames of its cut and every impact is on the exact frame of its text hit; print a table. Add to the lint pass.

**S3. Music written first, picture cut to it (CONFIRMS).** hashu-motion writes the music, then cuts the video to its beat so "every time something lands on screen there's a sound right on it". Same as our librosa beat grid; the new part is doing it before the visual build, not after.

**S4. Change the music when the mood changes (NEW for longer reels).** GrowthalgoYT, 2026-10-21: the same track at the same energy for the whole video gets tuned out; switch or re-level the music at the major turn. For a 30 to 45 s build reel, the contrast beat is the place: duck the song 6 dB and swap to the second section of the same track or to the ambience bed alone.

**S5. Transition SFX on every transition (CONTRADICTION, keep ours).** GrowthalgoYT puts a whoosh or click on every transition, but he also says transitions only happen on topic changes, which in a 20 s reel is one or two. Net effect matches our one-in-four cap.

### 2.5 Color

**C1. Node order and separation (NEW discipline for the ffmpeg grade chain).** Mehran Hadad, 2026-10-11. Exposure and contrast are two decisions and two nodes; balance white before shaping contrast; saturation is not one slider (use the saturation channel's gamma to lift mid-saturated colors without pushing the strongest ones); fix a single hue with a targeted tool instead of re-shaping the whole image; and if a print LUT is part of the final look, grade with it switched on rather than dropping it on at the end. Build: our chain becomes tone map, white balance (`colorchannelmixer` or `colorbalance` only for gray-card correction, never for warmth), exposure (`curves` master lift), contrast (`curves` S), per-hue fix if any (`hue` with a `selectivecolor` mask), saturation 0.92 to 0.95, then the 2383 blend; and render the preview with the LUT on from the first pass.

**C2. The Cineon trap (CONFIRMS yesterday's color lane).** Resolve's bundled Kodak 2383 expects Cineon log in, not Rec.709 gamma 2.4, so it crushes and oversaturates when applied to finished video; convert first. The color lane already flagged this and picked the Luttie 2383 specifically because it expects Rec.709. No change, but keep the note next to the lut3d line in build_reel2.py so nobody swaps LUTs casually.

**C3. Dull colors read expensive (CONFIRMS density rule).** Joseph's demo edit: luxury brands use dull blues and greens; bright red, pure black and pure white read beginner. Already in the playbook as "density reads expensive"; the actionable addition is T2 above (off-black backgrounds, off-white caption body).

**C4. iPhone 18 Pro settings (CONFIRMS with two additions).** Think Media, 2026-10-21: 4K, 24 or 30 fps for talking heads and 60 or 120 only for slow-mo, HDR Video off (editing apps mishandle it), Lock Camera on, Lock White Balance on, 1x lens for people (2x is a crop of the 1x), shutter at double the frame rate (1/60 at 30 fps), daylight 5600 K. New vs our brief: Enhanced Stabilization on (small crop, big gain handheld), and on the 18 Pro the main camera has a physical aperture (f/1.48, 1.8, 2.8, 4; f/4 starbursts on point lights) plus native shutter control, so an ND is only needed outdoors at 60 fps. Jacob's phone model is not on file; if it is an 18 Pro, add aperture f/2.8 and shutter 1/60 to the brief.

**C5. CapCut "adjustment layer with saturation, contrast and lower shadows" (CONTRADICTION, keep ours).** Matt Loui's default prompt to Claude for every CapCut edit. That is the look Jacob called crap on 2026-11-20. Our restraint rule stands.

### 2.6 Pacing

**P1. Word-level silence cut with 20 to 30 ms padding (NEW value).** Joseph, both videos: "create a word level transcript, remove every silence and every bad take, keep the padding around 20 milliseconds" (30 ms in the second video). His result: 76 s of raw to 50 s. Stockton Walbeck's "sift" does the same with dB-level dead-space detection, breath detection, retake detection and J and L cuts to hide the joins (6:24 of raw to 1:16). Our rule trims silences over 0.35 s and J-cuts every join; it does not state the padding. Set padding to 30 ms on the leading side and 60 ms on the trailing side (consonant tails).

**P2. Cut on transcript AND waveform (NEW rule).** Matt Wolfe, 2026-11-04: "when editing and doing initial cuts, use both the transcripts and the waveforms, because sometimes it'll read the transcript and cut you off mid-word." Build: after whisper word boundaries, snap each cut to the nearest RMS trough (window 80 ms, threshold -35 dBFS, 60 ms hangover) rather than the timestamp itself.

**P3. Announce on the face, describe with a visual (NEW talking-head cadence).** Joseph's Arthur edit plan: every time the speaker names a new item, stay on A-roll with captions; every time he describes it, cut to the visual (graph, b-roll, card); return to the face before the next item. It produces an A, B, A, B rhythm with no two full-screen graphics back to back. Our template C (talking head with b-roll) says cut to the noun within 0.3 s; add the alternation rule and the "face before each new item" rule.

**P4. Four scene types per line (NEW planning vocabulary).** Joseph's planning page: for every script line pick captions only, captions plus a small UI in the lower half, half-screen (graphic top, face bottom), or full-screen graphic. He chooses by content psychology: full screens on the big claims, half screens on examples, captions only on transitions between points. Stockton's short-form layout library overlaps: split screen (face bottom, thing top, captions between), three items popping above the head, blurred A-roll with words over it, full-screen b-roll. Build: add `scene: caption | captionUi | half | full` to each EDL line so the storyboard artboard shows the cadence at a glance; add `trio` (three items above the head) and `blurWords` (blurred plate plus composed line) to the Remotion kit.

**P5. First draft is 60 to 70 percent; plan a revision pass (CONFIRMS Phase 4, adds a checklist).** Joseph's six revisions on a 30 s edit: text design in scene 1, a rough cut between two animations, a texture that did not move with its animation, a bad cut at second 24, a graphic held too short, missing quotation marks. Karima's: too slow in the first 5 s, title too small, face held 4 s, cards entering late. Stockton: "no edit is perfect on round one, ever." Our revision checklist: hook speed, title size, longest static hold, every graphic entrance vs its word, every cut that a graphic should be covering, texture or grain that does not move with the element it sits on.

**P6. Motion plates as a unit of work (CONFIRMS our architecture, new name).** Ali Abdaal's team (skimmed): the A-cut is one stream; "motion plates" are 3 to 8 s self-contained motion graphics compositions built against real UI or stills and dropped into the timeline as b-roll; Remotion renders reached "97 percent there" after iteration. That is our plate factory plus Remotion tier. Adopt the name: a `plate` in the EDL is a 3 to 8 s Remotion comp with its own SFX.

**P7. Endings that do not announce themselves (CONFIRMS).** GrowthalgoYT: "that's it for today" is where viewers leave; point to the next related problem instead. Same as our no-outro and send-ending rules.

### 2.7 B-roll and overlays

**B1. Treat b-roll under text: vignette plus edge blur (NEW).** Joseph on Arthur's b-roll scenes: a light paper texture, darkened edges, slightly blurred edges "so the viewer focuses on the main focal point", then the composed line on top. Skip the paper texture (wrong brand); keep the edge treatment. ffmpeg: `split[a][b];[b]gblur=sigma=6[blur];[a][blur]maskedmerge=... ` with a radial gradient mask (`geq` or a pre-rendered PNG, center clear, edges white at 70 percent), then `vignette=PI/5`. Only on b-roll that carries text, never on the hero shot.

**B2. Line graph with camera follow (NEW component).** Arthur's "graph and statistics scenes": flat dark textured background, thin glowing grid, a ball riding the line while the camera tracks it. For price and count reels ("what the parts cost by month") build `lineGraph` in Remotion: grid 1 px at 12 percent white, line in tan, a 14 px dot at the head, camera x follows the dot with a 10-frame lag, the value counter next to the dot.

**B3. Spotlight the part being talked about (NEW).** argo and video-director (AI Labs) darken everything except the UI element the voice is naming. For us: when Jacob names a part on the engine, darken the plate 50 percent outside an ellipse around the part for the duration of the noun plus 0.6 s. ffmpeg: `geq` ellipse mask into `maskedmerge` with `eq=brightness=-0.3` copy; Remotion: radial-gradient overlay keyed to the words.json time of the noun. Pair it with the existing `tooltag`.

**B4. Hook header and stat card (see T8).**

**B5. B-roll density in top-performing shorts (CONTEXT).** Matt Wolfe's skill, after Claude analyzed his top shorts, wrote down "50/50 split with B-roll on top, captions, B-roll changing every 1.x seconds". That is a faceless-clipper cadence; our median shot of 1.8 to 2.5 s stays, but for the semi-side "what I order most" list reels, a 1.2 to 1.5 s b-roll cadence over a continuous voice line is the right exception.

### 2.8 AI tools

**A1. Claude Motion (NEW, context).** Beta since 2026-10-08, Team and Enterprise plans only as of 10-14 (Tristen O'Brien). It writes code, not pixels; every word, timing and color is editable in a Tweaks panel; a comment pin on any element triggers a scoped rebuild; export is GIF or MP4 with resolution, fps and quality options; usage counts against the plan. Not available on Pro or Max. Tristen, Joseph and AI Labs all name Claude Code plus Remotion as the equivalent ("Claude is the brain and Remotion is the hands"). Our toolchain decision from yesterday stands and now has three independent confirmations. hashu-motion is an open clone with director rules, three design directions written to a file for review, a timeline dashboard with comments, and music-first beat cutting; worth reading its skill.md for the lint rules, not worth adopting as a stack.

**A2. How to train a style skill properly (NEW method, the most valuable thing this month).** Joseph, 2026-10-31. Download 20 of the best reels in the target style; watch each and ask why for every scene; screenshot ~130 scenes onto a Figma board; sort them into the style's principles (he found 10); then give Claude the 20 videos and the board with a prompt that asks for a word-by-word transcript and frame-by-frame breakdown of each video to learn three things: where animations sit relative to the script, how each design is composed, and the animation logic (durations, feel); have it save the result as a skill with a reference folder per animation (225 of them) and a keyframe sheet. Second stage: a visual guide (captions; animations in four classes: text-, person-, object- and graphic-centric; the three-object rule: main object center, supporting elements at the edges, depth elements outside) and a separate sound guide plus library, each turned into a skill. Third stage per edit: a planning page with the script on one side and recommended scenes on the other, which the human fills in before anything is built. For us: do exactly this for the El Coyote look using `research/reel-references/` (the Chandler study was a one-reel version of it), with the 10 principles replaced by our house rules, and make the storyboard artboard the planning page.

**A3. Learn from Jacob's finishing (NEW loop).** Matt Loui's trick: after he tweaks the timeline by hand, he closes the project and asks Claude to re-analyze it, note every change, and update the skill. We already download the posted reel for VMAF; extend that to a diff: cut list, caption text and timing, music placement and level, anything Jacob changed in CapCut or Edits, logged to `research/2026-11-20-reels-made.md` and folded into the house rules when a change repeats.

**A4. Reference-driven prompting beats prompt-driven prompting (CONFIRMS, with numbers).** Zane Hoyer spends 20 to 60 minutes on Pinterest per edit collecting references before prompting; Karima says weak references give generic results and "the prompt is 90 percent of the work"; Joseph's whole method is references first. Our reel-references folder is the right instinct; the gap is volume. Target 20 reference reels per format, not two.

**A5. Reanimate-style timing copy (NEW tool idea).** reanimate (AI Labs) records a reference animation frame by frame, writes down when each part starts and how fast it moves, rebuilds it, then records its own copy and compares until they match (two to five rounds). For a reference reel we love, PySceneDetect plus per-frame motion energy gives us the cut times and the energy curve; a Remotion plate can then be checked against that curve numerically instead of by eye.

**A6. Things seen everywhere this month that we still do not do.** AI-generated b-roll through Higgsfield MCP (Karima, Matt Loui, Tristen, all sponsored by Higgsfield); CapCut draft-file automation (Matt Loui, twice, now also with ChatGPT and Codex). Both stay closed: no AI b-roll is a brand rule and CapCut draft automation breaks on updates and violates the terms. The code-built graphic (Remotion plate) is the agreed middle ground in every one of these videos.

**A7. Cost and time benchmarks for the record.** Joseph: 1 min reel, 110 min wall time, 20 min human time, about 10 percent of a Max plan's weekly usage, 24 of those minutes were Claude cutting silences (he recommends doing the cut with a dedicated tool instead); 30 s Arthur-style edit, 2 h wall, 15 min planning. Karima: 50 min vs a human editor's 5.5 h. Stockton: simple edit 30 min, retention-max edit 2 to 4 h. Our Remotion benchmark (5 s in 24 s wall) is consistent with those.

## 3. Contradictions with the playbook

1. **Caption style.** The mass look (Vizard, Filmora, FCP Magic Mode): two lines, all caps, black-outlined heavy sans, three highlight colors, emojis. Playbook: one accent, no stroke, mixed case, soft shadow. Keep the playbook; Joseph's premium breakdown lands on our side (one sans, one serif italic, one accent, no stroke).
2. **Transition sound on every cut** (GrowthalgoYT) vs our one-in-four cap. Keep the cap; his premise (transitions only at topic changes) makes the two equivalent in practice.
3. **"Saturation up, contrast up, shadows down" adjustment layer** (Matt Loui's default CapCut prompt) vs our restraint grade. Keep ours; this is the exact look that got rejected on 2026-11-20.
4. **AI b-roll as standard** (every Higgsfield-sponsored video) vs no AI b-roll. Keep ours.
5. **Text size.** Joseph's "25 percent smaller" vs Karima's reviewer twice saying "too small". Resolution: shrink shapes, cards and icons; never shrink the caption body or the hook card below the playbook sizes; add a minimum of 40 px for any text at 1080 x 1920.
6. **Padding.** Joseph's 20 to 30 ms word padding is tighter than most editors use; our tests should start at 30 ms lead and 60 ms tail and listen for clipped consonants before going tighter.
7. **Silence cutting speed.** Joseph says doing the silence cut inside Claude took 24 minutes for one minute of video and recommends a dedicated tool. We already planned auto-editor for the silence map; this is the reason to keep it in ffmpeg or auto-editor rather than inside the agent loop.
8. **Claude Motion.** It is not a contradiction but a check: it is Team and Enterprise only, so there is no case for moving off Remotion; three creators independently point Pro and Max users to Remotion.
9. **Music level.** Joseph places the song at -20 dB relative; our rule is "song added in app at 20 to 30 under talking". Same range; no change.
10. **LUT input space.** Mehran's Cineon warning matches the color lane's reason for choosing the Luttie Rec.709 LUT; no change, keep the note.

## 4. What to add to the house rules

Structure and pacing
- Silence cut padding: 30 ms lead, 60 ms tail, cut points snapped to the nearest RMS trough, never to the raw transcript timestamp (P1, P2).
- Talking head cadence: announce on the face, describe with a visual, face again before each new item; no two full-screen graphics back to back (P3).
- Every EDL line carries a scene type: caption, captionUi, half, full (P4).
- Readability floor for non-karaoke text: 0.3 s per word + 0.6 s, minimum 1.0 s; no repeated phrase except a hook callback (M3).
- Graphics straddle cuts: anything appearing within 10 frames after a jump cut starts 5 frames before it (M2).
- Revision pass is mandatory and uses the six-point checklist in P5.

Hooks
- Add the five audio hooks (sound-first, mid-sentence start, silence drop inside the first 3 s, room change, off-screen voice) to the 18 templates; mid-sentence start and sound-first are editable from words.json today (H1).
- The hook card accent is the curiosity word, declared explicitly in the EDL (H2).

Typography
- New components: `cinemaLine` (composed payoff line), `hookHeader`, `statCard`, `trio`, `blurWords`, `lineGraph` (T1, T8, P4, B2).
- Caption body color moves to #F2F2F2; card and background blacks to #111111; cards, pills and icons default to 0.75 of first-draft size; text never below 40 px (T2).
- Tracking drift of +6 percent over any hold longer than 1 s; motion blur on any element moving more than 20 px; 8 to 12 frames between in and settle (T4, T5).
- Word-rise-with-blur (blur 5 to 0, y +40 to 0, opacity 0 to 100, 4 to 5 frames) becomes the default caption pop in the Remotion tier (T5).
- Caption grouper stoplist: no group ends on an article, preposition or conjunction; no one-word group except the accent word (T6).
- Dim and blur the plate under any UI card (T3). Glow title variant allowed on dark plates only (M5).

Motion
- Ramped shots get `anchor: auto`: track the subject and recenter the crop before the ramp (M1).
- Voice-driven micro push-in (1.02 to 1.04 on the loud 20 percent of each sentence) replaces the time-based punch on talking heads (M6, test first).
- Pendulum drift on any still over 2 s (M7).
- Ship ramp-candidate shots at constant speed with `rampable: true` so the slow-fast beat can be redone in Edits' new speed curves without double interpolation (M4).

Sound
- Build the 16-slot SFX kit by family (five whoosh, three click, three sci-fi, three UI, two riser, two hit), gritty mechanical variants; clicks on text appearing, sweep on graphs, whoosh on transitions (S1).
- Alignment QA: every whoosh peak within 2 frames of its cut, every impact on the exact frame of its hit; printed as a table in the lint pass (S2).
- Music change or 6 dB re-level at the contrast beat on reels over 30 s (S4).

Color and camera
- Grade chain order: tone map, balance, exposure, contrast, per-hue fix, saturation, LUT blend; preview with the LUT on from pass one (C1).
- Shooting brief: Enhanced Stabilization on; if the phone is an 18 Pro, aperture f/2.8 and shutter 1/60 at 30 fps in the native app (C4).

Tooling and process
- Build the El Coyote style skill the Joseph way: 20 reference reels, a screenshot board sorted by our house principles, frame-by-frame breakdown, per-animation reference folders, planning page per edit (A2).
- Post-publish diff of Jacob's finished reel against our master, logged and folded into the rules when a change repeats (A3).
- Lint grows a plan-stage check (before render) and a fresh-context review pass (after render) in the spirit of video-director (H3).
- Claude Motion: not available on our plan, Remotion stays; read hashu-motion's skill.md for its director rules (A1).

## 5. Transcript files written this session

`research/transcripts/2026-11-21-INDEX.txt` lists all 22 files with title, channel, date, views and URL. The three skimmed videos (Ali Abdaal, Matt Wolfe, Usman Explains) were not saved; their useful lines are quoted in sections 2.6, 2.7 and 2.8.
