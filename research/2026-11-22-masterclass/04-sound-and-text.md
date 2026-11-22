# Clusters E and F: sound, and text on screen (questions 22 to 26)

Written 2026-11-22 for the masterclass run. Method: WebSearch standard then extended, 16 searches before the shared search budget ran out; WebFetch and curl failed on engineering.fb.com and socialmediatoday.com (hosts not allowed in this session), so Meta's xHE-AAC post is cited from search snippets and the Social Media Today write-up, not from the page itself. Repo evidence is the caption audit (`research/reel-references/2026-11-21-caption-audit/`, 55 reels measured at 1080x1920) and the Mariah and Caleb Ralston breakdowns (`2026-11-22-Derd9IvoWaj`, `2026-11-22-De11arZobPL`, `2026-11-22-DdmJNQJp81s`).

## At a glance

| Q | Claim in circulation | What holds up | Grade of the best evidence |
|---|---|---|---|
| 22 | "Instagram normalises to -14 LUFS" | Meta normalises at the player via xHE-AAC loudness management; the target is unpublished; -14 integrated, -1 dBTP is the safe delivery and a quiet file is not harmed | measured (first party) for the mechanism, folklore for the number |
| 22 | "Music 12 to 18 dB under voice, duck 6 to 12 dB" | Consistent practitioner band, no retention data; the one-take winners this week run no bed at all | practitioner |
| 22 | "Silence kills retention" | Unplaced gaps over about 0.4 s are swipe points; one placed beat after the turn is the device | folklore with a useful distinction |
| 23 | "Whooshes and risers lift retention" | No measurement anywhere; documented 2025 to 2026 backlash; the three measured winners are SFX-free | practitioner against, measured counterexamples |
| 24 | "85 percent of video is watched muted" | Digiday 2016, publisher self-report, Facebook feed, 3 s views; not a study | traced origin |
| 24 | "80 percent more likely to finish with captions" | Verizon and Publicis 2019 survey, stated preference, "watch an entire video"; 69 percent muted in public, 25 percent in private | measured (survey) |
| 24 | "Captions raise completion on Reels" | Instagram says one third of plays are muted; Facebook's 2016 ad test measured +12 percent view time; nothing isolates face reels | measured (first party, old) |
| 25 | "Karaoke captions beat phrase captions by 15 to 34 percent" | Vendor-run tests, no method; the academic single-word result is negative; every slow-edit winner uses 2 to 4 word plain phrases | measured against, folklore for |
| 26 | "Safe zone is the bottom 250 px" | Meta ads: 14 / 35 / 6 percent = 269 / 672 / 65 px; organic checkers disagree; winners keep caption bottom above y 1400 and the right 130 px clear | measured (ad spec and repo audit) |
| 26 | "The grid crops 9:16 to 4:5" | Tiles are 3:4 since January 2025: 1080x1440 shown, 240 px lost top and bottom on a centred crop | measured (tile size) |

Grades: **measured** = a number somebody actually measured and published with method; **practitioner** = a working editor or platform says so without data; **folklore** = repeated by vendors with no traceable source. Vendor blogs that sell caption or loudness tools are marked (vendor).

---

## 22. Voice loudness, music under voice, room tone, silence, and what Instagram does to the file

**Answer.** Nobody outside Meta has published a verified Instagram loudness target. The only first-party statement is Meta's April 2023 engineering post on xHE-AAC, which says uploads arrive "ranging from silence to full scale" and that the codec's built-in loudness management (MPEG-D DRC metadata read by the player) is used on Reels and Stories to give consistent volume between swipes; that is a player-side normalisation, so a quiet or a hot file both end up near the same perceived level and the loud file loses its transients to the limiter first. Third-party guides disagree on the target (-16, -14, or -10 to -12 LUFS) and none cites Meta or TikTok documentation; TikTok publishes nothing. The practical consequence is the same across every source: deliver the voice at about -14 LUFS integrated with a -1 dBTP ceiling, a -16 upload is safe (it is turned up or left alone, never damaged) and a -10 upload gains nothing and gets squashed. For music under voice, working guides cluster at 12 to 18 dB below the voice with a 6 to 12 dB duck when both play, judged by ear on a phone speaker; Jacob adds the song inside Instagram, so the mix happens on Instagram's percentage slider, not in the NLE, and has to be checked in the app preview. Silence is a device only when it is placed (a beat after the reveal); unplaced gaps over about 0.4 s are where viewers swipe, and the measured winners this week (Mariah, Ralston) run voice only, no bed, with real room tone under the cuts so the jump cuts do not click.

