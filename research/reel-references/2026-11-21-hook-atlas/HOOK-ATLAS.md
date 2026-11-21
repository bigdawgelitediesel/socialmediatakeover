# HOOK ATLAS: the first 3 seconds of 73 reels (2026-11-21)

Built from every reel on disk under `research/reel-references/2026-11-2*` (74 mp4s, one duplicate folded: 72 reference reels plus our own Harley Trade reel as the control). Each reel got a 0 to 3 s strip at 6 fps (`strips/<slug>.jpg`, 18 tiles, tile 1 = 0.00 s, tile 4 = 0.50 s, tile 7 = 1.00 s, tile 10 = 1.50 s, tile 13 = 2.00 s, tile 16 = 2.50 s), the strip was read frame by frame, and the spoken opener came from words.json or the timed transcript. Stats are from each reel's info.json at download time; share ratio = reposts / views x 100 (TikTok only, Instagram hides views and shares, YouTube hides shares). For Instagram reels the only ratio available is likes to comments (L/C), and for comment-gated reels ("comment STUDIO") that number is inverted on purpose, so read it as a funnel signal, not a quality signal. Raw manifest: `manifest.json` in this folder; the numbers behind sections 2 and 3 are in `atlas-data.json`.

Columns: text frame = the 6 fps tile where hook text is fully readable (1 = on from the first frame, 0 = no burned text in the first 3 s); words = words of hook text on screen by 3 s; first change = seconds to the first cut, zoom, or element entering (0.00 = camera or graphic already moving on frame 1; none = nothing moves in 3 s).

## 1. Per-reel table

