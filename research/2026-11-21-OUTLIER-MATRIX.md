# The outlier matrix: watch list, 5x+ outliers, 5 x 6 matrix, 30 ideas, 30-day calendar

Built 2026-11-21 for @elcoyotediesel (Project Rival, Chief, the parts counter). Steps 2, 3 and 4 of the "AI brain, watch list, outlier matrix, 30 posts" method. Step 1 (the brain file) is written separately.

Files this document rests on:

- Tool: `C:\Users\Parts\OneDrive - Elite Diesel Service\Desktop\VIDEO\tools\outlier_watchlist.py` (re-run weekly; instructions in `tools\WATCHLIST-README.md`)
- Input: `tools\watchlist\watchlist.json` (41 feeds, 40 accounts)
- Output of today's run: `tools\watchlist\2026-11-21-posts.csv` (2,286 posts), `2026-11-21-medians.csv`, `2026-11-21-outliers.md` (271 posts at 5x or more, Format and Subtopic columns filled), `2026-11-21-log.txt`
- Classified outliers: `research\reel-references\2026-11-21-outlier-matrix\2026-11-21-outliers-classified.csv` and `matrix.json`
- The 20 outliers downloaded and frame-read today: `research\reel-references\2026-11-21-outlier-matrix\NN-handle--slug.mp4` with `.info.json` and `watch-NN-*/` (scenes.csv, sheet-NN.jpg, transcript.txt)

## 0. Honesty notes, read first

