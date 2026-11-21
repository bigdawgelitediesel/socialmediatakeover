# The most viral diesel and truck reels, all time and the last 90 days, and why each one travelled

Research agent report, 2026-11-21, for @elcoyotediesel / Project Rival. Third file in the day's set. Reads after `2026-11-21-diesel-niche-winners/BREAKDOWN.md` (the last 30 days, 14 clips) and the diesel section of `2026-11-21-hook-atlas/HOOK-ATLAS.md`. Nothing from those two is repeated here except where a number is needed for comparison.

Method. yt-dlp flat listings of the YouTube Shorts tabs and TikTok profiles of 31 diesel, truck and build accounts (4,129 TikTok rows with view, like, comment and share counts; 780 Shorts rows), YouTube search sorted by all-time views across 20 diesel and truck queries, full-stat pulls on every record holder, and the account's own `data/instagram/posts.tsv` for the two Instagram data points that matter most. 16 clips downloaded with stats JSON into this folder and run through `VIDEO/tools/watch.py` (PySceneDetect, contact sheets, Whisper); every sheet read frame by frame. Instagram counts for other people's reels are not fetchable (profile pages give alt text only, reel pages are login walled), so every third-party row is TikTok or YouTube; the two Instagram rows are Jacob's own.

Share ratio = shares (TikTok "repost_count") divided by views. YouTube does not expose shares, so Shorts rows carry likes per 1,000 views (L/kV) instead. Views are as of pull time 2026-11-21.

Folder layout: `NN-handle--slug.mp4`, matching `.info.json`, `watch-NN-handle--slug/NN-handle--slug/` with `scenes.csv`, `transcript.txt`, `sheet-NN.jpg`.

---

## 0. The headline before the table

The biggest diesel and truck short-form clips are not about diesel. They are about who you are (Ford, Ram, Chevy), what the clip lets you say to one person (send this to the buddy who does this), or a payoff you did not see coming. Pure spectacle (smoke, burnouts, cold starts) collects the most views per clip and the fewest shares per view. The single highest share ratio in the entire 4,129-row TikTok set that is a truck clip is a shop skit about energy drinks (Dirty Diesel Customs, 6.89 percent). The single highest share ratio on @elcoyotediesel is also a meme (4.05 percent, Oct 26), twenty times the next best thing on the account and eighty times the gooseneck reel that gets called "the viral one".

Triggers used below: IDENTITY (I am this kind of person), JOKE (inside joke only the tribe gets), AWE (big number, big smoke, big machine), OUTRAGE (someone did something stupid or unfair), UTILITY (I can use this), ARGUMENT (settle this), PAYOFF (something breaks, lands or flips at the end).

---

## 1. The table (69 rows)

Downloaded and frame-read clips are marked D. Hooks for rows not marked D come from the title, caption, cover or listing and are flagged (t).

### 1a. YouTube Shorts and short YouTube videos, all time, sorted by views

| # | Account | Date | Views | Likes | Com | L/kV | Len | Format | Hook (first 3 s) | The line that made it travel | Trigger |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Y1 | WhistlinDiesel | 2022-12-24 | 35.8M | 1.28M | 20k | 36 | 23 s | Prank / reaction | (t) "Aggressive Bugatti Owner", a Bugatti pulls up and the owner starts shouting | A supercar owner losing it at a redneck in a truck | OUTRAGE |
| Y2 | WhistlinDiesel | 2025-08-23 | 31.5M | 202k | 8.5k | 6 | 21 s | Found-idiot repost | (t) "Absolute idiot drives away with boot on his wheel" | Title tells you exactly what you are about to watch | OUTRAGE |
| Y3 | WhistlinDiesel | 2025-08-23 | 26.9M | 517k | 4k | 19 | 8 s | Payoff | (t) "Wait for it" | Eight seconds, one payoff, loops | PAYOFF |
| Y4 | WhistlinDiesel | 2023-09-29 | 25.1M | 897k | 11k | 36 | 52 s | Destruction | (t) "Flawless G-Wagon gets Absolutely Ruined" | Expensive thing destroyed on purpose | AWE / OUTRAGE |
| Y5 | Lifted Rippers (20k subs) D | 2025-06-24 | 21.4M | 97.5k | 1.8k | 5 | 10 s | Brand identity test | Woman in front of a Super Duty with the hood up, label "GUESSING THE TRUCK BY THE SOUND OF THE HOOD" | Three hood slams labelled FORD, RAM, CHEVY (with a sick emoji on Chevy) | IDENTITY / ARGUMENT |
| Y6 | Tatum Maciejack (74.5k subs) D | 2026-01-10 | 18.1M | 185k | 4.2k | 10 | 61 s | Persona plus truck | Girl with a slushie walks up to a Holley-wrapped squarebody race truck at a 7-Eleven at night | Caption "went viral for no reason", which is the reason: pretty girl, rough race truck, no explanation | IDENTITY / AWE |
| Y7 | Dick Industries (112k) | 2023-11-23 | 18.0M | 209k | 1.2k | 12 | 59 s | Rust repair satisfying | (t) C10 short-bed conversion rust repair, cut and weld | Before and after metalwork, the "deadwood" shop tag | UTILITY / AWE |
| Y8 | joey25019 (21k) D | 2011-09-13 | 17.3M | 51.8k | 4.1k | 3 | 73 s | Lope and smoke | Horizontal phone clip of a lifted 6.0 Super Duty idling in a driveway, camera walks to the tailpipe | The oldest clip in the set; fifteen years of people searching "6.0 Powerstroke" land on it. Description is the mod list | AWE |
| Y9 | Oversteer (204k) D | 2026-01-06 | 15.8M | 533k | 5.7k | 34 | 119 s | Narrated fix with a story | Under a squarebody, drip visible, VO "So I saw some dripping under my truck and I thought, oh that's just the AC. Wait, this truck doesn't have AC" | Grandfather's farm truck, rusted tank, dog gets into the Mountain Dew, "she's back" | PAYOFF / IDENTITY |
| Y10 | bigtractorpower (948k) | 2024-11-03 | 15.1M | 189k | 2.7k | 12 | 22 s | Work footage | (t) F-250 plowing a field | A pickup doing a tractor's job | AWE |
| Y11 | Freedom Syndicate (403k) D | 2025-09-09 | 13.3M | 241k | 11k | 18 | 54 s | Tug of war | Static wide of a black F-250 Platinum chained to a squarebody, man walking back to the Ford, VO "I'ma take that square body right back to the junkyard where it belongs" | Trash talk, then the squarebody smokes the tires and the Ford goes nowhere | ARGUMENT / PAYOFF |
| Y12 | DieselSellerz (157k) | 2013-04-02 | 7.53M | 33k | 1.6k | 4 | 162 s | Prank | (t) "Twin Turbo Cummins PRANK! #DieselDave Rolls Coal!" | The rolling coal prank template everyone copied for a decade | OUTRAGE / JOKE |
| Y13 | Tom's Refurb | 2025-08-05 | 6.49M | 85k | 708 | 13 | 18 s | Understatement plus noise | (t, TikTok twin is D as T31) "Just A Little 331 Stroker" | The title undersells, the sound oversells | AWE / JOKE |
| Y14 | WhistlinDiesel | 2025-09-24 | 5.46M | 75.7k | 3.4k | 14 | 15 s | Absurd bit | (t) "Harvesting season is here! That means Ferraris are being harvested" | Farm equipment vs supercar, the WD formula in one line | JOKE / AWE |
| Y15 | aguyfromalabama (48.7k) | 2024-10-21 | 3.2M | 22k | 1.8k | 7 | 151 s | Wife reaction | (t) "My wife's reaction to Triple Turbo Duramax" | The "my wife said" format with a real wife and a real truck | JOKE / IDENTITY |
| Y16 | Tom's Refurb | 2025-12-23 | 2.23M | 43.9k | 2.4k | 20 | 21 s | Self-promo as a bit | (t) "Me, OMW to watch my most recent INSANE YouTube video" | The promo is a joke about promos | JOKE |
| Y17 | SquareBody Shelley (36.6k) | 2026-09-25 | 1.66M | 9.2k | 234 | 6 | 13 s | Money-pain meme | (t) "When your buddy just cost you 6k" | A number and a feeling every builder has had | JOKE / IDENTITY |
| Y18 | Camm Fisher (33.7k) | 2026-08-10 | 1.58M | 18k | 251 | 11 | 15 s | Reveal of a flaw | (t) "Good from far but far from good" on a C10 paint job | Self-deprecating reveal | JOKE |
| Y19 | SquareBody Shelley | 2026-07-05 | 1.24M | 22k | 1.4k | 18 | 50 s | Persona | (t) "Just doing Burbtha things" | A named truck with a personality | IDENTITY |
| Y20 | Inside Edition (13.8M) | 2021-10-20 | 1.13M | 30.6k | 4.8k | 27 | 86 s | News on outrage | (t) Rolling coal into a Whataburger | The clip that made "rolling coal" a national news phrase | OUTRAGE |
| Y21 | Vice Grip Garage | 2024-04-27 | 861k | 27.7k | 549 | 32 | 24 s | Shade-tree how-to gag | (t) "How to use a back cherry picker" | Redneck engineering with a straight face | JOKE / UTILITY |
| Y22 | Vice Grip Garage | 2024-04-20 | 851k | 82k | 2.3k | 96 | 35 s | Identity bit | (t) "How Country Boys Drive a Chevelle" (gravel) | Names the viewer in the title | IDENTITY |
| Y23 | JMR Rebuilders | 2025-10-07 | 747k | 6.2k | 229 | 8 | 11 s | Cheap fix | (t) "Turbo Can Clear Coat!" rattle can | $10 product on a truck, 11 seconds | UTILITY / JOKE |
| Y24 | JMR Rebuilders | 2025-09-09 | 567k | 7.3k | 190 | 13 | 10 s | Price hook | (t) "$600 FACEBOOK Marketplace Truck!" | A price in the title | UTILITY / AWE |
| Y25 | Whitt_Built (107k) | 2021-05-22 | 518k | 4.7k | 585 | 9 | 62 s | Dyno failure | (t) "Power Driven Diesel Dyno Explosion @ UCC 2021" | The only UCC clip with real Shorts numbers; it is the one that blew up | PAYOFF / AWE |
| Y26 | Matt's Off Road Recovery | 2024-11-05 | 180k | 3.8k | 39 | 21 | 28 s | Recovery | (t) "Chevy Truck Goes Over A Cliff!" | Best Short of a 1.2B-view channel is still under 200k; the format lives in long-form | AWE |

