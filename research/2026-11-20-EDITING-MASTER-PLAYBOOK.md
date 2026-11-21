# El Coyote editing master playbook (synthesis of the 2026-11-20 ten-lane research)

> **Read next: `2026-11-21-PLAYBOOK-ADDENDUM.md`** (2026-11-21 session: sends rules, the menu-reel grammar, the tenfoldmarc effect vocabulary, shooting openers, sound kit, series bible, profile spec, handoff files, and the 24 new Remotion components). The addendum builds on this file; where the two disagree the addendum is newer.

Written 2026-11-20 after Jacob called the first Harley Trade cut "low level editing" (color off, lettering weak, flow fine). Ten research agents each took one lane; 42 YouTube tutorial transcripts (4.9M combined views) were pulled through Composio and read, plus roughly 300 web sources. Several findings were verified on this PC, not just read. The ten lane reports sit next to this file as `2026-11-20-editing-*.md`. This document is the operating manual; the lane reports are the evidence.

## 1. Why the first cut read as low level (root causes, in order of weight)

1. **Color was a bug, not a taste problem.** Every iPhone clip is 10-bit HLG BT.2020 with a Dolby Vision 8.4 record. The renderer squashed it to 8-bit with no tone map and left HDR tags on the SDR file. That produces a milky, hue-skewed image (measured: saturation at about 60 percent of correct, 11 percent of sky pixels blown) which a saturation grade turned into neon rust, and which Instagram then tone-mapped a second time. Three agents found this independently. FIXED in build_reel2.py the same day: per-clip HDR probe, libplacebo spline tone map to BT.709 (zscale + tonemap=mobius:desat=0 is the fallback chain), BT.709/tv tags on every encode. DJI clips are already SDR and pass through.
2. **The footage has no camera moves.** Every viral car-edit tutorial starts from one continuous, smooth move (push, orbit, reveal) and a 60 fps source. Static phone-on-a-shelf clips give a speed ramp nothing to ride. This is a shooting problem Claude cannot edit around; section 4 is the fix.
3. **Text was a default.** Thick 7 px outlines on ExtraBold, then a plain SemiBold, instead of the 2026 premium grammar: medium-bold geometric sans, tight tracking, no stroke, a soft blurred shadow on a second layer, one accent word in the brand color, 120 to 160 ms eased pops, zero gaps between groups.
4. **No motion grammar, no sound layer.** Hard cuts plus one dissolve and one slow-mo, with raw shop audio and digital silence under the DJI clips. Pros ease every move, land the knee of a speed curve on a beat, J-cut every dialogue join, and put a whoosh, riser or impact on roughly one cut in four.

## 2. The rules (what every El Coyote reel does)

### Structure and pacing (lane 1, lane 6)
- Beat sheet before footage. Three house templates: A "one joke, real audio" (15 to 22 s), B "cinematic build progress" (25 to 40 s), C "talking head with b-roll" (20 to 35 s). Full second-by-second sheets are in the pacing report.
- Hook 0 to 3 s: motion in frame 1, text on by frame 4 (0.13 s), 3 to 7 words, one question the frame cannot answer by itself, first pattern change by 1.0 to 1.5 s, first payoff by 4 to 5 s. Never a wide, never a logo, never "hey guys".
- Body: median shot 1.8 to 2.5 s, no visual unchanged longer than 3 s (4 s absolute), max three consecutive shots under 1.5 s, max two over 3 s. A change is a cut, a punch step, a caption appearing, a speed change or strong in-frame motion.
- One deliberate contrast beat before the payoff: 2.5 to 4 s, slower or slow-mo, music dipped, 0.5 to 1 s of near silence.
- Payoff: no cut during the line, hold 0.6 to 1.2 s after a joke. Payoff must beat the hook or the reel gets cut shorter.
- Re-hooks: 20 s reel at 9 s; 30 s reel at 10 and 19 s; 45 s at 10, 20, 32 s. Each is a new question, a number, a reveal or an angle change, never the same device twice in a row.
- Dialogue: trim silences over 0.35 s, keep the breath before a punchline, every join is a J-cut (audio leads 6 to 12 frames) or is covered by b-roll cut to the noun within 0.3 s of the word. Alternate wide and 1.12 punched on consecutive talking clips, eye line on the same y.
- Ending: within 1.5 s of the payoff, no outro, no card, no fade to black. Default for build reels is the send ending (recipient-framed line in the last 3 s plus the series tag); loop ending for memes under 10 s (last frame rhymes with frame 1). "Tag 3 friends" never.

