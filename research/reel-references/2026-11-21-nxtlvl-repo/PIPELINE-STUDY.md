# @ai.nxtlvl pipeline study: the Nxtlvl-Social repo, read in depth

Written 2026-11-21. Companion to `../2026-11-21-nxtlvl-profile/DOSSIER.md` (who they are) and `../2026-11-21-DfU2nIgt8XK/BREAKDOWN.md` (the REPO reel frame by frame). This file is about HOW the reels are made and what is worth taking.

Method: `github.com/nxtlvlsocial1-web/Nxtlvl-Social` is public. The working tree is 77 MB but the git history is about 800 MB, so `main` was cloned at depth 1 into `clone/` and six branches were fetched with `--filter=blob:limit=1m` (no media blobs) and named `origin/console-skill-reel`, `origin/hf-install`, `origin/vibrant`, `origin/project-thread`, `origin/optimistic`, `origin/ccr7`. Branch files were read with `git show origin/<name>:<path>`; nothing in the repo was executed or installed. Everything quoted below is their text, treated as data; where their text contains dashes it has been re-punctuated. Paths are given relative to the repo root; for branch-only files the branch is named.

The REPO reel itself ("Stop paying for these 9 apps", posted 2026-11-04) is NOT in any pushed branch, and neither are the JARVIS, WATCH or TRADE reels. What is there: its Part 2 (`secret-store-9x16`, keyword REPO, 2026-11-10), the project that defines the cream-and-coral "ai.nxtlvl 2D style" in code (`prod-guard-explainer-9x16`, 2026-10-28), the neon GTA reel we have frames of (`gta6-playbook-9x16`, 2026-11-12), about 90 other reel projects, the full skill stack, their knowledge exports and the comment-to-DM service. So the design system and the pipeline are fully documented even though the one reel we studied is missing.

---

## 1. Repo map and the reel pipeline

### 1.1 Branch map (what lives where)

| Branch | Files | What it holds |
|---|---|---|
| `main` (cloned) | 2,426 | `.claude/skills/` (160 skills, 2,078 files), `CLAUDE.md`, `knowledge/creedom-creators100x/` (9 exports), `brands/` (nxtlvl, dr-kokila, kanav-kesar), two client reel projects (`kokila-peace-9x16`, `surrender-ad-9x16`), `website/`, `backend/` (Cloudflare Worker), `tools/see_link.py`, `tools/pexels_fetch.py`, `motion-canvas/` (unused scaffold) |
| `claude/console-skill-reel` | 3,576 | 40 reel projects incl. the @ai.nxtlvl 2D and 3D ones: `prod-guard-explainer-9x16`, `haunted-db-9x16`, `horror-db-9x16`, `growth-agent-9x16`, `youtube-agent-9x16`, `opengym-claude-9x16`, `console-skill-9x16`, `console-continue-9x16`, `gta6-playbook-9x16`, `gta6-claude-9x16`, `gta6-chat-clipper-9x16`, `fable-week-9x16`, `reel-flop-9x16`, `study-manga-9x16`, the Creedom and Creators 100X reels, plus `brands/ai-nxtlvl/brand.md` |
| `claude/hyperframes-cli-install-w6ziy7` | 3,550 | the "what if" voxel series (`ai-city`, `ai-f1`, `ai-bank`, `ai-clone`, `ai-closer`, `ai-exam`, `ai-posts`, `ai-future`), `zero-stack-9x16`, `secret-store-9x16` (REPO part 2), `autopilot`, `copycat`, `chatgpt-business`, `ideas/what-if-backlog.md`, `audits/` |
| `claude/vibrant-feynman-gaxg7b` (PR 13, open) | 2,899 | website relaunch, `nxtlvl-growth-timelapse-9x16`, `nxtlvl-ad-system-9x16`, `nxtlvl-edits-launch-9x16`, `nxtlvl-ledger` |
| `claude/project-thread-3lfh4n` (PR 11, open) | 1,726 | `automation/instagram-dm/` (the Graph API comment-to-DM service) |
| `claude/optimistic-newton-m7roun` (PR 15, merged) | 2,772 | five more Creedom reels (11-18 to 11-20), `creators100x-niche-9x16` |

Project creation dates run from 2026-10-15 to 2026-11-20: 97 dated projects in 37 days, so about 2.6 reel projects per day across all clients and pages (`meta.json` `createdAt` in each project).

### 1.2 How a reel project is laid out

Every reel is one folder `<campaign>-<aspect>/` (rule in `nxtlvl-social-video` § 2: "A different aspect is a separate HyperFrames project"). The paper-system projects look like this (`prod-guard-explainer-9x16`, branch console-skill-reel):

```
assets/fonts/   InstrumentSerif-Italic.ttf, JetBrainsMono-Bold/Regular.ttf, manrope.ttf, Silkscreen-Regular.ttf
assets/img/     pdf-cover-1.png (the lead magnet shown in the CTA)
assets/vendor/  gsap.min.js
build/voice.py  cut the VO take into lines, time every word -> assets/audio/voice.wav, build/words.json, voice/lines.json
build/generate.py  words.json + lines.json -> index.html (one GSAP timeline) + build/cues.json (every visual event, for sound)
build/audio.py  cues.json -> assets/audio/mix.wav (music + SFX + voice, -14 LUFS)
voice/raw/vo1.mp3, voice/raw/words_vo1.json   the ElevenLabs take and its Scribe word timestamps
hyperframes.json, package.json (pins hyperframes@0.8.203), meta.json, index.html (generated), caption.md
```

The later projects (gta6-playbook, fable-week, the Creators 100X reels) move to `plan/` (`script.json`, `words.json`, `vo_pick.json`, `edit.json`, `sfx_events.json`, `sfx_library.json`) and `build/vo_kokoro.py`, `build/vo_pick.py`, `build/sfx_mix.py`, `build/render_draft.sh`, `build/render_final.sh`, `build/cover.cjs`. Rendered MP4s are gitignored ("Keep rendered MP4s out of git; deliver them, don't commit them", `CLAUDE.md`).

Key point: **`index.html` is never written by hand.** A Python generator writes it from the word timings. New versions keep the old generator and add `generate_v2.py` etc.; the docstring at the top of each generator records the owner's notes for that version (e.g. `apoorva-ai-quiz-9x16/build/generate_v4.py` quotes "it doesn't give a leader vibe" and "looks like AI slop" and lists the fixes).

### 1.3 What they give Claude Code: CLAUDE.md and the house skill

`CLAUDE.md` (main, 12 KB; the branch copies are longer) is a routing table of 160 skills, nearly all third-party and pinned in `skills-lock.json` (HyperFrames skills from `heygen-com/hyperframes`, marketing skills from `coreyhaines31/marketingskills`, GSAP skills from `greensock/gsap-skills`, `charlie947/motion-graphics-skills`, `emilkowalski/skills`, fal.ai skills, and so on). Only one skill is theirs: `.claude/skills/nxtlvl-social-video/SKILL.md` (4.8 KB on main, longer on branches). The key instructions, verbatim apart from dash punctuation:

From `CLAUDE.md` (branch console-skill-reel, "Rules"):

- "Write every video script on the modern story arc (`nxtlvl-social-video` § 3a): hook at 70 dropped mid-story, first peak (contrast, contrarian take or shocking stat) by 5-15 s, then peak, release, peak, release, ending on the CTA."
- "Start every post description with the video's CTA keyword line (e.g. `Comment "AGENT" and I'll DM you my whole setup.`), then the hook and the body; don't repeat the CTA further down."
- "End every post description with up to 5 hashtags and then one plain line of relevant SEO keywords (the phrases people search for the topic, comma separated), and always hand over the full description in one block, ready to paste."
- "The keyword auto-DM (automation) is only the resource link and its setup steps, nothing else: no greeting, buttons, comment replies, follow line or caveats."
- "Never render a final until the person has approved the preview."
- "Run every render detached (`setsid nohup bash <script> > /dev/null 2>&1 < /dev/null &`), never as a time-limited background job."
- "Never use emojis in post descriptions, captions or hashtag blocks we write for clients (number lists with "1.", not emoji digits)."
- "Sound effects: always build the SFX library from Openverse first (`api.openverse.org`, licences CC0 or CC BY only, never NC, ND or SA; record each sound's title, creator, licence and link, and credit CC BY ones in the post)."
- Branch hf-install adds: "Keep every video under 60 seconds (aim for 45-58 s) ... Plan the script to fit before voicing it: cut lines, merge beats and turn repeated steps into a quick montage rather than going over." and "Write every hashtag in all lowercase."

From `nxtlvl-social-video/SKILL.md`:

