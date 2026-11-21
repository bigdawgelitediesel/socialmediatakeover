# Live Instagram algorithm check, 2026-11-21

Research agent sweep run 2026-11-21 for @elcoyotediesel (577 followers, Creator account). Scope: what Instagram, Mosseri and the trade press said in October and November 2026, what the newest datasets say moves distribution for a sub-1k account, the comment-keyword DM engine as it stands this month, Trial Reels / Blend / Threads, what the growth educators shipped in November, and the last 30 days of YouTube on the topic (five transcripts pulled through Supadata).

Read the 2026-11-20 file first (`2026-11-20-instagram-ranking-and-capcut-recipe.md`). This file only adds what is new or firmer. Every finding carries a date and a URL. Where the only source is a vendor blog, it says so.

Access caveats: Instagram's Help Center and Mosseri's Threads profile render only partially through the fetch tool, Rachel Karten's and Jade Beason's deeper posts are paywalled, and Instagram still publishes no numeric ranking weights. Everything with a percentage attached below is third-party data unless it is quoted from Mosseri.

---

## 0. What changed since 2026-11-20

New since the prior file, in order of importance for this account:

1. **Mosseri's Colin and Samir interview (recorded Oct 23, published Oct 26, 2026) is the most useful primary source of the quarter and was not in the prior file.** Verbatim: "Sends per reach is what is particularly important for that unconnected reach." "If you're a new creator, that's probably one of the most important metrics you could follow." Metrics to track, in his order: sends per reach, likes per reach, average watch time. "We focus way less on watch time than all the competition does, but we do care about watch time." On ranking goals beyond engagement: "Originality is a really key one... We try to give original content creators more distribution than aggregators. Breakouts is another key one. We try to give every piece of content a chance. So a brand new account can get millions of views, which wasn't possible two years ago. Recency is another one." On follower counts: "We want to make sure that having a follower count on Instagram means something even in a recommendations first world." On sends-per-reach as a metric: "We now do in Edits, we now do the math for you so you can see it, and we're bringing some of that goodness to the insights in Instagram now." (YouTube, 167k views, https://www.youtube.com/watch?v=sxizdQ2hRfk)
2. **Trial Reels may already be open to this account.** Multiple late-2026 guides (flowgent Oct 29, 2026; vidova; metrik; planoly) cite Instagram Help Center article 1013292530224018 as: public account, 200 followers for professional (business or creator) accounts, 1,000 for personal, and eligible for recommendations. The Help Center page would not load for me, and Brock Johnson still said "1,000 followers and a professional account" on Nov 19, so this is unconfirmed. The prior file and CLAUDE.md say "locked until 1,000." Check the Reels composer for the Trial toggle today. (https://flowgent.ai/blog/instagram-trial-reels, https://vidova.ai/blog/instagram-trial-reels-explained)
3. **Content protection launched on Instagram Nov 17, 2026**: originality is now enforced with a creator-facing tool, not just a ranking rule. (https://creators.instagram.com/blog/introducing-content-protection/)
4. **Amazon affiliate links inside Reels and feed posts, Nov 16, 2026**, US creators, up to 30 products per Reel, Instagram takes 0 percent. Directly relevant to a parts guy. (https://creators.instagram.com/blog/more-ways-to-earn-affiliate-links)
5. **Meta published how "Your Algorithm" topic profiles work, Nov 11, 2026.** An LLM turns interest signals into inferred topics, creator-level "see less" filters that creator out directly, and exposure is balanced across topics. Practical read: each post should classify cleanly into one topic. (https://www.socialmediatoday.com/news/meta-publishes-explainer-on-your-algorithm-controls/874460/)
6. **Two new datasets:** Buffer's 2.7M-reel length study (Nov 12, 2026) and Socialinsider's refreshed Reels benchmarks (updated Nov 17, 2026) with a skip-rate and reach-rate breakdown for 1k to 5k accounts. Dash Social's Issue 2 2026 benchmark (Nov 17) adds share counts by format. Details in section 2.
7. **Edits is now on Mac (Nov 5), has speed curves and auto audio balancing (Nov 12), Edits Cloud 10 GB free and Edits Plus 200 GB (Nov 19), and publishes directly as a Trial Reel from desktop.** Windows is not supported, so CapCut stays the tool here; Mosseri's Oct 30 "we don't demote content for being created with other apps" still stands.
8. **The ManyChat free tier is now 25 active contacts a month** (active-contact billing since March 2, 2026), and Meta Business Suite has a free native Comment to Message automation with a 15-minute delay and 5 exact-match keywords. Section 3.
9. **Linked Reels series were removed Oct 28, 2026**; the separate "Series" format is in international test with a US test expected by early 2027 (Geekout, Oct 30).
10. **Threads added "Gems" in November**, an originality-based recognition for text posts; nothing changed for Reels on Threads. Blend is unchanged since its April 2025 launch.

Not changed: the three-signal framework (watch time, likes per reach, sends per reach), the 3:00 ceiling for non-follower recommendation, the 5-hashtag cap, the April 30, 2026 originality rule, the "logo from another app reduces distribution" rule.

---

## 1. Official: Mosseri, @creators, Instagram blog, Meta newsroom (Oct and Nov 2026)

### Ranking statements

- **Oct 16, 2026, Stories AMA.** AI content is not throttled for being AI. Experimenting with Trial Reels "is not going to affect your account in a negative way." Reposting the same Trial Reel: "We're going to crack down on that." Hiding like counts, liking your own posts: no effect. (ZoomSphere, byline Oct 30, 2026, https://www.zoomsphere.com/blog/instagram-algorithm-2026-what-actually-gets-reach)
- **Oct 23, 2026, Stories AMA.** "We actually focus a lot more on finding reels and photos that you might send to a friend." Comments are "not the most important part of value by a long shot." "More and more of the reach on Instagram came from recommendations." "There are definitely accounts on Instagram that grow without posting any reels by just posting photos." Scheduling does not hurt reach. (same ZoomSphere source)
- **Oct 23, 2026, Colin and Samir interview (published Oct 26).** Quotes in section 0. Additional points from the transcript: repeat non-follower viewers matter "indirectly," because "we use your interaction history to predict the likelihood of what you're going to do in the future." AI content is not ranked differently, but AI accounts that reuse a human creator's script "could treat it as unoriginal content." Instagram is working on richer insights ("when you smile more, people like the thing more") and letting people "talk to your algorithm." On the long-form bet: "I don't want to become YouTube because then I think we lose the friends." (https://www.youtube.com/watch?v=sxizdQ2hRfk)
- **Oct 30, 2026, Stories AMA.** "We don't demote content for being created with other apps other than ours." A visible third-party logo does get less distribution. Removing a post does not affect the reach of other posts. (ZoomSphere)
- **Oct 2026 video interview (per Geekout, Oct 30).** Mosseri said reach is currently driven by sends, carousels and watch time, and on creator payments: "We spend more money than we make back by a long shot." (https://geekout.mattnavarra.com/p/instagram-90-minute-videos-zuckerberg-shareholder-lawsuit)
- **Week of Nov 13, 2026 (per Geekout).** Mosseri: "Following counts still matter on Instagram more than they do on platforms like TikTok." (https://geekout.mattnavarra.com/p/eu-addiction-rules-tiktok-shop-subscription-meta-muse-uk-launch-report)
- **Nov 3, 2026, Tessa Lyons (VP Product) with Rachel Karten.** Original clips linking to a Feature can run as Trial Reels; viewers who like a clip may later see the Feature in Explore. Lyons favors shorter vertical Reels and longer horizontal Features, "a direction, not a rule." Karten asked about the algorithmic benefit of a series ("it's like a goldmine"); the answer is paywalled. (https://www.linkinbio.news/p/my-call-with-instagrams-vp-of-product; Geekout Nov 6, https://geekout.mattnavarra.com/p/tiktok-shop-app-meta-robot-snap-settlement-ofcom)
- **Nov 11, 2026, Meta explainer on Your Algorithm.** Topic profiles are built by an LLM from refreshed interest signals; newly added interests get temporary extra weight then fall back to engagement weighting; exposure is spread so no topic dominates; "see less of this creator" filters the creator out directly; quality requests like "less AI" map to dedicated demotion signals. (https://www.socialmediatoday.com/news/meta-publishes-explainer-on-your-algorithm-controls/874460/)

### Features, long-form, Series

- **Oct 26, 2026.** "Features": horizontal video up to 90 minutes, test in Brazil and select US creators; "Clips as Reels" links up to eight Reels to one Feature with a "Watch full video" button; Features recommended in Explore. (TechCrunch, https://techcrunch.com/2026/10/26/watch-out-youtube-instagram-goes-from-short-form-to-90-minute-videos/)
- **Nov 1 and Nov 4, 2026.** One-off payments reportedly up to $500,000 to select long-form creators; Mosseri called them an unsustainable way to bootstrap Features; no ad revenue share; "you primarily get paid by brands." Long-form videos are being placed at the top of Explore for some users. (Social Media Today, https://www.socialmediatoday.com/news/instagram-offers-to-pay-creators-for-long-form-content/873402/ and https://www.socialmediatoday.com/news/instagram-tries-to-entice-long-form-creators/873820/; Later, Oct 27, https://later.com/blog/from-reels-to-the-living-room-what-instagrams-long-form-push-means-for-brands/)
- **Oct 28, 2026.** Linking Reels into a series ended; the separate Series format (grouped episodic Reels) is in international test, US test expected by early 2027. (ethicalsmm citing Metricool, https://ethicalsmm.com/blog/instagram-updates-november-2026; Geekout Oct 30)
- **Week of Nov 13.** A separate long-form upload flow is being tested, with snippet clips published as Reels. (Geekout Nov 13)
- **Regular Reels still cap at 20 minutes and Reels over 3 minutes get an in-composer warning that they are not eligible for unconnected reach.** (Brock Johnson, Nov 19, 2026, https://www.youtube.com/watch?v=6i6T33SAIRc)

### Originality and content protection

- **Nov 17, 2026, @creators blog.** Content protection: eligible creators (selected on originality and integrity standards) get a notification; once enrolled every new original video is protected and older ones can be added; matches show the copy's view count and the poster's follower count; actions are Track, Hide from everyone (reduces the copy's reach on Instagram and Facebook), Add credit link ("original by" label on Instagram), or Release; allow list for second accounts and brand partners; disputes via the tool or the IP Reporting Center. Coming: matching on spoken words when visuals were swapped for AI. Meta is "exploring ways to limit the reach of profiles that repeatedly post AI-generated content, similar to its existing limits on unoriginal content." (https://creators.instagram.com/blog/introducing-content-protection/; TechCrunch, https://techcrunch.com/2026/11/17/instagrams-new-tool-for-creators-targets-unauthorized-reposts-and-ai-modified-videos/)
- **Mosseri on Threads (about Nov 18).** Rolling out content protection in Insights; "We need a way to help those creatives without letting bad actors make more fake claims." (Medianama, https://www.medianama.com/2026/11/223-instagram-copyright-tool-deepfakes-stolen-content/)
- **AI labels (Hootsuite, Nov 4, 2026).** Realistic AI video or audio, including AI voiceovers in Reels, needs the "AI info" label; AI-written captions or scripts do not; unlabeled AI-generated profiles lose recommendations. (https://blog.hootsuite.com/ai-disclosure-policy-for-instagram/)

### Monetization and links

- **Nov 16, 2026, @creators blog.** Amazon affiliate links in Reels and feed posts for eligible US creators through a connected Amazon Influencer account; LTK and ShopMy collection links (US and Canada); any affiliate link can be pasted into "Add products"; product linking live in 26 countries; Instagram takes no cut; internal data (Sept 2026) says product links get about 2x the clicks of bio links. Jade Beason and Social Media Today report 30 products per Reel and 20 per feed post. (https://creators.instagram.com/blog/more-ways-to-earn-affiliate-links; https://www.socialmediatoday.com/news/instagram-adds-amazon-affiliate-links/874817/)

### Edits (Oct and Nov 2026)

- **Oct 7:** carousel editor. **Oct 15:** captions post ("Make your Reels easier to watch, and harder to scroll past"). **October:** beat-synced effects, bulk caption editor with transcript view and 7 new caption styles, Auto adjust, clip volume to 150 percent, 10 GB cloud, Audio Links, Kits, Popular Topics (10k+ accounts). (edits.instagram.com/blog; embedsocial, https://embedsocial.com/blog/new-instagram-features-2026/)
- **Nov 5:** Edits for Mac (Apple Silicon only): multi-track timeline, keyframes, waveforms, LUT color grading, voiceover, custom shortcuts, font import, 4K export with no watermark, direct publish to Instagram including as a Trial Reel. No Windows. (TechCrunch, https://techcrunch.com/2026/11/05/instagram-brings-edits-to-desktop-to-take-on-capcut/; 9to5Mac, https://9to5mac.com/2026/11/05/instagram-launches-edits-for-mac-with-multi-track-video-editing-and-4k-exports/)
- **Nov 9:** Effect Builder (prompt-to-Stories-effect, US 18+). **Nov 12:** speed curves (Montage, Hero, Bullet, Jump presets), Auto adjust audio, text animation timing, Inspiration topic preferences. **Nov 19:** Edits Cloud and Edits Plus (200 GB). (Social Media Today, https://www.socialmediatoday.com/news/metas-edits-app-gets-speed-curves-and-auto-audio-balancing/874586/; https://edits.instagram.com/blog/edits-cloud-edits-plus/)
- Instagram now shows a prompt pushing Edits when you tap create Reel (October). Edits does the sends-per-reach math in its insights (Mosseri, Oct 23).

### Other Nov 2026 product news

- **Nov 2:** Meta's AI creator assistant now flags niche trends, builds shot lists and generates comment replies "in the creator's voice"; it is in the Creator Dashboard. (https://www.socialmediatoday.com/news/meta-updates-creator-assistant-chatbot/873524/)
- **Nov 9:** AI age estimation rolled out globally. (TechCrunch)
- **Nov 16:** Meta tightened default recommendation protections in India after a government review (not US). (https://about.fb.com/news/2026/11/an-update-on-the-content-we-recommend-on-instagram-in-india/)
- **Nov 17:** Direct, a standalone Instagram DM app, testing in Türkiye and Thailand; consumer only, no business features reported. (https://techcrunch.com/2026/11/17/meta-launches-direct-a-standalone-messaging-app-for-instagram/)
- **Nov 18:** Stories editable for 15 minutes after posting (text, music, stickers, drawings; views kept; "Edited" label). Creator Dashboard on the web with a Reels composer, bulk upload, insights, content protection and "invite viewers to follow." (https://www.socialmediatoday.com/news/instagram-adds-stories-editing/875261/; https://www.socialmediatoday.com/news/meta-brings-its-updated-creator-dashboard-to-the-web/875143/)
- **Tests spotted in Nov (Geekout Nov 20):** new Reels icon in the nav bar, carousels up to 30 slides, multiple songs on a profile, "Open to Reels" home layout (Oct 9 PetaPixel), redesigned Insights (Home, Performance, Content, Audience; content sortable by follows; Trial reels shortcut) and professional dashboard (Summary / Tools). (https://geekout.mattnavarra.com/p/instagram-direct-meta-takes-muse-charm-price-gta-vi; https://petapixel.com/2026/10/09/meta-tests-opening-instagram-and-facebook-directly-to-tiktok-style-vertical-video-feeds/)

---

## 2. What moves distribution for a sub-1k account (best current evidence)

### Datasets published in the last 60 days

**Socialinsider, Reels benchmarks, updated Nov 17, 2026** (9.77M organic brand Reels, 1k to 1M followers, Jan to Jun 2026; the 1k to 5k bucket is 974k posts from 58k profiles). https://www.socialinsider.io/blog/instagram-reels-statistics/
- Reels reach rate by account size: 1 to 5k **9.78 percent** (carousels 8.80, images 7.00), 5 to 10k 7.55, 10 to 50k 7.10, 50 to 100k 5.60, 100k to 1M 5.00. Small accounts get the highest reach rate.
- Reach by length: under 30s 5.20 percent, **30 to 60s 5.60 (highest)**, 60 to 90s 5.30, 90 to 120s 4.30, over 120s 3.50.
- Skip rate (swiped away in the first 3 seconds): **1 to 5k accounts 65.5 percent**, down to 60.5 percent at 100k+. Our account average of 48.2 percent (CLAUDE.md) already beats the brand benchmark; the best posts at 32 percent are elite.
- Reposts (reshares) per post at 1 to 5k: 2 per Reel, 1 per carousel, 1 per image. Zero shares on a build reel is below even the brand floor.
- Average Reels posted per month at 1 to 5k: 8.

**Buffer, "How Long Should Instagram Reels Be?", Nov 12, 2026** (2.73M Reels for reach, Jan 1 to Aug 15, 2026, each account compared to its own baseline). https://buffer.com/resources/instagram-reels-length/
- 90 to 179s: **+7.4 percent reach** vs baseline (median account closer to +4). 30 to 59s +2.7. 60 to 89s +1.6. 15 to 29s -0.9. Under 15s -1.5. **180s or longer -49.3 percent reach and -45.9 percent views.**
- Engagement rate was highest for 180s+ (the followers who do watch are loyal), which is the trap: long Reels only reach followers.
- Buffer's own advice: test with Trial Reels, two versions with one variable changed, compare after about 24 hours. Effects are modest and correlational.
- Note the conflict with Socialinsider (30 to 60s best). Buffer's sample is Buffer customers (brands and creators with watch time to back longer cuts); Socialinsider's is brands only. For a 577-follower account with a 6.8s average watch time (CLAUDE.md), the Socialinsider read applies until watch time earns the longer cut.

**Dash Social, Issue 2 2026 benchmark, Nov 17, 2026** (3,313 Instagram accounts with 1k+ followers, Jan to Jun 2026, includes boosted posts). https://lifestyle.middletownlifemagazine.com/story/840116/instagram-carousels-average-24-more-views-than-reels-dash-social-benchmark-report-finds/
- Carousels averaged 24 percent more views per post than Reels (156k vs 126k). Reels still lead on shares: **711 shares per post vs an Instagram average of 562**, and lead on saves and interactions. The report's own conclusion: shares are what buy extra distribution.

**Buffer algorithm guide refresh, Oct 23, 2026** (https://buffer.com/resources/instagram-algorithms/): Reels got 36 percent more reach than carousels and carousels 12 percent more engagement (4M+ posts); accounts that replied to comments earned 21 percent more engagement (correlation); consistent posters earned nearly 5x engagement per post (100k+ users).

**Metricool 2026 study** (secondhand via several aggregators): average Reel watch time rose to 8.5 seconds; Reels reach down about 35 percent year over year. (https://metricool.com/press-release-instagram-study-2026/)

### Creator-run and consultant-run numbers (not peer-reviewed, dated, useful as targets)

**heyDominik, "How to Force the Instagram Algorithm to Push Your Reels (based on data)", Oct 26, 2026, 14k views, transcript pulled.** Claims to draw on hundreds of client accounts. https://www.youtube.com/watch?v=6u4MGM_KZ5I
- Median skip rate of a breakout reel (2x usual views or better): **45 percent or lower**. Top 10 percent of reels: **31 percent or lower**. "Skip rate alone has absolutely almost no correlation with how well your video is going to do."
- The pair that matters: skip rate under 45 percent **and** average watch over 5 to 10 seconds. "Just having those two metrics checked off, basically most people doubled their views at least." Low skip with no hold = nothing happens.
- Average-watch benchmarks to break out: a 10s reel needs near 100 percent; **a 30s reel needs about 8 to 11s**; a 60 to 90s reel about 18s; 90s+ about 28s. 90s+ reels broke out twice as often in his data, "contrary to what Instagram says."
- Share rate (shares divided by views): 0.5 to 1 percent is average and moves nothing; 1 to 2 percent slight lift; **2 to 3 percent is where "stuff really starts to hit the fan"**; 3 percent+ "haywire"; 5 percent overrides everything, "you can have a horrible skip rate." He notes these are for value content, not memes.
- Topic clarity: off-topic objects or words in frame dilute classification and send the reel to the wrong audience. Keep the words and the visuals unmistakably in-niche.
- "Trust tier": accounts that get "too similar" pop-ups on Trial Reels or whose Trial Reels sit at 150 to 200 views are in a low-trust tier; weeks of clean posting slowly lift it. Unverified, but it matches the 200-view plateau many small accounts report.

**Brock Johnson, "I Made 3,238 Reels To Learn This About Instagram", Oct 22, 2026, 83k views, transcript pulled.** https://www.youtube.com/watch?v=60eaURKkdBk
- "Retention is king." Completing a 30s reel beats completing a 10s reel. Target **50 percent or higher retention at the end** for reels that break out.
- Reads the retention graph (Reel > View insights > Overview > "How long people watched your reel"): a vertical drop at 0s means followers have pre-judged you or the first frame is off-putting (rare on Trial Reels because non-followers have no prior); a cliff right after the hook means the hook failed; a steady slide means the video stopped promising anything (fix with open loops and a second hook where it dips).
- First-frame checklist: visual relates to the topic, plain and obvious, no more than three focal points, HD, bright but not blown out, one unexpected element. Hook 5 to 8 words, fifth-grade reading level, include a negative word (don't, stop, avoid), visual over text.

**Creator Lane, "Mosseri Says vs What Creators Measure" (Jun 28, updated Aug 30, 2026).** Sends per reach 1 to 2 percent "strong," 3 percent+ "viral-tier"; reels with over 60 percent 3-second hold "out-reach those under 40 percent by 5 to 10x" (unsourced); 55 percent of Reel views from non-followers under 50k. https://creatorlanehq.com/blog/instagram-algorithm-2026-mosseri-vs-measured

**Lilach Bullock, daily vs 3x a week** (undated, "a few years ago"): watch-through 31 percent daily vs 44 percent at 3 a week; followers 118 vs 146; reach 41.2k vs 38.9k. Posting more cost quality. https://www.lilachbullock.com/how-many-instagram-reels-should-you-post/

**Robert Benjamin, Nov 4, 2026, 5k views, transcript pulled.** Claims "as of late October 2026, nearly 45 percent of all recommended content on Instagram Reels are under a day old" and recommends 1 to 2 feed Reels plus 5 Trial Reels a day. No source given; treat the number as unverified. Recency is a real signal (Mosseri, Oct 23) but the volume advice is a one-man-shop killer. https://www.youtube.com/watch?v=j3WILAPvgzo

### Signals this account can read in the API or app

Per CLAUDE.md, `reels_skip_rate` is per post, share rate is in Insights since April 2026, follows cannot be attributed to a reel, and the retention graph is in-app only. Nothing in November changed that. The Insights redesign (Home / Performance / Content / Audience) lets content be sorted by follows at the account level, which is the closest thing to per-reel follow attribution.

---

## 3. The "comment WORD and I'll DM you" engine, November 2026

### How it works and the rules (Meta's own)

- Private replies to comments go through the Instagram Messaging API: **one automated message per commenter, within 7 days of the comment**; the conversation may continue only if the person replies, and then within the 24-hour window. Requires a professional account linked to a Page, `instagram_manage_comments` and `pages_messaging`, Advanced Access. (Meta developer docs, https://developers.facebook.com/docs/messenger-platform/instagram/features/private-replies)
- Rate limits reported by secondary sources: 750 private replies per hour per account; Send API 100 to 300 calls per second. The "200 DMs per hour" number is a pacing convention vendors adopted, though Buffer (Jun 30, 2026) states it as a Meta cap. The "one automated DM per user per 24 hours from comment or story triggers" rule is reported as new in 2026 by Creator Lane and Buffer. (https://superprofile.bio/guides/instagram-dm-limits; https://buffer.com/resources/instagram-dm-automation/; https://creatorlanehq.com/blog/instagram-comment-automation-playbook-2026)
- No per-day DM cap for professional accounts was found anywhere.

### Native option (free)

Meta Business Suite > Inbox > Automations > **Comment to Message**: desktop only, up to 5 keywords or phrases per automation, exact and case-sensitive match, **sends after a 15-minute delay unless you reply personally first**, no setting to shorten it, template automations take priority over keyword ones, turning on Meta Business Agent pauses the other automations. In-app: FAQs (4), Saved Replies, Instant Reply, Away Message, AI Auto Replies (rolling out). No flow builder, no follow-to-unlock, no analytics. (Creatorflow, updated Nov 19, 2026, https://creatorflow.so/blog/instagram-built-in-automation/; Buffer, Jun 30, 2026)

The Nov 2 creator assistant drafts comment replies in your voice but does not run keyword-to-DM flows. The Nov 17 Direct app has no business features.

### ManyChat cost (Blotato, updated Nov 9, 2026)

Active-contact billing since March 2, 2026. Free: $0, **25 active contacts a month**, 4 live automations, "Powered by Manychat" line, Instagram comment-to-DM works. Essential $17 a month ($14 annual), 250 contacts, overage $0.10 each. Pro $39 ($29), 2,500 contacts, unlocks AI and broadcasts. Business $99 ($69), 7,500. Advanced $199 ($139), 25,000. A contact counts once per billing month when an automation messages them. (https://www.blotato.com/blog/manychat-pricing) At 200 to 500 views per build reel, 25 contacts a month covers roughly one keyword post per week.

### Does Instagram reward or punish it?

- No primary source says comment-keyword automation lifts reach. Mosseri, Oct 23, 2026: comments are "not the most important part of value by a long shot" and Instagram focuses "a lot more" on content you would send to a friend. On the "DM me a keyword" tactic he was reported as calling it "a little bit of an engagement hack" (secondhand, podcast write-up, https://finance.biggo.com/news/397441c73e4684c3). On hacks generally: "hack-type tactics sometimes work, usually don't, and when we find them, we usually shut them down" (Social Media Today, https://www.socialmediatoday.com/news/instagram-chief-debunks-popular-engagement-hack/816781/).
- Meta's recommendation guidelines list engagement bait ("posts that explicitly request engagement," example "Comment YES and see what happens") and the Spam policy bars "requiring users to engage" to access exclusive content. Comment-keyword DM automations are not named; the risk rises when a follow or public engagement is required to get the item. (FYProof, updated Oct 22, 2026, https://fyproof.com/guides/engagement-bait-penalties)
- Creator Lane claims Meta's classifier downranks reels with many comments but low sends per reach and low save rate, and that late-2025 enforcement included suspensions, not just reduced reach. Unverified, but consistent with the ratio logic in CLAUDE.md. Their "skip it" list includes accounts under 2,000 followers selling high-ticket offers. (https://creatorlanehq.com/blog/instagram-comment-automation-playbook-2026)
- The "comment velocity" idea (early comments in the first hour buy distribution) appears only in vendor and SEO blogs; the one vendor "data" piece (InstantDM, Jun 17, 2026) is a single unnamed case study with no control. No official metric exists. (https://instantdm.com/blog/why-the-instagram-algorithm-loves-automated-replies-in-2026)
- The honest positive case: Buffer's writer (about 3,000 followers) credits DM automation with roughly half her followers, through two real lead magnets (a Notion database and a CV template). Brock Johnson (Nov 2, 2026, ManyChat affiliate) argues "click the link in bio" CTAs hurt reach and keyword comments do not, and on Nov 19 said Amazon links in Reels do not replace ManyChat for him because the DM gives you the data on who clicked.

### Risks, in order

1. Any tool that asks for your Instagram password instead of the Meta OAuth pop-up (ban risk). 2. Requiring a follow to get the item (Spam policy). 3. Engagement-bait reels with no payoff. 4. Question comments (support requests) answered with a marketing DM. 5. Non-partner tools "working on borrowed time." 6. Comment-heavy, share-light posts polluting the ratios that this account depends on.

**Verdict for this account:** use it only when the DM delivers something a diesel owner actually wants (the Rival parts list, the FASS install checklist, a "don't buy this" price sheet), on at most one post in four, through the free ManyChat tier or the native tool, never with a follow gate. Reply to every comment manually anyway.

---

## 4. Trial Reels, Blend, Threads, non-follower seeding

### Trial Reels

- **Eligibility:** see section 0, item 2. Check today. If the toggle is live at 577 followers, this is the single biggest change for the account.
- **Caps:** Instagram limits how many Trial Reels an account can post in a 30-day window (SocialBee, dated April 2026, no number). Brock Johnson (Nov 19) mentions a max of 20 Trial Reels per day as the spam ceiling. Mosseri: several different Trial Reels in one day is fine (Oct 30); reposting the same one repeatedly will be cracked down on (Oct 16); experimenting does not hurt the account (Oct 16). (https://socialbee.com/blog/instagram-updates/)
- **Reading them:** insights land within 24 hours; the auto-share decision uses the first 72 hours; Trial Reels are ranked separately from feed Reels; a Trial Reel stuck at 0 is usually too new, a near-duplicate, over 3 minutes, watermarked, or on an account that is not recommendation-eligible (check Account Status). (https://vidova.ai/blog/instagram-trial-reels-explained)
- **Vertical drop retention graphs are rarer on Trial Reels** because non-followers have no prior on you (Brock Johnson, Oct 22). That makes a Trial Reel the cleanest hook test available.
- Buffer (Nov 12): A/B two versions with one variable changed, judge at about 24 hours.
- Edits on Mac publishes directly as a Trial Reel; the Insights redesign puts a Trial reels shortcut on the Home tab; Tessa Lyons says Feature clips can run as Trial Reels.

### Blend

Launched April 2025 (invite-only shared Reels feed inside a DM thread). Still described as a staged rollout in May 2026; creators cannot see how often they surface in Blends and have no placement control; the only lever is making Reels people send. No October or November 2026 change found. (https://instantdm.com/blog/instagram-blend-for-creators-2026)

### Threads

- **Gems (Nov 2026):** daily automated recognition for public posts and replies chosen for originality and discussion, US 18+ only, reposts and crossposts ineligible. (Gain, Nov 5, https://blog.gainapp.com/social-media-updates/)
- Save button next to Share, "Your Algo" side-menu shortcut test, a swipeable carousel of comments under some posts, Threads posts usable as carousel slides in Edits, posts shareable to Instagram Stories from web, a "Threads sticker" for Stories in test. (Geekout Nov 6, 13, 20)
- No change to how Reels appear on Threads. Threads video spec remains up to 5 minutes, 9:16 recommended.

### How non-follower reach is seeded right now

- Mosseri (Oct 23): the system ranks for originality, breakouts ("we try to give every piece of content a chance... a brand new account can get millions of views") and recency, on top of engagement predictions. Sends per reach is the key unconnected signal; repeat viewers feed predictions through interaction history.
- The Your Algorithm explainer (Nov 11) says topic profiles are LLM-inferred and exposure is balanced across topics, so a reel that reads as two topics competes in both and wins neither.
- The April 30, 2026 originality rule and the Nov 17 content protection tool mean reposted or aggregated footage is both demoted and now blockable by the original poster.
- "Open to Reels" and the new Reels icon tests push more sessions straight into the recommended surface.
- Blog "audition pool" sizes (200 to 1,000 viewers) remain estimates; no official number. The 200-view plateau is consistent with heyDominik's trust-tier read and with Mosseri's "if we take away reach, we'll tell you" in Account Status.

---

## 5. What the educators published in November 2026

**Brock Johnson, Build Your Tribe** (podcast and YouTube): Oct 22 #927 "I Made 3,238 Reels" (83k views, retention is king, 50 percent end-retention target); Oct 26 #928 "Not Getting Views On Reels? Do This NOW" (69k; posting-day routine: delete old Stories, 10 minutes of commenting in-niche, check location/music/captions/also-share settings, pinned comment, reply to everything, share to Story with text); Nov 2 #929 "What Is Manychat?" (42k); Nov 5 #930 "14 Viral Instagram Reels" (43k); Nov 9 #931 masterclass (36k, 3h55, "NAP method"); Nov 16 #932 "Claude Is Killing Your Instagram" (10.5k; outsourcing your own work to AI flattens the account); Nov 19 #933 "NEW Instagram Algorithm" (12k; Features explainer, Reels still cap at 20 minutes, over 3:00 not eligible for unconnected reach, cites Buffer's 90s to 3min lift, says 1,000 followers plus professional account for new features, Amazon links in Reels, "Q4 holiday shopping brings in 30 to 40 percent of affiliates' annual income"). (https://www.listennotes.com/podcasts/build-your-tribe-grow-your-business-with-x1YgDoJwb8d/)

**Vanessa Lau:** Nov 6 "The EXACT System I Used to Rebrand My Instagram in 7 Days (FULL MASTERCLASS)" (23k views, 1h00, Poppy AI sponsored); Nov 5 "What I've Learned From Hate Comments." No ranking claims extracted. (https://www.youtube.com/watch?v=dJxlFgG7CrA)

**Jade Beason, The Creator Project:** Nov 20 Issue 68 (Amazon links: 30 per Reel, 20 per feed post, connect in Professional dashboard > Monetisation, tag gift guides now; Stories 15-minute edit, rewatch every Story right after posting; content protection: watch the activity feed for enrollment, protect old Reels, add second accounts to the allow list); Nov 10 "Making the algorithm work FOR you" (paywalled; notes Mosseri's Sept 2026 argument that without ranking high-volume publishers would crowd out creators); Nov 6 Issue 66 (Instagram paying YouTubers); Nov 13 Issue 67 (AI age checks). (https://jadebeason.substack.com/p/instagram-x-amazon-is-here-youtube)

**Matt Navarra, Geekout:** Oct 30 "Instagram Declares War on YouTube" (Features, no rev share, $50k to $500k offers, Series US test early 2027, bio links limited with more for Meta One subscribers); Nov 6 (Edits desktop, Features in Explore, professional dashboard redesign, Tessa Lyons on Trial Reel clips); Nov 13 (Edits speed curves, "Following counts still matter," long-form upload flow with Reels snippets, DM "Invite" option); Nov 20 "Instagram Went Back to 2017" (Direct, Stories edit, content protection, Amazon and LTK links, 30-slide carousels test, new Reels icon, multiple profile songs, Threads save button). Archive: https://geekout.mattnavarra.com/archives

**Rachel Karten, Link in Bio:** Nov 3 "My call with Instagram's VP of Product" (Tessa Lyons; series as "goldmine"; what longer content already works; "context as a video hook"; paywalled); Nov 12 "Context is king" (context loops, paywalled); Nov 17 Tory Burch's secret TikTok. (https://www.linkinbio.news/p/my-call-with-instagrams-vp-of-product)

**Lindsey Gamble:** Nov 3 "Can Instagram Make Long-Form Video Work This Time?" (Features, Clips as Reels with a Watch full video button, brand deals as the early monetization route). (https://lindseygamble.beehiiv.com/p/can-instagram-make-long-form-video-work-this-time)

**Social Media Today (Andrew Hutchinson), Instagram items Nov 1 to 19:** long-form payouts (Nov 1, 4), creator assistant replies (Nov 2), Edits for macOS and Graph API changes (Nov 5), Effect Builder and age detection (Nov 9), Your Algorithm explainer (Nov 11), Edits speed curves and sports test (Nov 12), Amazon links and iPhone Duo app (Nov 16), content protection and Direct (Nov 17), web Creator Dashboard (Nov 18), Stories editing (Nov 19). (https://www.socialmediatoday.com/topic/instagram/)

**Later:** Oct 27 "From Reels to the living room" (Features for brands; Mosseri: "you primarily get paid by brands"); weekly Reels trends page. No November algorithm post.

**Buffer:** Oct 23 algorithm guide refresh; Nov 3 "13 Trending Sounds on Instagram in November 2026" (truck-friendly picks: "Upside Down" for before/after flips, "Windows in Brazil (Sped Up)" for 0 to 100 percent build progress, the sviola_handmade ON/OFF toggle reveal, "Pump It" for labeled shop-day vlogs, "Luminary" for finished-build reveals); Nov 4 scheduling Stories; Nov 12 Reels length study. (https://buffer.com/resources/trending-audio-instagram/)

**Hootsuite:** Nov 2 image sizes guide; Nov 4 AI disclosure policy; the algorithm guide is still dated July 15, 2026. (https://blog.hootsuite.com/ai-disclosure-policy-for-instagram/)

---

## 6. YouTube, last 30 days (uploaded Oct 22 to Nov 21, 2026), ranked by views

Searched through the YouTube Data API for "Instagram algorithm update November 2026," "Instagram reels not getting views 2026," "Instagram reels update new features November 2026" and channel uploads. View counts as of Nov 21.

| # | Views | Date | Video | Gist |
|---|---|---|---|---|
| 1 | 167,298 | Oct 26 | Colin and Samir, "Why Instagram Completely Changed Its Mind" (1h12), https://www.youtube.com/watch?v=sxizdQ2hRfk | Mosseri on Features, ranking for originality, breakouts and recency, sends per reach as the new-creator metric, watch time weighed less than rivals |
| 2 | 99,054 | Oct 29 | WsCube Tech, "The Instagram Game Has Changed! How to Win in 2027" (18m) | Hindi-language general strategy recap; nothing primary |
| 3 | 87,181 | Oct 27 | Technical Yogi, "Instagram BIG GOOD NEWS 2026: 90 Minute Videos, Monetization Update" (4m) | Hindi recap of the Features announcement |
| 4 | 82,814 | Oct 22 | Build Your Tribe, "I Made 3,238 Reels To Learn This About Instagram" (24m), https://www.youtube.com/watch?v=60eaURKkdBk | Retention is king, five retention-graph shapes, 50 percent end-retention target, first-frame checklist |
| 5 | 68,646 | Oct 26 | Build Your Tribe, "Not Getting Views On Reels? Do This NOW" (31m), https://www.youtube.com/watch?v=BsVFpdNCZhA | Study five accounts' top reels, then a posting-day routine (prime Stories, comment in-niche 10 min, settings check, pinned comment, reply to all) |
| 6 | 43,050 | Nov 5 | Build Your Tribe, "14 Viral Instagram Reels That You Need To Post ASAP" (26m) | Fourteen adaptable formats incl. talking-head, visual tricks, de-influencing |
| 7 | 42,350 | Nov 2 | Build Your Tribe, "What Is Manychat? How DM Automation Boosts Instagram 10X" (26m), https://www.youtube.com/watch?v=lnmfi-Td6dw | Link-in-bio CTAs hurt, comment-to-DM gives data; live ManyChat build |
| 8 | 35,847 | Nov 9 | Build Your Tribe, "THE Instagram Masterclass: How To Grow in 2027" (3h55) | Full-course format, "NAP method" |

Next in line: Vanessa Lau rebrand masterclass, Nov 6, 23,012; heyDominik data video, Oct 26, 13,994; Andrea Estratega (Spanish) "Todo lo que dijo el CEO de Instagram para 2027," Nov 2, 13,708; Build Your Tribe #933, Nov 19, 12,390; Robert Benjamin "NEW Algorithm Updates Explained for November 2026," Nov 4, 5,064. The "stuck at 200 views" genre (Outfame, Zero to Influence, Mitalee, SocioMee) is all under 1,000 views each and recycles the audition-pool theory.

**Transcripts pulled (Supadata) and concrete claims extracted:**

1. **Colin and Samir / Mosseri (Oct 26).** Quotes in sections 0 and 1. Additional: "We look at things like how likely you are to watch most of the video, how much of the video we think you're going to watch... but we also care about sends and comments and likes and story shares." Reels only became accretive once they "became more social," meaning people sent them to friends; long-form has to do the same or it fails.
2. **Build Your Tribe #933 (Nov 19).** Features up to 90 minutes, horizontal, separate upload flow, up to eight Reels clips attached, "Watch full video" button on the Reel, regular Reels cap at 20 minutes with an in-composer warning over 3:00 about unconnected reach, expects 1,000 followers plus a professional account as the gate, 20 Trial Reels a day as the spam ceiling, Amazon links free with 0 percent Instagram cut and 1 to 10 percent Amazon commissions, 20 links on carousels.
3. **Build Your Tribe #927 (Oct 22).** Retention claims in section 2.
4. **heyDominik (Oct 26).** Skip, watch and share-rate benchmarks in section 2.
5. **Robert Benjamin (Nov 4).** Ranks watch time first, then likes per reach, then sends per reach; "completion rate of 70 percent or higher" target; originality rule; the unverified "45 percent of recommended Reels under a day old" claim; text hook on screen should match the first line of the caption.

---

## 7. Do this now: @elcoyotediesel (577 followers, memes share, build reels 200 to 500 views and 0 shares)

1. **Open the Reels composer today and look for the Trial Reel toggle.** Four late-2026 guides say professional accounts need 200 followers. If it is there, every build reel goes out as a Trial first, hook variants get tested two at a time (one variable changed), and winners are shared to followers after 24 hours. Never post the same cut twice as a Trial.
2. **Write the send line before the shot list.** Mosseri (Oct 23) and Dash Social (Nov 17) both put shares at the center, and the account's own data says memes share because they are about the viewer. Every build reel needs one of: a dollar number, a mistake, a part that fails, a before/after, or a "send this to the guy with the..." line. Put it on frame one and in the first 125 characters of the caption. If a cut has no reason to be sent, it is a Story, not a Reel.
3. **Targets per reel, read in Insights:** skip rate under 45 percent (breakout median per heyDominik; the account's best posts already hit 32), average watch over 10 seconds on a 30-second cut, retention at the end above 50 percent (Brock Johnson), share rate (shares divided by views) above 1 percent as the floor and 2 percent as the goal. Below 1 percent on a build reel means the format, not the footage, failed.
4. **Length: 30 to 60 seconds for cold reach** (Socialinsider, best reach rate at 1k to 5k accounts). Test one 90 to 120 second story-driven build reel per week as a Trial only; Buffer's +7 percent for 90 to 179s came from accounts that already hold watch time, and the account's 6.8s average watch time does not yet. Nothing over 3:00, ever, for reach.
5. **One topic per reel, and make the first frame unmistakably diesel truck.** The Nov 11 Your Algorithm explainer says Instagram classifies each post into LLM-inferred topics and balances exposure across them. Do not mix a meme beat and a build update in one reel. Keep stray objects, music genre and vocabulary in-niche so the classifier sends it to truck people (heyDominik's point), and put the part name or truck in the caption's first line ("7.3 Powerstroke," "F350 6.7," "FASS").
6. **Use the retention graph, not the view count, to grade each reel** (Reel > View insights > Overview > "How long people watched"). Vertical drop at zero means the first frame; cliff after the hook means the hook; slow slide means no second promise. Fix the one shape that keeps recurring.
7. **Cadence a one-man shop can hold: 3 to 4 Reels a week, with Trial Reels as the extra reps.** Lilach Bullock's daily-vs-3x test lost watch-through and followers when volume went up; Robert Benjamin's 7-a-day advice is for teams. Recency matters (Mosseri), consistency matters (Buffer), burnout kills both.
8. **Comment-to-DM only with a real deliverable, at most one post in four, no follow gate.** Candidates: the Rival parts list PDF, the FASS install checklist, a "don't buy this" price sheet. Free ManyChat (25 active contacts a month) or Business Suite's native Comment to Message (15-minute delay). Reply to every comment by hand within 20 minutes regardless (Buffer's +21 percent correlation; Brock's routine).
9. **Connect an Amazon Influencer account in Professional dashboard > Monetization and tag the real parts and tools on screen** (up to 30 per Reel, Instagram takes nothing, product links get about 2x the clicks of a bio link). Paste partner-store affiliate links through "Add products" where a program exists. Q4 is when it pays, and "the parts I actually run are tappable" is a sponsor talking point.
10. **Enroll in content protection the moment the activity-feed notification appears**, protect the Harley trade reel and the gooseneck reel retroactively, and add any second account or partner (Elite Diesel, Rival partners who repost) to the allow list so their reposts are not flagged.
11. **Keep CapCut, strip every logo, skip AI voiceover.** Mosseri (Oct 30): no demotion for third-party editors, demotion for a visible logo. Realistic AI voiceover now requires the AI label (Hootsuite, Nov 4); AI-written captions do not. Edits on Mac is not an option on Windows; Edits mobile is still worth opening for its sends-per-reach readout.
12. **Post every reel to Stories with a line of text, and use the 15-minute Story edit window to fix typos instead of deleting.** Stories reduce unfollows (Mosseri via Hootsuite) and are where the DM conversations that feed "sends" start.
13. **Watch for two gates:** 1,000 followers (features bonuses and, per Brock, the Features test) and the Series US test expected by early 2027. A "Road to SEMA" series of grouped Reels is exactly what Series is built for, and Tessa Lyons called the series benefit a goldmine.

---

## Source index (all fetched 2026-11-21)

- Mosseri, Colin and Samir interview, Oct 26, 2026: https://www.youtube.com/watch?v=sxizdQ2hRfk
- ZoomSphere AMA log (Oct 16, 23, 30 AMAs): https://www.zoomsphere.com/blog/instagram-algorithm-2026-what-actually-gets-reach
- Instagram @creators, content protection, Nov 17: https://creators.instagram.com/blog/introducing-content-protection/
- Instagram @creators, affiliate links, Nov 16: https://creators.instagram.com/blog/more-ways-to-earn-affiliate-links
- Instagram @creators blog index: https://creators.instagram.com/blog
- Edits blog: https://edits.instagram.com/blog and https://edits.instagram.com/blog/edits-cloud-edits-plus/
- TechCrunch, Features Oct 26: https://techcrunch.com/2026/10/26/watch-out-youtube-instagram-goes-from-short-form-to-90-minute-videos/
- TechCrunch, Edits desktop Nov 5: https://techcrunch.com/2026/11/05/instagram-brings-edits-to-desktop-to-take-on-capcut/
- TechCrunch, content protection Nov 17: https://techcrunch.com/2026/11/17/instagrams-new-tool-for-creators-targets-unauthorized-reposts-and-ai-modified-videos/
- TechCrunch, Direct Nov 17: https://techcrunch.com/2026/11/17/meta-launches-direct-a-standalone-messaging-app-for-instagram/
- Meta newsroom, India recommendations Nov 16: https://about.fb.com/news/2026/11/an-update-on-the-content-we-recommend-on-instagram-in-india/
- Social Media Today Instagram topic page: https://www.socialmediatoday.com/topic/instagram/
- Social Media Today, Your Algorithm explainer Nov 11: https://www.socialmediatoday.com/news/meta-publishes-explainer-on-your-algorithm-controls/874460/
- Social Media Today, creator assistant Nov 2: https://www.socialmediatoday.com/news/meta-updates-creator-assistant-chatbot/873524/
- Social Media Today, long-form payouts Nov 4: https://www.socialmediatoday.com/news/instagram-tries-to-entice-long-form-creators/873820/
- Social Media Today, Edits speed curves Nov 12: https://www.socialmediatoday.com/news/metas-edits-app-gets-speed-curves-and-auto-audio-balancing/874586/
- Social Media Today, web Creator Dashboard Nov 18: https://www.socialmediatoday.com/news/meta-brings-its-updated-creator-dashboard-to-the-web/875143/
- Geekout archive and issues (Oct 30, Nov 6, 13, 20): https://geekout.mattnavarra.com/archives
- Link in Bio, Nov 3: https://www.linkinbio.news/p/my-call-with-instagrams-vp-of-product
- Lindsey Gamble, Nov 3: https://lindseygamble.beehiiv.com/p/can-instagram-make-long-form-video-work-this-time
- Jade Beason, Nov 20: https://jadebeason.substack.com/p/instagram-x-amazon-is-here-youtube
- Build Your Tribe episode list: https://www.listennotes.com/podcasts/build-your-tribe-grow-your-business-with-x1YgDoJwb8d/
- Buffer, Reels length Nov 12: https://buffer.com/resources/instagram-reels-length/
- Buffer, algorithm guide Oct 23: https://buffer.com/resources/instagram-algorithms/
- Buffer, trending sounds Nov 3: https://buffer.com/resources/trending-audio-instagram/
- Buffer, DM automation Jun 30: https://buffer.com/resources/instagram-dm-automation/
- Socialinsider Reels stats, updated Nov 17: https://www.socialinsider.io/blog/instagram-reels-statistics/
- Dash Social benchmark Nov 17 (mirror): https://lifestyle.middletownlifemagazine.com/story/840116/instagram-carousels-average-24-more-views-than-reels-dash-social-benchmark-report-finds/
- Hootsuite, AI disclosure Nov 4: https://blog.hootsuite.com/ai-disclosure-policy-for-instagram/
- Later, Features for brands Oct 27: https://later.com/blog/from-reels-to-the-living-room-what-instagrams-long-form-push-means-for-brands/
- heyDominik, Oct 26: https://www.youtube.com/watch?v=6u4MGM_KZ5I
- Build Your Tribe #927 Oct 22: https://www.youtube.com/watch?v=60eaURKkdBk
- Build Your Tribe #933 Nov 19: https://www.youtube.com/watch?v=6i6T33SAIRc
- Robert Benjamin, Nov 4: https://www.youtube.com/watch?v=j3WILAPvgzo
- Creator Lane, Mosseri vs measured: https://creatorlanehq.com/blog/instagram-algorithm-2026-mosseri-vs-measured
- Creator Lane, comment automation playbook: https://creatorlanehq.com/blog/instagram-comment-automation-playbook-2026
- Blotato, ManyChat pricing (updated Nov 9): https://www.blotato.com/blog/manychat-pricing
- Creatorflow, built-in automation (updated Nov 19): https://creatorflow.so/blog/instagram-built-in-automation/
- Meta developers, private replies: https://developers.facebook.com/docs/messenger-platform/instagram/features/private-replies
- FYProof, engagement bait (updated Oct 22): https://fyproof.com/guides/engagement-bait-penalties
- flowgent, Trial Reels 200 followers (Oct 29): https://flowgent.ai/blog/instagram-trial-reels
- vidova, Trial Reels explained: https://vidova.ai/blog/instagram-trial-reels-explained
- SocialBee update log: https://socialbee.com/blog/instagram-updates/
- embedsocial feature log (updated Nov 13): https://embedsocial.com/blog/new-instagram-features-2026/
- napoleoncat update log (Stories edit Nov 18, Effect Builder Nov 9): https://napoleoncat.com/blog/instagram-new-features-and-updates/
- Gain, November edition: https://blog.gainapp.com/social-media-updates/
- ethicalsmm, seven November changes: https://ethicalsmm.com/blog/instagram-updates-november-2026
- PetaPixel, Open to Reels test Oct 9: https://petapixel.com/2026/10/09/meta-tests-opening-instagram-and-facebook-directly-to-tiktok-style-vertical-video-feeds/
- Medianama, content protection and Mosseri quote: https://www.medianama.com/2026/11/223-instagram-copyright-tool-deepfakes-stolen-content/
- BigGo, Mosseri "engagement hack" (secondhand): https://finance.biggo.com/news/397441c73e4684c3
- Social Media Today, Mosseri on hacks: https://www.socialmediatoday.com/news/instagram-chief-debunks-popular-engagement-hack/816781/
- Lilach Bullock, posting frequency test: https://www.lilachbullock.com/how-many-instagram-reels-should-you-post/
- Blend for creators (May 30, 2026): https://instantdm.com/blog/instagram-blend-for-creators-2026
- InstantDM "automated replies" claims (vendor): https://instantdm.com/blog/why-the-instagram-algorithm-loves-automated-replies-in-2026