### 1b. TikTok, all time, sorted by views (shares visible)

| # | Account | Date | Views | Likes | Com | Shares | Share % | Len | Format | Hook (first 3 s) | The line that made it travel | Trigger |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T1 | @cleetusmcfarland | 2023-05-03 | 28.1M | 1.5M | 4.6k | 64.2k | 0.23 | 15 s | Burnout spectacle | (t) "We are ready for INDY" huge burnout | Biggest smoke in the set, lowest share rate of the top ten | AWE |
| T2 | @westengw D | 2021-02-23 | 19.5M | 2.7M | 6.6k | 9.0k | 0.05 | 11 s | Comment reply tease | Crated Hellcat engine, label "1500hp Cop Car!" plus the pinned comment "are you really going to do it", pan to a white Charger pursuit car | "You're new here aren't you? You better follow and stay along." A follow ask that works because it is a dare | AWE / PAYOFF (promised) |
| T3 | @cleetusmcfarland D | 2023-06-26 | 12.4M | 1.4M | 2.8k | 185.5k | 1.50 | 11 s | Fail payoff | Driver in a helmet in a race car, text "My seat couldn't handle the boost" | The seat back snaps on launch, he keeps going. 185k shares, the most shares of any truck or car TikTok in the set | PAYOFF / JOKE |
| T4 | @westengw | 2024-04-17 | 12.1M | 1.4M | 6.1k | 109.7k | 0.91 | 38 s | Dyno number | (t) "Today we find out what a Demon motor will do in a TRX" | A question with a number at the end | AWE / PAYOFF |
| T5 | @westengw | 2022-05-29 | 11.2M | 1.4M | 2.3k | 14k | 0.13 | 38 s | Blow-up | (t) "4 months to build 4 mins to blow up" | The caption is the whole joke | PAYOFF |
| T6 | @zac.lucarz D | 2026-08-17 | 9.8M | 394k | 3.4k | 7.9k | 0.08 | 68 s | Trend-jack explainer | Kid holding a NASCAR boom tube in front of a Ram, label "Putting BOOM TUBES On My Diesel Truck", VO at 0.0 s | "I want to be the first one to put boom tubes on a diesel." Rides a car-TikTok trend into the truck lane | AWE / JOKE |
| T7 | @westengw D | 2024-04-19 | 9.7M | 849k | 2.4k | 26.4k | 0.27 | 50 s | Cold start | Westen in a sherpa jacket, label "1500hp Diesel Mustang Cold start", "Guys you want to see what it looks like to cold start a 1500 horsepower diesel Mustang after it's been sitting outside in 20 degree weather" | The number plus the weather plus the begging ("come on baby, breathe the life for me") | AWE |
| T8 | @westengw | 2024-08-12 | 9.6M | 1.2M | 12.8k | 27.9k | 0.29 | 48 s | Expectation set | (t) "Well maybe not a 1000hp but I think she will still rip" | Public self-correction, 12.8k comments | PAYOFF / ARGUMENT |
| T9 | @westengw | 2021-03-19 | 8.4M | 860k | 3.0k | 1.5k | 0.02 | 31 s | Announcement | (t) "I bought a broken Hellcat. Who wants to see a 4x4 Hellcat?" | Pure watch, near zero send | AWE |
| T10 | @westengw | 2021-04-14 | 6.1M | 655k | 1.9k | 14.3k | 0.23 | 14 s | Smoke | (t) "it's spring and the Smoke-stang is ready to party" | Signature car doing its signature thing | AWE |
| T11 | @tomsrefurb D | 2025-08-05 | 5.0M | 357k | 1.0k | 14.1k | 0.28 | 18 s | Understatement plus noise | Tom leaning out a white '65 Mustang window, then a greasy finger on a toggle panel (FP, FAN, ACC), key turn | Caption "Just a little 331 stroker", the tach swings, the tailpipe shot, the car idles under a tree. One spoken word | AWE / JOKE |
| T12 | @darkirondiesel D | 2023-10-08 | 4.5M | 713k | 5.4k | 161.4k | 3.59 | 17 s | Culture-war identity meme | Protester with a megaphone, "I only realized this a couple of days ago and I've only come out to a few people" | Hard cut to white block letters MY TESLA on black, then a lifted black Ram rolling coal. 161k shares, one of the three highest in the set. Noted for what it is: an outgroup joke; not a format for this account | IDENTITY / OUTRAGE |
| T13 | @westengw | 2023-06-13 | 4.4M | 528k | 2.3k | 136.2k | 3.10 | 42 s | Vote prompt | (t) "What should we do next with the Ford Ranger tank?" | An open question on an absurd object, 136k shares | ARGUMENT |
| T14 | @cleetusmcfarland | 2023-07-08 | 4.1M | 521k | 1.9k | 45.1k | 1.10 | 16 s | Surprise claim | (t) "This truck is insane!!! Bone stock #RaptorR" | "Bone stock" is the argument | AWE / ARGUMENT |
| T15 | @davesautocenter | 2025-09-25 | 3.9M | 192k | 1.9k | 24.7k | 0.63 | 78 s | Money utility | (t) "Save Over 10k on your Diesel Truck" | A dollar figure in the first line | UTILITY |
| T16 | @dieselpowerproducts D | 2026-09-28 | 3.7M | 36.6k | 668 | 29.6k | 0.80 | 5 s | Deadpan wrong fix | Drill bit going into a dash cluster at the check-engine light, host face in the lower-left corner, "Quick and easy way to get rid of your check engine light" | "There you go, problem solved." Five seconds, loops | JOKE / PAYOFF |
| T17 | @darkirondiesel | 2025-07-12 | 3.6M | 132k | 326 | 6.8k | 0.19 | 33 s | Flex | (t) "Keeping the ladies happy" 12 valve | Innuendo title on a 5th gen | JOKE |
| T18 | @cleetusmcfarland | 2023-07-06 | 3.1M | 283k | 1.2k | 39k | 1.26 | 25 s | Call-out | (t) "Sorry Ford gotta call you out" | Picking a fight with a brand | ARGUMENT / OUTRAGE |
| T19 | @davesautocenter | 2025-05-01 | 3.0M | 119k | 3.7k | 2.8k | 0.09 | 64 s | Forensics | (t) 6.7 Cummins free-spins with no compression | Mystery failure; watched, not sent | UTILITY |
| T20 | @davesautocenter | 2025-09-17 | 2.9M | 149k | 2.9k | 54.6k | 1.88 | 45 s | Evidence utility | (t) "DEF fluid is an interesting thing. Amazing crystals ruin the pump" | Crystals in the hand, a rule you can repeat | UTILITY |
| T21 | @davesautocenter | 2026-07-01 | 2.8M | 340k | 1.9k | 66.9k | 2.39 | 73 s | Evidence utility | (t) "Blocked Radiator = Blocked Airflow = Big Problems" | Equation title, physical proof | UTILITY |
| T22 | @zac.lucarz | 2025-11-14 | 2.4M | 212k | 1.0k | 8.3k | 0.34 | 63 s | Fake news bit | (t) "Whistlindiesel arrested for tax evasion" | Borrowed name, fake headline | JOKE / OUTRAGE |
| T23 | @zac.lucarz | 2026-08-13 | 2.3M | 257k | 3.5k | 36.5k | 1.59 | 67 s | Scarcity utility | (t) "Get this spray before they stop selling it completely" | "Before they stop selling it" is the send line | UTILITY |
| T24 | @davesautocenter | 2025-05-09 | 2.1M | 80.3k | 343 | 2.4k | 0.11 | 112 s | Build | (t) "7.3 Ford Power Stroke Engine Build with Bob the Builder" | A 7.3 build on a 1M-follower account shares at 0.11 percent | AWE |
| T25 | @davesautocenter D | 2026-09-25 | 2.0M | 178k | 9.0k | 823 | 0.04 | 89 s | Mentor story | Dave at a bench, "Apparently the rumors are there's some young man that's trying to do a 7.3 for himself in a truck", cut to the parents, cut to the 17-year-old at his block | "Does the guy need my help? Put it in the comments." 9k comments, 823 shares: a comment format, not a share format | IDENTITY (7.3) / STORY |
| T26 | @fassfuelsystems | 2025-07-16 | 1.6M | 6.4k | 56 | 345 | 0.02 | 71 s | Brand explainer | (t) "FASS stands for Fuel Air Separation System" | 1.6M views bought or boosted; 345 shares. Nobody sends an explainer | none |
| T27 | @fassfuelsystems D | 2026-05-12 | 1.5M | 149k | 148 | 9.4k | 0.63 | 50 s | Feature build | Rusty 1950 Chevy 3600 wrecker in a field of wildflowers, black smoke rolling at 0.0 s, no text for 4 s | Host in the corner at 0:04, "Brown Bros Garage does not miss", spec list in word-by-word captions | AWE |
| T28 | @c10talk | 2022-01-02 | 1.2M | 84.8k | 1.0k | 5.9k | 0.49 | 51 s | Tech tip | (t) "Tech tip on those worn out Nader pins, cheap fix" | A specific cheap fix for a named platform | UTILITY |
| T29 | @dieselpowerproducts | 2026-11-01 | 643k | 31.7k | 1.2k | 13.7k | 2.13 | 52 s | Tribe news | (t) "Did you know about this?" | The question that implies the viewer missed something | UTILITY / JOKE |
| T30 | @fassfuelsystems | 2025-12-04 | 697k | 71.8k | 768 | 22.1k | 3.17 | 63 s | Rumor | (t) "Is Ford dropping a 8.0 Powerstroke in 2027?" | Rumor as a question; the Powerstroke tribe argues and sends | ARGUMENT / UTILITY |
| T31 | @tomsrefurb D | 2025-11-27 | 885k | 101k | 475 | 56.3k | 6.36 | 19 s | Inside joke | Teenager in a Dr Pepper shirt polishing a quarter panel, one locked shot, small lower-third caption "TF is my detailer doing?" | He keeps saying "oh my god" and the polisher never touches the paint. 6.36 percent shares: everyone has that employee | JOKE / IDENTITY |
| T32 | @squarebodysyndicate | 2023-01-04 | 674k | 67.6k | 1.5k | 13.7k | 2.03 | 50 s | Named build | (t) "Our old Cummins swapped 1973 Chevy Cheyenne Super 20" | Platform name plus swap name in line one | IDENTITY / AWE |
| T33 | @fassfuelsystems | 2026-09-21 | 855k | 46.7k | 558 | 9.3k | 1.09 | 26 s | Breaking news | (t) "BREAKING: The 8.3 liter MONGOOSE Duramax is coming!" | "BREAKING" plus a nickname | UTILITY / AWE |
| T34 | @bigtruckbigrv | 2026-02-07 | 667k | 25.1k | 264 | 12.3k | 1.84 | 426 s | Tour | (t) Spacecraft RV walkthrough, 7 minutes | Long-form tour that gets sent to a spouse | AWE / UTILITY |
| T35 | @whambaamteslacam | 2024-09-07 | 343k | 21.2k | 897 | 3.4k | 0.98 | 75 s | Dashcam outrage | (t) "Pickup truck roll coal on Tesla" | Tesla cam footage of a coal roll, posted by the Tesla side | OUTRAGE |
| T36 | @zac.lucarz | 2026-03-13 | 890k | 103k | 468 | 25k | 2.81 | 60 s | Wish | (t) "This with the matching Super Duty" | Send-to-spouse wish post | IDENTITY |
| T37 | @fassfuelsystems | 2026-04-02 | 274k | 9.4k | 1.1k | 14.5k | 5.28 | 7 s | Vote | (t) "Who's it going to be?" | Seven seconds, a choice, 1.1k comments and 5.28 percent shares | ARGUMENT |
| T38 | @fassfuelsystems | 2025-11-06 | 295k | 10.7k | 135 | 10.4k | 3.53 | 5 s | Tag-a-friend joke | (t) "Your short friends owe you a FASS Fuel System" | A product joke written as a tag line; 3.53 percent on a brand page | JOKE |
| T39 | @dirtydieselcustoms D | 2025-11-14 | 181.5k | 25.5k | 159 | 12.5k | 6.89 | 55 s | Nature-doc skit | Wide shot of two techs in a shop, deadpan Attenborough VO "The auto mechanic is a mysterious creature seen daily in shops across the country" | Every beat is a mechanic opening another energy drink; "Seriously, how many of these do they go through a day?" Highest share rate of any truck clip in the set | JOKE / IDENTITY |
| T40 | @dirtydieselcustoms | 2025-07-14 | 164k | 16.6k | 136 | 5.3k | 3.22 | 15 s | Warning | (t) "Anywhere but in your truck! The CP4 is a problematic fuel injection pump" | Names the part everyone fears | UTILITY / OUTRAGE |
| T41 | @zac.lucarz | 2025-12-17 | 109k | 15.6k | 45 | 3.3k | 3.02 | 73 s | Gift-season bit | (t) "Which one do you think she'll get you" | Tag-your-wife format | JOKE / IDENTITY |
| T42 | @zac.lucarz | 2024-01-04 | 463k | 48k | 454 | 1.0k | 0.22 | 64 s | Compilation | (t) "Diesel trucks that roll the most coal" | Compilation gets watched, not sent | AWE |
| T43 | @darkirondiesel | 2022-12-04 | 224k | 20.5k | 140 | 226 | 0.10 | 35 s | Cold start | (t) Cold start at minus 21 C, not plugged in | Classic cold start: 0.10 percent shares | AWE |
| T44 | @rust_ridge_ranch26 | 2026-08-10 | 451k | 28.9k | 1.6k | 3.7k | 0.81 | 64 s | Persona | (t) "42" (her best clip; the IDI clips sit at 40k) | Persona beats the truck on her own page | IDENTITY |
| T45 | @mattsoffroadrecovery | 2021-02-23 | 286k | 28.3k | 122 | 141 | 0.05 | 57 s | Call-out | (t) "So we got a call! Pt 1" | Best TikTok of a 1.2B-view YouTube channel | AWE |
| T46 | @justin_danger_nunley | 2026-10-13 | 8.9M | 325k | 4.7k | 576.4k | 6.48 | 46 s | Comedy | (t) "Oh...." | The SEMA S10 guy's biggest clip of the quarter, 576k shares, not about the truck | JOKE |