| # | Reel | Account | Niche | Frame 1 | Text fr | Words | First spoken (s) | First change s | Type | Stats | Ratio |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | diesel-01 rust_ridge 7.3 IDI cab talk | rust_ridge_ranch26 | diesel/auto | face (selfie in cab, steering wheel) | 0 | 0 | 0.7: It's getting cooler in North Carolina | none | STORY | 40,600 views, 5,088 likes, 117 com, 87 shares | 0.21% sh |
| 2 | diesel-02 throtl best of SEMA 18 | throtl | diesel/auto | car (six-wheel Testarossa, SEMA floor) | 1 | 6 | none: music only | 2.07 | LIST | 117,400 views, 14,400 likes, 43 com, 839 shares | 0.71% sh |
| 3 | diesel-03 stradman T-7 | thestradman | diesel/auto | car (teal Lambo in driveway, slow push) | 1 | 7 | none: music only | none | HQ | 667,100 views, 84,600 likes, 639 com, 1,070 shares | 0.16% sh |
| 4 | diesel-04 stradman keep it stock | thestradman | diesel/auto | car (wrapped Lambo in white studio) | 1 | 10 | none: music only | 1.27 | HQ | 405,300 views, 59,800 likes, 552 com, 1,572 shares | 0.39% sh |
| 5 | diesel-05 fass 2,078 hp | fassfuelsystems | diesel/auto | face + truck on dyno, black smoke building | 1 | 5 | 1.4: In case you guys missed the news, Kevin Young just smashed 2,000 wheel horsepower | 0.00 | NUM | 133,700 views, 19,100 likes, 132 com, 3,943 shares | 2.95% sh |
| 6 | diesel-06 nunley family ask | justin_danger_nunley | diesel/auto | face + inset photo of the family | 0 | 0 | 0.0: This family right here lost their home in a house fire | none | STORY | 1,500,000 views, 178,600 likes, 1,999 com, 4,222 shares | 0.28% sh |
| 7 | diesel-07 dieselpowerproducts trans line | dieselpowerproducts | diesel/auto | face from under a truck, hand on the part | 0 | 0 | 0.0: Check this out. This guy knows what he's doing. | 0.30 | QD | 923,900 views, 5,575 likes, 660 com, 2,804 shares | 0.30% sh |
| 8 | diesel-08 tomsrefurb which rig sounds best | tomsrefurb | diesel/auto | car (parked Mustang, lights flash) | 0 | 0 | none: engine only | 0.17 | SOUND | 221,900 views, 51,200 likes, 369 com, 2,418 shares | 1.09% sh |
| 9 | diesel-09 tomsrefurb creator of the year | tomsrefurb | diesel/auto | stage screen reading CONTENT CREATOR OF THE YEAR (in-world text) | 1 | 5 | 0.0: Tonight's honoree started repairing small engines at 13 | none | RESULT | 252,300 views, 52,400 likes, 476 com, 1,977 shares | 0.78% sh |
| 10 | diesel-10 dirtydiesel 3rd gen cruise | dirtydieselcustoms | diesel/auto | detail: gauge cluster, hand on the wheel, tach moving | 0 | 0 | 0.0: (garbled) everyone's hearing about cruise, shift... | 1.67 | STORY | 75,800 views, 6,381 likes, 84 com, 1,708 shares | 2.25% sh |
| 11 | diesel-11 daves hidden contamination | davesautocenter | diesel/auto | face (owner standing in shop) | 0 | 0 | 0.0: Customer bought an engine from us, we shipped it to him | 1.00 | STORY | 278,000 views, 19,500 likes, 345 com, 222 shares | 0.08% sh |
| 12 | diesel-12 jmr just a slow old 7.3 | JMR Rebuilders | diesel/auto | truck (walk-past of a brown OBS crew cab, camera moving) | 0 | 0 | 0.0: So he's already got a Hydra tuner. Go ahead and do it, Drew. | 0.00 | QD | 65,844 views, 1,833 likes, 159 com | L/C 11.5 |
| 13 | diesel-13 jmr super rare coldstart | JMR Rebuilders | diesel/auto | face in cab, dog jumps in at 0.33 | 0 | 0 | 0.3: Here's a cold start on a 97 F350 with a 10-inch exhaust | 0.33 | NUM | 57,687 views, 1,998 likes, 67 com | L/C 29.8 |
| 14 | diesel-14 chipfoose coming to SEMA | Chip Foose | diesel/auto | dark defocused letterboxed frame, taillights emerge | 0 | 0 | none: music only | 1.00 | SOUND | 445,095 views, 2,641 likes, 59 com | L/C 44.8 |
| 15 | own harley trade | elcoyotediesel | own (Rival) | truck (1959 F600 front three-quarter, static) | 1 | 6 | 2.7: (two men talking in shop; payoff line at 4.8) | 2.67 | QD | 2,161 views, 103 likes, 2 com, 1 shares | 0.05% sh |
| 16 | ui chandler jarvis 6.7M | chandlerintelligence | AI-editing explainer | face (split: man left, desk monitors right) | 1 | 6 | 0.5: Hey Jarvis, wake up, daddy's home | 0.67 | QD | 6,700,000 views, 297,296 likes, 45,155 com | L/C 6.6 |
| 17 | ui khalidxah adobe free | khalidxah | tech explainer | UI: app icons flying together on black | 2 | 7 | 0.0: One developer just rebuilt Adobe's entire suite with AI | 0.00 | NUM | 607 views, 15 likes, 0 com, 5 shares | 0.82% sh |
| 18 | ui rick mac vs windows | rick.theengineer | tech explainer | UI: fighting-game character select MAC vs WINDOWS | 1 | 3 | 0.0: Why do so many developers prefer Mac over Windows? | 0.17 | Q | 51,900 views, 2,779 likes, 53 com, 182 shares | 0.35% sh |
| 19 | ui speedy mac 16 GB | speedy_devv | tech explainer | UI: two laptops on black, benchmark numbers climbing | 1 | 1 | 0.0: Why can a new Mac with only 16 gigs of RAM humiliate a PC | 0.00 | Q | 141,000 views, 9,351 likes, 235 com, 1,176 shares | 0.83% sh |
| 20 | ui speedy quantum | speedy_devv | tech explainer | UI: 3D quantum computer render, dolly in | 1 | 1 | 0.0: Everyone says a quantum computer tries every answer at once | 0.00 | BELIEF | 50,800 views, 1,773 likes, 44 com, 96 shares | 0.19% sh |
| 21 | ui visualhustles rejection | visualhustles | motivation | book page with a red pen (in-world text only) | 0 | 0 | none: no speech | none | SOUND | 808 views, 61 likes, 5 com, 0 shares | 0.00% sh |
| 22 | ui justyn 3 launch mistakes | justyn.ai | AI-editing explainer | face (cap, home) + title + caption pill | 1 | 9 | 0.0: Three decisions I made that I thought would kill my viral launch | 1.17 | LIST | 712 views, 25 likes, 1 com, 0 shares | 0.00% sh |
| 23 | ig DcSq abigail visual hooks | abigaildaniellla | creator education | person walking out of a dark cave toward camera, no text | 3 | 4 | none: music only | 0.33 | LIST | 64,661 likes, 121 com | L/C 534.4 |
| 24 | ig Def9pj tenfoldmarc 17 effects | tenfoldmarc | AI-editing explainer | face + title + effect list sidebar + phone card | 1 | 6 | 0.0: orbit, couch wall, UI world | 0.33 | LIST | 21,249 likes, 34,194 com | L/C 0.6 |
| 25 | ig Df3t edita quad wall | edita.visuals | AI-editing explainer | UI: 2x2 wall of four motion panels + CTA pill | 1 | 8 | none: music only | 0.00 | GRID | 832 likes, 1,448 com | L/C 0.6 |
| 26 | ig DfII ultra.skills fix sound | ultra.skills | AI-editing explainer | UI: dark green DAW card, orange mascot | 2 | 4 | 0.0: Claude has now become insanely good at motion graphics | 0.17 | FIX | 7,185 likes, 16,357 com | L/C 0.4 |
| 27 | ig DfU2 nxtlvl 9 apps | ai.nxtlvl | AI-editing explainer | UI: 3x3 grid of app icons tagged PAID, mascot | 1 | 4 | 0.0: Stop paying for these nine apps. GitHub has a free version | 1.33 | FIX | 7,259 likes, 9,185 com | L/C 0.8 |
| 28 | ig Dfcx ultra.skills 30 animations | ultra.skills | AI-editing explainer | text: a bare 30 on black, terminal window slides in | 1 | 1 | none: music only | 0.17 | LIST | 3,144 likes, 8,288 com | L/C 0.4 |
| 29 | chandler every workflow | chandlerintelligence | AI-editing explainer | face + picture-in-picture card with giant I DIDN'T | 1 | 2 | 0.0: I didn't edit a single second of this video. Claude did. | 0.00 | RESULT | 19,100 likes, 21,900 com | L/C 0.9 |
| 30 | justyn claude edited this | justyn.ai | AI-editing explainer | face + giant serif CLAUDE EDITED + caption pill | 1 | 2 | 0.0: Claude edited this video | 0.83 | RESULT | 11,500 likes, 22,000 com | L/C 0.5 |
| 31 | viashaan captions behind head | viashaan | AI-editing explainer | UI: RAW | EDITED split presentation, title, silhouette flash | 1 | 5 | 0.0: Wait, how are these words going behind my head? | 0.17 | Q | 21,700 likes, 25,000 com | L/C 0.9 |
| 32 | justyn anthropic predicted the future | justyn.ai | AI-editing explainer | face + title + caption pill | 1 | 5 | 0.0: Anthropic just modeled what AI does to the economy by 2030 | 0.83 | NEWS | 41,300 views | n/a |
| 33 | justyn I didn't edit a single second | justyn.ai | AI-editing explainer | face in room + giant serif I DIDN'T | 1 | 2 | 0.0: I didn't edit a single second of this video. Claude did. | 0.17 | RESULT | 88,500 views | n/a |
| 34 | justyn chatgpt is a video editor now | justyn.ai | AI-editing explainer | face + giant serif I DIDN'T | 1 | 2 | 0.0: I didn't edit a single second of this video | 0.17 | RESULT | 15,600 views | n/a |
| 35 | justyn 18 effects 20 seconds | justyn.ai | AI-editing explainer | face + title + effect list + caption pill | 1 | 4 | 0.0: kinetic hook, gravity drop... | 0.33 | LIST | 104,200 views | n/a |
| 36 | justyn 20 effects v2 magazine | justyn.ai | AI-editing explainer | face + magazine cover overlay + title + list | 1 | 4 | 0.0: magazine cover, knockout captions... | 0.17 | LIST | 11,600 views | n/a |
| 37 | justyn it drops tomorrow | justyn.ai | AI-editing explainer | face + CLAUDE EDITED on cream | 1 | 2 | 0.0: Claude edited every second of this video | 0.67 | RESULT | 7,600 views | n/a |
| 38 | justyn still in shock | justyn.ai | AI-editing explainer | face (couple + dog on couch) + title | 1 | 8 | 0.0: This is my wife and I wanted to surprise her | 1.97 | NUM | 1,800 views | n/a |
| 39 | justyn chatgpt can edit | justyn.ai | AI-editing explainer | face + CHATGPT CAN EDIT serif | 1 | 3 | 0.0: ChatGPT can edit your videos. Not the only thing it can do. | 0.50 | BELIEF | 9,600 views | n/a |
| 40 | justyn 20 effects v3 | justyn.ai | AI-editing explainer | face + title + list + tracking box | 1 | 9 | 0.0: live cursor, clone row... | 0.17 | LIST | 14,200 views | n/a |
| 41 | justyn opus 5.5 vs fable 5.2 | justyn.ai | AI-editing explainer | face + two PiP cards + title | 1 | 9 | 0.0: (battle setup) | 0.33 | Q | 4,400 views | n/a |
| 42 | edita apple intelligence screen | edita.visuals | AI-editing explainer | UI: monitor on a desk, orange glow, CTA pill | 1 | 8 | none: music only | 0.17 | GRID | 555 views, 6 likes, 0 com, 1 shares | 0.18% sh |
| 43 | edita followers counter | edita.visuals | AI-editing explainer | UI: monitor with a talking man, CTA pill | 1 | 8 | 0.0: There's a way to get so many followers on social media it actually feels like cheating | 0.67 | NUM | 531 views, 11 likes, 0 com, 1 shares | 0.19% sh |
| 44 | edita pay off homes | edita.visuals | AI-editing explainer | UI: monitor with two phone cards, CTA pill | 1 | 8 | 0.0: A lot of people, when they pay off their homes | 0.17 | STORY | 515 views, 7 likes, 2 com, 1 shares | 0.19% sh |
| 45 | edita claude be honest | edita.visuals | AI-editing explainer | UI: 3D blocky character at a laptop + title | 1 | 5 | 0.0: Claude, be honest, are you replacing video editors? | 2.23 | Q | 821 views, 13 likes, 0 com, 1 shares | 0.12% sh |
| 46 | edita editors are switching | edita.visuals | AI-editing explainer | UI: robot with three photo cards + title | 1 | 5 | 0.0: Video editors are switching to Claude and they're not going back | 0.50 | TRIBE | 250 views, 2 likes, 0 com, 1 shares | 0.40% sh |
| 47 | nocodealex claude watches video | nocodealex | AI-editing explainer | UI: paper-craft TV + robot, title 17.6K GITHUB STARS | 1 | 3 | 0.0: You can now give Claude Code the ability to watch any video with this one skill | 0.17 | RESULT | 1,176 likes, 1,536 com | L/C 0.8 |
| 48 | nxtlvl gta6 clip for views | ai.nxtlvl | tech explainer | UI: GTA cover card, title GTA 6 DROPS NOV 19 | 1 | 5 | 0.0: GTA 6 drops November 19th and everyone's about to start | 0.17 | NEWS | 4 views | n/a |
| 49 | nxtlvl claude watches youtube | ai.nxtlvl | AI-editing explainer | UI: cream card, video player, mascot | 1 | 4 | 0.0: Claude Code can now watch YouTube for you. Not a summary. | 1.17 | RESULT | 3 views | n/a |
| 50 | nxtlvl gta6 earn 10k | ai.nxtlvl | tech explainer | UI: GTA art, blur to sharp, no title yet | 10 | 3 | 0.0: GTA 6 drops on the 19th. Save this | 0.17 | NEWS | 0 views | n/a |
| 51 | nxtlvl jarvis morning briefing | ai.nxtlvl | AI-editing explainer | UI: cream briefing card, inbox counter ticking | 1 | 2 | 0.0: Good morning. You have 40 unread emails. | 0.00 | QD | 15 views | n/a |
| 52 | tenfold 0922 opus tweet reaction | tenfoldmarc | AI-editing explainer | UI: X post screenshot + face PiP + caption | 1 | 4 | 0.0: Alright, this is insane | 1.00 | NEWS | 10,100 views, 246 likes, 8 com, 25 shares | 0.25% sh |
| 53 | tenfold 1001 first claude edit | tenfoldmarc | AI-editing explainer | face on couch, hands in motion blur, caption | 1 | 2 | 0.0: Everybody's talking about how Claude can edit your videos, but they're all | 0.17 | BELIEF | 9,399 views, 229 likes, 292 com, 79 shares | 0.84% sh |
| 54 | tenfold 1015 17 effects (TT) | tenfoldmarc | AI-editing explainer | face + title + 01/17 orbit label | 1 | 6 | 0.0: orbit, couch wall, UI world | 0.17 | LIST | 73,700 views, 2,425 likes, 526 com, 1,212 shares | 1.64% sh |
| 55 | tenfold 1017 10M views effect | tenfoldmarc | AI-editing explainer | face at desk + pill + phone card | 1 | 7 | none: (music + card audio) | 0.17 | Q | 963 views, 22 likes, 1 com, 1 shares | 0.10% sh |
| 56 | tenfold 1018 two looks no capcut | tenfoldmarc | AI-editing explainer | face at desk + pill + phone card | 1 | 8 | none: (music) | 0.17 | FIX | 769 views, 17 likes, 1 com, 0 shares | 0.00% sh |
| 57 | tenfold 1018 two clips rip | tenfoldmarc | AI-editing explainer | face on couch + handwritten title | 1 | 6 | 0.0: Claude sucks at video editing, but if you give it effects like this | 1.83 | HQ | 959 views, 20 likes, 8 com, 1 shares | 0.10% sh |
| 58 | tenfold 1019 five clips | tenfoldmarc | AI-editing explainer | face on couch + caption | 1 | 3 | 0.0: I'm terribly sorry to say, but video editors are absolutely | 1.67 | BELIEF | 925 views, 28 likes, 11 com, 3 shares | 0.32% sh |
| 59 | tenfold 1021 16 effects list | tenfoldmarc | AI-editing explainer | face + title + list, newspaper card enters | 1 | 6 | 0.0: headline wall, zoom through cut, vertigo | 0.17 | LIST | 2,384 views, 98 likes, 69 com, 34 shares | 1.43% sh |
| 60 | tenfold 1026 scroll part | tenfoldmarc | AI-editing explainer | face at desk + pill + phone card | 1 | 8 | 0.4: This is how you create a Spotify scrolling effect | 0.17 | FIX | 934 views, 47 likes, 5 com, 0 shares | 0.00% sh |
| 61 | tenfold 1028 pick a number | tenfoldmarc | AI-editing explainer | face + title pick your favorite 1 to 17 + 01/17 orbit | 1 | 6 | none: (music) | 0.17 | Q | 795 views, 27 likes, 2 com, 7 shares | 0.88% sh |
| 62 | tenfold 1030 creator studio made | tenfoldmarc | AI-editing explainer | face on couch + pill + caption | 1 | 6 | 0.0: something happened over the last two weeks that I've been working towards | none | NUM | 734 views, 13 likes, 0 com, 1 shares | 0.14% sh |
| 63 | tenfold 1030 recreated viral effect | tenfoldmarc | AI-editing explainer | face at desk + pill + phone card | 1 | 7 | none: (music) | 0.17 | Q | 439 views, 7 likes, 2 com, 4 shares | 0.91% sh |
| 64 | tenfold 1108 16 new effects | tenfoldmarc | AI-editing explainer | face + title + list + phone card (type wall) | 1 | 7 | 0.0: type wall, the stack, depth scatter | 0.17 | LIST | 3,624 views, 141 likes, 27 com, 42 shares | 1.16% sh |
| 65 | tenfold 1111 diary of a ceo | tenfoldmarc | AI-editing explainer | face at desk + pill + phone card of a DOAC reel | 1 | 8 | 0.0: from five to 12 | 1.50 | Q | 1,149 views, 26 likes, 9 com, 3 shares | 0.26% sh |
| 66 | tenfold 1118 remake viral text effect | tenfoldmarc | AI-editing explainer | face at desk + pill + phone card | 1 | 6 | 0.0: If you've ever wondered how people do this text effect | 0.33 | Q | 717 views, 19 likes, 6 com, 2 shares | 0.28% sh |
| 67 | tenfold 1119 10 new effects | tenfoldmarc | AI-editing explainer | face on couch + title, air-marker circle drawn | 1 | 7 | 0.0: air marker, screen dive | 0.17 | LIST | 781 views, 38 likes, 11 com, 3 shares | 0.38% sh |
| 68 | justyn one recording | justyn.ai | AI-editing explainer | face + ONE RECORDING. serif | 1 | 2 | 0.1: Claude turned this one recording into four reels and three carousels | 0.33 | NUM | 828 views, 35 likes, 16 com, 8 shares | 0.97% sh |
| 69 | ultra I edited nothing | ultra.skillz | AI-editing explainer | UI: dark green, timeline cards above a face | 1 | 1 | 0.0: I didn't edit a single second of this video. Claude did. | 0.17 | RESULT | 722 views, 13 likes, 5 com, 0 shares | 0.00% sh |
| 70 | ultra hey siri | ultra.skillz | tech explainer | UI: 3D iPhone on fabric, word-by-word caption | 1 | 1 | 0.0: Your iPhone hears every word you say on the couch | 1.67 | BELIEF | 3,410 views, 38 likes, 0 com, 2 shares | 0.06% sh |
| 71 | ultra prompt video factory | ultra.skillz | AI-editing explainer | UI: dark, tiny robots and icons, title lands 0.5 | 4 | 3 | 0.0: You can now create thousands of videos with one prompt | 0.50 | NUM | 1,305 views, 55 likes, 13 com, 9 shares | 0.69% sh |
| 72 | ultra sound pack | ultra.skillz | AI-editing explainer | UI: editor card flying in, GREAT at 0.33 | 3 | 4 | 0.0: Claude Code makes great motion, but the sound | 0.17 | FIX | 286 views, 4 likes, 2 com, 0 shares | 0.00% sh |
| 73 | ultra claude ranks you | ultra.skillz | AI-editing explainer | UI: Google results card, rank climbing, caption | 1 | 3 | 0.0: Claude can now check your whole website and tell you exactly why nobody's finding it | 0.17 | RESULT | 18,900 views, 731 likes, 518 com, 233 shares | 1.23% sh |

