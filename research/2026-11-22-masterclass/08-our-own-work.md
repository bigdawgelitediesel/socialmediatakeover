# 08. Learning from our own work (cluster J, questions 37 to 40)

Written 2026-11-22 from `data/instagram/posts.tsv` (84 posts, 71 reels with a skip rate), `data/instagram/reads-48h.tsv` (15 reads taken 05:14 UTC), `research/2026-11-20-reels-made.md`, `playbook/12-talking-head-in-the-truck.md`, the September audit, the 11-12 refresh, the 11-21 live pull, and the three rule files (master playbook, addendum rules 1 to 47, diesel hour rules 48 to 109). No web. Shares per reach below is `100 * shares / reach`. Opening types are inferred from the caption summary and the account notes, not from watching the files; where the inference is weak it says so.

**One limit up front: the repo holds no per-post length.** `posts.tsv` has `avg_watch_ms` and nothing to divide it by. `research/inventory/01` already flags `duration_s` as a missing column. The only lengths on record are Harley Trade (18.5 s, so 10.8 s watch is 59 percent) and the unposted gratitude cut (64.6 s). Watch share cannot be computed for anything else, so the tables below use absolute average watch. Adding `duration_s` to the pull is the single cheapest fix in the whole dataset.

## Question 37. The ten lowest and ten highest skip rates

Median skip across the 71 reels is 45.6 percent. Account average has drifted from 48.2 (September, 29 reels) to about 47 now.

### Ten lowest skip rates

| Date | Skip | Views | Shares | Shares/reach | Avg watch s | Inferred open | Caption |
|---|---|---|---|---|---|---|---|
| 07-24 | 20.0 | 396,640 | 13 | 0.01 | 27.3 | action, the gooseneck fail | Well it seemed like a good idea |
| 10-17 | 20.6 | 1,537 | 0 | 0.00 | 18.5 | talking, truck history | Absolutely incredible to just have a small glimpse |
| 10-07 | 23.6 | 1,687 | 0 | 0.00 | 16.4 | talking head, personal | The first Gift from my 2011 F350 |
| 10-19 | 23.8 | 1,542 | 4 | 0.29 | 13.8 | talking head, personal decision | Hard to come to this conclusion |
| 10-23 | 27.0 | 3,222 | 17 | 0.64 | 13.2 | relatable shop clip | What a shop dog actually looks like |
| 10-23 | 28.8 | 1,532 | 3 | 0.23 | 15.7 | talking, partner (II Diesel) | Oh yall gonna love this one |
| 11-11 | 29.8 | 1,659 | 0 | 0.00 | 21.7 | talking head, trust, one take | Why companies hate your truck |
| 11-05 | 30.1 | 1,545 | 25 | 1.99 | 6.8 | meme | At this point it's time to let it go |
| 11-19 | 31.7 | 989 | 1 | 0.12 | 10.2 | lyric montage | You just have to go for it |
| 06-26 | 32.4 | 261 | 0 | 0.00 | 8.3 | relatable | I have nothing else to say on this |

### Ten highest skip rates

| Date | Skip | Views | Shares | Shares/reach | Avg watch s | Inferred open | Caption |
|---|---|---|---|---|---|---|---|
| 08-13 | 85.4 | 1,768 | 1 | 0.06 | 2.6 | product, sponsor | Glasses from @twosvge, project truck Chief |
| 07-01 | 76.0 | 344 | 0 | 0.00 | 9.0 | product, sponsor | @issproofficial pillar and gauges |
| 11-19 | 74.8 | 417 | 0 | 0.00 | 4.6 | thank-you, partner Collab | Project Rival is Poppin off |
| 11-20 | 74.1 | 352 | 1 | 0.33 | 4.7 | product, partner giveaway | Move bumpers giveaway |
| 10-30 | 72.2 | 468 | 14 | 3.64 | 3.5 | skit | What my mechanics really wanna say |
| 08-20 | 72.1 | 161 | 1 | 0.67 | 4.2 | build update | Small update. New fuel system on |
| 11-18 | 71.7 | 348 | 0 | 0.00 | 7.4 | thank-you | Huge shoutout to the BOIZ |
| 10-30 | 70.9 | 173 | 0 | 0.00 | 3.4 | link-in-bio ask | Yeah we went all the way, link in bio |
| 07-01 | 68.3 | 425 | 1 | 0.26 | 9.5 | product, sponsor | @deraleperformance transmission cooler |
| 11-17 | 66.3 | 195 | 0 | 0.00 | 9.2 | build update | Project Rival is moving |

