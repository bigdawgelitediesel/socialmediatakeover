# El Coyote playbook addendum, 2026-11-21 (builds on the 2026-11-20 master playbook; nothing there is retired unless it says so here)

Jacob, Saturday morning: "use multiple agents to find live and up to date data and become the best at social media and editing... learn all of these edit techniques... build on what I've already been teaching you." Two hours, 20 agents, 7 reels he sent broken down frame by frame, about 25 reports, 40 more transcripts, 4 new tools and 24 new Remotion components. This file is the operating summary. Every claim below has a source file in this folder; read the source before arguing with the rule.

The one-paragraph read: the account's problem is not reach or hooks any more (Harley Trade fixed skip rate to 37.8 percent overnight); it is SENDS. Mosseri said it in his own words on Oct 23 ("sends per reach is what is particularly important for that unconnected reach"), our 600-clip TikTok measurement says the top-sending truck clips carry no ask at all, and Harley Trade got 1 share on 1,610 reach because it was about Jacob, not about the viewer's people. The editing level is now set by four accounts Jacob sent (nxtlvl, tenfoldmarc, ultra.skills, edita.visuals), and all four make their reels in code from word timestamps, which is exactly our stack. The kit now has their grammar. What it does not have yet is footage shot with moves, and that is still Jacob's half.

## 1. Rules added today (short form; sources in brackets)

