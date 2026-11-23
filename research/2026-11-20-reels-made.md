# 2026-11-20: two reels built from the Rival footage

Account snapshot 2026-11-20 (API pull): 577 followers, 102 posts. Pattern unchanged: meme reels share (17 Nov "Yep" 11.3k views / 64 shares; 20 Nov "Safety Reminder" 1.3k / 23 shares), build and partner reels sit at 190 to 550 views with 0 to 1 shares. The two reels below put a shareable line inside held build footage, which the 12 Nov refresh named as the fix.

| Reel | Length | Audio | Hook (frame 1) | Share line | Status |
|---|---|---|---|---|---|
| Harley Trade (Part 1) | 18.5 s | original dialogue | "how much you pay for that truck?" | send this to the guy who made a worse trade | ready, post first |
| Lumber to SEMA (Part 2) | 27.6 s | silent | number hook | grandpa's truck line | SCRAPPED by Jacob 2026-11-20 ("I don't like it"), files deleted |

Files: Google Drive `My Drive/VIDEO/inbox/Harley Trade (Reel 1) - completed 2026-11-20` (final MP4, no-captions MP4 for CapCut, posting-kit README). Rule: one folder per finished reel in inbox, named `<name> - completed <date>`, nothing else.
Renderer: OneDrive `Desktop/VIDEO/tools/build_reel2.py` (xfade transitions, minterpolate slow motion, crop-expression punch-ins, vidstab, ASS karaoke captions from Whisper word timestamps, audio beds + loudnorm, `--captions-only` re-burn).

Research behind the choices: `2026-11-20-diesel-reels-trend-research.md`, `2026-11-20-instagram-ranking-and-capcut-recipe.md`, `2026-11-20-cross-platform-trend-scan.md`.

Measure after 48 h: share rate and skip rate per reel in Insights (target: skip under 40 percent, sends per reach over 1 percent). Whichever moves, post the next one in the same lane within two days.

## 2026-11-22: Find the gratitude (Relatable talking head, 64.6 s)

Source IMG_4282.MOV (iPhone HEVC HLG, 83 s, porch selfie, Thanksgiving-week gratitude), pulled from Jacob's Drive link and cut in the cloud session with ffmpeg because the PC was not attached. Cold open on "even if life is really hard right now" (55.3 to 68.35), then the Sunday reflection (0.5 to 22.45), the people (22.45 to 37.45), payoff on the build and the stress (68.6 to 83.1); the "I wanted to make a post" filler cut. HLG tone-mapped (zscale + mobius), four hard cuts with 1.00 / 1.06 punch-in alternation, voice chain (highpass 90, afftdn, 3:1, two-pass loudnorm) landing at -15.2 LUFS / -0.9 dBTP after AAC, constant 30 fps verified, bt709 tags verified. Text: one TROPI lockup "find the gratitude" (Shrikhand 96, taupe, top band, 0.13 to 3.0 s) and PlainCaption-spec captions (Poppins SemiBold 68, no stroke, shadow, 2 to 4 words, chest band). Export 1080x1920 crf 17 maxrate 16M, 132 MB.

Delivery: Drive folder "Find the gratitude - completed 2026-11-22" under the inbox holds the cover, the .ass and the posting kit; the two mp4s were over the 10 MB connector limit and went to Jacob as file cards to save into the folder. Caption line 1: "For whoever is heading into Thanksgiving week with more on the plate than they can carry." Slot: afternoon, Sunday or Monday, before the plan starts. Variable: a personal no-truck talking head in the afternoon slot. Pending read to add once live: `coyote.py pending add <media_id> "Find the gratitude" <posted_iso>`.

Honest note: handheld selfie with the face half out of frame at times and heavy "like" in the first 20 s; the cut hides most of it. Next talking heads should follow playbook/12 (dash mount, same seat, five takes).

## 2026-11-22, 48 h read: Harley Trade (Reel 1)

