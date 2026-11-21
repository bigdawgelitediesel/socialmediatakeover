# The "animated UI card" explainer style (late 2026) and how to build it in rival-reels

Researched 2026-11-21 for @elcoyotediesel / Project Rival. Builds on two breakdowns already in this repo: `reel-references/2026-11-21-DfU2nIgt8XK/BREAKDOWN.md` (@ai.nxtlvl, cream paper, cards on spoken words, HUD counter, strike + stamp, count-up, comment-gate demo) and `reel-references/2026-11-20-justyn-ai-profile/STYLE-CATALOG.md` (@justyn.ai). New reference material downloaded today lives in `reel-references/2026-11-21-ui-card-style/` (seven clips, each with info.json, description, watch.py sheets, scenes.csv, transcript.txt, words.json).

Research constraints, stated up front: Instagram is login-walled and every mirror we tried (imginn, oleg.ae directory, profile reels pages) is Cloudflare-gated or 403s, so follower counts below come from dated secondary sources (Postiz 2026-11-16, Keyframes 2026-10-28, promptslove 2026-10-08, Apify 2026-03-31, hafi.pro 2026-11-21, modash 2026-11-09) and are labelled as such. yt-dlp does download public IG reels by shortcode and TikTok videos by URL (that is how the seven examples got here), but it returns no follower counts for either platform.

## 0. The short version