### Sends (the growth rule) [share-engineering, live-pull, algorithm]
1. Write the caption's first line before the shot list, as the name of a person type ("your 7.3 brother", "the guy who told you to keep it stock"). No person type, no Reel: it is a Story.
2. No ask on screen or in the audio. Jacob's rule stands and the data agrees: measured 0.03 percent sends with a spoken "tag him", 2.4 percent with a truck and a caption. The send lives in the moment and in caption line 1. Pin a comment that repeats the person type.
3. The reel is about the viewer's people, not about Jacob. Narrowcasting: a DM is picked for the recipient.
4. Named-tribe news is the top-sharing build format in the niche this month ("3rd Gen Cummins owners, this one's for you" 2.25 percent; FASS's 2,078 hp 6.0 2.95 percent). Open by naming who it is for, deliver one fact.
5. The hater quote is the new title card (Stradman tease and reveal): the audience's objection on screen first, the answer in the back half, the countdown in the caption.
6. Grade every reel on sends per reach at 48 h: floor 1 percent, goal 2 percent. Under 1 percent on a build reel means the format (trigger, recipient) failed, not the footage. Skip rate target stays under 45 percent (breakout median), ours is already 30 to 38 on the good ones.
7. Trial Reels: four late-2026 guides say 200 followers for professional accounts. Jacob checks the composer; if the toggle is there, every build reel goes out as a Trial first with two caption first lines tested.
8. One topic per reel (Meta's Nov 11 classifier explainer): never a meme beat and a build update in one reel; truck or part visible on frame one.

### The menu reel (new format, from the four reels Jacob sent) [DfU2nIgt8XK, Def9pj5TWtA, DfcxCxTBVsw, Df3tIAzhB9h breakdowns; nxtlvl PIPELINE-STUDY; ui-card-style report]
9. Structure: hook grid or hook line, a HUD counter (3/9 dots or a bar) that never leaves, one item per 3.7 to 5.6 s (voiced) or exactly 1.2 s (silent list), each item = question, strike, card drop, 2 to 3 chips on the spoken words, sticker; one iris wipe; 1.6 to 2.6 s silent hold on the last frame. Nothing cuts; elements enter. New visual every 0.9 to 1.3 s.
10. Everything lands on a spoken word (words.json): card at the item name minus 0.12 s, chips on their nouns, strike 0.5 s after the question word. `tools/words_to_props.py` does this.
11. Timings (shipped values, not the bouncy doctrine): card drop 0.35 s back.out(1.7) from y+40 scale .92; chips 0.2 to 0.3 s back.out(3) staggered 0.14 s; strike bar scaleX 0.3 s power3.out; stamp 0.25 s power4.out from scale 2.4 rotate -20 to -8; count-up 0.6 to 0.9 s power3.out with tabular figures; iris 0.6 s grow + 0.6 s shrink; typewriter 0.09 to 0.12 s per letter.
12. One accent color, three jobs: the current sidebar item, the accent word, the hero number. Ours is tan (yellow only inside the LOUDER lockup).
13. The accent word in a caption phrase is the payoff noun, set in serif italic on a filled pill. Stays one per phrase.
14. A frame object as the stage (phone card, terminal window, clipboard, work order, portal page) lets the demo carry novelty while the face stays on screen and hides compositing seams.
15. For El Coyote: card-only menu reels at most one a week ("Every stock part leaving the F600", "17 parts on Project Rival"); the rest of the time the menu grammar rides on top of Jacob's footage. CommentGate only on a gated deliverable (parts list PDF), one post in four at most.

### The tenfoldmarc effect vocabulary [Def9pj5TWtA breakdown, tenfoldmarc DOSSIER, capcut report]
16. The matte sandwich is the whole trick: base video, back layer, person cutout (RVM, tools/matte.py), front layer. RivalReel already does this with `behind: true`. Nine of the 17 effects are "something behind him or an edge around him".
17. Ranked for a diesel build account: before/after wipe, zoom-through cut, HUD digital zoom, checklist first (ffmpeg or trivial); then headline wall, cover story masthead, phone mockup, pull-back reveal; vertigo once for a dramatic beat; chart grow for cost or followers; skip glass type, shatter, spotlight, paper cut as a weekly tool.
18. Behind-head word placement: top of the word at head_top minus 0.57 x font size; only the bottom 25 to 30 percent of the letters may be hidden or it reads as broken.
19. All 17 plus the Nov additions are now components or CapCut step lists (capcut report, feasibility table): 12 of 17 are solo jobs in free CapCut.

### Shooting (the half that is still Jacob's) [camera-hooks report, DcSq-WQR5at breakdown, diesel niche]
20. Every talking shot opens with a move: walk-in, head-up, top-down drop, side sit, sit back, close turn out, lens block, reach-in. Never a static face on frame 1. (Abigail Norman's five plus fourteen more, all solo with a phone or the Pocket 3.)
21. Pocket 3 on the fender, Face Auto-Detect on, record, walk in. One real move per reel the edit cannot fake (part orbit, tilt reveal, pull-out, foreground pan), three takes at three speeds.
22. Physical transitions between locations: hand wipe or object wipe by default, whip only when the camera moved, light block or bay door for time passing, same device all reel, exposure locked, cut on the covered frame.
23. Text when the hook is a claim, no text when the hook is a noise or a face: six of fourteen diesel winners this month had zero on-screen text. Cold starts and running diesels: real sound, no music, wide static then low static at the pipe.
24. Milestones go out raw within the hour (frame rolls, engine in, first fire), before any edited version.

### Sound [audio report, ultraskills DOSSIER part 2]
25. Jacob's voice only on published reels; Kokoro (tools/vo_scratch.py) is a script timer. If an AI voice is ever used, the Add AI label toggle is mandatory.
26. One breath per card: 8 to 12 words, 3 to 4.5 s per card; 150 to 165 wpm; hook claim in 15 words inside 5 s.
27. SFX budget two or three per reel, tied to objects not cuts: card in, stamp, DM notify; UI pops 10 to 14 dB under voice, hits 6 to 8 dB under; CC0 only (Kenney, sfxmint, Real SFX set, Earshot for custom). tools/sfx-kit and tools/sfx_place.py (peaks: whoosh 2 frames before the cut, hit on the frame, riser ends on the hit).
28. Song in-app always (song page, trending arrow); voice-first reels can run the song at 1 percent to keep the page. About half of views are muted: every number and claim is typed on screen.
29. This week's format sounds: Time (then and now), Flower In A Hurricane (cinematic truck roll), Coming Up Roses (2026 recap), Last Christmas instrumental (Dear Santa parts list), Stop the Wedding (meme slot). Meme clips never under a build reel.

### Series [build-series report, section 5]
30. Project Rival is a numbered series held together by format, not by a platform feature (Instagram removed linked series Oct 28): the MEGANTE lockup with `PROJECT RIVAL · EP N` in the sub line is the only burned-in text, cold-open on the finished change, one recap line, one callback, one number, the problem in the last 1.5 s, caption line 1 = share line. Seasons end with the build phase (S1 long block). Cover = the lockup frame so the grid is the episode guide.
31. Sponsor episodes: the part is the payoff of a real episode, brand spoken not burned in, Collab invite (sponsored Collab reels run 1.52x views in Virev's data), thank-you as a Story, never a thank-you reel.

### Profile [profile-conversion report]
32. Name field `Jake Dalton | 7.3 Diesel Builds`; bio line 1 "Building a 1959 Ford F600 on a 7.3 Powerstroke", then "Road to SEMA 2027. New update every week", "Memes between the wrenching", "Cheyenne WY. Partners below"; drop the Elite Diesel line (F600 is El Coyote only). Link 1 the portal, link 2 partners.
33. Pins: Harley Trade, "Why companies hate your truck", and a rotating newest Rival episode. Unpin the October memes. Highlights RIVAL, PARTS, CHIEF, JAKE.
34. Every reel gets a chosen cover with a 3 to 4 word title in the middle band; seven of seven growing build accounts carry text on every tile and our grid has none. Pin a first comment naming the series and the next part, no "follow".

### Finishing and handoff [capcut report]
35. Hand Jacob `-EDIT.mp4` (crf 14, 30M cap) as the editing master plus `.srt`, the alpha `-cutout.webm` with a green fallback, full-frame `ov-*.png` overlays and a `-graphics.webm`; POST goes straight to Photos when no edit is needed. Export from CapCut at 1080p30 H.264 16,000 kbps, from Edits via Share to Instagram, never download and re-upload.

### Tutorial lane additions already folded in [editing-tutorials-fresh, section 4]
36. Silence cut padding 30 ms lead / 60 ms tail snapped to RMS troughs; graphics that follow a jump cut start 5 frames before it; readability floor 0.3 s per word + 0.6 s; word-rise-with-blur as the default caption pop in the Remotion tier; dim and blur the plate under any UI card; cards and pills default to 0.75 of the first-draft size, text never under 40 px; audio hooks (sound-first, mid-sentence start, silence drop) added to the hook templates.

### Added after the first write (same morning)
37. **Cross-posting (crossposting-decision report):** mirror the clean master (no app logo, no song) to TikTok (1 to 2 a day, not 4) and YouTube Shorts (everything, searchable noun titles on sound clips) through Buffer Free; flip Instagram's "Recommend on Facebook" toggle (rural men 50 to 64 are on Facebook at 71 percent vs 31 on TikTok); skip Threads video and Spotlight. About 3 minutes per reel.
38. **Comment gates (comment-gate-deliverables report):** nobody in the diesel niche runs them (0 of about 1,900 recent posts across 61 accounts), so it is an open lane and an untrained audience. Hand-send with a Saved Reply for the first two, Business Suite native Comment to Message as backstop (5 exact keywords, 15 minute delay), every file also at a public portal URL (Meta's spam policy: the comment buys delivery, not access). First deliverable: the RIVAL parts list from site/parts.json.
39. **Calendar (trend-calendar-30d):** Black Friday Nov 27 (Move Bumpers 20 percent, Driven Diesel sale Nov 23 to Dec 6), Spotify Wrapped day about Dec 2 ("Rival Wrapped" cards, no Spotify marks), block ship day and machine-shop numbers jump the queue, PRI Dec 10 to 12 (partner booth clips by phone ask, not a flight), Cheyenne Christmas Parade Nov 28, solstice "316 days" Dec 21. GTA 6 meme window closes about Dec 1. Amazon affiliate tags are not usable under about 1,000 followers.
40. **THE BAR weekly (the-bar-weekly/WEEKLY.md, repeat every week):** justyn.ai 247K (he now auto-posts hook variants as Trial Reels and keeps the winner), viashaan 57K, chandlerintelligence 105K with nothing new since Nov 20. New justyn devices: trial tray, A/B results table with a WINNER badge, variant quad, hook-swap timeline, app jiggle delete. viashaan's nine ANIMATE styles exist as a public repo (being read by the effect-repos agent).
41. **Sound tooling landed:** tools/sfx-kit (16 CC0 slots, 4 Earshot customs), tools/sfx_place.py (whoosh peaks 2 frames before the cut, hits on the frame, riser ends on the hit, measured to 0.03 frames), tools/sfx_lint.py; tools/vo_scratch.py (Kokoro am_michael, two takes per line, Whisper pick, pacing report; about a minute per script); tools/words_to_props.py (cue words to props, lint, sfx events). The whole chain ran on "Every stock part leaving this 7.3" (research/reel-references/2026-11-21-stock-parts-dry-run): script to voice to props to a 42.7 s render in under five minutes of machine time.
42. **Partners repost by accepting Collab invites, not by cold reposting (partner-repostability report):** 60 of 228 tiles across 19 brand grids are creator-authored (Derale 75 percent, Power Hungry 67). Jacob already has a live Collab on @issproofficial and @powerhungryperformance from the Nov 19 reel (407 views, 74.7 percent skip): Collab multiplies a reel that works, it does not rescue a thank-you selfie. Correct handles: @strictly_diesel (not @drivendiesel, a Nevada shop), @issproofficial, @iidiesel, @bd_performancemanufacturing, @dieselarmymagazine, aggregator @dieseltrucking (1.4M). 1.52x is all Collabs; sponsored Collabs run 1.00x vs 0.78x solo. Partner kit spec (12 files, paste caption, rights line) is in the report.

## 2. What was built today (all in VIDEO/tools, snapshot in research/tools-snapshot)

- `rival-reels/src/components/anim.ts`: backOut(s), expoOut, power4Out, power2In, steps(n), popSoft, sf.
- `rival-reels/src/components/Menu.tsx` (13): ProgressHud, SidebarList, PhoneStage, CountUp, StrikeStamp, ItemCard, Headline, GhostWord, IrisWipe, NegativeFlash, CommentGate, QuadWall, Checklist.
- `rival-reels/src/components/Effects.tsx` (11): WallBehind, Masthead, FrameBreak, Vertigo, BgReplace, ChartGrow, PullBackWindow, ZoomThrough, HudZoom, BeforeAfter, BlurWord.
- `rival-reels/src/CardReel.tsx`: plate-free composition (bg color / paper / still / blurred video, durationSec, same overlay schema). RivalReel now passes `plate` and `cutout` to every overlay.
- Tested: menu-test (14 s, 23 s render), fx-test and fb-test on the Driven plate + cutout (frames in research/reel-references/2026-11-21-menu-kit-test/).
- In progress by build agents at the time of writing (see their READMEs when they land): `tools/words_to_props.py` + specs/menu-reel-example.json (word-timestamp generator and lint), `tools/vo_scratch.py` + venv-voice (Kokoro scratch voice with words.json), `tools/sfx-kit` + `tools/sfx_place.py` + Earshot customs.

## 3. Reference library added today (research/reel-references/)

2026-11-21-DfU2nIgt8XK (nxtlvl 9 apps), 2026-11-21-nxtlvl-profile (dossier), 2026-11-21-nxtlvl-repo (their public pipeline, PIPELINE-STUDY.md; the clone is git-ignored), 2026-11-21-Def9pj5TWtA (tenfoldmarc 17 effects, per-effect frame strips), 2026-11-21-tenfoldmarc-profile (dossier, 50-effect glossary, 16 mirrors), 2026-11-21-DfcxCxTBVsw and 2026-11-21-DfII6u2Nl_p (ultra.skills), 2026-11-21-ultraskills-profile (dossier + sound tools), 2026-11-21-DcSq-WQR5at (visual hooks), 2026-11-21-Dfu1v5SRJzx (Hind camera moves, cover only), 2026-11-21-Df3tIAzhB9h (edita quad wall), 2026-11-21-edita-visuals-profile, 2026-11-21-diesel-niche-winners (14 clips), 2026-11-21-ui-card-style (7 clips), 2026-11-21-own-reels-compare (Harley Trade at 17 h), 2026-11-21-menu-kit-test, 2026-11-21-the-bar-weekly (in progress).

## 4. Reports added today (research/)

2026-11-21-live-instagram-algorithm.md, -share-engineering.md, -editing-tutorials-fresh.md, -ui-card-style-and-remotion-recipes.md, -audio-trends-and-voice.md, -build-series-structure.md, -profile-conversion.md, -camera-hooks-and-moves.md, -capcut-edits-finishing.md, -trend-calendar-30d.md (in progress), -comment-gate-deliverables.md (in progress); analysis/2026-11-21-live-pull-20-posts.md.

## 5. Corrections to older notes

- CLAUDE.md "instagram.com is dead for fetchers": profile pages fetch again logged out (name, bio, follower count, highlights, first 12 tiles with alt text). Reel pages are still login-walled, but yt-dlp downloads public reels and the `/p/<id>/` crawler page gives og meta.
- CLAUDE.md and the content plan "Trial Reels locked until 1,000": unconfirmed; may be 200 for professional accounts. Verify in the composer.
- 2026-11-20 hooks lane "burned-in share line plus small series tag": superseded by Jacob's rule (no on-screen CTA); the share line is caption line 1, the series tag is inside the lockup sub line.
- Own note from this morning on Harley Trade (bigger on-screen ask): withdrawn the same hour for the same reason.

## 6. Next
1. Jacob: check the Trial Reel toggle, apply the profile spec, shoot the five openers once each on the Pocket 3 so the kit has moving footage to ride.
2. First menu reel: "Every stock part leaving the F600" from words_to_props on Jacob's own voice (Kokoro for the timing pass only).
3. Sunday 11-22 afternoon: 48 h read on Harley Trade and the Dougie reel; sends per reach is the grade.
4. Weekly: re-pull THE BAR accounts (the-bar-weekly format), re-pull the trending audio Monday, update the trend calendar.
