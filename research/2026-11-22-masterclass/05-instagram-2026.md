# Cluster G: how Instagram Reels rank and behave, November 2026

Research agent, 2026-11-22, questions 27 to 31 of `00-questions.md`. This file extends `research/2026-11-21-live-instagram-algorithm.md` (the October and November 2026 sweep) and `research/2026-11-20-instagram-ranking-and-capcut-recipe.md`. It does not repeat their source lists; it adds the 2024 and early 2025 primary statements those files skipped, puts every ranking statement on one dated line, grades each source, and says what moved in the last six months.

Method note. WebSearch ran in two waves (standard for pre-2026 items, extended for 2026 items) before the session's shared search budget ran out. WebFetch failed on every host tried (socialmediatoday.com, creators.instagram.com, about.fb.com, buffer.com, creatorhouse.app all return ENOTFOUND in this container), so Instagram's own pages are quoted through press coverage and the 11-21 file's transcripts. Where a number comes only from a vendor blog it says so. Grades: **official** (Instagram, Meta, Mosseri, Help Center), **measured** (a dataset with a stated sample), **creator** (one account's experience or an educator's claim).

What changed since the 11-21 file was written, in one paragraph: nothing in the ranking framework. The new facts below are confirmations and corrections. The Trial Reels floor of 200 followers for professional accounts now has a Help Center citation with a date (November 6, 2026) from two independent guides, which upgrades it from "unconfirmed" to "probable, verify in the composer." The "Views as primary metric" change was announced in August 2024, not April 2025; April 21, 2025 is the API cutover. The skip rate metric dates to August 2025 and replaced "view rate." Mosseri's "sends per reach" line is from spring 2024, a year before the "three signals" video. One new measured source on Trial Reels (a 14-day, 20-reel test) and one new measured source on cadence (Buffer, 2.1M posts) are added.

---

## 27. What ranks a Reel now

**Answer.** Instagram's public position has been stable since January 2025 and Mosseri restated it in October 2026: the three signals that matter most for Reels are average watch time, likes per reach and sends per reach, with likes weighing slightly more for followers and sends slightly more for non-followers. Underneath those sit the 2023 prediction list (reshare, watch through, like, go to the audio page) which has never been retracted. The 2026 additions are not new signals but new ranking goals layered on top of engagement prediction: originality, "breakouts" (every post gets a chance with strangers) and recency. Completion and "3-second views" are not named by Instagram as ranking inputs; completion shows up only as the watch-through prediction, and the 3-second threshold exists only as the skip rate metric in Insights. Comments are explicitly down-weighted ("not the most important part of value by a long shot," October 2026) and watch time is explicitly lower-weighted than on TikTok ("we focus way less on watch time than all the competition does, but we do care about watch time").

**Sources.**
- Instagram blog, "Instagram Ranking Explained," May 31, 2023, https://about.instagram.com/blog/announcements/instagram-ranking-explained. "The most important predictions we make are how likely you are to reshare a reel, watch a reel all the way through, like it, and go to the audio page." Official.
- Mosseri Reel on sends, spring 2024 (press coverage dates it April to May 2024), via Uppbeat https://uppbeat.io/blog/creator-news/whats-working-on-instagram-right-now-carousels-and-sends-says-adam-mosseri and Social Media Today https://www.socialmediatoday.com/news/instagram-chief-post-share-rates-key-driver-reach/716540/. "One of the most important signals we use in ranking is sends per reach." Rate beats count. Official (quoted).
- Mosseri video, January 2025, via Social Media Today https://www.socialmediatoday.com/news/instagram-shares-algorithm-insights-2025/738034/ and t3n. Watch time, likes, sends as the top three; track average watch time, likes per reach, sends per reach; likes slightly more for connected, sends slightly more for unconnected. Official (quoted).
- Mosseri, Colin and Samir interview, recorded October 23, published October 26, 2026, https://www.youtube.com/watch?v=sxizdQ2hRfk. "Sends per reach is what is particularly important for that unconnected reach." Originality, breakouts and recency named as ranking goals. Official (verbatim from transcript, in the 11-21 file).
- Mosseri Stories AMAs October 16, 23 and 30, 2026, via ZoomSphere https://www.zoomsphere.com/blog/instagram-algorithm-2026-what-actually-gets-reach. Comments down-weighted; third-party editors not demoted; visible foreign logo demoted. Official (secondhand).
- Mosseri on Threads, late October 2026, https://www.threads.com/@mosseri/post/DQZibhAifap. Explains connected vs unconnected reach on a creator's insight (2.8 percent of viewers were followers, over 10 million views from non-followers). Official.
- Social Media Today, "Instagram engagement rates provide insight into reach," 2026, https://www.socialmediatoday.com/news/instagram-engagement-rates-provide-insight-into-reach/821170/. Mosseri: "of all the people who saw the post, how many of them actually engaged with that post?" Official (quoted).
- Meta explainer on "Your Algorithm," November 11, 2026, via Social Media Today https://www.socialmediatoday.com/news/meta-publishes-explainer-on-your-algorithm-controls/874460/. LLM-built topic profiles, per-creator "see less" filters, topic balancing. Official (secondhand).
- Creator Lane, "Mosseri Says vs What Creators Measure," August 30, 2026, https://creatorlanehq.com/blog/instagram-algorithm-2026-mosseri-vs-measured. Notes the "3 to 5x sends weighting" and "two-way conversation signal" have no Instagram source. Creator claim (useful as a debunk).
- dev.to and SocialPilot "3 official ranking factors" guides, 2026, https://dev.to/stklen/instagram-reels-algorithm-2026-the-3-official-ranking-factors-mme. Repeat the January 2025 list and add unsourced weights. Creator claim; ignore the weights.