### What each set shares

| Set | n | Median views | Median shares/reach | Median skip | Median watch s | Median likes/reach |
|---|---|---|---|---|---|---|
| Lowest ten | 10 | 1,544 | 0.06 | 27.9 | 14.8 | 3.75 |
| Highest ten | 10 | 350 | 0.03 | 72.2 | 4.6 | 1.45 |

The low-skip set: a person or an event is the subject in second one. Seven of ten are Jacob talking or a thing happening in the shop; none opens on a part. First words of the captions are plain speech ("Well", "Hard", "Why", "What", "Oh"). Median watch is 14.8 s, three times the high set. But the set splits in two on shares: the long holders (13 to 27 s watch) share at 0 to 0.3 percent, and the one meme in the set ("Let it go", 6.8 s watch) shares at 2 percent. Holding is not sending.

The high-skip set: nine of ten open on a product, a brand handle, a thank-you or an ask. First words are "@deraleperformance", "@issproofficial", "Glasses from", "Huge shoutout", "Project Rival", "Move bumpers". Median watch 4.6 s. The one exception is the mechanics skit (72 percent skip, yet 3.6 percent shares per reach on 385 reach): the people who stayed sent it. A bad first frame on a good joke.

The September finding holds at n=71: below-median skip gets 4.4 times the median views (1,544 vs 350) and 5.8 times the shares per reach (0.23 vs 0.04). But the correlation between skip and shares per reach, viral reel and under-200-reach posts removed (n=57), is now 0.00. Skip decides whether a reel gets seen; what it is about decides whether it gets sent. Average watch and shares per reach correlate at minus 0.21: the longer they watch, the less they send, on this account.

### Personal and relatable talking heads versus everything else

Talking head here means Jacob speaking to camera for the length of the reel (inferred from caption plus a watch time above 10 s). Seven qualify as personal or relatable: Why companies hate your truck, I need your help, Hard to come to this conclusion, Absolutely incredible, The first Gift, Am I crazy, Who is with me. Four more are build or partner talking (223 mileage makers, SEMA announcement, II Diesel, Incredible to think).

| Group | n | Median views | Median shares/reach | Median skip | Median watch s | Median likes/reach |
|---|---|---|---|---|---|---|
| Personal/relatable talking heads | 7 | 1,537 | **0.00** | **29.8** | **14.8** | 2.72 |
| Build/partner talking | 4 | 825 | 0.25 | 45.5 | 12.6 | 4.65 |
| Everything else | 60 | 496 | 0.20 | 46.3 | 6.0 | 4.05 |
| of which memes | 18 | 1,988 | **0.56** | 39.1 | 5.6 | 4.70 |
| of which short personal clips (Sept PERSONAL pillar) | 5 | 1,656 | 0.23 | 38.7 | 5.6 | **6.38** |
| of which build | 14 | 321 | 0.00 | 51.7 | 7.5 | 2.70 |
| of which sponsor and thank-you | 10 | 350 | 0.00 | 71.3 | 7.6 | 2.36 |

Three things this says that the plan has not absorbed:

1. The talking heads are the account's best hook and best hold (29.8 skip, 14.8 s) and its worst sender (median zero, best ever 4 shares). Across all 20 reels with a watch above 10 s the median shares per reach is 0.02 percent and the maximum share count is 17. The 39 reels under 7 s watch share at 0.30 percent median.
2. The September "PERSONAL 14.8 percent ER" pillar was five short clips with a caption ("It may cost you nothing", "And just like that"), not talking heads. They still carry the highest likes per reach on the account (6.4 percent). The daily talking head inherits the label, not the number.
3. Memes are the only format that does views and sends at once. Nothing with a face held past 10 s has ever cleared 0.7 percent sends.

## Question 38. The "Find the gratitude" cut, judged