**Sources.**
- Meta Engineering, "Improving audio quality with xHE-AAC" (Apr 2023). https://engineering.fb.com/2023/04/11/video-engineering/high-quality-audio-xhe-aac-codec-meta/ . Deployed on Facebook and Instagram Reels and Stories; has a "Loudness management" section; receives audio from silence to full scale. Grade: measured (first party), target number not visible in snippets.
- Social Media Today write-up of the same post. https://www.socialmediatoday.com/news/meta-updates-audio-encoding-for-reels-and-stories-to-provide-more-volume-co/647414 . "More volume consistency" between Reels and Stories. Grade: practitioner (press).
- Opus Pro, "10 Best Loudness Normalizers for Social Video" (vendor). https://opus.pro/blog/best-loudness-normalizers . Lists Instagram and TikTok at -10 to -12 LUFS, Facebook -13; no source. Grade: folklore.
- Cutscore, "What loudness should Instagram Reels be" (vendor). https://cutscore.io/blog/loudness-for-instagram-reels . -14 LUFS, says Instagram "pushes down hard" above it; notes Instagram has no official rule. Grade: practitioner.
- Cloudfront loudness page, "Integrated Loudness -16 LUFS" (vendor). https://d1lex0gkhzvix9.cloudfront.net/tiktok-instagram-reels-loudness . Says both apps normalise, target "around -16". Grade: folklore.
- Dev.to, "Mastering for Reels, TikTok and Shorts: the LUFS -14 standard". https://dev.to/arthurvalle1_a2586dd2b4bc/mastering-for-reels-tiktok-and-youtube-shorts-the-lufs-14-standard-2ck5 . -14 integrated, -1 dBTP, LRA 5 to 8. Grade: practitioner.
- Spotify loudness normalisation (the likely origin of the -14 number everybody copies). https://support.spotify.com/au/artists/article/loudness-normalization/ . -14 LUFS, -1 dBTP; official but for Spotify only. Grade: measured (first party, wrong platform).
- AudioForgePro, "Reels metallic sound bug" (vendor). https://audioforgepro.com/blog/instagram-reels-metallic-sound-bug-wav-files-sound-bad . Anecdote that hot or odd-format uploads come back tinny. Grade: folklore.
- Mubert auto-duck docs and Typecast ducking guide (vendor). https://mubert.com/tools/cast/docs/auto-ducking.md and https://typecast.ai/learn/?p=14829 . Duck 6 to 12 dB, attack 30 to 80 ms, release 250 to 700 ms; over-ducking (15 to 20 dB per line) is heard as automation. Grade: practitioner.
- Freepik, "Auto Ducking in Premiere Pro" and Adobe community thread. https://www.freepik.com/blog/how-to-use-auto-ducking-in-premiere-pro-for-clean-professional-audio and https://community.adobe.com/t5/premiere-pro-discussions/help-with-audio-settings-for-voice-over-and-music/m-p/12039105 . -12 dB subtle, -18 dB noticeable; one editor sits music 12 dB under voice. Grade: practitioner.
- Storyblocks, "How to balance audio in Premiere Pro". https://www.storyblocks.com/resources/tutorials/how-to-balance-audio-premiere-pro . Dialogue peaks -6 to -12 dBFS for web. Grade: practitioner.
- Blitzcut, "Dead air kills watch time" (vendor). https://blitzcutai.com/blog/dead-air-kills-youtube-watch-time . Intentional pause after a reveal makes viewers lean in; dead air makes them check their phone; pauses over 0.4 s are swipe points (unsourced). Grade: folklore with a sensible distinction.
- Nemovideo, "Remove silence without choppy cuts" (vendor). https://www.nemovideo.com/blog/ai-video-editing/remove-silence-from-audio . 64 s talking head to 48 s with no lines removed; cover the jump with a 10 percent punch-in. Grade: practitioner.
- Repo: Mariah "Think Like an Editor" breakdown. `research/reel-references/2026-11-22-Derd9IvoWaj/BREAKDOWN.md` . 68 s, no music under the voice, eight notebook inserts, hard cut out. Grade: measured (frame by frame, n=1).
- Repo: Caleb Ralston 90-second brand reel. `research/reel-references/2026-11-22-DdmJNQJp81s/BREAKDOWN.md` . "Audio is his voice only." 19.6K likes. Grade: measured (n=1).
- Repo: addendum rule 23 and 36. `research/2026-11-21-PLAYBOOK-ADDENDUM.md` . Cold starts and running diesels: real sound, no music; silence-cut padding 30 ms lead, 60 ms tail snapped to RMS troughs. Grade: practitioner (house).

