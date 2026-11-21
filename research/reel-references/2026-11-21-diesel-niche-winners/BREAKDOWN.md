# Diesel / truck-build niche winners, Oct 20 to Nov 21 2026: how the reels are made

Research agent report, 2026-11-21, for @elcoyotediesel / Project Rival. Builds on `research/2026-11-20-diesel-reels-trend-research.md` (platform rules, audio, cross-niche formats) and does not repeat it. This file is about the niche itself: who moved in the last 30 days, with the actual videos downloaded, scene-cut and frame-read.

Method: yt-dlp listings of the Shorts tabs and TikTok profiles of ~60 diesel, build and SEMA accounts, filtered to the window, sorted by views and shares; YouTube search sorted by views for the month; 14 clips downloaded with stats JSON into this folder; each run through `VIDEO/tools/watch.py` (PySceneDetect + contact sheets + Whisper); contact sheets read frame by frame. Instagram itself is login-walled, so every example is the creator's TikTok or Shorts mirror. Share counts are TikTok "reposts/shares" from the info JSON.

Folder layout: `NN-handle--slug.mp4`, matching `.info.json`, and `watch/NN-handle--slug/` with `scenes.csv`, `transcript.txt`, `sheet-NN.jpg`.

---

## 0. Scoreboard (window Oct 20 to Nov 21)

| # | Account | Clip | Date | Len | Views | Likes | Shares | Share rate |
|---|---|---|---|---|---|---|---|---|
| 05 | @fassfuelsystems (TikTok) | 2,078 hp iron-block 6.0 Powerstroke | Nov 10 | 36 s | 133,700 | 19,100 | 3,943 | **2.95%** |
| 10 | @dirtydieselcustoms (TikTok) | "3rd Gen Cummins owners, this one's for you" | Nov 6 | 58 s | 75,800 | 6,381 | 1,708 | **2.25%** |
| 08 | @tomsrefurb (TikTok) | "Which rig sounds best?" | Oct 28 | 28 s | 221,900 | 51,200 | 2,418 | 1.09% |
| 09 | @tomsrefurb (TikTok) | SEMA Content Creator of the Year | Nov 10 | 168 s | 252,300 | 52,400 | 1,977 | 0.78% |
| 02 | @throtl (TikTok) | Best cars of SEMA, Part 18 | Nov 7 | 11 s | 117,400 | 14,400 | 839 | 0.71% |
| 04 | @thestradman (TikTok) | SEMA widebody reveal, "Keep it stock" | Nov 5 | 17 s | 405,300 | 59,800 | 1,572 | 0.39% |
| 07 | @dieselpowerproducts (TikTok) | "This guy knows what he's doing" | Nov 16 | 9 s | 923,900 | 5,575 | 2,804 | 0.30% |
| 06 | @justin_danger_nunley (TikTok) | Family-lost-their-home ask | Nov 18 | 44 s | 1,500,000 | 178,600 | 4,222 | 0.28% |
| 01 | @rust_ridge_ranch26 (TikTok) | 7.3 IDI cold morning cab talk | Nov 20 | 66 s | 40,600 | 5,088 | 87 | 0.21% |
| 03 | @thestradman (TikTok) | "SEMA loading in T-7 days" | Oct 24 | 20 s | 667,100 | 84,600 | 1,070 | 0.16% |
| 11 | @davesautocenter (TikTok) | Hidden contamination that kills new engines | Nov 13 | 114 s | 278,000 | 19,500 | 222 | 0.08% |
| 12 | JMR Rebuilders (Shorts, 155k subs) | "Just a slow old 7.3" | Nov 12 | 26 s | 65,844 | 1,833 | n/a | n/a |
| 13 | JMR Rebuilders (Shorts) | "super rare diesel coldstart" | Oct 28 | 21 s | 57,687 | 1,998 | n/a | n/a |
| 14 | Chip Foose (YouTube) | "This is Coming with me to SEMA..." teaser | Oct 29 | 82 s | 445,095 | 2,641 | n/a | n/a |

Read the share-rate column, not the views column. The two clips above 2 percent are both "news for a named tribe": a horsepower record for 6.0 guys, and a feature drop addressed to 3rd Gen Cummins owners by name. Both are from brands with dull feeds otherwise (FASS's surrounding posts: 2k to 26k; DDC's: 700 to 5k). The million-view clips (Nunley, DPP) share at a third of that rate.

Accounts that were checked and did nothing in the window worth copying: Westen Champlin (no Short since Jun 25; long-form is where the 14.2M "10.3L engine in a 56-year-old car" lives), WhistlinDiesel (one Short on Nov 14, a Sweet James ad, 115k, his lowest Short ever), Vice Grip Garage (giveaway promos, 68k to 247k), Matt's Off Road Recovery (no Shorts since Mar 2025), Industrial Injection Shorts (1,200 to 2,700 views each in November, including "WHICH YOUTUBER IS GETTING THIS ENGINE?!" at 1,768, proof that brand build content does not travel even with a brand's reach), Dirty Diesel Customs on YouTube Shorts (200 to 2,100 views for the same shop that did 75k on TikTok), Cleetus (TikTok 55k to 86k kid clips, Nov 3).

---

## 1. Per-video breakdowns

### 01. @rust_ridge_ranch26, "It's getting cold in North Carolina and the ol' 7.3 IDI has about as much attitude as I do"
File: `01-rust_ridge_ranch26--73idi-cold-cab-talk.mp4`. TikTok, Nov 20, 66 s, 40.6k views, 5,088 likes, 117 comments, 87 shares. Same account as the 31k-like "7.3 IDI or 7.3 Powerstroke?" post flagged in the 11-20 doc.