### Hooks (lane 6)
Eighteen fill-in templates for this account are in the hooks report. The ones to lean on: quoted dialogue, price and number ("29 year old engine. 67 year old truck."), trade and sacrifice, nobody-tells-you, belief challenge (A vs B), callout, result-first, stakes and clock (SEMA countdown), story cold-open mid-motion, sound-first.

### Typography (lane 2, verified renders)
- Hook card: Oswald Bold 112 px caps, tracking +2, centered at (540,760), one word in Coyote tan, 120 ms fade, 140 ms pop from 94 percent, optional blur-in. Alternate: Montserrat ExtraBold 96 for questions.
- Dialogue caption: Montserrat SemiBold 66 px mixed case, tracking -1, no stroke, text bottom at y 1240, groups of 4 words or 28 characters, zero gaps, current word tan, pop only the first word of a group.
- Soft shadow is a second ASS layer (same text, black, blur 10 to 14, 50 percent alpha, offset 3/6 px). Blurring the text layer itself softens the glyph; never do that.
- Over bright footage, a blurred \p1 band or a geq bottom gradient at 45 percent black, never a stroke.
- Label and partner tag: Oswald Medium 40 tan caps with a 56x4 tan rule, left at x 72; or a tan pill (BorderStyle 3). End-card sign-off: Instrument Serif Italic 120 tan, the one serif beat.
- Static font files only (libass has no variable-font support). Fonts are now in VIDEO/tools/fonts.
- Avoid: Impact, Arial Black, Bahnschrift, Playfair for captions, neon fills, more than one accent, text below y 1500 or inside the right 130 px.
- Talking-head captions in the Remotion tier (added 2026-11-20 after the @chandlerintelligence study): plain white Poppins SemiBold 60 with a two-layer shadow, no pill, one to three words, y from the face tracker (1150 default), at most one word in a coral highlight box. His exact critique of the justyn pill: "I'd lose the green box though. Plain text with shadow looks way cleaner." `captionStyle: "plain"` in the props. The oxblood pill stays for loud comedic beats only.

### Color (lane 3, verified)
- Detect per clip: color_transfer arib-std-b67 or smpte2084 or bt2020 primaries means HDR, tone map first, before fps, crop, zoom, grade or captions.
- Grade is restraint: black point about 1 percent, highlight roll-off, saturation 0.92 to 0.95, a Rec.709 print LUT (Luttie Kodak 2383 or Portra 400) blended at 35 percent via split + lut3d + blend, fine temporal grain. No eq saturation boosts, no colorbalance warmth, no teal-orange. Density (saturated colors slightly darker) reads expensive; bright saturated reads cheap.
- Verify every render: ffprobe must say yuv420p bt709 bt709 bt709 tv.

### Sound (lane 4, verified chains)
- Dialogue first: highpass 90, afftdn (or arnndn with sh.rnnn, or DeepFilterNet3 for hero lines), deesser, 3:1 compression, limiter, voice stem to -16 LUFS.
- Never digital silence: record 30 s of shop room tone and 30 s of diesel idle, lay one under the whole reel at -26 to -30 dB under voice, duck it with sidechaincompress (threshold 0.05, ratio 4, attack 10, release 400).
- Three sounds on the right frames: whoosh starts 2 to 3 frames before a cut and peaks on it (one cut in four at most); impact on the exact frame of a hook text hit or reveal; riser 1 s ahead with a hard stop and 2 frames of silence before the hit. SFX 6 dB under voice. One SFX style per reel (gritty mechanical, not clean dings).
- Loudness -14 LUFS, true peak -1.5 after AAC. The song goes in inside Instagram (original 100, song 20 to 30 under talking, 100 on montage). Beat-match with librosa (installed) and finish exact dots in the Edits app if a song drives the cut.
- SFX sources: Pixabay, Mixkit, Freesound CC0, Soundly Free. Never CapCut's library for Instagram use.