### 1c. Instagram, the account's own two record posts (from `data/instagram/posts.tsv`)

| # | Post | Date | Views | Reach | Likes | Com | Shares | Saves | Share % | Avg watch | Skip | Format | Why it travelled |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I1 | @elcoyotediesel "Yo! Where the 10 mil @?!" | 2026-10-26 | 506,827 | 418,248 | 65,924 | 111 | 20,552 | 3,789 | 4.05 | 7.9 s | 38.6% | Meme (IG alt text: "a meme of car, wheel, windshield, blower and text"), pinned first on the grid | A joke about money that is not there, told over a truck image. 4.05 percent shares puts it in the same bracket as Nunley, Tom's Refurb and DDC above. This is the account's actual viral reel now, 28 percent more views than the gooseneck and 1,580 times the shares |
| I2 | @elcoyotediesel "Well it seemed like a good idea..." (gooseneck) | 2026-07-24 | 396,640 | 250,833 | 1,584 | 41 | 13 | 53 | 0.003 | 27.3 s | 20% | Hotshot trailer fail, long hold | Watched to the end (27 s average, 20 percent skip, the best hold on the account) and sent by nobody. Pure AWE/PAYOFF with no line to send it with |

Not verifiable but worth knowing: trend trackers put the most-viewed truck Reel of 2026 at 336.7M (a truck driver lip-sync from the cab, @cio0061, July 2026). Every source repeats the same number from the same blog, so treat it as unconfirmed. If true it is the extreme case of the pattern: the cab is the set, the driver is the content, the truck is irrelevant.