- Structure: one shot, 0:00 to 1:06, no cuts (PySceneDetect found one scene). Phone propped on the dash, she is in the driver's seat of an old truck with a square sunroof, headliner sagging, horse-print sweatshirt, western steering wheel wrap.
- Hook frame: her face, mid-sentence, eyes on the road, "It's getting cooler in North Carolina" at 0:00.7. Motion in frame 1 is her head; no text at all, anywhere, for 66 s.
- Beats: 0:04 cranks it ("Let's see how the IDI likes it because I don't like it, the audacity"), 0:22 "Did y'all see the smoke? What a puffer", 0:33 "It has been a while since I put glow plugs in her... why is it spicy?", 0:44 to 1:03 pivots to the sagging headliner and the silicone-sealed sunroof as "a winter project", 1:00 "No, I don't open it. It is silicone," big grin, hand wave to camera, end.
- Edit grammar: none. Real cab sound, the cold-start rattle is the soundtrack. Camera never moves. B-roll ratio 0 percent.
- Caption: restates the joke, asks "Did y'all see that puff of smoke?!", seeds the glow-plug comment thread and the winter project. Hashtags #RustRidgeRanch #73IDI #coldstart.
- Why it travelled (modestly): personality plus the 7.3 identity signal. Shares are low (0.21%) because it is a hangout, not a claim. Comments are the glow-plug argument. This is the "regular person, big feeling" lane from the 11-20 doc, applied to an IDI.
- For Rival: proof that a one-take cab clip with the truck's own noise and a self-deprecating line holds for a minute in this niche without text. Not the share format, but the follower-conversion format.

### 02. @throtl, "This is what SEMA is about right here!" (Best cars of SEMA, Part 18)
File: `02-throtl--best-of-sema-part18.mp4`. TikTok, Nov 7, 11.7 s, 117.4k views, 14.4k likes, 43 comments, 839 shares.

- Structure: 10 shots in 11.7 s (cuts at 2.1, 2.9, 4.4, 5.1, 6.2, 7.3, 8.5, 9.2, 10.3). Average shot 1.1 s. One car only: the Gas Monkey six-wheel Ferrari Testarossa in a booth.
- Hook frame: rear three-quarter of the red six-wheeler under a honeycomb light rig, with a small, plain, white, centered two-line label at the top of the frame: "Best cars of SEMA - Part 18". The label is on screen for the first two seconds only. Series numbering is the hook: "Part 18" tells you there are 17 more.
- Shot list: rear 3/4 wide (2 s), low rear-wheel detail, nose with logo, front 3/4 wide, side profile, rear wheel again, front light detail, cockpit/door, rear 3/4 reverse angle, dead-on front symmetrical (held 1.4 s to end).
- Camera: gimbal walk, every shot is a slow push or orbit; nothing static. Wide, detail, wide, detail alternation.
- Audio: trending song ("I wanna dance in the lights..."), cuts roughly on the beat, no voice.
- Caption: one line of hype plus #sema #cars #fyp.
- Why it travelled: a car nobody has seen, cut at 1 s per shot, wide-detail-wide rhythm, on a series label. The 0.71 percent share rate is "look at this thing" sends.
- For Rival: this is the grammar for a parts-arrival or walkaround reel when there is a hero object. 1 s per shot, alternate wide and detail, end on the symmetrical front.

### 03. @thestradman, "SEMA loading in T-7 days.... tick tock"
File: `03-thestradman--sema-t-minus-7.mp4`. TikTok, Oct 24, 20.5 s, 667.1k views, 84.6k likes, 639 comments, 1,070 shares. The pre-SEMA tease for his Zacoe widebody Lamborghini Temerario (built in about three days, per Supercar Blondie Nov 7).

- Structure: 9 shots. Two halves. 0:00 to 0:12: three slow beauty clips of the stock teal car in the driveway (wide from the street, front 3/4 low, rear 3/4), each 2 to 3.4 s, with a comment-style text pill in the upper third: "Don't modify it... You ruin every Lambo". 0:13 to 0:20: hard cut to the white-floor garage, car gutted, bumper and quarter panels on the floor, two techs working, then a hand holds a carbon fender toward the lens, then a carbon hood on the car. Text changes to "Don't worry.... She ain't done yet."
- Text style: white sans-serif in a rounded black pill, two lines, centered, upper third, clear of the UI. The quote is written as a hater comment, not a title.
- Camera: handheld, slow, every clip has a drift. No speech. Trending song (lyrics "like an empty fire, stand tall, go higher").
- Caption: the countdown lives in the caption ("SEMA loading in T-7 days.... tick tock"), not on screen. On screen is the argument.
- Why it travelled: the hater-quote-then-reversal structure. The first 12 s is comment bait (639 comments), the back 8 s is the payoff. 1,070 shares are "send to your keep-it-stock friend".
- For Rival: the single most copyable structure in this set for a build account. The countdown is the caption; the on-screen line is the argument the audience already has in the comments.

### 04. @thestradman, "Introducing the fully completed Zacoe Performance Lamborghini Temerario Widebody"
File: `04-thestradman--sema-reveal-keep-it-stock.mp4`. TikTok, Nov 5 (SEMA day 3), 17.5 s, 405.3k views, 59.8k likes, 552 comments, 1,572 shares (0.39 percent, double the tease).

