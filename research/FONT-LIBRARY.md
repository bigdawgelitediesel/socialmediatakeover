# El Coyote font library and lockup combos (locked 2026-11-20)

Jacob picked the direction himself with three Instagram references (saved in `research/font-references/`):

| Ref | Post | What it is | Fonts in the original |
|---|---|---|---|
| 1 (MAIN) | instagram.com/p/DaD4ZaUiJFi slide 2, @hamzakamboj | "Create LOUDER": yellow brush script word overlapping a huge white block word, small italic caps subline, subject low in frame, text in the empty upper half | Billion Dreams (script, paid), Anton (block), Poppins Italic (sub) |
| 2 | instagram.com/p/DetyHzIgaqR slide 3, @pagustian_ | "MEGANTE": heavy grotesque caps in deep red on a muted mint texture, tiny italic labels, a wide thin second rendering | Megante (paid) |
| 3 | instagram.com/p/DIR1UIZIpmF slide 2, @urvbz_ | "TROPI LAND": chunky retro rounded display, warm taupe, floating over sky above a car | DaFont groovy display |

Rule: poster lockups, not caption text. One lockup on the hook, placed in the open part of the frame with Jacob low and whole, 2.5 to 3 s, nothing else burned in. No location pills, no on-screen call to action, no caption band.

## The three combos (all free fonts, files in `research/fonts/` and `OneDrive Desktop/VIDEO/tools/fonts/`)

### Combo A "LOUDER" (default)
- Script word: **Kaushan Script** 190 px, yellow `#F7D43C` (ASS `&H003CD4F7`), rotated -4 deg, overlapping the top of the block word. Alternates: Caveat Brush (rougher), Yellowtail (thinner, retro).
- Block word: **Anton** 380 px, white, tracking +2, caps.
- Subline: **Poppins Italic** 46 px, white, tracking +3, caps.
- Soft blurred black shadow layer under all three (blur 14 to 16, 60 percent alpha, offset 4/8). Fades 100 to 120 ms, block pops from 96 percent, script from 92 percent, sub 0.18 s later.
- Renderer: `{"type":"lockup","preset":"louder","script":"Teach me how to","block":"DOUGIE","sub":"EVERY BAY IN THE SHOP","start":0,"end":3,"pos":[540,520]}`
- Use for: humor, memes, anything with a verb + noun punch ("Teach me how to / DOUGIE", "Traded my / HARLEY", "Built not / BOUGHT").

### Combo B "MEGANTE"
- Block word: **Archivo Black** 260 px, deep red `#8E1010` (ASS `&H0010108E`), caps, tracking +4. Alternate: Anton.
- Thin wide echo (optional second line): **Poppins Light** 150 px, same red, tracking +14, caps.
- Labels: **Poppins Italic** 34 px, same red, caps, tracking +4, top-left and bottom-right of the lockup ("DESIGN BY / EL COYOTE", "20.11 / 2026").
- Works on bright or muted backgrounds (sky, the tan truck, white shop wall). Pair with a light film grain. No shadow layer; the red carries it.
- Renderer: `{"type":"lockup","preset":"megante","block":"PROJECT RIVAL","sub":"EL COYOTE  ·  CHEYENNE WY","start":0,"end":3,"pos":[540,520]}`
- Use for: build updates, partner reveals, anything that should feel like a print poster.

### Combo C "TROPI"
- Single display word: **Shrikhand** 300 px, warm taupe `#5A4A42` (ASS `&H00424A5A`) or oxblood `#7A1F1F`. Alternates: Bagel Fat One (rounder), Chango (heavier), Rubik Bubbles (bubblier).
- No subline, or Poppins Medium 40 px in the same color.
- Float it over sky or a plain wall above the truck, slight -3 deg rotation.
- Renderer: `{"type":"lockup","preset":"tropi","block":"EL COYOTE","start":0,"end":3,"pos":[540,520]}`
- Use for: the truck outside, golden hour, nostalgia beats.

## Reference 4 (added 2026-11-21): @asherintech "The fonts I actually use"

Jacob sent instagram.com/p/DfcJ9VTEQsq (slides saved as `research/font-references/fontref_4_*.jpg`). Streaming-UI grammar: every slide is a Netflix-style beat ("Next episode", "Season finale", "Previously on...", "Skip intro", "Plot twist.", "Still watching?", "Roll the credits") set in one of six fonts over a dimmed photo, with an EP. 01 / 06 progress bar. The six, with licence and the stand-in we already own:

| # | His font | Where it is used | Licence | Our stand-in (on disk) |
|---|---|---|---|---|
| 1 | Helvetica Neue | default for titles, labels, captions | ships with macOS only, not on this PC | **Inter** (he lists it himself; Regular to Black added 2026-11-21) |
| 2 | Inter | clean UI-style overlays and story frames | free, Google Fonts / SIL OFL | **Inter** |
| 3 | Galderglynn 1884 (Typodermic) | tall condensed caps for punchy titles | paid | **Bebas Neue** (his own free alternative) |
| 4 | Founder's Hand (Jen Wagner Co.) | handwritten touch on covers and stories | paid; his free alt Hey Tiny is a personal-use demo | **Caveat Brush** (commercial-safe); Kaushan Script if it should read as script, not marker |
| 5 | Advercase (Indieground) | elegant condensed serif for captions and hooks | free for personal use only, so not for the account | **Instrument Serif** or **DM Serif Display** |
| 6 | Editor's Note (Jen Wagner Co.) | editorial serif titles, roman mixed with italic in one line | paid | **Instrument Serif** Regular + Italic (his own free alternative) |

His signature combo ("Roll the / credits"): a small handwritten word (Founder's Hand) tucked on top of a big lowercase Helvetica Neue Bold word. Ours would be Caveat Brush 90 px over Inter Bold or ExtraBold 300 px, white, no shadow layer, over a dimmed plate. Candidate **Combo D "CREDITS"** for series beats on the build episodes (S1 EP cards, "Previously on", "Season finale", a "Still watching?" mid-reel beat). Not rendered or approved yet; it lands in the renderer only after Jacob picks it on an artboard. Note the earlier rejection of Instrument Serif as a lone hook still stands; here it is the roman + italic title mix, a different use.

## Colors
- Yellow `#F7D43C` (script in Combo A; the lyric reel yellow `#F8D000` is close enough to swap)
- White `#FFFFFF` (block words)
- Deep red `#8E1010` (Combo B)
- Taupe `#5A4A42` and oxblood `#7A1F1F` (Combo C)
- Coyote tan `#C9B38C` stays the accent for site and labels, never the script word.

## Fonts on disk (static TTFs, libass-safe; all SIL OFL or Apache)
Anton, Archivo Black, Bebas Neue, Kaushan Script, Caveat Brush, Yellowtail, Poppins (Light, Medium, SemiBold, Italic, MediumItalic, SemiBoldItalic), Shrikhand, Bagel Fat One, Chango, Rubik Bubbles, Montserrat (SemiBold, Bold, ExtraBold), Oswald (Medium, Bold), Instrument Serif (Regular, Italic), DM Serif Display/Text, Playfair Display (variable, renders Regular only), Inter (Regular, Medium, SemiBold, Bold, ExtraBold, Black; added 2026-11-21 from the @asherintech guide).

## Rejected (do not come back to these)
Oswald Bold + Montserrat SemiBold caption system, Anton-alone hook, Bebas-alone hook, Instrument Serif hook, thick outlined ExtraBold, any per-word highlighted captions, the dark caption band.

## MAIN FONTS (Jacob's pick, 2026-11-23, supersedes the lockup combos as the default)

Source: @kalylsfilms reel DcBwAjvoEqI ("my favorite fonts", 40,598 likes). Jacob: "I love these fonts and want them as my main fonts in my style guide!"
Breakdown: `research/reel-references/2026-11-23-DcBwAjvoEqI/BREAKDOWN.md`.

| Role | His font | Used here | Licence |
|---|---|---|---|
| Big word | Impact | Impact (Windows system font, not in this repo) | system font; do not redistribute |
| Classy line | Snell Roundhand | Pinyon Script (`research/fonts/PinyonScript-Regular.ttf`) | stand-in, SIL OFL. Real font is paid Linotype, bundled with macOS and iOS |
| Painted word | Rocktown (Khurasan) | Permanent Marker (`research/fonts/PermanentMarker-Regular.ttf`); Knewave as a second option | stand-in, Apache 2.0. Real font is personal-use only without a paid licence |

Pairing: Impact caps always; one of the other two on top of it, never all three. Yellow `#FDC43A`, red `#F04625`, white. Top third, never on the face.
Renderer: Remotion overlay `mainlock` (Main.tsx). ASS names: Impact, Pinyon Script, Permanent Marker.
Combos A LOUDER, B MEGANTE and C TROPI stay on file but are no longer the default title.