---

## 2. The ten strongest, read frame by frame

Ordered by what they teach, not by views. Files and watch folders named in each.

### 1. Lifted Rippers, "If you really own it, you should know" (Y5). 21.4M views on a 20k-sub channel
`01-liftedrippers--if-you-really-own-it.mp4`, 10 s, 608x1080, 3 scenes.
- Structure: three static medium shots of the same woman in a black work shirt, each in front of a different truck with the hood up. 0:00 to 2.6 s Super Duty, label "GUESSING THE TRUCK BY THE SOUND OF THE HOOD" at the top, she drops the hood; 2.6 to 5.6 s Ram, label "RAM"; 5.6 to 9.6 s Chevy in a shop, label "CHEVY" with a nauseated emoji. The brand label lands after each slam.
- Sound: the hood slams, nothing else. Whisper heard "Ford, Ram, Chevy" spoken quietly under the slams.
- Text: one white italic bold label, top centre, no pill, changes per truck.
- Ending: on the Chevy label. No wrap, loops straight back to the first slam.
- Why it travelled: it is a test the viewer takes ("I'd know my truck's hood anywhere"), and a brand ranking the viewer can disagree with. The emoji on Chevy is the fight starter. 1,800 comments on 97k likes. Ten seconds, so a viewer watches twice while deciding.
- For Rival: the sound-identity test. Three doors, three hoods, three starters, three tailgates, labelled 7.3, 6.0, 6.7, or 1959 vs 2011.

### 2. Tatum Maciejack, "Throwback to this video that went viral for no reason" (Y6). 18.1M
`02-tatummaciejack--went-viral-for-no-reason.mp4`, 61 s, 2 scenes.
- Structure: 0:00 to 40.8 s one handheld shot following a young woman with a slushie as she walks the length of a Holley-wrapped, slammed squarebody race truck ("Rooster", number 29) at a 7-Eleven at night, opens the door, climbs in; 40.8 to 60.9 s second shot from outside the driver's window, she pulls the wheel, looks at camera, the truck idles.
- Sound: ambient, a few words ("Rooster's happy, give him a full tank"), loud idle.
- Text: none. No caption on screen at all for 61 seconds.
- Ending: she looks at the camera and the clip ends mid-idle.
- Why it travelled: a person and a truck that do not match expectations, no explanation offered, and a title that refuses to explain it. Her own November posts of the same truck do 2k to 19k; the throwback did 18.1M on YouTube. Persona plus mystery, zero production.
- For Rival: an unexplained walk-up to the '59 at night, one take, with nothing on screen, is a legitimate format. The caption does the understating.

### 3. Oversteer, "Make sure this doesn't happen to your square body" (Y9). 15.8M, 533k likes
`03-oversteer--squarebody-dont-let-this-happen.mp4`, 119 s, 49 scenes (average 2.4 s, the back half under 1 s).
- Structure: cold open under the truck on a drip, VO joke in the first 4 s ("that's just the AC... this truck doesn't have AC"). 0:14 the leaking tank. 0:20 one wide of two squarebodies and a line that turns a repair into a story: "My grandfather passed about six years ago and this was his truck." Then the old tank in the bed (rust hole, finger in it), new tank, Rust-Oleum, bolts, cut hoses, dog eats the Mountain Dew, carb primed, "She's back."
- Sound: voiceover the whole way, shop sounds under, no music.
- Text: white sans captions of the VO, lower third, present in the first 20 s, then sparse.
- Ending: "She's back. Right, buddy," to the dog. No CTA.
- Why it travelled: the title is a warning to a named tribe, the open is a joke, the twentieth second is a grandfather, and the rest is competence with a dog. It is Dave's forensics with a heart.
- For Rival: the one build-process format in the set with eight figures of views. The story line at 0:20 is the lesson: the truck's history goes in the first third, not the caption.

