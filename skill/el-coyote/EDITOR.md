> **Look before you edit (2026-11-23):** read `research/2026-11-23-LOOK-GUIDE.md` and run its section 9 check before Jacob sees anything. `python -I tools/streamline.py still plan.json -o still.jpg` renders the first and middle frame with the real conversion and grades them (mean luma over 145 or over 3 percent near white is washed out); `lint` runs the same check on the finished file. Open the frames yourself; rules do not judge the picture.

> **Beat words (2026-11-23, Jacob: "I want this in my reels"):** `preview plan.json --beats auto -o preview.jpg` first, look at every frame, then `render ... --beats auto` (or `--beats "word,*word"`). One big word per beat, cream, coral and tan, Shrikhand for the starred flavour word, placed by the face per frame, never on it, over the plain captions. Rule 118.

> **Streamline editor (2026-11-23):** `python -I tools/streamline.py plan --words words.json --src IN.MOV --job talk --open-on "..." --end-on "..." -o plan.json`, then `challenge plan.json --set ... --device ... --tone ...` (doctrine counter-arguments, sameness check against `data/edits/ledger.tsv`, the thinking test), then `render plan.json --lockup "..." -o post.mp4`, `lint plan.json`, `ledger add plan.json --label "..."`. Principles, not steps: `skill/el-coyote/PRINCIPLES.md`. Rotate one axis per episode, never all.

> **Read first (2026-11-22):** `research/2026-11-22-REEL-EDITOR-DOCTRINE.md`. Change, not cut; one physical device per talking head; grade by format; two lengths by job. It overrides the cut cadence, the re-hook, the pilot line and the 60 to 120 s default wherever this file says otherwise.

# EDITOR mode

The pipeline, tiers, components and non-negotiables are in the `reel-editor` skill (`C:\Users\Parts\.claude\skills\reel-editor\SKILL.md`). Load it. This page is what sits around it: choosing the tier, the pre-cut checks, studying a reel, porting a technique, and the delivery gate. Tool CLI reference: `research/inventory/03-tools.md`.

## Before any cut

1. `coyote.py status` and the last-12 pull. Know what he posted today and which calendar slot this cut fills.
2. Watch every candidate clip with `watch.py` (sheets, transcript, words.json). Read the sheets. Say when footage is weak; the edit cannot invent camera moves.
3. Name the one variable this post tests and the person type in caption line 1 before touching the EDL. If you cannot name who sends it to whom, the idea is not ready.
4. Decide the tier.

## Built for a million (first gate, 2026-11-21)

Before the tier: which shape is this? Story (60 to 120 s, narrated, the trouble in sentence one, the answer held to the end), skit (55 to 70 s, one shot, one coworker, the turn on the last line) or loop (6 to 12 s, closed, a joke a stranger gets). If it is 20 to 40 s or needs a part name to be understood, it is not ready; rewrite the open or merge it into a story. Checklist in `research/2026-11-21-MILLION-VIEW-RULE.md` section 3.

## Tier chooser

| Signal | Tier | Tool | Time |
|---|---|---|---|
| Meme, same-day, music-driven, milestone, one joke, 5 to 15 s | Fast | `build_reel3.py` (plate + one lockup) | 20 to 40 min |
| Talking head on real footage, partner or build update, cards on spoken nouns | Motion graphics on plate | build_reel3 NOCAP plate → `RivalReel` props (facetrack, matte, layout) | 1 to 2 h |
| List, menu, explainer, parts counter, no camera or screen captures | Menu / card | `vo_scratch` → spec → `words_to_props` → artboard → `CardReel` → `sfx_place` | 1.5 to 3 h |
| Vote, compare, two takes | Motion graphics | `duel` or `compare` over the plate | 1 h |
| DFC interview set | DFC | `dfc_track` + `gen_dfc`, 24 fps, corner logos on that set only | per memory `project_dfc_video` |

Card-only menu reels at most one a week; the grammar otherwise rides on footage. Rollers (no talk) ship with no text or one label.

## The hook, in order of what the data says