Type codes: **QD** = Quoted dialogue / skit line; **HQ** = Hater quote; **NUM** = Number or spec; **LIST** = List promise / menu; **Q** = Question, challenge or versus; **BELIEF** = Belief challenge / contrarian; **FIX** = Correction / stop doing X; **RESULT** = Result-first / capability flex; **STORY** = Story cold open, mid-sentence; **SOUND** = Sound-first / no text; **NEWS** = Timely news reaction; **TRIBE** = Tribe call-out; **GRID** = Grid of recognisables / showreel wall.

## 2. Per-type summary

Median share ratio is over TikTok reels with views (n_sh). Median L/C is over Instagram reels (n_lc). Text frame median excludes no-text reels (the no-text count is shown). First change median excludes reels with no change in 3 s (count shown as static).

| Type | n | n_sh | Median share % | Best share % (reel) | n_lc | Median L/C | Median text frame | No text | Median first change s | Static in 3 s | Median views (TT) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Quoted dialogue / skit line (QD) | 5 | 2 | 0.17 | 0.30 (diesel-07 dieselpowerproducts trans line) | 2 | 29.0 | 1 | 2 | 0.30 | 0 | 923900 |
| Hater quote (HQ) | 3 | 3 | 0.16 | 0.39 (diesel-04 stradman keep it stock) | 0 | n/a | 1 | 0 | 1.55 | 1 | 405300 |
| Number or spec (NUM) | 8 | 6 | 0.76 | 2.95 (diesel-05 fass 2,078 hp) | 0 | n/a | 1 | 1 | 0.33 | 1 | 781 |
| List promise / menu (LIST) | 12 | 6 | 0.94 | 1.64 (tenfold 1015 17 effects (TT)) | 3 | 0.6 | 1 | 0 | 0.17 | 0 | 3004 |
| Question, challenge or versus (Q) | 10 | 8 | 0.31 | 0.91 (tenfold 1030 recreated viral effect) | 1 | 0.9 | 1 | 0 | 0.17 | 0 | 892 |
| Belief challenge / contrarian (BELIEF) | 5 | 4 | 0.26 | 0.84 (tenfold 1001 first claude edit) | 0 | n/a | 1 | 0 | 0.50 | 0 | 6404 |
| Correction / stop doing X (FIX) | 5 | 3 | 0.00 | 0.00 (tenfold 1018 two looks no capcut) | 2 | 0.6 | 1 | 0 | 0.17 | 0 | 769 |
| Result-first / capability flex (RESULT) | 10 | 3 | 0.78 | 1.23 (ultra claude ranks you) | 3 | 0.8 | 1 | 0 | 0.17 | 1 | 18900 |
| Story cold open, mid-sentence (STORY) | 5 | 5 | 0.21 | 2.25 (diesel-10 dirtydiesel 3rd gen cruise) | 0 | n/a | 1 | 4 | 1.00 | 2 | 75800 |
| Sound-first / no text (SOUND) | 3 | 2 | 0.54 | 1.09 (diesel-08 tomsrefurb which rig sounds best) | 0 | n/a | n/a | 3 | 0.58 | 1 | 111354 |
| Timely news reaction (NEWS) | 4 | 1 | 0.25 | 0.25 (tenfold 0922 opus tweet reaction) | 0 | n/a | 1 | 0 | 0.50 | 0 | 10100 |
| Tribe call-out (TRIBE) | 1 | 1 | 0.40 | 0.40 (edita editors are switching) | 0 | n/a | 1 | 0 | 0.50 | 0 | 250 |
| Grid of recognisables / showreel wall (GRID) | 2 | 1 | 0.18 | 0.18 (edita apple intelligence screen) | 1 | 0.6 | 1 | 0 | 0.09 | 0 | 555 |

