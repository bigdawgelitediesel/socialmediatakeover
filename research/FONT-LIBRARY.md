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

## Colors
- Yellow `#F7D43C` (script in Combo A; the lyric reel yellow `#F8D000` is close enough to swap)
- White `#FFFFFF` (block words)
- Deep red `#8E1010` (Combo B)
- Taupe `#5A4A42` and oxblood `#7A1F1F` (Combo C)
- Coyote tan `#C9B38C` stays the accent for site and labels, never the script word.

## Fonts on disk (static TTFs, libass-safe; all SIL OFL or Apache)
Anton, Archivo Black, Bebas Neue, Kaushan Script, Caveat Brush, Yellowtail, Poppins (Light, Medium, SemiBold, Italic, MediumItalic, SemiBoldItalic), Shrikhand, Bagel Fat One, Chango, Rubik Bubbles, Montserrat (SemiBold, Bold, ExtraBold), Oswald (Medium, Bold), Instrument Serif (Regular, Italic), DM Serif Display/Text, Playfair Display (variable, renders Regular only).

## Rejected (do not come back to these)
Oswald Bold + Montserrat SemiBold caption system, Anton-alone hook, Bebas-alone hook, Instrument Serif hook, thick outlined ExtraBold, any per-word highlighted captions, the dark caption band.