- § 2 formats: Reels "9:16, 1080x1920, `portrait`, 7-30 s (max 60 s)" on main; "7-58 s (always under 60 s)" on branch hf-install. "30 fps unless the brief says otherwise."
- § 3: "Hook in the first 1.5 s. The first frame must already show the subject or the headline: no slow fade-in from black, no logo-first intro." / "Captions on by default." / "Safe zones for 9:16: keep text, faces and logos out of the top 250 px and the bottom 400 px (platform UI: username, caption, buttons), and 60 px from each side." / "One message per video. End on a clear CTA card (follow, link in bio, shop now) held >= 1.5 s." / "Loopable when it's a Reel/TikTok under 15 s."
- § 3a (branches only), the arc: "1. Start at 70, not 0 (0-5 s). The hook drops the viewer into the middle of a story that has already started: no setup, no intro, no 'today I'll show you'. 2. First peak at 90 (by 5-15 s). A contrast moment, a contrarian statement or a shocking stat: the first hit of dopamine. 3. Release, then peak again ... No single climax in the middle: stack mini peaks and re-hook as long as you can. 4. Close on the CTA ... straight after the last peak. When presenting a script, label each line with its arc beat (hook 70, peak, release, CTA)."
- § 5: "`npx hyperframes check` must pass", preview with `npx hyperframes preview --background`, "Render with `--quality draft` while iterating and `--quality delivery` for the final", verify with ffprobe. Branch version adds a pre-render frame checklist ("Characters in one piece", "Faces friendly, never creepy", "Overlays clear of faces").
- § 7 (branch hf-install), "what if" reels: "No keyword CTA by default ... when there is nothing to DM. End instead on the follow prompt ... and a question that invites comments." Arc timing: "Hook, 0-3 s, start at 70/100 ... First peak, by 5-10 s, spike to 90 ... Release, then peak again, every 8-15 s ... Aim for 4-5 peaks in a 45-58 s reel ... Leave no flat stretch longer than about 10 s." "On screen, every peak gets a visual event (a stamp, a counter, a camera move, a hit in the score)."
- § 8, the tutorial skit format: "One step at a time, on a screen big enough to read on a phone", "Always show where the viewer is in the steps (a progress cue of some kind)", "Captions a few words at a time", an "honest beat near the end (what it can't do)", end card with "a share prompt ... `Comment KEYWORD for the full setup`, `Follow for the next one`."

Everything else Claude reads is the HyperFrames skill set itself (`hyperframes`, `-core`, `-animation`, `-audio`, `-cli`, `-creative`, `-registry`, `media-use`, `faceless-explainer`), which is upstream code from HeyGen, not theirs. The owner's taste is injected per reel as chat feedback and lands in generator docstrings and the knowledge exports (see section 3).

### 1.4 The HTML + GSAP composition contract (what HyperFrames expects)

From `.claude/skills/hyperframes-core/SKILL.md`: "HyperFrames renders video from HTML. A composition is an HTML file whose DOM declares timing with `data-*` attributes, whose animation runtime is seekable, and whose media playback is owned by the framework." Rules that shape every generator:

- One root `<div id="root" data-composition-id="main" data-start="0" data-duration="37.1" data-fps="30" data-width="1080" data-height="1920">`. Render length is the root's `data-duration`.
- "Each composition registers exactly one `gsap.timeline({ paused: true })` at `window.__timelines["<id>"]`." The renderer seeks that timeline per frame. No `Math.random`, no `Date.now`, no CSS `transition` on animated elements, `fromTo` with explicit from-states so any frame is correct under seek, `immediateRender: false` when re-owning a target.
- Scenes are `class="clip"` elements with `data-start` / `data-duration` / `data-track-index`; the runtime shows and hides them, so you never tween `display` or `visibility` on a clip (lint error `gsap_animates_clip_element`).
- "Spatial motion uses GSAP transform aliases only (`x`, `y`, `scale`, `rotation`)"; never tween `width`/`height`/`top`/`left`. Never pair a CSS `transform` with a GSAP tween on the same property (lint `gsap_css_transform_conflict`).
- Fonts: "A named CSS `font-family` needs an in-file `@font-face` to a shipped local file." Every `<audio>` needs an `id` or the mixer skips it and the render is silent.
- Their own gotcha (workflow-and-skills.md § 18.3): "Sets at t=0 are skipped by cold render workers, so frame-0 visibility goes in CSS." The hook headline is therefore styled visible in CSS and only its accent word is tweened.

The generated skeleton, from `prod-guard-explainer-9x16/build/generate.py` lines 690-712:

```html
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-fps="30" data-width="1080" data-height="1920">
  <div id="bg" class="clip" data-start="0" data-duration="{DUR}" data-track-index="0" data-layout-ignore>...</div>
  <div id="giants" class="clip" ... data-track-index="1">{giant ghost words}</div>
  {one <div class="clip scene" data-start data-duration data-track-index="3|4"> per voice line}
  <div id="mlayer" class="clip" ... data-track-index="5">{mascot svg}</div>
  <div id="chrome" class="clip" ... data-track-index="6"><div class="top"><div class="brand"><i></i>AI.NXTLVL</div><div class="prog"><i></i></div></div></div>
  <div id="caps" class="clip" ... data-track-index="7">{caption chunks}</div>
  <audio id="mix" src="assets/audio/mix.wav" data-start="0" data-duration="{DUR}" data-track-index="10" data-volume="1"></audio>
</div>
<script>
  const tl = gsap.timeline({ paused: true });
  gsap.set([...every element that enters later...], {opacity: 0});
  tl.fromTo("#s2 .hw", {opacity:0,y:40}, {opacity:1,y:0,duration:.32,stagger:.06,ease:"back.out(2)",immediateRender:false}, 4.640);
  ... (300 to 500 tween lines)
  tl.set({}, {}, {DUR});
  window.__timelines["main"] = tl;
</script>
```

Layers are fixed: background, ghost word, scenes (alternating two tracks so Studio shows them as a checkerboard), mascot, chrome (HUD), captions, audio.

### 1.5 How timing is driven: word timestamps, not fixed beats

Every visual event is placed at the start time of a spoken word. The generator loads `words.json` (`[{"line": 1, "w": "deleted", "s": 2.01, "e": 2.35}, ...]`) and `lines.json` (line start/end), builds scene windows from line starts minus 0.12 s, and looks cue words up by prefix (`prod-guard-explainer-9x16/build/generate.py`):

```python
def word(li, text, nth=1):
    hits = [w for w in WORDS if w["line"] == li + 1 and re.sub(r"[^a-z0-9]", "", w["w"].lower()).startswith(text.lower())]
    if len(hits) < nth:
        raise SystemExit(f"cue word {text!r} not in line {li + 1}")
    return hits[nth - 1]["s"]

T = {"press": round(word(0, "deleted") - .05, 3), "rows": word(1, "rows"), "gone": word(1, "gone"),
     "backups": word(1, "backups"), "copy": word(2, "copy"), ... "comment": word(7, "comment"), "backup": word(7, "backup")}
```

Then `pop("#stamp1", T["press"] + .12, ...)`, `count 1,204,883 -> 0 from T["rows"] to T["gone"]`, and so on. The gta6 generator does the same with `T("p04", "paid")`. Where music matters, cuts are snapped to the track's half-beat grid: `BEAT = 60 / bpm; HB = BEAT / 2; snap(t) = round(t / HB) * HB` (workflow-and-skills.md § 5; CHECK 99.384 bpm, write-script 117.45 bpm, fable-week 117.5 bpm). The gta6 generator also writes `plan/edit.json` (`{"dur": 29.76, "scenes": {"hook": [0, 4.862], "proof": [4.862, 12.643], ...}}`) and `plan/sfx_events.json` (`[{"type": "whoosh", "t": 4.742}, ...]`), so the sound pass reads the picture's own event log. Frame-0 content is visible in CSS; word-chunk captions are `tl.set` on and off.

So: not fixed beats, and not a human-timed EDL either. The VO is recorded first, timed by ASR, and the picture is generated to the words. This is the single biggest structural difference from our footage-first EDL.

### 1.6 The HyperFrames render step

What HyperFrames is: `heygen-com/hyperframes`, Apache 2.0, created 2026-03-10, 87,727 stars on 2026-11-21, TypeScript, Node >= 22, FFmpeg required. README line: "a free, open-source framework for turning HTML, CSS, media, and seekable animations into deterministic MP4 videos." npm `hyperframes` latest 0.9.77 (also `0.8.190-hdr.2`, `0.9.28-alpha.4`); they pin `0.8.203` in every `package.json` (`"render": "npx --yes hyperframes@0.8.203 render"`). Dependencies include `puppeteer-core` and `@puppeteer/browsers`, i.e. it drives a pinned Chrome build ("pixel output drifts across Chrome versions", `hyperframes-cli/references/doctor-browser.md`), seeks the registered GSAP timeline frame by frame, captures (BeginFrame path, or screenshot fallback under software GL), and encodes with FFmpeg. Audio placed in the composition is mixed by the framework's own Web Audio graph ("preview and render run the same Web Audio graph", `hyperframes-audio/SKILL.md`). A desktop Studio app exists for Mac, Windows and Linux; the CLI itself has no `os` restriction on npm.

