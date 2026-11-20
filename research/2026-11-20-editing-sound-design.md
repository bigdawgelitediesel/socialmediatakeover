# Sound design and music for @elcoyotediesel Reels
Research date: 2026-11-20. Lane: sound design and music for short-form.
Context: Claude renders with ffmpeg 9.0.2 (full build, verified filters below); the song is added inside Instagram, so the file we hand over carries dialogue, ambience and SFX only and has to sound finished on its own AND under an IG song.

## 1. What the four transcripts actually teach

Herman Huang, "3 Sound Design Secrets That Feel Like CHEATING" (https://www.youtube.com/watch?v=tzfzkTAQsnE)
- Layer by frequency, not by quantity. A single whoosh reads thin on a big move. Stack a low whoosh (weight), a mid whoosh (body) and an airy high whoosh (speed). Same rule for impacts: sub thump + mid knock + high click/transient.
- Carve a pocket for dialogue. Instead of just turning music down, EQ a mid dip (roughly 1 to 4 kHz) into the music so the voice sits in it. He uses a de-esser on the music track as a cheap dynamic mid-cut. In our stack that is adynamicequalizer or a static equalizer dip on the bed.
- Commit to one SFX style per video. Random packs make a cut feel amateur; gritty mechanical hits for a diesel shop, not clean bell dings.
- Emotional realism: replace literal sounds with sounds that say what the moment means (coffee grounds became iceberg cracks). For Rival: a torch strike can become a riser, a bolt drop can become a sub thump.
- Getting into and out of a song: reverse the first beat (or the tail) to make a riser; to end early, cut before a downbeat and put reverb (Great Hall preset) on the final hit; layer a riser/suckback underneath the entry and an impact on the exit. This matters for us at the hook and at the last frame even though IG mixes the song, because our SFX layer is what makes the song entry feel designed.

Tim Runia, "The ONLY 3 Sound Effects You Need" (https://www.youtube.com/watch?v=JOm_EqBoW0M)
- Whoosh = motion (direction, speed, weight). Use on camera moves, subjects crossing frame, and between shots so two cuts feel like one continuous moment. Heavy/slow whoosh for big objects near camera; light/high whoosh for fast or fun; whip for snap-zooms; wind whoosh for drone/aerial floats.
- Riser = tension. Low bass rumble riser (felt, not heard) as a foundation, cymbal/noise riser on top for urgency. Riser into a smash cut to silence hits hardest.
- Impact = emphasis. Deep trailer-style with long tail for section changes and title cards; sharp short knocks for physical contact. His favorite: music drops out and the deep hit lands exactly as the new shot appears.
- Clicks = snappy sequences: three or four related shots, each landing on a click.
- Combos: riser into impact (reveal), rumble riser + cymbal riser (before the smash), whoosh into impact (make one cut stand out).

Wonderful Ida, Instagram Edits beat markers (https://www.youtube.com/watch?v=-Um6G1t3IX8) and Filmora beat edits (https://www.youtube.com/watch?v=laFsFblwdn8)
- Edits: add song, tap Beats, yellow dots appear on the beats, put the playhead on a dot, split, delete the excess, repeat; the dot snaps when the clip edge lines up. Filmora: beat detection, then "beat options = 2" to mark every second beat, then fit speed ramps so a clip starts and ends on markers. The lesson for us: cut on every 2nd or 4th beat, not every beat, and speed-ramp inside the slot so the action lands on the marker.

## 2. Sound grammar for a reel (web findings)

Timing relative to the cut
- Whoosh straddles the cut: starts 2 to 3 frames (roughly 70 to 100 ms) before the picture change, peaks on the cut, tails after. If the peak lands after the cut it feels reactive instead of driving. Length should match the move, about 400 to 500 ms for a half-second transition. (Zella https://zellahq.com/blog/sound-design-at-cuts-whoosh-impact-riser/ ; Freevisuals https://www.freevisuals.net/item/free-whoosh-transition-sfx-pack-5-transition-sound-effects ; Epidemic https://www.epidemicsound.com/sound-effects/playlists/transitions/)
- Impact lands on the exact frame the picture changes or the title appears. Zella: "even 50 ms early reads as sloppy." Trailer editors sometimes nudge a hit 1 to 2 frames early so the attack is felt on the frame. (Violet Recording https://violetrecording.com/sound-design-for-trailers/ ; Krotos https://www.krotosaudio.com/trailer-sound-design-tips-tricks/)
- Riser starts about 1 s before the key moment (0.75 to 1.5 s in practice), swells, and STOPS HARD on the moment; the hard stop is part of the effect. Trailer cues run 1 to 5 s. A 1 to 3 frame gap of near-silence before the final hit makes it feel twice as big.
- Sub drop under a title card is felt not heard; keep it short (0.5 to 1 s) and high-pass everything else so the sub has room.
- J-cut (sound before picture): start the next shot's audio 100 to 500 ms before its picture, with a short crossfade; never more than a second or two in short-form or the viewer loses place. Protect the sound track and move the picture cut around it. (Wikipedia https://en.wikipedia.org/wiki/J_cut ; cutfa.st https://cutfa.st/en/blog/j-cut-l-cut-audio-transition-editing-cutfast-method-2026 ; ZOOOP https://zooop.ai/glossary/editing/j-cut)
- Density: do not sound every cut. In a reel cutting every 1 to 2 s, sound only section changes, punch-ins, reveals and text hits, or it turns into a percussion track. Mismatched energy is worse than silence: soft whoosh on a dissolve, sharp whip on a snap zoom, impact on a hard cut to a claim.
- Levels: SFX about 6 dB under the voice. If the viewer consciously hears the whoosh it is too loud. Room tone or shop ambience bed 25 to 30 dB under voice and continuous under every cut so the hard cuts stop "popping." Fill DJI silent clips with the shop bed so there is never digital silence except as a deliberate pre-hit gap.

Dialogue cleanup chain (order matters)
High-pass 80 to 100 Hz, then denoise, then de-ess (5 to 8 kHz, 2 to 6 dB), then compression about 3:1, then a limiter at -1 to -2 dBTP; level the VOICE first and build the rest under it. Speech alone targets around -16 LUFS; the finished program -14 LUFS. (Evan Schiff https://www.evanschiff.com/articles/quick-and-easy-dialogue-cleanup/ ; jvid chain https://github.com/jarradbanks/jvid/pull/389 ; Shotcut guide https://simpleclean.app/blog/remove-background-noise-in-shotcut ; sprites https://www.sprites.ai/claude-video-editing/audio-cleanup)

Ducking (for the GUIDE render and for any ambience/SFX bed under speech)
Threshold does most of the work, ratio about 4:1 to 8:1, attack 5 to 20 ms, release 300 to 500 ms, soft knee, no makeup gain. DankDev measured ffmpeg sidechaincompress: defaults duck only 5.6 dB; threshold=0.05:ratio=8:attack=10:release=400 ducked 17 dB; a quieter voice ducks less, so normalize the voice before it keys the compressor. (https://www.dankdev.com/Blog/ffmpeg-duck-music-under-voice ; ffmpeglab https://www.ffmpeglab.com/articles/ffmpeg-sidechain-compression.html ; Resolve Club https://davinciresolveclub.com/davinci-resolve-audio-ducking/)

Loudness for IG/TikTok
Community consensus is -14 LUFS integrated, -1 dBTP, and nobody has an official Meta number. Meta's own engineering post says xHE-AAC loudness management "brings the average loudness of all sessions to the same target level" using loudness metadata applied at PLAYBACK, with playback DRC chosen per listening environment, so mastering hot buys nothing and overly dynamic mixes get squashed by DRC. Check true peak after AAC encode, not on the WAV. (Meta https://engineering.fb.com/2023/04/11/video-engineering/high-quality-audio-xhe-aac-codec-meta/ ; https://mixingandmastering.ai/blog/lufs-for-tiktok-and-reels ; https://www.audio2time.com/audio-loudness-standards/ ; https://cutscore.io/blog/loudness-for-instagram-reels)

Instagram music on top of our file
IG gives two 0 to 100 sliders (original audio, song) at post time; cannot be changed after publishing. For talking reels the common guidance is song at 20 to 30 percent, original at 100. So our render must be the complete mix minus melody: dialogue cleaned, ambience bed, SFX, a sub/riser layer that does not clash tonally (noise-based risers, not pitched ones), no melodic bed that fights the song, and peaks at -1.5 dBTP so IG's summing does not clip. (Vista Social https://support.vistasocial.com/hc/en-us/articles/51949258945051-Adding-Trending-Audio-to-Instagram-Reels ; Hollyland https://www.hollyland.com/blog/tips/keep-original-audio-on-reels-with-music)

What makes truck content sound expensive
Build vehicle sound as stacks: body layer (engine weight, metal mass, road rumble) + detail layer (ticks, clinks, air hiss) + sweetener (metallic ring, turbo whistle). Speed is sold by friction (tires, air) not engine volume. High-pass SFX at 20 to 40 Hz so low-end junk does not eat headroom. Automate levels; a static bed sounds flat. (sfxengine https://sfxengine.com/blog/cinematic-sound-design-tips ; Krotos https://krotos.studio/blog/car-driving-sfx ; Pro Sound Effects / Mangini https://blog.prosoundeffects.com/car-sound-design-master-class-with-mark-mangini-video). For a 7.3 build: low idle rumble bed under hero shots, real impact-gun bursts as rhythmic hits, wrench-on-concrete clinks as "clicks," compressor air release as a riser, torch pop as an impact.

## 3. Beat detection and Instagram Edits

- Meta added beat markers to the Edits app in June 2026 (Social Media Today https://www.socialmediatoday.com/news/meta-adds-more-features-edits-app-beat-markers/748043/ ; Beebom https://beebom.com/instagram-edits-adds-beat-markers-editing-feature). Edits pulls the IG music library and posts to IG with the song attached, so it is the only path that gives beat-accurate cuts AND song-page linkage. Workflow: Claude renders the clean cut, Jacob opens it in Edits, adds the song, taps Beats, and nudges the handful of cuts that should land on dots.
- For Claude to pre-cut to the beat, we need a local copy of the song and the song start offset Jacob will use in IG. librosa is the practical choice: pip dry-run on this machine resolved librosa 1.0.1 and all deps as wheels for Python 3.12 (numba 0.68.1, soxr, soundfile), no compiler. aubio 0.4.9 is sdist-only and will not build. madmom from PyPI fails to build on 3.12; madmom-prebuilt 0.17.post1 installs as a wheel if we want the more accurate RNN tracker (its pretrained models are CC BY-NC-SA, fine for internal tooling, do not redistribute). Known librosa bias: beats land 20 to 60 ms late, so subtract about 30 ms or refine each beat to the nearest onset peak (librosa issue https://github.com/librosa/librosa/issues/1052 ; madmom accuracy https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2025.1595939/full).

## 4. Royalty-free SFX sources (commercial-safe)

- Pixabay: Pixabay Content License, commercial OK, no attribution, no standalone redistribution. Verified 172 pages for "impact wrench" including Pneumatic Impact Wrench Loosening Bolts (27 s) https://pixabay.com/sound-effects/city-pneumatic-impact-wrench-loosening-bolts-502995/ , Air Impact Wrench (6 s) https://pixabay.com/sound-effects/film-special-effects-air-impact-wrench-82141/ , Cinematic Impact Boom 05 https://pixabay.com/sound-effects/film-special-effects-cinematic-impact-boom-05-352465/ .
- Freesound filtered to CC0 (72 percent of the catalog is CC0): 41 CC0 hits for impact wrench, e.g. IMPACT WRENCH https://freesound.org/people/SamuelGremaud/sounds/458855/ , 1 Inch Impact Gun https://freesound.org/people/dudebrobrodude/sounds/466716/ , Air Impact Wrench 39 s https://freesound.org/people/sevenbsb/sounds/349398/ , Wrench on concrete floor 5 impacts (Bibow); CC0 Sub Drop https://freesound.org/people/Qvantor/sounds/879281/ , Subterranean Deep Sub-Bass Rumble Drop https://freesound.org/people/brktkrgll/sounds/856174/ . Always confirm the license on the sound page; CC BY needs a credit line, CC BY-NC is out.
- Mixkit: own license, commercial OK, no credit, no redistribution as stock.
- Soundly Free: Soundly's FAQ says Free and Pro library sounds are cleared for commercial use; its Freesound add-on is mixed, set it to CC0 only (https://getsoundly.com/faq/how-can-I-use-the-sounds/).
- Paid: Artlist SFX (one license, social included, downloads stay licensed), Epidemic SFX (commercial on Pro/Business tiers, must connect the channel). Herman Huang's pick: Happy Editing transition pack. Tim Runia: Story Sound Pack.
- CapCut: the general Sounds tab is NON-commercial; only the Commercial Sounds library is cleared, and only for TikTok/CapCut, not Instagram. Mixing one non-commercial CapCut sound into a project makes the whole thing personal-use only. Do not source SFX from CapCut for @elcoyotediesel (https://www.capcut.com/material-license-agreement).
- License comparisons: https://sonilo.com/blog/comparisons/best-free-sound-effects-sites-2026 ; https://swarmify.com/blog/free-sound-effects-websites/

## 5. IMPLEMENT IN OUR STACK

All chains below were run on this machine against ffmpeg 9.0.2 (full build) on 2026-11-20 and produced output; the mixed test measured -14.2 LUFS integrated after AAC encode. Verified filters present: highpass, afftdn, anlmdn, arnndn, deesser, acompressor, alimiter, speechnorm, dialoguenhance, agate, adynamicequalizer, asubboost, sidechaincompress, asplit, adelay, amix, afade, loudnorm, ebur128.

5a. Dialogue cleanup (iPhone shop audio), run per dialogue clip before the mix

    -af "highpass=f=90:poles=2,afftdn=nr=12:nf=-40:tn=1,deesser=i=0.3:m=0.5:f=0.6,acompressor=threshold=-20dB:ratio=3:attack=8:release=120:makeup=3dB:knee=4,alimiter=limit=-2dB:attack=5:release=50"

Notes: raise afftdn nr to 18 to 20 for compressor-cycling rooms, never past 25 or the voice goes underwater. For impact-gun bursts between words add agate=threshold=-35dB:ratio=4:attack=5:release=200 after afftdn. arnndn (RNNoise) is stronger on broadband shop noise but needs a model file: download e.g. sh.rnnn from https://github.com/GregorR/rnnoise-models and use arnndn=m=tools/models/sh.rnnn:mix=0.8 in place of afftdn. Then normalize the voice stem alone: loudnorm=I=-16:TP=-2:LRA=7 so it keys the ducker consistently.

5b. Mix graph (voice + ambience bed + SFX, ducked, to -14 LUFS)

    [0:a]asplit=2[vmix][vkey];
    [1:a]volume=-26dB,afade=t=in:d=0.5[amb];
    [amb][vkey]sidechaincompress=threshold=0.05:ratio=4:attack=10:release=400:knee=4[ambduck];
    [2:a]adelay=2000|2000,volume=-8dB[sfx1];
    [vmix][ambduck][sfx1]amix=inputs=3:duration=first:normalize=0,
    loudnorm=I=-14:TP=-1.5:LRA=11:linear=true,aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo

Two-pass loudnorm for VOD: first run with print_format=json to -f null, then feed measured_I / measured_TP / measured_LRA / measured_thresh / offset back in with linear=true (https://dev.to/masonwritescode/two-pass-loudness-normalization-with-ffmpeg-loudnorm-the-right-way-1nm3). For the GUIDE render with example music, duck the music with threshold=0.05:ratio=8:attack=10:release=400 and add a mid pocket: equalizer=f=2200:t=q:w=1.2:g=-4 on the music. Verify after encode: -af ebur128=peak=true -f null - and read I and Peak.

5c. SFX placement rules for build_reel2.py (add an "sfx" list to the EDL, each item {file, at, gain_db, kind})
- kind=whoosh: at = cut_time - 0.08 (2 to 3 frames early), gain -6 dB relative to voice (about -22 dBFS peak if voice is around -16), trim to 0.4 to 0.5 s with afade out.
- kind=impact: at = cut_time exactly (0 ms tolerance), 50 ms early acceptable for a title card, gain -4 to -6 dB, high-pass the rest of the bed during the hit.
- kind=riser: at = moment - 1.0 (0.75 to 1.5 s), afade in over its length, HARD STOP at the moment (atrim, no fade out), gain -10 dB rising to -6.
- kind=gap: insert 2 frames of silence in all beds immediately before a big impact (volume=0:enable='between(t,T-0.07,T)').
- kind=click: at = cut_time, -12 dB, for rapid 3 to 4 shot runs.
- Budget: max one sounded cut per 3 to 4 cuts; always sound the hook text hit, the reveal, and the last frame.
- J-cut: start the next clip's audio stream 0.15 to 0.3 s before its picture with acrossfade=d=0.15.
- Ambience bed: shop room tone or low idle rumble, continuous, -26 to -30 dB under voice, never digital silence except the gap rule.
- IG-ready file: no melodic bed, noise/sub based risers only, final TP -1.5, and tell Jacob "song slider 25, original 100" in the posting kit.

5d. Beat detection and snapping (Python 3.12, wheels only)

Install: "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" -m pip install librosa soundfile  (optional: madmom-prebuilt)

    import librosa, numpy as np
    y, sr = librosa.load(song_path, sr=22050, mono=True, offset=ig_start_s, duration=reel_len_s)
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr, units='time', tightness=100)
    onsets = librosa.onset.onset_detect(y=y, sr=sr, units='time', backtrack=True)
    # correct librosa's late bias: move each beat to the nearest onset within 60 ms, else shift 30 ms early
    fixed = []
    for b in beats:
        o = onsets[np.argmin(np.abs(onsets - b))]
        fixed.append(o if abs(o - b) < 0.06 else b - 0.03)
    grid = np.array(fixed)[::2]   # cut on every 2nd beat (every 4th for slow songs)
    def snap(t):
        return float(grid[np.argmin(np.abs(grid - t))])

Then for each EDL slot: new_dur = snap(cum_end) - cum_start, and let the slot's speed ramp absorb the difference so the action still lands on the marker. Write the beat times out as beats.csv and overlay tick marks on the contact sheet so the choice is visible. Use the song's exact IG start offset (ig_start_s) and put that number in the posting kit so Jacob scrubs the IG song picker to it. With madmom-prebuilt: from madmom.features.beats import RNNBeatProcessor, DBNBeatTrackingProcessor; beats = DBNBeatTrackingProcessor(fps=100)(RNNBeatProcessor()(song_path)).

5e. Starter SFX kit (download once into VIDEO/tools/sfx, name by kind)
1. whoosh_low_heavy.wav (Pixabay "cinematic whoosh deep")
2. whoosh_light_fast.wav (Pixabay "swish fast")
3. whip_snap.wav for snap zooms (Mixkit "fast whoosh")
4. wind_whoosh_long.wav for DJI floats (Freesound CC0 "wind whoosh")
5. riser_noise_1s.wav (Freesound CC0 "noise riser")
6. riser_sub_rumble_2s.wav (Freesound CC0 brktkrgll 856174)
7. impact_deep_tail.wav (Pixabay Cinematic Impact Boom 05, 352465)
8. impact_short_knock.wav (Pixabay Cinematic Impact Hit 03, 637243)
9. sub_drop_short.wav (Freesound CC0 Qvantor 879281)
10. click_shutter.wav and click_pen.wav (Mixkit UI clicks)
11. impact_gun_burst_short.wav (Pixabay 82141 or Freesound 458855)
12. impact_gun_long_run.wav (Pixabay 502995)
13. wrench_on_concrete_clinks.wav (Freesound CC0 Bibow "34 Wrench on concrete floor")
14. compressor_air_release.wav (Pixabay "air release hiss")
15. diesel_idle_rumble_bed_30s.wav and shop_room_tone_30s.wav: RECORD THESE at the shop on the iPhone, 30 s each, phone still, nobody talking. Nothing downloaded will match the room like the real room.

Layering recipe for the hero reveal: riser_sub_rumble + riser_noise (start at -1.0 s), then a 2-frame gap, then impact_deep_tail + sub_drop_short + impact_gun_burst_short on the frame.

## 6. Top 5 priorities

1. Fix the dialogue first. Run every iPhone talking clip through 5a and level the voice to -16 LUFS before anything else; clean speech is 80 percent of "produced."
2. Never ship digital silence. Record a shop room tone and a diesel idle bed, lay one under the whole reel at -26 to -30 dB, duck it under speech, and fill all DJI clips with it.
3. Add the three sounds at the right frames: riser 1 s before the reveal with a hard stop, impact on the exact frame of every hook text hit and reveal, whoosh 2 to 3 frames early on no more than one cut in four. Build this as an sfx list in build_reel2.py.
4. Loudness and headroom for IG: two-pass loudnorm to -14 LUFS, TP -1.5 after AAC, verify with ebur128, and include the IG slider settings (song 25, original 100) plus the song start offset in every posting-kit README.
5. Beat-match when a song is planned: pip install librosa (wheels verified), snap cuts to every 2nd beat with the 30 ms late-bias correction, and hand Jacob the start offset; for exact dot alignment he finishes in the Edits app with Beats on, which keeps the song-page link.