- Structure: 11 shots. 0:00 to 0:07 process, 0:07 to 0:17 reveal. Opens on the stock car in the garage with three stacked hater quotes in the same black pill: "Keep it stock" / "You ruined it" / "You have the worst taste". Then 1 to 2 s cuts: hand holds a bodywork panel with masking tape, tech unrolls chrome wrap, tech squatting at the door wrapping, the half-wrapped car with air tanks in frame. At 0:07 the text drops and the finished chrome widebody sits text-free for 10 s: garage wide, wheel detail, driveway front 3/4, front 3/4 closer, rear wing low angle, rear 3/4, held 3 s to end.
- Edit grammar: process shots short (0.7 to 1.9 s), reveal shots long (1.5 to 3 s). The text is only on the "before" half. The reveal is never captioned.
- Why it travelled: same argument as 03, paid off. Eleven days between tease and reveal, then the long-form "My SEMA Build Full Reveal that No One has Seen" on YouTube (Oct 27, 1.0M views) carried the detail.
- For Rival: tease and reveal are the same reel template run twice, with the quote list growing. Save the actual payoff for the moment the frame swap, the engine drop or the first fire happens.

### 05. @fassfuelsystems, "Kevin Young just SMASHED 2,000rwhp with his iron-block 6.0 Powerstroke"
File: `05-fassfuelsystems--2078hp-iron-block-60.mp4`. TikTok, Nov 10, 36.6 s, 133.7k views, 19.1k likes, 132 comments, 3,943 shares. Highest share rate in the set at 2.95 percent, on a brand account whose neighbouring posts did 2k to 26k.