Render flags they use (`hyperframes-cli/references/preview-render.md` plus their scripts): `--quality draft | looks | delivery | standard | high` ("`looks` is CRF 16 on the standard preset. `delivery` is `high`"), `--fps 24|30|60` (default 30), `--crf` or `--video-bitrate 11M`, `--sdr` (force SDR when any source carries HDR tags), `-w 3` (workers; "Each worker spawns Chrome (~256 MB)"), `--resolution portrait` (supersampling via deviceScaleFactor). Their final command, `gta6-playbook-9x16/build/render_final.sh`:

```bash
export HYPERFRAMES_NO_TELEMETRY=1
npx --yes hyperframes@0.8.203 render --quality high --sdr -w 3 -o renders/master.mp4 > renders/final.log 2>&1
python3 build/sfx_mix.py renders/master.mp4 renders/nxtlvl_gta6-playbook_reels_9x16_v1.mp4
python3 build/sfx_mix.py renders/master.mp4 renders/..._v1_nomusic.mp4 --no-music
python3 ~/.claude/skills/openverse-sfx/scripts/verify_mix.py renders/..._v1.mp4 --target -14 --outdir renders/verify
```

Measured speed on their cloud Linux box (knowledge export § 10): 1,154 frames in 3 min 40 s (`--quality delivery -w 3`, about 5 fps), 1,388 frames in 7 min 26 s (explainer, `--quality high`, about 3 fps). Masters 27 to 51 MB. The whole house workflow is Linux: `setsid nohup`, bash scripts, `/root/tts/.venv`, and a hard rule that a render dies if its parent shell exits (`render_cancelled_parent_exited`).

### 1.7 The voice step: Kokoro, Chatterbox, ElevenLabs, and the take picker

Three voice routes, documented in `knowledge/creedom-creators100x/workflow-and-skills.md` § 4 and the `build/vo_*.py` files:

1. **Kokoro-82M (hexgrad, Apache 2.0), local, CPU.** House voice for the Creators 100X page is `af_heart`; the GTA playbook used `am_michael`; others seen `am_puck`, `af_bella`, `af_nova`, `am_liam`, `af_sky`, `am_fenrir`. Exact call (`gta6-playbook-9x16/build/vo_kokoro.py`):

```python
pipe = KPipeline(lang_code="a", repo_id="hexgrad/Kokoro-82M")
VOICE = "am_michael"
SPEEDS = (1.25, 1.32)   # the reel has to land at 25-30 s
for lid, text, _ in LINES:
    for k, sp in enumerate(SPEEDS):
        audio = np.concatenate([np.asarray(a, dtype=np.float32) for _, _, a in pipe(text, voice=VOICE, speed=sp)])
        sf.write(os.path.join(OUT, f"{lid}_t{k}.wav"), audio, 24000)
```

Rules they learned: generate at the speed you want, never time-stretch ("Chatterbox + atempo speed-up sounded unnatural; generate faster instead"); two takes per line at two speeds; pronunciation fixed with inline IPA `[Creedom](/kɹˈidəm/)` or respelling ("MAHNG-guh"); Kokoro dropped the "-ed" in "turned", so the line was rewritten. Speeds used: 1.06 to 1.34 depending on how slow the owner felt the cut was.

2. **Chatterbox (Resemble AI, MIT), CPU**, cloning a 10 s Kokoro clip as the reference so "nobody real is cloned", with `exaggeration` set per arc beat (hook .85, peak 1.0, release .6, CTA .75). Dropped as house voice after v4-v12 of one reel "sounded off".