1. **Every number for another account is TikTok or YouTube Shorts, never Instagram.** Instagram profile pages logged out show 12 tiles with no view counts and reel pages are login-walled. The watch list reads each account's TikTok mirror (views, likes, comments, shares, saves, dates) or its YouTube Shorts tab (views only in the listing; date, likes and comments were fetched per video for the 35 YouTube posts that cleared 5x). An account's Instagram reel can behave differently from its TikTok twin. The only Instagram numbers in this file are Jacob's own, from the Graph API.
2. **Outlier score = post views divided by that feed's median views over its last 60 posts.** It is relative to the account. A 5x on a 3k-median page (15k views) counts the same as a 5x on a 300k-median page. That is the point of the method: the idea travelled past the people who already follow.
3. **Share ratio = TikTok reposts divided by views.** YouTube hides shares. TikTok plays run higher than Instagram reach, so a TikTok 2 percent is roughly an Instagram 3 percent sends per reach (the account's own 10 mil meme is 4.05 percent of views, 4.91 percent of reach).
4. **Window bias.** Daily posters (DPP, bluecollar.memes, FASS) have a 3 to 8 week window; weekly posters (c10talk, dom_obs7.3) have a window going back to 2022. Both are in the table; the date column says which.
5. **Two feeds skipped** and logged: Puddin's Fab Shop (only 4 Shorts), Dylan McCool (no Shorts tab). Both are long-form channels. Lifted Rippers and Oversteer are only on YouTube; their share rates are unknown.
6. **Classification is a judgment.** 20 of the 271 were downloaded and frame-read today (the top in-niche ones not already read in the earlier reports); roughly 25 more were frame-read in VIRAL-DIESEL, BREAKDOWN and MEME-ECONOMY this morning; the rest are classified from title, caption, length and the account's known format. Rows classified from title only are the ones most likely to move a cell by one when re-read next week.
7. **The avoid list still applies to the data.** The highest share ratios in the whole pull are an albertamechanic racial-punchline series (6 to 8 percent) and two bensdiesels fuel-price memes (5.54 and 3.67 percent) built on a borrowed reaction cutout of a man with Down syndrome. They count in the cells because the method counts them; none of the 30 ideas copies them. Rolling coal and delete content are excluded from the ideas for the same legal reasons as before.

## 1. The watch list, with medians (pulled 2026-11-21, last 60 posts per feed)

| # | Handle | Platform | Lane | Posts | Median views | Max views | 5x+ | Median share % |
|---|---|---|---|---|---|---|---|---|
| 1 | rust_ridge_ranch26 | tiktok | 7.3 / OBS | 60 | 28.9k | 365.8k | 5 | 0.18 |
| 2 | dom_obs7.3 | tiktok | 7.3 / OBS | 40 | 20.1k | 727.8k | 9 | 0.69 |
| 3 | gas_guzzlin_obs | tiktok | 7.3 / OBS | 60 | 9.1k | 418.4k | 8 | 0.30 |
| 4 | 1738_ford | tiktok | 7.3 / OBS | 60 | 5.7k | 51.8k | 5 | 0.08 |
| 5 | jeff.salv | tiktok | 7.3 / OBS (dentside) | 60 | 19.4k | 517.7k | 7 | 1.00 |
| 6 | project_furd | tiktok | 7.3 / OBS (Colorado) | 60 | 3.1k | 200.1k | 5 | 0.23 |
| 7 | kory_ppei | tiktok | 7.3 / OBS (PPEI) | 60 | 10.2k | 183.3k | 4 | 0.12 |
| 8 | bensdiesels | tiktok | 7.3 / OBS | 60 | 9.2k | 811.5k | 14 | 0.86 |
| 9 | JMRRebuilders | youtube | 7.3 / OBS | 60 | 19.0k | 111.0k | 1 | n/a |
| 10 | FordBossMe | youtube | 7.3 / OBS | 60 | 3.5k | 37.0k | 3 | n/a |
| 11 | DentsideDepot | youtube | classic Ford | 60 | 44.0k | 552.0k | 3 | n/a |
| 12 | DriveHub | youtube | 7.3 / OBS | 57 | 14.0k | 5.7M | 9 | n/a |
| 13 | davesautocenter | tiktok | diesel shop | 60 | 92.8k | 2.0M | 9 | 0.12 |
| 14 | dirtydieselcustoms | tiktok | diesel shop | 60 | 2.6k | 94.2k | 9 | 0.15 |
| 15 | smithsdieselperformance | tiktok | diesel shop | 60 | 10.4k | 296.6k | 8 | 0.17 |
| 16 | cayleependerass | tiktok | diesel shop | 60 | 138.1k | 1.7M | 4 | 0.07 |
| 17 | albertamechanic | tiktok | diesel shop | 60 | 38.4k | 854.3k | 9 | 1.21 |
| 18 | hblakefitz | tiktok | diesel shop | 60 | 28.9k | 489.4k | 6 | 0.14 |
| 19 | gearman_93 | tiktok | owner-op / Class 8 | 60 | 8.5k | 446.1k | 4 | 0.10 |
| 20 | dieseltechchris | tiktok | diesel shop | 60 | 8.8k | 964.0k | 5 | 0.06 |
| 21 | thedreadlockmechanic | tiktok | diesel memes | 60 | 4.4k | 246.0k | 8 | 0.05 |
| 22 | tomsrefurb | tiktok | classic Ford / restomod | 60 | 86.9k | 596.9k | 1 | 0.29 |
| 23 | PuddinsFabShop | youtube | classic Ford / restomod | 0 | skipped (4 Shorts) | | | |
| 24 | ViceGripGarage | youtube | classic Ford / restomod | 29 | 197.0k | 861.0k | 0 | n/a |
| 25 | squarebodysyndicate | tiktok | classic / restomod | 60 | 4.3k | 177.9k | 11 | 0.27 |
| 26 | c10talk | tiktok | classic / restomod | 60 | 5.2k | 1.2M | 7 | 0.23 |
| 27 | Oversteer.Originals | youtube | classic / restomod | 60 | 98.5k | 14.0M | 10 | n/a |
| 28 | lifted_rippers | youtube | shop skits / identity | 60 | 7.2k | 885.0k | 9 | n/a |
| 29 | custom_harvest_guy | tiktok | farm truck | 60 | 3.6k | 80.8k | 5 | 1.57 |
| 30 | DylanMcCool | youtube | farm truck | 0 | skipped (no Shorts tab) | | | |
| 31 | bluecollar.memes | tiktok | diesel / trade memes | 60 | 4.2k | 358.5k | 9 | 1.50 |
| 32 | diesel_syrup | tiktok | diesel memes | 60 | 94.3k | 1.1M | 10 | 0.23 |
| 33 | topherolive | tiktok | diesel memes / skits | 60 | 90.0k | 2.5M | 8 | 0.77 |
| 34 | joegotti96 | tiktok | trade comedy | 60 | 151.8k | 7.3M | 11 | 0.21 |
| 35 | zac.lucarz | tiktok | diesel commentary | 60 | 69.2k | 1.6M | 4 | 0.07 |
| 36 | fassfuelsystems | tiktok | partner brand | 60 | 12.9k | 855.0k | 10 | 0.17 |
| 37 | dieselpowerproducts | tiktok | retailer | 60 | 3.3k | 929.0k | 21 | 0.07 |
| 38 | bddieselperformance | tiktok | partner brand | 60 | 1.4k | 122.9k | 7 | 0.07 |
| 39 | iidiesel | tiktok | partner brand | 60 | 2.9k | 46.1k | 2 | 0.12 |
| 40 | desertdieselscartel | tiktok | growing small account | 60 | 2.2k | 82.8k | 6 | 0.27 |
| 41 | powerhungryperformance | tiktok | partner brand | 60 | 1.4k | 15.7k | 5 | 0.93 |

What the medians say before any outlier is read: the three 7.3-and-OBS pages with the best median share rate are jeff.salv (1.00, dentside rollers), bensdiesels (0.86, memes on his OBS) and dom_obs7.3 (0.69, silent walkarounds). Among shops, albertamechanic (1.21, two-man skits) is the only one above 0.2. The meme pages split: bluecollar.memes 1.50 and custom_harvest_guy 1.57 (text and cutout memes) versus diesel_syrup 0.23 and joegotti96 0.21 (brand rage and long comedy). The brand feeds all sit at 0.07 to 0.17 except Power Hungry at 0.93 on 1.4k views, which is a 7.3 meme page in disguise.

### 1b. Jacob's own account on the same scale (Instagram, Graph API, 57 reels in posts.tsv, median 598 views)

| Outlier | Date | Views | Reach | Shares | Sends / reach | Skip % | Caption |
|---|---|---|---|---|---|---|---|
| 848x | 2026-10-26 | 506.8k | 418.2k | 20,552 | 4.91% | 38.6 | Yo! Where the 10 mil @?! |
| 663x | 2026-07-24 | 396.6k | 250.8k | 13 | 0.01% | 20 | Well it seemed like a good idea (gooseneck) |
| 9x | 2026-10-28 | 5.3k | 4.1k | 13 | 0.32% | 32.8 | Just remember! |
| 9x | 2026-10-27 | 5.3k | 4.6k | 113 | 2.46% | 35.6 | You know when the build just isn't going as quickly as you'd like |
| 9x | 2026-06-30 | 5.2k | 3.6k | 17 | 0.47% | 37.4 | It may cost you nothing, but to me. It means everything. |
| 8x | 2026-10-29 | 4.8k | 3.8k | 73 | 1.92% | 46 | You know it's true |
| 7x | 2026-10-23 | 3.9k | 3.4k | 19 | 0.56% | 39.6 | Go so hard it even makes me worried. |
| 6x | 2026-08-24 | 3.5k | 3.1k | 29 | 0.95% | 32.6 | Aaaaah yeah so there that |
| 6x | 2026-08-29 | 3.4k | 3.2k | 1 | 0.03% | 58.9 | Here we go boiz! @fassfuelsystems being installed |
| 5x | 2026-10-23 | 3.2k | 2.7k | 17 | 0.64% | 27 | What a shop dog actually looks like |

Ten of Jacob's 57 reels are 5x outliers on his own feed. Seven of the ten are memes or jokes (Shop life x Meme and Numbers x Meme in the matrix below), one is a spectacle fail (the gooseneck), one is a partner install, one is a person reel. The two above 2 percent sends are both Shop life x Meme. His account already behaves like the niche.

## 2. The outliers

271 posts cleared 5x out of 2,286 (11.9 percent). The full ranked list with every count, URL, Format and Subtopic is in `tools\watchlist\2026-11-21-outliers.md` and the classified CSV. The top 40 by outlier score, with the classification:

| # | Outlier | Handle | Plat | Date | Views | Shares | Share % | Len | Title (cleaned) | Subtopic | Format |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 407x | DriveHub | YT | 2026-01-11 | 5.76M | n/a | | 110 s | Rare 7.3 Won't Start | Fails, fixes | Narrated story-fix |
| 2 | 283x | dieselpowerproducts | TT | 2026-11-16 | 929k | 2,807 | 0.30 | 9 s | What do you think? (the roof-strapped truck, "this guy knows what he's doing") | Fails, fixes | Clip + question caption |
| 3 | 271x | DriveHub | YT | 2025-07-18 | 3.86M | n/a | | 75 s | I painted my car with $59 of turbo spray cans | Numbers (cost) | Narrated story-fix |
| 4 | 232x | dieselpowerproducts | TT | 2026-10-31 | 761k | 2,475 | 0.33 | 25 s | What would you do? (lifted Chevy sliding on a snow road) | Fails, fixes | Clip + question caption |
| 5 | 230x | c10talk | TT | 2022-01-02 | 1.2M | 5,911 | 0.49 | 51 s | Tech tip on worn-out Nader pins, cheap fix | Fails, fixes | other: tech tip |
| 6 | 196x | dieselpowerproducts | TT | 2026-11-01 | 644k | 13,700 | 2.13 | 52 s | Did you know about this? (ratchet strap opens a locked truck) | Fails, fixes | Clip + question caption |
| 7 | 150x | dieselpowerproducts | TT | 2026-10-29 | 493k | 596 | 0.12 | 9 s | That's one way to do it (F-150 strapped by the roof) | Fails, fixes | Clip + question caption |
| 8 | 142x | Oversteer.Originals | YT | 2026-08-25 | 14.8M | n/a | | 115 s | Daily drive a classic car they said | Old truck | Narrated story-fix |
| 9 | 140x | dieselpowerproducts | TT | 2026-10-17 | 461k | 25 | 0.01 | 10 s | What not to do | Fails, fixes | Clip + question caption |
| 10 | 122x | lifted_rippers | YT | 2026-09-03 | 885k | n/a | | 16 s | How many "promise you won't get mad" upgrades do you have? | Numbers (cost) | Two-man skit |
| 11 | 110x | dieseltechchris | TT | 2026-08-27 | 964k | 76 | 0.01 | 75 s | TikTok Shop tool post | Shop life | other: ad |
| 12 | 91x | bddieselperformance | TT | 2026-11-06 | 123k | 2,194 | 1.79 | 45 s | How much does it cost to have a booth at SEMA? | Numbers (cost) | Named-tribe news |
| 13 | 90x | Oversteer.Originals | YT | 2026-08-15 | 8.96M | n/a | | 176 s | Trying to get jet fuel for my truck almost killed me | Fails, fixes | Narrated story-fix |
| 14 | 89x | bensdiesels | TT | 2026-08-21 | 812k | 7,341 | 0.90 | 10 s | California trucks when the tire ban kicks in | Numbers (news) | Cutout / text-card meme |
| 15 | 86x | DriveHub | YT | 2021-05-10 | 1.28M | n/a | | 19 s | Supra donuts | other: life | Roller |
| 16 | 86x | DriveHub | YT | 2026-03-18 | 1.21M | n/a | | 104 s | Painting the Corvette with a Sharpie | Numbers (cost) | Narrated story-fix |
| 17 | 85x | bluecollar.memes | TT | 2026-10-31 | 359k | 12,000 | 3.35 | 8 s | POV: coming into work Monday and remembering Friday's "Monday problems" | Shop life | Cutout / text-card meme |
| 18 | 76x | bddieselperformance | TT | 2026-09-17 | 103k | 1,930 | 1.87 | 8 s | "Gas is so expensive" / Diesel owners RN | Numbers (cost) | Cutout / text-card meme |
| 19 | 73x | c10talk | TT | 2022-04-08 | 378k | 421 | 0.11 | 17 s | How many BowTies is too many? | Tribe identity | Clip + question caption |
| 20 | 66x | fassfuelsystems | TT | 2026-09-21 | 855k | 9,308 | 1.09 | 26 s | BREAKING: the 8.3 liter Mongoose Duramax is coming | Numbers (news) | Named-tribe news |
| 21 | 64x | project_furd | TT | 2024-12-27 | 200k | 4,544 | 2.27 | 18 s | Big booty blue (OBS dually walkaround) | other: show | Roller |
| 22 | 64x | dieselpowerproducts | TT | 2026-11-10 | 209k | 628 | 0.30 | 5 s | What do you think? | Fails, fixes | Clip + question caption |
| 23 | 57x | dieselpowerproducts | TT | 2026-10-19 | 186k | 54 | 0.03 | 12 s | Was this impressive? | other: sound | Clip + question caption |
| 24 | 56x | thedreadlockmechanic | TT | 2026-11-08 | 246k | 794 | 0.32 | 28 s | The real reason I don't use the E39 | Fails, fixes | Narrated story-fix |
| 25 | 53x | bluecollar.memes | TT | 2026-11-13 | 224k | 1,887 | 0.84 | 6 s | (jobsite meme) | Shop life | Cutout / text-card meme |
| 26 | 52x | gearman_93 | TT | 2026-10-30 | 446k | 2,846 | 0.64 | 444 s | (Class 8 transmission story) | Shop life | Narrated story-fix |
| 27 | 52x | dieselpowerproducts | TT | 2026-11-11 | 170k | 185 | 0.11 | 8 s | What do you think | Fails, fixes | Clip + question caption |
| 28 | 49x | bensdiesels | TT | 2026-03-20 | 448k | 24,800 | 5.54 | 11 s | Anything to save a few bucks (red diesel POV) | Numbers (cost) | Cutout / text-card meme |
| 29 | 49x | Oversteer.Originals | YT | 2026-03-18 | 4.9M | n/a | | 165 s | 351 Windsor had so many problems from the last mechanic | Fails, fixes | Narrated story-fix |
| 30 | 48x | joegotti96 | TT | 2026-11-12 | 7.3M | 64,900 | 0.89 | 63 s | Is trucking a trade? | Shop life | Two-man skit |
| 31 | 47x | thedreadlockmechanic | TT | 2026-10-17 | 208k | 600 | 0.29 | 8 s | I'm a boxer engine | Tribe identity | Cutout / text-card meme |
| 32 | 46x | dieselpowerproducts | TT | 2026-10-17 | 152k | 80 | 0.05 | 8 s | What do you think? | Fails, fixes | Clip + question caption |
| 33 | 46x | bluecollar.memes | TT | 2026-11-10 | 193k | 5,975 | 3.10 | 5 s | Woody, "Porch Light" HR confession | Shop life | Cutout / text-card meme |
| 34 | 46x | gas_guzzlin_obs | TT | 2026-03-12 | 418k | 3,327 | 0.80 | 20 s | Been a minute (OBS between hay bales, Grave Digger audio) | Tribe identity | Roller |
| 35 | 41x | squarebodysyndicate | TT | 2026-01-18 | 178k | 4,250 | 2.39 | 56 s | Extended cab 7 ft bed (interior detail walk) | Old truck | Roller |
| 36 | 41x | lifted_rippers | YT | 2026-07-17 | 298k | n/a | | 11 s | What are we putting on your truck | other: show | Clip + question caption |
| 37 | 40x | dieseltechchris | TT | 2026-07-16 | 349k | 224 | 0.06 | 60 s | Pool days (TikTok Shop) | other: life | other: ad |
| 38 | 37x | desertdieselscartel | TT | 2026-09-08 | 83k | 1,719 | 2.08 | 18 s | Built not bought, featured member truck | other: show | Roller |
| 39 | 37x | bensdiesels | TT | 2026-09-14 | 340k | 12,500 | 3.67 | 11 s | Guess we're farmers now (red diesel at $9 a gallon) | Numbers (cost) | Cutout / text-card meme |
| 40 | 37x | squarebodysyndicate | TT | 2026-08-10 | 160k | 3,533 | 2.22 | 37 s | Period-correct KC lights on all squarebodies | Old truck | other: before/after feature |

Other 5x+ rows that matter for the ideas below, by rank: 45 dom_obs7.3 "Your boyfriend's dream truck" (36x, 728k, 1.13 percent, silent walkaround); 49 bensdiesels "Bro doesn't know how fragile this is" (31x, 2.79 percent); 50 dirtydieselcustoms "3rd Gen Cummins owners, this one's for you" (30x, 2.25 percent); 53 bensdiesels "accurate version" (27x, 4.72 percent); 54 bensdiesels "7.3 owners will literally learn to fly before buying a new truck" (27x, 3.15 percent, a found stunt clip where the caption is the whole joke); 55 jeff.salv dentside roller (27x, 518k, 1.64 percent); 64, 75, 79, 107 albertamechanic (avoid list, 5 to 8 percent); 67 davesautocenter 17-year-old and a 7.3 (22x, 2.0M, 9k comments); 95 bensdiesels "so much torque the chassis twisted" (15x, 8.18 percent, the highest clean share rate in the pull); 110 DentsideDepot "always keep a screwdriver and paperclips in an old Ford" (13x, 552k); 114 dieselpowerproducts "Imagine" (12x, 4.4 percent, 5 s); 125 and 214 powerhungryperformance 7.3 memes (3.62 and 3.90 percent on 9k to 16k views); 136 FASS 2,000 rwhp 6.0 (10x, 2.95 percent); 154 thedreadlockmechanic glow-plug text card (9x, 2.28 percent).

### 2b. What the 20 frame-read today actually look like (one line each; sheets in the outlier-matrix folder)

| File | What is on screen | Sound | Text | Length, cuts |
|---|---|---|---|---|
| 01 DriveHub, Rare 7.3 Won't Start | Wide of a white OBS crew cab at 0.0, barn, dash, battery, corroded ground, cables, starter; face first at 12 s | VO from 0.0: "I bought one of the rarest trucks Ford ever built and I'm rebuilding it after it sat in a barn" | none burned | 110 s, 78 cuts (every 1.4 s) |
| 02 DPP, What would you do? | Dashcam, a lifted Chevy sliding across a snowy mountain road ahead | original, no voice | one white pill "WHAT WOULD YOU DO?" top centre for all 25 s | 25 s, 1 shot |
| 03 c10talk, Nader pins | Man beside an orange C10, label "GM door FIX!!" with a wrench emoji, cuts to PEX hose on the pin | talking from 0.2 s | one label held throughout | 51 s, 2 shots |
| 04 DPP, Did you know about this? | Found clip of a lineman opening a locked truck with a ratchet strap, host keyed lower-left reacting | host: "okay what do we got here... no way... somebody out there test this" | none | 52 s, 8 cuts |
| 05 DPP, That's one way to do it | F-150 strapped to a trailer by a strap over the roof, host lower-left | host: "New truck secured" | two pills: "And it's chained up" and "#Secured" | 9 s, 2 shots |
| 06 Lifted Rippers, promise you won't get mad | Woman and man in a shop beside a hot rod, "does this skirt make me look fat", "you promise you won't get mad", "I bought a new turbo" | spoken, karaoke caption small | small caption | 16 s, 3 shots |
| 07 BD Diesel, SEMA booth cost | Host walking the booth, dollar pop words ($15,000 carpet, $50,000 space, $10,000 sign, $54,000 internet, $18,000 handling) | spoken from 0.0 | big white pop words | 46 s, 13 cuts |
| 08 bensdiesels, tire ban | One still of a lifted red dually, text card "California Trucks When The Tire Ban Kicks In" | a rap clip | one text card | 10 s, 1 shot |
| 09 bluecollar.memes, Monday problems | One handheld shot of a drywaller looking around a gutted room | "oh f***, oh my god" | POV text card top | 8.5 s, 1 shot |
| 10 BD Diesel, gas is so expensive | A man "driving" in a plastic tote in the shop door, smoke behind, then a grinning reaction cutout | clip audio "you don't even know what a bad day is" | two cards: the quote and "Diesel Owners RN" | 8.6 s, 2 shots |
| 11 project_furd, big booty blue | OBS dually rolling out of a shed, on grass, on a dirt road, dusk, Colorado plains | song | none | 19 s, 7 shots |
| 12 bensdiesels, save a few bucks | A borrowed reaction cutout of a man drinking, over a still of his white OBS, POV red-diesel card | clip grunts | one card | 11 s, 1 shot |
| 13 bensdiesels, farmers now | Same template, card "after normal diesel hit $9 a gallon" | same | one card | 11 s, 1 shot |
| 14 bensdiesels, learn to fly | Found or generated stunt clip: an OBS drives up a vertical ramp and launches | music | none, the caption is the joke | 14 s, 3 shots |
| 15 Squarebody Syndicate, 7 ft bed | Interior detail walk: door panel, USB in the ashtray, bench, seat fabric | a song | none | 57 s, 1 handheld take |
| 16 dom_obs7.3, boyfriend's dream truck | Silent walk around a white OBS crew cab: tailpipe, BFG, door handle, grey cloth interior | ambient | none | 32 s, 1 take |
| 17 Dentside Depot, screwdriver and paperclips | Hand holds a screwdriver and a paperclip in front of a dentside at 0.0, then the starter relay and neutral safety switch | VO from 0.0 | none | 26 s, 5 cuts |
| 18 gas_guzzlin_obs, been a minute | OBS parked between hay walls at sunset, owner beside it | the Dennis Anderson "dig your grave" origin audio | none | 20 s, 4 shots |
| 19 jeff.salv, dentside | Handheld walk around a two-tone lifted dentside in a shop full of dentsides | song | none | 37 s, 1 take |
| 20 FASS, Mongoose | Split screen: GM's teaser on top, host bottom with karaoke captions, title card "8.3 MONGOOSE Duramax is OFFICIAL" | spoken from 0.0 | title card plus karaoke | 26 s |

What the twenty confirm about the earlier rules: the first word or the first picture lands at 0.0 in all twenty; eleven have no burned text and eight have exactly one card or pill; the rollers and memes are one take; only the narrated stories cut fast (DriveHub every 1.4 s, BD every 3.5 s); nothing ends with an outro; the two highest-sharing clips in the set (bensdiesels 5.54, bluecollar 3.35) are one still or one shot with one card.

## 3. The 5 x 6 matrix

Subtopics are the five that recur most across the 271 (raw counts: shop life 50, fails and fixes 47, tribe identity 43, old truck 34; news 19 plus power records 10 plus cost 16 merged as "numbers" 45). Left out as "other": lifted and show trucks (24), persona and off-topic life (18), pure sound and cold starts (10). Formats are the six that recur most (raw: roller 55, narrated story 53, meme 40, skit 35, named-tribe news 25, clip plus question caption 22 plus vote 14 merged as 36). Left out: before/after feature (11), tech tip (7), hater reply (7), ads (2). 196 of the 271 land inside the 5 x 6.

Each cell: count of 5x+ posts, median outlier score, median TikTok share percent where shares exist, number of different accounts.

| Subtopic \ Format | Roller / sound clip, no talk | Narrated story-fix | Cutout / text-card meme | Two-man one-liner skit | Named-tribe news, one fact | Clip + question caption |
|---|---|---|---|---|---|---|
| **Fails, fixes, warnings** | 0 | **24**, med 10.1x, share 0.17, 8 accts (DriveHub 407x, Oversteer 90x, dreadlock 56x) | 0 | 0 | 2, med 9.3x, 1 acct (Ford Boss Me oil myths) | **17**, med 18.1x, share 0.21, 4 accts (DPP 283x, 232x, 196x at 2.13 percent) |
| **Shop life** | 1, 6.6x | 6, med 6.8x, share 0.28, 3 accts (gearman_93 52x) | **18**, med 15.2x, **share 2.30**, 4 accts (bluecollar.memes 85x at 3.35) | **23**, med 11.2x, **share 1.79**, 5 accts (joegotti 48x, Lifted Rippers 36x, alberta clean 2.5 to 3.5) | 0 | 1, 9.2x (tag your favorite coworker) |
| **Tribe identity** | **13**, med 9.9x, share 0.80, 3 accts (gas_guzzlin 46x, dom_obs 36x at 1.13) | 2, med 16.7x, share 0.04 (Dave's 17-year-old) | **15**, med 10.6x, share 0.90, 4 accts (bensdiesels 4.72, dreadlock boxer 47x) | 0 | 0 | 7, med 8.3x, share 0.36, 7 accts (c10talk 73x, bensdiesels learn-to-fly 3.15, DPP Imagine 4.4) |
| **Old truck nostalgia** | **18**, med 11.1x, share 0.97, 6 accts (Squarebody Syndicate 41x at 2.39, jeff.salv 27x at 1.64) | 3, med 8.7x, share 1.82, 2 accts (Oversteer 142x) | 0 | 0 | 4, med 5.8x, share 1.23, 2 accts (Dentside Depot, c10talk) | 1, 6.2x |
| **Numbers: news, records, cost** | 2, med 11.0x, share 4.38 (bensdiesels chassis twist 8.18) | 9, med 8.6x, share 0.43, 6 accts (DriveHub $59 paint 271x) | 6, **med 43.1x**, share 1.39, 3 accts (tire ban 89x, BD gas 76x) | 4, med 13.2x, share 0.31, 2 accts (Lifted Rippers "promise you won't get mad" 122x) | **17**, med 16.7x, share 0.93, 5 accts (BD SEMA booth 91x at 1.79, FASS Mongoose 66x, FASS 2,000 hp 2.95) | 3, med 10.0x, share 0.31 (what MPG towing) |

How to read it:

- **Five cells hold 109 of the 196** (56 percent): Fails x Story (24), Shop x Skit (23), Shop x Meme (18), Old x Roller (18), Fails x Question-clip (17), Numbers x News (17). These are the proven cells. The ideas in them are the ones to post first and to give the cleanest 48 h reads.
- **Sends and views live in different cells.** Shop x Meme (2.30 median share) and Shop x Skit (1.79) are the send cells; Fails x Story and Fails x Question-clip are the view cells (median 10x and 18x, share 0.2). Numbers x News is the one cell that does both (16.7x median, 0.93 share, and the single best build-adjacent share rates in the niche: FASS 2.95, BD 1.79, DDC 2.25).
- **Eight cells are empty.** Nobody on the list has a 5x in Fails x Roller, Fails x Meme, Fails x Skit, Shop x News, Identity x Skit, Identity x News, Old x Meme, Old x Skit. An empty cell is not a dead cell; it means the idea in it is a bet backed by its row and column neighbours rather than by a direct outlier. They are scheduled in the second week.
- **Identity x News is empty on TikTok and is the top-sharing build format in the 30-day BREAKDOWN** ("3rd Gen Cummins owners, this one's for you", 2.25 percent; it is classified under Numbers here because the news is a product). Rival's named-tribe openers (the tribe report, section 8) are the test of that cell.

## 4. The 30 ideas, one per cell

Rules applied to every one: real footage only, one lockup on the hook at most (LOUDER combo for jokes), no on-screen call to action, no outro, no grade, the song added in-app if any, caption line 1 names a person type, no delete or coal content, no Elite Diesel or 307 anywhere on Rival or Chief content, the Rival transmission stays unmentioned beyond "built". Numbers in the facts are from BUILD.md and the tribe report. "Day" refers to the calendar in section 5.

Format of each row: hook (what is in frame 1 and the text on it), the first spoken line (or none), caption line 1, footage, the outlier(s) behind it, day.

### Fails, fixes, warnings

**1. Fails x Roller (empty cell, a bet): "One bolt."**
Frame 1: a breaker bar already on a rusted 1959 frame or cab-mount bolt, Jacob's hand on the bar, shop light. Lockup: "67 years" / "ONE BOLT". No speech; the bar creaks, the bolt does not move, cut on the exhale. 10 to 12 s, one shot. Caption line 1: "For whoever is pulling a cab off a 67 year old frame this weekend." Footage: the frame work, whichever bolt is real that day. Backed by the row (fails are the biggest view row) and the column neighbours (Old x Roller 18, 0.97 share); MEME-ECONOMY meme 5. Day 9 morning.

**2. Fails x Narrated story-fix (24 posts, median 10.1x; DriveHub 407x, Oversteer 142x): "It sat in a field and now it won't."**
Frame 1: wide of the F600 at 0.0, VO at 0.0: "I bought one of the last 1959 F600s left in Wyoming and it's trying to kill me." Then the actual first problem (seized bolt, rotten cab mount, the fuel line, whatever is real), cut every 2 to 3 s, Jacob's face not before 10 s, the fix, the key or the hoist at the end, "one down." 60 to 90 s. Caption line 1: "For the guy whose project tried to kill him this week." Footage: the frame swap prep, shot on the Pocket 3 on a magnet mount. DriveHub's 5.76M came from a 14k-median channel with exactly this structure. Day 2 afternoon.

**3. Fails x Cutout / text-card meme (empty cell): "Fit on the bench."**
Frame 1: Jacob's own cutout (shot on the shop's flat wall, keyed in CapCut) over a still of a bracket held against the frame, one text block top third: "Measured it four times. Fit on the bench. Does not fit on the truck. Same bracket." No speech. 6 to 8 s. Caption line 1: "Send this to the guy who measured twice and it still didn't fit." Backed by Shop x Meme (2.30 share) applied to the fails row; bluecollar.memes 17, 33. Day 10 morning.

**4. Fails x Two-man skit (empty cell): "Did it fit?"**
Solo. The question is a white pill on screen, nobody else in the shot: pill "Did it fit?" Jacob, alone at the frame: "It fit." Pill again: "...Did it fit?" "It fit on the bench." One locked-off shot, cut on the last word. 7 s. Caption line 1: "For every shop that has asked this question twice in one day." Backed by Shop x Skit (23 posts, 1.79); albertamechanic's clean versions at 2.5 to 3.5. Day 12 morning.

**5. Fails x Named-tribe news (2 posts, Ford Boss Me; plus the counter-credential lane): "7.3 guys, the three parts you will buy twice."**
Frame 1: Jacob at a counter-height bench with a CPS in his hand, "7.3 guys. Three parts you'll buy twice, in order." CPS, UVCH, IPR. Say the acronyms, do not explain them. One fact each, 25 s, no text. Caption line 1: "For the 7.3 owner saving up for the wrong thing." Footage: parts in hand, the 7.3 on the stand behind. Backed by Ford Boss Me 135 and 172, the 6.7 tribe's list-format results (Nick's Powerstroke 344k on 10k subs), and the parts-counter lane study. Day 6 afternoon.