### Motion (lane 5, verified graphs)
- Every move eased, never linear. Ease-in-out cubic for pushes, ease-out for hits.
- Eased punch-in on every static shot: 1.00 to 1.08 over the shot; 1.00 to 1.15 over 6 frames for a hit. Built with scale eval=frame plus center crop (crop w/h expressions do not animate).
- Speed ramp fast-slow-fast on one continuous move per reel: 3x to 6x into 0.3x, ramps of 6 to 15 frames, slow point on the action, knee on the beat, minterpolate to 120 fps first, tmix for shutter blur, deep whoosh, one shutter flash per reel.
- Whip pan between locations (dblur keyframed with sendcmd, same direction both sides, cut inside the blur, 8 to 12 frames). Soft eased wipes and luma wipes via xfade custom and geq plus maskedmerge.
- Shake only on a bass hit: sharp spike, 8 to 15 Hz, 20 to 35 px, decays in 0.3 to 0.5 s, applied after stabilization.
- Rebound (forward then reverse inside one beat) on one hero shot, never on people, smoke or steam. Do not interpolate steam, sparks or smoke at all.
- Reaction format and the Chandler components (added 2026-11-20, research/reel-references/2026-11-20-chandlerintelligence-every-workflow/): a second clip lives in a picture-in-picture card with a hero state (560 wide, top-left) and a thumbnail state (250 wide, bottom-left) and slides between them with speed-based blur (`pip`); tool or partner tag = icon plus name at top center when the name is spoken (`tooltag`); before/after = vertical white line with a <> handle sweeping across a filtered copy of the plate or an image (`slider`); proof wall = plate shrinks into the center of a 3x3 and eight tiles pop in (`grid`); numbers he says = dark panel with sliders moving to the values (`params`); storyboard table (number, he says, on screen, tool) as a card and as the artboard we hand Jacob (`storyboard`); one hollow word behind the head for a spoken CTA (`outline`, `behind: true`). Skip recursive zooms ("a bit too much"); move cards with a whip blur instead. Show the mechanism (the matte on a checkerboard, the sliders moving) rather than describing it. Brand stamp early, around 10 s.
- Smoothness (added 2026-11-20 night after Jacob: "make sure the reels aren't too choppy"). Three different things read as choppy and each has its own fix: (1) frame pacing: duplicated or dropped frames from a 24/60 fps source conformed to 30, VFR phone clips, or a padded slot; `tools/smooth_check.py <reel.mp4>` prints held frames, skipped-frame spikes and the cut list, and every delivered reel must come back clean (all three 2026-11-20 reels did: constant 30 fps, no duplicates, Remotion frame-accurate to the plate); (2) shutter strobe: phones expose fast motion at 1/500 s or faster in a bright shop, so a dance move or a wrench swing is razor sharp while it jumps 40 px between frames, which the eye reads as stutter; fix with `"mblur": true` on that slot (minterpolate to 120 fps, tmix 3, back to 30: a synthetic 270-degree shutter, about 1 s of render per output frame, verified on the Dougie dance shots: hands blur, truck stays sharp); the checker flags shots whose motion per frame is above 3.5; (3) editorial: cuts under a second back to back with no motion match; keep cuts on the beat and let one shot breathe. Not choppy and not to be "fixed": smooth handheld drift on a selfie talking head (vidstab only took it from 4.7 to 4.5 motion per frame; leave it). Slow motion stays `scd=none` interpolated and is verified frame by frame smooth.

### Delivery (lane 9, verified)
- 1080x1920, 30 fps, H.264 High 4.2, 8-bit yuv420p, crf 17 to 18, maxrate 16M bufsize 32M, closed 1 s GOP, 2 B-frames, aq-mode 3 strength 0.9, psy-rd 1.0:0.15, deblock -1:-1, light deband plus temporal grain, unsharp 0.5, BT.709 tags, AAC 192k 48 kHz stereo, faststart. Full command is in the platform report. Instagram re-encodes to 4 to 6 Mbps, so anything above 16 Mbps is wasted and HDR is not worth delivering.
- Safe zone: hook and hero inside y 285 to 1248 and x 65 to 880; captions above y 1250; cover title inside the center 1080x1440.
- Phone: "Upload at highest quality" on, Wi-Fi, Save video from Drive (never through a messaging app), no in-app trim or filters, song added in app, download the posted reel afterward so Claude can score it with libvmaf against the master.

## 3. Shooting brief for Jacob (lane 10, lane 3)

The edit can only be as good as the coverage. Every action gets a five-shot sequence before moving on: establishing wide (knee height), low push-in (lens a foot off the floor, one move, half pace), medium hands at work (45 degrees off axis), macro insert (bolt threads, gauge needle, torque click), reaction or one line to camera. Add per session: one foreground parallax pan, one orbit, one reveal (bay door or a rag pulled off a part), one light shot (steam, dust, sparks against the door), room tone and tool texture audio, and a before/after pair from a taped tripod mark. Twelve usable clips minimum, twenty is the target. Shoot the sequence before cleaning up; the mess is the content.

Settings: iPhone 4K60 HEVC, HDR Video OFF, Lock Camera and Lock White Balance on, long-press AE/AF lock, -0.3 to -0.7 EV, 1x lens, no pinch zoom. Pocket 3 stays on Normal 10-bit (it is the color reference), 4K60 (4K120 for inserts), manual white balance (5600 K outside, about 4200 K under shop tubes), sharpness -1, ND outdoors so the shutter sits near 1/120. Mic: DJI Mic 2 with a lav under the collar for every line to camera. Light: overheads off, bay door as the side key, or one Amaran 100d through a softbox; exteriors in the last hour before sunset. The full fourteen-row shot table and the per-milestone plans (block to machine shop, partner unboxings, frame swap, 10R140, engine assembly) are in the niche report.

