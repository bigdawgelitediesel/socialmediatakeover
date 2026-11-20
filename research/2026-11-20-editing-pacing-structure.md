# Editing pacing, rhythm and structure for @elcoyotediesel reels (2026-11-20)

Research agent report, lane: PACING / RHYTHM / STRUCTURE. Sources: nine YouTube transcripts (craft and capcut lanes) plus web research dated today. Written as rules Claude can encode in the build_reel2.py edit-list generator. Plain text, no em-dashes.

Diagnosis of the first cut (harley-trade.json, 18.8 s, 8 slots at 2.6 / 1.8 / 1.8 / 1.2 / 1.4 / 3.8 / 3.0 / 3.2 s, one 0.3 s fade): the shot lengths are already in the professional range (median 1.8 s, nothing over 4 s). That is why Jacob said "the flow is great." What is missing is what rides on top of a clean rhythm: cuts landing on action or on an audio hit, a J-cut lead into the dialogue, a held beat before the punchline, one deliberate contrast moment, and an ending that loops. Those separate a correct cut from a pro cut.

## 1. Findings

### From the transcripts

Tim Runia (https://www.youtube.com/watch?v=dhpazqW_OaU). Lock audio first: voice, music and key SFX before any picture, because pacing faults show in audio instantly. Three pacing levers: shot length (short = tension, long = emotion), shot motion (handheld = energy, stable = calm), and sound (driving beat pushes, soft lets it breathe, silence is a weapon). The biggest mistake he sees in experienced editors is staying at one pace too long; his own 30 s hook goes no-music tension, pause, fast cuts, one long breathing shot, fast again, release into silence. Flow beyond cutting on the beat: cut intentionally (carry motion direction and eye position across the cut), beat accents (land the ACTION on the beat, not the cut), audio transitions (one SFX bridging two shots). Break your own rhythm once per edit with a freeze, a sudden silence, or an unexpected cut. Assembly edit first, then refine. Kill shots that do not serve the story.

Herman Huang (https://www.youtube.com/watch?v=Zm7J3KqqXPk). Method: watch the genre until the pattern shows, bookmark the best, go frame by frame on pacing, framing, movement, graphics, SFX and music to learn why each decision was made. Differentiate by importing taste from another genre into the standard blocks. For us: the standard blocks of build reels are jump cuts, word captions and numbered lists; the imported taste is cinematic b-roll pacing plus shop humor.

Joseph (https://www.youtube.com/watch?v=jAvNgpcdD5k). Stage one of every edit: remove silences and bad takes, then make every dialogue join a J-cut (next clip's audio starts before its picture). Subtitles in the lower third, eyes in the upper third. Every zoom gets a whoosh aligned peak to peak, text pops get clicks, risers before reveals. Zoom pattern: fast in, slow out.

Chriss Boustedt (https://www.youtube.com/watch?v=wyKHkM0MXFg). Zero gap between caption blocks. Text eases in from 25 to 30 percent opacity with bezier velocity, never linear. A slow camera push on the hook section only.

Matt Loui (https://www.youtube.com/watch?v=pkyDzEHpZao). Auto remove pauses from the transcript, hide the jump cuts with a slight scale-up on the second clip while keeping the eye line on the same horizontal guide. Smooth zooms to about 118 percent with cubic ease; closer keyframes = faster. Beats 1 / Beats 2 marks the song's beat points for lining up cuts. Optical flow for slow motion under 0.5x. Motion blur on anything animated. Freeze frame as a pattern break.

Zeven 7 (https://www.youtube.com/watch?v=fKNDlT5JbTY, https://www.youtube.com/watch?v=MJHpo7pOaLg). Motion speed is keyframe distance; cubic out for arrivals, ease in-out for pushes. A scene-level push from 100 to 120 or 130 percent over 1 to 3 s reads as camera movement.

Justin Brown and Metics (https://www.youtube.com/watch?v=DtoXtnyA-GQ, https://www.youtube.com/watch?v=j5_471mO14c). Keep text and subject out of the right button column and bottom caption band; transitions are something you shorten to 0.5 s, not lengthen.

### From the web

Cut cadence. Every retention guide lands on a visual change every 2 to 4 s: 4 s with nothing new triggers the swipe, viral talking-head creators rarely pass 5 s, and small changes count (a 10 to 15 percent punch-in, a caption, a cut to the named object) (https://slidycreator.com/blog/video-pacing-retention/). Platform rates: Reels a cut every 2.5 to 4 s with audio hits driving peaks, TikTok 1.5 to 3 s; fast sections one cut per 1 to 2 s, slow sections one per 4 to 6 s; cut on the beat or one frame early (https://shortzly.com/blog/short-form-video-pacing-editing-guide). The AutoShot short-video dataset found most shots under 5 s (https://arxiv.org/pdf/2304.06116). A healthy curve holds 70 to 80 percent by second three and flattens; a steady slope means pacing, a cliff at 1 to 3 s means hook (Slidy).

Dialogue trimming. Remove pauses over roughly 0.3 s in short form but keep breaths that carry meaning (Slidy). Punch-in math: 110 percent hides a jump cut, 120 to 150 percent for 1 to 3 s lands a key word, no more than once every three or four cuts; voice about -6 dB, SFX -12, music -20 (https://evgenymaximov.com/blog/talking-head-video-editing/). Punch in on the line that deserves it, never at random (https://www.tiktok.com/@katiesteckly/video/7354004424777288965). Insert a brief b-roll shot between two jump cuts when the shots look identical or the speaker crosses the centre line (Shortzly).

Structure. Jenny Hoyos: hook, 3 s foreshadow, body connected by "but" and "therefore" (never "and then"), payoff, and "whatever you say you're gonna do, you end it right after you do it"; fast first 10 to 15 s, medium middle, deliberately slow right before the reveal; frame 1 is the thumbnail, the first words are the title; a short loops rather than ends (https://skills.lc/Farrice/mes-knowledge-base/farrice-mes-knowledge-base-skills-jenny-hoyos-shorts-skill-md, https://modedigitalmedia.com/videos/what-jenny-hoyos-s-shorts-playbook-says-about-hooks-rewatchability-and-platform-fit). Promise, progress, payoff: open on the result, show visible progress markers, pay the promise or the viewer does not trust the next one (https://www.overseeros.com/blog/youtube-retention-architecture-2026). Open 2 to 3 loops in 45 s, close the biggest in the last 5 s, re-hook near the midpoint (Slidy). Paddy Galloway: keep retention danger zones (transitions, ends of storylines, heavy context) as short as possible, cut repetition mercilessly (https://x.com/PaddyG96/status/1811083499044044951). Car content: setup, reveal, payoff, each beat about 2 s (https://www.car-editor.com/car-content-creation/). The payoff you cold-open on must be a payoff the video delivers (https://vanpelt.studio/learn/hooks/cold-open-dont-bury-the-payoff/).

Loops. Match the last frame's composition, motion direction and colour to frame one; carry audio across the seam; put the strongest beat on the seam; make the last sentence the grammatical first half of the hook; "closure kills loops" (logo card, thanks, on-screen CTA) (https://www.influencers-time.com/loop-optimized-reels-the-seamless-cut-that-boosts-rewatch-ra/, https://zeely.ai/blog/how-to-loop-a-video-on-instagram-in-2026/).

Silence and sound. A near-silent beat right before a punchline or reveal makes the next sound land harder; once or twice per clip (https://blog.redhub.ai/sound-design-for-video/). Showreel practice: 0.5 to 1 s of silence before the reveal cut, alternate one quick cut with one held reaction (https://magicians.top/short-form-showreels-that-land-editing-tips-from-film-market). Comic timing: hold after the punchline, do not rush past it; too long telegraphs it (https://jigreelstudios.com/comedy-demo-reel-timing-making-casting-directors-laugh/). Dead time (nothing new on screen or in audio) is the enemy, not silence.

Classical grounding. Murch's Rule of Six: emotion 51 percent, story 23, rhythm 10, eye trace 7; an emotionally right cut forgives small rhythm faults, never the reverse (https://www.studiobinder.com/blog/walter-murch-rule-of-six/). Pace is cumulative (cut rate + action in shot + subject distance + camera movement) and every pace change needs a narrative reason (https://www.insidetheedit.com/blog/pacing-in-video-editing). J and L cuts run a few frames to a couple of seconds (https://www.soundstripe.com/blogs/a-video-editors-guide-to-j-cuts-and-l-cuts).

Platform. Mosseri's Reels order: sends per reach, likes per reach, watch time (https://buffer.com/resources//instagram-algorithms/). Reels retention averages about 45 percent, with drop-off in the first 2 s and the last 10 percent (https://kinovela.com/insights/short-form-video-retention-benchmarks). Our data agrees: meme reels share, held build reels do not, so the edit must put a shareable line inside held footage.

## 2. Rule set to encode

Shot lengths by section (output seconds, 30 fps):
- Hook (0 to 3 s): first shot 1.5 to 2.6 s, motion visible in frame 1, text on by frame 4. Dialogue hooks start audio 0.2 to 0.4 s before picture.
- Body: median 1.8 to 2.5 s, range 1.0 to 3.5 s. No more than three consecutive shots under 1.5 s, no more than two over 3 s.
- Pre-payoff beat: one shot of 2.5 to 4 s, slower or slow-mo, music dipped. The deliberate slow-down before the reveal.
- Payoff: 2 to 3.5 s. Joke: no cut during the line, hold 0.6 to 1.2 s after it. Reveal: cut to it on a downbeat.
- Ending: last shot 2 to 3 s, built to loop.

Max hold without change: 3.0 s in the body, 4.0 s anywhere. A change is a cut, a punch step, a caption appearing, a speed change, or strong motion inside the frame. A static truck shot with nothing moving is dead at 2 s.

Cut type selection:
- Hard cut is the default, 85 to 90 percent of joins.
- Cut on action: pick in-points where something enters, leaves, drops, lifts or turns; carry motion direction across the cut.
- Dissolve (xfade 0.25 to 0.4 s) only for a time jump, the step into the pre-payoff beat, or the loop seam. Never between two shop shots of the same scene.
- Speed ramp (speed 0.5, minterpolate) on one or two moments per reel, the most physical action. Ramp in on a downbeat, back to 1x on the next.
- Punch-in (slow push 1.0 to 1.08, or a hard step 1.0 to 1.15) to hide a dialogue jump or land a key word. Alternate wide and punched on consecutive dialogue clips, eye line at the same y.
- Match cut when two clips share a shape or motion (round turbo to round wheel, hand reaching to hand reaching).
- Freeze frame or sudden silence: once per reel at most, as the pattern break.

Dialogue trimming:
- Remove silences over 0.35 s inside a run; keep one breath (0.15 to 0.3 s) before a punchline or a number.
- Keep "ums" only when they are the joke.
- Every dialogue join is a J-cut (audio leads 6 to 12 frames) or is covered by b-roll.
- B-roll over talking: cut to the named thing within 0.3 s of the word, hold 1.2 to 2.5 s, return on the next stressed word.
- Captions: word highlight, zero gap, lower third, 1 to 5 words per block.

Sound that drives picture:
- Pick the bed first, extract beats (or transients from the shop audio), snap cuts to beats or 1 frame early. Land actions on beats more than cuts.
- One SFX per movement: whoosh on punches and ramps, metal hit on hard reveals, riser into the payoff.
- Dip or kill music 0.5 to 1.0 s before the payoff line; bring it back on the payoff.

Ending:
- End within 1.5 s of the payoff. No outro, no logo, no spoken CTA.
- Last shot rhymes with the first (same subject, motion direction or framing), or the last line feeds the first. Audio carries across the seam, no fade to black.
- The share line goes in the last 3 s as text, not as a "share this" card.

## 3. Beat sheets for this account

A. One joke, real audio (the Harley Trade pattern, 15 to 22 s)
- 0.0 to 2.4: motion hook shot, the question on screen by frame 4 ("how much you pay for that truck?"), setup audio starts at 0.2 s (J-cut).
- 2.4 to 8.0: three or four b-roll shots over the setup dialogue, 1.2 to 2.0 s each, cuts on stressed words, one punch on the number or key noun.
- 8.0 to 10.5: pre-punchline beat, one slower shot, music out, room tone and breath kept.
- 10.5 to 13.0: punchline on the speaker or the reacting face, no cut during the line, hold 0.8 s after.
- 13.0 to 15.5: visual tag that pays the joke again (the empty space where the Harley was), slow push 1.0 to 1.08.
- 15.5 to 17.5: share line as text over the tag, last frame rhymes with frame 1. End.

B. Cinematic build progress (25 to 40 s, music bed, minimal voice)
- 0 to 2.5: result-first cold open, text names the stake with a number ("a 29-year-old engine in a 67-year-old truck").
- 2.5 to 4.0: rewind cue, one 0.3 s dissolve or a reversed shot, caption "3 weeks ago."
- 4 to 16: progress montage, 6 to 8 shots at 1.2 to 2.2 s, every cut on a downbeat, every third shot a macro, one speed ramp on the biggest action, captions as progress markers ("day 1," "block out").
- 16 to 20: midpoint re-hook, one line that opens a new loop ("then we found this"), cut to the problem.
- 20 to 27: second montage, faster, 0.8 to 1.6 s shots.
- 27 to 30: pre-payoff beat, 3 s slow-mo, music dips.
- 30 to 35: payoff, the thing the cold open promised, 2.5 to 3.5 s on the downbeat, SFX hit.
- 35 to 38: tag with the share line, last frame rhymes with frame 1. End.

C. Talking head with b-roll (20 to 35 s)
- 0 to 2: first sentence is the claim, no greeting, claim text on screen, 1.1 punch on the key word.
- 2 to 6: reason one, b-roll on the noun within 0.3 s, back to Jake on the next stressed word.
- 6 to 12: reason two, same pattern; alternate wide and 1.12 punched on every join; every join J-cut or covered.
- 12 to 14: pattern break, a freeze or a cut to silence on a face.
- 14 to 24: the story or the number, b-roll density highest, max 2.5 s on Jake without a change.
- 24 to 28: the line that answers the claim, on Jake, no cut, music dipped.
- 28 to 31: share line as text over one b-roll shot that echoes the opening. End.

## 4. IMPLEMENT IN OUR STACK

Inputs exist: watch.py gives scenes.csv (shot boundaries), words.json (word timestamps) and frame sheets; build_reel2.py takes slots with clip/in/dur/speed/zoom/stab/xfade/grade, audio beds and ASS captions. Add a generator between them.

Step 1, silence map (auto-editor 29.3.1 at Python312\Scripts\auto-editor.exe). Confirmed today on IMG_3784.MOV: `auto-editor <clip> --edit "audio:threshold=4%,stream=0" --margin 0.15s,0.25s --export v3 -o <clip>.v3 --no-open` writes a JSON timeline (frames at timebase 30/1, fields start/dur/offset) without rendering. iPhone MOVs MUST pin stream=0 or auto-editor fails with "Decoder not found" (track 2 is apple_apac). `--stats` prints the cut summary; `auto-editor levels <clip> --edit audio:stream=0` dumps the per-frame loudness envelope, the better input for a custom generator. At 4 percent the median kept run was 0.7 s (55 cuts in a 1 min clip), too choppy for conversation; use `--margin 0.3s,0.5s` for speech and merge kept segments closer than 0.35 s. Protect 0.3 s before any word Whisper marks as a number or that ends a sentence before a long gap (the punchline breath).

Step 2, picture cut candidates. Use scenes.csv boundaries plus a motion-energy score per 0.1 s (frame difference on 240p proxies, or ffmpeg `select='gt(scene,0.2)'`). Cut-on-action candidates are local maxima inside a shot; set in-points 4 to 8 frames before the peak so the action carries across the cut.

Step 3, audio transients and beats. Music beds: librosa `beat_track` for the grid plus `onset_detect` for off-grid hits; downbeats (every 4th) are the strong-cut set, all beats the allowed-cut set (https://librosa.org/doc/0.10.2/generated/librosa.beat.beat_track.html). Real shop audio with no music: `onset_detect` on the clip itself (clanks, air tools, steam) gives transients to land cuts and ramps on. Snap each planned cut to the nearest allowed beat within 0.15 s, biased 1 frame early. Dialogue cuts obey word timestamps, not beats.

Step 4, decision order per slot:
1. Section from the beat sheet (hook / body / pre-payoff / payoff / tag) sets the duration band and the change rule.
2. Dialogue slot: trim with the silence map, set `in` so audio leads picture by 8 frames, then cover: if the previous dialogue slot had the same framing, apply `zoom` step [1.0,1.12] with eye-line y preserved, or insert a 1.2 to 2.5 s b-roll slot at the noun's timestamp.
3. B-roll slot: in-point at a motion peak minus 6 frames, duration from the band, out-point snapped to the next allowed beat.
4. Treatment: no transition by default; `xfade fade 0.3` only into pre-payoff or at the loop seam; `speed 0.5` on the single highest motion-energy shot per montage block; `zoom` push [1.0,1.08] on any shot over 2.5 s so nothing sits still.
5. Constraints after assembly: max 3.0 s without a change event, max 3 consecutive slots under 1.5 s, max 2 over 3 s, one pattern break, a payoff hold, final frame rhymes with the first (same clip family or motion tag).
6. Emit SFX markers (whoosh at zooms and ramps, hit at the payoff cut, riser from pre-payoff to payoff) and a music-dip envelope from 0.8 s before the payoff line.

Step 5, lint before render. Print a table (slot, section, dur, change events, beat-snapped, J-cut) and refuse to render on any failed constraint. This is Runia's assembly edit, as data.

## 5. Prioritized top five

1. Beat sheet first, footage second. Pick template A, B or C, write the hook line, the payoff and the share line, lock the audio timeline, then assign picture. Every reel gets a named pre-payoff beat and a 0.6 to 1.2 s hold after the punchline.
2. J-cut every dialogue join and cover every jump with a punch-in or b-roll, eye line preserved. Trim silences over 0.35 s, keep the breath before the punchline.
3. Snap cuts and speed ramps to audio, beats of the bed or transients of the shop sound, one frame early; land actions on beats more than cuts.
4. One deliberate contrast per reel (silence, freeze, or slow-mo with the music out) right before the payoff; otherwise hard cuts only, dissolves reserved for time jumps and the loop seam.
5. End within 1.5 s of the payoff, share line as text in the last 3 s, last frame rhymes with the first, no card, no fade, so it loops.
