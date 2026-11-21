# Montage craft: music-driven truck build reels (lyric montages and beat-cut edits)

Research date: 2026-11-21. Lane: the format that already works on @elcoyotediesel ("You just have to go for it" lyric montage: 984 views, 31.6 percent skip, 10.2 s average watch, best build-footage retention; the 2026-11-19 Rival lyric reel copied a 33 s "Somewhere I Belong" montage). Builds on `2026-11-20-EDITING-MASTER-PLAYBOOK.md` (structure, motion, sound) and `2026-11-21-audio-trends-and-voice.md` (this week's charts). Nothing from those files is repeated except where a number changed.

House rules that frame everything below: song added inside Instagram (render is silent plus a guide track), one poster lockup on the hook (LOUDER / MEGANTE / TROPI from `FONT-LIBRARY.md`), no color grade, no CTA, end within 1.5 s of the payoff, Playfair yellow lyric text is the one lyric-reel exception.

Honesty note: Instagram is login-walled, so every example is a TikTok or Instagram mirror pulled with yt-dlp; the 2026 "truck edit" lane on TikTok is small and dominated by two or three accounts, so n is low. Beat alignment was measured with librosa beat tracking against PySceneDetect cuts and against frame-difference "visual hits" (cuts plus flashes, whips, zoom punches and velocity knees). librosa's beat phase is an estimate; absolute numbers are good to about a frame, downbeat labels are a guess verified by onset energy only.

Files: `research/reel-references/2026-11-21-montage-craft/` (17 clips, `NN-handle--slug.mp4` plus `.info.json`, `watch-NN-.../scenes.csv` and `sheet-NN.jpg`, `stats.txt`, `hits-analysis.txt`). Transcripts: `research/transcripts/2026-11-21-montage-*.txt` (5 pulled).

---

## 0. What the measurements say in six lines

1. The cleanest truck montage in the set (6ixoh_titan "First day of fall truck edits", 53.6k views, 30.6 percent like rate) cuts once per bar, every cut within a median 1.0 frame of the beat (88 percent inside 2 frames). Templates and velocity edits sit at 2 to 4 frames. Our generator standard is therefore 1 frame, not "close".
2. Montages open on a HOLD, not on fast cuts: 4.1 s static wide (05), 5.8 s door-open plus key-fob reveal (12), 2.2 s crash shot after a 1.8 s strobe (13). The hold is 2 to 3 bars. The fast cutting starts after it.
3. Body shot length is one bar (1.6 to 1.9 s at 123 to 143 BPM) or 3 beats (1.3 s). Six to twelve shots per 8 bars. Burst sections (strobe or flicker) run at a third of a beat for 1 to 2 s, once per reel, on the drop.
4. Edits earn likes, not shares. Share rates: pure montages 0.95 to 1.56 percent, lyric-word template 1.41 percent, the same creators' talking memes 1.44 to 2.35 percent. Same split as our account. A montage is the retention and like tool; the share line still has to come from the caption or a meme beat.
5. Pure edits carry zero on-screen text. Text appears only in two sub-formats: one lyric line per shot (the Somewhere I Belong reference) or one word per beat (the CapCut "BEAT IT" template, 297k views). Both put the word on the sung syllable, at the cut.
6. Endings bookend: the last shot is the hook wide again (05, 13, 14), held 1.0 to 1.9 s, cut on a downbeat. No outro.

---

## 1. Examples table (2026, downloaded and measured)

Share rate = shares / views. "Median offset" = median absolute distance from each hard cut to the nearest librosa beat, in frames at 30 fps; the random-cut baseline for the same clip is in brackets. Visual hits per 8 bars counts cuts plus in-shot hits.

| # | Clip (file prefix) | Posted | Len | Views | Likes | Shares | Share | Hard cuts | Median shot | Hits / 8 bars | Median offset (random) | What it is |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 05 | @6ixoh_titan "First day of fall truck edits" | Sep 2 | 18.9 s | 53,600 | 16,400 | 669 | 1.25% | 9 | 1.85 s | 6.1 | **1.0 fr** (3.2) | Tripod detail montage of a red F-250 at golden hour, one shot per bar at 129 BPM, no text |
| 12 | @trent_cody "iPhone clips lowkey fun" | Feb 19 | 18.2 s | 1,100,000 | 173,900 | 14,200 | 1.29% | 10 | 1.3 s | 8.4 | 2.6 fr (3.2) | iPhone night montage of a lifted Super Duty under a gas station canopy, 5.8 s hook hold, "Shake Dat Whammyyyy" 136 BPM |
| 14 | @trent_cody "Legacy" | May 25 | 17.6 s | 499,500 | 105,100 | 7,767 | 1.56% | 12 | 1.5 s | 11.4 | 3.6 fr (3.2) | Night convoy montage, 1.2 s chrome-lip reflection hook, whip pan at 12 s, 144 BPM |
| 13 | @trent_cody "Ran my truck into the wall just for the edit" | Jan 9 | 15.8 s | 361,600 | 96,900 | 3,904 | 1.08% | 13 (+16 flashes) | 1.1 s | 29.1 | 3.3 fr (3.6) | Warehouse edit, 1.8 s strobe open, crash shot held 2.2 s, burnout, bookend wide, 123 BPM |
| 11 | @pghdevinn "BEAT IT TRUCK EDIT" (CapCut Pioneer template) | May 20 | 21.9 s | 297,500 | 86,000 | 4,191 | 1.41% | 14 | 0.7 s (truck part) | 9.6 | 1.9 fr (3.3) | 14 s of MJ footage with one word per beat in wide-tracked serif caps, then the truck in 0.7 s slots; drop reveal on "IT" at 14.0 s |
| 17 | @trent_cody "Regular traffic" | Apr 1 | 14.7 s | 138,300 | 29,500 | 1,308 | 0.95% | 0 (11 flashes) | one take | 13.4 | 4.6 fr (3.5) | Single handheld orbit at 60 fps with a velocity flicker burst 6.0 to 7.7 s (one flash per 0.17 s = a third of a beat at 123) |
| 16 | @pghdevinn "#dodge #diesel" CapCut | May 27 | 15.7 s | 29,100 | 9,909 | 84 | 0.29% | 7 (+15 flashes) | 0.6 s | 27.1 | 4.9 fr (4.7) | Family Guy clip then truck stills with flash transitions. Random-level beat alignment, lowest share rate in the set |
| 08 | @truck_edit1 static-drop slideshow | Nov 1 | 60 s | 32,800 | 5,743 | 369 | 1.13% | 30 | 1.23 s | n/a | 2.8 fr (3.5) | CapCut slideshow template: fixed 37-frame slots regardless of the beat, one 17.7 s clip in the middle |
| 10 | Reference "Somewhere I Belong" lyric montage (the one the 11-19 Rival reel copied; creator stats unknown) | 2026 | 33 s | n/a | n/a | n/a | n/a | 15 | 1.9 s | 12.3 | 3.0 fr (4.1) | One lyric line per shot, yellow serif, line appears on the cut, cuts follow sung phrase starts not the drum grid, 5.5 s final hold |
| 04 | @6ixoh_titan 2nd gen dually walkaround | Oct 6 | 48 s | 142,600 | 21,900 | 3,262 | 2.29% | 1 | one take | n/a | n/a | Control: talking walkaround with ONE WORD per screen captions (white caps, centered). Not music driven, but the highest share rate of any truck clip here |
| 01/02/07 | @6ixoh_titan "POV: u drive a ..." memes | Nov 3 to 10 | 6 s | 64,800 to 177,000 | | 934 to 4,160 | 1.44 to 2.35% | 1 | one take | n/a | n/a | Control: talking-face memes from the same account share 1.5 to 2x the edits |
| 03/06/09/15 | walkaround one-takes and a 90 s dealer reel | | | | | | | | | | | Out of lane, kept in the folder for the record |

Account context: @6ixoh_titan is a 6.0 Powerstroke owner (main @6.0_titan on TikTok) who posts edits of his own truck between memes; his 2026 top is a traffic-stop clip (584k) and a "6.0 ASMR turbo noises" clip (370k, 58k likes). @trent_cody is a lifted Super Duty owner whose edits are the account; his memes ("Hit da sea lion", 1.8M) still out-share the edits. @pghdevinn is a CapCut-template account. @truck_edit1 is a static-drop (bagged truck) aggregator.

What did NOT show up: no truck "lyric montage" from 2026 with real traction on TikTok or Shorts beyond the word-per-beat template, and no "cold start to drive" montage above 25k in the window (JMR Rebuilders' coldstart Shorts in the 11-21 niche-winners file are one-takes). YouTube Shorts search for truck edits returns pre-2023 material; the 2026 Shorts ("OBS 7.3 Powerstroke 8K Cinematic Truck Film", Apr 13, 680 views) show the lane is dead there.

---

## 2. Measured rules of the format

Hook (0 to 4 s)
- A held or slow shot of 2 to 3 bars, something moving inside it: a door swinging open and a key fob coming into frame (12), a static tripod wide with the truck already lit by low sun (05), a chrome-lip reflection the camera pulls out of (14). The playbook's "motion in frame 1" holds; "first pattern change by 1.0 to 1.5 s" is satisfied by in-shot motion, not by a cut.
- Exception: the strobe open (13): 10 flashes in 1.8 s on the drop, then the crash held 2.2 s. One burst per reel.
- No text on any pure edit. Our lockup is the one burned element and it lives inside the hold.

Body (cuts)
- One shot per bar is the base unit (05: 1.86 s at 129 BPM; 14: 1.5 s median at 144). Two-beat and three-beat shots appear in the accelerations (12: 1.0 to 1.7 s alternating). Nobody sustains one cut per beat for more than 2 bars.
- Alternate lengths after the drop. Measured runs: 12 goes 1.3 / 1.4 / 1.0 / 1.2 / 1.5 / 1.3 / 1.7 / 1.3 s; 14 goes 1.9 / 0.9 / 0.7 / 1.8 / 1.9 / 1.4 / 2.2 / 1.5. The pattern the tutorials call "1-2-1-2" (two-beat, four-beat, two-beat, four-beat) is roughly what 14 does; no 2026 tutorial I could find names it, so treat it as an observed habit: never three equal shot lengths in a row after the drop (05 breaks this on purpose with its metronomic one-per-bar; that reel is a calm tripod piece, not a hype edit).
- Beat lock: the hand-cut reel sits at 1 frame; templates and velocity edits at 2 to 4 frames (because their hits are in-shot flashes, not cuts). Both land their big moments (drop reveal, crash, whip) on a beat within 1 to 2 frames.
- Downbeat vs snare: the drop reveal lands on a bar's beat 1 in every example that has one (11 at 14.0 s, 13 at 1.8 s, 05's first cut at 4.12 s on the bar line). Secondary cuts in the fast sections land on beats 1 and 3 (the kick / snare alternation), never on the off-eighths: zero cuts in the whole set sat closer to an eighth than to a beat.
- Shots per 8 bars: 6 (calm tripod), 8 to 12 (standard edit), 27 to 29 only when flashes are counted (template, strobe). Target for us: 8 to 10 per 8 bars at 120 to 140 BPM.

Speed ramps and in-shot hits
- Velocity flicker (17, 13): a burst of 6 to 11 exposure flashes spaced a third of a beat (0.17 s at 123 BPM) over 1 to 2 s, on one orbit, once. Reads as "velocity" without any actual slow motion.
- Real ramps (12's hook, 14's convoy): slow into the hit, normal after. The After Effects flow tutorial (transcript, Oct 2026) says what the measurements show: structure shots to the kicks and snares first, "the song is the most important thing"; sync the slow point to the sung word or the kick; add a single-frame "scope" (one frame punch) on the impact ("adds so much more impact"); enable frame blending when the source is not high frame rate.
- CapCut 2026 velocity guides: Speed > Curve > Custom, multiple points per clip; slowest point on the beat drop; "don't overuse speed changes, good velocity edits are smooth, beat synced, easy to follow"; shake only at the drop or a fast pass; motion blur on top (transcripts how2whiz May 2026, videonerd; fluxnote Apr 2026; capcut.com).

Reveal and payoff
- The drop reveal is the truck wide or the hero angle after a withhold: 11 withholds the truck for 14 s of lyric footage, then "IT" lands on the first truck frame. 12 withholds the whole truck behind the door for 5.8 s. 13 withholds the crash for 1.8 s of strobe.
- Payoff shot = the hook wide again (05 ends on the same framing as frame 1; 13 and 14 end on a wide with a walk-off or roll-off). Hold 1.0 to 1.9 s, cut on a downbeat, done. Nothing after.

Where lyric text sits and what font class
- Reference 10: Playfair-class serif, yellow, 92 px at 1080 wide, soft shadow, one line (3 to 5 words) per shot, centered horizontally, vertical position changed per shot to the empty zone (upper third over a hunched worker, lower third over a hand holding a part, mid over a car front); line appears on the cut and stays until the next cut.
- Template 11: wide-tracked white serif caps, one WORD per beat, centered, over everything including the face.
- Walkaround 04: white sans caps with a shadow, one word per screen in the upper third, spoken word timing.
- Jacob's "You just have to go for it" and the 11-19 Rival reel sit in the reference-10 class. Keep it there: it is the lyric exception to the "poster lockup only" rule, and the Playfair yellow is what tested best on his footage.

---

## 3. 2026 tutorial rules (sources read this session)

- Length: 7 to 15 s for a TikTok car edit (fluxnote, Apr 25 2026); 15 to 60 s per car-editor.com. Our data: the winners are 15 to 19 s. Keep Rival montages at 15 to 22 s unless the song section demands 30.
- Tempo: phonk and drift house at 130 to 160 BPM for car edits (fluxnote). Our truck set: 123 to 144 BPM. The pacing math (clipmusic, Jul 3 2026): seconds per beat = 60 / BPM; bar = 4 beats; "cut every bar when calm, every beat or two for intensity"; "a cut on every single beat is exhausting"; "one well-placed hero shot on a drop is worth twenty beat-matched filler cuts".
- Phrase structure (cutagent, Aug 2 2026): reserve the biggest picture change for the biggest musical change; phrase starts introduce something new; weak beats support motion inside the shot; "let motion begin before the marker when its impact, reveal or completion should land on the beat" (a hand enters early and completes on the downbeat).
- Drill from the Hollyland Premiere beat-edit guide: build 8 beats = 2 clips of 4 beats, one clip change exactly on the drop, then 2 beats per clip for 16 beats. This is the only published "shots per 8 bars" rule and it matches our measured 8 to 12.
- Cut on the downbeat vs the snare: the flow tutorial marks every kick AND snare, cuts on kicks for shots and uses snares for in-shot actions (scope-in, turn). fluxnote: "align cuts with the main beats and snares". Nobody cuts on hi-hats; the strobe bursts live on hi-hat spacing instead.
- Beat tools: CapCut tap music track > Beat > Auto Beat (markers), Edits Beat Markers (dots on the timeline since May 2025, Hypebeast June 2026 recap), Premiere auto beat markers with a sensitivity slider ("over-populate at higher sensitivity, thin them"), Resolve markers by ear. Our generator replaces all of these with librosa, which is the same thing with a frame of precision instead of a visual dot.

Transcripts pulled: `2026-11-21-montage-velocity-flow-time-remap-outoforder.txt` (After Effects, Oct 8 2026, the detailed one), `-velocity-capcut-2026-how2whiz.txt` (May 28 2026), `-beat-drops-capcut-videonerd.txt` (Nov 2025, CapCut's "velocity effect" auto-sync), `-edits-auto-lyrics-yourfixguide.txt` (Jul 23 2026, actually the Captions tool), `-baila-lento-car-edit-capcut-athextic.txt` (music only, nothing extractable). The "Keshav super smooth velocity" video (Feb 2026, 3.4k views) hit YouTube's 429 twice; skipped.

---

## 4. Lyric reel specifics

How the good ones time the words
- The word lands on the sung syllable. Practitioner numbers from 2026 guides: text in "at or just before" the vocal onset (Renderforest); 0.06 s early, about 2 frames (Vidova); punchy entries start a few frames before the downbeat so the impact lands on the kick or snare, soft entries start on the beat (lyricsflow tips); a word a few frames late "feels like a mistake even when viewers can't say why" (Captyne). Automatic word timing lands within about 2 frames at best and averages half a second of error (DaVinci Resolve Club), so auto lyrics still need a hand pass.
- Pickup words ("and", "so", "'cause") start before the beat; time them by ear, don't copy the first chorus's timing to the second (chatcut guide).
- The reference montage (10) ties each line to its cut: cut and line arrive together on the phrase's first word, so the cut itself is placed on the vocal onset, not on the drum grid (median 3 frames off the beat, which is the vocal lead).
- Line length: 3 to 5 words per line in the reference and in Jacob's EDLs (max "Until my wounds are healed"). One line per shot. Repeated lines ("I will never know" twice) get two shots.

Fonts and placement in 2026
- Lyric-video font guides lean bold sans for pop and keep serif, typewriter and handwritten for indie, alt and emo, and for "one emphasis word or a title card" (lyrc.studio, makelyricvideo). Serifs and italics are rising in short-form moodboard edits (Fontfabric 2026 trends; the Medium TikTok typography piece). Thin serifs need weight or a shadow on phones; the reference uses a soft shadow, Jacob's EDL uses shadow 3.
- Placement: pause on the lightest and darkest frames behind the words and move the line to the empty zone per shot (CapCut lyric workflow page); never over the face; keep out of the bottom 250 px where Instagram's UI sits.

Instagram's own lyric tools, status Nov 2026
- Reels composer: the native "Lyrics" option (launched 2023) is still there for songs that have synced lyrics in the library: add the song, swipe to the lyrics option, pick a font style, drag to reposition. Only select songs; professional accounts on the limited catalogue see fewer of them; style options are a handful of presets, none of them Playfair yellow. (Workroom guide; Social Media Today launch note; several 2026 how-tos agree.)
- Edits app: "Lyrics" shipped Aug 19, 2026 under Captions ("add music to your timeline, tap Captions, select Lyrics, Edits generates the lyrics from your selected track, styled like any other caption"). Timing control is not documented; it is a caption track, so lines can be trimmed and retimed by hand like any caption. Beat markers (dots) are in the same timeline. Edits also added font importing in Sept 2026 (EmbedSocial roundup), which means Playfair could be loaded in Edits if Jacob ever finishes a lyric reel there instead of in our renderer.
- Our position stays: render the lyric text ourselves (exact frames, Playfair yellow), silent plus guide track; add the song in Instagram or Edits; align by the guide track's first downbeat against the Edits beat markers. If Instagram's song offset lands more than 1 frame off the guide, nudge the clip, not the text.

---

## 5. Songs that fit a Rival montage this week, with measured grids

Cross-checked against `2026-11-21-audio-trends-and-voice.md`; that file's five picks are not re-argued. Below: montage-specific numbers (measured with librosa on the official uploads; published BPMs in brackets where they exist) and additions the audio file does not have. "Downbeat" = first bar line of the recommended 30 s section, on the official recording; the Instagram clip can sit up to a second off, so confirm against the Edits beat markers before rendering. Loudness map = RMS per 8-bar block, used to find the chorus.

| Song | BPM measured (published) | Bar | Recommended section | First downbeat (s) | Why for Rival |
|---|---|---|---|---|---|
| Time, Pink Floyd | 123 (120 to 122) | 1.95 s | 2 bars before the vocal entry, through the first verse: 128.2 to 157 s | 128.22, vocal entry on 132.17 | The then-and-now trend sound; the roto-tom build into "ticking away" is a ready-made drop for an as-found vs today cut |
| Flower In A Hurricane, Justice (GTA VI) | 129 (126 chorus) | 1.86 s | Pre-chorus into chorus: 55.9 to 86 s (loudness jumps 75 to 96 percent at 59.7) | 55.94, drop on 59.74 | Climbing 17k videos a day; the cinematic vehicle-edit sound of the next three weeks |
| Mr. Brightside, The Killers | 143.6 (148) | 1.67 s | "Jealousy" pre-chorus into the chorus guitar: 39.5 to 69 s | 39.45, drop on 52.41 | Nostalgia throwback trend; lyric-reel candidate because the lines are short and everyone knows them |
| Housewife, Tate McRae | 136 (133) | 1.76 s | Chorus 1: 37.0 to 66 s (94 to 98 percent) | 36.99 | "I just wanna" montage with a spending reveal; meme slot |
| Coming Up Roses, Harry Styles | 172 in 12/8 (177) | 1.39 s | Final chorus 191 to 221 s (100 percent) or chorus 2 at 115 to 142 s | 191.31 or 115.40 | Year-recap trend; count it in 12/8 so a bar is 1.39 s, cut every 2 bars |
| Jane!, The Long Faces (NEW, not in the audio file) | 143.6 (146) | 1.67 s | Chorus 1: 47.0 to 77 s (96 to 99 percent) | 47.04 | 2026 sleeper hit built on fan edits (anime "Ryu" edits), so the edit audience already associates it with montage cutting; indie-rock, fits an OBS Ford |
| Shake Dat Whammyyyy, BigKeiona (NEW) | 136 | 1.76 s | 0 to 30 s | measure in app | The sound under trent_cody's 1.1M truck edit (clip 12); listed on TikTok's "truck edit songs" page; rap, night footage |
| GOOD FOR NOTHING, Matthew Goodnough (NEW) | 152 | 1.58 s | 39 to 65 s (92 percent plateau) | 39.4 | TikTok's "truck edit songs" page names it as a go-to for diesel edits (#duramax #powerstroke posts); country-rock at 152 means cut every 2 bars |
| Evening and Balcony on a Saturday, Thalassor (NEW) | 112 | 2.14 s | any 30 s, ambient | n/a | 239k posts, "the trending version is an edit" (Brittley, Nov 12); slow recap bed for a progress montage, voice optional |
| Paper Moon Static, Marnie Cusk; Sweet As Honey, The Sundries; Perhaps That Day Should Be Left Behind, Nula (NEW) | not measured | | | | TikTok Hot list Nov 12: slow photo series (2.5M), "tight edit with close-up detail shots, 20 s" (539k), "quick before-and-after, 11 s" (176k). Formats match a parts-detail montage and a before/after frame swap |
| Montagem da Chupeta, Lthiago | not measured (age-gated upload) | | | | Worldwide TikTok number 1 on Nov 16; Brazilian funk edit sound; too far from the audience, listed for completeness |

BPM lookups that disagreed and how they were settled: Time 120 (SongBPM, Songdata) vs 122 (GetSongBPM, Planetary), measured 123; Flower In A Hurricane 126 chorus (Hooktheory) vs 69 half-time (Beatport), measured 129; Somewhere I Belong 162 (Tunebat) vs 81 half-time (SFR Beats, Klang): use 162 as the beat for cutting and 81 for the feel; librosa locked onto 108 on the 33 s reference clip, which is a mis-track, so always measure on the full song, not the reel.

---

## 6. Beat-grid recipe for the generator (librosa beats to an EDL)

Inputs: song section wav (or the guide track), BPM prior from the table, target length, shot bins (hook, build, hero, alternates, payoff), lockup preset and text.

1. Beats. `librosa.beat.beat_track(start_bpm=prior, units="time", trim=False)`. Fit a straight line to the beat times (least squares) to get a constant period and phase; discard tracked beats more than 25 ms off the fit; the fitted grid is the cut grid. Period at 30 fps is fractional (0.464 s = 13.9 frames at 129 BPM), so keep beat times in seconds and round each CUT to the nearest frame at the end (max error half a frame, 17 ms, inside the measured 1-frame standard).
2. Downbeat. Average onset strength on each of the four beat phases; the strongest is beat 1. Print the first four downbeats and have Jacob confirm one by ear in Edits (dots line up) before rendering. In the plans below the downbeat numbers come from this method on the official recordings.
3. Bar map for a 16-bar section (29 to 31 s at 123 to 136 BPM; drop two alternate bars for a 14-bar, 25 s cut):
   - Bars 1 to 2, hook hold: one shot, in-frame motion, eased push 1.00 to 1.06 over the 2 bars. Lockup on at frame 4, off at the end of bar 2 (2.5 to 3.9 s depending on tempo; cap at 3 s by fading it 0.3 s before the bar line if the bars are long).
   - Bars 3 to 6, build: cut on every downbeat (4 shots, one bar each), alternating wide and tight.
   - Bars 7 to 8, acceleration: cut on beats 1 and 3 (4 shots of 2 beats).
   - Bar 9 downbeat, drop: the hero shot, held 2 bars. Speed ramp on this shot only: 3x to 6x into 0.3x, ramp-in ends (the knee) on the bar-9 downbeat, hold slow for 2 beats, ramp out over 8 frames to 1x by beat 3 of bar 9, normal through bar 10. One white flash frame on the knee frame, shake spike on the same frame (20 to 35 px, 0.3 s decay), deep whoosh peaking on it. Nothing else burned in.
   - Bars 11 to 14, alternates: one shot per bar, lengths alternate 4 beats / 2 beats / 4 beats / 2 beats if the music keeps driving (that is the "1-2-1-2"), or straight one-per-bar if the song settles.
   - Bar 15 downbeat, payoff: the hook framing again (or the reveal the whole reel withheld), held 1.0 to 1.5 s, then end. Last frame = bar 15 downbeat plus 1.0 to 1.5 s, never later than bar 16 beat 1. No fade.
   - Optional burst: a strobe or velocity flicker of 6 to 10 flashes at a third of a beat may replace the flash frame on the drop. One per reel, never on people, smoke or steam (playbook motion rule).
4. Cut emission. Every cut time = a grid beat, rounded to the frame. Whoosh on at most one cut in four, starting 2 to 3 frames before the cut. Transitions are hard cuts; the only soft one allowed is the whip pan between two locations, cut inside the blur on the beat.
5. Lyric lines (lyric reels only): see section 7. Lines are their own track, keyed to vocal onsets, not to the cut grid, but each line's shot boundary is moved to the line's onset when the two are within one beat.
6. Output: build_reel3 EDL with `start` per slot in seconds (frame-rounded), `ramp` on the hero slot `{knee: <bar9 downbeat>, slow: 0.3, in_frames: 12, out_frames: 8}`, `lockup` with `start: 0.13, end: min(3.0, bar3 downbeat - 0.1)`, `flash: [<knee frame>]`, `guide_audio` = the song section so the Edits beat markers can be matched, then stripped for the posted file.
7. Check with `tools/smooth_check.py` (no duplicates) and a second librosa pass on the rendered guide: every cut within 1 frame of a grid beat, hero knee within 1 frame of the drop, or the render fails.

---

## 7. Lyric-timing rule

- ON = vocal onset of the line's first stressed syllable minus 2 frames (about 60 ms). Get onsets from a Whisper word-timestamp pass on the song section, then hand-check every first word against the waveform; Whisper on sung vocals drifts, so trust it only within 2 frames after checking.
- Pickup words ("and", "so", "'cause") are timed by ear; the 2-frame lead applies to the stressed word, not the pickup.
- OFF = the next line's ON (no gap) while the vocal is continuous; if the gap to the next line is longer than one bar, OFF at the phrase's last syllable plus 10 frames.
- One line per shot, 3 to 5 words, maximum 24 characters. A repeated line gets a second shot. No word-by-word reveal unless the song is being used as a word-per-beat track (template 11 style), and then it is a different reel.
- The line that carries the meaning (the title line, the turn) sits on the hero shot at the drop, and the cut arrives with it.
- Playfair Display, yellow 0xF8D000, 92 px at 1080 wide, shadow 3 (the 11-19 EDL values; FONT-LIBRARY says the lockup yellow #F7D43C is interchangeable). Centered horizontally; vertical slot chosen per shot (upper, mid, lower third) by the empty zone, never over a face, never in the bottom 250 px. No outline, no band, no per-word highlight (rejected list).
- Lyric reels keep the one hook lockup too: it lives in bars 1 to 2 and the first lyric line does not start until the lockup is gone.

---

## 8. Three Rival montage plans

Footage bins available now (Drive `VIDEO/inbox`): `2026-11-19 Rival Lyric Reel (Somewhere I Belong)/raw clips` (iPhone IMG_3856 to 3863 and IMG_4191 to 4194: shop interior, hands on parts, the body, Jacob working; DJI 2026-11-15 clips 0032 and 0033: outdoor truck moves), `2026-11-20 Harley Trade (Reel 1)/raw clips` (IMG_3784, talking plus the truck), `2026-11-20 Lumber to SEMA (Reel 2)/raw clips` (IMG_3787 and the as-found exterior footage). Shot labels below name the type; map them to clips in the EDL. All cut times are reel seconds from the first frame; the song's absolute downbeat is given so the guide can be aligned in Edits.

### Plan A: "As found / today" build montage. Time, Pink Floyd. MEGANTE lockup.
Song section: 128.22 s of the official recording (two bars before the vocal entry at 132.17). 123 BPM, bar 1.95 s. Reel length 29.0 s.
Lockup (bars 1 to 2, 0.13 to 2.9 s): MEGANTE, block "1959 F600", sub "PROJECT RIVAL  ·  CHEYENNE WY".

| Reel s (cut) | Bar.beat | Shot type |
|---|---|---|
| 0.00 | 1.1 hold | As-found exterior wide, the F600 cab on the old frame, Jacob walking into frame (eased push 1.00 to 1.06) |
| 3.95 | 3.1 vocal entry | Hands on the first bolt, tight |
| 5.88 | 4.1 | Body panel wide, shop |
| 7.85 | 5.1 | Grinder or cutoff wheel, tight (no interpolation on sparks) |
| 9.75 | 6.1 | Frame on stands, wide |
| 11.80 | 7.1 | 7.3 detail, tight |
| 12.78 | 7.3 | Parts on the bench, tight |
| 13.72 | 8.1 | Jacob at the truck, medium |
| 14.65 | 8.3 | DJI low pass, 2 beats |
| 15.58 | 9.1 DROP | Hero: DJI orbit of the body, ramp knee on 15.58, slow 2 beats, flash frame, held to 19.25 |
| 19.25 | 11.1 | Today's front end, wide |
| 21.08 | 12.1 | Badge or grille, tight (2 beats) |
| 22.06 | 12.3 | Door jamb or interior, tight |
| 22.90 | 13.1 | Three-quarter wide |
| 24.73 | 14.1 | Jacob closing the hood or door, medium |
| 26.56 | 15.1 PAYOFF | Same framing as 0.00, today's truck in it, held 1.4 s |
| 28.0 | end | |

### Plan B: Lyric montage. Mr. Brightside, The Killers. LOUDER lockup, Playfair yellow lines.
Song section: 39.45 s of the official recording ("jealousy" pre-chorus), 143.6 BPM, bar 1.67 s. Reel length 26.5 s. Lyric cues are given as two-word anchors; take exact lines from the song and time each to its sung onset minus 2 frames (section 7). Share line for caption line 1, not on screen.
Lockup (0.13 to 2.9 s): LOUDER, script "Built not", block "BOUGHT", sub "PROJECT RIVAL".

| Reel s (cut) | Bar.beat | Lyric anchor (ON = onset minus 2 fr) | Shot type |
|---|---|---|---|
| 0.00 | 1.1 hold | none until lockup is off | Static wide of the truck under shop lights, Jacob walking through (2 bars) |
| 3.25 | 3.1 | "jealousy" line | Hands, wrench on the frame, tight |
| 4.88 | 4.1 | "saints" line | Sparks or torch, tight |
| 6.48 | 5.1 | "lullabies" line | Body wide, fluorescent shop |
| 8.10 | 6.1 | "alibis" line | Parts on the bench, overhead |
| 9.73 | 7.1 | "price I pay" | Receipt, boxes, the Vinny-list part, tight |
| 10.55 | 7.3 | | Jacob's face, medium, 2 beats |
| 11.36 | 8.1 | "destiny" line | DJI low pass |
| 12.20 | 8.3 | | Engine detail, tight, 2 beats |
| 12.96 | 9.1 DROP | "Mr. Brightside" | Hero: DJI orbit reveal of the whole truck, knee on 12.96, slow 2 beats, flash frame, held to 16.21 |
| 16.21 | 11.1 | (guitar, no line) | Rolling shot wide |
| 17.83 | 12.1 | | Wheel, tight, 2 beats |
| 18.65 | 12.3 | | Mirror or badge, tight |
| 19.48 | 13.1 | | Three-quarter wide |
| 21.08 | 14.1 | | Jacob leaning on the fender, medium |
| 22.71 | 15.1 PAYOFF | | Same wide as 0.00, truck lit, 1.3 s |
| 24.0 | end | | |

### Plan C: Cinematic roll, no lyrics. Flower In A Hurricane, Justice (GTA VI). TROPI lockup.
Song section: 55.94 s of the official recording (two bars before the chorus lift at 59.74), 129 BPM, bar 1.86 s. Reel length 28.5 s. Outdoor, golden hour or night under the shop lights; DJI does the moves, iPhone does the tights.
Lockup (0.13 to 2.9 s): TROPI, block "EL COYOTE", no sub (float it in the sky above the cab).

| Reel s (cut) | Bar.beat | Shot type |
|---|---|---|
| 0.00 | 1.1 hold | DJI slow push on the grille from low, 2 bars |
| 3.80 | 3.1 DROP (early drop, chorus lift) | Hero: DJI orbit, knee on 3.80, slow 2 beats, flash frame, held to 7.61 |
| 7.61 | 5.1 | Headlight, tight |
| 9.52 | 6.1 | Side profile roll-by, wide |
| 11.42 | 7.1 | Wheel spinning, tight, 2 beats |
| 12.37 | 7.3 | Mirror with sky in it, tight |
| 13.33 | 8.1 | Rear three-quarter, wide, 2 beats |
| 14.28 | 8.3 | Exhaust or stack, tight |
| 15.23 | 9.1 | Second DJI move (reverse orbit), 2 bars, strobe burst allowed here: 8 flashes at 0.155 s from 15.23 |
| 19.04 | 11.1 | Interior through the window, tight |
| 20.94 | 12.1 | Jacob in the door, medium, 2 beats |
| 21.89 | 12.3 | Hand on the shifter, tight |
| 22.85 | 13.1 | Front wide, truck rolling toward camera |
| 24.75 | 14.1 | Tail lights pulling away, 2 beats |
| 25.70 | 14.3 | Badge, tight |
| 26.65 | 15.1 PAYOFF | Hook framing again, truck stopped, 1.3 s |
| 28.0 | end | |

Alternates if a song is unavailable on the professional-account catalogue: Jane! (47.04 s downbeat, 143.6 BPM) swaps into Plan B with the same bar map (bar 1.67 s, identical cut list); GOOD FOR NOTHING (39.4 s, 152 BPM, bar 1.58 s) swaps into Plan C with every cut moved to the 1.58 s grid (cut every 2 bars in the alternates section).

---

## 9. Sources

Examples: TikTok profiles @6ixoh_titan, @trent_cody, @pghdevinn, @truck_edit1 listed with yt-dlp 2026-11-21 (stats from each clip's info JSON); Instagram @liftedtrucks profile page (logged out) and reel DcZfheoSvFL via yt-dlp. TikTok discover pages for truck-edit songs: https://www.tiktok.com/discover/truck-edits-songs , /good-songs-for-truck-edits , /diesel-truck-edits (JS-rendered, read through search snippets only).
Tutorials and guides: https://fluxnote.io/guides/how-to-make-viral-car-edits-tiktok (Apr 25 2026); https://clipmusic.ai/blog/bpm-video-editing-guide (Jul 3 2026); https://www.cutagent.ai/en/blog/davinci-resolve-edit-to-beat (Aug 2 2026); https://store.hollyland.com/blogs/creator-hub/beat-edit-in-premiere-pro ; https://www.car-editor.com/how-to-make-cinematic-car-reels/ ; https://www.capcut.com/resource/how-to-do-velocity-on-capcut ; https://editingbyvikas.com/velocity-capcut-template/ ; YouTube transcripts listed in section 3.
Lyric timing and type: https://www.capcut.com/features/how-to-make-a-lyric-video-capcut-workflow-comparison ; https://chatcut.io/blog/how-to-make-a-lyric-video ; https://lyrc.studio/blog/best-fonts-for-lyric-videos ; https://makelyricvideo.com/guides/lyric-video-fonts ; https://vidova.ai/blog/what-is-kinetic-typography ; https://captyne.com/blog/kinetic-typography-captions-explained ; https://davinciresolveclub.com/kinetic-lyric-video-davinci-resolve/ ; https://www.renderforest.com/blog/how-to-make-lyric-video-with-ai ; https://www.fontfabric.com/blog/top-typography-trends-for-2026/ .
Instagram and Edits: https://edits.instagram.com/blog/multi-language-captions/ (Aug 19 2026, Lyrics under Captions); https://workroom.ph/add-lyrics-instagram-reels/ ; https://www.socialmediatoday.com/news/instagram-adds-song-lyrics-display-reels-clips/698697/ ; https://hypebeast.com/2026/6/instagram-edits-app-adds-beat-markers-and-ai-tools ; https://embedsocial.com/blog/new-instagram-features-2026/ ; https://www.socialchamp.com/blog/instagram-edits/ .
Songs and charts: https://jordanbrittley.com/blog/trending-songs-on-instagram-reels-today (Nov 12 2026); https://newengen.com/insights/instagram-trends/ (Nov 20 2026); https://later.com/blog/instagram-reels-trends/ ; https://tokchart.com/tiktok-trending-sounds/united-states ; BPM: https://getsongbpm.com/song/time/3l8G9 , https://songbpm.com/@pink-floyd/time , https://www.hooktheory.com/theorytab/view/justice/flower-in-a-hurricane-feat-tame-impala-sza-and-king-gizzard-the-lizard-wizard , https://www.hooktheory.com/theorytab/view/tate-mcrae/housewife , https://www.hooktheory.com/theorytab/view/harry-styles/coming-up-roses , https://songbpm.com/@the-long-faces/jane , https://tunebat.com/Info/Somewhere-I-Belong-Linkin-Park/3agtg0x11wPvLIWkYR39nZ , https://en.wikipedia.org/wiki/Jane! . Measured tempos and downbeat grids: librosa 1.0.1 on the official YouTube audio (scratch files, not kept).