## 4. Toolchain decision (lane 7, lane 8, verified)

- **Keep ffmpeg as the plate factory and finisher**, now with the tone map, tags, eased zoom, ramps, whip pans, wipes, shake, dialogue cleanup, ducking, loudnorm and the export recipe. build_reel2.py stays as fast mode for memes and same-day posts.
- **Adopt Remotion 4.x as the motion-graphics tier.** Node 24 is on the box. Benchmarked today: a 5 s 1080x1920 composition over a real plate rendered in 24 s wall time on CPU including bundling, so a 30 s reel is about 2 to 3 minutes. Free for an individual; $25 per seat per month if it ever runs under a company with more than three people. Pin versions (4.0.540 and Chrome 158 broke determinism on Windows this month). The edit list JSON becomes the Remotion inputProps so there is one schema.
- **Closed doors:** DaVinci Resolve Free removed Python scripting in 21.1 (Sept 2026) and Studio still needs the GUI open; CapCut draft automation violates its terms and breaks on updates; ffmpeg-gl-transition has no Windows build; libplacebo tone mapping worked in my renders but one agent saw corrupt frames on this driver, so the zscale chain is the fallback; cloud render APIs add cost and an upload step for nothing Remotion cannot do locally.
- **AI tools worth adding (all local, no GPU purchase):** DeepFilterNet3 for dialogue under shop noise; YOLO11n via OpenVINO for a tracked 9:16 reframe of landscape iPhone clips with a smoothed crop path and hand-following punch-ins; faster-whisper hotwords plus a part-name dictionary ("7.3", "F600", "rocker arms", "Rival") with WhisperX alignment if karaoke timing drifts; rife-ncnn-vulkan on the iGPU for clean 2x slow-mo of 30 fps iPhone clips. Upscaling is not worth it for a 1080 deliverable; sharpen with lanczos plus CAS instead. Gyroflow does not apply to either camera. No AI b-roll, no synthetic voice, ever.

## 5. Build order

Phase 1, renderer upgrade (build_reel2.py, this week): tone map and tags (done), two-layer shadow caption system with per-word tan from words.json, eased zoom via scale eval=frame, J-cut audio offsets, sfx list with the timing rules, dialogue cleanup chain and ambience bed with ducking, the Instagram export recipe, a lint pass that refuses to render on a broken rule (static shot over 4 s, hook over 7 words or not on screen by frame 4, missing payoff hold, missing end line), and the ffprobe tag check. Re-render Harley Trade as the before/after.
Phase 2, Remotion project in VIDEO/tools (next): plate pass from ffmpeg (short-GOP 1080x1920 intermediates), edit-list bridge, caption component, motion kit v1 (hook title with trail, punch-in with motion blur, highlighter underline, light leak, counter, lower-third, three transitions) with SFX auto-attach, still-frame QA, pinned versions. A/B against Phase 1 on the same reel.
Phase 3, analysis helpers: auto-editor silence map, librosa beat grid, motion-energy cut candidates, YOLO reframe, DeepFilterNet3, RIFE. These feed the edit-list generator so Claude proposes cuts from data, then applies the rules above.
Phase 4, measurement: download each posted reel, ffprobe and libvmaf against the master, log skip rate and share rate at 48 h, change one variable per post.

## 6. Lane report index
- 2026-11-20-editing-pacing-structure.md (cut rhythm, beat sheets, edit-list generator design)
- 2026-11-20-editing-hooks-retention.md (18 hook templates, frame-by-frame first 3 s, re-hook schedules, endings)
- 2026-11-20-editing-typography-captions.md (verified ASS style system, fonts, avoid list)
- 2026-11-20-editing-color-pipeline.md (HLG diagnosis, tone map tests, grade, camera settings)
- 2026-11-20-editing-sound-design.md (verified ffmpeg audio chains, SFX timing, starter kit, librosa)
- 2026-11-20-editing-motion-transitions.md (verified filter graphs for zoom, ramp, whip, wipe, shake)
- 2026-11-20-editing-tooling-landscape.md (Remotion decision, Resolve and CapCut dead ends)
- 2026-11-20-editing-ai-tools.md (DeepFilterNet, RIFE, YOLO reframe, Whisper hotwords, CPU timings)
- 2026-11-20-editing-platform-delivery.md (export command, safe zones, upload checklist, VMAF loop)
- 2026-11-20-editing-niche-style-shot-design.md (style guide, shot list, gear, per-milestone plans)
