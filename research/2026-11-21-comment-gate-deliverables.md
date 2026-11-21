# Comment-gated lead magnets for @elcoyotediesel (2026-11-21)

Research agent sweep run 2026-11-21 for @elcoyotediesel (577 followers, Creator account, Project Rival, parts manager at a Class 8 shop, owner of the 6.7 F350 "Chief"). Question: how do the accounts that run "comment WORD and I'll DM you X" well structure the reel, the keyword, the deliverable and the DM, what does Meta's free native tool actually do as of November 2026, and what should El Coyote's own six deliverables look like.

House rules this file obeys: a comment gate only with a real deliverable, at most one post in four, no follow gate, Meta Business Suite native Comment to Message (15-minute delay, 5 exact keywords) or ManyChat Free (25 active contacts a month). No on-screen call to action burned into the footage, per Jacob's 2026-11-21 rule; the keyword lives in the spoken last line, the caption's first line and the pinned comment.

Read with: `2026-11-21-live-instagram-algorithm.md` section 3 (the DM engine findings), `reel-references/2026-11-21-nxtlvl-profile/DOSSIER.md` section 4 (their keyword system, and the keyword reels they shipped with no DM behind them), `2026-11-21-share-engineering.md` section 5 (the ten send rules; this file does not repeat them).

Method and access caveats: web search engines do not index Instagram captions, Instagram's profile JSON endpoint returned 429 to the fetcher, and yt-dlp cannot list an Instagram profile. Two things do work: yt-dlp reads a single public Instagram reel without login (likes, comment count, caption), and a logged-out profile page fetched with a crawler user agent returns the caption start of the newest 12 grid tiles as image alt text (no shortcodes, no counts). Every Instagram number below marked "verified" came from the first route; the Instagram half of the niche sweep (section 1a) came from the second. TikTok creator pages list fine through yt-dlp with counts, so the other half of the sweep is TikTok captions. Meta's own Business Help Center pages would not load; the native-tool facts come from six independent setup guides dated June to November 2026 plus two Meta developer pages that did load (private replies, rate limits). Where guides disagree the disagreement is shown, not resolved.

---

## 0. The short version

1. **Nobody in the diesel and truck niche is doing this.** Across 61 TikTok accounts and about 1,900 of their most recent posts, plus 36 Instagram accounts and their newest 421 grid captions (truck, diesel, detailing, farm, fab, tool brands, parts retailers, from @throtl at 946K to @dom_obs7.3 at 12K), the sweep found zero "comment WORD" gates. The control account (@nocodealex, AI tools) showed six gates in its newest twelve posts through the same method, so the detector works. The niche's call to action is "link in bio" or "DM us for a quote." The comment-keyword lead magnet is an Instagram-side tactic that lives in the AI-tools, coaching and creator-education niches. For El Coyote that is both the risk (the audience has not been trained to type a keyword) and the opening (nobody in diesel hands a real file to a stranger's DMs).
2. **Where it works, three things are always true:** the deliverable is specific and already exists before the reel goes out, the reel shows the deliverable on screen before asking, and the keyword is one plain uppercase word that names the thing (REPO, WATCH, GUIDE, CHECKLIST). The study reel (@ai.nxtlvl, "Comment REPO") pulled 9,185 comments on 7,259 likes; the account it copied (@nocodealex, "Comment WATCH") pulled 1,536 comments on 1,176 likes (verified today). Comments above likes is what a working gate looks like, and it is a lead list, not love.
3. **The native Meta tool is enough for this account, with one adjustment.** Business Suite desktop, Inbox, Automations, Comment to message: free, no contact cap, 5 exact-match case-sensitive keywords per automation (one guide says 10), one text DM with a typed URL, 15-minute delay unless Jacob replies first, no per-post targeting, no analytics. At 200 to 500 views a reel the comment volume is 5 to 25 people, so for the first two gated reels Jacob should send the DM by hand with an in-app Saved Reply (instant, no delay, no tool) and switch the native automation on as the backstop for hours he is at the counter. ManyChat Free (25 active contacts a month, specific-post trigger only on Free) is only worth adding if the 15-minute delay measurably costs deliveries.
4. **Meta's Spam policy, by the letter, bans requiring "any other public-facing form of engagement" to get "exclusive content."** The fix is structural, not cosmetic: the file is never exclusive. Every deliverable also lives at a public URL on elcoyotediesel.com; the comment buys convenience (it lands in your DMs), not access. That also removes the follow-gate temptation entirely.
5. **Six deliverables, ranked by value:** the Rival parts list with partner tags (RIVAL, buildable today from `site/parts.json`), the 6.7 FASS install checklist (FASS, the pickup lane, the "disable instead of swap" angle nobody covers), the "don't buy this" return-rate sheet from the counter (RETURNS, the most shareable thing only Jacob can publish), the 7.3 torque card (TORQUE, cheapest, evergreen saves), the Super Duty frame-swap checklist (FRAME, when the donor arrives), and the SEMA 2027 reveal waitlist (SEMA, built now, promoted in 2027). Specs in section 4.

---

## 1. What the field does

### 1a. The niche sweep (TikTok captions, pulled today with yt-dlp)

Two passes, `--flat-playlist`, 40 to 60 most recent posts per account, captions grepped for "comment" followed by an uppercase word, "DM you/me/us," "I'll send," "storefront."

| pass | accounts (posts read) | comment-keyword gates found |
|---|---|---|
| 1, creators | dieselpowerproducts, whitefaceford, throtl, barntalk, desertdieselscartel, dom_obs7.3, skatin_6.7, rust_ridge_ranch26, royaltyautoservice, thedetailgeek, wilsonautodetailing, pandetailing, torquetestchannel, fabrats, trailrecon, millennialfarmer, cleetusmcfarland, donutmedia, vcgconstruction, electricianu, dsdiesel20, powerstrokerescue, thatdieselguy, dieselcreek (about 1,150 posts) | **0** |
| 2, retailers, brands, educators | 1aauto, lmr, fitmentindustries, summitracing, americantrucks, extremeterrain, realtruck, bulletproofdiesel, sinisterdiesel, bankspower, xtremediesel, thoroughbreddiesel, dieselpowergear, heavydsparks, mattsoffroadrecovery, milwaukeetool, harborfreight, chemicalguys, adamspolishes, meguiars, ammonyc, colethecornstar, welkerfarmsinc, humblemechanic, scottykilmer, thecarcarenut, southmainauto, ratchetsandwrenches, sbfilters, dieselworldmag, fullsenddiesel, carthrottle, hoonigan (about 770 posts) | **0** |

| 3, Instagram grid captions (newest 12 per account, logged-out profile page, crawler user agent) | whitefaceford (177K), throtl (946K), summitracing (631K), fitmentindustries (470K), adamspolishes (448K), ammonyc (432K), bankspower (330K), fassfuelsystems (291K), mattsoffroadrecovery (288K), dieselpowerproducts (200K), realtruck (177K), trailrecon (173K), humblemechanic (167K), sinisterdiesel (124K), extremeterrain (122K), sbfilters (90K), fabrats (84K), dieselworldmag (80K), americantrucks (58K), dieselcreek (54K), vcgconstruction (52K), hoonigan, dieselpowermag (30K), 1aauto (20K), torquetestchannel (17K), dom_obs7.3 (12K), plus milwaukeetool (2M), donutmedia (2M), chemicalguys (1M), harborfreight (884K) and a few small or mis-resolved handles (421 captions) | **0** (control: @nocodealex, 6 gates in 12: TUBE, ECC, DAILY, INTERVIEW, CITE, HARVEY, every one "and I'll DM you the link," four with "Follow so the DM lands") |