- Structure: 2 scenes. 0:00 to 0:11: phone footage of a red-and-white Super Duty on a chassis dyno blowing a black column, crowd behind, with the host (FASS staffer, backwards cap, chain) green-screen-cut into the lower left, pointing up at the headline. Headline text at the top: "2,078hp Iron Block / 6.0 Powerstroke!" in bold condensed uppercase, white with a heavy black drop shadow, two lines, centered, on screen the whole 11 s. 0:11 to 0:36: a still photo of the same truck sled-pulling fills the top half, the host cutout sits in the bottom half against black, and word-by-word karaoke captions (small caps, white, the active word highlighted in a red box) run under his chin.
- Transcript: "In case you guys missed the news Kevin Young just smashed 2,000 wheel horsepower with a factory iron block 6.0, not a billet block, 2,078 wheel horsepower out of a Ford iron block 6.0 which is absolutely insane. Of course it's built to the nines, it's got everything thrown at it including our 540 gallon Power Competition FASS fuel system, but point is what Kevin Young has done with the 6.0 platform is wild, so a huge shout out to Kevin, we're glad to be on the truck, congratulations sir."
- Brand mention: one clause, buried at 0:27, framed as "of course it's got everything, including ours". The reel is 90 percent someone else's achievement.
- Why it travelled: a number nobody in the 6.0 community can leave alone, on a headline in frame 1, delivered as news. Shares are the audience telling each other. The brand gets carried by the tribe's news.
- For Rival: this is the template to hand to Driven Diesel, ISSPRO and Power Hungry for posting about Rival (their footage, Jacob's number, one clause of product). It is also Jacob's own "number hook" format: headline up top, face in the corner, the footage does the work.

### 06. @justin_danger_nunley, "Check the comments for the link"
File: `06-justin_danger_nunley--family-ask.mp4`. TikTok, Nov 18, 45 s, 1.5M views, 178.6k likes, 1,999 comments, 4,222 shares. Nunley is the comedy creator whose 1993 S10 "Cream Soda" sat in the Holley booth at SEMA.

- Structure: split screen the whole way. Top half: Nunley talking to camera, backwards cap, moustache, in front of a wall of sports memorabilia. Bottom half: a still photo of the family on a football field. One hard cut at 0:34 when he reaches for the phone. No text.
- Transcript: a house fire, grandparents raising three grandkids, carpenter lost his tools, a week before Thanksgiving, "y'all know what to do, I know y'all got me."
- Why it is in this set: it is the only seven-figure clip from a SEMA-build creator in the window, and it is not about the truck. His SEMA truck posts in the same fortnight ("Fun was had! Photos by...", 72.6k; "Last night was absolutely EPIC!!! Top 5 finish!!!!", 27.4k) were his lowest numbers, while "My niblings!" did 1.2M and "Crayons" 667k. Even the internet-darling SEMA truck lives in long-form and press; on short-form the account is carried by the persona. Exactly "memes share, build reels don't", at 10,000x the scale.

### 07. @dieselpowerproducts, "What do you think?"
File: `07-dieselpowerproducts--this-guy-knows-what-hes-doing.mp4`. TikTok, Nov 16, 9.7 s, 923.9k views, 5,575 likes, 660 comments, 2,804 shares. The rest of DPP's November feed: 241 to 45,600 views.

- Structure: 3 shots. 0:00 to 0:04: phone under a truck, pointed up at a transmission case and hard lines, the host's face green-screen-cut into the lower left (curly hair, beard, shop shelving behind), a finger comes into frame and points at the line. 0:04 to 0:06: closer on the line where it is held against the case with what looks like an improvised clip. 0:06 to 0:09: tighter still, finger tapping it.
- Transcript (sarcastic): "Check this out. This guy knows what he's doing. Never leave a transmission line loose. That could start leaking oil and that's expensive. What do you guys think?"
- No on-screen text. Original audio. Ends on the question.
- Why it travelled: "look what this guy did" shop-floor content with a deadpan voice and a question that forces the comments to explain the joke (660 comments). 2,804 shares at 0.30 percent are "send to the buddy who does this". Short enough to loop twice.
- For Rival: the found-fix on a 67-year-old farm truck is an endless supply of these. Nine seconds, point, deadpan, ask.

### 08. @tomsrefurb, "Which rig sounds best?"
File: `08-tomsrefurb--which-rig-sounds-best.mp4`. TikTok, Oct 28, 28.9 s, 221.9k views, 51.2k likes, 369 comments, 2,418 shares (1.09 percent). Tom's Refurb was named SEMA 2026 Content Creator of the Year on Nov 6 (2.4M combined following, budget muscle-car resurrections, self-deprecating humour).

- Structure: 8 shots, four vehicles, about 7 s each, every vehicle gets the same two-shot pair: a static wide from the driveway, then a static low-angle at the rear wheel and exhaust while it revs. 0:00 Mustang wide (headlights on), 0:03 low rear-wheel with "NOISE COMPLAINT" lettered on the quarter, tire smoke; 0:06 primer Camaro wide, 0:09 low wheel; 0:12 maroon Z71 under the carport wide, 0:17 low at the rear tire, smoke; 0:20 red lowered Silverado wide, 0:25 low rear wheel.
- No text. No speech. Whisper found zero words. The sound is the content.
- Caption carries the whole prompt: "Which rig sounds best?"
- Why it travelled: four exhaust notes, a vote in the caption, a comment war (369), and sends to "settle it". Zero production.
- For Rival: the two-shot pair (static wide, static low rear wheel) is a house style worth adopting for anything that makes noise. Also the only format here where the caption, not the video, is the hook.

### 09. @tomsrefurb, "We went to SEMA last week... and won CREATOR OF THE YEAR!"
File: `09-tomsrefurb--sema-creator-of-the-year.mp4`. TikTok, Nov 10, 168 s, 1920x1080 horizontal (letterboxed on TikTok), 252.3k views, 52.4k likes, 476 comments, 1,977 shares.

- Structure: raw phone footage from an audience seat at SEMA Industry Honors. 0:00 to 0:16 the "CONTENT CREATOR OF THE YEAR" slide while the presenter reads his bio ("started repairing small engines at 13 to help pay for his '67 Mustang"); 0:16 to 1:13 the tribute reel on the big screen (38 scene changes, his own clips: lawn Mustang, garage talking head, burnout, Gremlin, truck cab); 1:13 the Tom's Refurb logo, the name card with his photo; 1:18 the camera swings as the row stands, phones go up; 1:24 to 2:38 one wide, unmoving shot of the stage while he gives a two-minute speech (thanks Westen Champlin for nominating him, thanks his parents and team).
- No edit, no text, no music. Horizontal.
- Why it travelled: a real moment from a liked person, posted raw, with the whole feed's goodwill behind it. 1,977 shares are fans sending pride.
- For Rival: the biggest reach for this creator in the fortnight came from an unedited horizontal phone clip. The lesson is not "post horizontal"; it is that a genuine milestone needs no grammar. When Rival hits one (frame rolls, engine in, first fire, SEMA acceptance), post the raw clip first, polish later.

### 10. @dirtydieselcustoms, "3rd Gen Cummins owners, this one's for you"
File: `10-dirtydieselcustoms--3rd-gen-cummins-this-ones-for-you.mp4`. TikTok, Nov 6, 58.8 s, 75.8k views, 6,381 likes, 84 comments, 1,708 shares (2.25 percent, second highest in the set). Same shop's YouTube Shorts of the same material: 367 views.

- Structure: 12 shots, all first-person from the driver's seat of a 3rd Gen Ram, phone handheld at chest height. 0:00 to 0:03 cold open on the gauge cluster with a thumb on the cruise buttons (motion in frame 1); 0:03 wide of the wheel and dash with an EFI Live screen on the pillar; 0:09 one 2 s cutaway to the red Ram rolling toward camera on a road with a smoke cloud; 0:11 back inside; 0:16 to 0:46 hands on the wheel pressing cancel, resume, set while he narrates; 0:46 to 0:58 the launch at 2,100 rpm from the cab.
- Transcript opens mid-sentence (a jump-cut tease of the payoff), then: "So everyone's hearing about cruise shift-on-the-fly for the new Powerstrokes and Cummins. Well it's time us older trucks get a little bit of love. Brand new from Peakside Performance: shift on the fly through the cruise on EFI Live..." Ends "This is only available at dirtydieselcustoms.com."
- No on-screen text in the first 40 s. Original audio, road noise under.
- Caption is the headline: names the tribe in the first five words, bullet list of the two features, "Available exclusively through Dirty Diesel Customs for the month of November."
- Why it travelled: an announcement addressed to a specific owner group that has been left out ("us older trucks get a little love"). Shares are 3rd Gen owners tagging each other. It is sales content and it still shared at 2.25 percent because the first line names the person it is for.
- For Rival: "7.3 guys, this one's for you" is the opening line. Pick the one thing on Rival that 7.3 owners have never seen done on their platform and address them by name.

### 11. @davesautocenter, "The Hidden Contamination That Kills New Engines!"
File: `11-davesautocenter--hidden-contamination.mp4`. TikTok, Nov 13, 114.9 s, 278k views, 19.5k likes, 345 comments, 222 shares (0.08 percent). Dave's November TikToks for context: "New mechanic given a 7.3 nobody could fix" 156k, "AI replace mechanics?" 6k, SEMA flashlight-hunt posts 15k to 88k.

- Structure: 8 scenes. 0:00 one second on Dave in the shop (grey hair, glasses, black shop tee, lav mic); 0:01 to 0:04 a 3 s insert of a bare block being torn down; 0:04 to 0:43 Dave talking, static medium shot, hands working; 0:43 to 0:50 insert of a gloved hand with a main cap on a crank; 0:50 to 1:44 Dave again, then he walks the camera to a steel bench, bearings laid on a shop towel, fingertip on the wear marks, a bearing shell held up to the lens, a microscope monitor in the background; 1:44 to 1:54 back to Dave for the close.
- No on-screen text at any point. One static camera position for the talking parts, handheld for the bench.
- Argument: customer bought an engine, instructions said replace every cooler, the son installed it and did not, it puked oil, the teardown shows dirt impacted in brand-new bearings, "Will that probably be okay? I guess. But I'm not warranting it." Close: "If the shop's telling you to flush them, tell them you want them replaced."
- Why it travelled: failure forensics with physical evidence and a rule you can repeat. Views are high and shares are low: authority gets watched, not sent. 345 comments arguing about flushing coolers.
- For Rival: Jacob's parts-counter credential fits this shape, but at 20 to 30 s, not 115, and with the evidence in frame 1 (the dirty bearing, not the face).

### 12. JMR Rebuilders (Shorts), "Just a slow old 7.3"
File: `12-jmrrebuilders--just-a-slow-old-73.mp4`. YouTube Short, Nov 12, 25.8 s, 65,844 views, 1,833 likes, 159 comments. Channel 155k subs. Same channel in the window: "super rare diesel coldstart" 57.7k (Oct 28), "6.0 cold start" 6.5k, "Just a mild 454!" 9.4k, "got a clogged" 4k, "Just a slow 7.3" 1.7k (one day old at pull).

- Structure: 3 shots. 0:00 to 0:03 a walk past a tan OBS crew cab in a gravel lot ("So he's already got a Hydra tuner. Go ahead and do it, Drew."); 0:03 to 0:17 the phone drops to the tailpipe of a green OBS with a diamond-plate toolbox and a black column rolls out across the lot, filling the frame by 0:06, the truck pulls away through it; 0:17 to 0:26 the camera pans to the road as the truck goes by and the smoke drifts over the shop sign.
- No text. No music. Real sound. Handheld phone, wide lens.
- Title is the hook: "Just a slow old 7.3" is understatement bait; 159 comments correct it. Note the near-identical "Just a slow 7.3" posted Nov 20 did 1.7k in its first day; the word "old" and the smoke seem to carry the first one, though one day of data is not a fair comparison.
- For Rival: the 7.3 audience on Shorts rewards (a) the sound, (b) smoke, (c) an understated, slightly wrong title that the comments must fix. The Hydra chip mention is a free data point for the Power Hungry partnership: the name was said out loud and nobody minded.

### 13. JMR Rebuilders (Shorts), "super rare diesel coldstart"
File: `13-jmrrebuilders--super-rare-diesel-coldstart.mp4`. YouTube Short, Oct 28, 21 s, 57,687 views, 1,998 likes, 67 comments.

- Structure: 2 shots. 0:00 to 0:04 selfie in the cab with a German shepherd's head across the frame, red cap, "Here's a cold start on a 97 F350 with a 10-inch exhaust." 0:04 to 0:21 low on the tailpipe, 4x4 badge in frame, white smoke, then the camera walks in until the 10-inch tip fills the frame.
- No text, no music, no cuts beyond the one. Vague title ("super rare diesel") is the curiosity gap.
- For Rival: the two-shot recipe for every "it runs" moment: one sentence of setup from the seat, then hold on the pipe.

### 14. Chip Foose, "This is Coming with me to SEMA..."
File: `14-chipfoose--this-is-coming-with-me-to-sema.mp4`. YouTube, Oct 29, 82 s, horizontal, 445k views on a 313-sub-count-reporting channel (the view count came from being embedded in the FOOSE.com giveaway).

- Structure: 40 shots, cinematic. 0:00 extreme macro of a part, 0:03 Chip in a leather jacket at dawn in the desert looking off, 0:07 Mustang nose at sunrise, 0:11 drone of the Foose shop, 0:17 to 0:24 a green F-150 and crate arriving, 0:25 to 1:08 hands-on build inserts (tape lines, tail lights, grille pony, paint booth, pinstriping the hood), 1:10 to 1:22 black cards: "ENTER / TO / WIN / FOOSE.COM / Foose x Coulson Group" with legal fine print.
- No speech. Score only. Teaser grammar: never shows the finished car. Description: "Being officially unveiled on 11/3."
- For Rival: the pro-studio version of the tease. Worth noting only for the structure: a dated promise ("unveiled 11/3") and a reason to care beyond the car (a giveaway). Not a format a one-man account should imitate.

---

## 2. Cross-video patterns

1. **Named-tribe news beats everything on shares.** The two clips over 2 percent share rate both open by naming who the clip is for ("3rd Gen Cummins owners, this one's for you"; "2,078 hp iron block 6.0") and deliver one fact. Spectacle (Stradman, 0.16 to 0.39 percent) and comedy (DPP, 0.30 percent) get views; tribe news gets sent. This is the 10x-targeted-claim figure from the 11-20 doc, observed in the wild.

2. **The hater quote is the new title card.** Both Stradman clips, and the structure of DPP's sarcasm, put the audience's own objection on screen first ("Don't modify it", "Keep it stock", "This guy knows what he's doing") and spend the back half answering it. The countdown and the facts go in the caption. The argument goes on the screen.

3. **Six of fourteen winners have zero on-screen text.** Rust Ridge, Tom's Refurb (both), Dave's, both JMR clips. This cuts against the 75-of-79 "text in the first 3 s" stat from the broader Reels study. In this niche on TikTok and Shorts, persona plus real sound carries; text shows up on the brand/news clips (FASS, DDC caption, throtl label) and on the comment-bait clips (Stradman). Rule of thumb: text when the hook is a claim, no text when the hook is a noise or a face.

4. **Sound is a format.** "Which rig sounds best", both JMR cold starts, the IDI cab clip: the engine is the audio bed and the content. Every one of them uses the same two-shot pair: wide static, then low static at the pipe or wheel. No music over a running diesel.

5. **Face-in-the-corner news (greenscreen cutout) is the brand grammar.** FASS and DPP both cut the host into the lower-left corner over the footage, headline on top, then switch to a still photo with karaoke captions once the footage runs out. It lets one person make a "news" reel from a phone clip and a selfie. Jacob can do this in CapCut alone.

6. **Cut rate splits cleanly by job.** Walkarounds and reveals: ~1 s per shot (throtl 1.1 s avg, Stradman reveal 1.5 s). Explanations and sound clips: 5 to 15 s per shot, or one take. Nobody in the window mixed the two inside one reel except Stradman, who used short cuts for process and long holds for the reveal, which is the right way round.

7. **Build posts still underperform on the accounts that have the best builds.** Nunley's Cream Soda posts were his lowest of the fortnight; Industrial Injection's engine builds do 1,300 views on Shorts; DDC's install Shorts do 300. The exceptions are build posts that are secretly something else: a record number (FASS), a tribe feature (DDC), a hater argument (Stradman), or a milestone emotion (Tom's award).