**Confidence:** medium on "deliver -14 LUFS, -1 dBTP, and a quiet file is safe" (every source agrees on the delivery number even though they disagree on the platform number); low on any claim about what Instagram's exact target is; medium on music 12 to 18 dB under voice (consistent practitioner band, no retention data); high that the one-take winners this week run voice only.

---

## 23. Sound design (whooshes, risers, SFX on text): retention lift or tell?

**Answer.** There is no measured retention study either way; every number offered for SFX ("effects in the first two seconds", "risers build anticipation") comes from vendors selling sound libraries or AI editors. What exists is a documented practitioner backlash in 2025 to 2026: editors describe shorts getting worse when every swipe and zoom gets its own whoosh, Mariah's 50K-like reel names "constant transitions, obnoxious sound effects, Cocomelon for grown-ups" as the AI-edit tell, and Mosseri's December 2025 memo (as reported) argues raw imperfect content is now proof a human made it. The no-SFX winners this week replaced sound design with a change the viewer can see or hear for free: Mariah's hand writing the point in a notebook cut in on the noun every 8 to 10 s, Ralston's countdown ring and one headline per rule, both with the voice as the only audio. Where an SFX still earns its place in a talking head it is a diegetic sound (the door, the key, the engine, the notebook page), not a library whoosh, and it is one per reel.

**Sources.**
- Nemovideo, "AI sound effect generator workflow for Shorts" (vendor, but candid). https://www.nemovideo.com/blog/ai-sound-effect-generator-short-videos . Solid shorts get worse when every move has a whoosh; stacked effects turn to mush on phone speakers. Grade: practitioner.
- Fish.audio, "Using sound effects for short-form content" (vendor, Feb 2026). https://fish.audio/blog/using-sound-effects-for-short-form-content . Avoid overused stock sounds; build a signature. Grade: folklore.
- Soundstripe, "What are cinematic riser sound effects" (vendor). https://www.soundstripe.com/blogs/what-are-cinematic-riser-sound-effects . Risers build anticipation; no data. Grade: folklore.
- Followr help, "Sound effects". https://help.followr.ai/en/articles/9504557-sound-effects . Claims retention when "placed strategically", no study. Grade: folklore.
- Social Media Examiner, "Short-form video visual effects" (Apr 2025). https://www.socialmediaexaminer.com/short-form-video-visual-effects-the-key-to-more-views-and-sales/ . Average social watch 1.7 s, put effects in the first two seconds. Grade: practitioner.
- Manychat, "2026 Instagram trends creators are actually doing". https://manychat.com/blog/instagram-trends-for-creators-2026/ . Minimally edited talking-head content, skip the fancy edits; cites Mosseri's Dec 2025 memo on raw content as proof of a human. Grade: practitioner.
- Opus Pro, "11 editing aesthetics dominating short-form in 2026" (vendor). https://www.opus.pro/blog/editing-aesthetics-dominating-short-form-2026 . Lists "talking-head static: just you, a camera, no cuts" and "no captions, no music, just the work" as live aesthetics. Grade: practitioner.
- Repo: Mariah breakdown (above). The reel that argues against SFX is itself SFX-free and outperformed her ad reels on Instagram. Grade: measured (n=1).
- Repo: Ralston breakdown (above). Voice only, new visual element every 1 to 3 s from headlines and a ring, zero sound design. Grade: measured (n=1).
- Repo: caption audit section 3. Ten of fourteen diesel winners burn no text; cold starts run real engine sound and nothing else. Grade: measured (n=14).

**Confidence:** medium. The absence of any measured lift after four searches, plus a visible practitioner reversal and three measured counterexamples this week, is enough to drop library SFX from the daily talking head; it is not enough to say SFX hurt in other formats (memes, montages), where the library is silent.

---

## 24. Burned captions: the "80 percent muted" claim, where it came from, what Instagram says now, and completion for a face reel

