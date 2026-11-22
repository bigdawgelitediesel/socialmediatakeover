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