- There are two families of this style. **Family A, "cards on paper"**: @ai.nxtlvl, @justyn.ai, @chandlerintelligence, @viashaan. Flat UI mock objects (repo cards, comment boxes, DM cards, chips, stamps) on a cream or dark plate, driven word by word by a voice. Built with code (Remotion) or AE. **Family B, "redrawn world"**: @speedy_devv, @scroll.engineer, @charles.zhengg, @khalidxah, @rick.theengineer. Black background, isometric or 3D redraws of the real thing (a motherboard as a city), a cartoon presenter, the one key word per caption line boxed. Also built with code (Claude Code + Remotion is the stated pipeline for speedy_devv's 43.4M views in 30 days). A third, older family (**black and white stick figures**: @visualhustles 1.7M, @neuronvisuals 936K, @valueanimate 254K) is After Effects or Pillow + ffmpeg and carries no voice.
- The shared grammar: no cuts, one continuous scene; something new lands every 0.9 to 1.5 s; every element is tied to a word timestamp; one accent word per caption line (pill, box, or italic serif); a visible progress device; the CTA is demonstrated as a fake comment and DM, not stated.
- The pipeline the top accounts actually use in Nov 2026 is: script → TTS with word timings (ElevenLabs / OpenAI / Fish, or local Kokoro + Parakeet) → coding agent writes each scene as a React component → Remotion renders 1080x1920 → post. Keyframes sells exactly that folder for $99 to $249. Our kit is already this pipeline; what is missing is eight components (section 6) and a handful of timing conventions (section 4).
- Sound: the voice carries it. UI ticks, if present, sit 18 to 24 dB under the voice. CC0 packs: Kenney UI Audio (50 files), Kenney Interface Sounds (100), sfxmint UI (815, hotlinkable), Freesound filtered to CC0.

## 1. Who posts this style right now (Oct to Nov 2026)

| # | Handle | Size (date, source) | What they post | One recurring named effect |
|---|---|---|---|---|
| 1 | @ai.nxtlvl (IG) | Count not retrievable (login wall, mirrors blocked). Reel DfU2nIgt8XK posted 2026-11-04: 7,259 likes, 9,185 comments. | "Stop paying for these 9 apps": paid app vs free GitHub repo, 9 per reel, comment REPO gate | **Strike + FREE stamp**: name struck through left to right in 8 frames, green FREE sticker slaps on at about -8 degrees. Plus the 0/9 HUD with filling dots. |
| 2 | @speedy_devv (IG, Hugues Bouissonnie, founder of Keyframes) | 182K and 43.4M views/30 d on 2026-10-28 (Keyframes guide); 231K on 2026-11-16 (Postiz). Median views per post 3,075 before the format, 69,913 after (IG API, Aug 1 to Oct 21). | 60 to 150 s tech explainers, no face, cartoon presenter, 60 fps | **Selection-box key word**: one word per caption line sits in a thin blue rectangle with four corner dots (a Figma selection handle), colour-matched to the object it names. |
| 3 | @neuronvisuals (IG) | 936K; 265M views on 42 reels; top 3 reels (Oct 9 to 13) 228M (Postiz, 2026-11-16) | 8 to 16 s, two white stick figures on black, two caps labels, no voice | **Winner turns yellow**: at about second 9 the right-hand figure and its label go yellow and raise both arms. |
| 4 | @charles.zhengg (IG) | 325K; 17.6M on 18 reels; 1K to 150K in two weeks (Postiz, 2026-11-16) | 3D "how it works" explainers with brief face-on segments | **3D teardown**: layers of a product lift apart with leader-line labels. |
| 5 | @scroll.engineer (IG) | 186K; 30M in 20 days (Postiz, 2026-11-16, calls it "one of two originals" of the format) | Science and engineering, isometric redraws | **Isometric city**: the mechanism drawn as a small white model world the camera glides through. |
| 6 | @chandlerintelligence (IG, Chanyoung Ryu, Seoul, ex-Higgsfield, CEO Feed Media) | 78K (oleg.ae tracker, undated); reel DaebyH0xIDQ (2026-07-07) 297,296 likes, 45,155 comments, "Comment JARVIS for the full guide" | Reaction/breakdown of other creators' Claude-edited reels, re-creating each effect | **Repo card**: dark GitHub card with star and fork counts that count up; plain white captions with drop shadow, one word in a coral box. |
| 7 | @justyn.ai (IG + TikTok) | TikTok 179.9K (search snippet, Nov 2026); IG reel DehbdDYssBE 11.5K likes / 22K comments | Talking head + branded UI mock cards on forest green, serif captions | **Comment drop**: a comment box slides in, "EDIT" types itself, a reply appears, comments stack as testimonials. |
| 8 | @visualhustles (IG) | 1.7M, 3,168 posts (promptslove, 2026-10-08); course page claims 1.2M gained with the B&W style | Minimalist black-and-white stick-figure metaphors (ladders, bridges, two paths) | **Two-path metaphor**: five projects vs one, drawn as two routes, one lights up. |
| 9 | @valueanimate (IG) | 254K, 957 posts (promptslove, 2026-10-08) | "Discipline, but make it animated", same B&W family, sells a Gumroad course | **Line-draw reveal**: the figure draws itself as a single stroke. |
| 10 | @rick.theengineer (IG + TikTok) | 108K and top reels 607K / 749K / 954K (Brainrot Shorts blog, 2026-08-17, vendor claim); TikTok posts this week 13K to 52K views | Tech explainers with a presenter character, self-drawing diagrams | **Counter + diagram per beat**: one element per frame, each a counting stat or a diagram that draws itself on the word. |
| 11 | @khalidxah (IG + TikTok) | Keyframes customer; reel posted 2026-10-24 had 228,813 views by 10-29 | Dev/tech explainers ("How Vercel really works when you git push") | **Race track card**: competitors as cars on a track, one marked last. |
| 12 | @statbolthq (IG) | Keyframes customer; reel posted 2026-10-27 had 2,807,230 views by 10-29 | Football stats in the same format | **Pile-up counter**: 61 balls fall into a net while the number counts. |
| 13 | @ashutoshwithclaude (IG) | 41.7K; 3.3M views in a month; 52 posts; sells a tool (Postiz, 2026-11-16) | Low-poly character explainers | **Low-poly presenter**. |
| 14 | @agentpoly (IG) | 24.4K; 5.5M views; first 10K followers in one week (Postiz, 2026-11-16) | Low-poly 3D explainers | **Voxel assemble**: the object builds block by block. |
| 15 | @tiffintech (IG) | 697K (Oct 2026 ranking via fixieit); YouTube 654K (yt-dlp today) | 60-second AI/robotics explainers, face plus graphics | **Giant caption + card** on a talking head (the hybrid our kit already targets). |
| 16 | @viashaan (IG, Shaan Johari, Creative Director at AI Makeover) | Count not found | "Editing, storytelling and making videos with AI"; third creator in the Claude-editing niche with justyn and chandler | **Captions behind the head** (see our 2026-11-20 viashaan folder). |
| 17 | @godofprompt, @mavgpt, @noevarner.ai, @tenfoldmarc, @thekeshavkrishnan (IG) | Listed in Apify's 125-account AI creator dataset (data 2026-03-31, 35M followers total, ~278K average, no per-account counts) | Prompt packs, Claude Code, n8n; comment-keyword gates on most posts | **Comment-gate CTA** as the closing card on nearly every reel. |

Adjacent, for the comment-gate mechanics rather than the look: ManyChat is still the default tool (pricing changed 2026-03-02, free tier now 25 contacts), Meta's native Custom Keywords automation is free but capped at 5 keywords per account with a 15-minute delay unless you reply first, InstantDM is $9.99 flat, CommentKeyword gives 300 free DMs a month. Only one DM may be sent per commenter within 7 days.

### 1a. Downloaded examples and what the sheets show

All seven are in `reel-references/2026-11-21-ui-card-style/<name>/` with the video beside them. Frame counts below are at the clip's native rate unless noted.

**speedy-devv-mac-ram** (TikTok 7708777395716623649, 140.9K views / 9,345 likes on TikTok at download; the IG original is one of his 1M+ reels). 62.8 s, 1080x1920, **60 fps** HEVC. Transcript: "Why can a new Mac with only 16 gigs of RAM humiliate a PC with twice as much?"
- Plate: pure black, no texture, no vignette.
- Caption zone: top, baseline about y 130 of 1920, white Inter-class sans about 34 px, sentence case, 2 to 4 words per line, revealed word by word on the voice. Emphasised nouns go bold; the ONE key word per line gets a thin 1.5 px rectangle with four 5 px corner dots, coloured to match the object it names (purple for "processor" because the CPU block is purple, green for "graphics card", yellow for "RAM", blue for neutral terms). The box fades the previous word to grey as the next arrives.
- Content zone: y 300 to 1250. The hook is two real laptops with live percent counters (25 to 100 percent on the Mac, 10 to 59 on the PC) and "16 GB" vs "32 GB" counting in. Then a real Legion laptop flips to its open PCB, which becomes an isometric city: the CPU as a purple tower, the GPU as a green block, the RAM as a yellow block, couriers (tiny trucks) driving a "PCIe 5.0 x16, 64 GB/s, the narrow highway" road. Micro-labels are 16 to 18 px caps with a hairline leader ("PROCESSOR / Core Ultra 7 255HX / the brain").
- Presenter: a cartoon man (red tee, green glasses) about 380 px tall, bottom centre, swaps pose on every beat (points, shrugs, holds a stopwatch, facepalms). He is a sprite set, not animation: 1 to 2 pose changes per second, no in-betweens.
- Motion: camera glides and scale changes are continuous; objects enter by scaling from about 0.9 with a 10 to 15 frame ease-out (at 60 fps, so 0.2 s). Counters tween over about 30 frames (0.5 s). No hard cuts in 62 s except a 6-frame "layer explode" on "they broke all of that" where the PCB splits into shards.
- Sound: voice only, close mic, music absent. Follow-for-the-next-one ending.

**speedy-devv-quantum** (TikTok 7709836182317763873, 50.8K views). 146 s, 60 fps. Same system, so what is worth recording is the object library: a 3-wheel suitcase lock with rolling digits (odometer-style count), a 1000-code grid as a field of thin bars whose heights are the "wave", a qubit circuit redrawn in magenta on a grey chip, an IBM dilution fridge, a sign-in dialog and a search bar ("piz|") typed with a caret as UI redraws, a scanned Grover paper, a "5.1 K / 180 x" vertical scale. The payoff beats ("three times taller", "opens.") get the box; filler words never do. Sheet-03 shows the whole second half runs on one object (the bar field) with labels and counters changing, which is why 146 s holds: nothing re-learns.

**khalidxah-adobe-free** (TikTok 7698399160428514566, Keyframes customer, 158 s, 30 fps, 576x1024 TikTok re-encode). This is the cleanest Family A + presenter hybrid of the batch and the closest to what Jacob described.
- Plate: starts black for the 7 s hook (a 2x4 grid of Adobe app icons with a glowing centre split, "+ AI" chip, a cracked-glass overlay and a green "$0" price tag stamped at an angle), then hard-switches to a white #FAFAFA plate for the body.
- Caption: top centre, y about 70 to 90 of 1024 (about 130 to 170 at 1920), grey-then-ink sans about 20 px at 576 (about 38 px at 1080), word by word, the payoff word boxed in a thin blue rectangle with corner dots (same selection-box device as speedy_devv, so it is a Keyframes house style).
- Cards: white GitHub-style repo card with a 1 px #E5E5E5 border, radius 10 to 12, soft shadow (about 0 6px 20px rgba(0,0,0,0.08)), header row (octocat, "ArtCraft", "Public", a "2 apps" count that climbs to "7 apps"), an author row with a "Built with Claude Opus 5.5" chip, then a two-column mapping list (Photoshop → PhotoCraft) whose rows pop in on the spoken app names, then licence chips (Open source, MIT, Apache 2.0). A second stat card: "Adobe research & development" with "$4.29B" rolling in odometer-style over about 12 frames with a red bar under it, then "vs 1 developer" appearing to the right. Then a 3D building on a glass disc (the "moat") with a red "ADOBE R&D, 1 YEAR $4.29B" bar and a green "COST TO REBUILD almost free ≈ $0" bar sliding in underneath. Later: a PS5 render with a "SONY PlayStation" notice card, an "AnyPS5" repo card, a Windows file-explorer card, a "Your company" org chart with avatars, a Grok Bot phone mock. Every noun gets a redrawn UI object; nothing is a stock icon.
- Presenter: a hoodie-and-sunglasses cartoon man, about 280 px tall at 1024, bottom centre, 8+ poses swapped on beats (facepalm on "crack", pointing on "open-source", shrug on "almost free").
- Motion: card entrances translate up about 20 px with a 10 to 12 frame ease-out, rows stagger 3 to 4 frames, counters 12 to 18 frames, no cuts except the black-to-white plate switch at 7 s. Voice only, no music.

**rick-engineer-macbooks** (TikTok 7706733859718581526, 51.9K views, 158 s, 30 fps). Same "redrawn UI" family but with a video-game skin: a "P1 MAC vs P2 WINDOWS" fighter-select hook with gold bevelled titles, a "STAGE SELECT / TECH STARTUP" grid of laptops, then a macOS desktop (dock, menu bar with a real-looking clock, Spotlight typing "unix", Terminal windows with the lines typing in, an AWS instances table, a Finder window with file icons, a Microsoft Learn page with a cursor clicking "wsl --install", a MacBook Pro spec sheet, an Apple hardware overview with CPU/GPU/Neural Engine blocks, an Activity Monitor graph drawing itself). Captions: bottom third (y about 290 of 1536 tile, around 1180 at 1920), white sans on a dark pill, one key word per line on a blue highlight box. Presenter: a Rick-style cartoon scientist sprite at the left edge holding a paper. Cursor clicks are a real device: the pointer moves to the button and the button depresses on the word. Everything is a redrawn screen, which is why it reads as "software tutorial" even though it is explainer content. Voice only.

**chandler-jarvis-6.7M** (IG DaebyH0xIDQ, 297,296 likes / 45,155 comments, "Comment JARVIS for the full guide", a repost of @lukebuildsai, 82 s, 30 fps). This is the TALKING-HEAD variant and the proof that the card grammar works over footage, which is our actual use case: luke at his desk, hard cuts between a medium and a wide; a 3-line Anton-class caps title "HOW TO BUILD JARVIS USING CLAUDE" centred for the first 4 s; captions white sans about 34 px with a soft drop shadow, no pill, 2 to 4 words, around y 1180 to 1240; then one card per named tool exactly on the word: a red arrow pointing at a monitor, a movie still, a dashboard screenshot card, a cream "Claude Code /voice" card with a pixel-robot icon and serif wordmark, the ElevenLabs wordmark on black, a "Claude in Chrome" coral card with a cursor icon, the RevenueCat and Buffer logos on white tiles, a browser screenshot of the Meta Ads MCP page, the Gmail wordmark. Cards are 300 to 420 px wide, soft shadow, radius about 16, enter with a 10 frame pop (scale 0.9 to 1), hold 1.5 to 3 s, and exit with a 5 frame fade. Tiny secondary captions in 18 px white float next to his head quoting the data he reads out ("Over the last seven days, we had 2,459 new downloads"). One tool tag per named brand is the exact pattern our `ToolTag` already implements; what it adds is the second, smaller "quote" caption and the sticky title for the first 4 s. Sound: voice plus a low music bed.

**justyn-launch-mistakes** (TikTok 7709716526542097685, 93 s, 30 fps, 720x1280). Justyn's own newer style, two days old: talking head, serif captions in a dark green pill at y about 1020 of 1280 (about 1530 at 1920, lower than his IG reels), the key word of each line in a lighter tint; a small white "chapter" tag top centre in bold sans ("1. Pricing", "2. A money-back guarantee", "Two reasons:", "1. It's very good", "2. Can't take it back", "An easy yes."); UI cards on the words: a Stripe "Gross volume $258k" chart card, a TV news still, a cream "$97 USD, One payment, no subscription, 7-day money-back guarantee" pricing card with the guarantee text highlighted in yellow on the second visit, stacked comment screenshots as testimonials (the "comment stack"). Black-and-white beat on "scared" (desaturate, colour returns). Cards sit top-left over the dark wall, about 380 px wide, radius 12, soft shadow, 8 to 10 frame pop. Takeaway: the chapter tag at top centre is a cheap retention device for numbered talking-head reels (our `Numeral` is the giant version; this is the small persistent one).

**visualhustles-rejection** (TikTok 7699921106974674228, 40 s, no speech). Not the animated style at all: a phone video of a red pen on a book page about rejection with a music bed. Kept as a negative example: the account's 1.7M-follower IG animations are not what it posts to TikTok, so the TikTok mirror is not a reliable source for the B&W style. Use Postiz's and promptslove's written descriptions for that family instead.

**@ai.nxtlvl DfU2nIgt8XK** (already broken down; measurements added today from frames/hook, card-enter and cta tiles, 1080-wide frame): background #EDE8E0 to #EFEBE3 with a faint radial vignette; cards are off-white #FBF9F4 with a 2 px ink (#1B1B1B) border and a HARD offset shadow (about 5 px right, 5 px down, 0 blur, ink), radius about 14 px on the big repo card and 10 px on the 3x3 tiles; tiles about 190 px square on an 18 px gutter; PAID tag is a 20 px mono caps word in a 1.5 px red (#D9412E) outline pill, radius 4; FREE sticker is a green (#2E9E5B) fill with white mono bold, rotated about -8 degrees, overlapping the card's bottom-right corner; the star pill is mono "★ 32.2 K stars" with an ink border; OPEN SOURCE is a green-outline mono caps chip; feature chips are peach (#F6C9BA) fill, ink border, 3 px hard shadow, bold sans about 30 px; the caption is grey (#6B6B6B) sans about 34 px at y 220 with the accent word in italic serif on a peach pill (#F3C4B4, about 6 px padding); the HUD at y 100 is a mono "0/9" in a bordered box, then nine 26 px outlined squares on an 8 px gap that fill coral (#E0624A) one per item, with the handle in mono grey at the right; the mascot is a coral pixel robot about 90 px with a dotted thought bubble that parks on the top-right corner of the current card; the iris is a coral circle growing from the centre of the frame; the comment card has a centred bold "Comments" header, a coral avatar circle, "you · just now", the keyword in bold, an input pill and a heart; the DM card has "Messages · now" in small grey, "Your 9 free repos" bold, and 2-column bordered chips that fill two per beat.

## 2. What these creators actually use

Stated by the creators or their vendors, with the source. Where it is inference it says so.

| Creator / family | Tool | Evidence |
|---|---|---|
| @speedy_devv, @khalidxah, @statbolthq, @nielshg_, Koen Salo | **Claude Code or Codex writes each scene as code, Remotion renders 1080x1920 MP4 locally; voice from ElevenLabs, OpenAI or Fish with the user's own key; word timings measured from the voice and every caption word and picture tied to them.** | Keyframes guide "How people make those Claude reels on Instagram" (getkeyframes.com, Oct 28 2026 data) and the Keyframes product page. Hugues sells the folder as "Full Visual" ($99, was $199), "+ Character" ($129, needs one photo of you), "Complete" ($249, six reels' project files, 33M views), "Product Demo" ($39, from a URL, repo, app, design or recording). Commercial use included; Remotion itself is free for individuals and companies up to 3 people, $25/seat/month above that. |
| @chandlerintelligence | Claude Code, FFmpeg, Remotion named on screen (slider reveal credited to Remotion), yt-dlp for grabbing references, a storyboard table before render; rejects CapCut and the Edits app (icons crossed out). | Our 2026-11-20 breakdown of De8SPjEAuV0. |
| @justyn.ai | "Claude edited this": strongest model at max effort, a brand style guide plus sample reels, a shot-by-shot artboard before rendering. Sells an "AI Video Editing Masterclass" waitlist. | Our 2026-11-20 breakdown; TikTok bio. |
| @visualhustles, @weissvideo | **After Effects** (course asks for AE 24.03 plus plugins); minimalist black-and-white; course "Viral Animated Reels" on Gumroad, chapter 6 is SFX, VFX and export; claims 200K (Weiss) and 1.2M (Visual Hustles) grown on the style. | weissvideo.gumroad.com/l/animationcourse and reseller listings. |
| @neuronvisuals clones | Claude writes a **Python script that draws frames with Pillow and encodes with FFmpeg**; 30 videos in about 13 minutes; trending audio added in the IG app. | Postiz "Claude Animation: faceless videos" (Nov 16 2026). This is how Postiz reproduced the look, not a statement from neuronvisuals. |
| @rick.theengineer | Vendor says the account is made with Brainrot Shorts' "AI Motion Graphics Generator" from a script, no AE; optional uploaded character image as presenter; about 20 minutes per video. | brainrotshorts.com blog (Aug 17 2026). Vendor claim; the TikTok bio calls itself an unofficial fan account. |
| Hosted "Claude + code" services | Ootto ($48/month, up to 50 IG accounts, stock or cloned voice; React renderer unnamed), promptslove "Motion Graphics PRO" skill (zip, renders on your machine, 1080p MP4 plus contact sheet), Kolbo, ngram. | ootto.ai blog (Nov 1 2026), promptslove (Oct 8 2026). |
| Open-source skill stacks | Remotion's official Agent Skills (launched Jan 20 2026; the launch post is reported at 6M to 18.9M views on X); `claude-motion` (whaleyxbt, MIT, motion rules + sound engine + self-check loop on Remotion); HyperFrames (HeyGen, Apache 2.0, mid-April 2026, about 21.9K stars, HTML to MP4, 9 skills, about 450 blocks); artemnovitckii/claude-animation-skills (1.0K stars, 11 styles, HyperFrames + GSAP + three.js, 1080x1920 at 30 fps, 2D renders in about 10 s, free local Kokoro voice + Parakeet word timings); yashm1/instaedits (Claude plans, Remotion renders infographic cards on transparent, ffmpeg composites over the camera footage, Edits app only for audio and caption text). | GitHub READMEs fetched today; Keyframes "Claude skills for video" (Nov 21 2026). |
| Claude Motion (Anthropic) | Beta since Oct 8 2026, Team and Enterprise only, builds animation as code, exports MP4 from the app. No voice, no word-level captions, no stated vertical support. | support.claude.com article 17454997 and secondary coverage. Not what the big accounts use. |
| Jitter | Browser motion tool with Figma layer import; free plan exports 720p at 30 fps max, so paid is required for 1080x1920. Has "Animated UI Kit" and "Animated App List" templates that approximate Family A cards. | jitter.video template pages. No creator in the table above credits Jitter. |
| Canva, CapCut, Edits | Appear only in tool roundups. CapCut's general Sounds tab is non-commercial and only cleared for TikTok (our sound-design doc). Edits added a teleprompter, Ideas tab and templates this year. | Roundups; Wikipedia Edits (app). |
| Mascots and characters | speedy_devv's red-tee presenter and Keyframes' "+ Character" (built from one photo) point to an image-gen character turned into a pose sprite set; nxtlvl's pixel robot is a hand-drawn sprite (pixel art, two poses). **No creator statement found that Higgsfield or Kling generates the mascot**; Chandler is ex-Higgsfield but does not use a mascot. Treat "AI video generator for the mascot" as unverified. | Inference from frames plus the Keyframes FAQ. |
| Templates (AE) | Motion Array and Envato Elements still supply lower thirds, stickers and UI kits for the AE family; nothing specific to this card look was found that the code family uses. | Roundups. |

