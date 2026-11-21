# words_to_props.py: spoken words -> rival-reels props

The generator layer for menu reels. You record the voiceover first, time it with Whisper (words.json), write a
short spec of the items and their cue words, and this script writes the props JSON that `CardReel` / `RivalReel`
render. Every card, chip, strike, stamp and caption lands on the start of a spoken word. This is the
@ai.nxtlvl structure (PIPELINE-STUDY.md 1.5 and 5/12): picture generated to the words, not a footage-first EDL.

Files
- `tools/words_to_props.py` (the generator)
- `tools/specs/menu-reel-example.json` (annotated schema + a Rival example)
- `tools/specs/nxtlvl-recreate.json` (the test spec, 9 items from the nxtlvl voiceover)
- output: `<out>.props.json` and `<out>.sfx.json` next to it

## Run

```
"%LOCALAPPDATA%\Programs\Python\Python312\python.exe" -I "...\VIDEO\tools\words_to_props.py" spec.json words.json out\name.props.json
cd rival-reels
npx remotion render src/index.ts CardReel out/name-video.mp4 --props=out/name.props.json --codec=h264 --crf=18 --log=error
```

Then mux voice + sfx with build_reel3.py (its `sfx` block takes the `.sfx.json` list as is).

## Input 1: words.json

Whisper word list: `[{"w": " word", "s": 0.46, "e": 0.80}, ...]`, seconds, leading space on `w` is fine.
Cue matching normalizes each word to lowercase letters and digits and matches by prefix, so `cue: "eleven"`
hits " Eleven" and `cue: "600"` hits " 600".

## Input 2: the reel spec

```
{
  "composition": "CardReel" | "RivalReel",
  "bg": "#0b0b0c" | "paper" | "still.png" | "clip.mp4",      CardReel
  "plate": "plate.mp4", "cutout": "cutout.webm",               RivalReel
  "fps": 30,
  "handle": "@elcoyotediesel",                                  HUD handle (optional)
  "ghost": "RIVAL",                                             giant outline word behind everything (optional)
  "hook": { "text": "max seven words", "accent": "one word" },
  "hud": "dots" | "bar" | null,
  "sidebar": true | false,
  "captions": "auto" | "none",
  "captionStyle": "plain" | "pill",
  "captionY": 1129,                                             override (optional)
  "items": [
    {
      "name": "Driven Diesel fuel system",     card title
      "short": "Fuel system",                  sidebar label and gate chip (optional, default name)
      "cue": "driven",                         spoken word that triggers the item
      "at": 12.4,                              explicit start in seconds instead of a cue (optional)
      "old": "Stock lift pump",                StrikeStamp row at the cue, card 0.5 s later (optional)
      "oldTag": "STOCK", "oldMeta": "1999", "stamp": "RIVAL",
      "sub": "regulated return", "icon": "cards/x.png", "tag": "PARTNER",
      "count": { "to": 600, "prefix": "", "suffix": " hp", "label": "ready" },
      "chips": [ { "text": "Regulated return", "cue": "return" }, { "text": "timed", "after": 0.8 } ],
      "foot": "footnote", "sticker": "ON THE TRUCK", "stickerCue": "truck",
      "accent": "Driven"                       caption accent word (optional, default first word of name)
    }
  ],
  "gate": { "word": "RIVAL", "reply": "Your Rival parts list", "items": [...], "cue": "comment", "handle": "you" }
}
```

Cue forms: `"word"`, `"word#2"` (second hit), `"two words"` (consecutive words), or `{"word": "x", "nth": 2}`.
Item cues are searched forward from the previous item's cue, so a repeated word ("open") resolves to the next
one spoken. Chip cues are searched forward from the card inside the item's window, in the order listed.
`gate` is optional and under the house rule: only on a comment-gated deliverable reel (parts list, checklist).

## Timing rules

| rule | value |
|---|---|
| card appears | cue word start minus 0.12 s |
| `old` set | StrikeStamp at cue minus 0.12 s, item card 0.5 s after that |
| chip `at` | (chip cue start minus card start) in frames, clamped at 0 |
| sticker | at `stickerCue`, else 10 frames after the last chip, else frame 24 |
| item window | from its start to the next item's start (last item: to the iris, or the end) |
| HUD | count 0 during the hook, then one `hud` overlay per item window with count = item number |
| sidebar | one `sidebar` overlay per item window, `current` = item number, 2 columns above 5 items |
| headline | the hook text, 0 to the first item start |
| captions | none during the hook, none during the gate, grouped 2 to 5 words, max 28 chars (one line), split on gaps > 0.55 s and . ! ?, singles merge into the previous group (forward if they open an item), never across an item start |
| caption accent | the item's first name word, only when that word is actually spoken in the group |
| caption end | next group start if the gap is under 0.8 s, else last word end + 0.4 s |
| gate | at its cue minus 0.12 s; iris 0.4 s before it (0.7 s long); DM card after the word is typed |
| durationSec | last word end + 1.6 s hold |