### 4. Freedom Syndicate, "Chevy Square Body vs Ford F250 Tug of War" (Y11). 13.3M, 11k comments
`04-freedomsyndicate--squarebody-vs-f250-tug.mp4`, 54 s, 3 scenes.
- Structure: one phone camera on a lawn. 0:00 to 19 s a man walks from the squarebody back to a black F-250 Platinum saying "I'ma take that square body right back to the junkyard where it belongs. Do you hear me, Mom?" 19 to 33 s the trucks tension the chain, the Ford squats, the squarebody lights the tires. 33 s to the end the squarebody vanishes in its own tire smoke and the Ford is dragged.
- Sound: real. Trash talk, then engines, then tires.
- Text: none.
- Ending: smoke fills the frame, cut.
- Why it travelled: the trash talk is a bet the viewer takes a side on, new truck vs old truck is a brand war and a generation war at once, and the payoff is visible from space. 11,000 comments.
- For Rival: the Ford vs Chevy argument is still the most reliable fight on the internet. Rival is a Ford on a Ford frame; the argument it can own is old vs new, not brand vs brand.

### 5. Westen Champlin, "Reply to @memphiscatron: are we really building a 1500hp cop car" (T2). 19.5M, 2.7M likes
`05-westengw--1500hp-cop-car-reply.mp4`, 11 s, 2 scenes.
- Structure: 0:00 to 4 s pan across a crated Hellcat crate engine to a white Charger pursuit car in the shop, the TikTok comment-reply sticker in the upper left ("are you really going to do it") and a white label "1500hp Cop Car!" above it; 4 to 11 s Westen's face, laughing, then straight to lens: "You're new here aren't you? Well you better follow and stay along."
- Sound: his voice only.
- Text: the pinned comment and one label, both gone when the face arrives.
- Ending: on the dare. The follow ask is the punchline, not an outro.
- Why it travelled: the reply format makes the audience the co-author; the engine and the car are shown before any talking; the ask is written as a flex. 2.7M likes on 9k shares (0.05 percent): a watch-and-follow format, not a send format.
- For Rival: the comment-reply tease is the right way to answer "is this thing ever getting done". Show the part, read the doubt, dare them to stay.

### 6. Cleetus McFarland, "Old seat couldn't handle the freedom" (T3). 12.4M, 185.5k shares (1.50 percent)
`07-cleetus--old-seat-couldnt-handle-freedom.mp4`, 11 s, 2 scenes.
- Structure: 0:00 to 6 s in-car camera, helmeted driver staging; at about 2 s the seat back collapses and he goes flat, arms up; 6 to 11 s exterior pan of the white Nova leaving.
- Sound: VO "My seat couldn't handle the boost... oh my god!" plus the car.
- Text: one small white two-line caption, top centre, "My seat couldn't handle the boost," on for the full clip.
- Ending: on the car pulling away through the frame.
- Why it travelled: the fail happens inside the first three seconds and he keeps racing. 185k shares is the largest share count of any truck or car clip in this set. People send fails to the person who would do the same thing.
- For Rival: when something lets go (a jack, a stand, a seat, a chain), the clip is the first 3 s plus the recovery. Post it the same day.

### 7. Diesel Power Products, "Problem solved" (T16). 3.7M, 29.6k shares, posted Sep 28 2026
`10-dieselpowerproducts--problem-solved.mp4`, 5 s, 1 scene.
- Structure: a single phone shot of a cordless drill boring into a dash cluster exactly where the check-engine light is, the host's face keyed into the lower-left corner, the light goes out at 4 s.
- Sound: VO, "Quick and easy way to get rid of your check engine light. There you go, problem solved." Drill under it.
- Text: none.
- Ending: on the dead light. Loops at 5 s, so one "view" is three plays.
- Why it travelled: the shortest clip in the set, a joke every diesel owner has made, a face in the corner to make it a person's joke. 0.80 percent shares at 3.7M views on a parts-store account whose other November posts do 500 to 45k.
- For Rival: the five-second deadpan fix. Rival's first owner-fixes are an endless supply.

### 8. Tom's Refurb, "He's a hard worker" (T31). 885k views, 56.3k shares (6.36 percent)
`15-tomsrefurb--hes-a-hard-worker.mp4`, 19 s, 1 scene.
- Structure: one locked phone shot of a teenager in a Dr Pepper shirt kneeling at a black quarter panel with a polisher. He talks, gestures, turns the polisher on and off, never actually polishes.
- Sound: ambient, the polisher spinning, "Oh my god. Oh. Oh my god."
- Text: one small lower-third caption, "TF is my detailer doing?", on for the whole clip.
- Ending: he leans out of frame, cut.
- Why it travelled: 6.36 percent shares, the third highest in the set. Everyone has worked with this kid, and the caption is the exact text you would send with it. A joke about a person on the team, with the team member in on it.
- For Rival: Jacob has no employees, but he has a dad, a buddy with a trailer, Vinny on the phone, and himself at 11 pm. Point the camera at the person being useless and caption it as a complaint.

### 9. Dirty Diesel Customs, "Looks like we need an energy drink sponsor" (T39). 181.5k views, 12.5k shares (6.89 percent)
`13-dirtydieselcustoms--energy-drink-sponsor.mp4`, 55 s, 18 scenes.
- Structure: a nature documentary about mechanics. Wide of two techs talking at a bare chassis, then a tech at a parts cart cracking a can, a tech under a hood with a can, a tech at a vise with a can, the lunch-room fridge, "it's really time to put the hammer down... or not." Every scene change lands on another can.
- Sound: a deadpan Attenborough voiceover, shop ambience under.
- Text: none.
- Ending: on the question, "Seriously, how many of these do they go through a day?"
- Why it travelled: the highest share rate of any truck clip in 4,129 rows. It is an inside joke that names a tribe (mechanics), is harmless to send to a mechanic, and the caption ("Looks like we need an energy drink sponsor") turns it into a pitch the audience makes for the shop. The same shop's install reels do 300 views on Shorts.
- For Rival: the skit grammar for a one-man account is a nature doc about the builder. "The one-man truck builder is a nocturnal creature. He has three projects and finishes none of them."

### 10. Dave's Auto Center, "A 17 year-old and a 7.3 L. Who knows the story on this?" (T25). 2.0M, 9,029 comments, 823 shares
`09-davesautocenter--17-year-old-and-a-73.mp4`, 89 s, 14 scenes.
- Structure: Dave at the bench, static, "Apparently the rumors are there's some young man that's trying to do a 7.3 for himself." 0:07 cut to the kid's parents at the shop (captions on), 0:13 the kid's camshaft, 0:16 the kid at his own block, "I've been watching Dave's videos for a long time," 0:21 back to Dave for the rest.
- Sound: talk only.
- Text: white lower-third captions on the inserts, none on Dave.
- Ending: "It reminds me of me, 50 plus years ago." Comments asked to decide whether he should help (the follow-up, "20,000 people told me to help this young engine builder," did 1.1M three days later).
- Why it travelled: a 7.3 and a kid are the two most sympathetic objects in the diesel audience, and the clip asks the audience to vote on a kindness. 9,029 comments on 823 shares (0.04 percent): the audience talked to Dave instead of sending it to each other. The two-part structure (ask, then deliver) is the thing to copy, not the share rate.
- For Rival: the "should I" question gets comments; the deliver clip gets views. Pair them.

### Six more, read and worth a paragraph each