8. **Platform split.** Same material, DDC: 75.8k TikTok vs 367 YouTube Shorts. Dave's, FASS, DPP: TikTok is where the diesel shop clips run. JMR is the only small account winning on Shorts, and only with cold starts. For @elcoyotediesel the practical read is that Instagram behaves more like TikTok (sound, persona, pill text) than like Shorts.

9. **Raw beats polished at milestones.** The highest-reach Tom's Refurb clip of the window is horizontal, unedited, 168 s. Milestone footage should go out as shot.

10. **Caption as hook.** Tom's "Which rig sounds best?" and DDC's "3rd Gen Cummins owners, this one's for you" put the entire hook in the first line of the caption, with a video that would not work without it. Write the first five words of the caption before shooting.

---

## 3. How SEMA 2026 builds were revealed and documented on social this month

The show ran Nov 3 to 6 in Las Vegas. Observed cadences:

- **TheStradman (Zacoe widebody Temerario)**: Oct 24 TikTok tease ("SEMA loading in T-7 days", hater quote, 667k), Oct 27 YouTube long-form "My SEMA Build Full Reveal that No One has Seen" (1.0M), Nov 3 TikTok "Introducing my Zacoe Performance Lamborghini Temerario" (357k), Nov 5 TikTok "fully completed" reveal with the stacked hater quotes (405k, 1,572 shares), then press pickup (Supercar Blondie Nov 7: "built in three days"). Pattern: short-form tease with the argument, long-form with the detail, short-form reveal that reuses the tease's text, press last. His SEMA content out-shared his usual supercar content.
- **DailyDrivenExotics**: Oct 28 "Revealing Our MOST Ambitious SEMA Build EVER!" (553k, pre-show, sponsor read), Nov 4 "We Can FINALLY Reveal Our Two SEMA Builds!" (659k) with a booth call-to-action in the description: "Come see the truck in person this Friday at 2 PM at the Elevation Off Grid booth in SEMA's West Hall... exclusive collab T-shirts, 100% FREE." The booth time and the free shirt are the reveal's share mechanic.
- **Chip Foose (Foose x Coulson Mustang)**: Oct 29 cinematic 82 s teaser, no car shown, "Being officially unveiled on 11/3", tied to an enter-to-win. Dated promise plus a prize.
- **Kindig-it Design**: Nov 7 recap "Big Reveals & Wild Builds! Dave & Kev Explore SEMA 2026" (585k), description line worth stealing: "You've followed these builds in the shop, now see them take the spotlight." The reveal is framed as the payoff of a series the audience already watched.
- **Justin Nunley / Holley "Cream Soda" S10**: the truck sat in the Holley booth (#22463) with a scheduled Nov 6 appearance; Holley's Nov 3 press release listed the parts. Nunley's own feed in the window is comedy; the truck posts did 27k to 72k against 667k to 1.5M for the jokes. The build won press (HotCars: "already an internet darling") and a booth, not short-form numbers.
- **Tom's Refurb**: did not bring a SEMA build; won Content Creator of the Year (nominated by Westen Champlin) and posted the raw ceremony clip (252k, 1,977 shares). Also "The most controversial Mustang of all" (375k, Oct 23) and "Which rig sounds best?" (222k) the week before the show.
- **throtl**: a numbered "Best cars of SEMA, Part N" series of 11 s walkarounds posted daily from the floor, 12k to 199k each (carbon Civic Type R 199k, Gas Monkey six-wheeler 117k). Also Shorts of the Prelude Type R and TJ Hunt's Aston GT3 unveilings (49k to 90k). Volume plus a series label.
- **Brands on the floor**: Dave's Auto Center ran a "free flashlights hidden at SEMA" scavenger hunt on TikTok (15k to 88k per post) and an Edge CTS4 giveaway (88k). XDP posted "Wrapping up an incredible week at SEMA" (1.2k). Dirty Diesel Customs posted "A little DDC showing up at SEMA" (1.5k). Floor presence without a hook did nothing.
- **Named trucks from the 11-20 doc**: the 1973 F-600 "Yeti" by Jacked Up Trucks (modern chassis, Whipple) made AutoGuide's five craziest list; the Jacked Up Trucks TikTok has no videos, so it had no short-form reveal at all. Trick Rides' carbon 1968 F-100 and Fat Fender Garage's $1M 1956 F-100 GT/FX travelled on press (CarScoops, HotCars, Motor1, autoevolution) rather than creator reels. Battle of the Builders went to Eddie Pettus's 1,300 hp '70 Chevelle; Young Guns to Jesse Rieger's '69 Mustang; neither surfaced a viral reel.

Takeaways for a "Road to SEMA 2027" account: (1) the tease carries the argument, the reveal reuses it; (2) give the reveal a time and a place ("Friday 2 PM, West Hall") even a year out, because the booth is the share mechanic; (3) frame the eventual reveal as the payoff of the series ("you followed this in the shop"); (4) a numbered series label ("Part 18") is itself a hook; (5) a build with no short-form reveal (Yeti) got press and nothing else. Rival is a year out, which is the Kindig position: the next 12 months are "the shop", and every entry should be numbered.

---

## 4. Live formats this week (additive to the 11-20 list)

From Later (Nov 20) and New Engen (Nov 20): "Dear Santa, I'm a size..." (Wham! "Last Christmas" instrumental, 5 to 10 s, ends with something that does not come in sizes); "Get up, diva" (a setback and a comeback, original audio); "Appointment timestamps" (one job from arrival to leaving, timestamped); "Christmas wrapping paper reveal" (tear through paper taped over a box, door or sign, 6 to 12 s, no set sound); "Add to Cart" (hands hand in four to six items one at a time with an on-screen reason, 8 to 15 s); "Paid me no mind" (single-take lip sync repeating a line with different stress). Audio chart for Nov 17 to 25 (SocialPilot): Pink Floyd "Time" still top, "Last Christmas", Harry Styles "Coming Up Roses" (49k to 116k reels in three weeks), Ashe "Stop the Wedding!" (82k, doubled). "NO-vember" expires Dec 1.

---

## 5. Ten reel concepts for Project Rival this week

All solo-shootable. Hooks open on motion in frame 1. No Elite Diesel anything. Partner names appear only where they would appear naturally (a box, a gauge, a chip), one clause max. Share lines go in the caption, not on screen.

**1. "7.3 guys, this one's for you." (DDC named-tribe template)**
- Hook line (text pill, upper third, frame 1 over a hand slapping the 7.3 on the stand): "7.3 guys, this one's for you."
- Shot list: 0:00 hand slap on the valve cover (motion); 0:02 to 0:08 three 2 s cuts of the one thing 7.3 owners have never seen on their platform (the regulated-return fuel plan laid out on the bench, the gauge set still in its box, the chip and media interface on the fender); 0:08 to 0:18 one held shot of the engine while a second line lands at 0:12: "Stock 7.3 fuel rails starve the back cylinders. Not on this one."; 0:18 to 0:22 wide of the '59 cab on the floor beside the frame.
- Caption first five words: "7.3 guys, this one's for you." Share line: "Send this to the one who still says a 7.3 can't make real power."

**2. "Leave the '59 alone." (Stradman hater-quote then reversal)**
- Hook line (pill): "Leave the '59 alone... you'll ruin it."
- Shot list: 0:00 to 0:09 three slow handheld drifts of the F600 as found (street wide, low front 3/4, rear 3/4 with the express bed), text up the whole time; 0:09 hard cut to the bare Super Duty frame on stands / cab off / engine on the stand, text changes to "Don't worry... she ain't done yet."; 0:09 to 0:17 three 1.5 s cuts of work in progress, end on a hand holding a new part toward the lens, 2 s hold.
- Caption: "SEMA 2027 loading. T-346 days. Tick tock." (the countdown lives here, not on screen). Share line: "Tag the guy who told you to keep it stock."

**3. "Just an old 7.3." (JMR understated cold start; run it the day the donor or any 7.3 on hand fires, otherwise bank it for first fire)**
- Hook line: none on screen. Title/caption only: "just an old 7.3".
- Shot list: 0:00 to 0:03 one sentence from the seat ("Here's the 7.3 that's going in the '59, cold, 28 degrees out"); 0:03 cut to the tailpipe, low, hold for the crank and the first smoke, walk in until the tip fills the frame; 0:15 pan to the truck pulling away or idling, end on the smoke drifting. 20 to 25 s. Real sound, no music, no text.
- Caption share line: "If you know, you know. Send it to someone who doesn't."

**4. "67-year-old truck. 29-year-old engine. 600 horsepower." (FASS number headline, face in the corner)**
- Hook line (bold condensed uppercase, white with black shadow, top of frame, on from 0:00): "67 YEAR OLD TRUCK / 29 YEAR OLD ENGINE / 600 HP"
- Shot list: 0:00 to 0:10 the best 10 s of existing Rival footage (frame, engine, cab) with Jacob green-screen-cut into the lower left pointing up at the headline (shoot the selfie against a plain wall, key it in CapCut); 0:10 to 0:25 a still of the '59 fills the top half, Jacob cutout in the bottom half, karaoke captions, 30 words: "This is the one I'm taking to SEMA 2027. Compound turbos, regulated return, built 4R100, daily driven when it's done. Day 346."
- Caption share line: "Send this to someone who'd drive it."

**5. "This guy knows what he's doing." (DPP deadpan found-fix)**
- Hook line: spoken, 0:00, deadpan: "Check this out. This guy knows what he's doing."
- Shot list: phone under or inside the '59, a finger enters frame and points at the worst farm fix on the truck (baling wire, a bolt where a pin goes, a wood block spacer, a spliced wire); 0:04 tighter; 0:06 tighter, tap it. 9 s. Ends spoken: "What do you guys think?" Optional Jacob cutout lower-left, no text.
- Caption share line: "Send this to the guy who fixes everything with zip ties."

**6. "Dear Santa, I'm a size..." (this week's format)**
- Hook line (text, frame 1, over hands wiping the fender): "Dear Santa, I'm a size..."
- Shot list: 0:00 to 0:02 hands on the '59 fender; 0:02 to 0:05 three 1 s cuts (empty engine bay, the frame, the parts shelf); 0:05 to 0:08 wide of the whole truck, text lands: "...1959 F600 cab on a Super Duty frame. It doesn't come in sizes." Wham! "Last Christmas" instrumental from the in-app library. 8 s, loops.
- Caption share line: "Send this to whoever's still buying you socks."

**7. "Lately on my SD card, Rival edition" (no new filming)**
- Hook line (text over an SD card or the camera screen, frame 1): "Lately on my SD card"
- Shot list: 10 to 14 clips from the last three weeks, each 0.7 to 0.9 s, cut on the beat, loudest-motion clip first (a grinder, a hammer, a hoist), end on the single best frame held 2 s with "Day 346" in the pill.
- Caption share line: "Save this so you can say you were here early."

**8. "Wrapping paper reveal" of the next partner part**
- Hook line (text): "Sneak peek at what's going in the '59."
- Shot list: tape wrapping paper over the opened box (gauges, fuel kit, chip) or over the engine bay; frame 1 is the hand already tearing; 0:01 to 0:05 tear through, 0:05 to 0:10 pull the part out, turn it once in the light, 0:10 to 0:12 set it on the fender of the truck. 10 to 12 s, paper sound only. Brand on the box is the only brand mention.
- Caption share line: "Send to the gauge nerd." (or "the fuel system nerd", whichever part)

**9. "The three parts every 7.3 guy buys twice. I'm buying them once." (Dave's forensics at 25 s, parts-manager credential)**
- Hook line (text over a dirty old sensor held to the lens, frame 1): "Every 7.3 guy buys these twice."
- Shot list: three parts, 5 s each, old one and new one held side by side over the engine: cam position sensor, under-valve-cover harness, injector pressure regulator (or whichever three Jacob can actually show); text label per part; 0:15 to 0:25 one line to camera from the seat: "I order parts for a living. I know which ones come back. These don't get a second chance on this truck."
- Caption share line: "Send this to your buddy who got stranded by a $30 sensor."

**10. "Add to cart: everything that showed up this week" (this week's format, partner-friendly)**
- Hook line (text): "Add to cart. Rival, week 3."
- Shot list: locked camera on the bench, Jacob's own hands enter from off-frame and set down four to six items one at a time, 1.5 s each, with a four-word on-screen reason per item ("regulated return: feeds cylinder 8", "pyro gauge: because compounds", "chip: because 1996 PCM", "ARP studs: because 40 psi"), end on the full pile with the '59 behind it. 10 to 14 s, original audio (parts hitting the bench).
- Caption share line: "Send this to the guy who thinks it's just a motor swap."

Series note: give every Rival post a number ("Day 346", "week 3", "Part 18" style) so the eventual reveal can be framed the Kindig way: "you followed this in the shop, now see it under the lights." And when a real milestone lands (frame rolls, engine in, first fire), post the raw clip within the hour, before any of the above.

---

## 6. Sources

- Clip stats: each `*.info.json` in this folder (TikTok and YouTube metadata via yt-dlp, pulled 2026-11-21 ~08:25 MT).
- Channel listings: yt-dlp over the Shorts tabs and TikTok profiles named in section 0.
- SEMA honors: https://www.sema.org/news-media/press-release/sema-names-2026-sema-person-year-and-content-creator-year
- Battle of the Builders: https://www.sema.org/news-media/enews/2026/45/eddie-pettus-wins-2026-sema-battle-builders-70-chevrolet-chevelle
- Stradman build timeline: https://supercarblondie.com/utah-youtuber-thestradman-sema-widebody-lamborghini-temerario/
- Holley / Cream Soda: https://www.globenewswire.com/news-release/2026/11/03/3394286/0/en/holley-performance-brands-highlights-new-products-sxth-element-acquisition-and-amotiv-collaboration-at-sema-2026.html ; https://www.hotcars.com/sema-2026-best-builds-highlights/
- SEMA trucks in press: https://www.autoguide.com/auto/the-5-craziest-trucks-we-found-at-sema-2026-44642092 ; https://www.carscoops.com/2309037/carbon-fiber-1968-ford-f100-sema/ ; https://www.autoevolution.com/news/this-1956-ford-f-100-with-800-horsepower-is-the-truck-your-grandpa-wished-he-had-277936.html
- Weekly formats: https://later.com/blog/instagram-reels-trends/ ; https://newengen.com/insights/instagram-trends/ ; https://www.socialpilot.co/blog/instagram-reels-trends
- WhistlinDiesel channel state: https://vidiq.com/youtube-stats/channel/@whistlindiesel/
