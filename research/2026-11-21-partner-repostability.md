# What Rival content gets reposted by partners and diesel media, and the partner kit that makes it happen

Research agent report, 2026-11-21, for @elcoyotediesel / Project Rival (1959 Ford F600, 7.3 Powerstroke, Super Duty frame, Road to SEMA 2027). Builds on `research/2026-11-21-build-series-structure.md` section 3 (sponsor integration) and `research/reel-references/2026-11-21-diesel-niche-winners/BREAKDOWN.md` section 2 (cross-video patterns). North star: every reel should work twice, once on Jacob's account and once on a partner's.

Method (all pulled 2026-11-21, roughly 09:00 to 11:30 MT): Instagram profile pages fetched logged out for 23 brand and media accounts (follower counts from the og:description meta tag with a crawler user agent, the first 12 grid tiles with Instagram's own alt text, which names the author of every tile, so a tile that reads "Video by <creator>" on a brand grid is a co-authored Collab post, not a native repost; reposts live on a separate tab that is not visible logged out). Post captions read from the /p/<id>/ meta tags where Instagram served them. TikTok listings via yt-dlp (`--flat-playlist`, last 10 to 12 posts) for 33 handles. Web sources for the platform mechanics, with vendor claims marked as such.

Four things this changed about what I thought going in:

1. **Jacob already has a Collab live on two partner grids.** His Nov 19 reel "Project Rival is Poppin off!!!" (`/reel/Df7xe9EAq4o/`) sits on @issproofficial and @powerhungryperformance as "Video by Jake Dalton | Diesel Trucks." Both brands accepted. The reel still did 407 views, 317 reach, 14 likes, 4 comments, 0 shares, 4.6 s average watch, 74.7 percent skip (live pull, 11-21). The same-day personal reel did 984 views at 31.6 percent skip with no collaborator. A Collab multiplies a reel that works; it does not rescue a thank-you selfie.
2. **The brands that repost do it by accepting Collab invites, not by reposting.** Across 19 grids, zero visible native reposts (expected, the tab is hidden), but 60 of 228 tiles (26 percent) are co-authored with a creator. Derale runs at 75 percent creator-authored, Power Hungry 67, BD and @dieseltrucking 42, FASS, Industrial Injection and Axiom 33. The caption on the brand's grid is the creator's own caption, so the first line Jacob writes IS the brand's post.
3. **The 1.52x figure in the 11-21 build-series doc is mis-attributed.** Virev's Oct 7, 2026 algorithm study puts 1.52x views on ALL Collab reels versus the same creator's solo reels (nano accounts 1.91x). Sponsored Collabs specifically held 1.00x of usual views versus 0.78x for solo sponsored posts. The doc's "sponsored Collab Reels 1.52x" line should read "Collabs 1.52x, sponsored Collabs 1.00x vs 0.78x solo."
4. **Half the handles we had in mind are dead or wrong.** @drivendiesel is a Sparks NV repair shop (never tag it); @dieseltrucks has 0 posts; @dieselnation stopped in 2021; @dieselsellerz has not posted since Sep 2024; @dieselarmy is a 314-follower nobody; @isspro is a 72-follower nobody. The live ones are in the tables below.

---

## 1. Current partners and prospects: what they post and whether they repost

### 1a. Brand table

| Brand | Handle (IG) | Followers | Cadence (last 12 tiles) | Reposts creators? | Example | Social contact |
|---|---|---|---|---|---|---|
| Driven Diesel / Strictly Diesel | @strictly_diesel | 3,565 (768 posts) | unknown: profile is age-gated 18+, logged-out read blocked | unknown | Jacob's Nov 19 "S/O to the big dawg Driven Diesel Performance aka @strictly_diesel" reel (320 views, 66.1 skip, 0 shares) tagged them; no sign it was a Collab | Dennis Schroeder, co-owner (email thread 11-18). No TikTok (the @strictly_diesel TikTok is a Peterbilt fan page) |
| ISSPRO | @issproofficial | 2,833 (323 posts) | about daily Nov 6 to 20; 7 photos, 3 own reels, 2 Collabs | **Yes** | @elcoyotediesel Nov 19 (Rival); @doubledutydiesel Nov 15 carousel "EGT gauge and custom length lead... 6BT powered motor home" (13 likes); @crazy.k.kustomz Nov 6 reel | No name found. Account DM; X @Isspro3; Portland OR HQ. Their own reel captions are literally "www.ISSPRO.com" (4 likes), so Jacob's clip is the best thing on their grid |
| Power Hungry Performance | @powerhungryperformance | 6,970 (455 posts), verified | about 2 a week Oct 14 to Nov 19 | **Yes, 8 of 12** | @elcoyotediesel Nov 19; @veronica_cars Nov 7 (Diesels in Dark Corners event, 42 likes); @73dipstick Nov 1 race recap naming "the @powerhungryperformance hydra chip" (22 likes) and Oct 18; @dillon.houck Oct 30 (SEMA Corral Subaru giveaway guy); @holders_diesel Oct 14, 15, 17 (Chimera release party) | Bill Cohron, founder (no social operator named). TikTok @powerhungryperformance: 7.3 memes, 153 to 11.2K views, last post Sep 4 |
| Move Bumpers | @movebumpers | 97K (3,293 posts) | daily Nov 8 to 20; photos, reels, carousels | **Yes, 3 of 12** | @lurkoffroad photo Nov 18; "Macaiah Schoch" reel Nov 11; "Casey" reel Nov 11; bio: "tag #MOVEBumpers for a feature" | Kevin Casteel (Marketing, per ZoomInfo), Kathy Sas (GM); outside agency Hudson Integrated runs digital. HQ Lewistown MT. TikTok dead since Dec 2023 (1K to 5K views) |
| Axiom Supply | @axiom_supply | 25.6K (362 posts), verified | about 5 a week Nov 4 to 18, mostly reels | **Yes, 4 of 12** | @ironrodoffroad reels Nov 5 x2 (coil, auto part: install clips); @holdosi_30 reel Nov 11 (wrench in frame: install); @limitless_auto_pnw photo Nov 13 | "Josh," founder (first name only, via Diesel Power Products "Diesel Talk" video). lnk.bio/axiomsupply. No TikTok videos. Ad library shows 3 live Meta ads, 3 run as partnership ads with creators |
| CNC Fabrication | none found | n/a | n/a | n/a | Tried cncfab, cncfabrication, cnc_fabrication, cncfab_, cncfabrication7.3: all unrelated | Corey Hurtt (waiting on him and Chris since 11-19). Facebook: facebook.com/cncfabricationllc; site cncfab.us; Bryan OH. Hand them the kit for Facebook |
| Industrial Injection | @iidiesel | 201K (3,374 posts) | daily or more, Nov 14 to 21 | **Yes, 4 of 12** | @m.h.p.d.inc Nov 18 "SHE'S ALIVE!!!" first-fire reel (1,458 likes) and Nov 19; @welderupvegas Nov 20; @beamanbuilds Nov 14 | Scott Dana (@scottddana, text). TikTok @iidiesel daily, 585 to 13.9K; "WHICH YOUTUBER IS GETTING THIS ENGINE?!" 2,936 views. Sponsorship page now 404 |
| BD Diesel | @bd_performancemanufacturing | 23.9K (1,494 posts), verified | daily Nov 12 to 20 | **Yes, 5 of 12** | @boostedsixx reels Nov 15, 18, 19 (the "Ramborghini" builder); @six.ho3 carousel Nov 15 "Engine tear down, heads going off to machine shop" (117 likes); @merganevans Nov 15 | Paul Thiessen (LinkedIn). Creator program bddiesel.com/pages/collab (details below). TikTok @bddieselperformance: "How much does it cost to have a booth at the SEMA show?" 122.9K views, 2,193 shares; "Carnage Corner" series |
| PPEI | @ppei_tuning | 131K (734 posts) | **Instagram dormant since Sep 14, 2026**; before that 1 to 3 a week | 1 of 12 | @code_stpeter63 photo Jul 7 | Kory Willis (@kory_ppei, on camera). TikTok @ppeituning is where they are: 8 posts Nov 5 to 21, 219 to 1,486 views. Not an Instagram repost path right now |

Reference brands already in the memory (not Rival partners yet): FASS @fassfuelsystems 290K, 4 of 12 creator-authored, 3 to 4 posts a day, Jake Hopkins marketing director; S&B @sbfilters 90K, 3 of 12 (two are @socalsupertrucks dealer builds with the full parts list as the caption); Derale @deraleperformance 8,362, 9 of 12 creator-authored, the highest ratio in the set.

### 1b. What the reposted creator content looks like (from the credited tiles and the captions Instagram served)

| Type | Seen on | Example caption that made a brand grid |
|---|---|---|
| Milestone (first fire, engine in, teardown) | II, BD, FASS | "SHE'S ALIVE!!!" (@m.h.p.d.inc, on both @iidiesel and @fassfuelsystems, 1,458 likes); "Engine tear down, heads going off to machine shop" (@six.ho3 on BD) |
| Install with a thank-you in line one | Derale, Axiom, ISSPRO | "Big thanks to my guys @deraleperformance for the oil filter relocation kit, now can get our new motor mounts on and drop this bad boy in" (@cockrencustomz); "@issproofficial egt gauge and custom length lead to suit customers 6bt powered motor home, last pic why to have an ISSPRO egt gauge" (@doubledutydiesel) |
| Race or event recap that names the part | Power Hungry | "#agnustheshortbus went racing again... the @powerhungryperformance hydra chip with @jelibuilt tunes... happy to see a #73powerstroke take the win" (@73dipstick) |
| Dealer build sheet | S&B | "2027 Ford F-350 Platinum, S&B 2 to 3.5 in Fully Loaded Suspension System... S&B 68 Gallon tank..." (@socalsupertrucks, 136 likes) |
| Brand-owned "news" using the creator's footage | FASS (TikTok) | Kevin Young 2,078 hp iron-block 6.0: 133.7K views, 3,943 shares (2.95 percent), brand mentioned in one clause at 0:27 |
| SEMA / show presence | Derale, Hot Shot's Secret, PRI | @helloooimjensen "I will be at @semashow burning tires..." (1,171 likes, on Derale); @donabenante on HSS |
| Dyno numbers, before/after, UGC testimonial to camera | none in the 60 credited tiles | Nobody in this set is reposting talking-head testimonials. The brands repost footage of the part doing something, with the creator's words underneath |

Patterns across the 60 creator-authored tiles:
- The brand is named or tagged in the creator's first sentence in every caption Instagram served. Nothing buried.
- Video over stills, 48 of 60. The stills that got through are carousels with the part visible and a parts list.
- The brand did nothing but tap Accept. Every one of these is a Collab the creator initiated (the alt text names the creator as author and the tile links into the creator's own profile).
- The clip is about the truck, the brand is a clause. Same lesson as FASS Kevin Young and the account's own SPONSOR vs PERSONAL numbers.
- Nobody is on screen thanking the brand. The thanks is in the caption.

### 1c. What partners want from a creator (their own words)

- **BD Diesel creator program** (bddiesel.com/pages/collab): perks are commission on sales through an affiliate link or code, early access to launches "including opportunities to test or feature new products before they're publicly announced," coordinated access to engineering for technical questions, and a parts discount. Expected: "Authentic, Build-Focused Content... installs, walk-throughs, reviews, or on-truck updates"; approved logos and BD style guidelines; "No misleading claims or comparisons against competitors"; consistent activity, "tagging BD Diesel when appropriate"; respond to marketing opportunities and share audience feedback. Apply via the page.
- **Industrial Injection** sponsorship page (now 404, cached wording via search): partners who "represent our brand professionally and provide real value in return." II has given an 800 hp 12-valve to the Laytona 250 winner and runs engine-giveaway content for named YouTubers; the leverage is footage of their part doing something, not a thank-you.
- **Hot Shot's Secret Secret Society** (The Shop, Apr 30 2026): seven founding ambassadors (Don Abenante, Devin Henry, Mickayla VanBuren, Jake Hopkins of FASS, Jimmy Dale, Emily Reeves, Morgan Evans), R&D lab access, the ask is that they "understand the science" and "explain how those products work in ways their audiences will relate to." Matt Ryce, influencer marketing manager: "builders and racers who are actually putting in the work." Josh Steinmetz, brand manager. Kyle Fischer, director of field marketing and partnerships.
- **Move Bumpers**: bio asks owners to "tag #MOVEBumpers for a feature." Three of twelve tiles are exactly that.
- **Diesel World Readers Rides**: "messaging us on Facebook, Instagram, or by filling out the submission form on dieselworldmag.com"; older page asks for "a print-quality, horizontal photo" plus a short description.
- **FTC baseline** (16 CFR 255, as summarized by 2026 compliance guides): free product is a material connection; the platform label is "the minimum, not the finish line"; "#sp", "#collab", "ambassador" and a bare "thanks [Brand]" are not enough; disclosure in the first lines, and spoken plus on-screen for video. For Jacob: "Parts provided by @brand for Project Rival" in line three plus the Paid partnership label covers it.

---

## 2. Diesel media and aggregator accounts

| Account | Handle | Followers | Cadence | Creator-authored (last 12) | How they take submissions / what they pick | Contact |
|---|---|---|---|---|---|---|
| Diesel World | @dieselworldmag | 80.2K (3,501 posts) | near daily, reels and photos | 2 of 12, both the publisher's own photographer (@pistonsandink, Chris Hamilton) | Readers Rides monthly: DM on IG or FB, or the form on dieselworldmag.com; wants a horizontal print-quality photo plus a short write-up. May 2026 edition ran a 1988 F-150 body on an F-350 chassis with a 2001 Power Stroke, the closest thing to Rival they have printed this year. No creator Collabs observed | Tucker Harris, editor-at-large (letters through Apr 2026); tucker@engaged.media (older page). TikTok dead since Apr 2023 |
| Diesel Army | @dieselarmymagazine | 25.9K (4,474 posts) | daily carousels, no reels in the last 12 | 0 of 12 | "Reader's Ride of the Week" by Facebook message (older page); their IG is article promotion | Artie Maupin, editor (Power Automedia). TikTok dead since Nov 2024 |
| DieselSellerz | @dieselsellerz | 523K (1,503 posts) | **dormant since Sep 8, 2024** | 0 | Not a path. The audience moved to @heavydsparks (4M) | none |
| "@dieseltrucks" | @dieseltrucks | 89, 0 posts | dead | n/a | The live aggregator with that name is **@dieseltrucking**, 1.4M (11K posts), near daily, **5 of 12 creator-authored** (@langomotorsports x2, @hostilewheels, @mcgaughys, @danascustoms); bio "Daily source for #Diesel #Trucks, Business Inquiries Contact Us" | DieselTrucking@yahoo.com; dieseltrucking.co. TikTok dead since May 2025 |
| Diesel Nation | @dieselnation / @dieselnation_ | 18.4K (dormant since Mar 2021) / 32.4K (590 posts, last Oct 16) | the underscore one posted 8 reels Oct 11 to 16 then stopped | 0 of 12, all re-uploads with no credit | Bio: "Diesel content daily! DM for Advertisement." Pay-to-play reupload page; exactly the account type Instagram's Apr 30, 2026 originality policy demotes | none worth having |
| Ultimate Callout Challenge | @ultimatecalloutchallenge | 74.6K (8,280 posts) | daily | 0 of 12 | Event account; it posts entrants and sponsors, not builds. Next show June 4 to 6, 2027; media applications open in April (TikTok Apr 12 post). TikTok seasonal: 180K on "seventy2 Fast Class" | Cody Brown, @cwb6.7 "for ALL QUESTIONS," cody@dpiexpo.com |
| PRI | @myprishow | 229K (6,868 posts) | daily | 2 of 12 (@realbrianmello, @the_xcalibur) | Show Dec 10 to 12, 2026, Indianapolis. Reposts exhibitor and racer clips during show weeks. TikTok active, 92 to 27.5K | linktr.ee/myprishow; press via performanceracing.com |
| Banks Power | @bankspower | 330K (2,920 posts) | 1 to 2 a week, memes and tests | 2 of 12 (@davesautocenter Oct 2025, @chucklesgarage Oct 15) | "Review Us, Please!" asks owners to tag the brand on IG; customer stories go to their YouTube. No TikTok videos | none named |
| Hot Shot's Secret | @hotshotssecret | 71.3K (6,771 posts) | daily plus | 1 of 12 (@donabenante, a Secret Society member) | Reposts come through the ambassador program; cold creators get nothing visible. TikTok @hotshotsecret daily, 338 to 4.2K | Matt Ryce (influencer marketing manager), Josh Steinmetz (brand manager), Kyle Fischer (field marketing and partnerships) |
| Fleece Performance | @fleeceperformance | 120K (2,386 posts) | **dormant since Sep 16, 2026** | 3 of 12 (@connor_osully, @zero_tolerance_diesel, @thefallshowdown) | Customer builds with Fleece turbos; nothing since September. TikTok sporadic; the one tribe post ("6.7L Power Stroke Owners!") did 56.4K | none found |
| S&B Filters | @sbfilters | 90K (1,596 posts) | daily | 3 of 12 (@socalsupertrucks x2, @alloutoffroadperformance) | Dealer builds with the parts list caption; product clearly on the truck. TikTok last post Jul 2026 (447K on bump spacers) | none found |
| FASS | @fassfuelsystems | 290K (4,801 posts) | 3 to 4 a day | 4 of 12 (@m.h.p.d.inc x2, @matt.latino, @polardiesel) | Reposts first fires, dyno records, customer trucks; brand-owned "news" reels built from creator footage (Kevin Young). TikTok daily; the record post shared at 2.95 percent | Jake Hopkins, marketing director (SEMA FLN profiles), also a Hot Shot's Secret ambassador |
| Derale | @deraleperformance | 8,362 (992 posts) | about 2 a week | **9 of 12** | Will co-author almost any install or event clip that names the part (@cockrencustomz oil filter relocation, @helloooimjensen SEMA drift car) | none named; existing relationship per CLAUDE.md |
| Diesel Power Products | @dieselpowerproducts | 200K (4,628 posts) | 2 to 3 a day | 0 of 12 | Retailer; everything is in-house (host "Kyle"), including the 925K deadpan TikTok. Runs "Diesel Talk" interviews with brand founders (Axiom's Josh). Pitch is a product story, not a repost | none named |

**What makes a media or aggregator account pick a clip** (from the 60 credited tiles plus the two 2 percent-share brand posts in the BREAKDOWN):
1. The creator already did the work: shot vertical, wrote the caption, sent the Collab invite. The account only taps Accept. None of the 19 grids shows a cold repost of an untagged creator.
2. One fact a named tribe will argue about (2,078 hp iron block; "3rd Gen owners, this one's for you"). News travels, builds do not.
3. The part or the brand is visible or named inside the first line and the first three seconds.
4. A milestone frame (first fire, engine in, bare block on the bench) over a product-on-a-table frame.
5. Length 9 to 36 s for the ones that moved. Horizontal only for Diesel World print.
6. Credit style the accounts themselves use: alt-text author plus the creator's own caption (Collab), or a "Via @handle (IG)" line in the caption on TikTok (@dieseltrucking's old TikToks: "Via mainlyofthepatrols_ (IG)").

**DM pitch that matches how they operate** (under 60 words, one clip link, no deck): "Jake with Project Rival, a 1959 F600 going on a Super Duty frame with a built 7.3, Road to SEMA 2027. Here's the 20 s of the block coming off the bench [link]. Your audience is 7.3 guys. I'll send you a Collab invite on the next one so it sits on your grid; you just accept. Vertical, credited, no edits needed." For Diesel World add a horizontal still and three lines of spec and send it to the Readers Rides form the same week.

---

## 3. Platform mechanics as of Nov 2026, with dates and sources

### 3a. Collab posts

- **What it is.** One post, two to six authors, one set of likes, comments and view count, shown on every accepting author's profile and pushed to each author's followers. Launched Oct 2021. Meta's Aug 11, 2023 newsroom post: "invite up to three friends to co-author a feed post, carousel or reel"; the current app limit is five collaborators plus the creator (Instagram's Reels tips page and Help Center, cited by Adobe, Neal Schaffer, Sked; the Meta publishing API accepts three usernames). (about.fb.com/news/2023/08/music-and-collabs-on-instagram/; skedsocial.com/blog/instagram-collaboration-feature)
- **Invite flow.** On the share screen: Tag people, then Invite collaborator (on a Reel: Add tag, then Invite collaborators; a plain tag does not put it on the other grid). Can be added after publishing: three dots, Edit, Tag people, Invite collaborator. The invitee gets a notification; until they accept the post shows only on the creator's profile; on accept it appears on both and goes to both follower sets. A collaborator can remove themselves; the creator can remove them. A private account can invite only accounts that follow it; Collabs do not exist for Stories. (buffer.com/resources/instagram-collab-post/; loomly.com/blog/instagram-collab-posts-how-to; socialpilot.co/blog/instagram-collab-post)
- **Who can accept.** Any public professional, creator or personal account; no follower minimum. Observed: ISSPRO (2.8K) and Power Hungry (7K) accepted Jacob's invite within the day. (observed 11-19 to 11-21)
- **How reach combines.** The post is one object served to both follower graphs; distribution beyond that is ranking as usual. Insights: conflicting reports. Meta's developer docs say insights exist only for media the account owns, and one guide reports no "View insights" button for the non-owner; Buffer and others say both see the dashboard. Jacob is the owner on every Rival Collab, so he gets the full Insights either way; assume the brand sees public counts only. (socialscheduler.ai/blog/instagram-insights; buffer.com/resources/instagram-collab-post/)
- **Collab plus Paid partnership label.** Separate toggles, both can be on the same post; the Collab tag is not a disclosure. Label required when there is an exchange of value, including gifted or loaned product. (makeinfluence.com academy; vamp.com paid-partnership guide; influencerfee.com)
- **The data.** Virev, published Oct 7, 2026, updated Oct 30: 10,442,930 reels from 288,117 creators, Aug 18, 2025 to Sep 29, 2026; Collabs are 26 percent of reels; fixed-effects model against the same creator's own reels; Collabs get **1.52x views and 1.51x likes plus comments**; by tier, nano 1.91x, micro 1.46x, mid 1.17x, macro 1.07x, mega 0.99x; the lift comes from small accounts co-authoring with bigger ones. Sponsored Collabs kept **1.00x** of usual reel views vs **0.78x** for solo sponsored posts. The 0.79x vs 0.64x likes-and-comments pair in the build-series doc is from Virev's separate paid-partnership post. Vendor data, no independent replication. (virev.ai/blog/instagram-algorithm; virev.ai/blog/use-instagram-s-paid-partnership-label-correctly)
- **Who should initiate.** A secondhand Mosseri line says Collabs reach more when the larger account starts the post (unverified). FASS's Kevin Young reel is the working model: the brand owns the post, the creator's footage is the content, the creator is tagged or co-authored. Ask partners with real followings (FASS-size, II-size) to post Jacob's clip as their own and invite him as collaborator; let Jacob initiate with the small ones (ISSPRO, Power Hungry, Axiom).
- **Jacob's own test.** Nov 19 Collab with two partners totalling about 10K followers: 407 views. The co-authors added maybe a couple hundred views; the hook capped it. Build the reel for Jacob's audience first, then collab.

### 3b. Reposts (native)

- **Launch.** Aug 6, 2025 (Instagram newsroom, GMA, Social Media Today). "Repost public reels and feed posts"; reposts are "recommended to your friends' and followers' feeds" and "will also be in a separate tab on your profile"; "Reposts are credited to the original poster"; you can add a note in a thought bubble. For creators: reposted content "may be recommended to that person's followers, even if those people don't follow you." No opt-out described on that page; later reports of creator-side controls are unconfirmed. (about.instagram.com/blog/announcements/instagram-new-features-connect-friends/)
- **Originality policy.** Apr 30, 2026: the Reels-only rule since 2024 now covers photos and carousels; accounts that mostly share content they did not create or meaningfully transform are not recommended to non-followers, judged over a month; Mosseri: "If most of what you post to Instagram is someone else's content, your account is no longer going to be recommendable." Instagram's named alternatives: remix with your own words, use the built-in repost button, or publish a Collab with the original poster. (petapixel.com/2026/04/30/new-instagram-policies-target-reposted-content/) Mosseri's Sept 2026 ranking series (videos Sep 2 or 3, 8, 17) names originality as one of four ranking principles. (zoomsphere.com, kabo.sh guides; the "10 reposts in 30 days" threshold and "40 to 60 percent" figures appear only in vendor blogs and are unverified.)
- **How brands use it.** Marketing coverage frames reposts as the safe way to show customer content with automatic credit and no grid clutter. In practice the diesel brands in this set use Collab for the grid (it reads as original co-authored content) and, presumably, the Reposts tab for the rest; we cannot see the tab logged out. A brand reposting via the tab gives Jacob a feed placement to its followers with his handle on it and no caption of their own; a brand co-authoring gives him a permanent grid tile with his caption. Ask for both: accept the Collab, then also tap Repost with a one-line note, which hits their followers' feeds a second time.
- **For Jacob's own account.** Never re-upload a partner's clip; use Repost or Collab. One re-upload a month will not trip the policy; a habit will.

### 3c. Add Yours and templates

- Add Yours sticker: Stories, Nov 2021. Add Yours on Reels: Aug 16, 2022 (a prompt page collects every reel that joins). Aug 11, 2023: creators can pick favorites from a prompt and participants get notified. Dec 15, 2023: customizable Add Yours templates for Stories (pinned elements others cannot change). Reels template browser (Recommended, Trending, Saved) since Jul 2023; a reel needs three or more clips to be usable as a template, and a video edited outside the app is treated as one clip. Secondary logs (SocialBee) list a "Template" option inside the Add Yours sticker in Oct 2025, trending Add Yours prompts surfaced in Mar 2026, and cross-posting Add Yours stories to Facebook in Jul 2026; not confirmed against Meta. (techcrunch.com 2022-08-16 and 2023-12-15; about.fb.com 2023-08; planoly Reels templates guide; socialbee.com instagram-updates)
- Brand participation: the documented wins are small-shop Stories prompts ("show us your purchase"). Nothing in the diesel set uses it. For Rival this is a Story-tier tool: an Add Yours "show me your 7.3" prompt reaches followers only. Reels templates matter in one case: if Jacob cuts a reel in-app from three plus clips, a partner's audience can tap Use template and remake it with their own truck, which is a free UGC mechanic for Move Bumpers-type brands. Low priority; note it and move on.

### 3d. What this means for the house rules

The caption's first line is doing double duty: it is Jacob's share line AND the brand's grid caption. Write it so a 7.3 owner who follows @powerhungryperformance and has never heard of El Coyote understands it in one read. The series line ("Project Rival, EP 07. 1959 F600, 7.3 Powerstroke, Road to SEMA 2027") now matters more, because on the partner grid it is the only context. Partner tag plus Collab invite plus Paid partnership label on every episode where parts changed hands; the disclosure line in the caption; nothing on screen (house rule holds).

---

## 4. The partner kit Jacob delivers per episode

Goal: a partner can post about Rival in under ten minutes with no editing, in their own channel, with the right credit and the right claims. One Drive folder per episode, `My Drive/VIDEO/out/partner-kits/S1-EPnn-<brand>/`, link sent 24 hours before the episode goes live so the Collab is accepted the hour it posts.

### 4a. Files

| File | Spec | Content rule |
|---|---|---|
| `01-hero-15s.mp4` | 9:16, 1080x1920, H.264, 30 fps (24 if shot that way), 8 to 12 Mbps, AAC 48 kHz, 12 to 18 s, under 100 MB, no burned-in text, no music, original audio at -14 LUFS | The part in use on the truck. Jacob says the brand name once, inside the first 5 s, in a full sentence ("Driven Diesel regulated return, going on a 7.3 that has to make 600"). Opens on motion, ends within 1.5 s of the payoff. Subject kept inside the center 1080x1350; top 250 px and bottom 320 px clear of anything that matters |
| `02-hero-15s-captioned.mp4` | same, with light SemiBold captions, thin outline (house caption style) | For brands whose audience watches muted (Move, Axiom). Same cut |
| `03-install-30s.mp4` | 9:16, 25 to 32 s, 5 to 7 shots, no voice, original sound | The vertical install sequence: box open, first fitting, hands, macro, the part on the truck. Brands can lay their own VO or music over it |
| `04-install-voice.wav` | 48 kHz mono | Jacob's "why this part" sentence and the thank-you, separate from picture, so the brand can use the line over their own footage |
| `05-still-truck-4x5.jpg`, `06-still-part-1x1.jpg`, `07-still-horizontal-16x9.jpg` | sRGB JPG, 4:5 1080x1350, 1:1 1080x1080, 16:9 at 4000 px wide (print) | Part on the truck, truck recognizable, no shop signage, no Elite Diesel anything. The horizontal is for Diesel World Readers Rides and the brand's website |
| `08-cover.jpg` | the lockup frame from the episode | So the partner's repost thumbnail matches the series look |
| `09-caption.txt` | paste-ready, under 300 characters before tags | See 4b |
| `10-quote.txt` | three lines | Testimonial line (under 20 words, Jacob's voice), the "why this part" sentence, one spec line (part number, fitment, the number it has to hit) |
| `11-tags-and-disclosure.txt` | | Handles, the disclosure line, the rights line |
| `12-raw/` (optional) | the 3 to 5 best raw clips, untrimmed, HDR off | Only for partners who edit (FASS, II, BD run in-house teams). Lets them cut their own "news" reel in the Kevin Young format |

Every file is El Coyote only. No shop, no 307, no Elite Diesel in frame, on a shirt, or in a filename.

### 4b. The caption they can paste (template)

Line 1: the fact, written for their audience. "A 1959 F600 is getting a 7.3 built for 600 hp. The fuel system went on this week."
Line 2: the credit. "Build and footage by @elcoyotediesel. Project Rival, 1959 Ford F600, 7.3 Powerstroke on a Super Duty frame, Road to SEMA 2027."
Line 3: their product, one clause. "Running our 7.3 regulated return kit with the fuel bowl delete."
Line 4 (optional): their question. "What would you run for fuel at 600 hp?"
No hashtag wall. Two hashtags max if their house style uses them.

Jacob's own caption on the same episode: line 1 share line, line 2 series line, line 3 "Parts provided by @brand for Project Rival," then Tag people plus Collab invite plus the Paid partnership label.

### 4c. Tag rules

- One partner per episode. Never two brands in one reel (the classifier note and the sponsor template both say this; it also keeps the Collab list to one brand plus Jacob).
- Tag the brand's real handle: @strictly_diesel (not @drivendiesel), @issproofficial (not @isspro), @powerhungryperformance, @movebumpers, @axiom_supply, @iidiesel, @bd_performancemanufacturing, @ppei_tuning. Wrong-handle tags send the Collab invite to a stranger.
- Tag people AND Invite collaborator; the tag alone does not put it on their grid.
- Brands may re-tag @elcoyotediesel and must keep "Build and footage by @elcoyotediesel" when they post the files.
- SEMA is "the target," never a promise. The brand's caption gets the same wording.

### 4d. Disclosure and rights lines (in `11-tags-and-disclosure.txt`)

- Jacob's side: "Parts provided by @brand for Project Rival." Paid partnership label on. Spoken thank-you lands at the payoff (sponsor template 5.5), which also satisfies the "say it in the video" guidance.
- Brand's side: nothing extra needed (it is their product), but if they quote Jacob they keep the "Parts provided" sentence intact rather than trimming it to a bare thanks.
- Rights: "El Coyote grants [brand] a non-exclusive, perpetual license to post these files on brand-owned social channels, website and email with credit to @elcoyotediesel. No paid promotion (boosts or partnership ads) without written OK from Jacob. No edits that change what is said about the part." Partnership ads need the creator's approval inside Instagram anyway; this just says it up front.

### 4e. What to ask the partner for, in order

1. Accept the Collab invite within the hour (combined first-hour signal is the whole point).
2. Tap Repost on it with a one-line note (second feed placement to their followers).
3. Story it with @elcoyotediesel and a link sticker to their product page.
4. Post `01-hero-15s.mp4` as their own reel with Jacob invited as collaborator (the larger account originates; the Kevin Young model). For FASS or II scale, send `12-raw/` too and let them cut the "news" version.
5. Use `07-still-horizontal-16x9.jpg` and `10-quote.txt` on their site or dealer newsletter.
6. Put Rival in their SEMA 2027 plans now (booth time, a slot on the floor) so the finale has a place.

### 4f. Jacob's checklist per episode (adds to the seven-item pre-flight in the series bible)

Shoot the 15 s hero as its own take with the brand said once. Shoot the three stills before the part goes on and after. Film the horizontal. Export the kit the same night. Send the folder link and the exact posting time. Post, invite, label, Story. Check the partner grid the next morning; if the Collab is not accepted by noon, text the contact.

---

## 5. Eight Rival reels built to be reposted by a named partner

All obey the house rules: open on motion, one lockup on the hook and nothing else burned in, no on-screen CTA, no outro, end within 1.5 s of the payoff, song added in-app on music cuts, share line in caption line 1, the brand spoken once, El Coyote only. Each one is a real episode of the build with the partner's part as the payoff, never a thank-you reel.

**1. "FUEL SYSTEM" for Driven Diesel / @strictly_diesel (S1 EP 05, box day or install day, 28 s)**
- Hook: cold open on the stock 7.3 fuel bowl in Jacob's hand over the empty valley, lockup block FUEL SYSTEM.
- Shown: the dead-head stock layout versus the regulated return laid out on the fender; hands plumbing the heads; macro of the regulator; the fitment catch (a line that needs re-routing); the loop complete.
- Spoken brand line (one): "Driven Diesel regulated return. Every injector on this 7.3 sees the same pressure, which is the only way it lives at 600 horse."
- Caption line 1: "Send this to whoever is still dead-heading a 7.3."
- Why they repost it: it is the product explainer Dennis's own feed cannot shoot (his profile is age-gated and barely readable logged out); install plus the "why" from a parts guy, in their words from the 11-18 email.

**2. "GAUGES" for @issproofficial (S1 EP 06, 25 s)**
- Hook: cold open on the EV2 pyro needle sweeping on first power-up inside the '59 cab (motion in frame 1), lockup GAUGES.
- Shown: the bare 1959 dash; drilling the pod; the thermocouple going into the manifold; the harness; the dash lit at dusk.
- Spoken brand line: "ISSPRO gauges, because a 29-year-old engine with compounds tells you it is dying about four seconds before it does."
- Caption line 1: "What is the one gauge you would never run a diesel without? Comments."
- Why they repost it: their grid is product photos captioned "www.ISSPRO.com"; the only creator tiles on it are EGT installs; this is one, on a truck nobody else has.

**3. "THE CHIP" for @powerhungryperformance (S1 EP 06 alternate, 22 s)**
- Hook: cold open on the Hydra chip sliding onto the 1996 PCM edge connector, lockup THE CHIP.
- Shown: the PCM out from under the dash; cleaning the connector; the chip seated; the media interface on the dash; the first tune selected; one smoke roll from the pipe (JMR two-shot: one line from the seat, then hold on the pipe).
- Spoken brand line: "Power Hungry Hydra. Multiple tunes on a 1996 PCM so the same truck can tow Monday and run the target by Friday."
- Caption line 1: "7.3 guys, this one's for you. A 1996 PCM can do this."
- Why they repost it: 8 of their last 12 tiles are creator Collabs, including race recaps that just say "hydra chip" once; their TikTok is 7.3 memes; this is their whole audience.

**4. "WHAT IS ON THE FRONT" for @movebumpers (giveaway tie-in, 15 s, music episode)**
- Hook: cold open on Jacob's hand tearing wrapping paper taped over the '59's front end (this week's "wrapping paper reveal" format), lockup block FRONT END.
- Shown: 1 s per shot, wide-detail-wide (throtl grammar): the bare 1959 nose, the bumper kit on the floor, tack welds, the kit on the truck, dead-on front held 2 s.
- Spoken brand line: none in the music cut; the box label is the brand. On the captioned version Jacob's one line in caption: "MOVE kit, weld it yourself, which on this truck is the point."
- Caption line 1: "Send this to the guy who still thinks a '59 should keep the chrome."
- Why they repost it: they feature anything tagged #MOVEBumpers, 3 of 12 tiles are customer clips, and it gives the giveaway a reveal moment. Entry mechanic lives in their post, not Jacob's.

**5. "FRONT END" for @axiom_supply (donor-frame episode, 24 s)**
- Hook: cold open on a 20-year-old Super Duty ball joint with visible play, Jacob's hand rocking the wheel (motion), lockup FRONT END.
- Shown: the donor frame on stands; the old parts in a pile; new bearings, ball joints and tie rods laid out; press work; torque wrench click; the hub spinning free.
- Spoken brand line: "Axiom front end. A 2005 Super Duty frame under a 1959 cab gets new everything, lifetime warranty, because this one gets driven."
- Caption line 1: "Every Super Duty owner buys these twice. Here is the once."
- Why they repost it: all four of their creator tiles are install clips with a wrench in frame; this is one, on a frame swap, with the daily-driven claim their warranty line wants.

**6. "INJECTORS" for @iidiesel (prospect; the long-block episode, 30 s)**
- Hook: cold open on eight injectors in a row on the bench, one stock cup next to them, lockup INJECTORS.
- Shown: the bore numbers printout (callback to THE NUMBERS); heads on; injector cups; the set going in; hold-downs torqued; the number on screen once in the caption, not the video.
- Spoken brand line: "Industrial Injection sized these for 600 at the wheels on a 7.3. Any more and I am buying rods twice."
- Caption line 1: "67-year-old truck. 29-year-old engine. 600 horsepower. Send it to someone who'd drive it."
- Why they repost it: their creator tiles are first fires and milestones ("SHE'S ALIVE" did 1,458 likes), their TikTok runs "which YouTuber is getting this engine" build content, and Scott Dana already has Jacob's number. Send the raw folder so they can cut their own version.

**7. "HPOP" for CNC Fabrication (prospect; Facebook-first kit, 22 s)**
- Hook: cold open on the old high-pressure oil pump coming off, oil stringing (motion), lockup HPOP.
- Shown: stock pump versus the new one side by side; the fuel line kit laid out; install; the gauge needle reaching ICP target on crank (callback to GAUGES).
- Spoken brand line: "CNC Fabrication pump and lines. A 7.3 at 600 is an oil pressure problem before it is a fuel problem."
- Caption line 1: "Send this to the 7.3 guy chasing a hard start."
- Why they repost it: they have no Instagram, so the kit goes to their Facebook page (facebook.com/cncfabricationllc) as native uploads with the caption file; the horizontal still goes on cncfab.us. Corey gets a finished post, not a request.

**8. "CARNAGE CORNER, RIVAL EDITION" for @bd_performancemanufacturing (prospect; format match, 12 s, DPP deadpan)**
- Hook: spoken, 0:00, deadpan, phone pointed at the worst thing that came out of the 7.3 or off the 1959 chassis (a wiped cam lobe, a cracked exhaust manifold, the baling-wire fix), finger enters frame.
- Shown: three shots, each tighter, finger tapping it. Ends on "What do you guys think?"
- Spoken brand line: "This is going to BD for Carnage Corner." (said once, as the reason the part exists on camera)
- Caption line 1: "Send this to the guy who fixes everything with zip ties."
- Why they repost it: BD's TikTok runs a weekly "turbo carnage" series fed by creators ("This weeks turbo carnage comes from the guy behind the camera"), their grid is 5 of 12 creator Collabs, and the format shared 2,804 times for DPP at 9 s. It opens the door without BD having a 7.3 part on the truck yet.

Hold for later: a @ppei_tuning idea is not worth building until their Instagram wakes up (dormant since Sep 14); their TikTok with Kory on camera is the live channel, and that is a text to Kory, not a reel.

Order of play for the next four weeks, matched to the series bible's week plan: 1 (Driven Diesel) and 2 or 3 (ISSPRO or Power Hungry, whichever has product in hand) in week 3; 4 (Move) the day the kit lands; 5 (Axiom) when the donor frame is on stands; 6, 7, 8 as the parts and the prospects come through.

---

## 6. Source index

Instagram profile and post reads (2026-11-21): instagram.com/issproofficial/, /powerhungryperformance/, /movebumpers/, /axiom_supply/, /iidiesel/, /bd_performancemanufacturing/, /ppei_tuning/, /strictly_diesel/ (age-gated), /fassfuelsystems/, /sbfilters/, /fleeceperformance/, /deraleperformance/, /bankspower/, /hotshotssecret/, /dieselworldmag/, /dieselarmymagazine/, /dieselsellerz/, /dieseltrucking/, /dieselnation/, /dieselnation_/, /ultimatecalloutchallenge/, /myprishow/, /dieselpowerproducts/, /elcoyotediesel/; posts /p/Df7xe9EAq4o/ (Rival Collab), /p/Df7ZijwApqo/, /p/Df5JE70gJTh/, /p/DfyQVlDmdmK/, /p/Dfd0H9KprRO/, /p/Dd4zf3UyQ2j/, /p/DfxwoQqEirs/, /73dipstick/reel/DfN1XQZNqkM/, /socalsupertrucks/p/DfxX-kPjckI/, /holders_diesel/reel/DemSHQwMYnd/, /veronica_cars/reel/DfcqRjJhrg7/
TikTok listings via yt-dlp (2026-11-21): @fassfuelsystems, @sbfilters, @fleeceperformance, @movebumpers, @dieselworldmag, @dieselsellerz, @dieselpowerproducts, @powerhungryperformance, @iidiesel, @dieseltrucking, @bddieselperformance, @hotshotsecret, @ppeituning, @dieselarmymagazine, @myprishow, @ultimatecalloutchallenge, @deraleperformance (private or empty: @isspro, @issproofficial, @axiom_supply, @bd_performancemanufacturing, @bankspower, @industrialinjection, @ppei_tuning, @hotshotssecret)
Account's own numbers: analysis/2026-11-21-live-pull-20-posts.md
Collabs: https://about.fb.com/news/2023/08/music-and-collabs-on-instagram/ ; https://skedsocial.com/blog/instagram-collaboration-feature ; https://buffer.com/resources/instagram-collab-post/ ; https://www.loomly.com/blog/instagram-collab-posts-how-to ; https://www.socialpilot.co/blog/instagram-collab-post ; https://www.makeinfluence.com/en/academy/instagrams-collab-tag-how-co-authored-posts-work-and-what-they-mean-for-reach-and-disclosure ; https://socialscheduler.ai/blog/instagram-insights ; https://www.inro.social/blog/instagram-dashboard-professional-dashboard-guide
Collab data: https://virev.ai/blog/instagram-algorithm (Oct 7, 2026, updated Oct 30) ; https://virev.ai/blog/use-instagram-s-paid-partnership-label-correctly ; https://www.sociavault.com/blog/instagram-paid-partnership-label-study
Reposts: https://about.instagram.com/blog/announcements/instagram-new-features-connect-friends/ ; https://www.socialmediatoday.com/news/instagram-adds-reposts-friends-feed-reels-friend-map/756996/ ; https://www.goodmorningamerica.com/living/story/new-instagram-map-repost-share-location-friends-124442765 ; https://petapixel.com/2026/04/30/new-instagram-policies-target-reposted-content/ ; https://www.zoomsphere.com/blog/instagram-algorithm-2026-what-actually-gets-reach ; https://kabo.sh/guides/instagram-ranking-2026 ; https://creatorlanehq.com/blog/instagram-algorithm-2026-mosseri-vs-measured (vendor)
Add Yours and templates: https://techcrunch.com/2022/08/16/meta-new-reels-features-instagram-and-facebook-including-add-yours-sticker ; https://techcrunch.com/2023/12/15/instagram-add-yours-template-story-sticker/ ; https://planoly.webflow.io/blog/instagram-reels-templates ; https://socialbee.com/blog/instagram-updates/ (secondary log) ; https://www.shopify.com/il/blog/instagram-stickers
Partner programs and contacts: https://us.bddiesel.com/pages/collab ; https://theshopmag.com/news/hot-shots-secret-secret-society-influencer-program/ ; https://industrialinjection.com/pages/sponsorship (404 on 11-21) ; https://industrialinjection.com/blogs/news/industrial-injection-800hp-cummins-laytona-250 ; https://www.sema.org/news-media/enews/2023/27/fln-member-spotlight-jake-hopkins-fass-diesel-fuel-systems ; https://www.dieselworldmag.com/features/influencer-insider-fass ; https://www.zoominfo.com/c/move-bumpers/414900966 ; https://hudsonintegrated.com/case-studies/move-bumpers ; https://dieselpowerproducts.com/pages/video/diesel-talk-founder-of-axiom-supply-co-breaks-down-products ; https://www.facebook.com/cncfabricationllc/ ; https://cncfab.us/pages/contact ; https://www.dieselworldmag.com/diesel-rides/readers-rides-real-diesel-builds-from-around-the-world/ ; https://www.dieselworldmag.com/uncategorized/diesel-enthusiasts-share-your-custom-rigs/ ; https://www.dieselarmy.com/?p=198344 ; https://official.bankspower.com/insider_news/review-us-please/ ; https://sites.sema.org/ext-assets/media/25_PR_PRI_Fact_Sheet_Final.pdf ; https://raceirp.com/races/ultimatecalloutchallenge/
FTC: https://www.upgrow.com/blog/ftc-influencer-rules-2026-instagram-summary ; https://www.celavii.com/blog/industry/ftc-influencer-disclosure-rules-2026 ; https://marketer.law/knowledge/ftc-influencer-affiliate-disclosure
House files: research/2026-11-21-build-series-structure.md (section 3, 5.5) ; research/reel-references/2026-11-21-diesel-niche-winners/BREAKDOWN.md (section 2, clips 05, 07, 10) ; research/FONT-LIBRARY.md ; playbook/00-content-plan.md