- **Westen, Smokestang cold start (T7)**, `06-westengw--easiest-cold-start-smokestang.mp4`, 50 s, 7 scenes. Label "1500hp Diesel Mustang Cold start" on from frame 1 for 7 s over his face, then engine bay, then four long holds (13.5 s, 10.4 s, 10.4 s) on the hood-open front three-quarter while it cranks, smokes and catches. Talking the whole way ("come on baby, breathe the life for me"). 9.7M and 0.27 percent shares: cold starts are a view format. The number in the label is what makes it a 1500hp cold start and not a cold start.
- **Zac Lucarz, boom tubes (T6)**, `11-zaclucarz--roa-look-what-you-started.mp4`, 68 s, 17 scenes. Label "Putting BOOM TUBES On My Diesel Truck" for 2 s, then word-by-word white karaoke captions in bold italic caps (GUYS, CRAZY, ON, TIKTOK), a 1 s meme insert of the car-TikTok trend, then him explaining to camera with the part in his hands. Trend-jack from the car side into the truck side, 9.8M and 0.08 percent shares. The "I want to be the first one to do X on a diesel" line is the hook.
- **Tom's Refurb, 331 stroker (T11)**, `12-tomsrefurb--just-a-little-331-stroker.mp4`, 18 s, 6 scenes. Face out the window (1.1 s), toggle panel with greasy finger (3.2 s), key (1.9 s), tach (2.5 s), tailpipe (3.6 s), rear three-quarter under a tree held 5.9 s while it idles. No text. One spoken word. 5M on TikTok, 6.5M on Shorts. This is the "it runs" recipe: switch, key, tach, pipe, wide.
- **FASS, Brown Bros 1950 Chevy 3600 (T27)**, `14-fassfuelsystems--cummins-swapped-chevy-3600.mp4`, 50 s, 9 scenes. 4 s of a rusty wrecker rolling coal in a field of wildflowers with no text, then the host keyed into the top-left with a red-and-white "BROWN BROS GARAGE 1950 CHEVY 3600" headline, then karaoke captions with the key words in red while the camera orbits the truck (a 15 s hold, then a 9.5 s hold). Brand mention is one clause. 1.5M, 0.63 percent. The named-shop feature travels; the brand explainer (T26) does not.
- **Dark Iron Diesel, "If she can do it so can I" (T12)**, `08-darkirondiesel--if-she-can-do-it.mp4`, 17 s, 8 scenes. Found footage of a protester with a megaphone for 7.7 s, a black card with MY TESLA in white block caps, then seven cuts of a lifted black Ram rolling coal, 0.7 to 2.6 s each. 3.59 percent shares, 161k sends. Logged because it is one of the three highest share rates in the set and shows the mechanism (an outgroup setup, a one-word reversal, then the truck as the punchline). It is a culture-war post and not a format for an account that wants brand partners.
- **joey25019, "6.0 Powerstroke lope and smoke" (Y8)**, `16-joey25019--60-powerstroke-lope-and-smoke.mp4`, 73 s, horizontal 720p, 1 scene, no speech. A 2011 driveway clip, camera walks around a lifted Super Duty and parks at the tailpipe. 17.3M views over fifteen years, 3 likes per thousand views. It is the search result for "6.0 Powerstroke", not a reel. Lesson: an exact platform name in the title is a fifteen-year annuity on YouTube.

---

## 3. What the top ten percent share

Measured on the 412 TikTok rows in the top view decile (threshold about 650k views), plus the 26 Shorts record holders, plus the 16 frame-read clips.

1. **Trigger mix.** Of the 46 TikTok rows in the table, the trigger counts are IDENTITY 14, JOKE 16, AWE 20, UTILITY 13, ARGUMENT 8, OUTRAGE 7, PAYOFF 9 (multi-tagged). Sorting by share ratio instead of views flips it: of the 15 rows above 2 percent shares, 11 are JOKE or IDENTITY, 5 are ARGUMENT or UTILITY, and exactly one is AWE (the Westen Ranger tank vote, which is an ARGUMENT dressed as AWE). Nothing above 2 percent is a cold start, a burnout, a dyno pull or a walkaround.

2. **Length.** Top-decile average length is 60 s because the Dave's and Nunley talk clips pull it up. The share-rate leaders are short: of the 15 rows above 2 percent, 9 are 20 s or under (5, 7, 5, 10, 13, 15, 17, 19 s). By length bucket across all 1,163 rows over 100k views, the 31 to 60 s bucket has the best average share rate (0.62 percent) and the 0 to 15 s bucket the most views (1.1M average). Read it as two jobs: under 15 s for reach, 30 to 60 s for sends, and under 10 s for a loop (DPP 5 s, FASS 5 s and 7 s, WD "Wait for it" 8 s).

3. **Sound.** 12 of the 16 frame-read clips use original sound (voice or machine) and no music. The four exceptions are the Dark Iron meme (sound bite plus cut), Lifted Rippers (hood slams only), the 2011 lope clip (engine only) and Tom's 331 (engine only). Every voice clip has the first word inside 0.0 to 0.9 s. There is not one trending-audio clip in the top ten of either platform.