**6. Fails x Clip + question caption (17 posts, median 18.1x; DPP 283x, 232x, 196x at 2.13 percent): "Did you know about this?"**
Frame 1: a real clip from Jacob's own world with something going wrong or a hack happening (a load strapped the wrong way at the lot, the paperclip-on-the-relay trick from Dentside Depot done on the '59, a Marketplace truck "repair"), one white pill top centre: "WHAT WOULD YOU DO?" or "DID YOU KNOW ABOUT THIS?" Jacob keyed lower-left reacting out loud ("no way... somebody test this") for the hack version; silent for the fail version. 9 to 25 s. Caption line 1: "For the guy who's been locked out of his truck in a parking lot at 6 a.m." Footage must be his own or clearly reposted with credit; no shop signage. Backed by DPP 2, 4, 6, 7; Dentside Depot 110. Day 1 morning.

### Shop life

**7. Shop x Roller (1 post, a bet): "6:02 a.m."**
Frame 1: the parts counter in the dark, the first light flickers on, the phone is already ringing. One locked shot, 10 s, real sound, no text. Caption line 1: "For every parts guy whose phone rings before the lights are on." Footage: a morning at the counter, nothing identifying. Backed by Lifted Rippers 218 only; the cell is a bet. Day 15 afternoon.

**8. Shop x Narrated story-fix (6 posts; gearman_93 52x on 446k): "The order that came back three times."**
Frame 1: Jacob at the counter screen, VO at 0.0: "One part. Three returns. Same truck. Here's what was actually wrong." Named engine (ISX, X15, DD15), no customer, no shop name, the principle at the end ("the part was never the problem"). 60 s, cut on the screen, the box, the part. Caption line 1: "For the parts guy who has explained a core charge four times today." Backed by gearman_93 26, 205, 216 and the owner-operator finding that exact bills travel. Day 5 afternoon (the semi variety slot).