What the captions do instead: "Link in bio" (throtl, electricianu on every product post; 5 of the 421 Instagram captions), "DM us or email" (desertdieselscartel, 1,935 views, 2 comments), "drop a comment of your state" (whitefaceford, 59,600 views, 222 comments), "comment below what we should give away" (sinisterdiesel, 41,800 views, 50 comments), one discount code. Handles that failed to list on TikTok (dirtdiesels, obsfordnation, brickhouseautos, dieseltechron, westengarage, laura.farms) need a video URL instead of a profile URL; on Instagram, bulletproofdiesel, bddiesel, industrialinjection, dieselbrothers, thedetailgeek, pan_the_organizer and westengarage did not resolve under the handles tried.

Read on it: the truck audience knows "DM for a quote" and "comment your opinion." It has not been taught "comment a word, get a file." The first gated reel has to teach the mechanic in the reel itself (show the DM arriving), and the pinned comment has to say where the DM lands (Requests folder for non-followers).

### 1b. Examples table

Fourteen examples. The first six are the closest the automotive and trades niche gets; the rest are the gated reels that actually work, from adjacent niches, included because the structure is the lesson. Counts marked "verified" were pulled today; the rest are from the source named.

| # | account, niche | the ask (keyword) | deliverable promised | reel format | counts | source |
|---|---|---|---|---|---|---|
| 1 | 4 Wheel Parts, Jeep/off-road retailer (TikTok) | DM "Parts" | help planning upgrades (a sales conversation, no file) | diesel Jeep build walk-around with the parts named in the caption (AccuAir 3.5" air suspension, Fuel 20x12, Arctic steering kit) | discover page updated 2026-11-02, counts not shown | tiktok.com/discover/how-to-fix-your-jeep-in-diesel-n-steel-suspension |
| 2 | Cosmos Truck Accessories, lift shop (TikTok) | "DM on Instagram if you need parts and installation" | parts and install quote | before/after 2019 Sierra 2500, build sheet in the caption (5" Zone lift, 37x12.50R20 Toyo RT, 20" Fuel Covert) | 56,700 views, 2,156 likes, 31 comments, 87 shares, 70 s, 2025-03-02 (verified) | tiktok.com/@cosmos.truckaccessories/video/7477038927275134251 |
| 3 | STW_autosport, wheel and lift shop (TikTok) | "DM for a quote" | quote | Silverado on 544 wheels, 12" lift, static reveal | 291.7K likes, 1,463 comments (search snippet) | tiktok.com/discover page via search |
| 4 | Onsite Detail, mobile detailer (Instagram bio) | DM "DETAIL" | free quote | bio keyword, not a reel | n/a | instagram.com/onsitedetail |
| 5 | dieselpowerproducts (TikTok) | spoken "comment down below if your truck could do this" | nothing (engagement ask) | react clip, Ford tows a semi in snow | 65,600 plays, 308 shares, 0.47% sends | share-engineering file row 25 |
| 6 | Blowing Diesel, OBS 7.3 YouTuber | discount code in the description ("BD10 at archoil.com," "OBS10 at Auxbeam") | 10% off | install videos, code ungated in the description | 2,000 to 14,000 views each, 2020 to 2022 | yt-dlp description sweep today |
| 7 | @ai.nxtlvl, AI tools (Instagram) | "Comment REPO and I'll DM you all 9 links" | nine GitHub links | 52 s faceless card list, HUD counter 0/9, fake comment box + DM preview at the end | 7,259 likes, **9,185 comments**, 2026-11-04 | DOSSIER.md; reel.info.json |
| 8 | @ai.nxtlvl | "Comment TRADE and I'll DM you all 11 skills" | skills pack | 46 s list reel | **126,000+ plays, "85x my usual"** | DOSSIER.md section 2 |
| 9 | @ai.nxtlvl | JARVIS, WATCH, CLIPS | one repo link, one skill link, a 3-step workflow | 30 to 46 s single-reveal reels | not published; several shipped with **no DM behind them** (their own open-items log) | DOSSIER.md section 4 |
| 10 | @nocodealex, AI tools (Instagram) | "Comment WATCH and I'll DM you the repo link, free. Follow so the DM lands" | one GitHub link | 52 s paper-craft explainer, proof banner on every beat | 1,176 likes, **1,536 comments**, 2026-09-24 (verified today) | instagram.com/reel/DdrpcQ2zcuq |
| 11 | @creators.100x (nxtlvl's lead-magnet page) | HOOK, STUDY, PROMPT, CHECK, SCRIPT | 6 to 10 page 4:5 PDFs built from JSON | list reels | not published | DOSSIER.md section 4 |
| 12 | Buffer's writer (about 3,000 followers, career niche) | "comment GUIDE and I'll send it to your DMs" | a Notion database of remote-work resources; a CV template | talking head and text reels | "roughly half" of her 3,000 followers attributed to DM automation | buffer.com/resources/instagram-dm-automation |
| 13 | Amy Porterfield (courses) | comment trigger for a masterclass | registration link | talking head | 85% of commenters registered vs her 30 to 40% landing-page norm (ManyChat-attributed) | manychat.com blog via search |
| 14 | Brock Johnson (educator) | keyword in a text-heavy Story or reel | event ticket link, sent "within seconds" | Story with one line of text and a keyword | vendor claim "$100k a month," unverified | manychat.com/meet-brockjohnson |

Supporting numbers: a HypeAuditor and ManyChat study (vendor-linked) says micro creators running comment automation averaged 46 comments a post against 18 without. ReplyRush (vendor) cites Instagram DM open rates of 85 to 90%, link taps at 40 to 65% of DM openers, and email capture at 15 to 35% of triggers. Treat all three as directional; none publishes a method.

### 1c. Which deliverables work in this niche

No truck creator publishes comment-gate results, so this ranking is built from four things: the share-engineering data (what truck viewers already send), the vendor consensus on lead-magnet formats, what Jacob can produce from his own records, and the Nov 16 Amazon-links change.

| deliverable | evidence for | evidence against | verdict |
|---|---|---|---|
| **Parts list / build sheet** | Cosmos put the build sheet in the caption and got 87 shares on 56k; zac.lucarz "This got expensive quick" (cost reveal, no gate) did 112,400 views, 12,500 likes, 139 shares; nxtlvl's whole engine is "the list of things in the video, as links" | the list in the caption already earns saves without a gate (nxtlvl's own audit: "saves come from lists written out in the caption") | **Yes.** Put a partial list in the caption for saves, gate the full file with part numbers and partner links |
| **Build budget** | "what it cost" is the most-sent utility trigger in the share data (price reveal, format 7); zac.lucarz above | public dollar figures on Rival expose partner pricing; the F600 trans detail is private | Yes as ranges and categories, not line items. Fold into the parts list as a "what it costs" column with ranges |
| **Torque spec sheet** | checklists "have higher saves and repeat visits than most formats" (ReplyRush); a 7.3 guy needs the same 14 numbers every time he opens the valve covers | low novelty; the numbers exist in forums | **Yes, cheap.** The value is one phone-sized card, not the information |
| **Wiring diagram** | the Ahlbilt standalone harness and the 1959 dash on a 7.3 PCM is a real problem for swap guys | Jacob does not own the diagram; redrawing a vendor's diagram is their IP | Not as a deliverable. A one-page "what plugs into what" pin list for the 7.3 swap can live inside the FRAME checklist |
| **Tool list / Amazon storefront** | Instagram added Amazon affiliate links inside Reels on Nov 16, 2026 (US, Amazon Influencer account connected, "Add products," 30 per Reel per secondary reports, Instagram takes nothing); the Milwaukee FOUR FLAT list already exists in memory | Amazon Influencer approval is informal below about 1,000 followers (no published minimum, practically near 1k); a storefront link is a weaker reason to comment than a file | Do not gate it. Tag the tools in the Reel with product links once the Amazon account connects, and keep the gate for files |
| **Discount / partner code** | the standard ecommerce DM (ReplyRush "SHOP20," Creatorflow "Comment VIP") | a code alone reads as an ad, and sponsor reels on this account run 1.36% ER against 14.8% for personal | Only as the last line inside a real file ("Driven Diesel: code X on the regulated return kit"), never as the deliverable itself |
| **PDF vs Google Sheet vs Notion** | PDF: phone-readable, no login, 25 MB attachment limit through the API (Creatorflow), prefer a link so the file can be updated without resending; Google Sheet: live, updatable, right for anything with counts that change (the returns sheet); Notion: flagged for login prompts and slow loads on phones (UnlockDM) | Google Drive sharing breaks when files move folders (Creatorflow's weekly logged-out check) | **PDF on elcoyotediesel.com for static files, a published Google Sheet (view-only, "publish to web") for the returns sheet, with a PDF snapshot for the DM** |

Two cautions that belong here. First, the only measured platform penalty on comment gates is LinkedIn's: MagicPost's 1,983-creator sample shows "Comment KEYWORD" posts falling from +10% to about half their authors' average impressions from the week of July 27, 2026 (vendor data, correlation). Instagram has not done this, but Mosseri called the tactic "a little bit of an engagement hack" (secondhand) and Meta's Recommendations guidelines name "Comment YES and see what happens" as engagement bait. One in four is the right ceiling. Second, a gated reel's comments-to-sends ratio is the ugliest ratio on the account by design; the prior file's verdict stands: keep sends per reach above 1% on gated reels too, or the gate is buying comments with reach.

---

## 2. Meta Business Suite Comment to Message, November 2026

### 2a. Setup checklist (desktop only)

1. Open business.facebook.com on a computer (keyword and comment automations are not in the mobile app; Meta's wording per Creatorflow: "only available on the Meta Business Suite desktop experience at this time"). The Instagram professional account must be connected to a Facebook Page in the same business portfolio.
2. Left menu: **Inbox**, then **Automations**, then **Create automation**, then choose **Comment to message** (CXWizard's direct template link uses `automation_template=comment_to_inbox_v2`). Meta's description of the template: "Send a message reply to comments on your posts that contain specific keywords or phrases."
3. Name it after the deliverable ("Comment to message, RIVAL parts list"). Leave the status toggle **Off** while drafting.
4. **Channels:** tick **Instagram**. Messenger optional. If Instagram is not ticked the automation runs only on the Facebook Page.
5. **When this happens:** add the keywords. Most guides (Planoly, Creatorflow, Getkanal, Reachlee, Messengerbot): **up to 5 keywords or phrases, case-sensitive, exact match**, and a keyword can live in only one automation. CXWizard (Nov 2026) says up to 10. Spend the slots on case variants of ONE word: `RIVAL`, `Rival`, `rival`, `RIVAL.`, `Rival!`. Do not spend them on a second deliverable.
6. **Take this action:** optional public comment reply (write it: "Sent. If you don't follow me it lands in Message Requests."), then the private message. Composer: text, a first-name variable, "often up to 1000 characters" (CXWizard), image attachment allowed per CXWizard; Reachlee (Facebook side) says one fixed text reply with a typed URL, no buttons, no tracked link. Paste the full `https://` URL into the text; the DM also auto-includes a link back to the post (Meta private-replies doc).
7. **Save changes**, toggle **On**.
8. **Test from a second account** on a real reel: comment the keyword, wait the full 15 minutes, confirm the DM arrives and where (Inbox for followers, Requests for non-followers), confirm the link opens logged out. Heyy.to (one dissenting guide) claims Instagram keyword comment-to-DM is "limited or absent" in Business Suite; every other 2026 guide says it works. The test settles it for this account in 20 minutes.
9. Pin a comment under the reel before anything else: the keyword, the 15-minute note, the Requests-folder note, and the public URL.

### 2b. Limits and behavior

| item | what the sources say | source quality |
|---|---|---|
| Delay | "sends after 15 minutes unless you personally respond before then"; stated for keyword automations and applied to Comment to message by Creatorflow, Planoly, Reachlee; no setting shortens it | 3 guides quoting Meta help text |
| Post targeting | page-wide, every post and reel; no per-post or "next post" option; cannot act on comments posted before setup | Reachlee (Facebook side); not contradicted |
| Reels | Meta's rate-limit page covers "private replies to comments on Instagram posts and reels," so Reels comments are in scope | Meta developer docs (fetched) |
| One DM per comment | "Only one message can be sent to the Instagram user who commented," within 7 days of the comment | Meta private-replies doc (fetched) |
| Where it lands | Inbox if the commenter follows the account, otherwise the Request folder | Meta private-replies doc (fetched) |
| Continuing the thread | only if the person replies; then the standard 24-hour window applies and reopens on each reply | Meta private-replies doc; Creatorflow; Spur |
| Rate limit | 750 private replies per hour per Instagram professional account; Send API 100 calls per second for text and links; per account, not per tool | Meta rate-limit page (fetched) |
| Priority | a matching template automation (away message, instant reply) beats the keyword reply; turning on Meta Business Agent pauses existing automations | Creatorflow, Getkanal |
| Analytics | none; no delivery count, no click count | Reachlee, Creatorflow |
| Regions | some organic messaging features unavailable for Europe and Japan (not relevant here) | Meta notice quoted by Getkanal |
| In-app alternatives | FAQs (4 questions), Saved Replies (shortcut text, manual send, no cap), Instant Reply, Away Message, AI Auto Replies rolling out | Creatorflow |

### 2c. How the 15-minute delay affects comment velocity, and what to do about it

What happens: a viewer comments RIVAL at second 40 of the reel, keeps scrolling, and 15 minutes later a message lands in Requests (non-follower) with no notification badge they will notice. Vendors sell "within 5 seconds" because the commenter is still on the post; Reachlee's own line for moving to a paid tool is "replies must arrive while the commenter is still on the post." The delay does not reduce how many people comment; it reduces how many open the DM, and it removes the live proof ("just got it, thanks") that pulls the next commenter in.

Mitigations, in order:

1. **Send by hand for the first two gated reels.** At 200 to 500 views and a 2 to 5% keyword rate that is 5 to 25 DMs. Save the DM text as an in-app Saved Reply (long-press a sent message, More, Save, give it the shortcut "rival"), then reply to each comment publicly and send the DM from the commenter's profile. Instant, no tool, no delay, and Jacob sees who they are. The API cannot initiate DMs but Jacob's thumbs can.
2. **Native automation on as the backstop** for the hours he is at the counter. One unknown to test: whether Jacob's public comment reply counts as "personally responding" and cancels the automated DM. If it does, reply publicly only after the DM has gone out.
3. **Pinned comment does the velocity work:** "Comment RIVAL, the list lands in your DMs in about 15 minutes (Message Requests if you don't follow me). Or grab it here: elcoyotediesel.com/..." The public URL is also the Spam-policy fix (section 2e).
4. **Post the gated reel at 16:00 to 19:00 Mountain** (the account's best window) on a day Jacob can sit with the phone for the first hour. Brock Johnson's posting routine (reply to everything in the first hour) applies doubly to a gated reel.

### 2d. ManyChat Free, as of November 2026

- $0, no card. **25 active contacts a month** since the March 2, 2026 billing change (was 1,000). A contact counts once per billing month when an automation messages them. Notifications at 70, 90 and 100%; behavior at contact 26 on Free is undocumented, treat 25 as a hard ceiling.
- 4 live automations, 2 channels (Instagram plus one), 1 seat, "Powered by Manychat" line in the DM.
- Instagram comment-to-DM is included, **but on Free the trigger is a specific post only**; "any post" and "next post" need Pro (Chatimize, confirmed by its author in comments). Collecting a reply (name, email) also needs Pro. So Free gives: one reel, one keyword, one instant DM with a button or link, up to 25 people a month.
- Essential $17 a month ($14 annual), 250 contacts, $0.10 per extra contact. Pro $39 ($29), 2,500 contacts, unlocks input collection and broadcasts.
- Math for this account: at 500 views and a 3% keyword rate, one gated reel uses 15 of 25 contacts. Two gated reels a month fits; the third does not. The native tool has no contact cap. ManyChat earns its place only if the instant DM measurably beats the 15-minute DM on deliveries, which the first two hand-sent reels will show.

### 2e. Instagram's rules for the automated DM

- **Trigger must be the person's own action.** Comment, Story reply or DM keyword. No cold DMs, no scraped lists, no password-based tools (the ban tier). Meta's private reply is one message per comment within 7 days; everything after that needs the person to reply, inside 24 hours of their last message (Meta developer docs). The HUMAN_AGENT 7-day tag is for people, not bots.
- **Meta Spam policy, current text (transparency.meta.com):** prohibits "Requiring users to engage (in the form of likes, shares, follows, or any other public-facing form of engagement) to gain access to specific, exclusive content" and "Requiring or claiming that users are required to engage with content (e.g., liking, sharing) before they are able to view or interact with promised content." A follow gate is named outright. A comment is "public-facing engagement" too. The design answer: **the content is never exclusive.** Every file sits at a public URL that the pinned comment and the bio carry; the comment is a delivery method. That is also why ManyChat's "ask to follow" step stays off even though vendors say it is "allowed if disclosed."
- **Recommendations guidelines (via FYProof, Oct 2026):** engagement bait ("posts that explicitly request engagement," example "Comment YES and see what happens") can keep a post out of recommendations. A keyword tied to a named deliverable is not the example given, but a reel whose only content is the ask is. The deliverable has to be visible in the reel.
- **Opt-in and opt-out:** Meta App Review requires "a documented opt-out mechanism reachable from inside the DM conversation" (Creatorflow). For a one-message private reply there is nothing to opt out of; if Jacob ever follows up, the follow-up has to be a reply to their reply.
- **Email capture:** Meta stopped creating phone and email quick replies on October 5, 2026 (Creatorflow, single source). Email collection by DM now means a typed reply (ManyChat Pro) or a form on the portal. For the SEMA waitlist that means a portal form, not a DM field.
- **AI labels:** irrelevant to the DM; relevant to the reel if a synthetic voice is used (it should not be).

### 2f. Decision rule for @elcoyotediesel

Hand-sent Saved Reply for gated reels 1 and 2, native Comment to message switched on as the backstop from reel 1, ManyChat Free only if a third gated reel in a month is planned and the delay has shown a cost. Never a follow gate. Public URL on every file. One gated reel in four, so at 3 to 4 reels a week that is one gated reel every 10 to 14 days.

---

## 3. What a good trades lead magnet looks like

Pulled from the vendor guides that agree with each other (Creatorflow, UnlockDM, ReplyRush, Claimful, Webby) and from the nxtlvl PDF spec, then filtered through what a diesel owner opens on a phone in a parking lot.

1. **One outcome, named in the title, for one named person.** UnlockDM's frame: "For [specific person], a [one-page format] that solves [urgent problem]." Not "7.3 Powerstroke guide." Instead "7.3 torque card: the 14 numbers you need with the valve covers off."
2. **Readable in under a minute, usable in under fifteen.** Checklists and single templates beat guides; a "focused 7-page guide consistently outperforms a 40-page guide" (ReplyRush); "Fifty pages is a weekend project" (Creatorflow). Cap at 8 pages.
3. **Portrait, phone-first.** 4:5 at 1080 x 1350 (the nxtlvl spec: cover, rules page, card pages, checklist) or 9:16; single column; 16 px minimum body type; one idea per page; white space. Landscape PDFs lose.
4. **Branded, lightly.** The El Coyote lockup on the cover and a footer line with the handle and the URL on every page, so a screenshot of page 3 still says where it came from. Palette and type from `FONT-LIBRARY.md`; no gradients, no sheen, flat color.
5. **A reason to save, not just read.** A blank column the reader fills in (their own torque wrench setting, their part numbers, their date), a checkbox list, or a number that changes (the returns sheet). Checklists "have higher saves and repeat visits than most formats."
6. **Proof inside the file.** A photo of the real part on Jacob's bench, a screenshot of the actual return record (vendor name blurred if needed), the real binder page. The nxtlvl rule "never show real handles in fake UI" runs the other way here: everything in the file is real.
7. **The next step is a door, not a push.** Last page only. Three lines maximum: the live version on elcoyotediesel.com, the partner who makes the part (with their code if one exists), and one question that invites a reply ("What truck is this going on? Reply and I'll tell you if the number changes."). The reply reopens the 24-hour window and moves the thread into the main inbox. No "buy," no "book a call," no countdown.
8. **Hosted where Jacob controls the link.** `elcoyotediesel.com/files/<name>.pdf` on the rival-build Vercel project. The file can be replaced without changing the link, the link never asks for a login, and a redirect path (`/r/rival`) gives a tap count from the Vercel logs, which the native tool does not provide. Google Drive is the fallback, with Creatorflow's weekly logged-out check.
9. **The DM is the link plus three lines.** nxtlvl's rule: "only the resource link and its setup steps, nothing else: no greeting, buttons, comment replies, follow line or caveats." ReplyRush: under 60 words, link first because the person has already waited, one closing question. Builder voice, no exclamation marks, no emoji.
10. **The reel shows the file.** Every working gated reel in section 1b puts the deliverable on screen before the ask (the binder, the card, the sheet, the DM preview). For El Coyote that is footage of the real thing in Jacob's hand, not a mock-up.

---

## 4. Six El Coyote deliverables, ranked by value

Value = how much a diesel owner wants it x how much only Jacob can credibly make it x how cleanly it leads somewhere (portal, partner, waitlist). Effort is one evening unless noted. All files: 4:5 PDF, 1080 x 1350, El Coyote lockup, footer with @elcoyotediesel and the URL on every page, hosted on elcoyotediesel.com, public link in the pinned comment. Reel rules from the share-engineering file apply (identity marker on frame one, 30 to 60 s for utility, hard cut inside 1.5 s of the payoff); the keyword is spoken once in the last line and sits in the caption's first line and the pinned comment. Test a 1-second end frame with the keyword as a Trial Reel variant against the clean cut and keep whichever earns more keyword comments per reach without dropping sends below 1%.

### 4.1 The Rival parts list with partner tags

- **Keyword:** RIVAL (native slots: RIVAL, Rival, rival, RIVAL., Rival!)
- **Why first:** it already exists (`F600-BUILD/site/parts.json` drives `build-list.html` on the portal), it is the sponsor deliverable partners.html promises ("one part sells ten more" needs the list in strangers' hands), and it sends people to elcoyotediesel.com, which is where every Rival conversation should land.
- **The reel that earns it (30 to 40 s):**
  - Frame one: the printed binder open on the 7.3 on the stand, Jacob's hand on it, 1959 grille or the Wyoming plate in the background. Spoken, mid-story: "Every part going on this truck is in here. Part numbers, who makes it, who stepped up."
  - 3 to 20 s: nine fast cuts, one real part per cut, each held 1.5 to 2 s, the binder page for that part in the same shot where possible: Driven Diesel fuel system, Power Hungry Hydra chip, ISSPRO gauges, BD Diesel manifolds, Mishimoto radiator and intercooler, DieselSite HPOP, Choate valve covers, ARP studs, the Super Duty frame (or the donor hunt photo). Spoken: the part name and one number per part (psi, hp, lbs, cc). No prices.
  - 20 to 30 s: Jacob flips to the last page: the partner column. "The ones with a logo next to them are partners. The rest I bought."
  - Last 3 s: binder closes on the hood, thump, spoken over the thump: "Comment RIVAL and it's in your DMs." Cut on the word DMs.
  - Caption first line: "Comment RIVAL and I'll DM you the full Project Rival parts list, part numbers and partners included." Then the first nine parts written out (saves), five lowercase hashtags, one line of search phrases (1959 f600 restomod, 7.3 powerstroke compound turbos, obs 7.3 swap, road to sema 2027).
  - Pinned comment: "RIVAL gets you the PDF in about 15 minutes (Message Requests if we're not following each other). Live version, always current: elcoyotediesel.com/build-list.html"
- **The DM:**
  > Project Rival parts list: elcoyotediesel.com/r/rival
  > 1. Pages 2 to 7 are the build in order: engine, fuel, air, trans, chassis, interior.
  > 2. A logo in the right column means a partner; a blank means I paid for it.
  > 3. The live list updates as parts land: elcoyotediesel.com/build-list.html
  > What are you building? Reply and I'll tell you what carries over.
- **Format:** 8-page 4:5 PDF generated from `parts.json` (so it never drifts from the portal), plus the live page. Rebuild the PDF whenever `seedRev`-style data changes; the link stays the same.
- **Content outline:**
  1. Cover: lockup, "Project Rival, 1959 Ford F600, 7.3 Powerstroke, Road to SEMA 2027," the truck photo, date of this version.
  2. How to read this: the columns (part, spec, maker, part number where public, status: decided / partner / in talks), the rule that every decided part is a baseline and can change when a partner steps up.
  3. Engine: block and machine work, rotating assembly, cam and valvetrain, heads and gaskets, ARP hardware, oiling package, HPOP, injectors (status, no pricing).
  4. Fuel and air: Driven Diesel fuel path (partner), compound turbo plan, manifolds and up-pipes, intercooler, radiator, exhaust.
  5. Tuning and monitoring: Power Hungry Hydra chip (partner), ISSPRO gauges (partner), standalone harness, PCM.
  6. Driveline and chassis: 2WD, Super Duty 2005-2007 frame, dead-axle Dana 60, SRW Sterling 10.5, transmission as published in STATUS.md (no builder, no pricing), driveshafts, air ride 4-link, shocks, wheels and tires direction, brakes and hydroboost.
  7. Body and interior: express bed, cab, dash and gauges, climate, seats, leather, audio (directions, not vendors' prices).
  8. Partners and the door: partner logos with one line each and codes where a partner provides one; "want your part on this list" line pointing at partners.html; the live URL; the reply question.
- **Private exclusions (hard rule):** transmission builder, pricing and part numbers; any vendor cost; anything from `notes/research/`; no Elite Diesel or 307 names anywhere in the file.
- **Next step it leads to:** the portal (build-list and partners pages), partner codes, replies that become sourcing conversations.

### 4.2 The 6.7 Powerstroke FASS install checklist

- **Keyword:** FASS (slots: FASS, Fass, fass, FASS., Fass!)
- **Why second:** pickup is the primary lane and this is the one pickup story Jacob owns outright: he disabled the CP4 and ran a FASS on his own 2011 F350 instead of the thousands-of-dollars CP3 or DCR conversion everyone else recommends, and the FASS does both jobs (clean, consistent fuel to the CP4 now, the volume for the power later). FASS is an existing relationship with no follower minimum, so the file is sponsor-adjacent without reading as an ad.
- **The reel that earns it (35 to 50 s):**
  - Frame one: Jacob under the F350, phone on the ground, FASS pump visible on the frame rail, hand on it. Spoken: "A guy told me there's zero reason to run a lift pump under 750 horsepower. This one's been feeding my CP4 for [real time] and it's already there for the power."
  - 4 to 15 s: three cuts: the pump and bracket on the rail, the draw straw / tank side, the wiring run to the ignition source. One sentence each, what it does.
  - 15 to 30 s: the part nobody covers, spoken plain: "I did not do a CP3 swap. I did not do a DCR. I disabled the CP4 failure path and put a FASS in front of it. Here is the order I did it in." Jacob holds up a one-page printed checklist, folded, grease on it.
  - 30 to 40 s: two mistakes he made or almost made (the real ones: the fitting, the filter he bought twice, the prime step), 4 s each.
  - Last 3 s: the key turns, the pump hums, Jacob: "Comment FASS and the checklist is in your DMs." Cut on the hum.
  - Caption first line: "Comment FASS and I'll DM you the one-page install checklist I used on my 2011 F350 6.7, CP4 disabled, no CP3 or DCR swap." Then the three mistakes written out.
  - Pinned comment: the keyword, the 15-minute and Requests note, the public URL.
- **The DM:**
  > 6.7 FASS install checklist (2011 to 2016 F350): elcoyotediesel.com/r/fass
  > 1. Page 1 is the order of operations with the torque and the prime step.
  > 2. Page 2 is the part numbers I used and the two I bought wrong.
  > 3. Page 3 is the CP4 disable, what it is and what it is not.
  > What year is your truck? Reply and I'll flag what changes.
- **Format:** 3 to 4 page 4:5 PDF; page 1 is a printable checkbox list (the reason to save).
- **Content outline (Jacob fills values from his own install and the FASS instruction sheet; nothing published that he did not do):**
  1. Cover: "6.7 Powerstroke FASS install, the one-page version," photo of the pump on his rail, truck year range it applies to, the one-line position: a FASS does both jobs.
  2. Order of operations, checkboxes: bracket and pump location on the rail; tank access and draw straw (or suction tube) install; supply and return line routing with clip points and heat-shield spots; filter orientation and part numbers (FASS water separator and fuel filter numbers he actually runs); wiring: battery power with the inline fuse, ground point, ignition-switched trigger; prime procedure (key cycles, what pressure he saw); leak check; first drive check; service interval he uses.
  3. Part numbers and the two mistakes: the kit number, the filters, the fittings, the bracket; "bought wrong" lines with what to buy instead.
  4. The CP4 disable, explained in six lines: what the failure path is, what the disable kit does, why this is cheaper than a CP3 or DCR conversion, what it does not do, when he would still convert. Ends with the rebuttal to the 750 hp comment.
  5. Door: FASS code if the relationship provides one, the Chief build list on the portal (or the Instagram highlight), the reply question. Harbor Freight and Hot Shot's Secret programs are noted in memory; do not stack brands in this file.
- **Next step it leads to:** FASS (the relationship), the F350 build content, replies that are pickup owners, which is the audience the account is supposed to be converting.

### 4.3 The "don't buy this" return-rate sheet from the parts counter

- **Keyword:** RETURNS (slots: RETURNS, Returns, returns, RETURNS., Returns!)
- **Why third:** it is the one thing nobody else in diesel can publish. Jacob orders the replacements and sees what comes back. "Don't buy this" is the account's own listed format and the most shareable utility trigger there is (a buddy about to buy the part). It ranks third, not first, because it needs data work, a legal read and the Class 8 framing, and because the counter serves semis: this is the semi slot, told as transfer knowledge for pickup owners.
- **Data source:** `Desktop\Parts Returns Tracker.xlsx` (the CREDIT workflow) reconciled against Fullbay "Returned to Vendor" records; units bought from the Parts Pricing Tool history (`Desktop\Parts Pricing Tool\parts_history.csv`). Return rate = returns divided by units bought, per part family, last 12 months, minimum 10 units bought so one bad box does not make a row.
- **Rules before publishing:** facts from Jacob's own records only; every row states the reason category (fitment, dead on arrival, failed in service, wrong application) because a fitment return is not a quality verdict; brand names only where the count is large enough to be fair, otherwise "aftermarket X vs OEM X"; no shop name, no customer, no VIN; Troy or Holly see it before it ships; no "junk" language, just the count and the swap Jacob made. This is observation, not drama, which is also the house rule for Fullbay findings.
- **The reel that earns it (30 to 45 s):**
  - Frame one: a returned part on the counter, the return tag on it, Jacob's hand turning it over. Spoken: "I order the parts for a semi shop. This is the one that comes back the most. You've got the same part family on your pickup."
  - 4 to 20 s: three return tags, three parts, one line each: what it is, how many went out, how many came back, why. Numbers spoken and visible on the tags.
  - 20 to 32 s: the transfer: "On a Class 8 that return costs a day of downtime. On your 6.7 it costs a tow. Here's what I run instead on mine," one cut to the part on the F350.
  - Last 3 s: Jacob drops the sheet on the counter: "Comment RETURNS. Twelve months, every part family, what came back." Cut on the drop.
  - Caption first line: "Comment RETURNS and I'll DM you the return-rate sheet from a diesel parts counter: 12 months, what comes back and why, and what I run on my own 6.7."
- **The DM:**
  > Parts counter return-rate sheet, last 12 months: elcoyotediesel.com/r/returns
  > 1. Rows are part families, sorted by return rate; the reason column matters more than the rate.
  > 2. The "on your pickup" column is the same part family on a 6.7 and what I run.
  > 3. The live sheet updates monthly at the same link.
  > Which part are you about to buy? Reply with it and I'll check the row.
- **Format:** published Google Sheet (view-only, "publish to web," no login) as the live version; a 2-page 4:5 PDF snapshot for the DM and the save. The sheet is the reason it keeps earning: the link is permanent and the numbers move.
- **Content outline:**
  1. Cover page (PDF): title, the month, the method in three lines (units, returns, reason categories, minimum sample), the honesty line ("fitment returns are my mistakes as often as the vendor's").
  2. The table: part family | units out | returns | rate | top reason | OEM or aftermarket | what I run on the F350 | note. Fifteen to twenty rows, red flat bar for anything over the shop's average rate, no color grade beyond that.
  3. Three short callouts at the bottom: the one with the worst in-service failure rate, the one where OEM was cheaper over 12 months once returns counted, the one where aftermarket beat OEM.
  4. Door: "monthly update at this link," the F350 build list, the reply question. No shop name, no vendor pitch.
- **Next step it leads to:** replies from people about to buy a part (the exact conversation the account's credibility is built on), monthly re-shares of the same link, and the first file a brand like FASS or S&B would want to be on the right side of.

### 4.4 The 7.3 Powerstroke torque card

- **Keyword:** TORQUE (slots: TORQUE, Torque, torque, TORQUE., Torque!)
- **Why fourth:** cheapest to make, highest save rate per effort, evergreen, and it rides the Rival engine assembly footage that Jacob is shooting anyway. Lower than the first three because the information is not scarce; the one-card format is the product.
- **Values policy:** every number comes from the Ford Workshop Manual for the 94-03 7.3 and the ARP instruction sheet for the kits on the Rival list, checked by Jacob against the sheet in his hand before publishing, with the source named on the card. Nothing published from memory or a forum. ARP values are "with ARP lube" and say so.
- **The reel that earns it (20 to 30 s):**
  - Frame one: torque wrench clicking on a head stud on the Rival 7.3, close, real sound. Spoken: "Every time I open this engine I look up the same fourteen numbers. So I put them on one card."
  - 3 to 15 s: four fasteners, four clicks, each with the number spoken and the wrench dial in frame: head studs, rocker bolts, valve cover, HPOP. Torque sequence pattern shown on the head for 2 s.
  - 15 to 24 s: the card itself, laminated, zip-tied to the engine stand; Jacob's finger runs down it.
  - Last 2 s: the fourteenth click: "Comment TORQUE, it's yours." Cut on the click.
  - Caption first line: "Comment TORQUE and I'll DM you the one-card 7.3 Powerstroke torque sheet, 14 fasteners, sequences included, manual and ARP sourced."
- **The DM:**
  > 7.3 Powerstroke torque card: elcoyotediesel.com/r/torque
  > 1. One page, phone size; save it to Photos, it reads offline.
  > 2. ARP numbers are with ARP lube, factory numbers are from the Ford manual, source is printed on the card.
  > 3. Page 2 is the head and main sequences.
  > Building a 7.3 or keeping one alive? Reply and I'll tell you which numbers change with studs.
- **Format:** 2-page 4:5 PDF plus a 1080 x 1350 PNG of page 1 (the image is what people save to Photos; attach it in the native composer if attachments work on the test).
- **Content outline:**
  1. Page 1, the card: fourteen rows, fastener | factory spec | ARP spec (where an ARP kit exists) | note. Rows: head bolts or studs (with the step sequence note), main caps (and the girdle note), rod bolts, rocker arm bolts, valve cover and UVCH, intake plenum, exhaust manifold, up-pipe flanges, turbo pedestal and turbo-to-pedestal, HPOP mounting and drive gear, injector hold-downs, glow plugs, oil pan, flexplate and damper. Footer: "Ford Workshop Manual 94-03 7.3L; ARP kit instructions; verified [date]." Blank column "my setting" for the reader.
  2. Page 2: head bolt and main cap tightening sequences as diagrams, a lube-and-thread-prep line, and the door: the Rival parts list link, the reply question.
- **Next step it leads to:** the RIVAL list (cross-sell inside the file), Rival engine assembly reels, and a deliverable that keeps getting requested in comments for years.

### 4.5 The Super Duty frame-swap checklist

- **Keyword:** FRAME (slots: FRAME, Frame, frame, FRAME., Frame!)
- **Why fifth:** it is Rival's core idea (a 1959 cab on a 2005-2007 Super Duty 4x4 frame, run 2WD) and the old-Ford crowd asks these questions constantly, but the audience is narrower than the first four and the checklist is only credible once the donor frame is in the shop and the first measurements are real. Schedule it for the week the donor arrives.
- **The reel that earns it (40 to 60 s):**
  - Frame one: the 1959 cab and the Super Duty frame side by side on the floor, Jacob walking between them. Spoken: "The body stays 1959. The frame does not. Here is what you keep off the donor, what you buy, and what I measured wrong."
  - 5 to 25 s: the donor walk: frame, dead-axle Dana 60 on the coil front, steering box and linkage, hydroboost and pedals, tank and lines: "keep." Transfer case, front driveshaft, front drive internals: "gone."
  - 25 to 45 s: the buys: SRW Sterling 10.5, 8x170 pattern, engine mount adapters, trans crossmember, driveshafts to length, air ride rear. Wheelbase set by the express bed, with the tape on the frame.
  - 45 to 55 s: the one thing he got wrong or almost did (the real one from the logs).
  - Last 3 s: clipboard on the frame rail: "Comment FRAME, the whole checklist." Cut.
  - Caption first line: "Comment FRAME and I'll DM you the checklist for putting an old Ford cab on a 2005 to 2007 Super Duty frame: what to keep, what to buy, what to measure first."
- **The DM:**
  > Super Duty frame swap checklist: elcoyotediesel.com/r/frame
  > 1. Page 1 is the donor spec and the keep / sell list.
  > 2. Page 2 is the measure-first list, in the order I wish I had done it.
  > 3. Page 3 is the buy list by category with the status on Rival.
  > What cab is going on yours? Reply and I'll tell you where the numbers differ.
- **Format:** 4 to 5 page 4:5 PDF with checkboxes; updated as the swap progresses (same link).
- **Content outline:**
  1. Cover and the decision in five lines: why 2WD, why this frame (the driveline was already Super Duty), what it costs in complexity versus a 1959 frame.
  2. Donor spec and shopping rules: 2005-2007 F250/F350 4x4 roller, straight frame, rear hangers, what a dead 6.0 donor is worth; keep list (frame, Dana 60 housing as a dead axle, steering, hydroboost, pedals, tank, brake lines); sell list.
  3. Measure first: wheelbase from the bed, cab mount positions, firewall-to-engine clearance for the 7.3 and the turbo, steering column path, fuel tank location, cooling package depth, ride height target (stock F600 height or a touch taller), tire clearance for a medium-duty look on singles.
  4. Buy list by category: rear axle, engine mounts (7.3 to 6.0-frame perches), transmission crossmember (per STATUS.md, no builder or pricing), driveshafts, rear 4-link air ride and shocks, brakes, wheels 8x170, harness (standalone), gauges.
  5. Paperwork and safety: title stays with the 1959 body, check the state's frame-swap and VIN rules before cutting, brake proportioning, steering stops, a note to have the fab checked. Door: the Rival parts list, the reply question.
- **Private exclusions:** transmission builder and pricing; shop names; donor seller details.

### 4.6 The SEMA 2027 reveal waitlist

- **Keyword:** SEMA (slots: SEMA, Sema, sema, SEMA., Sema!)
- **Why sixth now, first later:** the deliverable is a link, not a file, and the value peaks in the last six months before November 2 to 5, 2027. Build the page now (an evening), use it quietly in the DM door lines of the other five files, and run its own gated reel only when there is a truck on a frame to show. Gating a milestone reel (first fire, cab on the frame) would waste the account's most sendable moments; the SEMA reel is a separate, talking, plan reel.
- **Why a page and not a DM field:** Meta ended email quick replies on October 5, 2026 (Creatorflow, single source) and ManyChat input collection is Pro only, so the email lives on the portal. `site/api/` already exists in the rival-build project; a form that writes to a Vercel KV or Blob list, or a Formspree endpoint, is enough. Collect email and first name only; say what they get (reveal date, the unveil photos first, partner codes) and how often (monthly at most).
- **The reel that earns it (30 to 40 s, run in 2027 Q1 or later):**
  - Frame one: the truck as it sits that day, Jacob in frame. Spoken: "This truck is going to be in Las Vegas on November 2nd, 2027. Here's the next twelve months in forty seconds."
  - 4 to 30 s: the plan in cuts: long block, chassis, body and paint, interior, the bed, the partners, each 3 to 4 s with the real part or the real sketch.
  - 30 to 36 s: "The people on the list see the finished truck before the show floor does."
  - Last 3 s: "Comment SEMA." Cut.
  - Caption first line: "Comment SEMA and I'll DM you the link to see Project Rival finished before it hits the show floor, Nov 2 to 5, 2027, Las Vegas."
- **The DM:**
  > Project Rival SEMA 2027 list: elcoyotediesel.com/sema
  > 1. Name and email, nothing else.
  > 2. You get the finished truck the night before the floor opens, the partner codes, and nothing more than one email a month until then.
  > 3. The build log is live at elcoyotediesel.com if you want to watch it happen.
  > Will you be in Vegas that week? Reply and I'll let you know where the truck sits.
- **Format:** a portal page with a two-field form and a thank-you state; a 1-page 4:5 image of the plan timeline as the save object (optional).
- **Content outline (page):** headline with the date; the truck photo; three lines on what the list gets; the form; the partner logo bar; a "follow the build" link. No countdown widget, no sheen, flat red.
- **Next step it leads to:** an owned list for the reveal, the partners' launch assets, and the "we had N people on the list" line for partners.html.

### 4.7 Order of operations and calendar

| when | gated reel | needs first |
|---|---|---|
| week 1 | RIVAL | PDF built from parts.json, `/r/rival` redirect, pinned comment text, Saved Reply saved, native automation tested from a second account |
| week 3 | FASS | checklist written from Jacob's own install, part numbers checked, FASS code confirmed or omitted |
| week 5 | TORQUE | fourteen values verified against the manual and ARP sheets, card laminated for the reel |
| week 7 | RETURNS | 12-month pull from the returns tracker and Fullbay, owners' read, sheet published |
| donor week | FRAME | donor frame on the floor, first measurements real |
| 2027 Q1+ | SEMA | page live now, reel when the cab is on the frame |

Everything else between them is ungated: identity shots, sound reels, the glovebox part, the LS swap guy. One in four means roughly one gated reel every two weeks at the current cadence. Build the file before the reel is shot; nxtlvl's own log calls shipping keyword reels with nothing behind them their top blocker.

---

## 5. Measurement

Per gated reel, read at 48 hours:

| metric | how to read it | floor | goal |
|---|---|---|---|
| keyword comments / reach | count the keyword comments by hand, divide by reach in Insights | 2% | 5% |
| deliveries | hand-sent count plus the automation's (count DM threads opened that day; the native tool has no counter) | 90% of keyword comments | 100% |
| link taps | hits on `/r/<keyword>` in the Vercel logs | 40% of deliveries | 65% (ReplyRush's upper band) |
| replies to the DM | threads where the person wrote back (the 24-hour window reopened) | 10% | 25% |
| sends per reach on the gated reel | shares / reach in Insights | 1% | 2% |
| skip rate | `reels_skip_rate` | under 45% | under 40% |

If keyword comments are under 2% of reach, the reel did not show the deliverable well enough or the keyword was not clear; fix the reel, not the file. If deliveries lag comments, the 15-minute delay or the Requests folder is eating them; move to hand-sending or ManyChat Free. If sends per reach fall under 1% on gated reels while ungated reels hold, the gate is costing reach and the cadence drops to one in six.

---

## Sources (all fetched or pulled 2026-11-21 unless marked)

Primary and verified
- Meta developer docs, Instagram private replies (one message per comment, 7 days, Inbox vs Requests, 24-hour window on reply): https://developers.facebook.com/docs/messenger-platform/instagram/features/private-replies
- Meta developer docs, rate limits (750 private replies per hour per account; 100 calls per second text and links): https://developers.facebook.com/docs/graph-api/overview/rate-limiting
- Meta Community Standards, Spam (engagement-to-access wording): https://transparency.meta.com/policies/community-standards/spam/
- Instagram @creators, affiliate links Nov 16, 2026 (US, Amazon Influencer account, Professional dashboard > Monetization > Affiliate programs): https://creators.instagram.com/blog/more-ways-to-earn-affiliate-links
- @nocodealex reel DdrpcQ2zcuq, counts and caption via yt-dlp today: https://www.instagram.com/reel/DdrpcQ2zcuq/
- @ai.nxtlvl study reel and dossier: `reel-references/2026-11-21-nxtlvl-profile/DOSSIER.md`, `reel-references/2026-11-21-DfU2nIgt8XK/reel.info.json`
- TikTok sweeps (yt-dlp, 61 accounts): scratch files `tiktok_sweep.txt`, `tiktok_sweep2.txt`; Cosmos Truck Accessories 7477038927275134251 and zac.lucarz 7507779410884316446 pulled individually
- Own account data: `2026-11-21-share-engineering.md` (20-post table), CLAUDE.md

Native tool setup guides (third party, June to November 2026; Meta Business Help Center would not load)
- Creatorflow, built-in automation (updated Nov 19, 2026): https://creatorflow.so/blog/instagram-built-in-automation/
- CXWizard, free IG comment DM setup (template link, 10 keywords, 1000 characters, images): https://cxwizard.app/blog/how-to-setup-ig-comment-dm-automation-for-free
- Planoly, free comment-to-DM with Business Suite (5 keywords, case-sensitive, 15 minutes): https://www.planoly.com/blog/free-instagram-comment-to-dm-meta-business-suite
- Getkanal, native setup guide: https://getkanal.com/blog/instagram-automatic-messages
- DMcompared, auto-replies in Business Suite: https://dmcompared.com/how-to/auto-reply-in-meta-business-suite/
- Ahammed Rishan, comment automation steps: https://ahammedrishan.com/instagram-comment-automation-using-meta-business-suite/
- Reachlee, Comment to message limits (Facebook side; page-wide, no analytics, plain text): https://www.reachlee.co/guides/meta-business-suite-comment-to-message-limits/
- heyy.to, the dissenting read: https://heyy.to/blog/meta-business-suite-comment-auto-reply/
- Messengerbot, built-in replies: https://messengerbot.app/instagram-auto-reply/

ManyChat and rules
- Creatorflow, ManyChat Free plan: https://creatorflow.so/blog/manychat-free-plan/
- PilotDM, ManyChat Free in 2026 (competitor): https://www.pilotdm.com/blog/is-manychat-free-in-2026-what-the-0-plan-actually-gives-you
- Blotato, ManyChat pricing (updated Nov 9, 2026): https://www.blotato.com/blog/manychat-pricing
- Chatimize, comment-to-DM build (Free = specific post only; follow condition; no DM on follow): https://chatimize.com/auto-reply-instagram-comments/
- Creatorflow, DM compliance (24-hour window, Oct 5 quick-reply change, penalties): https://creatorflow.so/blog/instagram-dm-compliance-meta-rules/
- Spur, DM automation rules: https://www.spurnow.com/en/blogs/instagram-dm-automation-rules
- Buffer, DM automation (writer's results, 200 per hour claim): https://buffer.com/resources/instagram-dm-automation/
- FYProof, engagement bait penalties (Oct 22, 2026): https://fyproof.com/guides/engagement-bait-penalties
- Creator Lane, comment automation playbook: https://creatorlanehq.com/blog/instagram-comment-automation-playbook-2026
- BigGo, Mosseri "engagement hack" (secondhand): https://finance.biggo.com/news/397441c73e4684c3

Deliverable design
- Creatorflow, deliver free PDFs via DM (25 MB, hosting, formats table): https://creatorflow.so/blog/instagram-lead-magnet-automation-deliver-free-pdfs-via-dm/
- UnlockDM, what makes a good Instagram lead magnet: https://www.tryunlockdm.com/blog/instagram-lead-magnet-dm-delivery
- ReplyRush, lead magnet automation (60-word DM, numbers): https://www.replyrush.com/post/instagram-lead-magnet-automation
- Claimful, lead magnets for contractors: https://claimful.co/blog/lead-magnet-ideas-contractors-home-services
- Webby, lead magnets for trades: https://www.webby.net.au/blog/marketing-how-to/lead-magnets-for-trades/
- UPDF, lead magnet PDF examples: https://updf.com/knowledge/lead-magnet-pdf-examples/
- MagicPost, LinkedIn comment-bait study (684k posts, July 27, 2026 drop): https://magicpost.in/studies/linkedin-comment-bait
- Amazon Influencer requirements (no public minimum, practical 1k, business account): https://www.adbadger.com/blog/amazon-influencer-program/ and https://indm.social/blog/amazon-influencer-program-requirements
- Social Media Today, Amazon links in Reels (30 per Reel, 20 per post): https://www.socialmediatoday.com/news/instagram-adds-amazon-affiliate-links/874817/

Rival build facts (public repo only): `Desktop\F600-BUILD\STATUS.md`, `BUILD.md`, `notes\daily-hunt-list.md`, `site\parts.json`, `site\build-list.html`, `site\partners.html`