Takeaway for us: the two accounts whose look is closest to what Jacob asked for (nxtlvl, speedy_devv) are code-rendered. Our kit is on the same stack and the same version family (Remotion 4.0.545 vs Keyframes' unstated 4.x).

## 3. The design system of the style

Values are measured from frames (nxtlvl, speedy_devv) or quoted from the sources named. Where a value is our translation into El Coyote it is marked OURS.

**Plates**
- Family A paper: cream #EDE8E0 to #F7F3EA, optional faint radial vignette (nxtlvl uses about 8 percent darkening at the corners), zero texture. promptslove's light theme: bg #F7F3EA, ink #18222D, "bad" #C95050, "good" #247A60. Dark variant: #080B0F / #F4F2EA / #EF7D7A / #74C9AE.
- Family B: pure #000000 (speedy_devv, neuronvisuals). vanja.io's generated-default warning: bg #0E0F13 with one accent #FF5A1F is "what the brief produces every run" if you do not set hex values first.
- OURS: black #0b0b0c (talking-head reels) or a cream card-only plate #efe9dc for list reels. Never both in one reel.

**Cards and shadows**
- nxtlvl "sticker" card: fill #FBF9F4, 2 px ink border, hard offset shadow `5px 5px 0 #1B1B1B`, radius 14 px (big) / 10 px (tiles) / 4 px (tags). No blur anywhere. This is the neo-brutalist recipe and it reads crisp at 1080 downscale.
- justyn / chandler soft card: white or cream, no border, soft shadow about `0 18px 50px rgba(0,0,0,0.35)`, radius 20 to 24 px.
- Kit today: `cardShadow = "0 18px 50px rgba(0,0,0,0.55), 0 2px 6px rgba(0,0,0,0.35)"`, radius 22. Add a `hardShadow = "6px 6px 0 #0b0b0c"` token for the sticker family and let `Card` take `variant: "soft" | "sticker"`.

**Type**
- Family A caption: grey sans (Inter / Geist class), 34 px at 1080, sentence case, 2 to 5 words. Accent word: Instrument Serif Italic in ink on a peach pill. Card titles: Inter SemiBold 36 to 40 px. `owner/repo`, star counts, HUD, PAID/FREE tags, feature footnotes: a mono (JetBrains Mono / Geist Mono class) 18 to 22 px, often uppercase with 2 to 4 px tracking.
- Family B caption: white sans 34 px at the TOP of the frame, bold on emphasised nouns, one key word boxed. Micro-labels 16 to 18 px caps with hairline leaders.
- justyn: EB Garamond / Cormorant-class serif caps for titles, same serif italic for the accent word, small-caps sans for micro labels, cream on forest green.
- artemnovitckii's skill fonts (all OFL): Inter, Inter Tight, Poppins, JetBrains Mono, Montserrat, Lora. vanja's "where generated design lands" list: Inter, Space Grotesk, Instrument Serif, Geist, JetBrains Mono.
- OURS: Poppins Medium for the caption, Instrument Serif Italic for the accent word (already in theme.ts), Anton for block titles, and ADD one mono: JetBrains Mono Regular + Bold (OFL) for HUD, part numbers, prices and specs. Part numbers in mono is the single biggest "software look" borrow that also fits a parts manager.

**Chips, tags, stamps**
- Tag (PAID / STOCK): mono caps 20 px, 1.5 px outline in the status colour, radius 4, 4 x 10 px padding, white fill.
- Sticker (FREE / SPONSORED / BOUGHT): filled status colour, white mono bold 24 px, radius 6, rotation -8 degrees, overlapping the card edge by about a third of its height, hard shadow 3 px.
- Chip (features): fill peach #F6C9BA (OURS: tan #c9b38c at 35 percent over cream, or oxblood fill with cream text), 1.5 px ink border, radius 8, 8 x 16 px padding, bold sans 30 px, 3 px hard shadow, enters scale 0.8 to 1.
- Count pill: mono, "★ 32.2 K stars" pattern, ink border, counts up.
- Status colours nxtlvl: red #D9412E, green #2E9E5B, coral #E0624A. OURS: oxblood #7a1f1f for the old/stock state, green #1f3a2d for done/free, tan for accent.

**HUD counter**: y 100, left: `n/total` mono in a bordered box; then `total` outlined squares 26 px on 8 px gaps that fill one per item; right: handle in mono grey 20 px. Entire HUD is static except the fill, which pops (scale 1.3 to 1 over 5 frames).

**Mascot**: a 90 to 120 px sprite with 2 to 4 poses, parked on the top-right corner of the live card, swapping pose on the item change. speedy_devv's presenter is a 380 px sprite set bottom centre with 10+ poses, swapped 1 to 2 times per second. Rule from the nxtlvl breakdown stands: skip unless we draw a coyote mark.

**One-accent-word pill**: the accent is always the payoff noun of the phrase (Open Generative AI, cinematic, fully local, REPO, links). Pill radius 6, 4 x 10 px padding, lands on the same frame the word is spoken, serif italic. speedy_devv's variant: no pill, a 1.5 px colour-matched rectangle with four corner dots, the previous line's words dim to 55 percent grey.

**Layout zones (1080x1920)**: HUD y 90 to 130; caption y 200 to 260 (Family A) or y 110 to 170 (Family B); content y 320 to 1250, single column 760 to 940 px wide, centred; IG UI clear zone right 130 px and bottom 680 px (matches `SAFE` in theme.ts). The final frame holds 2.5 s silent.

## 4. Animation recipes in Remotion terms

All frame-based, fps-aware, written against the kit's conventions (`useCurrentFrame`, `useVideoConfig`, `spring`, `interpolate`, `Easing`, and `pop` / `prog` / `tailFade` from `components/anim.ts`). Frame counts are for 30 fps; speedy_devv renders at 60 fps and his equivalents are double.

Remotion facts used: `spring()` defaults are mass 1, damping 10, stiffness 100, overshootClamping false; `durationInFrames` stretches the curve; `delay` holds the start value; `measureSpring({fps, config})` returns the settle length in frames (damping 200 at 30 fps = 23). `iris()` lives in `@remotion/transitions/iris` since 4.0.316 and takes `{width, height}`. Craft rules worth adopting from vanja.io: arrivals use long-tail ease-out, exits are 40 to 50 percent shorter than entrances, position and scale may bounce but opacity and colour never do, stagger list items 40 to 80 ms (1 to 2 frames) and start the next element when the previous is 30 to 50 percent done, letters 1 frame apart, words 2 to 4 frames apart, sound peaks one frame AFTER the picture.

Add these to `components/anim.ts` first:

```tsx
import { interpolate, spring, Easing } from "remotion";

/** Card drop: ~40 px rise, 4 percent scale, small overshoot. Settles in ~14 f at 30 fps. */
export const DROP = { damping: 14, stiffness: 180, mass: 0.9 };
/** Chip / dot pop: fast, one visible overshoot. ~8 f. */
export const POP = { damping: 12, stiffness: 320, mass: 0.7 };
/** Stamp slap: hard, almost no bounce. ~6 f. */
export const SLAP = { damping: 18, stiffness: 420, mass: 0.6 };
/** Slide: no bounce at all (DM card, HUD fills). */
export const GLIDE = { damping: 200 };

export const EO3 = Easing.out(Easing.cubic);
export const EO2 = Easing.out(Easing.quad);
export const EIO = Easing.inOut(Easing.cubic);

/** spring 0..1 with a frame delay, named config */
export const sp = (frame: number, fps: number, delay: number, config = DROP) =>
  spring({ frame: frame - delay, fps, config });

/** clamped eased 0..1 over [start, start+dur] */
export const ramp = (frame: number, start: number, dur: number, easing = EO3) =>
  interpolate(frame, [start, start + dur], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing });
```

**4.1 Card drop with overshoot** (nxtlvl 12 f, speedy 10 to 15 f at 60)

```tsx
const p = sp(frame, fps, delay, DROP);            // 0 -> ~1.04 -> 1
const style = {
  transform: `translateY(${(1 - p) * 40}px) scale(${0.96 + 0.04 * p})`,
  opacity: Math.min(1, ramp(frame, delay, 5)),    // opacity never bounces: separate linear-ish 5 f fade
};
```

**4.2 Count-up** (18 f, eased, K/M formatting, mono)

```tsx
export const fmtK = (n: number) => n >= 1e6 ? `${(n / 1e6).toFixed(1)} M` : n >= 1e3 ? `${(n / 1e3).toFixed(1)} K` : `${Math.round(n)}`;
const t = ramp(frame, start, 18, EO3);
const value = from + (to - from) * t;              // render fmtK(value); for $ use toLocaleString
// speedy_devv odometer variant: each digit column translates by (digit * lineHeight), eased per column with a 2 f stagger
```

**4.3 Strike-through wipe** (8 f, left to right, slight tilt)

```tsx
const s = ramp(frame, at, 8, EO2);
<span style={{ position: "relative", display: "inline-block" }}>
  {text}
  <span style={{ position: "absolute", left: -4, top: "54%", height: 5, width: `${s * 106}%`, background: C.oxblood, borderRadius: 3, transform: "rotate(-2deg)" }} />
</span>
// nxtlvl also dims the struck text: color: s > 0.9 ? "#9a9a9a" : C.ink
```

**4.4 Stamp slap** (scale 1.4 to 1, rotation settles to -8 degrees, 6 f, shadow lands with it)

```tsx
const p = sp(frame, fps, at, SLAP);                 // 0..1 fast
const scale = 1.4 - 0.4 * p;
const rot = -14 + 6 * p;                            // -14 -> -8
const o = ramp(frame, at, 2);                       // 2 f pop-in, no fade
<div style={{ position: "absolute", right: -18, bottom: -14, transform: `rotate(${rot}deg) scale(${scale})`, opacity: o,
  background: C.green, color: C.cream, fontFamily: F.mono, fontWeight: 700, fontSize: 24, padding: "6px 14px", borderRadius: 6,
  boxShadow: `${3 * p}px ${3 * p}px 0 ${C.black}` }}>FREE</div>
// optional: a 1-frame white flash of the parent card at frame `at` (opacity 0.25 overlay) sells the impact
```

**4.5 Iris / circle wipe** (grow 9 f, hold 0, shrink 9 f; the one full-frame transition per reel)

```tsx
// standalone overlay version (fits the REG/overlay model better than TransitionSeries)
const grow = ramp(frame, 0, 9, EIO), shrink = ramp(frame, 9, 9, EIO);
const r = Math.max(grow - shrink, 0) * 1400;        // px radius, 1400 covers 1080x1920 from centre
<AbsoluteFill style={{ clipPath: `circle(${r}px at 540px 960px)`, background: C.tan }} />
// between two Sequences use: import { iris } from "@remotion/transitions/iris"; presentation={iris({ width, height })} timing={linearTiming({ durationInFrames: 18 })}
```

**4.6 Ghost-then-resolve** ("fetching" entrance: 9 f at 30 percent, then snap)

```tsx
const ghost = frame < at + 9;
const p = sp(frame, fps, at + 9, DROP);
const style = {
  opacity: ghost ? 0.3 : 0.3 + 0.7 * Math.min(1, p),
  filter: `blur(${ghost ? 2 : 2 * (1 - Math.min(1, p))}px)`,
  transform: `translateY(${ghost ? 6 : 6 * (1 - p)}px)`,
};
// in the ghost phase render placeholder bars (#ddd) instead of text so the resolve reads as data arriving
```

**4.7 Typewriter comment** (3 f per character, blinking caret, heart pops 10 f after the last char)

```tsx
const n = Math.min(word.length, Math.floor(Math.max(0, frame - at) / 3));
const caret = n < word.length && frame % 16 < 8 ? "|" : "";
const heart = sp(frame, fps, at + word.length * 3 + 10, POP);
// render word.slice(0, n) + caret ; heart: transform: scale(heart), opacity: heart > 0 ? 1 : 0
// speedy_devv's UI redraws use the same loop for a search bar ("piz|") and a sign-in dialog
```

**4.8 DM notification slide** (card up 60 px, no bounce, then chips fill two per beat)

```tsx
const p = sp(frame, fps, at, GLIDE);
const card = { transform: `translateY(${(1 - p) * 60}px)`, opacity: p };
const chipOn = (i: number) => sp(frame, fps, at + 12 + Math.floor(i / 2) * 9, POP);   // pairs, 9 f apart
// chip: transform: `scale(${0.8 + 0.2 * k})`, opacity: Math.min(1, k * 1.5)
```

**4.9 Progress HUD fill** (one square per item, pop scale 1.3 to 1 over 5 f)

```tsx
const k = sp(frame, fps, fillAt, POP);
const sq = { width: 26, height: 26, borderRadius: 4, border: `2px solid ${C.ink}`, background: filled ? C.tan : "transparent", transform: `scale(${1 + 0.3 * (1 - Math.min(1, k))})` };
```

**4.10 Boxed key word (speedy_devv variant of the accent)** 

```tsx
// box draws in 6 f around the word: scaleX from 0 at left edge, four corner dots pop after
const b = ramp(frame, at, 6, EO3);
<span style={{ position: "relative", padding: "2px 8px" }}>
  {word}
  <span style={{ position: "absolute", inset: 0, border: `1.5px solid ${color}`, transform: `scaleX(${b})`, transformOrigin: "left" }} />
  {[[-3,-3],[-3,null],[null,-3],[null,null]].map(/* 5 px dots at the corners, opacity = ramp(frame, at + 6, 3) */)}
</span>
```

Timing grammar to encode in the EDL generator, not in components: one new element every 27 to 40 frames; list item = 15 f question, 15 f strike, 15 f card, 60 to 90 f chips; chips and caption words land on the spoken word's frame from words.json; exits (tailFade) 4 to 6 f, entrances 8 to 14 f; the final frame holds 75 f with no audio.

## 5. UI sound layer: free packs and how the top creators mix them

**What they actually do.** @ai.nxtlvl: no separately detectable SFX in 52 s, voice mastered to -14.3 LUFS integrated, -0.3 dBTP (measured in the breakdown). @speedy_devv: voice only, no music bed in either clip. @justyn.ai: soft type clicks and a pop on card arrivals under the voice, tied to objects, never to cuts, plus a low music bed. @neuronvisuals family: no voice; trending sound added in the IG app. instaedits (the open-source Claude + Remotion + Edits pipeline): voice normalised to -14 LUFS, music capped at 0.16 linear and ducked to at most 0.6x under speech (0.12 ducked to 0.072 in the example), at most one SFX per six seconds and one riser per video. vanja.io: hits 3 to 6 dB above the bed, sound peak one frame after the picture, rotate 2 to 3 takes of any repeated sound, program -16 to -14 LUFS, -1 dBTP. Our own sound-design doc (2026-11-20): SFX about 6 dB under the voice for cinematic hits, ambience 25 to 30 dB under.

**Our rule for UI ticks** (a pop is a UI tick, not a cinematic hit): chip pops, HUD fills and stamp slaps at -18 to -22 dB relative to voice peak so they are felt, not heard; typewriter key clicks at -24 dB and only on every other character; one soft airy whoosh on the iris at -16 dB, 400 ms, peaking on the frame the circle is largest; nothing on caption words; no bed at all on card-only reels so IG's song mix has room (song at 20 to 30 percent in the app). Keep the final 2.5 s hold silent.

**Free, CC0 sources** (confirm the licence on each page before shipping):
- Kenney UI Audio, 50 files, CC0: https://kenney.nl/assets/ui-audio (button, switch, click). Also on OpenGameArt and the Godot asset library.
- Kenney Interface Sounds, 100 files, CC0: https://kenney.nl/assets/interface-sounds (mirror: https://github.com/Calinou/kenney-interface-sounds).
- sfxmint UI category, 815 sounds in 41 collections, CC0 1.0, WAV + MP3, stable hotlinkable URLs, free API and MCP server: https://sfxmint.com/category/ui (collections: ui-click 69, ui-pop 49, ui-swipe 47 "quick airy whoosh", ui-chime 98 notifications, ui-typing 14).
- Freesound filtered to CC0 (72 percent of the catalogue): https://freesound.org/search/?q=ui+click&f=license:%22Creative+Commons+0%22 ; same for "pop", "whoosh short", "keyboard click".
- itch.io "23 retro UI sound effects" pack, CC0, 44.1 kHz WAV: https://itch.io/t/7191751/free-cc0-pack-23-retro-ui-sound-effects-12-rpg-item-icons-16px
- videoeditingsfx.com UI set, 19 MP3s stated CC0 (homepage wording is looser, so treat as "free commercial"): https://videoeditingsfx.com/free-ui-sound-effects/
- Pixabay sound effects: Pixabay Content Licence (commercial OK, no attribution, not CC0): search "ui click", "pop", "swoosh".
- Not CC0, avoid or read terms: MadRooster / Swish-Swoosh free UI pack (royalty-free, licence unstated), Mixkit (Mixkit licence), CapCut Sounds (non-commercial, TikTok only), Artlist "Clear UI" pack (paid).

Starter kit to drop into `rival-reels/public/sfx/`: `pop_soft.wav` (chip), `tick.wav` (HUD fill), `slap.wav` (stamp: a short low click layered with a paper tap), `key_1..3.wav` (typewriter, rotate), `swipe_air.wav` (iris), `chime_soft.wav` (DM card). Add an `sfx` list to the EDL `{file, at, gain_db}` and mix in ffmpeg after render exactly as the 2026-11-20 sound doc's graph 5b does.

## 6. Components to add to rival-reels next, ordered by value

Each is a `React.FC` registered in `REG` in RivalReel.tsx, receives `dur` (frames) like the rest, and uses the theme tokens. Props sketches only; implementation follows section 4.

1. **ProgressHud** (`hud`) `{ total: number; count: number | { at: number }[]; handle?: string; y?: number; dur }` Persistent across the whole reel (one overlay with `at: 0, dur: full`), `count` either a static number or the list of item start times so it fills itself. Value: retention device on every list reel, zero per-reel cost once built.
2. **StrikeStamp** (`strikestamp`) `{ text: string; tag?: string; stamp: string; icon?: string; price?: string; strikeAt?: number; stampAt?: number; variant?: "bar" | "inline"; dur }` The single-item PAID bar: tag, icon, name, price, strike wipe, then the sticker. Value: the contrast beat of every "stock vs Rival" item.
3. **CountUp** (as a prop on SpecCard and a standalone `countpill`) `{ from?: number; to: number; unit?: string; prefix?: string; at?: number; len?: number; mono?: boolean }` Value: any number on screen reads as evidence when it counts.
4. **CommentGate** (`gate`) `{ word: string; handle?: string; dmTitle: string; items: string[]; typeAt?: number; dmAt?: number; perBeat?: number; dur }` Comment box with typewriter + heart, then the DM card sliding up with numbered chips filling two per beat. Value: demonstrates the ask; nxtlvl got 9,185 comments on 7,259 likes with it.
5. **IrisWipe** (`iris`) `{ color?: string; grow?: number; shrink?: number; cx?: number; cy?: number; dur }` Value: the one sanctioned full-frame transition, 18 frames.
6. **RepoCard / PartCard** (`part`) `{ icon: string; title: string; sub: string; count?: { label: string; to: number; from?: number }; tag?: string; chips: { text: string; at: number }[]; foot?: string; stamp?: { text: string; at: number }; ghost?: boolean; variant?: "soft" | "sticker"; dur }` The nxtlvl payoff card with chips landing on words, a count pill, a footnote and a corner stamp. Value: the template that makes items 2 to 9 cost nothing to read.
7. **GhostCard** (behaviour flag `ghost: true` on PartCard, LogoCard, PhotoCard) `{ ghostFrames?: number }` 9 frames at 30 percent with placeholder bars, then resolve. Value: a "fetching the part" entrance for Fullbay or Marketplace screenshots.
8. **BoxedWord** (caption option) `{ box?: string }` on `Caption`: the speedy_devv selection-box accent with colour-matched outline and corner dots, as an alternative to the pill. Value: a second accent style for the dark Family B look over Jacob's footage.
9. **Chip row** (`chips`) `{ items: { text: string; at: number }[]; x?: number; y?: number; w?: number; fill?: string; dur }` Standalone chip pops for spec lists over footage. Value: cheap, reusable, lands on words.
10. **DmCard** (`dm`) split out of CommentGate `{ title: string; sub?: string; items: string[]; at?: number; dur }` Value: a "what you get" list for sponsor pitches and partner reels.
11. **Odometer** (`odo`) `{ digits: number; to: number; at?: number; len?: number }` speedy_devv's rolling suitcase-lock digits. Value: torque specs, boost, horsepower rolling in.
12. **HardCard variant + tokens** in theme.ts: `hardShadow`, `F.mono` (JetBrains Mono), `C.good`/`C.bad` status colours. Not a component, but everything above needs it; do it first in the same session as ProgressHud.

Suggested first reel with the new pieces: "Every stock part leaving the F600", 9 items, HUD 0/9, StrikeStamp (STOCK → RIVAL or the partner's logo), PartCard with a CountUp (hp, psi, lbs or dollars), 2 to 3 chips per item on the words, IrisWipe into CommentGate("RIVAL", "Your full Rival parts list", 9 items), 2.5 s silent hold. Card-only, cream plate, one per week maximum per the nxtlvl breakdown's "what not to copy".

## Sources

- Keyframes, "How people make those Claude reels on Instagram": https://getkeyframes.com/blogs/guides/how-people-make-claude-reels
- Keyframes product and packs: https://getkeyframes.com/ ; "Claude skills for video: 6 worth installing" (Nov 21 2026): https://getkeyframes.com/blogs/guides/claude-video-skills
- Hugues Bouissonnie, Medium, "My Claude Code reel got 13.5 million views" (403 to fetchers, title and search snippet only): https://medium.com/@hugues.bouiss/my-claude-code-reel-got-13-5-million-views-heres-what-nobody-tells-you-7e6e1c7cc2d6
- Postiz, "Claude Animation: how to make faceless videos (the 265M-view format)", figures as of Nov 16 2026: https://postiz.com/blog/claude-animation-faceless-videos
- promptslove, "I made viral Instagram animations with one Claude skill" (Oct 8 2026): https://promptslove.com/blog/i-made-viral-instagram-animations-with-one-claude-skill/
- oleg.ae creator page for @chandlerintelligence: https://www.oleg.ae/creators/chandlerintelligence
- Apify, "Top 100+ AI influencers to follow on Instagram" (data Mar 31 2026): https://blog.apify.com/top-ai-instagram-influencers/
- hafi.pro most-followed AI and tech accounts (Nov 21 2026): https://hafi.pro/top/most-followed-instagram/ai-tech
- modash US productivity influencers (Nov 9 2026): https://www.modash.io/find-influencers/united-states/productivity
- Brainrot Shorts, "@rick.theengineer formula" (Aug 17 2026): https://www.brainrotshorts.com/blog/how-to-make-animated-explainer-reels
- Weiss Video x Visual Hustles AE course: https://weissvideo.gumroad.com/l/animationcourse
- Ootto, "How are these AI motion graphics reels made" (Nov 1 2026): https://www.ootto.ai/blog/how-are-claude-motion-graphics-reels-made
- ReelDrop, "How to make reels with Claude: 4 methods": https://www.reeldrop.io/blog/how-to-make-reels-with-claude/
- vanja.io, "Motion graphics with Claude Code: engines, craft, rules": https://vanja.io/motion-graphics-claude-code/
- yashm1/instaedits (Claude plans, Remotion renders, Edits assembles; mix levels): https://github.com/yashm1/instaedits
- artemnovitckii/claude-animation-skills: https://github.com/artemnovitckii/claude-animation-skills
- HeyGen HyperFrames: https://github.com/heygen-com/hyperframes
- Anthropic, "Get started with Claude Motion": https://support.claude.com/en/articles/17454997
- Remotion docs: spring https://www.remotion.dev/docs/spring ; measureSpring https://www.remotion.dev/docs/measure-spring ; iris https://www.remotion.dev/docs/transitions/presentations/iris
- Jitter templates and plan limits: https://jitter.video/templates/social-media/
- ManyChat pricing change and comment-to-DM limits: https://www.featurebase.app/blog/manychat-review ; https://creatorlanehq.com/blog/instagram-free-comment-to-dm-2026
- Sound: https://kenney.nl/assets/ui-audio ; https://kenney.nl/assets/interface-sounds ; https://sfxmint.com/category/ui ; https://freesound.org ; https://itch.io/t/7191751/free-cc0-pack-23-retro-ui-sound-effects-12-rpg-item-icons-16px ; https://videoeditingsfx.com/free-ui-sound-effects/
- Our own: `research/2026-11-20-editing-sound-design.md`, `research/2026-11-20-editing-tooling-landscape.md`, the two breakdowns named at the top.