**Not official, treat as folklore:** sends weighted 3 to 5x likes; a "two-way conversation" signal from March 2026; a 70 percent originality similarity threshold; a 10-reposts-in-30-days aggregator rule (the official page says "most" of recent posts, not a count).

**Confidence:** high on the signal list and its order; high that nothing was added in 2026; medium on the relative weight of watch time versus sends, since Mosseri gives no numbers.

---

## 28. Trial Reels: eligibility, graduation, hook testing

**Answer.** Trial Reels launched December 10, 2024 and opened widely in July 2025. Two guides (dated November 6, 2026 and one from August 2026) quote the current Help Center as: public account, at least 200 followers for a professional (Business or Creator) account, 1,000 for a personal account, and the account must be eligible for recommendations (check Account Status). The @elcoyotediesel account is a Creator account at about 580 followers, so the toggle should be present; Brock Johnson still said 1,000 on November 19, so this is probable rather than certain until someone opens the composer. Mechanics from Meta's own launch post: the reel is shown only to non-followers, does not appear on the grid or in followers' feeds, metrics appear about 24 hours after posting with a comparison to prior trials, and if auto-share is on Instagram will push it to followers when it is performing well on views in the first 72 hours; you can also share it manually at any time. Creator tests agree it is a hook-testing surface, not a reach hack: non-follower reach goes up (2.3x in one 20-reel test), engagement per view goes down (0.6x), and the net follower gain is modest (1.4x) and concentrated in a few winners.

**Sources.**
- Meta Newsroom, "Test Content With Non-Followers Using Trial Reels," December 10, 2024, https://about.fb.com/news/2024/12/trial-reels-try-content-non-followers-first/. 24-hour metrics, 72-hour auto-share rule, eligibility deferred to Help Center. Official.
- Instagram @creators blog, same day, https://creators.instagram.com/blog/instagram-trial-reels. Official.
- Betanews, "Instagram opens up trial reels to more creators," July 14, 2025, https://betanews.com/2025/07/14/instagram-opens-up-trial-reels-feature-to-more-creators/. Wider rollout. Press.
- Exemplary.ai, https://exemplary.ai/blog/instagram-trial-reels, and AI Social Media Now, https://www.aisocialmedianow.com/blog/instagram-trial-reels. Both quote the US English Help Center (article 1013292530224018) as 200 followers professional, 1,000 personal, dated as of November 6, 2026 in the first. Official (quoted through a vendor); the page itself would not load here.
- flowgent, October 29, 2026, https://flowgent.ai/blog/instagram-trial-reels; vidova, https://vidova.ai/blog/instagram-trial-reels-explained; metrik, https://metrik.social/blog/instagram-trial-reels. Same 200 figure. Creator claim, corroborating.
- Postfa.st and Reshma Shaji guides, 2026, still say 1,000 for professional accounts; Plumefy says no hard threshold is published. Creator claim, conflicting.
- Brock Johnson, November 19, 2026, https://www.youtube.com/watch?v=6i6T33SAIRc. "1,000 followers and a professional account." Creator claim, conflicting.
- Mosseri AMAs, October 16 and 30, 2026 (ZoomSphere link above). Experimenting with Trial Reels does not hurt the account; several different Trials in a day is fine; reposting the same Trial will be cracked down on. Official (secondhand).
- Creatorhouse, "Trial Reels: We Ran a 14-Day Test on a Real Account," 2026, https://creatorhouse.app/blog/trial-reels-14-day-test-2026. 4,200-follower account, 20 reels, 14 days: 2.3x non-follower reach, 0.6x engagement, 1.4x net follower conversion; conclusion: use as a hook A/B surface. Measured (n = 20, one account).
- Millie Adrian via Soundstripe and brandID, 2026, https://www.soundstripe.com/blogs/what-are-instagram-trial-reels, https://brandid.app/blog/instagram-trial-reels/. About 2,600 followers from about 75 Trials in 15 days, 90 percent from two talking-head videos that had already worked. Creator claim.
- Instagram's own claim (undated, quoted by Soundstripe and brandID, the latter says June 2026): 40 percent of creators who tried Trials posted more often and 80 percent of those saw higher non-follower reach. Official (secondhand, unverified).
- Buffer, Trial Reels guide, https://buffer.com/resources/instagram-trial-reels/. Two versions, one variable changed, judge at about 24 hours. Creator claim from a vendor.