What was built (reels-made, 2026-11-22): 83 s handheld porch selfie, cut to 64.6 s with four hard cuts; cold open on "even if life is really hard right now" (55.3 to 68.35), then the Sunday reflection (0.5 to 22.45), the people (22.45 to 37.45), payoff on the build and the stress (68.6 to 83.1); 1.00 / 1.06 punch-in alternation; one lockup "find the gratitude" 0.13 to 3.0 s; PlainCaption 68 px captions throughout; caption line 1 "For whoever is heading into Thanksgiving week with more on the plate than they can carry." Not yet posted, so no read.

### What it got right

- The filler ("I wanted to make a post") is gone and the cut opens on the strongest line. That is the mid-sentence cold open the hook atlas and playbook/12 ask for.
- Length sits inside the 60 to 120 s shape playbook/12 and rule 96 prescribe, and outside the banned 20 to 40 band.
- One lockup on the hook, off by 3 s, captions 2 to 4 words on the chest band, no stroke: the caption audit spec exactly. No burned CTA, no outro, no fade, no grade beyond the HLG tone map: Jacob's standing rules all kept.
- Caption line 1 is a person type, not a description of the video. It is the first reel on the account whose line 1 names the recipient before it names Jacob.
- Subject: no truck, no 7.3, a stranger with no truck sees himself. That is the 11-22 community rule, and the slot variable ("personal no-truck talking head in the afternoon") is the right test to run before Tuesday.
- Audio chain and delivery tags are to spec. Nothing technical will cost it views.

### What it got wrong