Layout (1080 x 1920, values in the code as of 2026-11-21): HUD y 300, headline 440, strike row 620, card 660 (780 under a strike), gate 660, captions 1150 to 1180 (2 to 4 words, 24 chars max),
captions at sidebar top minus 130 (1150 without a sidebar), sidebar anchored so it ends at y 1430.
Overlays are emitted in time order with hud/sidebar before the card at the same `at`, because CardReel
stacks overlays in array order.

## Lint (nothing is written when any of these hit)

- a cue word is not found in its search range (item, chip, sticker or gate)
- two item cards overlap by more than 0.3 s
- the hook has more than 7 words
- any text is estimated to sit below y 1440 (HUD, headline, strike, card, captions, sidebar, gate DM)
- an item window is shorter than 1.2 s, or a card would show for under 0.6 s
- an item's card bottom collides with the caption line (drop `foot` or chips, or move the sidebar)

The plan table (item, cue word, cue time, start, card time, window, chips) prints before writing.

## SFX events (`<out>.sfx.json`)

`[{ "at": 5.58, "kind": "whoosh", "gain_db": -10, "kit": "whoosh", "file": "...\\tools\\sfx\\whoosh.wav" }, ...]`

| kind | when | gain_db (study peaks) | build_reel3 kit sound |
|---|---|---|---|
| whoosh | each card drop, the iris | -10 | whoosh |
| pop | each chip | -12 | click (stand-in) |
| stamp | the StrikeStamp slap (strike + 16 frames), a sticker | -7 | impact (stand-in) |
| tick | each typed letter in the gate | -17 | click (stand-in) |
| notify | the DM card | -12 | none in the kit yet (event is emitted, `file` omitted, build_reel3 skips it) |

build_reel3 reads `file` first and falls back to `kit.get(kind)`, so pop/stamp/tick play through the stand-ins
until proper pop/stamp/tick/notify wavs are added to `tools/sfx/`.

## Test result (2026-11-21)

Spec `tools/specs/nxtlvl-recreate.json` against the nxtlvl voiceover
`research/reel-references/2026-11-21-DfU2nIgt8XK/words.json` (49.9 s, 126 words):

```
 #  item                cue        cue@  start   card   win
 1  Open Generative AI  Hicks      5.20   5.08   5.58  6.88
 2  Voice Studio        Eleven    12.08  11.96  12.46  4.84
 3  Open SEO            SEMrush   16.92  16.80  17.30  4.70
 4  AppFlowy            Notion    21.62  21.50  22.00  4.96
 5  Open Whisper        Whisper   26.58  26.46  26.96  4.34
 6  OpenProject         Asana     30.92  30.80  31.30  3.94
 7  Cal.com             Calendly  34.86  34.74  35.24  4.46
 8  Chatwoot            Intercom  39.32  39.20  39.70  4.68
 9  Cap                 Loom      44.00  43.88  44.38  3.26
gate "REPO" at 47.24 (iris 46.84), duration 51.48 s, 40 overlays, 32 captions, 45 sfx events
```

Negative tests all refused to write: missing item cue, 8-word hook, chip cue outside its window,
0.5 s window, captions pushed to y 1400 (floor), chip cues listed out of spoken order.

Render: `rival-reels/out/nxtlvl-recreate.props.json` -> `out/nxtlvl-recreate-video.mp4`,
contact sheet `out/nxtlvl-recreate-sheet.png` (1 frame per second, 10 x 6), key frames at 5.9, 10.6 and 48.9 s.
Render exit 0 with an empty error log. Read against the transcript: the hook headline holds 0 to 5 s with the
"nine" pill, the HUD ticks 01 to 09 on each strike row, the Higgsfield strike is on screen at 5 s before its
FREE stamp and the card lands at 5.6 s, the three chips arrive at 8, 9 and 10 s on "images", "cinematic" and
"600", every later strike appears one frame-second before its stamp, captions change with the card (no
caption spans two items), the iris and comment box come in at 47 s and the DM card with nine numbered chips
is complete by 50 s. Nothing sits below the sidebar's y 1430 floor. One spec-level note: a `stickerCue` near
the end of an item window (Loom's "click" at 46.74, window ends 47.14) gives the sticker only a few frames;
pick an earlier word or let it default to after the last chip.

## What the components still lack

- `ProgressHud` bar variant only moves per item window (count/total), not continuously across the reel; the dots variant fills instantly on the window start, which matches the study.
- `ItemCard` has no `accent` on the title and no per-chip color; chips are all tan.
- `StrikeStamp` and `ItemCard` cannot be told to stay through a crossfade into the next item (each window hard-cuts; `tailFade` 6 frames only).
- `CommentGate` has no `items` cap; more than 8 gate chips push the DM card toward the floor (the lint catches it).
- No SFX wavs named pop/stamp/tick/notify in `tools/sfx/`; build_reel3 plays click/impact stand-ins and skips notify.
- Captions use `PlainCaption` (whole-group highlight on one accent word), not the per-word pill of the study (port item 4, `WordPillCaption`, is not in the kit yet). The generator keeps the group word lists, so adding it later is a one-line change in the caption emitter.