**Answer.** The 85 percent figure is a May 2016 Digiday article quoting publishers' own Facebook feed numbers (LittleThings 85 percent, Mic 85 percent of 30-second views, PopSugar 50 to 80 percent) in the era when Facebook autoplayed muted and counted a view at 3 seconds; TechCrunch and Tubefilter re-reported it as "a study", which it never was. The 80 percent figure is different: Verizon Media and Publicis Media, April 2019, 5,616 US adults, found 69 percent watch with sound off in public and 25 percent in private, and 80 percent said they are "more likely to watch an entire video" when captions are available; it is a stated preference, not measured completion. The only platform numbers are Facebook's own 2016 internal test (captioned video ads raised average view time 12 percent) and Instagram's accessibility blog, which says one third of video plays on Instagram are with the sound off and that auto captions became the default for creators in March 2022; Reels in the app play with sound on, so the Reels muted share is lower than the feed-era 85 percent and no 2024 to 2026 figure has been published. Nothing in the record isolates face-to-camera reels; the measured winners split by niche: all 17 talking-head creators in the audit burn captions, 10 of 14 diesel winners burn none, and every vendor number above 12 percent for a captions lift is unsourced.

**Sources.**
- Digiday, "85 percent of Facebook video is watched without sound" (May 2016). https://digiday.com/media/silent-world-facebook-video/ . Publisher-supplied numbers, 3-second view definition. Grade: practitioner (publisher self-report).
- Tubefilter re-report (May 2016). https://tubefilter.com/2016/05/17/85-percent-facebook-video-views-without-volume/ . "Surmises". Grade: folklore origin.
- TechCrunch, "strategies that win in a silent autoplay world" (Jun 2016). https://techcrunch.com/2016/06/14/facebook-content-and-brand-strategies-that-win-in-a-silent-auto-play-world . Calls it a study. Grade: folklore origin.
- Facebook Business, "Updated features for video ads" (Feb 2016). https://www.facebook.com/business/news/updated-features-for-video-ads . Internal test: captions raised view time 12 percent on average. Cited from memory of the announcement, matches 3Play's roundup; not re-fetched this session. Grade: measured (first party, ads, 2016).
- 3Play Media, "Verizon Media and Publicis Media find viewers want captions". https://www.3playmedia.com/blog/verizon-media-and-publicis-media-find-viewers-want-captions/ . 80 percent more likely to watch an entire video; 37 percent say captions make them turn sound on. Grade: measured (survey, stated preference).
- Next TV, "Mobile videos often watched without audio, study finds". https://www.nexttv.com/news/mobile-videos-often-watched-without-audio-study-finds . 69 percent public, 25 percent private. Grade: measured (survey).
- Streaming Media, "80 percent of caption users aren't hearing impaired". https://www.streamingmedia.com/Articles/News/Online-Video-News/80-of-Video-Caption-Users-Arent-Hearing-Impaired-Finds-Verizon-131860.aspx . Same study. Grade: measured (survey).
- TechRadar (Veed sponsored), sample size 5,616, 18 to 54. https://www.techradar.com/pro/why-you-need-to-add-subtitles-to-your-online-videos-and-its-not-just-because-69-percent-of-viewers-watch-on-mute . Grade: practitioner.
- Instagram, "Advancing accessibility on Instagram". https://about.instagram.com/blog/tips-and-tricks/advancing-accessibility-on-instagram . One third of video plays with sound off; auto captions default for creators from March 2022 (undated stat). Grade: measured (first party, undated).
- TechCrunch, "Instagram is rolling out auto-generated captions" (Mar 2022). https://techcrunch.com/2022/03/01/instagram-is-rolling-out-auto-generated-captions-for-videos/amp/ . Grade: practitioner (press).
- 9to5Mac, "Instagram Stories playing sound by default" (2022). https://9to5mac.com/2022/09/15/instagram-stories-sound/ . Reels play with sound on by default in app. Grade: practitioner (press).
- Kapwing, "Subtitle statistics" (vendor roundup). https://kapwing.com/resources/subtitle-statistics . Restates 80 percent as "more likely to finish", the common misquote. Grade: folklore.
- Clipspeed, Videocaptions.ai, Monty (vendors). https://www.clipspeed.ai/blog/ai-captions-increase-views.html , https://www.videocaptions.ai/blog/how-video-captions-increase-engagement , https://monty.fast/blog/auto-captions/ . 40 to 60 percent watch-time claims, no method. Grade: folklore.
- Repo: caption audit, section 3. `research/reel-references/2026-11-21-caption-audit/` . 17 of 20 talking-head creators caption; 4 of 14 diesel winners burn any text; FASS karaoke reel had the highest share rate of the diesel set. Grade: measured (n=55, selected not random).

