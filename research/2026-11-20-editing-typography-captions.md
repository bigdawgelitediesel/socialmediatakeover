# Typography, captions and on-screen text for El Coyote Reels (2026-11-20)

Lane: premium-looking captions and titles that Claude can burn automatically with ffmpeg + libass from Whisper word timestamps. Everything in the "recommended system" section was test-rendered on this machine (ffmpeg 9.0.2, libass 0.17.5, HarfBuzz 14.4, DirectWrite font provider) with the fonts in VIDEO\tools\fonts plus two downloads. The ASS lines below are the ones that rendered, not theory.

## 1. What the source videos actually do

Matt Loui, "Smooth Style Captions" (758k views, https://www.youtube.com/watch?v=YddyvmAFxnY)
- Font: Inter Bold; alternates Montserrat, Poppins, Arial, Helvetica. Uppercase, letter spacing -1.
- No stroke. Shadow: blur up, distance 10, angle -70, opacity 25 percent.
- In: opacity 0 to 100 and Y from -100 to 0 over about 12 frames (400 ms at 30 fps), quad ease, fast start then settle. Blur-in and blur-out at 0.5 s. Each word is its own layer, staggered to the word timing.
- Emphasis: one word per group gets a different color (orange-yellow), sometimes a different font and a little glow, and a bigger scale.

The Nicks Edit, Premiere caption animation (495k views, https://www.youtube.com/watch?v=ymjkifj0Y5g)
- SF Pro Display Bold, centered, lower third, size about 100 on a 1080 frame, built-in shadow OFF.
- Hierarchy: the emphasized word is 200 to 250 percent, supporting words 70 percent, placed above and below it.
- Long Shadow effect with alpha falloff 100 percent on emphasized words only.
- In: Gaussian blur 50 to 100 down to 0, position slides up (or in from the left), opacity 0 to 100, over 15 to 20 frames (500 to 650 ms), ease in and out with a bezier curve.
- Finishing move: a black solid masked to the bottom third with feather 200 to 300, under the footage, so captions sit on a dark gradient.

Patrik Key, viral captions in CapCut (325k views, https://www.youtube.com/watch?v=l9JlsmzQs7Y)
- Guides: a horizontal line "under the chin" is the caption baseline; turn on the Instagram UI preview so nothing hides behind the buttons.
- Mix two or three fonts (thin, modern, one unusual). Allowed animation presets: slide up or down, blur, fade, wave in, zoom in, open, inhale. Fade in 0.2 s, slide up 0.6 s, blur out. Extend the layer past the last word so the out-animation has room and there is no gap.
- Gradient text (duplicate layer, split mask, feather) and a feathered black band as an extra layer behind the words.

Aeovisuals, viral captions in CapCut (232k views, https://www.youtube.com/watch?v=oUU1Lj7hcNU)
- "You need Montserrat, Poppins, Helvetica or Arial; any other font will not look right." Letter spacing -1.
- In: position from below to rest in ONE frame of keyframes then quad ease with the handle dragged to the start; opacity 0 to 100. Shadow opacity 26 percent, blur 26 percent.
- Out: fade out. Emphasis: color keyframe to a red, caps, bigger.

Chriss Boustedt, minimal text in Premiere (513k views, https://www.youtube.com/watch?v=wyKHkM0MXFg)
- Montserrat, Franklin Gothic Heavy or Open Sauce Sans Black. Shadow feathered way out and low opacity. Letter spacing -40 (Premiere units). Zero gap between captions. Single line, few characters per line.
- Position changes per scene (above the head, or centered). "Staircase" the words: each word layer starts slightly after the previous, all share one slide-up preset (opacity from 25 to 30 percent, not 0, position from below, bezier velocity ramp, motion blur on).
- Second look: Gaussian blur 6 to 15 on the text itself for a soft reveal. Flicker-out via random opacity keyframes.

Zeven 7, minimal reel edits in CapCut (889k views, https://www.youtube.com/watch?v=MJHpo7pOaLg)
- SF Pro Display Bold main word, dark grey on white, supporting words smaller, placed around it. Typewriter ("type one/two") for small text. Blur 20 to 0 over about 20 frames on the whole composition. Cubic ease on scale.

Shared grammar across all six: medium or bold geometric sans, tight tracking, no stroke, a soft low-opacity shadow, position from below plus opacity with an ease-out, optional blur-in, one accent word per group, and a dark gradient under the text when the footage is bright.

## 2. What 2026 "premium" looks like (web)

- The thick-stroke neon-highlight Hormozi look is called dated. The successor is "dynamic minimalism": clean sans (SF, Roboto), white text, subtle shadow, keyword in the creator's brand color, fades instead of hard pops, no emojis or flashing colors. https://joyspace.ai/hormozi-editing-style-2026-analysis
- Clipspeed's style ranking separates "Minimal" (clean sans, no fills or heavy effects, reads premium) from MrBeast or Hormozi (yellow and green color coding). https://www.clipspeed.ai/blog/11-caption-styles-ranked-viral-performance-2026.html and https://zellahq.com/blog/best-caption-styles-for-short-form-video/ (2 to 4 words on screen, middle 60 percent of the frame, one brand highlight color).
- Font lists: Montserrat Bold or SemiBold remains the default; Poppins, Inter, DM Sans, Archivo, Manrope, Figtree; Bebas Neue, Anton, Archivo Black for hooks; TikTok Sans is now free (OFL) and is what TikTok's native captions use. https://blitzcutai.com/blog/best-caption-fonts-tiktok , https://reelwords.ai/blog/best-fonts-for-captions , https://reloop.so/blog/article/best-fonts-for-subtitles/ , https://developers.tiktok.com/blog/tiktok-sans-open-source
- Rules repeated everywhere: 1 to 2 lines, 3 to 5 words per group, break lines by meaning, never a single orphan word, one accent color, white body text, 2 to 4 percent tracking when in all caps, tighter when mixed case. https://reelwords.ai/blog/best-fonts-for-captions , https://driveeditor.com/blog/text-overlays-in-short-videos
- Timing: 200 to 400 ms per word of display, entries under 200 ms, scale from 80 to 90 up to 100 with ease-out, optional 105 overshoot; pop only the words that matter. https://shortzly.com/blog/animated-captions-style-guide-short-form-video , https://makemoonshot.co/blog/kinetic-typography-captions
- Safe zone on 1080x1920. Meta's ad guidance is 14 percent top, 35 percent bottom, 6 percent sides (269 / 672 / 65 px). In-app Reels UI measured by vendors: top 220 to 250 px, bottom 400 to 420 px, right column 120 to 130 px. Recommended caption band Y = 850 to 1250. https://www.itnavideo.com/blog/where-to-put-subtitles-on-instagram-reels-safe-zone-guide , https://www.trymypost.com/blog/instagram-reels-safe-zones-2026 , https://filmscribe.ai/en/tools/instagram-reels-safe-zone
- Contrast: white text with a soft shadow is the safe default; a 20 to 45 percent dark gradient under the text zone beats a stroke for the premium look; a pill or box only for chaotic footage. Nicks Edit and Patrik Key both end with the feathered black band.

## 3. libass capability map (verified against Aegisub tag reference and local renders)

Reference: https://aegisub.org/docs/latest/ass_tags/ and https://github.com/libass/libass/wiki/ASS-File-Format-Guide

- Fade: \fad(in,out) in ms. Blur-in: \blur8\t(0,180,\blur0). Scale pop: \fscx92\fscy92\t(0,120,0.5,\fscx100\fscy100) where accel 0.5 = fast start then settle (ease-out). Slide-up: \move(x,y+18,x,y,0,160) (constant speed only; combine with \fad to hide the linearity).
- Shadow: \shad depth, \4c color, \4a alpha. Soft shadow is the catch: \blur blurs the border if \bord > 0, otherwise it blurs the glyph fill too (Aegisub \be note, confirmed in render: a \bord0\shad4\blur1.2 word looks slightly soft). Clean fix is two Dialogue lines: Layer 0 is the same text in black with \blur10 to 14, \alpha&H70& to &H80&, offset 3 px right and 6 px down; Layer 1 is the crisp text with \bord0\shad0. Rendered perfectly.
- Spacing: \fsp (style Spacing field) accepts negatives, so -1 to -2 at 66 px gives the tight look the tutorials dial in. Enable Kerning: yes in [Script Info]; libass disables kerning by default (libass Changelog).
- Alignment and position: \an5 for centered cards (scale pops from the center), \an2 for captions (pops from the bottom-center anchor), \an1 for lower-thirds. \pos sets the anchor.
- Karaoke: \kf sweeps secondary to primary per word; \k snaps. Both only move forward (spoken words stay primary), so "highlight the current word" needs one event per word with \1c on that word. That is also where per-word scale pops live. Rule: each accumulated event ends exactly when the next starts, or they overlap (that bug showed up in the first test).
- Backdrop band: a drawing event on Layer 0, {\pos(0,1060)\bord0\shad0\blur50\1a&H66&\p1}m -300 0 l 1380 0 l 1380 420 l -300 420{\p0}. With \bord0 the blur softens the fill, which is exactly what a band wants. Extend the shape past the frame edges or the sides fade too. \blur is capped at 100 in libass.
- Pill tag: BorderStyle 3 in the style line; OutlineColour becomes the box color and Outline becomes the padding. Rendered: tan pill with near-black text, and the inverse.
- Layers: higher Layer draws on top; \pos disables collision handling so stacked events never shove each other.
- Fonts: pass fontsdir to the subtitles filter and name the style's Fontname exactly as the font's family name ("Montserrat SemiBold", "Oswald Medium"). Use STATIC weight files: libass has no variable-font axis support (PR #792 still a draft, #579 abandoned, https://github.com/libass/libass/issues?q=variable+font), so a [wght].ttf renders at its default instance only. Add shaping=complex to the filter and keep the 4:4:4 trick in mind.
- Cannot do: real backdrop blur of the video (do it in ffmpeg: split, crop the band, boxblur or gblur, overlay, then subtitles), non-linear \move, per-character animation inside one event (emit one event per word or character), chroma-accurate thin gradients when burned to 4:2:0 (put format=yuv444p before subtitles then format=yuv420p after; libass issue https://github.com/libass/libass/issues/816). For gradient fills on text or anything libass cannot draw, render a PNG sequence with Pillow and overlay it.
- Gradient band in ffmpeg (verified): [0:v]split[a][b];[b]format=rgba,geq=r=0:g=0:b=0:a='clip((Y-1000)/600*255*0.45,0,255*0.45)'[g];[a][g]overlay=0:0:format=auto,format=yuv420p,subtitles=filename=reel.ass:fontsdir=fonts:shaping=complex. That darkens from Y 1000 to 1600 to 45 percent black, which is the Nicks Edit bottom-third fade without a mask layer.

## 4. Recommended El Coyote text system

Palette: white &H00FFFFFF (body), off-white &H00F2F2F2 (hook caps), Coyote tan &H008CB3C9 (= #c9b38c, the only accent), near-black &H00141414 (pill text), oxblood &H001F1F7A (= #7a1f1f, end card and rules only, never for words on footage). ASS colors are &HAABBGGRR.

Header for every file:
[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
LayoutResX: 1080
LayoutResY: 1920
WrapStyle: 0
ScaledBorderAndShadow: yes
Kerning: yes

Style lines (Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding):

Style: Hook,Oswald Bold,112,&H00F2F2F2,&H00F2F2F2,&H00000000,&H00000000,0,0,0,0,100,100,2,0,1,0,0,5,90,90,0,1
Style: HookShadow,Oswald Bold,112,&H00000000,&H00000000,&H00000000,&H00000000,0,0,0,0,100,100,2,0,1,0,0,5,90,90,0,1
Style: HookAlt,Montserrat ExtraBold,96,&H00F2F2F2,&H00F2F2F2,&H00000000,&H00000000,0,0,0,0,100,100,-2,0,1,0,0,5,90,90,0,1
Style: Cap,Montserrat SemiBold,66,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,-1,0,1,0,0,2,90,90,680,1
Style: CapShadow,Montserrat SemiBold,66,&H00000000,&H00000000,&H00000000,&H00000000,0,0,0,0,100,100,-1,0,1,0,0,2,90,90,680,1
Style: Label,Oswald Medium,40,&H008CB3C9,&H008CB3C9,&H00000000,&H00000000,0,0,0,0,100,100,5,0,1,0,0,1,72,72,0,1
Style: LabelSub,Montserrat SemiBold,34,&H00E6E6E6,&H00E6E6E6,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,1,72,72,0,1
Style: Tag,Oswald Medium,38,&H00141414,&H00141414,&H008CB3C9,&H008CB3C9,0,0,0,0,100,100,4,0,3,14,0,1,72,72,0,1
Style: Serif,Instrument Serif,120,&H008CB3C9,&H008CB3C9,&H00000000,&H00000000,0,-1,0,0,100,100,0,0,1,0,0,5,90,90,0,1
Style: Band,Arial,20,&H00000000,&H00000000,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1

A. Hook card (first 0.5 to 3 s). Oswald Bold 112 px all caps, tracking +2, two or three lines, centered at (540,760), which is the upper-middle of the frame where the eye lands and well clear of the top UI. One word in tan. Soft shadow layer, 120 ms fade, 140 ms scale pop from 94, optional blur-in. HookAlt (Montserrat ExtraBold 96, tracking -2) is the same card in the brand's heavier voice; use it when the hook is a question. Tested, both read on busy color bars.
Dialogue: 0,0:00:00.00,0:00:03.00,HookShadow,,0,0,0,,{\pos(543,766)\blur14\alpha&H70&\fad(120,120)\fscx94\fscy94\t(0,140,0.6,\fscx100\fscy100)}I TRADED MY HARLEY\NFOR THIS {\1c&H8CB3C9&}TRUCK
Dialogue: 1,0:00:00.00,0:00:03.00,Hook,,0,0,0,,{\pos(540,760)\fad(120,120)\blur6\t(0,160,\blur0)\fscx94\fscy94\t(0,140,0.6,\fscx100\fscy100)}I TRADED MY HARLEY\NFOR THIS {\1c&H8CB3C9&}TRUCK

B. Dialogue caption (talking, voiceover). Montserrat SemiBold 66 px mixed case, tracking -1, no stroke, centered with the bottom of the text at Y 1240 (MarginV 680), one line, max 2 when forced. At 66 px about 23 px per character, so 900 px of width holds about 38 characters; cap groups at 4 words or 28 characters. Each group is a set of accumulating per-word events: the current word is tan, previous words white, next words not yet shown; the first event of the group pops from 92 with a 50 ms fade, the last event fades out 80 ms. A shadow twin on Layer 0 spans the whole group. The band or gradient goes under it whenever the footage behind Y 1100 to 1350 is bright.
Dialogue: 0,0:00:03.00,0:00:06.00,CapShadow,,0,0,0,,{\pos(543,1246)\blur10\alpha&H80&\fad(50,80)}the whole frame is coming off
Dialogue: 1,0:00:03.00,0:00:03.40,Cap,,0,0,0,,{\pos(540,1240)\fad(50,0)\fscx92\fscy92\t(0,120,0.5,\fscx100\fscy100)}{\1c&H8CB3C9&}the
Dialogue: 1,0:00:03.40,0:00:03.90,Cap,,0,0,0,,{\pos(540,1240)}the {\1c&H8CB3C9&}whole
Dialogue: 1,0:00:03.90,0:00:04.50,Cap,,0,0,0,,{\pos(540,1240)}the whole {\1c&H8CB3C9&}frame
Dialogue: 1,0:00:04.50,0:00:04.90,Cap,,0,0,0,,{\pos(540,1240)}the whole frame {\1c&H8CB3C9&}is
Dialogue: 1,0:00:04.90,0:00:05.50,Cap,,0,0,0,,{\pos(540,1240)}the whole frame is {\1c&H8CB3C9&}coming
Dialogue: 1,0:00:05.50,0:00:06.00,Cap,,0,0,0,,{\pos(540,1240)\fad(0,80)}the whole frame is coming {\1c&H8CB3C9&}off
Variant for music-driven or lyric reels: a single \kf event (secondary &H00B4B4B4 grey for unspoken words) gives the smooth left-to-right reveal; only use it over dark footage because dim grey dies on bright backgrounds (seen in the test).

C. Label / lower-third (part names, specs, partner tags). Oswald Medium 40 px caps in tan, tracking +5, left aligned at x 72, baseline Y 1400, a 56 x 4 px tan rule under it, then LabelSub Montserrat SemiBold 34 px off-white. Left side is UI-safe (the right column is the button stack). For a stronger tag use the Tag style pill: BorderStyle 3, tan box, near-black text, 14 px padding.
Dialogue: 1,0:00:12.00,0:00:15.00,Label,,0,0,0,,{\pos(72,1400)\fad(120,120)}PROJECT RIVAL
Dialogue: 1,0:00:12.00,0:00:15.00,Band,,0,0,0,,{\pos(72,1412)\bord0\shad0\1c&H8CB3C9&\1a&H00&\p1\fad(120,120)}m 0 0 l 56 0 l 56 4 l 0 4{\p0}
Dialogue: 1,0:00:12.00,0:00:15.00,LabelSub,,0,0,0,,{\pos(72,1460)\fad(120,120)}1959 F600  ·  7.3 Powerstroke
Dialogue: 1,0:00:06.00,0:00:09.00,Tag,,0,0,0,,{\pos(72,1380)\fad(120,120)}DRIVEN DIESEL

D. End card (last 1.5 to 2.5 s). Full-frame black at 80 to 90 percent or the oxblood solid (flat, no sheen), "EL COYOTE" in Oswald Bold 112 tan at (540,880), the handle in Montserrat SemiBold 48 white at (540,1000), and the Serif style (Instrument Serif Italic 120, tan) for a one-line sign-off such as "built, not bought" at (540,700) with \fad(200,200)\blur0.4. The serif beat is the one classy accent; it never carries dialogue.

Backdrop band event (Layer 0, under any caption group over bright footage):
Dialogue: 0,0:00:03.00,0:00:06.00,Band,,0,0,0,,{\pos(0,1060)\bord0\shad0\blur50\1a&H66&\p1}m -300 0 l 1380 0 l 1380 420 l -300 420{\p0}

Automation rules from words.json: split groups on a gap over 350 ms, on sentence punctuation, or at 4 words / 28 characters, whichever comes first; merge a trailing 1-word group into the previous one; a group displays until the next group starts (no gaps); minimum 700 ms per group; start each word 40 ms before the Whisper onset; pop only the first word of the group plus any word flagged as emphasis (numbers, part names, the payoff word), everything else just changes color. Pick Hook vs HookAlt per reel, never both. One accent color per reel. Switch between band, gradient, or nothing by measuring the mean luma of the caption zone in the frame grabs (over 0.55 means use the band).

## 5. Free font downloads (static weights, libass-safe)

- Montserrat SemiBold / Bold / ExtraBold: https://raw.githubusercontent.com/JulietaUla/Montserrat/master/fonts/ttf/Montserrat-SemiBold.ttf (swap the weight name; all three verified 200)
- Oswald Medium / SemiBold / Bold: https://raw.githubusercontent.com/googlefonts/OswaldFont/main/fonts/ttf/Oswald-Medium.ttf (verified)
- Instrument Serif Regular and Italic: https://raw.githubusercontent.com/google/fonts/main/ofl/instrumentserif/InstrumentSerif-Italic.ttf (verified)
- Poppins SemiBold / Bold: https://raw.githubusercontent.com/google/fonts/main/ofl/poppins/Poppins-SemiBold.ttf (verified)
- Bebas Neue: https://raw.githubusercontent.com/google/fonts/main/ofl/bebasneue/BebasNeue-Regular.ttf ; Anton: https://raw.githubusercontent.com/google/fonts/main/ofl/anton/Anton-Regular.ttf ; Archivo Black: https://raw.githubusercontent.com/google/fonts/main/ofl/archivoblack/ArchivoBlack-Regular.ttf ; Barlow Semi Condensed SemiBold: https://raw.githubusercontent.com/google/fonts/main/ofl/barlowsemicondensed/BarlowSemiCondensed-SemiBold.ttf (all verified)
- Inter 4.1 (zip contains static TTFs): https://github.com/rsms/inter/releases/download/v4.1/Inter-4.1.zip
- DM Sans, Big Shoulders Display, TikTok Sans, Space Grotesk, Figtree, Archivo: the google/fonts repo only carries variable files, so use the Google Fonts zip (contains a static folder) e.g. https://fonts.google.com/download?family=DM+Sans , https://fonts.google.com/download?family=Big+Shoulders+Display , https://fonts.google.com/download?family=TikTok+Sans , https://fonts.google.com/download?family=Space+Grotesk (all return 200)
- Satoshi (Fontshare, ITF Free Font License: free personal and commercial use, no redistribution or modification): https://api.fontshare.com/v2/fonts/download/satoshi
- The variable files (Montserrat[wght].ttf etc.) render at one default weight in libass. Do not point fontsdir at them.

## 6. What to avoid

- Thick black strokes (the 7 px outline of attempt one) and neon green or yellow keyword fills: the dated Hormozi signature.
- Blurring the glyph itself by accident (\blur with \bord0 on the text layer). Blur the shadow twin or the band instead.
- Impact, Arial Black, Bahnschrift, Segoe UI, Playfair Display for captions: they read as defaults or as a wedding invite. Playfair stays off Reels captions; Instrument Serif Italic replaces it for the one serif beat.
- Variable font files in fontsdir.
- Full sentences, more than two lines, orphan single-word lines, gaps between groups, captions below Y 1500 or inside the right 130 px.
- More than one accent color, drop shadows with hard edges, glossy or metallic text, gradient fills on text (chroma striping when burned to 4:2:0 and off-brand anyway).
- Hard linear \move slides without a fade; pops on every word; animation longer than 200 ms on captions or 300 ms on hooks.
- Grey "unspoken word" karaoke over bright footage.

## 7. Top 5, in order

1. Replace the single-event outline look with the two-layer shadow system (CapShadow + Cap, HookShadow + Hook) and tracking -1 / +2. This alone is the gap between attempt two and "paid editor".
2. Generate accumulating per-word events from words.json with the current word in Coyote tan, a 120 ms ease-out pop on the first word only, zero gaps, groups of 4 words or 28 characters.
3. Add the luma check and auto-insert the blurred \p1 band (or the geq gradient) under caption groups over bright footage; never add a stroke to fix contrast.
4. Download Oswald Medium and Instrument Serif Italic into tools\fonts and build the Label, Tag (pill) and end-card Serif styles so part names and partner tags stop living in the caption style.
5. Move the hook to Oswald Bold 112 (or Montserrat ExtraBold 96 for questions) centered at Y 760 with blur-in plus scale pop, tan on one word, and keep Hook and HookAlt as the only two display treatments.

Test artifacts (scratch, may be cleared): C:\Users\Parts\AppData\Local\Temp\claude\ec5c0be963e5d034\cf397af3-c62e-4e28-90bd-4c7642d0dc8c\scratchpad\typo\test.ass, test2.ass, out\sheet.png, out\sheet2.png.