**Graduation in practice.** Winners graduate by one of three routes: auto-share on the 72-hour views test, a manual "share to followers" tap, or (the common creator pattern) re-shooting the winning hook as a normal Reel. Trial Reels are ranked separately from feed Reels, so a Trial that flops has no recorded effect on the next feed post (Mosseri, October 16). Reposting the identical file as a second Trial is now flagged as a duplicate.

**Confidence:** high on mechanics; medium-high on the 200 floor (two Help Center quotations, one dated this month, versus one educator still saying 1,000); medium on the creator numbers.

---

## 29. Length: does longer help a 500-follower creator

**Answer.** Facts first. Reels went to 3 minutes on January 17 and 18, 2025 (Mosseri's post coincided with the TikTok shutdown weekend), uploads now allow 20 minutes, and the composer warns that anything over 3:00 is not eligible for non-follower recommendation. "Views" became the headline metric across all formats in August 2024; the API dropped Impressions and Plays on April 21, 2025 after a January 8, 2025 developer notice. On length versus reach the two big 2026 datasets disagree because their samples differ: Socialinsider (9.77M brand Reels, January to June 2026) has reach rate peaking at 30 to 60 seconds and falling steadily after 90, while Buffer (2.73M Reels, January to August 2026, each account against its own baseline) has 90 to 179 seconds at plus 7.4 percent reach and everything 180 seconds or longer at minus 49 percent. Neither splits by follower tier for length, so there is no measured curve for a 500-follower account specifically; the nearest is Socialinsider's finding that 1k to 5k accounts have the highest reach rate of any tier (9.78 percent) and the highest skip rate (65.5 percent), which argues for short until the hook is fixed. Instagram does not publish retention curves by length; the in-app curve is per reel, and the creator benchmark that fits this account's data is heyDominik's: a 30-second reel needs about 8 to 11 seconds average watch to break out, a 60 to 90 second reel about 18 seconds. Mosseri's own line is "the shorter the better" and Tessa Lyons (November 3, 2026) favours short vertical Reels with long form moved to horizontal "Features."

**Sources.**
- Mosseri announcement of 3-minute Reels, January 2025, via Marketing Dive https://www.marketingdive.com/news/instagram-reels-tips-3-minutes-unfiltered-nyc/742335/ and David Zucker https://davidzucker.substack.com/p/three-minute-instagram-reels-have. Official (quoted).
- PetaPixel, "Instagram Makes Views The Primary Metric," August 8, 2024, https://petapixel.com/2024/08/08/reels-stories-carousels-likes-followers-instagram-will-now-focus-on-views-in-metrics-for-photos. Official (quoted).
- SocialPilot, "Instagram Metrics Changes: From Impressions and Plays to Views," https://www.socialpilot.co/instagram-marketing/instagram-views-metrics-changes. January 8, 2025 developer notice, April 21, 2025 API cutover. Vendor summary of an official notice.
- Brock Johnson, November 19, 2026 (link above). 20-minute cap, in-composer warning above 3:00. Creator claim consistent with Help Center text quoted in the 11-20 file.
- Socialinsider Reels benchmarks, updated November 17, 2026, https://www.socialinsider.io/blog/instagram-reels-statistics/. Reach by length and by tier, skip rate by tier. Measured (9.77M posts).
- Buffer, "How Long Should Instagram Reels Be?", November 12, 2026, https://buffer.com/resources/instagram-reels-length/. Measured (2.73M posts).
- Metricool 2026 Instagram Study, https://metricool.com/press-release-instagram-study-2026/, and Sotrender, August 2026, https://www.sotrender.com/blog/2026/08/instagram-reach-is-down-what-the-data-actually-says/. Average watch time 8.5 seconds; Reels reach down about 35 percent year over year; only 21 percent of accounts under 10k growing. Measured (24.4M posts), length split not published.
- heyDominik, October 26, 2026, https://www.youtube.com/watch?v=6u4MGM_KZ5I. Average-watch thresholds by length; 90s+ reels broke out twice as often in his client data. Creator claim with internal data.
- Tessa Lyons with Rachel Karten, November 3, 2026, https://www.linkinbio.news/p/my-call-with-instagrams-vp-of-product. Short vertical, long horizontal, "a direction, not a rule." Official (secondhand).

**Read for this account.** Average watch is 6.8 seconds on roughly 30-second cuts, so the account is below the breakout threshold at its current length. Longer only helps once average watch clears about a third of runtime; until then every extra second is unwatched runtime that drags the watch-through prediction. The honest test is two Trials of the same story at 25 seconds and 55 seconds.

**Confidence:** high on the dates and limits; medium on length versus reach (two large datasets disagree and neither is tiered); low on any claim about a retention curve by length, because none is published.

---

## 30. Originality, aggregators, the repost label, cross-posting

**Answer.** Three separate things get confused here. (1) The originality ranking rule, April 30, 2024: Instagram replaces a repost with the original in recommendations when the original is recent and the match is confident, labels reposts with a link to the original creator, and removes aggregator accounts from recommendations until most of their recent posts are original again over a 30-day window; low-effort edits such as adding a watermark, border, or a sticker do not make content original. April 30, 2026 extended the same rules to photos and carousels. (2) The Reposts product, August 6, 2025: a repost button that puts the item in a separate Reposts tab on your profile with credit to the original poster; this is the sanctioned way to share someone else's work and is not the same as the originality label. (3) Content protection, November 17, 2026: enrolled original creators can see, track, hide or add a credit link to copies of their videos. Cross-posting your own master to TikTok and Shorts is not penalised as such; Mosseri has said repeatedly that content made in other apps is not demoted and that your own logo is fine, but a visible TikTok, CapCut or YouTube watermark keeps the Reel out of recommendations (a rule since February 2021, restated October 2024 and October 30, 2026). Instagram has given no indication that it detects "this video also exists on TikTok"; what it detects is visual and audio matches to other Instagram posts and foreign logos in the frame.

**Sources.**
- Instagram @creators, "Rewarding original creators on Instagram," April 30, 2024, https://creators.instagram.com/blog/rewarding-original-creators-on-instagram, and the standing page https://creators.instagram.com/recommendations-and-originality. Official.
- TechCrunch, April 30, 2024, https://techcrunch.com/2024/04/30/instagram-is-updating-its-ranking-systems-to-surface-more-content-from-smaller-original-creators; Engadget, same day. Press on the official post.
- Instagram @creators, April 30, 2026 extension, via TechCrunch https://techcrunch.com/2026/04/30/instagram-restricts-reach-of-content-aggregators-in-new-crackdown/, PetaPixel https://petapixel.com/2026-04-30/new-instagram-policies-target-reposted-content/, Tubefilter https://tubefilter.com/2026/04/30/instagram-removes-algorithm-recommendations-repost-content-aggregator. "Can become eligible again when most of their recently posted photos, carousels and reels are considered original in a 30-day period." Official (quoted).
- Meta Newsroom, "New Instagram Features to Help You Connect," August 6, 2025, https://about.fb.com/news/2025/08/new-instagram-features/; PetaPixel https://petapixel.com/2025/08/06/instagram-adds-a-reposts-tab-to-users-profiles-similar-to-tiktok/. Reposts tab and credit. Official.
- Instagram @creators, "Introducing content protection," November 17, 2026, https://creators.instagram.com/blog/introducing-content-protection/. Official (details in the 11-21 file).
- Mosseri on logos, October 2024, via Social Media Today https://www.socialmediatoday.com/news/instagram-clarifies-including-your-own-logo-on-a-reel-is-ok/730852/. Own logo fine; other apps' logos not recommended. Official (quoted).
- Tubefilter, February 10, 2021, https://www.tubefilter.com/2021/02/10/instagram-reels-with-tiktok-watermark-less-discoverable/. The original watermark rule. Official (quoted).
- Hootsuite experiment, 2024, https://blog.hootsuite.com/experiment-reels-editing-app/. CapCut-edited (clean export) Reels reached 2,712 vs 1,672 for in-app edits. Measured (small n).
- Mosseri AMA, October 30, 2026 (ZoomSphere link above). "We don't demote content for being created with other apps other than ours." Official (secondhand).
- gotmenow, socialync, syncstudio "originality score" posts, 2026. Specific thresholds (70 percent similarity, 10 reposts) appear only here and contradict each other. Creator claim; disregard the numbers.

**What counts as original when one master goes everywhere.** Original means you made it and it is not already circulating on Instagram. The same clean 1080x1920 export can go to Reels, TikTok and Shorts; keep the Instagram upload free of any other platform's logo, template watermark or caption bar, add the song inside Instagram rather than baked into the file, and post to Instagram first or same-day so that if anyone clips it the Instagram copy is the earlier match. Reposting your own Reel to a second account you run should go through the Reposts button or the content protection allow list, not a re-upload.

**Confidence:** high on the rules and dates; high on the watermark rule; medium on how matching works internally, since Instagram describes it only as "audio and visual signals."

---

## 31. Cadence versus quality under 1,000 followers

**Answer.** The only large dataset on frequency (Buffer, about 2.1M posts from over 100,000 accounts, published August 13, 2025) found reach per post rising with weekly volume: about 12 percent higher at 3 to 5 posts a week, 18 percent at 6 to 9 and 24 percent at 10 or more, against 1 to 2 a week, with the share of your own audience reached per post falling as volume rises. Buffer's October 2026 refresh adds that consistent posters earn almost 5x the engagement per post of irregular ones. Socialinsider's 1k to 5k brand tier averages 8 Reels a month. Mosseri's standing advice is two feed posts a week and a couple of Stories a day, with "the more you post the more reach, but watch out for burnout," and in October 2026 he named recency as a ranking goal, which is the mechanical reason volume helps. The documented small-account experiments go the other way on quality: Lilach Bullock's daily-versus-three-a-week test gained reach (41.2k vs 38.9k) but lost watch-through (31 vs 44 percent) and followers (118 vs 146); Katie Kinsley's 30 daily Reels gained about 96 followers. Nobody has published a controlled test at two a day on a sub-1k account. The honest reading is that the second daily post is worth it only if it is a different format with its own hook, because at this follower count reach comes from strangers and the stranger judges each Reel alone.

**Sources.**
- Buffer frequency study, August 13, 2025, via Social Media Today https://www.socialmediatoday.com/news/study-shows-posting-more-instagram-leads-to-more-reach/757633/ and Buffer https://buffer.com/library/how-often-to-post-on-instagram/. Measured (2.1M posts).
- Buffer algorithm guide refresh, October 23, 2026, https://buffer.com/resources/instagram-algorithms/. Consistency and reply-to-comments correlations. Measured (4M+ posts, correlational).
- Socialinsider, November 17, 2026 (link above). 8 Reels a month at 1k to 5k. Measured.
- Mosseri @creators Q&A on frequency, via Social Media Examiner https://www.socialmediaexaminer.com/how-to-determine-your-ideal-instagram-posting-frequency/ and RouteNote https://routenote.com/blog/how-often-you-should-post-on-instagram/. Two feed posts a week, Stories daily, more posting more reach, burnout warning. Official (quoted, undated, pre-2025).
- Mosseri, October 23, 2026 (Colin and Samir). Recency as a ranking goal. Official.
- Lilach Bullock, https://www.lilachbullock.com/how-many-instagram-reels-should-you-post/. Daily vs 3x a week, one business account. Creator (one account, dated "a few years ago").
- Katie Kinsley, "I Posted One Reel a Day for 30 Days Straight," 2022 updated 2026, https://www.katiekinsley.com/i-posted-one-reel-a-day-for-30-days-straight/. About 96 followers in 30 days ending at 1,029. Creator.
- Robert Benjamin, November 4, 2026, https://www.youtube.com/watch?v=j3WILAPvgzo. 1 to 2 feed Reels plus 5 Trials a day; "45 percent of recommended Reels under a day old" (unsourced). Creator claim.
- Viralday and Sooper "frequency cap over 2 a day" claims, 2026. No source given. Creator claim; no Instagram statement supports a cap.

**Confidence:** medium. The volume-helps finding is measured but from brands with teams and feed posts of all kinds; the quality-cost finding is real but n = 1. The two-a-day question for a one-man account is untested in any public dataset.

---

## New in the second half of 2026 (not covered or only partly covered in the earlier files)

- August 2025 (context): Reels retention chart and skip rate added to Insights, skip rate replacing "view rate"; definition is the share of views that left within 3 seconds. Social Media Today https://www.socialmediatoday.com/news/instagram-adds-retention-insights-reels/758464/. Official.
- April 26, 2026: Insights rebuilt (Overview, Engagement, Audience); share rate, skip rate and views over time at the top of each post. inro.social https://www.inro.social/blog/instagram-insights-update and only.ag. Vendor reports, no Instagram post located.
- April 30, 2026: originality rules extended to photos and carousels. Official.
- August 6, 2025 and 2026 follow-ups: Reposts tab; Friends tab in Reels global; a "Following" tab in Reels in test (SocialBee, November 16, 2026, https://socialbee.com/blog/instagram-updates-news-features/).
- October 9, 2026: "Open to Reels" home layout test. PetaPixel.
- October 26, 2026: Features (horizontal up to 90 minutes) and Clips as Reels; October 28: linked Reels series removed, Series format in international test.
- November 5 to 19, 2026: Edits on Mac with direct Trial Reel publish, speed curves, auto audio mixing, Edits Cloud. Windows still unsupported.
- November 11, 2026: Meta explainer on Your Algorithm topic profiles. Official.
- November 16, 2026: Amazon and other affiliate links inside Reels, 30 products per Reel. Official.
- November 17, 2026: content protection. Official.
- November 20, 2026: Insights redesign in test again (Home, Performance, Content, Audience) with a Trial reels shortcut and content sortable by follows (Geekout).
- Unchanged all year: three-signal framework, 3:00 recommendation ceiling, 5-hashtag cap (December 18, 2025), no demotion for third-party editors, demotion for foreign logos.

---

## Timeline of ranking statements, 2024 to 2026

| Date | Who | Statement | Grade |
|---|---|---|---|
| Feb 10, 2021 | Instagram | Reels with a visible TikTok logo made "less discoverable" | official |
| May 31, 2023 | Mosseri, Instagram blog | Reels predictions: reshare, watch all the way through, like, go to the audio page; most of Reels is from accounts you do not follow | official |
| Apr to May 2024 | Mosseri Reel | "One of the most important signals we use in ranking is sends per reach"; rate, not count | official |
| Apr 30, 2024 | Instagram @creators | Originality: replace reposts with originals, label reposts, remove aggregators from recommendations; small creators get more chances with non-followers | official |
| Aug 8, 2024 | Instagram | Views becomes the primary metric across formats | official |
| Oct 2024 | Mosseri | Your own logo on a Reel is fine; other apps' logos are not recommended | official |
| Dec 10, 2024 | Meta Newsroom | Trial Reels: non-followers only, metrics at 24 hours, auto-share on 72-hour views | official |
| Jan 8, 2025 | Meta developers | API notice: Impressions and Plays retired for Views, effective Apr 21, 2025 | official |
| Jan 17 to 18, 2025 | Mosseri | Reels up to 3 minutes | official |
| Jan 2025 | Mosseri video | Top three signals: watch time, likes, sends; track average watch time, likes per reach, sends per reach; likes lean connected, sends lean unconnected | official |
| Jul 14, 2025 | Instagram | Trial Reels opened to more creators | official |
| Aug 6, 2025 | Meta | Reposts tab with credit; Friends tab in Reels | official |
| Aug 2025 | Instagram | Retention chart and skip rate in Insights; skip rate replaces view rate | official |
| Dec 18, 2025 | @creators | Five hashtags maximum | official |
| Apr 26, 2026 | Instagram (vendor-reported) | Insights redesign, share rate and skip rate surfaced | vendor |
| Apr 30, 2026 | Instagram @creators | Originality rules extended to photos and carousels | official |
| 2026 (first half) | Mosseri | Judge a post by engagement among those who saw it, not by reach | official (quoted) |
| Oct 16, 2026 | Mosseri AMA | AI content not throttled; Trials do not hurt the account; reposting the same Trial will be cracked down on | official |
| Oct 23, 2026 | Mosseri AMA | "We focus a lot more on finding reels and photos that you might send to a friend"; comments "not the most important part of value by a long shot" | official |
| Oct 23, 2026 | Mosseri, Colin and Samir | Sends per reach "particularly important" for unconnected reach; originality, breakouts, recency as ranking goals; "we focus way less on watch time than all the competition" | official |
| Oct 30, 2026 | Mosseri AMA | No demotion for other editing apps; visible foreign logo gets less distribution; several different Trials a day is fine | official |
| Nov 3, 2026 | Tessa Lyons | Short vertical Reels, long horizontal Features, "a direction, not a rule" | official |
| Nov 6, 2026 | Help Center (as quoted) | Trial Reels: 200 followers professional, 1,000 personal, public, recommendation-eligible | official (quoted) |
| Nov 11, 2026 | Meta | Your Algorithm: LLM topic profiles, per-creator see-less filters, topic balancing | official |
| Week of Nov 13, 2026 | Mosseri | "Following counts still matter on Instagram more than they do on platforms like TikTok" | official (via Geekout) |
| Nov 17, 2026 | Instagram @creators | Content protection launched; exploring reach limits for repeated AI-generated posting | official |

---

## What it means for a 500-follower diesel creator posting two reels a day

1. Build every reel for one send, not for comments. The one signal Instagram has called out by name in 2024, 2025 and 2026 is sends per reach, and it is the one that moves non-follower reach, which is where almost all of this account's views already come from. Before the shot list, write the line a viewer would text to his buddy. If there is no such line, it is a Story.
2. Treat skip rate and average watch as a pair. Skip rate under 45 percent gets the reel past the first three seconds; average watch over about a third of runtime gets the watch-through prediction. The account sits at 48 percent skip and 6.8 seconds on 30-second cuts, so the fix is shorter cuts and a stronger frame one, not more cuts inside the reel.
3. Stay under 60 seconds for anything meant to reach strangers until average watch clears 10 seconds consistently. Both 2026 datasets agree that under 30 seconds and over 3 minutes are the losers; they disagree in the middle, and the account's own watch time settles the argument in favour of short.
4. Open the Reels composer and look for the Trial toggle today. If it is there at 580 followers, the second reel of the day becomes a Trial: same story, different first three seconds, judged at 24 hours on skip rate and sends, winner re-shot or shared to followers. Never post the identical file twice as a Trial.
5. Two a day is fine only as two different formats. The measured data says more posts means more total reach; the creator data says the same person posting more loses watch-through. Pair a 20 to 40 second talking head in the truck with a Trial or a Story-first clip, not two of the same thing.
6. Keep the file clean. No CapCut, TikTok or template logo anywhere in frame, song added inside Instagram, Instagram upload first or same day as TikTok and Shorts. Cross-posting the master is not penalised; the watermark is.
7. Enrol in content protection the day the notification lands and allow-list the shop and any partner account that reposts. For sharing someone else's reel use the Reposts button, which credits them, not a re-upload, which counts against your own originality.
8. Make every reel classify as one thing. The November 11 explainer says Instagram builds topic profiles with an LLM and balances exposure across topics. A meme beat and a build update in one reel splits the classification; keep the truck, the part or the counter unmistakable in frame one and in the caption's first line.
9. Read the retention chart, not the view count, after 24 hours. Vertical drop at zero is the first frame; a cliff after the hook is the hook; a slow slide is a reel that stopped promising anything. Fix whichever shape repeats across the week.
10. Ignore the numbers nobody official has said: 3 to 5x send weighting, a two-a-day frequency cap, a 10-repost rule, a 70 percent similarity score. The official list is short and has not changed in 22 months; the account's job is to be measurably better on it, not to chase rumours.