Frame 1 moves (walk-in, head-up, drop, reach-in, the engine turning). First noun by 0.9 s. Text only when the hook is a claim; no text when the hook is a noise or a face. Lockup 3 to 7 words in the empty part of the frame, never over his face. Hook types ranked by sends on this account and the 600-clip measurement: named-tribe news ("7.3 guys, this one's for you"), hater-quote opener ("Leave the '59 alone"), desire hook (outcome then character), third-party news ("Someone just put 600 hp through a stock 7.3 bottom end"), identity test / inside joke (the 10-mil meme). Run `coyote.py lint hook "<text>"` on the spoken first line and on the lockup.

## Artboard before render (new cuts only)

`python -I tools\artboard.py out\<name>.props.json` makes the contact sheet with the 480/1440 safe lines and a lint. Show it, take redlines by tile number, then render. Layout constants live in `words_to_props.py` (Y_HUD 300, Y_HEADLINE 440, Y_STRIKE 620, Y_CARD 660 / 780 under a strike, captions 1150 to 1180). Face owns y 150 to 760 in selfies.

## Delivery gate (all must pass)

- Frame grid read (8 to 9 frames) and the output audio transcribed against caption times.
- `smooth_check.py` clean; `mblur` on fast subject motion; bt709 tags; ebur128 near -14 LUFS; no digital silence.
- No burned-in ask, outro, fade, handle, location pill, grade.
- Lockup is one of the three combos; nothing else on the fast tier.
- El Coyote only; trans detail absent; numbers right (550 to 600 crank, SEMA Nov 2 to 5, 2027).
- Cover still rendered (`Cover` composition) for the grid.
- One Drive folder `<Name> - completed YYYY-MM-DD` with POST mp4, no-captions mp4, `-EDIT.mp4` master, `.srt`, cutout webm if made, `README - posting kit.txt`. Nothing else in the Drive.
- Then MANAGER: caption through lint, slot, pending read added.

## Study a reel (what the `reel-scout` agent does; do it inline for one URL)

1. `yt-dlp.exe --write-info-json -o reel.%(ext)s <url>` into `research/reel-references/<date>-<id>/` (yt-dlp lives in the WinGet packages folder). Read `reel.info.json` for uploader, caption, likes, comments, date. The `/p/<id>/` page with a crawler user agent gives og tags if yt-dlp cannot.
2. `watch.py reel.mp4 --out <folder>` then move `reel/*` up: sheets, transcript, words.json, scenes.csv.
3. Read every sheet. Write `BREAKDOWN.md`: what is on screen second by second, the format and timing, the numbers, "what is new for the kit", "what to take for El Coyote" (always translated to Rival, filtered by the house rules), and the gate shape.
4. Port what is new: a component in the right file (`Menu.tsx`, `Effects.tsx`, `Paper.tsx`, `Rapid.tsx`, or a new file), register it in `REG` in `RivalReel.tsx`, `npx tsc --noEmit`, a test props JSON on `CardReel` or `RivalReel`, render, tile key frames with ffmpeg (`-fps_mode vfr`, not `-vsync`), read the tile, fix layout against the safe lines.
5. Log it: a numbered rule in `DIESEL-HOUR.md` (next number after the last), one line in the reel-editor skill component list, the memory `project_editing_mastery`, snapshot `src/` and the test props into `research/tools-snapshot/rival-reels`, add the folder's `*.mp4` to `.gitignore`, commit, push.
6. Never redistribute third-party media or clones; sheets, transcripts, stats and breakdowns are what gets committed.

## Known open build items (keep this list honest; also in the addendum section 2 and `03-tools.md`)

**First on the list (2026-11-22): the motion-rules port**, `research/2026-11-22-motion-rules-port.md`. Curves by name, duration from distance, uneven reactions instead of staggers, text cuts on, exits faster than entrances, holds alive, one device per reel. About a day in anim.ts and words_to_props.py.


matte.py morphological close; CardReel caption y 360 on paper; serif-italic selection-box accent; PlainCaption y from the face tracker; legacy ASS styles in build_reel3; `rampable` slots; karaoke-dim captions (future words grey, needs per-word times); the remaining port list (digital zoom curve, floor timeline, paper desk, 2.5D teardown or remocn exploded-view, split flap, blueprint wipe, price-slate, rotary dial); the "lower band empty" layout note on card reels; Teardown sim of the 7.3 (needs Jacob's yes against the real-footage rule).