4. **Text.** 8 of 16 have no burned text at all (Tatum, Freedom Syndicate, Oversteer after 0:20, DDC, Tom's 331, DPP, joey, Dave's on Dave). Where text exists it is one label, top centre or lower third, 3 to 8 words, set on frame 1 and left alone (Cleetus "My seat couldn't handle the boost", Westen "1500hp Diesel Mustang Cold start", Lifted Rippers "GUESSING THE TRUCK BY THE SOUND OF THE HOOD", Tom's "TF is my detailer doing?"). The two karaoke-caption clips (Zac, FASS) are the two polished brand-style clips, and both share under 1 percent.

5. **Cut rate.** Share leaders are one or two shots (Tom's hard worker 1, DPP 1, Cleetus 2, Lifted Rippers 3, Freedom Syndicate 3). View leaders with stories cut every 2 to 3 s (Oversteer 49 scenes in 119 s, DDC 18 in 55 s). Nobody above 1 percent shares cuts faster than 1 s per shot. The throtl-style 1 s walkaround does not appear in the all-time list at all.

6. **How they end.** 14 of 16 end on the payoff frame or the last spoken word with no outro: smoke fills frame (Freedom Syndicate), the light goes out (DPP), the kid leans out of frame (Tom's), "She's back" (Oversteer), the dare ("you better follow", Westen), the question ("how many of these do they go through", DDC; "put it in the comments", Dave's). Two end on a static hold of the vehicle idling (Tom's 331, Tatum). Zero fades, zero end cards, zero on-screen CTAs. When an ask exists it is spoken as a line of the bit.

7. **The person.** 13 of 16 have a human in frame inside the first 3 s. The three that do not (joey, Freedom Syndicate's wide, FASS's smoke open) put a voice or a truck doing something loud in frame 1 instead.

8. **The caption is the send text.** Tom's "TF is my detailer doing?", DDC "Looks like we need an energy drink sponsor", Cleetus "Old seat couldn't handle the freedom", SquareBody Shelley "When your buddy just cost you 6k", FASS "Your short friends owe you a FASS": each caption is the sentence the sender would have typed. The clip is the attachment.

9. **Brand pages win only when the brand is a clause.** FASS 8.0 rumor 3.17 percent, FASS vote 5.28 percent, FASS tag-joke 3.53 percent, DDC skit 6.89 percent, DPP deadpan 0.80 percent at 3.7M; FASS "FASS stands for" 0.02 percent, Industrial Injection build Shorts 1,200 views. Same pages, same reach, the difference is whether the product is the subject or an aside.

10. **Platform.** Same clip, Tom's 331 stroker: 5.0M TikTok, 6.5M Shorts. Same clip, DDC 3rd Gen: 75.8k TikTok, 367 Shorts. Shorts rewards exact platform names in titles (joey's 2011 clip, "7.3 obs straight pipe", "Just a slow old 7.3"); TikTok rewards the person and the joke. Instagram, from Jacob's own two data points, behaves like TikTok: the meme shared at 4.05 percent, the spectacle at 0.003 percent.

---

## 4. Formats ranked by share ratio

From the 46 TikTok rows plus the two Instagram rows, grouped by format, average of the share ratios in the group (n in brackets). YouTube rows excluded because shares are hidden.

| Rank | Format | Avg share % | n | Examples | Views it typically gets |
|---|---|---|---|---|---|
| 1 | Inside joke about the tribe (skit, caption as complaint, tag-a-friend) | 5.5 | 6 | DDC energy drink 6.89, Nunley 6.48, Tom's hard worker 6.36, @elcoyotediesel 10 mil 4.05, FASS short friends 3.53, Zac "which one she'll get you" 3.02 | 100k to 900k, occasionally 9M |
| 2 | Vote or open argument (pick one, what next, settle it) | 3.1 | 4 | FASS "who's it going to be" 5.28, Westen Ranger tank 3.10, Zac matching Super Duty 2.81, Tom's "which rig sounds best" 1.09 | 100k to 4M |
| 3 | Outgroup identity meme | 3.6 | 1 | Dark Iron 3.59 | 4.5M, and a brand problem |
| 4 | Tribe news, rumor, record number | 2.3 | 5 | FASS 8.0 rumor 3.17, FASS 2,078 hp 2.95, DDC 3rd Gen 2.25, DPP "did you know" 2.13, FASS Mongoose 1.09 | 75k to 850k |
| 5 | Warning with physical evidence | 1.8 | 5 | DDC CP4 3.22, Dave's radiator 2.39, Dave's DEF 1.88, Zac spray 1.59, Dark Iron #1 upgrade 0.82 | 160k to 2.9M |
| 6 | Fail or break with a recovery | 1.3 | 4 | Cleetus seat 1.50, Cleetus Raptor R 1.10, Cleetus "Sorry Ford" 1.26, Westen Demon TRX 0.91 | 3M to 12M |
| 7 | Named-platform build feature | 1.1 | 3 | Squarebody Syndicate '73 Cummins 2.03, FASS Brown Bros 0.63, c10talk Nader pins 0.49 | 670k to 1.5M |
| 8 | Deadpan found-fix / wrong fix | 0.55 | 4 | DPP problem solved 0.80, DPP who wants one 0.90, DPP what do you think (Nov) 0.30, DPP what do you think (Sep) 0.13 | 900k to 4.4M |
| 9 | Money utility talk | 0.36 | 2 | Dave's save 10k 0.63, Dave's 7.3 build 0.11 | 2M to 4M |
| 10 | Spectacle: smoke, burnout, cold start, compilation | 0.22 | 7 | Westen cold start 0.27, Tom's 331 0.28, Westen spring 0.23, Cleetus INDY 0.23, Zac coal comp 0.22, Dark Iron cold 0.10, Dark Iron ladies 0.19 | 200k to 28M |
| 11 | Persona story, mentor story, tease | 0.09 | 6 | Rust Ridge 0.81, Zac boom tubes 0.08, Westen cop car 0.05, Dave's 17-year-old 0.04, Matt's 0.05, Westen Hellcat 0.02 | 300k to 19M |
| 12 | Brand explainer | 0.02 | 1 | FASS "FASS stands for" | 1.6M, paid |
| 13 | Own spectacle (gooseneck) | 0.003 | 1 | @elcoyotediesel Jul 24 | 397k |

The ranking is monotonic in one variable: how easy it is to type the sentence that goes with the send. Rank 1 clips come with the sentence in the caption. Rank 10 to 13 clips are impressive and have no sentence.

---

## 5. Fifteen Rival and Chief reel concepts, each copying one proven mechanism

Rules carried from the house playbook: one lockup on the hook at most, nothing else burned in, no on-screen CTA, no outro, no fade, song added in-app if at all, share line is caption line 1 written as a person type, no Elite Diesel or 307 anywhere on Rival, no em-dashes. All solo-shootable with the Pocket 3 on a stand or a magnet mount.

**1. "Guess the truck by the door." (Lifted Rippers hood test, Y5, 21.4M)**
- Mechanism: identity test, three slams, labels, 10 s.
- Hook: frame 1 is Jacob's hand already on the '59 door, label top centre "GUESS THE TRUCK BY THE DOOR".
- Shots: 0:00 '59 F600 door slam (that hollow 1959 clang), label "1959"; 0:03 Chief's door, label "2011"; 0:06 a modern aluminum Super Duty door at a parking lot, label "2024" with a nauseated emoji. Static medium each, real sound only.
- Caption line 1: "For the guy who says they don't build them like they used to."

**2. "TF is my helper doing?" (Tom's Refurb, T31, 6.36 percent)**
- Mechanism: one locked shot of a person being useless, small complaint caption.
- Hook: a buddy, Jacob's dad, or Jacob himself on a second camera, holding a tool, talking, never using it.
- Shots: one 15 to 20 s locked shot. The person turns the grinder on and off, points at the frame, says "oh man" three times. Lower-third caption, one line, "TF is my shop help doing?"
- Caption line 1: "Send this to the friend who 'came over to help'."

**3. "The one-man truck builder is a nocturnal creature." (DDC nature doc, T39, 6.89 percent)**
- Mechanism: Attenborough VO over ordinary shop footage, each cut lands on the same running gag.
- Hook: wide of the shop at night, lights on, Jacob small in frame, VO at 0.0 s.
- Shots: six to eight 3 to 5 s clips already on the SD card (walking to the parts shelf, staring at the frame, reading a part number off a phone, opening a box, the same box again), each landing on a coffee cup or the phone screen. VO beats: "He has three projects. He will finish none tonight." Ends on the question, "Seriously, how many times does he measure that?"
- Caption line 1: "Looks like we need a coffee sponsor."

**4. "Problem solved." (DPP, T16, 3.7M in 5 s)**
- Mechanism: deadpan wrong fix, face in the corner, loops.
- Hook: frame 1 is the tool already touching the problem on the '59 (tape over a rust hole, a zip tie on a brake line, a sticker over the fuel gauge).
- Shots: one 5 s shot, Jacob keyed lower-left in CapCut, line: "Quick and easy way to deal with 67 years of rust. There you go, problem solved."
- Caption line 1: "For the guy whose whole truck is held together like this."

**5. "Where the 10 mil at, part 2." (Jacob's own 4.05 percent meme, I1)**
- Mechanism: the account's proven meme voice, a money joke over a truck image.
- Hook: a still of the bare Super Duty frame next to the '59 cab, one line of text in the house lockup.
- Shots: 6 to 8 s, two stills or one slow push, text lands at 0:00 and changes once at 0:04. Setup: "Sponsors: 'send us the build budget.'" Payoff: "The build budget:" over the frame on jack stands.
- Caption line 1: "Tag the guy who thinks SEMA builds pay for themselves."

**6. "Junkyard where it belongs." (Freedom Syndicate trash talk and payoff, Y11, 13.3M)**
- Mechanism: a bet stated out loud in the first 4 s, payoff on camera. Rival cannot tug yet, so the bet is a measurable one.
- Hook: Jacob walking back from the '59 to camera, "Buddy says this frame won't take a 7.3 and a 4R100. Hear that, Vinny?"
- Shots: the doubt (4 s), then the thing happening (the cab lifting onto the frame, the engine clearing the firewall, the mock-up bolting down), one static wide held to the end, real sound. Save this for the actual frame day.
- Caption line 1: "For the buddy who called it a parts truck."

**7. "Just an old farm truck." (Tatum understatement plus Tom's 331, Y6 and T11)**
- Mechanism: a title that undersells, a clip that oversells, no text, no talk.
- Hook: a hand on the toggle panel or key in frame 1, 1 s, then the key turn.
- Shots: switch (1 s), key (2 s), gauge (2.5 s), tailpipe (3.5 s), wide under the shop light held 6 s while it idles. 18 s. Real sound only. Use Chief's compound whistle until the 7.3 fires; then redo it with the '59.
- Caption line 1: "Just a little 6.7." (then, on first fire: "Just an old 7.3.")

**8. "Does this kid need help?" then "You told me to." (Dave's two-parter, T25, 9k comments then 1.1M)**
- Mechanism: ask the audience to vote on a kindness, deliver three days later.
- Hook: Jacob at the counter-height bench, "There's a kid in Cheyenne trying to do his first 7.3 and he's stuck on the same thing I was stuck on."
- Shots: part one, 30 s, Jacob talking, two 2 s inserts of the kid's engine or the part in question, ends on "Should I go help him? Tell me." Part two, the drive over, the fix, the kid's face, 45 s, raw.
- Caption line 1 (part one): "For anyone who learned this stuff from a stranger."

**9. "Is Ford really dropping an 8.0?" (FASS rumor as a question, T30, 3.17 percent)**
- Mechanism: tribe news framed as a question the viewer wants to argue about.
- Hook: Jacob with a phone screen or a parts catalog page, "Somebody at the counter told me Ford is doing X. I order the parts. Here's what I actually see."
- Shots: 20 s, one talking shot with two 2 s inserts of the part or the listing. No text except a label of the rumor on frame 1. Rotate: 6.7 CP4 rumors, 7.3 injector supply, the 6.8 gas replacing diesel in fleets. Keep every claim to what the counter actually shows.
- Caption line 1: "Send this to your Powerstroke group chat and watch it fight."

**10. "Your short friends owe you a FASS." (FASS tag-joke, T38, 3.53 percent)**
- Mechanism: a product joke written as a tag line, 5 s.
- Hook: the FASS on Chief's frame rail, frame 1, Jacob's hand slapping it.
- Shots: one 5 s shot, text one line in the lockup: "Your friend with the stock lift pump owes you an apology."
- Caption line 1: "Tag the 6.7 guy still running the CP4 on faith."

**11. "My seat couldn't handle the boost." (Cleetus fail with recovery, T3, 185k shares)**
- Mechanism: the fail is inside 3 s and the person keeps going.
- Hook: whatever lets go next, in the first 2 s: the jack stand that walks, the come-along that slips, the gauge needle that pins, the '59 seat spring that gives out when Jacob sits in it.
- Shots: the moment (3 s), the recovery (5 s), one label at the top: "The '59 seat couldn't handle 67 years."
- Caption line 1: "Send this to the guy who says they don't make them like they used to."

**12. "Which one sounds best?" (Westen Ranger tank vote and Tom's which rig, T13, 3.10 percent)**
- Mechanism: a vote in the caption, zero talking, two-shot pair per option.
- Hook: Chief's exhaust at idle, low static shot at the pipe, frame 1.
- Shots: Chief wide then low pipe (7 s), Jacob's dad's truck or a buddy's 12-valve wide then low pipe (7 s), the 7.3 on the stand or the donor wide then low pipe (7 s). 21 s. Nothing on screen. Caption carries the vote.
- Caption line 1: "Settle it: which one sounds best?"

**13. "First to put X on a 1959." (Zac boom tubes trend-jack, T6, 9.8M)**
- Mechanism: take a running trend from the car side and be first to do it on the odd platform.
- Hook: Jacob holding the part in front of the '59 cab, label "Putting [X] on a 1959 F600", VO at 0.0 s: "Nobody has done this on a '59."
- Shots: 30 to 45 s, part in hand, two inserts of the trend on car accounts (1 s each), the mock-up on the truck, ends on "as soon as the frame's under it we'll know if it works." Candidates: ISSPRO digital gauges in a 1959 dash, a Hydra chip in a 1959 glovebox, a regulated return on a 7.3 in a 1959 engine bay.
- Caption line 1: "For the guy who thinks old trucks can't have nice things."

**14. "This truck doesn't have AC." (Oversteer story-fix, Y9, 15.8M)**
- Mechanism: joke in 4 s, history at 0:20, competence with a dog, "she's back" at the end. Length 60 to 90 s, voiceover, cuts every 2 to 3 s.
- Hook: under the '59 on the first real problem (the rusted cab mount, the fuel tank, the brake line), VO: "So I found a puddle under the '59 and thought, oh, that's the AC. This truck has never had AC."
- Shots: the problem (14 s), one wide of the truck and the line about where it came from (6 s), the parts arriving, the fight, the wrong bolt, the fix, the first turn of the key. Captions of the VO for the first 20 s only. Ends on "she's back" or "one down."
- Caption line 1: "Make sure this doesn't happen to your old Ford."

**15. "Guess which one the parts manager drives." (identity bit, Lifted Rippers plus Vice Grip "how country boys", Y5 and Y22)**
- Mechanism: a title that names the viewer and a reveal that flatters them.
- Hook: three truck doors in a row at the lot (a new Super Duty, a 3rd gen Ram, Chief), label "Guess which one the parts manager drives."
- Shots: 1.5 s on each door, then Jacob's hand opens Chief's door, then the FASS, the ISSPRO pods and the 6R140 shifter in three 1 s cuts. 10 s. Real sound.
- Caption line 1: "For every parts guy whose own truck is the test mule."

Series note: give each of these a running number in the caption ("Rival, day 346") and never on screen. Post concept 7, 11 and 6 the same day they happen, raw. Everything else is a 15-minute edit.

---

## 6. Accounts checked that produced nothing worth a row

WhistlinDiesel's own TikTok (reupload page, 15 posts, 432k best), Heavy D Sparks TikTok (fan placeholder, 129 views), DieselSellerz TikTok (three September posts under 100 views), Vice Grip Garage TikTok (both handles under 130k, best clip is an unrelated comedy repost), Matt's Off Road Recovery TikTok (2021 dance videos), Dirty Diesel Customs Shorts (200 to 2,100), Industrial Injection Shorts (1,200 to 2,700), obsfordtrucks TikTok (under 2k), Diesel Power Products Shorts (76k best against 4.4M on TikTok for the same material), Power Stroke Nation TikTok (profile did not resolve). UCC 2026 (June 5 to 7) produced no short-form clip over 100k that could be found; the 3,825 hp dyno blow-up lives in long-form and blog posts.

## 7. Sources

- Clip stats: `*.info.json` in this folder (pulled 2026-11-21 ~10:00 to 11:00 MT).
- Listings: `scratchpad/yt_shorts.tsv`, `tt_prof.tsv`, `tt2.tsv` (31 accounts), YouTube search `sp=CAMSAhgB` (sort by views, under 4 min) for 20 queries.
- Own account rows: `data/instagram/posts.tsv`, `analysis/2026-11-12-refresh.md`; profile alt text via logged-out fetch of instagram.com/elcoyotediesel/ (583 followers at fetch).
- Whataburger coal roll: https://www.newsweek.com/coal-rolling-whataburger-driver-fumes-diesel-truck-1640737
- WhistlinDiesel channel scale: https://vidiq.com/youtube-stats/channel/@whistlindiesel/ ; https://hypeauditor.com/youtube/UCdqp0KK_Io7TwK5cJMBvB0Q/
- Westen Champlin background: https://www.hotcars.com/westen-champlins-smokestang-diesel-mustang-coolest-youtuber-build/
- Matt's Off Road Recovery scale: https://vidiq.com/youtube-stats/channel/UCwdVOry0oNF9WIe_3uCfz9Q/
- UCC 2026: https://www.turboandstance.net/3825-hp-world-record-diesel-truck-explodes-on-dyno-ucc-2026-insane-pulls-engine-failures/
- Most-viewed truck Reel 2026 (unverified): https://www.wavevision.io/blog/instagram-reels-that-performed-best-in-july-2026-and-why-they-worked