**Confidence:** high on the provenance (both numbers are traced to their origin and both are misquoted); medium that captions help a face reel on Instagram (one first-party 12 percent test on ads, a one-third muted base, and every talking-head winner in the audit captions); low on any effect size above that.

---

## 25. Word-by-word karaoke versus phrase captions versus none

**Answer.** No controlled study isolates karaoke against phrase captions in short-form; the published vendor tests (FluxNote 80 videos, +34 percent for word-by-word colour emphasis; Blitzcut 15 percent completion gap; Clamper 15 to 25 percent) do not publish method and sell the feature they measured. The two academic results point the other way for anything dense: a 2023 arXiv study found synchronised word highlights helped comprehension in language learning, while an ACM study with Deaf and hard-of-hearing viewers found single-word presentation significantly worse than 6 and 12 word lines because it splits attention between the caption and the face. Practitioner commentary in 2026 says the Hormozi look is saturated and the move is "dynamic minimalism": plain white phrase captions, 2 to 4 words, no emoji, no colour flash, kept for the strongest lines. That is exactly what the measured slow-edit winners use: Mariah and Ralston both run plain small white phrase captions lower third, no accent, no stroke; across 17 talking-head creators in the audit, zero use per-word colour flashes and the per-word behaviours that survive are a dim-to-bright tint reveal and one payoff word popping larger under a line that stays.

**Sources.**
- FluxNote, "AI captions that improve watch time" (vendor). https://fluxnote.io/blog/ai-captions-that-improve-watch-time . 80-video test, word-by-word +34 percent, sentence pop-in +8 percent; matched for content, no raw data. Grade: practitioner, self-interested.
- Blitzcut, "Word-by-word vs full-sentence captions in 2026" (vendor). https://blitzcutai.com/blog/word-by-word-captions-vs-full-sentence-captions . 15 percent completion gap; admits methodology not published; says dense or technical material needs the full phrase. Grade: folklore.
- Clamper on Dev.to, "How AI caption styles affect watch time" (vendor). https://dev.to/clamper_ai/how-ai-caption-styles-affect-watch-time-and-engagement-409i . 15 to 25 percent, smaller on YouTube. Grade: folklore.
- NSF-hosted ACM paper on caption line length for Deaf and hard-of-hearing viewers. https://par.nsf.gov/servlets/purl/10253921 . 6 and 12 word lines preferred over single words; single words split attention. Grade: measured (academic, accessibility population).
- arXiv 2023 study on keyword highlights and time-synchronised captions (cited in the Blitzcut and Kompozy pages; direct link not retrieved). Synchronised highlighting improved comprehension for language learners. Grade: measured (academic, different task).
- Kompozy, "Video captions for retention". https://kompozy.io/how-to/video-captions-for-retention . Content-type split: word-by-word for punchy speech, phrase for demonstration. Grade: practitioner.
- Joyspace, "Alex Hormozi editing style: does it still work in 2026". https://joyspace.ai/hormozi-editing-style-2026-analysis . "Dynamic minimalism": keeps timing, drops emoji and colour. Grade: practitioner.
- Clipspeed, "11 caption styles ranked" (vendor). https://www.clipspeed.ai/blog/11-caption-styles-ranked-viral-performance-2026.html . Saturation risk in-niche; reserve the bold style for opinion content. Grade: folklore.
- Viralday, "6 Hormozi caption alternatives". https://viralday.app/en/blog/6-caption-styles-beyond-hormozi-that-retain-high-attention . Use captions as punchlines, not wall to wall. Grade: practitioner.
- Repo: Mariah and Ralston breakdowns (above). Plain white phrase captions, 2 to 4 words, lower third, no accent, no stroke. Grade: measured (n=2).
- Repo: caption audit, sections 3 and 5. Zero per-word colour flashes in 55 reels; cap height 44 to 58 px; 2 to 4 words; centre y about 1185; never on the face. Grade: measured (n=55).