3. **ElevenLabs** (eleven_v3 with mood brackets like `[whispering, conspiratorial, excited]`, or the owner's own take) for client work and the REPO part 2 reel (`secret-store-9x16/voice/elevenlabs_direction.json`: voice "Lukas - Excited youthful young man", two takes per line, then `build/voice.py` pitches the chosen take up 2 semitones by resampling 500/561, which also makes it 12 percent faster, and adds "a short metallic comb and a touch of ring modulation" for the robot).

**Take picking and word timing** (`build/vo_pick.py`, copied between projects): each take is transcribed with `faster-whisper` `Systran/faster-whisper-small.en` (`device="cpu"`, `compute_type="int8"`, `word_timestamps=True`, `beam_size=5`); score = words wrong against the script (numbers normalised), then the wider 5-95 percent F0 spread (librosa pyin 80-600 Hz, a spread over 300 Hz counts as a squeak); the winner is trimmed from 0.04 s before the first word to 0.12 s after the last with 12 ms fades, lines are joined with a pause per arc beat (`GAP = {"p00": .2, "p01": .08, "p02": .3, ...}` times `GAP_SCALE = .4`), then polished:

```
atempo=1.04,highpass=f=80,acompressor=threshold=-20dB:ratio=3:attack=5:release=80:makeup=2,loudnorm=I=-16:TP=-2:LRA=9   -> 48 kHz mono vo.wav
```

Word times are divided by the atempo factor and written to `plan/words.json` with the script's own spelling when the word counts match. On client ElevenLabs takes they use ElevenLabs Scribe word timestamps instead (`voice/raw/words_vo1.json`).

### 1.8 Sound and mux: two patterns

Pattern A (paper reels, October): `build/audio.py` synthesises an original chiptune bed in numpy ("104 bpm in C major ... square-wave lead and arp, triangle bass") plus SFX from the HyperFrames bundled library and small synthesised blips, one per logged event, masters to -14 LUFS / -1.5 dBTP, writes `assets/audio/mix.wav`, and the composition references it with `<audio id="mix" ...>`, so HyperFrames muxes it during the render.

Pattern B (November reels): render the picture silent, then `build/sfx_mix.py` muxes with FFmpeg (`gta6-playbook-9x16/build/sfx_mix.py`): voice `-16 LUFS` on top; music bed `-ss {SONG_AT}`, `afade in 0.12 / out 1.0`, `loudnorm=I=-18:TP=-3:LRA=11`, then ducked with `sidechaincompress=threshold=0.03:ratio=5:attack=15:release=300:makeup=1`; each SFX kind trimmed (`silenceremove ... atrim=0:{max_len}`), normalised to a per-kind peak (whoosh -10 dBFS, impact -7, pop -12, click -11, tick -17, stamp -7, riser -13, notify -12), alternately panned +/- 0.22 (impact, riser, stamp stay centre), same kind skipped if within 0.12 s of the last; `amix=normalize=0`; two-pass `loudnorm=I=-14:TP=-1.5:LRA=11` with `linear=true`; `-map 0:v -c:v copy -map 1:a -c:a aac -b:a 256k -movflags +faststart`. They also deliver a `_nomusic` file so the song can be added from Instagram's picker (keeps it licensed, counts as trending audio). Music is Openverse/Jamendo CC BY (credited in the caption), instrumental only (checked with Demucs), never reused.

### 1.9 Cover and caption

`build/cover.cjs`: Playwright Chromium opens the composition (or a dedicated cover HTML), seeks the timeline to a strong frame (`window.__timelines.main.seek(4.8, false)`), hides the headline, shrinks the scene, adds a cover title and a CTA pill, screenshots 1080x1920; everything key inside Instagram's 3:4 grid crop (y 240 to 1680). `caption.md` holds the paste-ready description in the house order (CTA line, hook, body with "1." lists, credits, 5 lowercase hashtags, one SEO line) plus the auto-DM block and notes on what is illustrative.

---

## 2. Their design system in code

Two visual systems share one skeleton (top-left label, handle top-right, one headline with one accent word, a proof object mid-frame, word captions, a comment box plus DM card at the end).

### 2.1 Paper system tokens (`prod-guard-explainer-9x16/build/generate.py`, 2026-10-28)

```python
CREAM, GRID, INK, CORAL, CORAL_D = "#F1E9DC", "#E4D9C7", "#1E1B18", "#E8735A", "#B9523D"
GREEN, AMBER, TERM, CARD, CARD_B, RED = "#3FA372", "#F2B33D", "#1B1A1F", "#FFFDF8", "#E2D6C3", "#D9483B"
CORAL_T = "#D45C40"   # coral for text and for pills under white text (3:1 on cream)
```

- Background: `#F1E9DC` with a 60 px grid of 2 px `#E4D9C7` lines (`background-image: linear-gradient(#E4D9C7 2px, transparent 2px), linear-gradient(90deg, ...)`, `background-position: 30px 0`). A dark twin `#bgdark` (`#1B1A1F` with `#2A2830` grid) fades in for one "twist" beat and flips `--ink` to cream.
- Ghost word behind every scene: `.giant { top: 760px; font: 800 330px/1 "Manrope"; letter-spacing: -10px; color: transparent; -webkit-text-stroke: 4px rgba(30,27,24,.08) }`, enters `opacity 0, scale 1.25 -> 1` over 0.5 s `power3.out`.
- Type: Manrope 800 headlines (`.l1 { font: 800 76px/1.05; letter-spacing: -2.5px }`), accent word Instrument Serif Italic (`.acc { font: 400 128px/1 "ISerif"; color: #D45C40 }`), JetBrains Mono 700 for every label (`.lab { font: 700 28px "JBMono"; letter-spacing: 3px; color: #8A7F70 }`), Silkscreen for pixel text. The AI.NXTLVL kit (`brands/ai-nxtlvl/brand.md`, branch console-skill-reel): "Headlines: Montserrat or Manrope 800, tight tracking. Accent words: Instrument Serif Italic. Labels, code, the handle: JetBrains Mono."
- Card: `.card { background: #FFFDF8; border: 3px solid #E2D6C3; border-radius: 28px; box-shadow: 0 18px 40px rgba(60,40,20,.12) }` (soft shadow in October). By 2026-11-02 the end card had moved to the neo-brutalist hard offset we saw in the REPO reel: `ai-exam-9x16` `#endc { background: #FFFDF8; border: 3px solid #1E1B18; border-radius: 40px; box-shadow: 12px 13px 0 #1E1B18 }` and the comment box `box-shadow: 6px 7px 0 #1E1B18`.
- Chip: `.chip { padding: 8px 18px; border-radius: 30px; font: 700 26px "JBMono"; letter-spacing: 2px; color: #fff }`, `.red #D9483B`, `.green #3FA372`, `.amber #F2B33D` with ink text.
- Command chip: `.chipcmd { padding: 18px 26px; border-radius: 18px; background: #1E1B18; color: #F1E9DC; font: 700 38px "JBMono"; box-shadow: 0 12px 24px rgba(30,20,10,.18) }`.
- Terminal card: `#1B1A1F`, radius 28, 64 px title bar `#26252C` with three dots, body `font: 700 44px/1.6 "JBMono"; color: #F4EEE6`.

### 2.2 HUD, headline, caption band, mascot

HUD (`.top`, y 262): `.brand { font: 700 30px "JBMono"; letter-spacing: 4px }` with an 18 px coral dot, text `AI.NXTLVL`; `.prog { width: 220px; height: 26px; border-radius: 13px; border: 3px solid var(--ink) }` whose inner bar runs `tl.to(".prog i", {scaleX: 1, duration: DUR, ease: "none"}, 0)` (a progress pill, not yet the 0/9 dots of the REPO reel; `ai-exam` uses the same bar). The GTA neon HUD: `#topbar { top: 92px }`, label `font-family: Mono; font-size: 30px; letter-spacing: .14em; padding: 10px 18px; border-radius: 12px; background: rgba(16,2,44,.55); border: 2px solid rgba(182,135,249,.5)`, wordmark PNG 52 px high on the right.

Headline (`.hl`, y 340): kicker `STEP 1/3` in JBMono 700 28 px with three 54x10 px segments that fill coral; line 1 words `.hw` enter `fromTo({opacity:0, y:40}, {duration:.32, stagger:.06, ease:"back.out(2)"})`; the accent word enters 0.3 s later `fromTo({opacity:0, scale:.6, rotation:-6}, {duration:.45, ease:"back.out(2.4)"})`.

Caption band (`.cap`, y 1330 in this project; the REPO reel moved it to y 220 under the HUD): `font: 800 60px/1.25 "Manrope"; letter-spacing: -1px`, chunks of at most 4 words or up to punctuation, chunk fades in `{opacity:0, y:16} -> 0.12 s power2.out`, and the spoken word gets a pill by `tl.set` at `w.s - 0.02`: `.cw { padding: 2px 12px 6px; border-radius: 16px }`, `backgroundColor: #D45C40, color: #fff`, reset at the next word's start. The gta6 captions are 2-3 words, `font: 900 74px/1.05 Montserrat; text-transform: uppercase; top: 1390px`, key words `#ff4fa3`, `fromTo({opacity:0, scale:.85, y:12}, {duration:.14, ease:"back.out(2.4)"})`.

Mascot: a 16x13 pixel sprite drawn as SVG `<rect>`s at 14 px per cell (`PX = 14`, `SPRITE` string rows, colours `s #F7C6B6`, `B #E8735A`, `D/L/a #B9523D`), with swappable eye and mouth groups (`m-eo`, `m-es`, `m-eh`, `m-ew`, `m-sm`, `m-fr`, sweat `m-sw`). Hop: `x` tween 0.42 s `power1.inOut`, `y -= 90` over 0.21 s `power2.out` then down `power2.in`, landing squash `fromTo(#m-body, {scaleY:.78, scaleX:1.15}, {scaleY:1, scaleX:1, duration:.3, ease:"back.out(3)"})`; idle bob `y:-6, 0.38 s, yoyo, repeat` for the whole reel; blinks `scaleY .1` for 0.1 s at hand-placed times; arm rotations `back.out(2)`; wave `rotation -70, 0.16 s, yoyo, repeat 9`.

### 2.3 Motion recipes with exact values (the "elements, not cuts" grammar)

| Move | Where | Values |
|---|---|---|
| Card drop in | `pop()` default in prod-guard; `show()` in gta6 | `fromTo {opacity:0, y:30, scale:.9} -> {1, 0, 1}`, 0.35 s, `back.out(1.8)`; gta6 default `{opacity:0, y:40}`, 0.3 s, `back.out(1.7)`; panels `{y:80, scale:.94}` 0.4 s |
| Big reveal card | prod-guard `#snap` | `{opacity:0, y:120, scale:.6, rotation:8}` 0.5 s `back.out(1.6)` |
| Feature chip / step dot | prod-guard `.st` | `{opacity:0, scale:0}` 0.3 s `back.out(3)`, stagger 0.14 s on the spoken words |
| Tag slam | gta6 `.tag` | `{opacity:0, x:-80}` or `{x:80}` 0.28 s; hot tag `{scale:.6}` |
| Stamp | prod-guard `.stamp`, gta6 `.stamp` | CSS `border: 8px solid #D9483B; border-radius: 16px; font: 800 76px Manrope; letter-spacing: 2px; transform: rotate(-8deg); background: rgba(255,250,245,.92)`; enters `{opacity:0, scale:2.4, rotation:-20}` 0.25 s `power4.out` (gta6: `scale 2.2, rotation -24 -> -12`, `expo.out`, border 10 px, glow `0 0 80px`), with a `stamp` + `buzzer` SFX |
| Strike-through | `surrender-ad-9x16`, `creedom-reel-analyser`, `apoorva` | a bar `height: 12px; border-radius: 6px; transform-origin: 0 50%`, `fromTo {scaleX:0} -> {scaleX:1}` 0.3 to 0.4 s `power3.out` (REPO measured about 8 frames) |
| Count-up | prod-guard rows, gta6 views, zero-stack bill | proxy object + `onUpdate` writing `Math.round(o.v).toLocaleString("en-US")`; 0.6 to 0.9 s `power3.out` for a reveal (`vc.v: 0 -> 30.5` then `toFixed(1) + "M"`), `power2.in` for a drain to zero timed from the word "rows" to the word "gone"; zero-stack steps the bill down in 8 writes 0.05 s apart; `tabular-nums` mandatory |
| Ghost-then-resolve | prod-guard `.chipcmd.ghost` | commands fly in `{opacity:0, x:+/-520}` 0.22 s `power2.in`, then out `{x:+/-140, rotation:+/-14, opacity:0}` 0.4 s with a `permission denied` chip popping 0.2 s |
| Scene change (no cut) | prod-guard `scene_tl` | incoming `.inner` `fromTo {x:300, opacity:0} -> {0,1}` 0.3 s `power3.out`; outgoing `{x:-260, opacity:0}` 0.16 s `power2.in`, plus a `whoosh` event |
| Punch-in cut | gta6 `cut()` | white `#flash` `fromTo {opacity:.85} -> 0` 0.22 s `power2.out`, stage `fromTo {scale:1.08} -> 1` 0.45 s `expo.out`, whoosh 0.12 s before; `mini_cut` is `.45 -> 0` over 0.14 s with a swish |
| Iris wipe | `sucsess-maperrs-9x16` | `fromTo(#stage, {clipPath:"circle(0% at 50% 40%)"}, {clipPath:"circle(86% at 50% 40%)", duration:.6})` and the reverse; `console-continue` draws a 2400 px coral circle `#iris` centred on the frame; REPO: 0.6 s grow then shrink |
| Typing | prod-guard `#ch{i}`, comment box | `tl.set(opacity 1)` per character spaced evenly between two word times; cursor `opacity 1 -> 0, 0.25 s, yoyo, repeat, ease steps(1)` |
| Key press | prod-guard `#key` | `y:14, boxShadow 0 2px 0` 0.07 s `power2.in`, back `y:0, boxShadow 0 14px 0` 0.18 s `back.out(2)`; screen flashes `#3A1513` 0.08 s and shakes `x += 10, 0.05 s, yoyo, repeat 7` |
| Hold at the end | all | 1.6 to 2.0 s after the last word (`DUR = E[-1] + 1.6`); REPO held 2.6 s silent |

### 2.4 Comment box and DM preview (the CTA kit)

Comment box, paper version (`ai-exam-9x16/build/generate.py`, also `ai-posts`):

```html
<div class="ec-box"><i class="av"></i><span class="fld"><span class="mono">you &middot; now</span><b class="ec-typed"></b></span><b class="ec-heart">&#9829;</b></div>
```
```css
.ec-box { display:flex; align-items:center; gap:18px; width:640px; padding:16px 24px; border-radius:26px; border:3px solid #1E1B18; background:#fff; box-shadow:6px 7px 0 #1E1B18; }
.ec-box .av { width:52px; height:52px; border-radius:50%; background:linear-gradient(135deg,#F2B33D,#E8735A); }
.ec-typed { font:800 52px "Manrope"; letter-spacing:2px; } .ec-typed::after { content:"|"; color:#6B5BD6; font-weight:400; }
.ec-heart { font-size:44px; color:#8a847c; }
```
Timeline: letters appear by `tl.set(".ec-typed", {textContent: "EXAM"[:k+1]}, t0 + k * .12)`; the heart turns coral `tl.set(".ec-heart", {color:"#E8735A"})` while `fromTo {scale:1} -> {scale:1.5, duration:.15, yoyo:true, repeat:1, ease:"sine.inOut"}`. The prod-guard variant: `.cbox` 940x132, radius 66, letters every 0.09 s with a `key` tick each, send button `scale .85, 0.08 s, yoyo` on the word "send". Above it the keyword: `.cchip` (`COMMENT`, JBMono 700 34 px, letter-spacing 8 px, ink pill) and `.cword` (`font: 800 150px/1.05 Manrope; background: #D45C40; color: #fff; border-radius: 40px; box-shadow: 0 18px 0 #B9523D`) entering `{opacity:0, scale:2.2, rotation:-8}` 0.32 s `power4.out` with a `slam`.

DM card (`creedom-check-9x16/build/generate.py` line 856, glass version; `gta6-playbook` line 350, light version):

```css
.dm { width:760px; height:124px; border-radius:36px; display:flex; align-items:center; gap:22px; padding:0 30px; }
.dm img { width:72px; height:72px; padding:10px; border-radius:20px; background:#fff; }
.dm b { font-weight:700; font-size:32px; }  .dm span { font-weight:500; font-size:28px; opacity:.7; }  .dm em { margin-left:auto; font-family:Mono; font-size:20px; }
```
Markup `<img logo><div><b>Creedom</b><span>sent you the link</span></div><em>now</em>`; entrance `fromTo {opacity:0, y:-160, scale:.9, filter:"blur(12px)"} -> {1, 0, 1, blur 0}` 0.7 s `back.out(1.4)`, a shine sweep 0.35 s later and a `notify` SFX. gta6: `#dm { top:200px; border-radius:30px; background:rgba(255,255,255,.95); box-shadow:0 20px 60px rgba(7,5,15,.6) }` with an 84 px gradient icon tile, `New message / Your GTA 6 playbook is here`, from `y:-160` 0.4 s `back.out(1.6)` on the word "send". The REPO reel's nine numbered chips filling two per beat is the same card with a chip row; no source for that exact variant exists in the repo.

### 2.5 Neon system tokens (`gta6-playbook-9x16/build/generate.py`, `brands/ai-nxtlvl/brand.md`)

```python
NIGHT, DEEP, VIOLET, STAR, LAV = "#07050f", "#10022c", "#7f1bf8", "#7a2ffb", "#b687f9"
PINK, ORANGE, GREEN, RED = "#ff4fa3", "#ffb36b", "#38e08c", "#ff3b5c"
```
Grade over the plates: `linear-gradient(170deg, rgba(127,27,248,.38), rgba(255,79,163,.22) 45%, rgba(255,179,107,.2))` in `soft-light`; two 900 px radial light leaks drifting across the whole reel (`sine.inOut`, full duration); grain `background-size 512px; opacity .07; overlay`, stepped `steps(DUR*12)`; vignette `radial-gradient(120% 80% at 50% 45%, transparent 55%, rgba(7,5,15,.7))`. Titles Montserrat 900 96-108 px, `letter-spacing -.035em`, the key line in `background-clip: text` gradient `#ffb36b -> #ff4fa3 45% -> #b687f9`; the keyword `#kw` 300 px gradient `#fff 10%, #ffb36b 35%, #ff4fa3 60%, #7f1bf8` with `drop-shadow(0 16px 60px rgba(255,79,163,.8))` and a pulsing `textShadow 0 -> 50px` yoyo. Panels `rgba(16,2,44,.82)`, radius 36, `border 2px rgba(182,135,249,.45)`, `backdrop-filter: blur(14px)`. Plates: muted Rockstar clips as `<video class="full plate">` with `filter: blur(3px) brightness(.72) saturate(1.3)` and a slow `scale 1 -> 1.07` push per plate.

### 2.6 The GSAP doctrine in the skills versus what they actually ship

`hyperframes-animation/rules/spring-pop-entrance.md`: "Smooth beats bouncy ... Bouncy `back.out` is the #1 instant turn-off in agent-made videos ... never the default", house ease `power3.out`, `POP_DUR 0.4-0.7 s`, `STAGGER 0.04-0.08 s` with `ITEM_COUNT x STAGGER <= ~0.5 s`, hero visible by t <= 0.5 s. `counting-dynamic-scale.md`: `tabular-nums` mandatory, `Math.round` not floor, `COUNT_DUR 1.2-2.5 s`, "Avoid `back.out` / `elastic.out` on the counter itself". `waterfall-entry.md`: binary opacity via `tl.set`, `power4.out`, anchors travel 60-80 px for 0.16-0.20 s, normal words 40-50 px for 0.13-0.16 s, punctuation 30-48 px for 0.10-0.13 s, each starting 1-2 frames before the previous settles. `gsap-easing-and-stagger.md` ships a closed-form `springEase({response, dampingFraction})` (critically damped at 1.0, "iOS register" 0.80-0.85, playful 0.60-0.70) because real-time spring solvers cannot be seeked.

Their reels ignore the first rule: almost every entrance is `back.out(1.6)` to `back.out(3)` with 0.25 to 0.45 s durations, counters run 0.6 to 0.9 s, and the owner keeps asking for more motion, not less. The shipped values are the ones to copy; the doctrine is the one to remember when something reads cheap.

---

## 3. Their knowledge base: numbers, rules, flops

All from `knowledge/creedom-creators100x/*.md` (exported 2026-11-17), the branch `CLAUDE.md` files, `brands/ai-nxtlvl/brand.md`, `secret-store-9x16/POST.md`, `ideas/what-if-backlog.md` and the storyboards cited in the dossier. Times UTC, quotes verbatim apart from dash punctuation.

### 3.1 Every performance number they wrote down

| Number | Context | Source |
|---|---|---|
| 6,205 followers, "6 recent posts" scanned, content score 82/100 | @ai.nxtlvl in Creedom, October 2026 | creedom-brief.md § 3.4 |
| 126,000+ plays on one reel = "85x my usual"; usual "low thousands"; a draft said "366K PLAYS" | the TRADE reel ("Comment TRADE and I'll DM you all 11 skills"), Oct 2026 | creedom-brief.md § 3.4, § 9.1 |
| Creedom 4.2/5 "Very good" on that reel; "best hook buried at 0:34" | same | creedom-brief.md § 3.4 |
| 339 to 6,700 followers | the growth number the owner asked to put in an @ai.nxtlvl reel; the client's own claim in `growth-agent-9x16` ("the page went from 339 to 6,700 followers, the five moves and the AGENT comment keyword") | creators100x-brief.md § 10.3; growth-agent generate.py docstring |
| 7,100 followers with 22 posts | Meta ad script, 2026-10-29 | `nxtlvl-ad-system-9x16/STORYBOARD.md` (branch vibrant) |
| 9,924 then 10,000 followers, 31 posts, 1.0M views, following 16 | growth timelapse, 2026-11-06 | `nxtlvl-growth-timelapse-9x16/STORYBOARD.md` (branch vibrant) |
| OpenJarvis reel 4/5; GTA 6 playbook 3.8/5 ("You blur the tool name at 0:14, so viewers may lose trust") | Creedom scores of two @ai.nxtlvl reels | creedom-brief.md § 3.2, § 10 |
| "one 'Comment HUMAN' skill post hit 37% engagement" | another creator, 10-day audit | hooks-ctas-automations.md § 1.3 |
| Sabrina Ramonov STUDY-prompts reel: 131K, 19.8 percent, 11.6K saves | the model for their STUDY reel | hooks-ctas-automations.md § 1.3 |
| "$113.98 a month (over 1 lakh a year)" savings; 9 repos; pinned comment "Chest 7 is the one everyone asks about" | REPO part 2 post kit | secret-store-9x16/POST.md |
| $374.86/mo to $0 across 8 swaps | zero-stack what-if | zero-stack-9x16/build/generate.py |
| Render: 1,154 frames in 3 min 40 s; 1,388 frames in 7 min 26 s; finals 27-51 MB | HyperFrames on their cloud box | workflow-and-skills.md § 10, brand-style-guide § 1.9 |
| Loudness: masters -14.0 to -14.1 LUFS at -1.5 to -1.8 dBTP; the explainer -16.0 / -4.4 | verify_mix results | open-items.md § 6.1 |
| Cree's 13 poses: about 12,600 ElevenLabs image credits ("around $2"); ElevenLabs VO 654 credits a take; Kokoro, Chatterbox, faster-whisper free | costs | workflow-and-skills.md § 19 |

What they do NOT have: posting dates, views, saves, comments or DMs per reel for anything they made ("Performance (views, likes, saves, comments, keyword DMs sent): UNKNOWN. Worth asking, to steer the backlog", open-items.md § 9.3; "Performance per keyword (comments, DMs sent, clicks): UNKNOWN; never reported", hooks-ctas-automations.md § 5). The editor never sees analytics. The only real numbers come from Creedom screenshots the owner pasted.

### 3.2 Rules about hooks

- The arc (§ 1.3 above) came from a reference video the owner sent on 2026-10-30: "Use this formula to make script first" / "And remember to follow this arc from now".
- Owner, 2026-11-11: "try something miraculous in the first 6-7 seconds that really feels like 'whoa what is happening in this reel'". 2026-11-15: "pls make the hook more engaging people may skip that". 2026-11-10: "The starting hook texting, styling and how the text appears feels very dull and basic make it feel premium".
- "Problem first, then solution": "the script and hook should be based on the logic of people's problem they face and how we can provide a solution based on it" (2026-11-12).
- Name the unique point: "No these dont hooks dont emphasize on the fact that there is an app that can rate your video before you post".
- Be accurate: "But when does instagram tells your reel flopped?" (a hook rejected as untrue); "10 seconds" removed from a STUDY hook "as untrue".
- The five formulas from their 12-creator audit (2026-11-12): "News plus a fix, within a day"; "GitHub stars as proof ... usually with 'free and open source'"; "Secret codes or a numbered list"; "The best tool for each job: the most-saved post in the sample"; "Disbelief: 'This shouldn't be possible'". Plus "News alone underperforms. News plus a demo wins" and "'5 prompts / codes' lists get the most saves".
- Techniques that shipped: cold open with the hook text on frame 0; "skip-then-callback" (a fake "Hey guys, welcome back" reel gets swiped, then "This video already lost you"); a 1.2 s mid-hook pause cut to 0.3 s; the hook's payoff noun as the one accent word.
- PDF rules they sell to their own audience ("20 Hooks That Work"): "Open with the result, not a greeting", "Make frame one move", "Show it, then explain it".

### 3.3 Rules about length and pace

- House target "7-30 s (max 60 s)" became "7-58 s (always under 60 s)" and "aim for 45-58 s" for what-ifs. Shipped finals: 23.5 to 38.5 s for explainers, 30 s for GTA, 52 s for REPO.
- From the audit: "Lists and codes: 19-26 s. Repo explainers: 23-41 s. Tutorials: 60-90 s. Build demos: about 2 minutes."
- Script length that worked: "about 75-110 spoken words for 23-38 s" (HyperFrames narration guide: 2.5 words per second).
- Pace fixes the owner approved in one go ("Go with all of them"): "voice 1.12x, a punchier 120-128 BPM track, split score scene, snappier transitions, punch-ins on key words, more in-between motion, busier sound, start in motion."
- "a new idea every half second to second"; "not a single frame should feel dull"; "Something moves at every moment"; "a camera that never sits still"; "a cut or card change every 1.5-2 s".
- Words appear only as spoken: "Animate this in a way they only appear when it's spoken not every word already there before even spoken".
- "remove the bottom captions cause they do feel uneccesary, keep the above caption type texts": the one-line headline band replaced bottom captions.

### 3.4 Rules about the CTA, keyword and caption

- Keyword only on resource posts: "Keep reach posts and lead posts separate. Use the keyword only on resource posts: repos, prompt packs, guides. Wonder and news posts should end on a question or 'follow', so the keyword doesn't cost them reach." Codified as § 7 of the skill.
- "the hook and the topic drive reach, while the 'Comment KEYWORD' line turns that reach into leads."
- "Saves come from lists, codes and prompts written out in the caption ... Shares come from wonder clips and news that affects the viewer. Comments come from the keyword CTA and from direct questions."
- Keyword choice: the resource's own noun (REPO, STACK, BACKUP, EXAM, POSTS, CLONE, CLOSE, SPY, CHATGPT, FABLE, GAME, CONSOLE, AGENT, HALLMARK, MOD); weekly series idea "This GitHub repo has ___ stars and replaces a ___/month app" with the repo name as the keyword. Spoken as `Comment "X" and I'll DM you ...`, on screen as a typed comment box, in the caption as line one.
- Caption format: CTA line, hook, numbered body, "Save this ...", credits, 5 lowercase hashtags, one SEO line. Part 2 of REPO also ends on a question ("Which chest are you opening first?") and has a pinned comment and a "Follow @ai.nxtlvl so you don't miss Part 3" line inside the DM.
- Auto-DM text shape, from `secret-store-9x16/POST.md`: a one-line header, numbered "Name (X alternative): link" rows, the locked extras, one follow line. Set up "before the reel goes live".
- Cover: "Make the sure the cover image represents the actual context of video and viewers tap on the video to check it out"; a short headline with one accent word, the hook object, a black pill with the keyword.
- Posting time: nothing written anywhere. No calendar, no best-hour note. (Our own data says 16:00-19:00 for @elcoyotediesel.)

### 3.5 What flopped and why (their own words)

- Voice: "the voiceover done in the video is feeling weird fix that make it natural" (Chatterbox cloned, over-emoted, atempo 15 percent). Fix became the house rule: Kokoro af_heart spoken directly, no atempo, no cloning.
- Look: "The whole art style looks weird, go with profesional after effect type of feel"; "Remove these shapes that are floating around"; "Remove these bubble things in background it looks like an pimple"; the papercraft version of a reel was dropped; the v2 GTA part 2 "looks like a reskin of the reference" and was rebuilt in a Vox style; "don't keep that single robot mascot" for people-heavy stories.
- Clarity: "I feel like the dull intentional video may not be understood by many viewers" (a deliberately boring fake hook had to get a payoff).
- Trust: Creedom flagged the blurred tool name at 0:14 of the GTA reel ("viewers may lose trust"); the owner wanted it blurred ("keep the suspense").
- Repetition: "this looks like the rebranding or some kind of part 2 of that earlier video we made, and I don't want to do that" (vary concept, voice and footage between reels for one client).
- Technical: HDR phone clips promoted the whole render to HDR ("DOM layers lose their stacking (overlays and washes vanish), frames go dark"); renders killed when the parent shell exited; disk full before renders; never loudnorm a short SFX; Chromium PDFs drop leading spaces.
- Process: keyword reels shipped with nothing behind them ("the Creedom link was asked for at least ten times ... and never sent"; three PDFs never hosted); the repo is public so the lead magnets people comment for are downloadable from GitHub ("being public may undercut them").

### 3.6 The comment-to-DM Graph API service (`automation/instagram-dm/`, branch project-thread, PR 11, unmerged)

TypeScript, Node 22.18+, Hono, "27 tests, no network", uses only the official Instagram API with Instagram Login. From its README:

- Flows: comment-to-DM ("gets the DM within seconds, as a private reply to their comment. Optionally a short public reply"), DM keyword auto-replies, welcome and fallback, up to 4 ice breakers, `ig.me/<username>?ref=` referrals, human takeover ("When someone on the team replies in the Instagram app, the bot stays quiet in that chat for 12 hours").
- Explicit limits: "It does not follow accounts or send DMs to people who haven't contacted the account. Meta has no API for either." "a private reply can only be sent once per comment and within 7 days of it; DM replies only within 24 hours of the person's last message. Each person gets one DM per post per trigger, however many times they comment."
- Routes: `GET/POST /webhooks/instagram` (verify token, `X-Hub-Signature-256` check), `/oauth/start`, `/oauth/callback`, `/meta/deauthorize`, `/meta/data-deletion`, `/admin/reload`, `/admin/refresh-tokens`, `/healthz`. State in `data/store.json`.
- Rules file per client `brands/<client>/dm-automations.yaml`:

```yaml
account: nxtlvl.social
comment_triggers:
  - keywords: [FIGHT]          # whole word, any case, punctuation and emoji ignored
    project: fight-night-9x16
    media_ids: []              # empty = any post
    dm: "Here's the free /court skill {link}"
    link: https://github.com/alexyc9381/court-skill
    public_replies: ["Sent! Check your DMs", "Just DM'd you"]
dm_replies: [{keywords: [price, pricing, cost, how much], reply: "Our packages start at ..."}]
welcome: "..."   fallback: "..."   ice_breakers: [...]   referrals: [{ref: bio, reply: "..."}]
```

- Meta app checklist: Business or Creator account, "Allow access to messages" on, Business app with the Instagram product, webhooks `comments`, `messages`, `messaging_postbacks`, `messaging_referral`, then business verification and App Review for `instagram_business_basic`, `instagram_business_manage_messages`, `instagram_business_manage_comments` ("Review usually takes 1 to 3 weeks"). Hosting: "any always-on Node host (Render, Railway, Fly.io, a small VPS)" plus a tunnel for development.
- What actually runs their DMs is still unknown ("The automation tool ... was never named in the chat or the repo").

---

## 4. Better and worse than our stack

Our stack: `build_reel3.py` (ffmpeg 9 plate renderer with EDL JSON: slots, speed ramps, punch-ins, whip xfades, vidstab, ASS captions, SFX kit, loudnorm -14, x264 crf 17 recipe) and the Remotion 4.0.545 kit in `VIDEO/tools/rival-reels/src` (`Root.tsx` 1080x1920 at the plate's fps via `calculateMetadata`, `RivalReel.tsx` with a props-driven overlay registry over `OffthreadVideo`, `theme.ts` brand tokens and fonts, `components/anim.ts` with `prog`, `pop` = `spring({damping:16, stiffness:170, mass:0.9})`, `tailFade`, `Cards.tsx` and `Text.tsx` with 13 components, `Chandler.tsx`, `Brand.tsx`).

### 4.1 Where they are ahead

1. **The clock is the voice, not the footage.** `words.json` from ASR drives every element (`T("p04","paid")`), so a 500-tween reel is authored as "this chip lands on that word". Our EDL takes hand-typed seconds (`[["What?",2.9],["I",3.3]]`) and our Remotion overlays take `at`/`dur` in seconds. We already produce word timings (`watch.py` runs Whisper), we just do not feed them back into the overlay props.
2. **Generated compositions with a visual event log.** `generate.py` writes `index.html` plus `cues.json`/`sfx_events.json`, and `audio.py`/`sfx_mix.py` gives every logged event a sound. Our SFX list is typed separately from the captions and overlays, so hits and pops drift.
3. **Two takes per line, machine-picked.** WER against the script, then pitch spread; trim, join with beat-sized gaps, polish, write word times. Cheap and it removes the "which take" conversation.
4. **A written house grammar.** Arc beats labelled in every script, a safe-zone grid, caption rules, caption.md with the paste-ready description, a cover built from the composition, an auto-DM block, a pre-render checklist. Our playbook has the rules; the per-reel artefacts are not standardised.
5. **The card kit itself.** One fixed layout the viewer learns on item 1, elements changing every 0.9 to 1.3 s with zero hard cuts, a HUD progress cue, the demonstrated CTA. We have `SpecCard`, `StrikeList`, `CommentDrop`, `CountCard`; we lack the HUD, the stamp, the single-item strike, the DM preview, the ghost word and the iris.
6. **HyperFrames' tooling around the render:** `lint`, `check` (runtime errors, layout, contrast), `timeline --json`, `snapshot --at`, a Studio preview the owner can click into, a catalog of about 450 blocks, batch renders from a rows file. Remotion has Studio and `@remotion/*` packages but no lint for seek-safety or safe zones.

### 4.2 Where we are ahead, or they are worse

1. **Footage.** Their whole system is faceless and synthetic. Jacob's PERSONAL pillar runs 14.8 percent ER on the same reach as sponsor posts at 1.36 percent; the face and the truck are the asset. Remotion over `OffthreadVideo` with a cutout layer is exactly the right shape for us; HyperFrames can place `<video>` clips too, but nothing in their repo shows a footage-first reel done well (the only real footage reels are client talking heads with overlays).
2. **Platform fit.** Their pipeline is Linux and cloud: `setsid nohup`, `/root/tts/.venv`, bash render scripts, Puppeteer with a pinned Chrome download, and a documented failure mode when the parent shell exits. Remotion runs natively on this Windows box today with fonts, brand tokens and 25+ components already built and tested (DFC reels shipped 2026-11-21).
3. **Codec control.** Our x264 recipe (High 4.2, crf 17, 1 s closed GOP, aq-mode 3, deband and grain, bt709 tags, HLG tone map on input) is more deliberate than `--quality high` or `--video-bitrate 11M`. Their HDR incident is the bug our tone-map step already prevents.
4. **No analytics loop at all on their side.** The editor never sees skip rate or saves. Our `posts.tsv` has `skip_rate_pct` per reel and the account audit; that is the feedback loop they are missing.
5. **Version churn risk.** They pin `hyperframes@0.8.203` while npm is at 0.9.77 and the CLI nags "7 HyperFrames skills out of date". The contract (`data-*`, one paused timeline) is stable, the flags and skills are not. Remotion 4.0.x has been stable for us.
6. **Bounce everywhere.** Their reels use `back.out(1.6-3)` on nearly every entrance, against their own skill doctrine. Jacob already called heavy outlines and saturation "crap"; the restrained read is ours to keep. Take the timings, not the overshoot amounts.

### 4.3 Judgements

**HTML + GSAP + HyperFrames versus Remotion for card reels on a CPU-only Windows box:** do not switch. Both are Chromium-screenshot renderers with FFmpeg behind them, so render speed on CPU is the same order (their 3-5 fps on a cloud box; ours comparable per frame, and we have no GPU either way). HyperFrames' real advantages are the authoring contract an LLM writes fluently (flat HTML plus a Python generator), the lint/check gates and the block registry; Remotion's are that it is already installed, branded, Windows-native, footage-first and typed. The card grammar ports cleanly: a `Sequence` per item driven by word times, `interpolate` for strikes and counters, `spring` for drops. What to borrow is the generator layer: a small script that reads `words.json` plus a short item list and emits the `overlays[]` and `captions[]` props for `RivalReel`, so Jacob's voice (or a scratch VO) becomes the clock. If we ever want a pure card series at volume, revisit HyperFrames then, in WSL, with the registry as the reason.

**Is Kokoro worth installing (CPU, Python 3.12)?** Yes, as a scratch-voice and timing tool, not as a published voice. Facts checked 2026-11-21: PyPI `kokoro` 0.9.4 requires Python >= 3.10 and < 3.13 (our 3.12.10 qualifies) and pulls `torch`, `transformers`, `misaki[en]` (English G2P, no espeak needed for most words; espeak-ng is the out-of-vocabulary fallback and is not on this machine); model `hexgrad/Kokoro-82M` is Apache 2.0, `kokoro-v1_0.pth` plus per-voice `.pt` files (`af_heart`, `af_bella`, `am_michael`, `am_puck` and so on). Lighter route: `kokoro-onnx` 0.6.1 (Python >= 3.10 < 3.14) needs only `onnxruntime`, `numpy`, `phonemizer` and `espeakng-loader` (bundles espeak), with the ONNX model and a voices file; no torch, so a few hundred MB instead of a gigabyte-plus, and CPU inference of an 82M model is faster than real time for short lines. Install it in its own venv, never into the system Python. Uses for us: (1) hear a script at 150 wpm before Jacob films, to cut lines and set the arc; (2) a scratch VO so a card reel can be laid out and timed before he records his own read, then swap the real voice in and re-run the word timing; (3) the rare faceless list reel (the "nine stock parts leaving the F600" idea) if we decide to test one. Keep their rules: speed in the model call, not atempo; two takes; Whisper picks; explicit respellings for part names ("Powerstroke", "4R100"). Do not voice the main account with it; the data says Jacob's own delivery is the engagement.

**Should any GSAP timing recipes be ported into our Remotion anim helpers?** Yes, five of them, with their shipped values rather than the doctrine values: the 0.35 s card drop with a small overshoot and 40 px rise; the 0.2 to 0.3 s chip pop staggered on spoken words; the 0.25 s stamp from scale 2.4 and minus 20 degrees; the 0.3 s left-to-right strike; the 0.6 to 0.9 s `power3.out` count-up with `tabular-nums`. Plus the typing and heart beats for the CTA kit, the 0.6 s iris, and the `springEase` closed form (useful because Remotion's `spring()` already is a closed form, but their damping table maps nicely to configs: damping fraction 1.0 = our calm settle, 0.8 = "felt not seen", 0.65 = their shipped bounce). Ease equivalents for `interpolate`: `power3.out` = our `EASE_OUT` cubic; `power4.out` = `1 - (1-t)^4`; `expo.out` = `1 - 2^(-10t)`; `back.out(s)` = `1 + (s+1)*(t-1)^3 + s*(t-1)^2` with s = 1.70158 for `back.out(1.7)`; `steps(n)` = `Math.floor(t*n)/n`.

---

## 5. Port list for rival-reels

Component names are proposals for `VIDEO/tools/rival-reels/src/components/`; palette and type stay El Coyote (`theme.ts`: black, cream `#efe9dc`, tan `#c9b38c`, oxblood `#7a1f1f`, Anton/Poppins/Instrument Serif), never cream-and-coral.

| # | Port | Source in their repo | Exact values to carry over |
|---|---|---|---|
| 1 | `anim.ts`: add `backOut(s)`, `power4Out`, `expoOut`, `steps(n)` eases and a `popSoft` spring (`damping 12, stiffness 170, mass 0.9`) beside the existing `pop` | `.claude/skills/hyperframes-animation/adapters/gsap-easing-and-stagger.md`; shipped eases in `prod-guard-explainer-9x16/build/generate.py` | `back.out(1.7)` s = 1.70158; `back.out(2)` s = 2; card drop 0.35 s (10-11 frames); chip 0.2-0.3 s (6-9 frames); stagger 0.06 s words, 0.14 s chips, capped so a group lands inside 0.5 s |
| 2 | `ProgressHud` (`count`, `total`, `handle`) | `prod-guard-explainer-9x16` `.top`/`.prog`; REPO frames for the dots variant | y 262 (ours: inside `SAFE.top` 290), label mono 30 px letter-spacing 4 px with an 18 px dot; pill 220x26, 3 px border, fill `scaleX 0 -> 1` linear over the reel; dots variant: `total` 20 px dots, filled on each item's start word |
| 3 | `Headline` (one phrase, one accent word) | `.hl` in prod-guard | words rise `y 40 -> 0, opacity 0 -> 1`, 0.32 s, stagger 0.06 s, `back.out(2)`; accent `scale .6 -> 1, rotation -6 -> 0, opacity`, 0.45 s, `back.out(2.4)`, starts 0.3 s after the first word; sizes 76 px sans / 128 px serif italic (ours: Anton 76 / Instrument Serif Italic 128 in tan) |
| 4 | `WordPillCaption` (spoken word highlighted) | `captions()` in prod-guard | chunks of at most 4 words or to punctuation; chunk in `y 16 -> 0` 0.12 s; active word pill `padding 2px 12px 6px; radius 16` set at `word.start - 0.02 s`, cleared at the next word; pill colour = our `C.hi` `#e2543e` or oxblood with cream text |
| 5 | `ItemCard` (the swap card: icon tile, name, mono sub-line, counter pill, outline tag, chips on words, footnote, corner sticker) | `.card`/`.chip`/`.chipcmd` in prod-guard; `#endc` in `ai-exam-9x16` for the hard shadow | card radius 28 (end card 40), border 3 px ink, hard shadow `12px 13px 0 ink` (REPO look) or soft `0 18px 40px rgba(60,40,20,.12)` (October look); chips `padding 8px 18px; radius 30; mono 700 26px; letter-spacing 2px`; entrance `y 40 -> 0, scale .92 -> 1`, 0.35 s, `back.out(1.7)`; optional ghost state: 0.3 s at 30 percent opacity then snap to 1 |
| 6 | `CountUp` (prop on `ItemCard`, `SpecCard`, `CountCard`) | `prod-guard` rows counter, `gta6` views counter, `counting-dynamic-scale.md` | 0.6-0.9 s, `power3.out` (ours `EASE_OUT`), `Math.round(v).toLocaleString("en-US")`, `fontVariantNumeric: "tabular-nums"`, fixed-width box, no overshoot on the number, suffix (`hp`, `psi`, `K`) lands after the count; drain variant `power2.in` from word A to word B |
| 7 | `StrikeStamp` (single item: strike bar then a rotated stamp) | `surrender-ad-9x16` `.strike`, `prod-guard` `.stamp` | bar `height 12px; radius 6px; transformOrigin 0 50%`, `scaleX 0 -> 1` 0.3 s `power3.out`; stamp `border 8px; radius 16px; font 800 76px; rotate(-8deg); background rgba(cream,.92)`, enters 0.12 s after the strike from `scale 2.4, rotation -20, opacity 0` over 0.25 s `power4.out` (replace `tailFade`-less pop in `StrikeList` with this per item) |
| 8 | `GridWall` upgrade: 3x3 hook grid with `PAID`/`STOCK` tags that strike and stamp left to right | REPO frames 0-5 s; `GridWall` already exists in `Chandler.tsx` | 9 tiles, tag chip top-right, stamp cadence one tile per 0.22 s (9 in 2 s), ribbon slides in under the grid after the last stamp |
| 9 | `GhostWord` (giant outline word behind a scene) | `.giant` in prod-guard | `font 800 330px; letter-spacing -10px; color transparent; WebkitTextStroke 4px rgba(ink,.08)`, enters `scale 1.25 -> 1, opacity 0 -> 1` 0.5 s `power3.out`, exits 0.15 s fade; Anton 330 in our kit |
| 10 | `IrisWipe` (the one full-frame transition before the CTA) | `sucsess-maperrs-9x16/build/generate.py` lines 237-263 | `clipPath: circle(0% at 50% 40%) -> circle(86% at 50% 40%)` 0.6 s, then reverse; REPO: a solid accent circle grows 0.3 s and shrinks 0.3 s; use oxblood |
| 11 | `CommentGate` (comment box typed and hearted, then a DM preview card) | `.ec-box` in `ai-exam-9x16`; `.dm` in `creedom-check-9x16`; `#dm` in `gta6-playbook-9x16`; `CommentDrop` already exists | box 640-940 wide, radius 26-66, border 3 px ink, hard shadow `6px 7px 0`, avatar 52 px gradient, "you · now" mono 18 px, word typed one letter per 0.09-0.12 s with a `|` cursor, heart 44 px grey -> accent with `scale 1 -> 1.5 -> 1` over 0.3 s on the keyword; DM card 760x124, radius 30-36, logo tile 72 px, `b` 32 px / `span` 28 px / `em` mono 20 px "now", enters from `y -160, scale .9` 0.4-0.7 s `back.out(1.4-1.6)` on the word "send", then numbered chips fill two per beat; end hold 2.5 s silent |
| 12 | `wordsToProps.py` (generator layer): `words.json` + an items list -> `overlays[]`/`captions[]` JSON for `RivalReel` | `prod-guard` and `gta6` `generate.py` (`T(line, word)` lookup, scene windows at line start minus 0.12 s, `edit.json`, `sfx_events.json`) | cue = word start, card drop at the item's name word, chips at their words, strike 0.5 s after the question word, CTA on "comment"; also emit the SFX list (`whoosh` on card, `pop` on chip, `stamp` on stamp, `tick` on typing, `notify` on the DM) for `build_reel3.py`'s `sfx` block with their peaks (whoosh -10 dBFS, pop -12, stamp -7, tick -17, notify -12) |
| 13 | Voice scratch track: `kokoro-onnx` in a venv, two takes per line at two speeds, Whisper pick | `gta6-playbook-9x16/build/vo_kokoro.py`, `build/vo_pick.py` | `af_heart` or `am_michael`, speeds 1.06-1.25 chosen in the call, trim 0.04 s before first word to 0.12 s after last, 12 ms fades, gaps per beat (hook .2, peak .3, release .22, CTA 0) times 0.4, polish `highpass 80, acompressor -20 dB 3:1 attack 5 release 80 makeup 2, loudnorm I=-16 TP=-2 LRA=9`; never atempo more than 1.04 |
| 14 | `caption.md` per reel in `VIDEO/<project>/` plus a cover frame rendered from the composition | their `caption.md`, `build/cover.cjs`, `nxtlvl-social-video` § 6 | order: CTA line, hook, numbered body, 5 lowercase hashtags, one comma-separated search line; cover = the composition seeked to the hook frame with a keyword pill, key content inside y 240-1680 |
| 15 | Pre-render lint additions to `build_reel3.py` / a Remotion check: safe zones (top 250, bottom 400, 60 px sides), hook element visible by frame 4, no static stretch over 4 s, every number element uses tabular figures | `nxtlvl-social-video` § 3 and § 5; `hyperframes check` behaviour | our lint already checks hook timing and static slots; add the safe-zone box test on overlay positions |

Not worth porting: the pixel mascot (no coyote mark drawn yet), the chiptune bed synthesiser, the three.js voxel worlds, the glass-UI recipe, the Hindi/Hinglish client templates, and the HyperFrames CLI itself for now.

## 6. Files

- `clone/` : depth-1 clone of `main` with six branch refs fetched without media (`.git` about 275 MB). Nothing in it was run.
- `tree.json`, `branches.json` : GitHub API listings used to map the repo (main tree, 3,030 entries; 26 branches).
- This file.