- **Frame 1 is a static handheld face.** Playbook/12: "Never a static face on frame 1." Rule 20: every talking shot opens with a move. The hook atlas: every reel above 1 percent sends moved in frame 1 or had an element entering by 0.33 s. The lockup appearing at 0.13 s is the only change; the face does nothing.
- **The opening line has no noun and no stake by 0.9 s.** "Even if life is really hard right now" is a feeling, not a situation. The account's own low-skip opens are concrete ("Why companies hate your truck", a shop dog, a gooseneck). The stranger test in sentence one (rule 96) is not met until the people segment.
- **Segment order dips where the drop-off lives.** The emotional peak runs 0 to 13 s, then the slowest material (the Sunday reflection, 22 s of it) follows. The account's average watch on talking heads is 14.8 s; the cut puts its lowest-energy block at 13 to 35 s with no re-hook at a third or two thirds.
- **It is about Jacob's people, not the viewer's.** Rule 3 (the reel is about the viewer's people) and rule 105 (one person, "you" for what they want, "I" for the failures) are the sends rules, and the account's own talking heads share at zero because they never turn to the viewer. The caption turns to the viewer; the footage never does.
- **Four cuts with punch-in alternation on handheld footage.** The alternation exists to hide jump cuts on a locked camera. Handheld already moves, so the 1.00 / 1.06 step reads as a tell, and none of the four cuts lands on a gesture because the source was not shot for it.
- **64 s of burned captions on a face.** The caption audit: talking-head captions never on the face; diesel winners mostly burn none. With the face half out of frame at times (reels-made's own honest note), the captions will sit on it.
- **Ending on the build and the stress** hands a relatable piece back to the truck in the last ten seconds, the opposite of the 11-22 rule and of the "answer held" shape, which wants the gratitude line as the close, not as the open.
- **No question that splits the comments, no sign-off, no cliffhanger.** Three items from the playbook/12 shape, all missing because the source has none and nothing was recorded to add them.

### The better cut, specifically

Open (0 to 4 s): the most concrete line in the people segment, the one that names a person and a thing ("my wife", "the shop", "the kid", whichever is there), started mid-sentence, with the lockup landing on its noun at 0.13 s and a single 1.08 push over the first 3 s so something moves. If no such line exists, keep the current open but put the lockup on the word "hard" and add a 6-frame sound-first lead (the porch, wind, a door) before the voice.

Order: people (trimmed to the two most specific sentences, 12 to 15 s), then the stress and the build (10 to 12 s, the honest low point, Jacob's failure in the first person), then "even if life is really hard right now" as the turn (8 s), then the gratitude line as the close and a hard cut within 1.5 s of it. The Sunday reflection goes entirely; it is the "and then" block (question 7).

Cuts: two, not four, each at a breath between segments, no punch-in alternation. The handheld movement is the change.

Length: 40 to 48 s. That contradicts the 60 to 120 rule on purpose: the account's best talking-head watch is 21.7 s and nothing proves a 65 s face hold on this audience yet. A 45 s cut at the same 15 s watch is a third watched; the 65 s cut is under a quarter.

Captions: keep them (muted viewing on a face video), but drop them to the lower band only on the sentences where the face is fully in frame, and let the open run caption-free under the lockup. One accent word per phrase, the noun.

Caption: line 1 as written. Line 2 one real sentence with a number ("Fifteen hour days this month and one truck that doesn't move."). Pinned comment within 60 s repeating the person type and asking the one question that splits the comments ("What's the thing you're grateful for that cost you the most?").

And the honest version: the better cut is a re-shoot. Same script, dash mount in Chief, five takes, eyes at the lens, a line that names the viewer first. Post the porch cut anyway on Sunday or Monday because it exists, the slot is empty, and it tests the only variable the account has never tested: a personal talking head whose caption is about the viewer. Grade it on watch and likes per reach, not sends.

## Question 39. Harley Trade, judged

Facts: 18.5 s, original dialogue, text quote "how much you pay for that truck?" on a static front three-quarter of the F600 for 2.67 s, voice at 2.7 s, payoff at 4.8 s, burned send line and series tag at 27 to 30 px on a 3.5 s static rear-quarter hold at the end. Posted Fri 11-20 15:30 MT.

The read: `reads-48h.tsv` holds a 30.7 h early read (the 48 h read was due 15:30 UTC 11-22 and is still pending in `pending-reads.tsv`): 2,214 views, 1,655 reach, 104 likes, 2 comments, 1 share, 4 saves, skip 38.0, watch 10.8 s, sends per reach 0.06, likes per reach 6.28, saves 0.24. Grade MISS. At 17 h it was 2,161 views, so it stalled between 17 and 31 h.

### What it got right

- Skip 38 against 59 to 75 for every other Rival or build reel this month. The quoted-dialogue hook on frame 1 works as a hook.
- 10.8 s of 18.5 s is 59 percent watched, the only measured watch share on the account and well above the 23 percent the September audit estimated for the old 30 s reels.
- 6.28 percent likes per reach is the highest of the 15 reads in the file and the best on the account this month.
- Original dialogue, no music, real sound: the top-decile diesel mechanics (rule 49).
- Views five to ten times the build baseline on a build subject. The subject was never the problem.

### What it got wrong

- **Nothing moves until 2.67 s and nobody speaks until 2.7 s.** The hook atlas put it against 72 reference reels: every reel above 1 percent sends moved inside frame 1 or had an element entering by 0.33 s. It held because the text asked a question; it did not travel because the first three seconds were a poster.
- **The send line was burned, tiny and late.** The smallest text of 55 reels measured, on a static hold after the payoff that broke the end-within-1.5 s rule. The caption, the field Jacob writes, carried no send reason at all. Withdrawn the same day; the rule since is caption line 1 only.
- **It is about Jacob's trade.** Rule 3 and rule 69 (omgadrian's numbers: the same system shares at 0.5 percent about him and 2.6 to 4.3 percent about the viewer's person). "Traded my Harley for this" is a story people like; "the guy who sold his Harley" is a person people send to. Saves above sends (4 to 1) is the education signature from the measurement protocol, not the tribe signature.
- **Two men talking in a shop is the two-man skit shape (rule 96, 55 to 70 s, turn on the last line) cut to 18.5 s.** It got the dialogue and lost the turn. The payoff at 4.8 s left 13 s of coast.

### The better cut

Frame 1: the two men mid-conversation, Jacob's hand on the fender, voice at 0.0 with the other man's question; the quote as the one lockup on its spoken word, or no text at all (nine of fourteen diesel winners burn none). Cut once to the truck on the word "truck", back to the faces for the answer, punch in 1.08 on "Harley". End on the other man's reaction, hard cut within a second of the payoff; no rear-quarter hold, no burned send line, no tag. Length 12 to 15 s as a loop (the last frame rhymes with the question so it replays), or, if the full exchange has a turn, 45 to 60 s as the skit with the turn held to the last line. Nothing in between.

Caption line 1: "Send this to the guy who sold his Harley for a truck." Line 2 the number ("One Harley, one 1959 F600, zero regrets so far."). Two line-1 variants as a Trial if the toggle is open. Pinned comment names the recipient type again.

## Question 40. Where the rules contradict each other, and which side the evidence takes

Numbers below refer to the addendum (1 to 47) and the diesel hour (48 to 109); MP is the master playbook; P12 is playbook/12; the rule index already records 21 supersessions, so this list holds only live conflicts.

| # | Rule A | Rule B | Account's own numbers | Studied reels | Resolved rule |
|---|---|---|---|---|---|
| 1 | Cut every 2 to 4 s; nothing unchanged over 3 s (MP body, P12 edit, 70, 96 shape A) | Share leaders are one to three shots (49); Mariah no transitions (109); Caleb one locked shot (97); Lana no b-roll (99); menu reels "nothing cuts" (9) | The three best holds (21.7, 18.5, 16.4 s) are one-take talking clips; the 506K meme is one shot with a cutout; the gooseneck is one shot. No cut-heavy reel is in the top ten of anything | Split: software reels change every 0.9 to 1.3 s without cutting; diesel winners one to three shots; the 1M story shape says 2 to 4 s cuts but its own exemplar (DriveHub) is VO over slow coverage | Change, not cut. One take; cut only to remove, and only on a breath or gesture; a change (insert, prop, punch, caption) every 4 to 8 s; at most three cuts per 30 s of face |
| 2 | Nothing 20 to 40 s (96, P12 "do not") | MP templates A 15 to 22, B 25 to 40, C 20 to 35; Sept audit 12 to 18; SE under 20 for sends | Share leaders watch 4 to 8 s (so short); Harley at 18.5 s got views not sends; no reel over 30 s has ever been posted, so 60 to 120 is untested here | 1M table: under 10 s 0 of 228, 10 to 20 s 3 of 435 (0.7 percent), 20 to 40 s 0 of 353, 40 to 90 s 3.0 percent. The ban on 20 to 40 but not 10 to 20 rests on three posts | Two lengths by job: loop or meme 6 to 20 s, story or skit 45 to 120 s. The 20 to 40 ban stands for narrated story only. The first 60 s talking head is a test, not a rule, until one reads |
| 3 | Never a static face on frame 1 (20, P12) | Kitton 30 s in a car (103), Lana on one sofa (99), Caleb locked shot (97) all open on a seated face | "Why companies hate your truck" (29.8 skip, best hold) is a seated one-take face; the seven personal talking heads median 29.8 skip with, as far as the notes say, no openers | The studied talking heads open static and win on the first sentence; the diesel action winners open on motion | The sentence is the opener on a talking head; the move is optional. A static face with a noun by 0.9 s beats a walk-in with "so today" |
| 4 | Face late, truck first (96 shape A "his face late", 8 "truck or part visible on frame one", DriveHub face at 12 s) | Daily talking head: face at 0.0 in the truck (P12, 98); community rule: the truck is backdrop | Face-first reels hold 14.8 s at 29.8 skip; truck-first or part-first reels (build, sponsor) skip 51 to 71 | Story shape winners open on the subject (truck, barn) with VO; talking heads open on the face | Rule 8 is retired for talking heads and memes. Truck first for the narrated Rival story; face first for the afternoon slot |
| 5 | No follow ask, ever (Jacob, 2, P12 "do not") | Mariah "Follow for Part Two" (109), omgadrian asks spoken once late (70), Lana asks (99), Brock digests | Direct asks flopped (link in bio 70.9 skip, "Be a MAN" 57 skip); spoken "tag him" measured 0.03 percent on TikTok; a late spoken follow ask has never been tested here | Three of the four studied growth cases ask, spoken, once, late | No burned ask stands. One spoken line at the end is an untested variable; run it once as a Trial variant against the cliffhanger before calling it banned |
| 6 | Every number and claim typed on screen; captions always (28, MP, P12 captions) | Six of fourteen diesel winners zero text (23); ten of fourteen burn no captions (46); Jacob: one lockup and nothing else on the fast tier | Harley captions were the smallest measured; the 10 mil meme carried a text confession; whether the long-hold talking heads were captioned is not recorded | Talking-head creators caption (17 of 17 in the audit); diesel action reels do not | By tier: talking heads captioned, chest band, never on the face; action and sound reels one lockup or nothing; memes the confession text only |
| 7 | Series title held top centre for the whole episode (P12 series section, 102) | Title in the upper third only during the open, off by 3 s (P12 edit section, same page); Jacob: one poster lockup on the hook | No held-title reel exists | Kitton holds for 30 s; Gaffney holds; Caleb does not | Internal contradiction on one page. Hold the series lockup small for the whole episode on the daily format only; everything else off by 3 s. Jacob picks |
| 8 | Sends per reach floor 1 percent, goal 2, under 1 means the format failed (6) | Daily talking head graded at 48 h on sends (P12 posting) | No face held past 10 s has cleared 0.7 percent in 71 reels; talking heads median 0.00; memes median 0.56 | Lana and Kitton grow on talking heads at low shares, high completion | Grade by format: memes and loops on sends (floor 1); talking heads on watch share (floor 50 percent) and likes per reach (floor 4), sends logged not graded |
| 9 | The reel is about the viewer's people, not about Jacob (3) | PERSONAL is the best pillar (Sept 14.8 percent); "I" owns the failures (105); Lana's one-seat personal format (99) | Personal clips 6.4 percent likes per reach, 0.23 sends; memes 0.56 sends. Both true at once | Personal subject with a viewer-facing line is the Boyfriend Bootcamp pattern (69) | Subject personal, address the viewer: "I" in the footage, "you" in line 1 and in sentence one |
| 10 | Pilot line "if you're new here, I'm Jake" at 15 to 20 s (P12) | Never "hey guys", nothing that needs explaining, first noun by 0.9 s (MP, 57, 94) | None | Lana tucks the credential into a sentence already doing work (99); nobody studied stops to introduce | Credential inside a working sentence ("I order parts for semis all day, and..."), never a standalone intro line |
| 11 | Re-hook at a third and two thirds (MP, P12) | Mariah, Caleb, Kitton, Lana run one line of argument with no scheduled re-hook | None; no reel long enough to have one | The long-hold winners re-hook by information (open loops), not by device | Open loop in sentence one, close it last; no scheduled re-hook device. Question 15 is right that the schedule is inherited from YouTube |
| 12 | Punch-in alternation 1.00 / 1.12 on consecutive talking clips (MP dialogue) | Cut on motion only (70, P12); handheld moves already | The gratitude cut used 1.00 / 1.06 on handheld; unread | Documentary practice: hide the cut on a gesture, not a zoom | Alternate punch only on a locked tripod; never on handheld; never both a punch and a cut on the same join |
| 13 | SFX two or three per reel (27); whoosh one cut in four (MP) | Mariah and omgadrian no SFX (70, 109); skill: SFX off on the fast tier | Every sharing reel on the account has no SFX | Talking-head winners none; menu reels on objects only | None on talking heads and memes; objects only on card reels |
| 14 | Song in-app always (28) | Top five meme templates have no melodic bed; cold starts real sound (23, 52) | The 10 mil meme ran a sound; Harley ran original audio and held | Format-dependent | Song on montage and lyric formats; original sound on dialogue, memes with a line, and anything with an engine |
| 15 | Skip under 40 (CLAUDE.md), under 45 floor and 35 goal (6) | Sept craft: under 20 excellent | Every reel under 40 this month cleared 1,000 views; every reel over 60 stayed under 600; median is 45.6 | Breakout median 45 | 40 as the gate, 30 as the goal; 45 is this account's median, so it is not a target |
| 16 | Two posts a day for days 1 to 15 (88) | 3 reels a week sustained (content plan); 3 to 4 a week floor (rule index 8); 3 to 6 a day in month one (61) | 20 reels in 20 days in November: median views fell to 350 to 550 on the thank-you half; the dark stretches in June to September were the costliest pattern | Fast growers front-load; Mariah films a day ahead | Two a day only while half are banked; the shout-out half is cut to Stories; floor three a week forever |
| 17 | One topic per reel, never a meme beat and a build update together (8) | "The fix is a shareable line inside the held reel, not a new format" (11-12 refresh, reels-made) | Nothing posted yet does both; Harley was the first attempt and did one half | Numbers x named-tribe news is the one cell that does both (87) | One topic, two registers: a build fact delivered in the meme voice. The classifier rule bans two topics, not two tones |
| 18 | Trial Reels at 1,000 (CLAUDE.md, content plan) | 200 for professional accounts (7) | Unverified | Four guides | Check the composer; unresolved until Jacob looks |

The pattern across the eighteen: where the account's own numbers and the studied reels agree (change not cut, sentence not move, format-specific grading), the rule files were written from the software-reel studies and need the correction. Where they disagree (the follow ask, length over 40 s), the account has no data at all, and the honest rule is "test once" rather than either side.

## Ten things our own data proves

1. Skip under 40 is the gate to being seen: below the median skip (45.6) reels get 4.4 times the median views and 5.8 times the shares per reach (n=71).
2. Skip no longer predicts sends once the reel is seen: correlation 0.00 at n=57 with the outliers out. Hook quality and send quality are separate skills.
3. Holding and sending are inversely related here: watch versus shares per reach correlates at minus 0.21; the 20 reels watched past 10 s share at 0.02 percent median, the 39 under 7 s at 0.30.
4. Talking heads are the best hook on the account (29.8 median skip, 14.8 s watch) and have never produced more than 4 shares.
5. Memes are the only format that does both: 1,988 median views, 0.56 percent median sends, 39 skip, and all seven of the account's own share leaders.
6. Product, thank-you and ask openers lose two thirds of viewers in three seconds (71.3 median skip on ten reels, 350 median views) regardless of the brand or the reach.
7. Short first-person clips with a caption carry the highest likes per reach (6.4 percent); that is the September "PERSONAL 14.8 percent" number, and it was never a talking head.
8. The skit sends even with a dead first frame (mechanics skit, 72 skip, 3.6 percent sends on 385 reach); the joke is the format, the first frame cost it the reach.
9. Original dialogue on frame 1 fixes the build-reel hook: Harley Trade 38 skip against 59 to 75 for every other Rival reel, 59 percent watched.
10. Static posts are dead at every follower count tried: 13 images and carousels, 30 to 173 reach each, against a reel median of 496 views.

## Ten things it cannot prove yet, and the post that would test each

1. Whether a 60 s face hold works here. No reel over 30 s has been posted. Test: the gratitude cut, graded on watch share, against a 45 s recut of the same footage a week later.
2. Whether a talking head can send at all. Test: one Trust episode whose first spoken line names the recipient ("send this to the guy who still runs the stock CP4"), caption line 1 the same, graded at 48 h.
3. Whether a late spoken follow ask costs or earns. Test: the same episode as two Trials, one ending on the cliffhanger, one on "follow for the part that came back three times."
4. Whether a static seated open loses to a move. Test: the same script filmed twice in Chief, one door-shut walk-in, one seated with the sentence at 0.0, posted a week apart.
5. Whether captions on a face raise completion. Test: one talking head posted with captions, its Trial twin without; the account has never run a captionless face.
6. Watch share by length, because duration is not stored. Test: add `duration_s` to the pull (ffprobe on the yt-dlp file) and backfill the 71 reels before any length rule is argued again.
7. Whether a build fact in the meme voice sends. Test: "10 mil part 2" with one real Rival number inside it (the frame swap cost), caption line 1 a person type.
8. Whether the two-man skit shape at 55 to 70 s beats the 18 s cut. Test: the counter skit ("parts is not a trade", rule 96) in one shot with the turn on the last line.
9. Whether Trial Reels are open at 577 followers and whether two line-1 variants move sends. Test: Jacob opens the composer; first Trial is the gratitude cut with two first lines.
10. Whether the profile converts talking-head viewers better than meme viewers. Test: profile visits and follows from the account-level pull on a talking-head day against a meme day, same week, since the media level cannot attribute follows.