**Confidence:** medium-high that phrase captions (2 to 4 words, plain white) are the right default for a talking head about parts and trucks: the only measured evidence that favours karaoke is vendor-run, the only academic result on single words is negative, and every slow-edit winner studied this week uses phrases. Low on any numeric lift either way.

---

## 26. Caption placement and size against the Reels UI; safe zones as measured now

**Answer.** Meta publishes safe-zone margins only for Reels ads: 14 percent top, 35 percent bottom, 6 percent each side, which on 1080x1920 is 269 px top, 672 px bottom, 65 px sides (768 px bottom when a disclaimer runs); nothing official exists for organic Reels, and the third-party checkers for organic disagree, with the right rail quoted from 90 px to 230 px and the bottom band from 250 px to 461 px, the bottom-right corner always the deepest because the action buttons stack there. The right rail is the one zone every source agrees on: the like, comment, share, save and audio stack occupies roughly the right 10 to 20 percent of the frame from about y 1000 down. The repo's own measurement of 55 winners is tighter than any checker: talking-head caption centres run 1050 to 1360 with the block bottom never below 1400, titles in the upper third at y 220 to 541, nothing in the right 130 px, and cap height 44 to 58 px (about 64 to 80 px font size in Poppins). For the grid, Instagram has shown 3:4 tiles since January 2025, so a 1080x1920 reel cover is shown as 1080x1440: 480 px of height is lost, 240 from the top and 240 from the bottom on a centred crop, which is adjustable in the cover picker but means any lockup must sit between y 240 and y 1680 to survive the profile grid.

**Sources.**
- Lilach Bullock, "Instagram Reels safe zone". https://www.lilachbullock.com/instagram-reels-safe-zone/ . Meta's 14 / 35 / 6 percent; 269 / 672 / 65 px; notes the Meta pages have moved. Grade: measured (Meta ad spec, second hand).
- Adnova, "Meta ad safe zones guide". https://adnova.ai/blogs/meta-ad-safe-zones-guide . Same percentages; 20 to 35 percent bottom range; disclaimer case 768 px. Grade: practitioner.
- Admake AI safe-zone checker. https://admakeai.com/free-tools/instagram-reels-safe-zone . Draws 269 / 672 / 65 by default, says nothing equivalent exists for organic. Grade: practitioner.
- Jon Loomer, "TikTok and Instagram Reels safe zone templates". https://www.jonloomer.com/tiktok-instagram-reels-safe-zones-templates/ . Overlay templates and Ads Manager yellow guardrail. Grade: practitioner.
- Reap, "Shorts, Reels and TikTok safe zones". https://reap.video/blog/short-form-video-safe-zones . Organic estimates: 211 px top, 461 px bottom, 65 px left, 173 px right. Grade: practitioner.
- Trymypost, "Reels safe zones and text placement 2026". https://www.trymypost.com/blog/instagram-reels-safe-zones-text-placement-2026 . Right 21 percent (230 px), bottom deepens on the right. Grade: practitioner.
- Kapwing Reels safe zone tool and Revid checker. https://www.kapwing.com/video-editor/instagram-reels/safe-zone and https://www.revid.ai/instagram-reels-safe-zone . 250 to 280 px bottom, 90 px right. Grade: practitioner.
- Hopper HQ, "Instagram Reel size in 2026". https://www.hopperhq.com/blog/instagram-reel-size/ . Grade: practitioner.
- Kapwing, "Instagram's new grid layout size and dimensions" and Buffer, "Instagram's grid just changed". https://www.kapwing.com/resources/instagrams-new-grid-layout-size-and-dimensions-2025/ and https://buffer.com/resources/instagram-grid/ . 3:4 tiles from January 2025; 1080x1440 preview for a 9:16 reel; 4:5 upload loses about 34 px per side. Grade: measured (tile dimensions), practitioner (dates).
- Blitzcut, "Best caption size for Instagram Reels 2026" (vendor). https://blitzcutai.com/blog/best-caption-size-instagram-reels-2026 . 60 to 75 px font, 48 px floor, two lines max, weight matters more than size. Grade: practitioner.
- Rev, "Best open caption font sizes for social". https://www.rev.com/blog/best-open-caption-font-sizes-for-videos-on-social-media . Grade: practitioner.
- Opus Pro, "Video caption design and placement" (vendor). https://www.opus.pro/blog/video-caption-design-placement . 32 characters per line, two lines. Grade: practitioner.
- Repo: caption audit, sections 3 to 5, and addendum rules 45 and 46. Measured caption centres 1048 to 1360, bottom floor 1400, right 130 px clear, cap 44 to 58 px, titles y 220 to 541; artboard tool draws 480 and 1440 safe lines. Grade: measured (n=55 at delivery resolution).

