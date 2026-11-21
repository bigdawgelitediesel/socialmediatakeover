# Marc Cleroux / @tenfoldmarc dossier

Compiled 2026-11-21 for the "learn all of these edit techniques" request (source reel: https://www.instagram.com/reel/Def9pj5TWtA/, "17 video effects Claude can create", posted 2026-10-15, 21,249 likes, 34,194 comments). The frame-by-frame read of that reel lives in `..\2026-11-21-Def9pj5TWtA\`. This file covers everything around it: who he is, what he sells, what his tooling is, his full effect vocabulary, eight of his other videos read from frames, and a ranking of which effects fit El Coyote.

Folder layout:

- `dl\` 16 downloaded TikTok mirrors of his reels, each with `.info.json` (captions, counts)
- `watch-<slug>\<video>\` watch.py output (sheet-01..03.jpg at 1 fps, transcript.txt, words.json, scenes.csv) for 10 videos
- `strips\` 36 hand-cut 10 fps strips (10x2 tiles, 2.0 s windows) of specific effects, filename carries source, start and duration

---

## 1. Who he is

**Marc Cleroux**, French-Canadian (name, French-language PR reimplementations of his work, and his older YouTube Shorts audience suggest Quebec, but no source states a city). Runs **Ten Fold Marketing** (tenfoldmarketing.com, tagline "10X Your Business Growth", support email info@tenfoldmarketing.com). Before the AI pivot his content was agency/coaching marketing: the older YouTube channel `@marc-cleroux` is 30-plus Shorts about closing rates, show-up rates, ads for coaches, "broke coach to $100k per month". In his March 2026 YouTube video he refers to "F and L Fixer" as "our old business" and says he had "just started using Claude Code a couple of weeks ago".

Positioning line on his IG profile (visible in his own follow-button inserts): "Teaching AI to non-technical folks. Automate your ads, business and content with AI." He repeats "I'm not a tech bro, I suck at design" in reels.

He credits the Claude-video-effects trend to other creators: a 2026-10-30 launch-day post thanks **@noevarner.ai** "for inspiring me to start talking about AI", plus **@jessijeanhome, @the.jessicacarter, @itsmegkilgore** (the three creators whose reels orbit him in the Oct 1 reel) and **@justyn.ai** "for being in the trenches with me" (justyn.ai runs a parallel "AI Video Editor, 40+ effects, works in ChatGPT and Claude" product; Digital Zoom Studio wrote up his 20-effect reel on 2026-10-28). The Nov 18 text-sandwich reel credits **@itsbaileymacninch** for the effect idea. He has also done "Claude vs Ali Abdaal's editor" and "Claude vs Diary of a CEO" comparison reels.

### Numbers, dated

| Date | Platform | Figure | Source |
|---|---|---|---|
| 2026-03-05 | Instagram | 0 to 2,000 followers "in one week" after building an IG analytics dashboard with Claude Code | YouTube video 0vD-mC1luN4 description |
| 2026-04-08 | Instagram | "0 to 22K followers in 30 days" | guide title, guides.tenfoldmarketing.com |
| 2026-06-02 | Instagram | "60K followers in 60 days" + $12,230.34 revenue | "SYSTEM" guide |
| undated (Sonnet 5 video) | Instagram | "84k" | YouTube channel description |
| 2026-09-22 / 10-02 | Instagram | ~102K / 102,986; +23K in prior 90 days; 3.2% engagement; est. $2.1K to $5.1K per sponsored post | creatordb.app |
| 2026-10-01 | Instagram | 103K followers, 372 posts | his own profile insert in the Oct 1 reel |
| 2026-10-18 | Instagram | "Claude just grew my account by 14k followers in 7 days" | TikTok caption |
| 2026-11-08 | Instagram | 125K followers, 405 posts | profile insert, Nov 8 reel |
| 2026-11-18 | Instagram | 126K followers, 410 posts, 221 following | profile insert, Nov 18 reel |
| 2026-11 | TikTok @tenfoldmarc | 6,843 followers, 40.2K likes; top video 73.7K views (the Oct 15 effects reel), most others 700 to 1,200 | TikTok profile / yt-dlp |
| 2026-11-21 | YouTube "Marc Cleroux" (UCOhbq9sinCaT92xcibJ_m2A) | 1,770 subscribers, 7 long videos (top: "Build a Custom AI Business Dashboard With Claude Code" 32K, "5 Hacks To Create $10k Websites" 12K) | yt-dlp |
| 2026-11-21 | Threads | 555 followers | threads.com |
| 2026-11-21 | GitHub tenfoldmarc | 144 followers, 68 repos; llm-council-skill 1.1k stars, website-builder-setup 391, video-edit-skill 164 (36 forks), studio-plugin 13 | github.com |
| 2026-11-21 | Skool "AI Builders - Ten Fold" | 76 members | skool.com/ten-fold/about |

Read on the growth: Instagram is the whole business (TikTok and YouTube are mirrors with under 1 percent of the audience). Growth came in two bursts, Feb to Jun 2026 (carousel + hook-bank system) and Oct 2026 (the Claude video-effects reels, +14K in a week). The 34K comments on the source reel are a keyword DM funnel ("comment STUDIO"), not conversation. Engagement is roughly 2x the category median per creatordb.

### What he sells and for how much

| Product | Price | Notes |
|---|---|---|
| **Claude Creator Studio** (the "Studio" in every reel) | not published; invite link by DM after commenting STUDIO / SYSTEM, waitlist "link in bio" | Launched ~2026-10-30 (his #digitalproductlaunch shoutout post). Delivered as a Claude Code plugin marketplace `tenfoldmarc/studio-plugin` with three plugins: `video-studio` (edit raw clips into a finished reel), `carousel-studio`, `script-studio`. Latest release v2.7.1 on 2026-10-30 (iPhone sideways-clip zoom crash fix, lip-sync drift fix). A Codex edition exists (`studio-plugin-codex`). Buyer portal with walkthrough videos at portal.tenfoldmarketing.com. Pitched features: edit "in your own style", analyze reference reels and copy their look, 26 then "46" effects, turn one video into 10 trial reels, auto-post, video to carousel, Arcads-generated B-roll |
| **AI Builders - Ten Fold** (Skool) | $59/month for the first 150 members, $29/month on annual, "price rises at 150" | Go Viral System, Marketing OS, 6-module Claude Code Mastery, "$10k Website Creation Mastery", 56+ custom skills, weekly calls. Last updated Oct 15 |
| **video-edit-skill** (GitHub, free) | $0 | The Oct 1 free skill; he says "20,000 of you downloaded" it by Oct 14. This is the public ancestor of Creator Studio and the best window into his pipeline (section 3) |
| **128 free guides** at guides.tenfoldmarketing.com | $0, email-gated per guide via comment keywords | Categories: Claude Code 39, Skills & Agents 23, Marketing & Sales 22, Websites & Apps 13, Content & Social 12, Video & Media 12, Money & Trading 7 |

Podcast / newsletter / X: a Spotify episode titled "Marc Cleroux - AI Builders - Ten Fold" exists but has no indexed description; no X account, Substack or beehiiv surfaced. His Instagram is login-walled and third-party mirrors (imginn, picuki/tikvib) returned 403 or paywalls, so the follower figures above come from his own on-screen inserts and creatordb.

---

## 2. Tooling and pipeline

**Short answer: not Remotion, not After Effects, not CapCut. It is HyperFrames (HeyGen's open-source HTML-to-video renderer) driven by Claude Code, with GSAP timelines, faster-whisper for word timing, ffmpeg for cutting, and HyperFrames' built-in background removal for the matte.** Claude "creates" an effect by writing an HTML composition (divs, CSS, a GSAP timeline) that HyperFrames renders frame by frame in headless Chrome and encodes with ffmpeg. Every effect is therefore code generated per edit from a skill's written description, not a template library.

Evidence and timeline:

- **2026-03-23**: his first video guide is "How to Edit Videos With AI for Free (Using Remotion + Claude Code)" (Notion page, not fetchable). So he started on Remotion.
- **2026-09-10**: "The Prompt That Edited My Reel With Zero Editing Skills" guide. Pipeline named explicitly: Claude Code (Opus) + **HyperFrames** ("each edit is one HTML file plus a GSAP timeline, rendered to MP4 in headless Chrome") + faster-whisper small.en + ffmpeg/ffprobe + Google Fonts (Archivo, IBM Plex Mono). Effects in that prompt: karaoke captions on a frosted plate, versus card, slamming "0", terminal typing the prompt, comment bubble typing "edit", follow button flipping to Following.
- **2026-10-01**: `video-edit-skill` published. README credits HyperFrames "for HTML-to-video rendering and background removal", faster-whisper, ffmpeg, Node 22+, Python 3.10+, optional Apify (to pull the user's own reels for orbit/profile inserts). Remotion is gone.
- **2026-10-30**: Creator Studio 2.7.1. Same stack, now private.
- **2026-11-10**: "EDIT" guide adds **Arcads** (via a Claude custom connector, mcp.arcads.ai) for generated overlays, B-roll, logo animations and SFX; the Nov 11 "Diary of a CEO" reel shows "Generated b-roll on Arcads" in the task list.

### The video-edit-skill pipeline (his own SKILL.md and references, paraphrased)

1. Intake: clips to a project folder; `ingest.py` builds contact sheets and transcripts (faster-whisper, word-level).
2. Take selection: rebuild the script from all takes, keep the cleanest take per line, cut dead air (confirm with ffmpeg silencedetect n=-40dB d=0.08 because Whisper word starts drift 0.1 to 0.3 s), write `edl.json`.
3. `assemble.py` concatenates from the originals (sharp punch-ins cropped from 4K), re-encodes to constant 30 fps (`setpts=N/30/TB`, `-fps_mode cfr`) because concat offsets and VFR make the matte drift.
4. `cutout.py` runs `npx hyperframes remove-background` (CoreML on Apple Silicon, CPU on Windows) to get a person matte; `headpos.py` finds head top and chin per word so words can sit behind the head.
5. Inserts (app windows, IG profile, scrolling file) are built by **parallel Opus sub-agents**, each as its own HyperFrames project rendered to a **transparent VP9 WebM** at fixed size and duration, then placed with a wrapper div (position, scale, tilt) in the main composition. Timing is locked to word timestamps first (±0.05 s beats).
6. Main `build.py` writes the HTML: a paused GSAP timeline named "main"; `fromTo` tweens with `immediateRender:false`; typed text as one span per character revealed by `tl.set`; every `<video>` needs an id and its own `data-track-index`.
7. Lint, snapshot 10 to 20 frames with a red safe-zone overlay (`--safe`), render with HyperFrames, then `check_cuts.py` extracts frames from the final MP4 to verify every cut (snapshots seek approximately and lie by a frame).
8. Deliver a 720p crf 26 to 28 phone copy plus the full render; every version kept in `renders/`.

### The "matte sandwich" (the single idea behind most of the effects)

Layer order, bottom to top: **base video** (full frame, often graded or blurred) > **back layer** (anything that should appear behind the person: big words, reel tiles, phone mockups, wallpaper) > **person cutout** (base video multiplied by the alpha matte) > **front layer** (captions, cards, magazine frame, stickers). Orbit, couch wall, headline wall, cover story, glass type, spotlight, pastel word, text sandwich, green screen all reduce to "put something on the back layer". The community rebuilds (section 4) all converged on the same structure.

### House numbers worth stealing (from his looks.md / layout.md)

- Canvas 1080x1920, 30 fps. Safe zones: top 220 px, bottom 450 px (nothing below y=1470), 35 px each side, right 100 px column clear from y≈1155 down.
- Lead-in captions centered in the chest band y 950 to 1300; never over the face (eyes to chin).
- Word pop: scale 1.22 + 22 px blur to 1 in 0.2 s, power3.out; groups blur out in 0.12 s. Every cut gets a stage punch 1.05 to 1 over 0.32 s.
- Behind-head word placement: top = head_top minus 0.57 x font size; only the bottom 25 to 30 percent of letters may be hidden or it "reads as broken".
- Orbit: each tile exists twice (back copy below the cutout, front copy above), GSAP keyframes every 0.1 s around an ellipse, `autoAlpha` swapped at the ring's left and right extremes, tiles 190x338 (or 260x462 for creator cards with a white border and a -7 or +6 degree tilt plus an @handle pill).
- Accent colour butter yellow #FAE67A; fonts Inter Tight 800/900 (bold look), Instrument Serif italic (cool girl), DM Serif Display + Montserrat tracked caps (cool dude), Caveat for handwriting, JetBrains Mono for code.
- His "avoid" list: orange captions, **Anton or condensed poster caps**, black-and-white grades, corner @handle watermarks, date stamps, AI backgrounds, crushed darks, film grain. (Note: El Coyote's locked typography is Anton + Oswald + Inter, so his avoid list is his taste for a lifestyle/AI-tips account, not a law. Our reel-look rule "no grade, light clean captions" agrees with his no-grain, no-crushed-darks stance.)
- Gotchas that will bite us on Windows: iPhone/HLG BT.2020 footage loses alpha unless converted to BT.709 before matting (we already hit the HLG issue on Jacob's footage); CSS masks do not survive the renderer (bake alpha into WebM with ffmpeg alphamerge); heavy backdrop-filter on many elements turns captures black; no GPU matte path on Windows without a CUDA onnxruntime build.

### Public code

- https://github.com/tenfoldmarc/video-edit-skill (his, free, 164 stars): SKILL.md, scripts/, references/looks.md, layout.md, overlays.md, gotchas.md. The orbit, three looks and three inserts are fully specified here. The 17/26/46 effects are **not** in it.
- https://github.com/tenfoldmarc/studio-plugin (paid product's installer; the actual skill content is pulled from a private source at install).
- The 17-effect code "is exchanged for a comment" and never published. Three independent rebuilds exist (section 4).

---

## 3. His effect vocabulary

He has now named roughly 50 effects across four list reels plus one-off demos. He says "26" on Oct 15 to Oct 30, then "all 46" on Oct 21 (the Studio count), and the Nov 8 reel is "16 new" and Nov 19 "10 new". The names are marketing labels; the classic editing name is in column 2.

Columns: **Classic** = what an editor would call it. **Mechanics** = what moves, layers, timing as observed in his frames (1 s per effect in list reels, so entrances are 0.2 to 0.4 s, holds 0.6 s). **Footage** = what you must shoot. **Solo** = difficulty for a one-man phone shooter (Easy / Medium / Hard, counting both the shoot and the edit). **Feasible** = how we would build it: `ffmpeg` (pure filters, build_reel2 territory), `comp` (needs a compositor: Remotion or HyperFrames, HTML/React over video), `matte` (also needs a person cutout).

### 3a. The original 17 (Oct 15 reel)

| # | Name | Classic | Mechanics (observed) | Footage | Solo | Feasible |
|---|---|---|---|---|---|---|
| 1 | orbit | 3D card carousel / orbiting layers | 5 to 6 portrait reel tiles circle the head on a tilted ellipse, passing in front of and behind him (two copies per tile, alpha-swapped at the extremes). ~2 s per revolution, linear. Gold script caption in his version | locked-off talking head, plus 6 clips to use as tiles | Medium (needs own reels + matte) | comp + matte |
| 2 | couch wall | multi-clip wall / video wallpaper | a dense grid of post and reel thumbnails fills the wall behind him, staggered blur-to-sharp with slight scale up; he stays sharp in front. In the Oct 21 outro the wall also scrolls slowly | static shot in front of a plain wall | Medium | comp + matte |
| 3 | ui world | subject composited inside an app UI | frame splits: mock AI app chrome on top, his clip inside a window, thumbnails fly in and a command types itself ("edit my reel", progress 0 to 100 percent, timeline strip below) | any clip | Medium (design work) | comp |
| 4 | frame break | pop-out / break-the-frame | the full-bleed video shrinks into a rounded social-post card (likes, follow pill, handle) while his gesturing hand breaks past the card edge via the matte copy drawn outside the clip. ~0.3 s shrink, back-ease | gesture toward camera | Medium | comp + matte |
| 5 | digital zoom | punch-in with HUD / viewfinder overlay | slow push 1.0 to ~1.18 with word captions, then a hard punch to ~1.3 on the emphasis word; REC dot, timecode, corner brackets and a "1.51x ... 1.60x" readout counting up | any; must be shot 4K for a clean 1.5x crop | Easy | ffmpeg |
| 6 | phone mockup | device mockup insert | a CSS phone with a scrolling app screen slides in from the left, tilted ~10 degrees, settles beside the shoulder; content inside scrolls | any | Easy to Medium | comp |
| 7 | checklist | animated to-do card | translucent card; rows tick green one by one in sync with spoken words (stroke-drawn checkmarks), counter and progress bar | any | Easy | comp |
| 8 | headline wall | paper collage / clippings | newspaper-style clippings and cards pop onto the wall behind the head with seeded random rotations, back-ease pops, staggered ~80 ms | plain wall | Medium | comp + matte |
| 9 | zoom-through cut | zoom transition with radial blur (whip zoom) | shot A scales up fast into a radial blur and a white flash, hard cut at the peak to shot B which settles from oversized and blurred. ~8 frames total in his version. Whoosh SFX | two shots; works best if B is framed as a detail of A | Easy | ffmpeg (zoompan + radial-ish blur via stacked scaled copies) |
| 10 | chart grow | animated line chart / data reveal | dark grade; a glowing SVG polyline draws point by point across a weekday axis (dash-offset tween), dots pop at each point, his hand sweeps along it. Base video darkened ~25 percent | plan the hand sweep | Easy | comp |
| 11 | pull-back reveal | reveal shot is inside an editor / infinite zoom-out | motion blur, then the clip is revealed as a small preview window inside a dark NLE UI (timeline, waveform, "cut pauses / add effects / export" checklist ticking), camera pulls back over ~1 s | any | Medium | comp |
| 12 | green screen | keyed subject over a graphic plate | he is matted over a full UI (focus timer, task rows) with a highlighted word behind the chest; stepped digit swaps, cursor path | plain background helps the matte | Medium | comp + matte |
| 13 | paper cut | cut-and-paste collage / ransom note | brief REC HUD frame, then a white die-cut sticker outline around his matte, grid-paper background, torn tape, the words "paper cut" stamped letter by letter in mismatched ransom tiles, red scribble circle. Letters land ~70 ms apart | plain background | Medium | comp + matte |
| 14 | doodle boil | line boil / hand-drawn rotoscope outline | a chalky white outline (dilated matte minus matte) traces his body and jitters at ~10 fps (stepped displacement), coloured doodles and stars drift and recolor; runs ~1.3 s | any | Medium (edit), Easy (shoot) | comp + matte (or ffmpeg edge + displace) |
| 15 | vertigo | dolly zoom / Hitchcock zoom | the background scales 1 to ~1.35 while the matted subject holds size; a faint seam shows at the head if the clean plate is not inpainted. Pure post version. In-camera version is a walk-back-while-zoom | locked-off subject; or walk backward while zooming in | Easy (post) / Medium (in camera) | ffmpeg (scale + overlay) + matte |
| 16 | cover story | magazine cover | large serif masthead behind the head, thin inner border, cover lines, barcode, date line; the shot often desaturates | plain background | Easy | comp + matte |
| 17 | glass type | frosted extruded 3D type / liquid glass | a thick translucent word behind him with refraction layers (stacked offset copies, gradient text clip, blurred caustic highlight) | plain background | Medium | comp + matte (backdrop-filter heavy) |

### 3b. Added in the Oct 21 "16 video effects" list reel (Studio launch list)

| Name | Classic | Mechanics | Footage | Solo | Feasible |
|---|---|---|---|---|---|
| sticky text | tracked label / pointer tag | a yellow pill "12 sticky text" is pinned to his raised index finger and follows it for ~1.5 s with a tiny lag | point at something and keep the finger in frame | Medium (tracking) | comp (needs a track; Pocket 3 footage is stable enough for a manual 5-key track) |
| before + after | wipe reveal / split slider | a bright vertical light bar sweeps left to right over ~0.6 s, graded "before" on the left becomes "after" on the right, labels on each side | one shot, or two aligned shots | Easy | ffmpeg (crop + overlay with a moving x) |
| depth scatter | parallax type / layered text in Z | "depth" in white behind the head, "scatter" in yellow in front over the chest, both drift at different rates like a 2.5D parallax, soft blur on the back word | plain background | Easy | comp + matte |
| comment bubble | UI insert | an IG comment box types "STUDIO", posts, a reply drops in; used as the CTA in every reel | none | Easy | comp |

### 3c. The Nov 8 "16 new video effects" list (demoed inside a phone card)

| Name | Classic | Mechanics | Footage | Solo | Feasible |
|---|---|---|---|---|---|
| type wall | kinetic typography wallpaper | giant repeating uppercase words ("EVERYBODY'S EVERYBODY'S") scroll horizontally behind the matte | plain wall | Easy | comp + matte |
| the stack | stacked cards / document stack | a white document card with a bar chart stacks above the clip; layered sheets | none | Easy | comp |
| depth scatter | see 3b | | | | |
| rack focus | focus pull (post) | background blurs out while the subject stays sharp, then flips; needs the matte for the post version. In camera, the Pocket 3 can do it with a tap | subject plus a background object | Easy | ffmpeg + matte |
| spatial glass | visionOS-style glass panels | frosted panels with a video thumbnail and a checklist float at a slight angle beside him | none | Medium | comp |
| scene text | text locked to the scene (3D track) | a word sits "on" the wall behind him and holds position as the camera moves | handheld push-in | Hard (needs camera solve) | comp + track |
| freeze sticker | freeze frame + sticker cut-out | the frame freezes, he is cut out as a white-bordered sticker on a blue radial-burst background, a "CERTIFIED NOT a tech bro" handwritten label writes on, then the sticker tilts and flies out | any | Medium | comp + matte |
| sticky text | see 3b | | | | |
| clone | split-screen clone / duplicate self | two copies of him in one frame (locked-off shot, two takes, matte or split) with "or like that" caption | locked-off, two takes, do not cross the center | Easy to shoot, Medium to edit | ffmpeg (hard split) or matte |
| blackout | lights-out / spotlight dim | the room drops to near black and only he stays lit; the word "time" in yellow behind | any | Easy | comp + matte (or just a vignette for a cheap version) |
| freeze + label | freeze frame with callout labels | freeze, zoom slightly, two or three small labels with thin leader lines pop onto parts of the frame ("sucks at design") | any | Easy | comp |
| shatter 3d | glass shatter transition | the frame breaks into shards that fall away revealing the next shot | two shots | Medium | comp (canvas/three.js) |
| chip row | pill / chip tags row | a row of rounded chips ("edits", "edits + posts") animate in under a serif title | none | Easy | comp |
| serif flow | serif text animation | large serif italic words ("five variations") fade and drift up on a dark green plate | none | Easy | comp |
| spotlight | spotlight word behind head | "stand out" in big type behind him, one word white one yellow, room darkened | plain background | Easy | comp + matte |
| prompt box | chat input insert | a Claude-style prompt bar types the command over the clip | none | Easy | comp |

### 3d. The Nov 19 "10 new video effects" list (all gesture-driven, physical)

| Name | Classic | Mechanics | Footage | Solo | Feasible |
|---|---|---|---|---|---|
| air marker | hand-drawn annotation following the hand | he draws a circle in the air with a finger; a red marker stroke follows the fingertip and the circled text ("the hook") pops in. Stroke is a dash-offset SVG tied to a hand track | deliberate slow circle gesture | Medium | comp + hand track |
| screen dive | zoom into a device screen (match move) | he holds a phone up; the camera pushes into the phone screen and the screen's content becomes the next shot (screen recording), finishing on a laptop screen | hold the phone steady, 1 s push | Medium | comp (corner-pin) |
| finger tags | finger counting labels | holding up 1, 2, 3 fingers; "step 1 / step 2 / step 3" tags with leader lines attach to each fingertip as it appears | count on fingers slowly | Medium | comp + track |
| face lock | face-tracked crop / locked-on | corner brackets lock onto the face, then a stack of polaroid-style frames of past clips flips through while his face stays centered in each | several old clips | Medium | comp + face detect (OpenCV YuNet) |
| swipe | screen swipe transition | a diagonal wipe with a thin white edge pushes shot A off and shot B on, following a hand swipe | swipe hand across frame | Easy | ffmpeg (xfade custom) |
| hand frame | finger-frame viewfinder | he makes an L-shaped finger frame; the region between his hands becomes a sharp "viewfinder" while the rest blurs or a label fills it | hold the finger frame still | Medium | comp + track |
| pocket proof | pull a card out of your pocket | he reaches down and "pulls" a receipt/screenshot card ("$68,766") up from out of frame; the card is pinned to the hand position, then he tosses it away | reach down, lift, flick | Medium | comp + track |
| clap wave | clap-triggered wall reveal | he claps; a shockwave reveals a wall of reel thumbnails behind him | clap on beat | Easy | comp + matte |
| ball toss | prop toss transition | he tosses a white ball up; the frame follows it into a white flash and the next shot | toss a real object | Easy | ffmpeg (flash xfade) |
| rewind | VHS rewind / reverse | the shot runs backward with a bleach flash and a "rewind" tag | any | Easy | ffmpeg (reverse) |

### 3e. One-off demos

| Name | Classic | Mechanics | Source |
|---|---|---|---|
| Spotify scroll | screen replacement / fake interaction | he mimes scrolling with a finger; a tilted phone card showing a Spotify list scrolls in sync and a song "taps"; a second version has the card translucent so his face shows through | Oct 17 / 26 / 30 reposts |
| the rip | paper tear transition | a jagged tear splits the frame vertically with white torn edges and reveals a second take of himself behind; ~0.5 s | Oct 18 "even the rip" |
| text sandwich | text behind subject, outline in front | "TEXT EFFECT" in yellow with a pink outline; the fill sits behind him, the outline in front, so he walks "through" the word. Task list shown: found the effect in the reference, cut you out, sandwiched the text, graded your D-Log footage | Nov 18 (credit @itsbaileymacninch) |
| DOAC look | podcast cinematic grade | dark cinematic grade, mixed caption styles (bold uppercase red, serif italic, pill), Arcads-generated B-roll inserts ("$20K in debt at 20") | Nov 11 "Can Claude edit like Diary of a CEO" |
| 20 movies | film-look presets | "20 different movies Claude can recreate for you" (Nov 13); not downloaded |

---

## 4. Community rebuilds (free, public, useful as reference code)

None are his code, but they document the same 17 effects and the same layer logic, and two of them are complete Claude Code skills we could install and read.

| Repo | What | Stack | Notes |
|---|---|---|---|
| ONIKOSIOLA/video-editing-kit, `skills/video-overlays/reel-effects-17.md` | plan-by-plan rebuild of the 17 with layer notes | HyperFrames, ffmpeg, MediaPipe | only cover story verified, paper cut and vertigo partial; same HLG/BT.2020 trap noted |
| itsCet/Your-AI PR #13 (merged 2026-10-28, French) | 13 of the 17 as `js/reel.js` in a browser canvas engine | MediaPipe in-browser cutout | explicitly states his code "is exchanged for a comment", so they rebuilt from descriptions |
| Vibha-Ramprakash/claude-video-effects (1.1k stars) | 51 effects as `/effects`, face tracking, behind-head layers | ffmpeg + Python 3.12, OpenCV YuNet faces, MediaPipe Selfie Segmenter | **ffmpeg-only**, which is closest to our build_reel2 stack. Effects 1.5 to 4 s. Names overlap his (orbit, headline-wall, checklist, cover-star, spotlight, rabbit-hole, over-the-shoulder-zoom) |
| adamgodigital/claude-reel-effects (55 effects, free with email) | same family, grouped: behind-head 12, reels-around-you 9, cards/UI 16, layouts/looks 13, camera moves 5 | Claude Code skill | adds captions in 4 styles, pause trimming, `/effects full edit` |
| Dryxio/effects-skill (French, 36 effects) | `/effects spotlight` renders 4K | **Remotion** + BiRefNet cutout (1 GB model, ~15 s/frame on CPU) | proves the Remotion route; notes Remotion licence is free up to 3 people |
| HyperFrames itself (heygen-com/hyperframes, Apache 2.0) | the renderer; Claude Code plugin `claude plugin marketplace add heygen-com/hyperframes` | Puppeteer + ffmpeg, GSAP/CSS/Lottie/three.js adapters | has `/reverse-any-video` and `/style-sampling` skills, which is how his "copy this reference reel's look" works |

---

## 5. Downloaded examples, read from frames

All eight below were run through watch.py (1 fps sheets, Whisper transcript, PySceneDetect cuts) and then cut into 10 fps strips for the moments that matter. Paths are relative to this folder.

### 5.1 `watch-standout-hit-oct15` (TikTok 7696732316181351700, 2026-10-15, 29 s, 73.7K views, 2,425 likes, 1,212 shares)

TikTok mirror of the source reel. Same 17-name run at ~1.0 s per effect (scene cuts at 2.9, 5.2, 6.3, 7.3, 8.5, 10.8, 12.2, 13.3, 14.2, 15.2, 16.2, 17.5, 18.4 s), then a 10 s pitch. Whisper hears "vertical" for "vertigo". It is his best-performing TikTok by 7x, and the share count (1,212 on 73.7K views, 1.6 percent) is the signal: list reels of named effects get saved and shared. Not re-read here; see the parent folder.

### 5.2 `watch-effects-list-oct21` (7699170314885844245, 2026-10-21, 35 s, 2,384 views)

Second list reel, "16 video effects claude can create" with a two-column sidebar that highlights the current item in yellow. Order: headline wall, zoom-through cut, vertigo, green screen, phone mockup, digital zoom, paper cut, ui world, orbit, frame break, doodle boil, sticky text, before + after, pull-back reveal, depth scatter, comment bubble. Precise reads from the strips:

- **headline wall** (0 to 1.0 s): he holds a physical newspaper-clipping card "claude can now edit your videos" in front of his chest; more clippings sit on the wall behind. Hard cut into:
- **zoom-through cut** (1.0 to 1.5 s): frames 4 to 6 of the strip show the clipping scaling up with heavy radial blur, a yellow-white flash at frame 5, then shot B (same framing, no clipping) lands sharp by frame 7. Total transition 5 frames at 10 fps, so ~0.4 s, with the cut hidden inside the flash.
- **vertigo** (4.4 to 5.5 s): subtle. Background lamp and shelves grow ~15 percent over 1 s while he holds size. Readable only if you watch the lamp. Lesson: a post dolly zoom needs a background with strong lines.
- **green screen** (5.5 to 6.6 s): his matte over a dark grey UI plate.
- **phone mockup** (6.6 to 7.5 s): the phone enters from the left edge rotated ~15 degrees, decelerates into place beside his shoulder in ~0.3 s (back-ease overshoot visible at frame 3), screen content scrolls for the rest of the second.
- **digital zoom** (7.5 to 8.6 s): motion-blur punch at frame 2, then corner brackets, REC dot, timecode "00:00:04" and a magnification readout climbing 1.51x, 1.52x, 1.54x, 1.56x ... 1.60x, i.e. the zoom keeps creeping ~0.02x per frame after the punch.
- **paper cut** (8.6 to 9.4 s): cut to a 1.60x framing, then the matte gets a white die-cut border, yellow-green grid-paper background, "paper cut" lands as ransom-note tiles one letter per frame (~100 ms), a torn-tape strip rotates in top-right.
- **ui world** (9.4 to 10.4 s): a dark app frame builds in two frames (tool rail, "edit my reel" typing, "editing... 0% > 2% > 29% > 85% > 100%" over 0.6 s, live preview tile, timeline strip of thumbnails at the bottom).
- **orbit** (10.4 to 11.7 s): three to four tiles labelled with other effect names circle him once in ~1.2 s, visibly passing in front of his face on the near side and behind on the far side.
- **frame break** (11.7 s): one frame of glass shards and a polygon mesh, then the clip is a rounded social card with like icons and a follow pill; his hand extends beyond the card's left edge.
- **doodle boil** (11.9 to 13.0 s): the white chalk outline appears at frame 3, and the strip shows it jittering position every frame with coloured scribbles (rings, stars, tally marks) drawn over his chest and arm; the outline is clearly a dilated matte because it tracks his hands exactly.
- **sticky text** (13.0 to 14.0 s): the "12 sticky text" pill appears next to his raised finger and rides it as he wags it left and right across ~10 frames with a one-frame lag.
- **before + after** (14.0 to 14.6 s): the light bar enters from the right edge at frame 1 and crosses to the left by frame 8 (~0.7 s), "before" label on the left, "after" on the right, the two halves differ by a warm grade.
- **pull-back reveal** (14.6 to 16.0 s): whip blur, then his clip is the preview monitor inside a dark NLE with a green waveform and purple clip blocks; a checklist card (cut pauses, add effects, export) ticks in three steps ~0.3 s apart.
- **depth scatter** (16.0 to 17.3 s): "depth" in white sits behind his head, "scatter" in yellow in front across his chest; both drift slightly in opposite directions.
- **comment bubble** and **couch wall** (17.2 to 19.5 s): the 16-item sidebar fades out, then a wall of ~40 reel thumbnails pops onto the back layer in two bursts (frame 3 and frame 5 of the second strip) behind "to get all 46 video effects", with the wall sharp and him sharp, no depth blur.
- **trial reels insert** (24 to 26 s): a translucent portrait card of his own clip slides in from the right edge over ~0.4 s and stops at the right safe-zone margin, then multiplies into a fan of ten cards for "10 trial reels", then a mock "Posting 10 trial reels to Instagram" notification.
- CTA: typed comment "STUDIO" in a dark comment bar, then the follow button flips to Following.

### 5.3 `watch-16-effects-nov08` (7705944517094182164, 2026-11-08, 34 s, 3,624 views, 141 likes, 42 shares)

Different format: he sits in a beige sweater, and each effect plays inside a small floating phone card (~320x560 px) at his chest with a "01/16" counter, while a two-column sidebar highlights the name. Order: type wall, the stack, depth scatter, rack focus, spatial glass, scene text, freeze sticker, sticky text, clone, blackout, freeze + label, shatter 3d, chip row, serif flow, spotlight, prompt box. Scene cuts every 1.0 to 1.6 s. Observations from the strips: type wall scrolls the repeated word right to left at roughly one word per 0.5 s behind his matte; the stack places a white chart document above a second card; rack focus blurs the room and keeps him sharp, then at 4.2 s a serif "Skill" label fades in; spatial glass is a floating frosted panel with a small checklist and a yellow progress dot; freeze sticker turns his frame into a white-bordered cut-out on a blue radial-burst background with a handwritten "CERTIFIED NOT a tech bro" label writing on over ~0.5 s, then the sticker tilts and exits top-right in two frames; clone is two of him on the same couch; blackout drops the room to black behind "time"; freeze + label adds two small callouts with leader lines; shatter 3d shows the frame fracturing into shards over ~0.4 s; chip row and serif flow are typographic cards on a dark green plate ("five variations", "edits + posts"); spotlight is "stand / out" behind the head with the room darkened; prompt box is a typed command bar. Pitch: "16 effects and a way to get Claude to edit your videos, turn them into carousels and trial reels and post them automatically". CTA profile insert reads 125K followers.

### 5.4 `watch-favorite-nov19` (7709733260590337301, 2026-11-19, 20 s, 781 views)

"10 new video effects claude can create", all gesture-triggered, black fleece on a green chair, no sidebar, bottom-left label "01 air marker" etc. From the strips:

- **air marker** (0 to 1.6 s): his finger starts the circle at frame 1; the red marker stroke begins at frame 2 and the "the hook" label pops at frame 4 (~0.3 s in); the stroke keeps drawing for 10 more frames and finishes as a closed ellipse at frame 14 (1.4 s). The stroke lags the fingertip by about one frame.
- **screen dive** (1.6 to 3.4 s): he raises a black phone (frames 1 to 6, phone dark), the phone screen lights up with his own clip at frame 7, and from 2.6 s the whole frame pushes into the phone with motion blur over 3 frames, lands inside a screen recording ("well, because it always felt like... this UNATTAINABLE"), then a laptop-screen wide shot. Corner-pin plus a match-moved push.
- **finger tags** (3.4 to 5.1 s): "step 1" tag with a thin leader line attaches to the index finger at frame 6 (0.5 s after the finger is up); "step 2" and "step 3" attach as each finger rises, each tag offset so they stack diagonally.
- **face lock** (5.1 to 6.9 s): brackets lock his face, then 9 different past clips flash as white-bordered tilted polaroids at ~5 per second, each with his face centered, the background dark and blurred.
- **swipe** (6.9 to 8.0 s): a diagonal wipe with a bright thin edge sweeps from upper-right to lower-left in 5 frames (0.5 s), revealing shot B (a camera on a tripod) then wiping back to him as his arm sweeps.
- **hand frame** (8.0 to 9.9 s): he forms an L-frame with both hands; a sharp rectangular "viewfinder" region appears between his hands at frame 7 and holds for ~1 s while he keeps the frame still.
- **pocket proof** (9.9 to 11.6 s): he reaches down out of frame, and as the hand rises a tilted screenshot card "$68,766" rises with it, pinned to the hand, holds 0.5 s, then is flicked up out of frame with motion blur in 2 frames.
- **clap wave** (11.6 to 13.0 s): hands together, and on the clap the reel-thumbnail wall is instantly present behind him (no visible ripple in the strip; the reveal is a one-frame cut on the clap).
- **ball toss** (13.0 to 15.4 s): he tosses a white ball; frames 6 to 9 track it upward, frame 10 is a whip-pan blur, frames 11 to 13 are a white flash that dissolves into shot B ("rewind").
- **rewind** (15.4 s): bleach-white flash, then the previous second plays backward with a "rewind" tag.

### 5.5 `watch-first-claude-edit-oct01` (7691841945886297364, 2026-10-01, 24 s, 9,399 views, 292 comments, 79 shares)

The free-skill launch reel and the best demo of his three looks in one piece. 0 to 5 s **bold look**: he sits on a couch, two creator reel cards (@itsmegkilgore, @the.jessicacarter) tilted beside him with handle pills, white Inter Tight lowercase captions, yellow punch word ("videos."), then a huge "course" behind his head. 5 to 7 s: "no sense" slams in yellow at 300 px with a SKILL.md code card behind him. 7 to 13 s **cool girl**: warm sepia grade, "cool girl" in Instrument Serif italic yellow with sparkles, and six of his reels orbit him; the strip at 7.4 s shows the tiles entering from the right one at a time over 0.6 s and then revolving, with the front copies occluding his torso. Then a Claude Desktop insert (drag five clips, type /video-edit, "Transcribing 5 clips, Picking the best takes, Cutting, captions, motion graphics, Rendering reel.mp4" ticking). 13.9 to 16 s **cool dude**: dark editorial grade, blur-to-focus transition over ~0.45 s, tiny tracked caps "OR YOU CAN GET" spread across the width, then "cool dude" in DM Serif Display rising letter by letter from a mask (the strip shows "ool dude" then "cool dude" settling over 3 frames, ~0.1 s) with "AESTHETIC" in small caps under it, then "like this." the same way. CTA: profile card (103K) and a comment sheet typing "EDIT".

### 5.6 `watch-scroll-part-oct26` (7700962568537492744, 2026-10-26, 47 s; same video reposted Oct 17 and Oct 30)

Reaction-and-remake format: he watches a CapCut tutorial for a "Spotify scrolling effect" on his phone (the tutorial creator's reel floats beside him as a tilted card), re-shoots himself miming a scroll and a tap, types "recreate this effect" into a Claude prompt bar insert, and plays the result. The result (22.6 to 27 s strips): a tilted phone card to the right of his head at ~15 degrees, showing a dark Spotify-like list; the list scrolls while his finger moves and stops when he taps; in the second version the card is semi-transparent so his face is visible through it; captions "scroll" and "tap a song" in yellow sit inside the card. Lesson for us: the mime is the whole trick; the card is a scrolling div matched to the finger's start and stop times, not a track. The outro (37.8 s) shows the couch wall appearing over ~0.3 s as two bursts of thumbnails behind "26 different video effects".

### 5.7 `watch-remake-viral-nov18` (7709596145751723284, 2026-11-18, 39 s, 717 views)

The text-sandwich remake. 0 to 9 s: reaction to @itsbaileymacninch's Edits-app tutorial (her reel as a card beside him). 9 to 15 s: he explains the shoot ("walk in from one side and move enough to show the text") with a tilted "RAW CLIP" card showing the raw take. 15 to 23 s: the Claude Code desktop UI inserts, plugin picker showing video-studio, carousel-studio and script-studio, the prompt "recreate the text effect from this reel on my raw clip <instagram url>", and the task list "Found the text effect in the reference / Cut you out of the background / Sandwiched the text: fill behind you, outline in front / Graded your D-Log footage / text-effect.mp4 ready". 23 to 27 s result: "TEXT EFFECT" in two lines, yellow fill with a pink outline, the fill behind his body and the outline drawn over him, so as he walks right the letters appear to pass through him; the strip shows the word pops in at frame 3 (0.2 s) with a slight scale-down settle and holds. D-Log mention matters: he is shooting a DJI camera now, same colour pipeline as Jacob's Pocket 3.

### 5.8 `watch-two-clips-rip-oct18` (7698131489724140821, 2026-10-18, 25 s, 959 views)

Hook "Claude sucks at video editing UNLESS..." in a handwritten marker font with a yellow underline, held for 2 s with no other motion (the hook text is in before he speaks). At 3.3 s three creator cards pop in with "like this one," then a one-frame cut to the couch wall version ("this one,"), then at 5.3 s **the rip**: a jagged vertical tear opens from the top center over 4 frames (0.4 s), white torn edges, the two halves slide apart ~60 px and the second take is revealed behind, then the halves fade. At 9 s "stand out" slams at 300 px behind the head while the room dims; at 10 s a translucent reel card slides in from the right with a view counter that ticks 0 > 101,000 > 182,000 > 244,000 > 289,000 > 319,000 > 331,000 > 340,000 > 341,086 across ~1 s (ease-out counter). CTA with a CapCut icon struck through in red.

### 5.9 `watch-five-clips-oct19` and `watch-next-level-nov11` (bonus reads)

Oct 19 (26 s): the "video editors are cooked" reel. A full NLE timeline card slides up under his chin for "video editors" (0.5 s), "cooked." in 300 px yellow with ember particles, then a cream-paper layout with a "100% edited by Claude" counter and a task card, then handwritten Caveat arrows ("can't edit", "not techy") pointing at his head, then CapCut/DaVinci/Premiere app-icon cards flying in and out, then invoice cards "$150 per video" stacking up to "$750 every single video" with a red strike. Every graphic is 1 to 2 s and timed to the spoken word.

Nov 11 (49 s, "Can Claude edit like Diary of a CEO?"): he films "podcast style" clips in a cowboy hat and sunglasses against a window, drops them in Downloads, runs video-studio with "edit my podcast clips like @steven's Diary of a CEO reel: dark cinematic grade, same captions, fire b-roll". The result alternates his dark-graded talking head with Arcads-generated B-roll (a man on a bed, a man at a machine) and three caption styles in one piece: bold white uppercase with a red highlight word ("$20K IN DEBT AT 20"), red italic uppercase plus white serif ("LIFE OR DEATH situation."), and mixed-weight lowercase ("i had to do what i never thought"). Word-by-word reveal, each word landing ~0.15 s apart.

---

## 6. Which of these fit a diesel build account

Context: El Coyote is a 1959 Ford F600 road-to-SEMA build, Jacob talking to camera plus truck and shop footage, phone and DJI Pocket 3, one man, no second operator. House rules: no colour grade on his footage, captions light and clean, Anton + Oswald + Inter, flat red, no sheens. The audience is diesel and truck people, not AI-tips people, so UI mockups and "look at my own reels" effects carry less weight than anything that puts the truck on screen.

Ranked by (fit to the story) x (can one guy shoot and we can build it) x (likely to be shared by truck people):

1. **Before + after wipe.** The single most native effect for a build: rust to primer, stock bed to the finished bed, old 7.3 to the compounds. Shoot the same locked-off angle before and after (Pocket 3 on a tripod, mark the floor with tape). Build: ffmpeg crop/overlay with a moving edge plus a soft light bar, already within build_reel2's reach. Labels in Oswald, no grade.
2. **Zoom-through cut.** Talking head to a detail of the truck (push into the hood, land on the turbo). ~0.4 s, flash hidden cut, whoosh. ffmpeg zoompan + stacked-scale radial blur. Cheap, reusable on every reel, and it is the transition that makes a two-shot phone reel feel edited.
3. **Digital zoom with HUD.** We already punch in; add the REC dot, timecode and the creeping 1.51x to 1.60x readout on the emphasis word. Needs 4K source (Pocket 3 shoots 4K). ffmpeg only. Pairs with the "walk around the truck" footage as a viewfinder motif.
4. **Checklist.** Build-step cards ticking off in sync with speech ("frame swap, fuel system, turbos, paint"). Also doubles as a partner-status board (Driven Diesel, ISSPRO, Power Hungry). Compositor, easy, no matte.
5. **Headline wall / paper cut (magazine-clipping collage).** The Road to SEMA story wants a clippings aesthetic: "Diesel World", event flyers, partner logos popping onto the shop wall behind him. Paper cut's ransom-note type is the fun version for a punch line. Needs a matte if the clippings go behind him; skip the matte and put them beside him for a v1.
6. **Cover story.** One magazine-cover frame of the truck (not of Jacob) as a reel opener or the closing card: "EL COYOTE, Road to SEMA 2027". Static, no matte needed if the subject is the truck. Strong share bait for the SEMA angle.
7. **Sticky text / finger tags / air marker (pointer labels).** Jacob pointing at a part and a label riding his finger, or circling a component on the truck in the air. This is the "parts manager" credential made visual. Medium: needs a hand track (manual keyframes on Pocket 3 footage are fine, 5 to 8 keys per second of hold). Build after the top four are routine.
8. **Phone mockup.** The daily Vinny texts, vendor quotes, DM from a partner. Natural for the partner-pitch and daily-hunt storylines. Easy in a compositor, no matte. Keep the screen content real (screenshots), his rule too.
9. **Pull-back reveal.** The clip revealed inside an "editor" is his AI-tips joke; our version is the clip revealed inside the shop camera, the Fullbay screen, or a phone in Jacob's hand. Medium. Use sparingly.
10. **Vertigo.** In camera: Jacob (or the truck) locked while the shop stretches. The Pocket 3 has only digital zoom, so do it in post with a matte, or shoot it with a slow walk-back and rely on the shop's strong lines. Great once for a dramatic beat (first start, first drive), not a weekly tool.
11. **Doodle boil.** A hand-drawn boil outline on the truck's silhouette for a sketch-to-reality beat, or scribbled arrows on parts. Edit-heavy, but it fits the builder-journal feel better than any glass or UI effect. Medium.
12. **Chart grow.** Horsepower, budget, follower count. Fine for a "what this cost" reel. Easy, but keep it flat red and white.
13. **Couch wall / orbit / clap wave (own-reels wallpaper).** Only works once there are 30 to 60 good build clips to tile. Save it for a recap reel; today the wall would be thin.
14. **Swipe / ball toss / rewind / the rip.** Cheap ffmpeg transitions. The rip is the one with character for a "scrap that plan" moment. Use any of them once per reel at most.
15. **Face lock, clone, freeze sticker, pocket proof, hand frame, screen dive.** Creator-persona gimmicks. Low priority; screen dive could work once for "this is the portal" (elcoyotediesel.com).
16. **UI world, green screen, prompt box, comment bubble, spatial glass, type wall, serif flow, chip row.** Software-aesthetic inserts for an AI-tools audience. Comment bubble is the only one worth keeping, as a CTA, and only if we ever run a keyword DM funnel.
17. **Glass type, shatter 3D, spotlight, blackout, depth scatter.** Conflict with the flat, no-sheen, no-grade house rules. Skip.

Build order recommendation: 1 to 4 are ffmpeg or trivial compositor work and could ship in build_reel2 this month; 5 to 8 justify standing up the compositor (Remotion per the roadmap, or HyperFrames since it is literally what he uses, has a Claude Code plugin, and renders transparent WebM inserts we can drop on top of build_reel2 output); 9 to 12 need the person matte (MediaPipe Selfie Segmenter or BiRefNet on CPU; convert Pocket 3 D-Log/HLG to BT.709 first).

---

## 7. Sources

- Source reel: https://www.instagram.com/reel/Def9pj5TWtA/ (local copy in `..\2026-11-21-Def9pj5TWtA\`)
- TikTok mirrors: https://www.tiktok.com/@tenfoldmarc (ids in `dl\`)
- YouTube: https://www.youtube.com/@Tenfoldmarc and the older https://www.youtube.com/@marc-cleroux
- Threads: https://www.threads.com/@tenfoldmarc
- GitHub: https://github.com/tenfoldmarc, https://github.com/tenfoldmarc/video-edit-skill (README, SKILL.md, references/looks.md, layout.md, overlays.md, gotchas.md), https://github.com/tenfoldmarc/studio-plugin (and /releases/tag/v2.7.1), https://github.com/tenfoldmarc/studio-plugin-codex
- Guides: https://guides.tenfoldmarketing.com/ (video-edit, ai-reel-editing-prompt, 60k-content-system, arcads-unique-edits)
- Skool: https://www.skool.com/ten-fold/about
- creatordb: https://creatordb.app/creatorstats/tenfoldmarc/ (data refreshed 2026-09-22 and 2026-10-02)
- Community rebuilds: https://github.com/ONIKOSIOLA/video-editing-kit, https://github.com/itsCet/Your-AI/pull/13, https://github.com/Vibha-Ramprakash/claude-video-effects, https://www.adamgodigital.com/guides/claude-video-effects, https://github.com/Dryxio/effects-skill
- HyperFrames: https://github.com/heygen-com/hyperframes
- Related creator: https://digitalzoomstudio.net/2026/10/20-video-effects-claude-made-for-one-reel-from-magazine-cover-to-lens-ring/ (justyn.ai's 20-effect reel, 2026-10-28)