**9. Shop x Cutout / text-card meme (18 posts, median 15.2x, median share 2.30; bluecollar.memes 85x at 3.35): "Porch light."**
Frame 1: Jacob's own cutout (laughing or shrugging) over a still of the shop floor, text top third like a text message: "Got called to the office again. Apparently calling the new guy 'Porch Light' because he only works when somebody walks by isn't acceptable." No speech, 6 s. Caption line 1: "Send this to the coworker who only works when someone walks by." This is the account's own best cell (10 mil, 4.91 percent). Backed by bluecollar.memes 17, 25, 33, 46, 85 and I1. Day 3 morning.

**10. Shop x Two-man skit (23 posts, median 11.2x, median share 1.79): "It's a sensor."**
Solo. Pill on screen: "What's it need?" Jacob, alone at the counter: "A sensor." Pill: "Which one?" Jacob holds up a can of brake clean. Cut on the can. 6 s, one locked-off shot, no music, the two pills are the only text. Caption line 1: "Send this to the guy whose diagnosis is always 'it's a sensor.'" Backed by Lifted Rippers 44, 103, 126; joegotti 30; the albertamechanic clean versions. Day 2 morning.

**11. Shop x Named-tribe news (empty cell): "Parts guys, the most returned part in the building this year."**
Frame 1: Jacob with the returns shelf behind him, the part in hand, "Parts guys, this one's for you. The most returned part in this building in 2026, and it's not the one you'd guess." One part, one reason, principle only. 20 s. Caption line 1: "For the guy who buys by the box color." Backed by the Numbers x News column (17 posts) and the September "don't buy this" format; employee disclosure in the caption. Day 11 afternoon.