**Confidence:** high on the Meta ad percentages and the pixel arithmetic; high on the repo's measured caption window because it was measured on the winners at delivery scale; medium on organic rail and bottom numbers (the UI changes and the checkers disagree); medium on the grid crop (3:4 is confirmed, the exact crop offset depends on the cover picker).

---

## What it means for a one-man diesel creator filming a daily talking head in his truck cab

Every rule below is testable in Insights (skip rate, average watch) or by downloading the posted reel and measuring it.

1. **Deliver the voice at -14 LUFS integrated, true peak -1 dBTP, loudness range under 8 LU.** Measure in the NLE's loudness meter or `ffmpeg -af loudnorm=print_format=summary`. If the take lands at -16 leave it; never push past -12, Instagram's player-side management takes the gain back and keeps the squash. Test: download the posted reel once a week and confirm it comes back within 1 LU of a reference reel.
2. **Record the cab at least 1 s of room tone before the first word and after the last, every take,** and use it under every jump cut (30 ms lead, 60 ms tail, snapped to RMS troughs per addendum rule 36). This is what makes a cut sound like nothing happened; it costs nothing and needs no second person.
3. **Default is voice only.** No music bed on the daily talking head. When a song is wanted (memes, montages), add it inside Instagram per Jacob's rule and set the Instagram mixer so the music sits about 15 dB under the voice, which on the app's slider is roughly 15 to 25 percent against original audio at 100; check it on the phone speaker, not headphones, and if the words need effort the music is too loud.
4. **No library SFX.** No whoosh, riser, pop or typewriter click on text or cuts. The only allowed sounds beyond the voice are things in the cab or the shop (door, key, engine, a notebook page) and at most one per reel. Test over 10 reels: skip rate on voice-only versus the two SFX reels already posted.
5. **Silence is placed, not left.** One held beat (0.6 to 1.0 s) after the line that turns the story, nothing else over 0.4 s. Cut every other gap. Mark the beat in the script before filming so it is a choice on camera, not a rescue in the edit.
6. **Burn captions on every talking head.** One third of Instagram plays are muted, every talking-head winner studied captions, and the only first-party test (Facebook, 2016) measured +12 percent view time. Phrase captions, not karaoke: 2 to 4 words, 24 characters, one line, sentence case as spoken, zero gaps between groups, no per-word colour flash, no stroke, no pill.
7. **Caption size and position for 1080x1920:** Poppins SemiBold 68 px (cap height 47 px), range 64 to 80, never under 64; white, two-layer shadow (`0 3px 5px rgba(0,0,0,.65), 0 10px 28px rgba(0,0,0,.40)`); block centre y 1190 by default, allowed window 1050 to 1360 chosen from the chin line (block top at least 120 px below the chin), block bottom never below 1400, nothing inside the right 130 px. Readability floor 0.3 s per word plus 0.6 s.
8. **Accent sparingly.** At most three tan words per reel (the number, the part name, the punchline noun), same size, same line. Once per reel at most, the payoff word may drop in larger under the line. Nothing else moves.
9. **Title in the upper third only.** The one poster lockup or two-line question sits with its centre between y 300 and 540, on screen 2.5 to 4 s, never together with a caption group, never below the head. Keep the lockup between y 240 and y 1680 so the 3:4 grid tile (1080x1440 out of 1920) still shows it, and pick the cover frame from the lockup.
10. **Keep the ad-grade zones clear when a brand will repost:** top 269 px, bottom 672 px, sides 65 px. For Jacob's own reels the organic floor of 1400 is enough; for anything a partner will run as a Collab or boost, apply the 672 px bottom and check with `tools/artboard.py` before render.

Open items the search budget did not reach: the actual LUFS target inside Meta's xHE-AAC loudness management (fetch the engineering post when the host is allowed, or upload a -14 and a -20 test reel and measure both downloads); a 2024 to 2026 first-party figure for Reels watched muted; and a direct read of the ACM single-word captions paper.