## 3. Diesel winners vs software explainers, first 3 seconds

| Measure | Diesel / auto (n=14) | Software / AI explainers (n=56) |
|---|---|---|
| Median share ratio (TikTok, n) | 0.39% (n=11) | 0.27% (n=32) |
| Hook text on from frame 1 | 5 of 14 | 51 of 56 |
| No burned text in first 3 s | 9 of 14 | 0 of 56 |
| Median hook words on screen (text reels) | 6 | 5 |
| Frame 1 is a face | 6 | 31 |
| Frame 1 is a UI / rendered card | 0 | 24 |
| Frame 1 is a vehicle, part or scene | 8 | 0 |
| Median first change (s, movers only) | 0.67 | 0.17 |
| Nothing changes in 3 s | 4 of 14 | 1 of 56 |
| Median first spoken word (s) | 0.0 | 0.0 |
| No speech in first 3 s | 5 | 7 |

### Reading the summary

- The two highest share ratios in the whole atlas are diesel, and neither has a cut in the first 3 s: FASS at 2.95% (face, truck on the dyno, a smoke plume that is already growing on frame 1, five words of text, voice at 1.4 s) and Dirty Diesel at 2.25% (gauge cluster, hand on the wheel, no text, the hand reaches for the cruise button at 1.67 s). What moves is the subject, not the graphics.
- In the software cohort the menu reel is the share engine: LIST median 0.94%, three of the top six share ratios (tenfoldmarc 17 / 16 / 16 effects), text on frame 1, first element entering at 0.17 s, one item per second. NUM (0.76%) and RESULT (0.78%) are next. FIX (stop paying, fix the sound, no CapCut) is the worst share type at 0.00% median even though the gated versions collect comments.
- Hater quotes are a views type, not a share type: 667k and 405k views for thestradman at 0.16% and 0.39% shares, with the comment counts inflated. Same with quoted dialogue used as bait (Diesel Power Products, 924k views, 660 comments, 0.30%).
- Story cold opens split: a physical detail in motion shares (2.25%), a talking head telling the customer story gets views but hardly any sends (Dave's, 278k views, 0.08%; Rust Ridge 0.21%). Nunley's 1.5M is an emotional ask with a link, a different mechanic.
- On Instagram every AI-editing account runs a comment gate, so L/C sits under 1.0 for all of them (0.4 to 0.9). The one Instagram reel in the set without a gate, the 6.7M chandler Jarvis skit, sits at L/C 6.6, and the pure visual reel (abigaildaniellla) at 534. L/C is a funnel readout, not a hook readout.
- Our Harley Trade control: text on frame 1, six words, nothing else happens until the 2.67 s cut and nobody speaks until about 2.7 s. Skip rate 37.8% says the frame held; 1 share in 2,161 views (0.05%) says it gave nobody a reason to send. The measured quoted-dialogue winner (Diesel Power Products) put a hand on the part and the voice at 0.0 s.

## 4. What separates the diesel winners from the software explainers in the first 3 seconds

1. **The subject is the hook, not the typography.** 9 of 14 diesel reels have no burned text in the first 3 s; 51 of 56 software reels have text on from frame 1, and 24 of them open on a rendered UI card with no human in it. Frame 1 in diesel is the truck, the part, the smoke, the gauge, or a face next to the machine. Nothing in the software set opens on an object.
2. **Diesel moves later and bigger; software moves constantly and small.** Median first change 0.67 s in diesel against 0.17 s in software, and 4 of the 14 diesel reels do not change at all in 3 s (two of those have 667k and 1.5M views). The software reels keep a graphic entering every 1 to 6 frames because the frame itself is not interesting; the diesel winners can hold because a running truck, a growing smoke plume or a hand on a part is already a change.
3. **Text, when diesel uses it, is a label.** One line, 5 to 10 words, top third, set on frame 1 and left alone (FASS "2,078hp Iron Block 6.0 Powerstroke!", thestradman's stacked quotes, throtl's "Best cars of SEMA - Part 18"). Software text is a build: word by word, serif to sans swaps, a strike-through, a highlighted keyword. The build is the entertainment there. For us it reads as a different genre and Jacob has already ruled out most of it (one lockup on the hook, nothing else burned in).
4. **Diesel talks like a person at 0.0 s.** Where the diesel reels speak, the first word lands at 0.0 to 0.7 s in plain talk ("Check this out", "So he's already got a Hydra tuner, go ahead and do it, Drew", "Customer bought an engine from us"). Software openers are written lines ("Stop paying for these nine apps", "Everyone says a quantum computer tries every answer at once"). Both start at 0.0; the diesel line is a sentence someone would say in the shop.
5. **Shares come from a number or a specific, physical thing.** FASS (a number), Dirty Diesel (a button you did not know a 3rd gen had), tomsrefurb (a sound and a question in the caption). The software shares come from a menu you want to save or forward. Both are "a thing I can hand to someone"; neither is a mood.
6. **What the software set does better and we should take:** text readable by frame 1 when there is text; the first element entering by 0.17 to 0.33 s when frame 1 is not already moving; a counter or label (01/17) that tells the viewer the length of the ride; one item per 1 to 1.2 s in a list. What we should not take: the UI-only frame 1, word-by-word type builds, the comment gate.

## 5. Twelve hook templates for Project Rival

Each one is written as frame-1 picture, the one line of text (or none), and the first spoken line, with the type's measured numbers from this atlas. House rules apply: one poster lockup on the hook at most, no on-screen call to action, no grade, the share line goes in caption line 1.

1. **The number in front of the thing (NUM, FASS pattern).** Frame 1: Jacob in front of the F600 with something physically happening behind him (hoist taking the cab, grinder sparks, the Super Duty frame coming off the trailer). Text on frame 1, 5 to 7 words: "1959 Ford. 1999 frame. 0 running engines." First spoken at 0.0 to 1.4 s: "In case you missed it, the frame showed up today." Measured: NUM median share 0.76%, best 2.95% (FASS), text frame 1, first change 0.00 (motion already in frame), no cut needed before 3 s.
2. **Hand on the detail, no text (STORY, Dirty Diesel pattern).** Frame 1: extreme close-up of one part in the cab or on the bench (the HPOP, the glow plug relay, the ISSPRO gauge face), a hand already in frame. No text. First spoken at 0.0 s, mid-sentence: "...which is why every 7.3 guy tells you to do this one first." First change at 1.5 to 1.7 s when the hand does the thing (flips the switch, pulls the plug). Measured: 2.25% share on 75.8k views, no text, change at 1.67 s. Caption carries the tribe line ("7.3 owners, this one's for you").
3. **Sound first, question in the caption (SOUND, tomsrefurb pattern).** Frame 1: the F600 static in the yard or the bay, then the starter crank or the compressor spool with lights flashing at 0.17 s. Zero text in the first 3 s, zero speech. Caption line 1: "Which sounds better, stock 7.3 or compounds?" Measured: 1.09% share on 221.9k views, no text, first change 0.17 s, first cut 3.47 s. Also Chip Foose's defocused opener (445k views, 0.6% likes) says do not start dark and blurry; start on the truck.
4. **The parts menu (LIST, tenfoldmarc and justyn pattern).** Frame 1: Jacob at the bench or in front of the truck with the lockup already on ("7 parts on the Rival that aren't ours", "10 things already on the frame") and the first item label "01/07 Hydra chip" visible. First element (the part, a card, a cut to it) enters at 0.17 s; one item per 1 to 1.2 s; first spoken word at 0.0 s is the first item name. Measured: LIST median share 0.94%, best 1.64%, text frame 1, first change 0.17 s. Partner-friendly by design (Power Hungry, ISSPRO, Driven Diesel, Axiom each get a slot).
5. **Quoted line, hand on the part, voice at zero (QD, Diesel Power Products pattern, not our Harley version).** Frame 1: Jacob under or inside the truck, hand on the thing being talked about, face in frame. No text or the quote as the lockup. First spoken at 0.0 s: "Check this out. A guy told me this truck isn't worth a frame." First change at 0.3 s, the hand moves to the part. Measured: 924k views, 0.30% share, 660 comments; our static version of the same type did 0.05%.
6. **Three hater lines over a slow push (HQ, thestradman pattern).** Frame 1: the F600 on a slow push-in, three stacked quotes on frame 1 in small white caps on black pills: "LS swap it" / "Should've been a Cummins" / "It'll never see SEMA". Music or shop sound, no voice. First cut at 1.3 s to the work that answers them. Measured: 405k to 667k views, 0.16% to 0.39% share, comments 550 to 640. Use when the goal is comments and reach, not sends.
7. **Finished thing first (RESULT, tomsrefurb SEMA and ultra.skills ranks-you pattern).** Frame 1: the finished part filling the frame (powder-coated frame, the first fire, the cab back on). Text on frame 1, 2 to 4 words: "Frame's done." First spoken at 0.0 s: "This is what six weeks and a Super Duty frame look like." First change at 0.17 s (a rank, a counter, a cut back to the mess). Measured: RESULT median share 0.78%, best 1.23%, 252k views for the SEMA award version, text frame 1.
8. **Everybody says (BELIEF, tenfoldmarc 1001 and speedy_devv pattern).** Frame 1: Jacob mid-gesture, hands already in motion blur, two-word caption on frame 1: "everybody says". First spoken at 0.0 s: "Everybody says a 7.3 can't make 600 and live. Here's the parts list that says otherwise." First change at 0.17 s, parts or cards fly in beside him. Measured: BELIEF median share 0.26%, best 0.84%, 50.8k views for the quantum version. A views type; pair it with a number to get sends.
9. **Side by side versus (Q, Mac vs Windows and 16 GB pattern).** Frame 1: two objects already sliding in from the edges (stock 7.3 turbo vs the compound set; the 1959 frame rail vs the 1999 rail), one word of title on frame 1: "Why". First spoken at 0.0 s: "Why does a 1999 frame go under a 1959 truck?" First change 0.00 (objects moving on frame 1), VS beat at 0.17 s. Measured: 0.35% and 0.83% share, 51.9k and 141k views, text frame 1.
10. **One to many (NUM, justyn "one recording" pattern).** Frame 1: Jacob, two-word serif lockup "ONE TRUCK." Cut at 0.33 s to a clean background or the truck. First spoken at 0.05 s: "One truck, three frames, two engines, one deadline." Measured: 0.97% share, text frame 1, first change 0.33 s.
11. **The news card (NEWS, justyn Anthropic and tenfoldmarc Opus pattern).** Frame 1: Jacob with a 5-word title on frame 1 ("Ford just killed the 7.3 part") and the news card or clip sliding in at 0.83 s. First spoken at 0.0 s: the news in one plain sentence, then what it costs us. Measured: 41.3k views for the Anthropic reel on a 4k-view baseline, 0.25% share for the Opus reaction. Views, not sends; use it the day the news breaks.
12. **Walk-in title build (LIST, abigaildaniellla pattern).** Frame 1: Jacob walking out of the shop door or around the truck toward camera, no text. The title builds in one plain heavy sans from 0.33 s and is complete by 2.7 s: "RIVAL / WEEK 12 / THE FRAME". No speech, sound is the yard. First cut at 3.07 s. Measured: 64.7k likes against 121 comments (L/C 534, no gate), text frame 3, first change 0.33 s. The one software-cohort opener that is a person and a place, not a UI.

## 6. Against the 18 templates in 2026-11-20-editing-hooks-retention.md

Confirmed by measurement (with the number that confirms it):

- **1 Quoted dialogue**: confirmed as a type (Diesel Power Products 924k, chandler 6.7M), with an amendment: the winners put the voice at 0.0 s and a hand on the object; our static text-only version shared at 0.05%.
- **2 Price and number**: confirmed, strongest single result in the atlas (FASS 2.95%; NUM median 0.76%).
- **5 Belief challenge**: confirmed as a views type (speedy_devv quantum 50.8k, tenfoldmarc 0.84%), median share only 0.26%.
- **7 Result first, then how**: confirmed (tomsrefurb SEMA 0.78%, ultra.skills 1.23%, justyn "I didn't edit" 88.5k views on a 10k baseline).
- **10 Story cold open mid-motion**: confirmed (JMR walk-past with "go ahead and do it, Drew", Dirty Diesel 2.25%).
- **11 Before/after**: confirmed as a device by viashaan's RAW | EDITED split (21.7k likes), but as a split screen, not a 0.4 s flash. No flash version was in the set.
- **16 Timely angle**: confirmed for views (justyn Anthropic 41.3k vs a 4k baseline), weak for shares (0.25%).
- **17 Help me settle this**: confirmed, and the measured version keeps the question in the caption and the evidence in the video (tomsrefurb "which rig sounds best" 1.09%, tenfoldmarc "pick a number" 0.88%).
- **18 Sound-first**: confirmed (tomsrefurb 1.09%, 222k views). Chip Foose's dark defocused version got 445k views but only 0.6% likes, so the sound-first frame still has to show the subject.

Partially confirmed:

- **6 Callout / tribe**: on screen it was the weakest reel in the set (edita "editors are switching", 250 views); in the caption over a physical detail it was the second-best share ratio (Dirty Diesel). Keep the call-out in caption line 1.
- **9 Stakes and clock**: only seen as thestradman's "T-7 days" caption (667k views, 0.16%) and nxtlvl's dead GTA channel. Views yes, shares unproven.
- **12 Correction**: the worst share type in the software set (FIX median 0.00%); the one that worked (nxtlvl 9 apps, 7.3k likes) is a comment gate. Keep it for comments, not for sends.
- **14 Rate it with my face**: not seen as such, but its mechanic (one item per second with a counter) is the menu reel, which is the top software share type (0.94%).

Not observed in this set (still untested): **3 trade and sacrifice**, **4 nobody tells you**, **8 expert confession** (nearest is Dave's customer story at 0.08% share), **13 put a finger down**, **15 the quiet text-only flex**.

New in the atlas, not in the 18:

- **The menu reel** (LIST): title plus counter on frame 1, item one at 0.17 s, one item per 1 to 1.2 s. Median share 0.94%, three of the top six software share ratios. Template 4 above.
- **The stacked hater quote** (three lines on frame 1 over a slow push, payoff cut at 1.3 s). Template 6.
- **Side by side versus** with objects sliding in on frame 1. Template 9.
- **One to many** as a two-word lockup and a 0.33 s cut. Template 10.
- **Walk-in title build**, the only no-UI opener in the software cohort. Template 12.
- **The AI-speaks skit** (chandler "Hey Jarvis, wake up", 6.7M views, nxtlvl morning briefing): the machine talks first. Not for Rival unless the truck gets a voice.

Two corrections to the frame-by-frame spec in section 3 of that document, from measurement: (a) "text by frame 4" is right when there is text, but 9 of 14 diesel winners have no text at all in 3 s and the frame does the work; (b) "first pattern change at frames 30 to 45" is late against this set: software moves at 0.17 s median, diesel at 0.67 s, and every reel above 1% share either had motion inside frame 1 or an element entering by 0.33 s.