Read at 48.7 h (pull saved at data/instagram/pulls/2026-11-22T2255Z-media.json, logged by coyote.py grade): 2,219 views, 1,659 reach, 104 likes, 2 comments, 1 share, 4 saves, average watch 10.8 s of 18.5 (59 percent), skip 38.0. Sends per reach 0.06 percent, likes per reach 6.3 percent. Grade MISS on sends; it stalled between 17 h and 31 h (2,161 to 2,214 views) and added five views in the last 18 hours. Reading per the doctrine (section 16): the hook and the hold worked, the send line and the dead 3.5 s end hold did not, and the story was about Jacob's trade rather than the viewer's friend. Dougie (Reel 2) at 27 h: 344 views, 270 reach, skip 65.7, watch 5.3 s; its 48 h read is due Monday 13:00 MT and it is already under the 500-reach floor. Safety Reminder (meme, 11-20) is the week's only GOAL on sends at 2.22 percent on 1,036 reach.

## 2026-11-22: Find the gratitude v2 (40.4 s, one cut)

Recut of IMG_4282.MOV after the masterclass run, per research/2026-11-22-masterclass/08-our-own-work.md and the doctrine: opens on the people line at 15.60 ("in the right place at the right time with the right people"), one cut on the breath to 49.20 ("I really challenge you this week"), the turn, the stress owned, hard cut on "I'm grateful for that" at 82.60. No punch-in. Lockup 0.13 to 3.0 s, no captions under it, chest-band captions after (22 groups). Voice chain as v1, two-pass loudnorm to -14 / -1.0, landed -15.5 LUFS, -0.7 dBTP. Files: outbox/ (v2 POST THIS, alt no captions, cover, .ass, README - v2 recut notes.txt), delivered to Jacob as file cards. Build script: scratchpad cut-IMG_4282/v2/build3.py. Both versions exist; the doctrine's call is v2 first, v1 a week later as the long-hold test, graded on watch share and likes per reach.

## 2026-11-22, laptop: Find the gratitude, final (57.9 s, approved by Jake)

Rebuilt on the laptop in the motion-graphics kit (RivalReel over a streamline plate) after Jake rejected four passes: the streamline v2 reproduction ("terrible"), a 27 s zero-cut one-take that passed the doctrine ("you cut way too much out, I want the whole message in there"), the 82 s uncut take ("I do still need it under a minute"), then "keep it creative" and "grab attention right off the bat". Approved version: cold open on "even if life is really hard right now ... buried within those hard choices" (55.37 to 66.19), then the take in order (0.51 to 5.25, 7.13 to 14.11, 15.57 to 32.11, 49.13 to 55.39, 68.31 to 75.87, 77.71 to 82.45), six cuts on breaths. White kinetic hook "IF YOUR WEEK IS HEAVY" over the chest 0 to 2.9 s, plain captions, one tan word ("grateful"), a `checklist` card ticking Right place / Right time / Right people on the spoken words, a `pip` of the F600 (raw IMG_3856) on "doing the build". The earlier Drive folder contents (v1 kit, cover, .ass) were deleted at Jake's request. Lesson: on this account the whole message under a minute with cards on the words beats the shortest cut; tan accents wash out on bright footage. Drive folders are now `VIDEO\raw` and `VIDEO\finished`. Pending read to add once live.

Posted 2026-11-22 21:02 MT through the API at Jake's request ("post it on my instagram right now"), no song, outside the 16:00 to 19:00 slot: https://www.instagram.com/reel/DgEeb6YDxKI/ (media id 18133164190863833). 48 h read due Tue Nov 24 21:02 MT.

Taken down by Jake the same night: "the edit sucks, like the lighting ... the first shot is all washed out". Cause: streamline.py tone-mapped iPhone HLG with npl=100 mobius, which blew out a direct-sun selfie. Fixed in the tool (npl=203, hable) and the cut re-rendered. Pending reads for media 18133164190863833 removed. Jake posts the corrected file himself.