**12. Shop x Clip + question caption (1 post, Lifted Rippers "tag your favorite coworker"): "Who's this at your shop?"**
Solo. Frame 1: Jacob himself, camera locked off wide, doing the thing everyone's coworker does (carrying one bolt the whole length of the shop, opening a third energy drink, standing in the bay door looking busy), one pill: "WHO'S THIS AT YOUR SHOP?" No speech, 8 s. Caption line 1: "Every shop has this guy. This one's for him." Backed by 150 and the DDC energy-drink nature doc (6.89 percent). Day 8 morning.

### Tribe identity

**13. Identity x Roller (13 posts, median 9.9x; dom_obs7.3 36x at 1.13, gas_guzzlin 46x): "Your boyfriend's dream truck, 1959 edition."**
Frame 1: the '59 cab at golden hour, the Ford script, the handheld walk starts moving at 0.0. Silent, ambient only, no text, 25 to 30 s, one take: door latch, the lettering, the dash, the Super Duty frame beside it. Caption line 1: "For the girl whose boyfriend keeps sending her old Fords." Backed by 45, 34, 106, 16 (walkarounds with nothing on screen). Day 4 afternoon.

**14. Identity x Narrated story-fix (2 posts; Dave's 17-year-old 22x, 2.0M, 9k comments): "There's a kid in Cheyenne doing his first 7.3."**
Frame 1: Jacob at the bench, "There's a kid in Cheyenne trying to do his first 7.3 and he's stuck on the exact thing I was stuck on." 30 s, two 2 s inserts of the part in question, ends on "should I go help him?" Part two three days later. Caption line 1: "For anyone who learned this stuff from a stranger." Only if the kid is real; otherwise swap for the "why it stays 2WD" reply-to-comment reel. Backed by 67 and 119. Day 14 afternoon.

**15. Identity x Cutout / text-card meme (15 posts, median 10.6x; bensdiesels 4.72 and 2.79, dreadlock boxer 47x): "7.3 owners when someone asks how fast it is."**
Frame 1: Jacob's own cutout, deadpan, over the 7.3 on the stand, text: "7.3 owners when someone asks how fast it is: 'it's not about that.'" Second card at 0:04: "550 to 600 on compounds. It is a little about that." 8 s. Caption line 1: "Send this to your 7.3 brother." Backed by 53, 49, 31, 125, 214 (Power Hungry's 7.3 memes share at 3.6 to 3.9 on a 1.4k-median page). Day 5 morning.

**16. Identity x Two-man skit (empty cell): "Nice Cummins."**
Solo. Jacob stands at the fender of his own Powerstroke, badge in frame. Pill on screen: "Guy at the pump: nice Cummins." Jacob just looks at the lens, then at the badge, then back. 6 s, cut on the look. Caption line 1: "Send this to the guy who calls every diesel a Cummins." Backed by Shop x Skit and MEME-ECONOMY meme 4. Day 11 morning.

**17. Identity x Named-tribe news (empty on TikTok; the BREAKDOWN's top-sharing build format): "7.3 guys, this one's for you."**
Frame 1: Jacob beside the engine, first line: "7.3 guys, this one's for you." The fact: it is an OBS-era core built with the 99 to 03 fuel and electronics package, HPOP, IDM, PCM and harness, mechanical lift pump drive blocked off on the front cover. Both halves of the tribe get their engine. 20 s, no text. Caption line 1: "For the one who still says OBS or Super Duty, pick one." Backed by DDC 50 (2.25 percent), FASS 136 (2.95) and the tribe report opener 1. Day 1 afternoon.

**18. Identity x Clip + question caption (7 posts across 7 accounts; c10talk 73x, bensdiesels learn-to-fly 3.15, DPP Imagine 4.4): "Guess the truck by the door."**
Frame 1: Jacob's hand already on the '59 door, one pill top centre: "GUESS THE TRUCK BY THE DOOR." Three static medium shots: the 1959 door slam (that hollow clang), label 1959; Chief's door, 2011; a new aluminum Super Duty door at the lot, 2024. 10 s, real sound only. Caption line 1: "For the guy who says they don't build them like they used to." Backed by Lifted Rippers Y5 (21.4M on a 20k channel), 19, 54, 114. Day 3 afternoon.

### Old truck nostalgia

**19. Old x Roller (18 posts, median 11.1x; Squarebody Syndicate 41x at 2.39, jeff.salv 27x at 1.64): "DEAL LUMBER & CONST. CO., LARAMIE, WYO."**
Frame 1: the door lettering, close, the phone turning the handheld walk at 0.0. Silent detail walk: the lettering, FR-5-4866, the door latch, the dash, the F600 badge, the hood ornament, one wide at the end. 30 s, no text, one take, song added in-app (the Seger clip did 1.9 for dom_obs7.3). Caption line 1: "Send it to whoever still talks about grandpa's Ford." Backed by 35, 55, 70, 71, 15 and 19 (interior and detail walks with nothing on screen). Day 4 morning.

**20. Old x Narrated story-fix (3 posts; Oversteer 142x on 14.8M, jeff.salv 1.82): "This truck worked for a lumber company in 1959."**
Frame 1: the truck wide, VO at 0.0: "This truck hauled lumber out of Laramie, Wyoming starting in 1959. Here's what 67 years did to it." A walk through the damage with the story: the cab, the rot, the 2WD, the frame that is leaving, the lettering that gets photographed before paint. Cut every 2 to 3 s, 60 to 75 s, captions for the first 20 s only. Caption line 1: "For the guy restoring his grandpa's truck one bolt at a time." Backed by 8, 160, 215 and the Oversteer Y9 read. Day 7 afternoon.

**21. Old x Cutout / text-card meme (empty cell): "It's all original."**
Frame 1: Jacob with a hand on the cab, text card "it's all original" (LOUDER lockup), 2 s; the phone pans down to the Super Duty frame and the modern suspension mounts, 5 s; back to his face, cut. Caption line 1: "Send this to the purist in your group chat. He is not going to like it." Backed by the Old row (34 outliers) and the meme column; MEME-ECONOMY meme 14; the 57 to 60 tribe's "leave the '59 alone" reflex. Day 13 afternoon (the one meme in an afternoon slot, because the week's afternoons are otherwise all talking reels).

**22. Old x Two-man skit (empty cell): "Numbers matching?"**
Solo. The questions are pills on screen: "What year?" Jacob, alone in front of the cab: "Fifty-nine." Pill: "Original?" "The cab is." Pill: "...And?" "That's it." One locked-off shot, cut on "that's it." 8 s. Caption line 1: "For the guy who asks 'numbers matching?' at every show." Backed by Shop x Skit and the classic tribe's purist argument. Day 14 morning.

**23. Old x Named-tribe news (4 posts; Dentside Depot "Ford trucks were brilliant in the 1970s" 6.2x, "screwdriver and paperclips" 12.6x on 552k): "57 to 60 Ford guys, I know what you're thinking."**
Frame 1: the hater quote on screen, "Leave the '59 alone", Jacob reading it off his phone. Then the facts: only the cab and front sheet metal survive, the 1959 frame is retired and goes to the 57 to 60 group with the original running gear if they want it, 1959 was the first year Ford built its own 4x4 and this one left the factory 2WD and stays 2WD. 25 s. Caption line 1: "For the guy who told you to keep it stock." Backed by 234, 266, 110 and the Stradman "keep it stock" tease (BREAKDOWN 04). Day 8 afternoon.

**24. Old x Clip + question caption (1 post, Oversteer "anyone ever seen one on the road?"): "Anyone seen a '59 F600 on the road lately?"**
Frame 1: the cab on the hoist or beside the frame, one pill: "WHEN DID YOU LAST SEE ONE OF THESE ON THE ROAD?" Silent, 10 s. Caption line 1: "For the medium-duty guys who ran one of these for a living." Backed by 231 and the F600 question the tribes ask first (what is in it now). Day 10 afternoon.

### Numbers: news, records, cost

**25. Numbers x Roller (2 posts; bensdiesels chassis twist 8.18 percent, the highest clean share in the pull): "Pyro and boost, no talking."**
Frame 1: the ISSPRO pyro and boost on Chief at idle, Jacob's hand on the shifter, then the pull: needles move, real sound only, 10 s, nothing on screen. Caption line 1: "For the guy running compounds with no pyro." On the 7.3 later: the same shot on first fire. Backed by 95 and 192 (a number happening on camera, no words). Day 6 morning.

**26. Numbers x Narrated story-fix (9 posts; DriveHub $59 paint 271x, Sharpie Corvette 86x, Kory Willis transparency 18x): "What the frame swap has cost so far, to the dollar."**
Frame 1: a stack of real receipts on the frame rail, VO at 0.0: "Everybody posts the build. Nobody posts the bill. Here's the frame swap so far, to the dollar." The frame, the dead axle, the fab consumables, the stuff bought twice; running total card updated three times (the one text exception, it is the content). 60 s. Caption line 1: "For the person who wants the number nobody posts." Backed by 3, 16, 82, 204 and the growth-study gap (nobody in the twelve filled the ledger). Day 12 afternoon.

**27. Numbers x Cutout / text-card meme (6 posts, median 43.1x, the highest median in the matrix; tire ban 89x, BD gas 76x at 1.87): "Where the 10 mil at, part 2."**
Frame 1: a still of the bare Super Duty frame beside the '59 cab, LOUDER lockup: "sponsors: 'send us the build budget'" / 0:04 "THE BUILD BUDGET:" over the frame on jack stands, Jacob's own cutout shrugging. 7 s. Caption line 1: "For the guy who thinks SEMA builds pay for themselves." The account's own record cell (I1, 4.91 percent). Backed by 14, 18, 28, 39, I1. Day 7 morning.

**28. Numbers x Two-man skit (4 posts; Lifted Rippers 122x "promise you won't get mad"): "Promise you won't get mad?"**
Solo, one side of a phone call. Jacob alone at the parts shelf, phone to his ear, we only hear him: "Promise you won't get mad?" (listens) "...A turbo." (listens) "...The second one." Cut on "second." 10 s, one locked-off shot. Caption line 1: "For whoever has a 'promise you won't get mad' part in the garage right now." Backed by 10, 91, 133. Day 15 morning.

**29. Numbers x Named-tribe news (17 posts, median 16.7x; BD SEMA booth 91x at 1.79, FASS Mongoose 66x, DDC 3rd Gen 2.25, FASS 2,000 hp 2.95): "What it costs to put a truck at SEMA when you are nobody."**
Frame 1: Jacob with the SEMA 2027 dates, pop numbers in the BD style, spoken from 0.0: "You cannot just drive your truck to SEMA. Here's what it actually takes." Facts from the pitches report: every vehicle must be owned or sponsored by an exhibitor; feature-vehicle space $499 to $599, applied by the sponsor around July 30 and paid by August 6, 2027; non-exhibitor logos capped at two marks of 50 square inches; booth carpet alone cost BD $15,000. 40 s. Caption line 1: "For the guy who thinks you just drive your truck to SEMA." Backed by 12, 20, 41, 50, 136. Day 9 afternoon.

**30. Numbers x Clip + question caption (3 posts; "what MPG are you getting towing", DPP "who wants one"): "What are you paying for diesel?"**
Frame 1: the pump screen on Chief's fill-up, the total, one pill: "WHAT'S DIESEL WHERE YOU ARE?" and the Cheyenne price in the caption. Silent, 8 s. Caption line 1: "For everyone who just filled a 48 gallon tank and felt it." Backed by 226, 78, 18 (gas-price question clips) and BD 18 at 1.87. Day 13 morning.

## 5. The 30-day calendar

Slots: **morning 09:00 to 11:00** (followers online 80 to 85 percent of peak) for memes, skits, rollers and question clips; **afternoon 16:00 to 19:00** (the account's measured peak, 87 to 92) for the build, credential and story reels. One topic per reel. Build reels go out as Trial Reels if the composer shows the toggle, with two caption first lines tested. Pin a comment that repeats the person type. Share each to Story with the same line.

Days 1 to 15: all 30 ideas, proven cells first so they get clean 48 h reads before the bets. Each post gets the 48 h read logged in the five blank columns (reach, sends, sends per reach, skip percent, saves per reach), taken from the Graph API or the in-app insights at hour 48, not before.

| Day | Date | Slot | Idea | Cell | Reach 48h | Sends | Sends/reach | Skip % | Saves/reach |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Sat Nov 22 | AM | 6 Did you know about this? | Fails x Question-clip | | | | | |
| 1 | Sat Nov 22 | PM | 17 7.3 guys, this one's for you | Identity x News | | | | | |
| 2 | Sun Nov 23 | AM | 10 It's a sensor | Shop x Skit | | | | | |
| 2 | Sun Nov 23 | PM | 2 It sat in a field and now it won't | Fails x Story | | | | | |
| 3 | Mon Nov 24 | AM | 9 Porch light | Shop x Meme | | | | | |
| 3 | Mon Nov 24 | PM | 18 Guess the truck by the door | Identity x Question-clip | | | | | |
| 4 | Tue Nov 25 | AM | 19 Deal Lumber lettering walk | Old x Roller | | | | | |
| 4 | Tue Nov 25 | PM | 13 Your boyfriend's dream truck, 1959 | Identity x Roller | | | | | |
| 5 | Wed Nov 26 | AM | 15 7.3 owners when asked how fast | Identity x Meme | | | | | |
| 5 | Wed Nov 26 | PM | 8 The order that came back three times | Shop x Story | | | | | |
| 6 | Thu Nov 27 | AM | 25 Pyro and boost, no talking | Numbers x Roller | | | | | |
| 6 | Thu Nov 27 | PM | 5 Three parts you will buy twice | Fails x News | | | | | |
| 7 | Fri Nov 28 | AM | 27 Where the 10 mil at, part 2 | Numbers x Meme | | | | | |
| 7 | Fri Nov 28 | PM | 20 This truck worked for a lumber company | Old x Story | | | | | |
| 8 | Sat Nov 29 | AM | 12 Who's this at your shop? | Shop x Question-clip | | | | | |
| 8 | Sat Nov 29 | PM | 23 57 to 60 guys, I know what you're thinking | Old x News | | | | | |
| 9 | Sun Nov 30 | AM | 1 One bolt | Fails x Roller (bet) | | | | | |
| 9 | Sun Nov 30 | PM | 29 What it costs to put a truck at SEMA | Numbers x News | | | | | |
| 10 | Mon Dec 1 | AM | 3 Fit on the bench | Fails x Meme (bet) | | | | | |
| 10 | Mon Dec 1 | PM | 24 When did you last see one on the road? | Old x Question-clip | | | | | |
| 11 | Tue Dec 2 | AM | 16 Nice Cummins | Identity x Skit (bet) | | | | | |
| 11 | Tue Dec 2 | PM | 11 Most returned part in the building | Shop x News (bet) | | | | | |
| 12 | Wed Dec 3 | AM | 4 Did it fit? | Fails x Skit (bet) | | | | | |
| 12 | Wed Dec 3 | PM | 26 What the frame swap has cost, to the dollar | Numbers x Story | | | | | |
| 13 | Thu Dec 4 | AM | 30 What's diesel where you are? | Numbers x Question-clip | | | | | |
| 13 | Thu Dec 4 | PM | 21 It's all original | Old x Meme (bet) | | | | | |
| 14 | Fri Dec 5 | AM | 22 Numbers matching? | Old x Skit (bet) | | | | | |
| 14 | Fri Dec 5 | PM | 14 A kid in Cheyenne doing his first 7.3 | Identity x Story | | | | | |
| 15 | Sat Dec 6 | AM | 28 Promise you won't get mad? | Numbers x Skit | | | | | |
| 15 | Sat Dec 6 | PM | 7 6:02 a.m. at the counter | Shop x Roller (bet) | | | | | |

Shooting note: ideas 10, 4, 16, 22, 28 (the five skits) need one coworker for ten seconds each and can all be shot in one lunch break and banked. Ideas 9, 3, 15, 21, 27 (the five memes) need one cutout session of Jacob against the flat wall and five stills. Ideas 19, 13, 1, 25 (the rollers) are one take each. The stories (2, 8, 20, 26, 14) are the only ones that take an evening.

### The ranking rule at day 15 (Sunday Dec 7, after the Dec 6 posts have their 48 h)

1. Every post is read at exactly 48 h. Posts under 500 reach at 48 h are marked "no read" and do not rank (the sample is too small to trust the ratio); they can be re-shot in week 3 if their cell wins on the other post.
2. Rank all 30 by **sends per reach** (the growth number; floor 1 percent, goal 2 percent).
3. Ties within 0.2 points go to the **lower skip rate** (the hook number; target under 45 percent, ours is 30 to 38 on the good ones).
4. Remaining ties go to **saves per reach**.
5. Views and likes do not rank anything. Comments only matter as a flag: a post with comment rate above 1 percent of reach and low sends is an argument reel, which is a separate lane, not a winner here.
6. The **winning cell** is the cell of the number one post. The **second cell** is the highest-ranked cell that is in a different column from the winner (so the next 15 days never run two of the same format) if its post is within 50 percent of the winner's sends per reach; otherwise there is one winning cell.
7. If the winner is a meme or skit cell (the data says it will be) and the best build-adjacent cell (Identity x News, Numbers x News, Fails x Story, Old x Story, Numbers x Story) is at or above the 1 percent floor, that build cell is kept as the afternoon slot regardless of rule 6, so the Rival story keeps moving. If no build cell clears 1 percent, the afternoon slot becomes the second meme or skit cell and the build goes to Stories for two weeks.

### Days 16 to 30: the winners only, a new hook every time

One or two posts a day from the winning cell(s), each with a hook that has not been used (section 6 has 10 ready per predicted cell). Same slots: the send cell in the morning, the build cell in the afternoon. Log the same five columns. Rule for the stretch: if three consecutive posts in a winning cell fall under the day-15 median, the cell is spent; swap to the third-ranked cell.

| Day | Date | AM (send cell, new hook) | PM (build cell, new hook) |
|---|---|---|---|
| 16 | Sun Dec 7 | winner hook 1 | build cell hook 1 |
| 17 | Mon Dec 8 | winner hook 2 | build cell hook 2 |
| 18 | Tue Dec 9 | winner hook 3 | build cell hook 3 |
| 19 | Wed Dec 10 | winner hook 4 | build cell hook 4 (PRI week starts, Dec 10 to 12: the SEMA-cost reel's sibling, "what a PRI booth costs", fits here) |
| 20 | Thu Dec 11 | winner hook 5 | build cell hook 5 |
| 21 | Fri Dec 12 | winner hook 6 | build cell hook 6 (first real cold morning if it lands: the Wait To Start reel) |
| 22 | Sat Dec 13 | winner hook 7 | build cell hook 7 |
| 23 | Sun Dec 14 | winner hook 8 | rest or Story |
| 24 | Mon Dec 15 | winner hook 9 | build cell hook 8 |
| 25 | Tue Dec 16 | winner hook 10 | build cell hook 9 |
| 26 | Wed Dec 17 | second cell hook 1 | build cell hook 10 |
| 27 | Thu Dec 18 | second cell hook 2 | re-read: are the winners still above the day-15 median? |
| 28 | Fri Dec 19 | second cell hook 3 | "Grandpa had one" (Old x Roller) if Old won anything |
| 29 | Sat Dec 20 | second cell hook 4 | re-run `outlier_watchlist.py` (second weekly run; the first is Monday Dec 1) |
| 30 | Sun Dec 21 | second cell hook 5 | the solstice "316 days to SEMA" card over the frame, the one build-count reel |

## 6. Hook variants, 10 each, for the three cells the data says will win

Prediction from the matrix plus the account's own record: the morning winner will be **Shop x Meme** (2.30 median share, the account's 4.91 record) or **Shop x Skit** (1.79); the afternoon winner will be **Numbers x News** (16.7x median, 0.93 share, the best build-adjacent send rates in the niche). Ten hooks each so days 16 to 30 never repeat a hook. Hook = frame-1 picture plus the one text line (memes) or the first spoken line (skits, news). Caption line 1 follows each.

### A. Shop x Meme (Jacob's own cutout over his own still, one text block, 5 to 8 s)

1. Still: the returns shelf. Text: "Got called to the office. Apparently telling a tech 'the part's on the truck, the truck's the one with the hood open' isn't acceptable." Caption: "Send this to the coworker who asked where the truck was."
2. Still: an empty socket slot in the drawer. Text: "'I definitely put it back.'" Caption: "Send this to whoever 'definitely put it back.'"
3. Still: four empty brake-clean cans on the bench. Text: "Diagnosis complete." Caption: "For the guy whose whole process is brake clean and vibes."
4. Still: the counter phone off the hook. Text: "'It just started doing that today.' The belt has been shredded since July." Caption: "Every service writer has this customer. Send it to yours."
5. Still: a box labelled with a January date. Text: "Backorder update: there is no update." Caption: "Send this to whoever has been 'waiting on a part' since October."
6. Still: Jacob's cutout in front of a stack of cores. Text: "Core charge explained for the fourth time today. Same guy." Caption: "For the parts guy who is one core charge from retirement."
7. Still: a 7.3 head on the bench, nobody around. Text: "'Lift with your legs.' There are no legs for this." Caption: "Send this to the guy who lifts 7.3 heads alone."
8. Still: the shop at 6 a.m., lights half on. Text: "Monday problems, as left on Friday." Caption: "For everyone whose Friday self hates their Monday self."
9. Still: a wall of hanging airlines and a Class 8 bumper. Text: "Customer: 'don't worry about the noise, it's always done that.'" Caption: "Send this to the owner-op whose truck has 'always done that.'"
10. Still: Jacob holding a part number tag up to the camera. Text: "Three numbers. One part. Wrong truck. 11 a.m." Caption: "For the parts guy who has been wrong by one digit since 8."

### B. Shop x Skit (two people, one shot, setup and turn, cut on the last word, 5 to 10 s)

1. "What's it need?" "A sensor." "Which one?" (holds up brake clean). Caption: "Send this to the guy whose diagnosis is always 'it's a sensor.'"
2. "Did it fit?" "It fit." "...Did it fit?" "On the bench." Caption: "For every shop that has asked this twice in one day."
3. "You got a 10 mil?" "I had one." Caption: "Send this to whoever has your 10 mil."
4. "How long's it been making that noise?" "It just started today." (pan to the obviously ancient damage) Caption: "Every service writer in America has this customer."
5. "Nice Cummins." (silence, the look) Caption: "Send this to the guy who calls every diesel a Cummins."
6. "Promise you won't get mad?" "What did you buy." "The second turbo." Caption: "For whoever has a 'promise you won't get mad' part in the garage."
7. "Is it under warranty?" "It was." "When did it expire?" "When you touched it." Caption: "Send this to the guy who 'just looked at it.'"
8. "Where's the new guy?" "Which one?" "The one from this morning." "He left at lunch." Caption: "For every shop that has hired three guys named Tyler this year."
9. "Can you check if you have it in stock?" (Jacob looks at the shelf behind him, back at the phone) "...Let me check." Caption: "Send this to the parts guy who can see it from his chair."
10. "What year?" "Fifty-nine." "Original?" "The cab is." "...And?" "That's it." Caption: "For the guy who asks 'numbers matching?' at every show."

### C. Numbers x Named-tribe news (Jacob to camera, the tribe named in the first five words, one number, 20 to 40 s)

1. "You cannot just drive your truck to SEMA." (the exhibitor rule, the $499 to $599 feature-vehicle fee, the July 30 deadline) Caption: "For the guy who thinks you just drive your truck to SEMA."
2. "7.3 guys, here's the number nobody says out loud: 550 to 600 crank on compounds, on a bottom end built before the turbos were picked." Caption: "Send this to your Cummins buddy. He'll be fine."
3. "Frame swap, to the dollar, week one." (the running total) Caption: "For the person who wants the number nobody posts."
4. "Injector nerds: 160 split-shot to 238/80 hybrid when the target went to compounds. Too big for the street or just right?" Caption: "Send to the guy who runs 238s and daily drives it."
5. "6.0 guys, you'll appreciate this: ARP studs over a custom-bore Cometic MLX, no O-rings, 55 to 65 psi, before the engine ever fires." Caption: "Send to anyone who's done head gaskets in a driveway."
6. "Gauge guys, I heard you: ISSPRO pyro and boost go in before the compounds get fabricated." Caption: "Send to the guy running compounds with no pyro."
7. "Medium-duty guys, this is an F600, not a pickup: 2-ton class, duals from the factory, going to single 22.5s pushed to the fenders." Caption: "Send to the guy who ran a two-speed rear for a living."
8. "Laramie, this one's for you: the doors say Deal Lumber & Construction, FR-5-4866, and the FRanklin exchange dates that to the late 1950s." Caption: "Send to the oldest Laramie person you know."
9. "6.7 guys: a FASS does both jobs. It feeds the CP4 clean fuel now and it is already there when the power comes. Not either or." Caption: "Tag the 6.7 guy still running the CP4 on faith."
10. "Chip guys, Hydra or nothing? Four things changed when the target went to 600: turbo layout, injectors, tune, intake size. Rods, pistons, girdle, cam and springs did not." Caption: "Send to the guy still on a TS6."

## 7. What to carry forward

- Re-run the tool every Monday (Dec 1 is the first). A cell that gains outliers two weeks running is a cell to post in; a post that was 5x last week and 8x this week is still climbing and is worth a frame-read.
- The matrix is a 60-post-window snapshot. The February version will look different; the five subtopics are stable, the formats drift.
- The one measurement that decides the second half of the month is sends per reach at 48 h. Everything in this file is a way to get that number above 1 percent on a build reel and above 2 on a meme.
