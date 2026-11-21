# 03. Tool inventory: the reel-editing toolchain (surveyed 2026-11-21)

Read-only survey of the live folder `C:\Users\Parts\OneDrive - Elite Diesel Service\Desktop\VIDEO\tools` (called TOOLS below), its snapshot `research/tools-snapshot`, the `reel-editor` skill and the four editing memories. Every script's docstring, argparse block and README was read; component signatures were read, not component bodies. Byte-compared live vs snapshot: all 14 scripts, 5 READMEs and the whole `rival-reels/src` tree are identical. The skill file is identical to the snapshot copy.

## 0. Interpreters, binaries, paths (every tool assumes these)

| thing | path | note |
|---|---|---|
| system Python | `%LOCALAPPDATA%\Programs\Python\Python312\python.exe` (3.12.10), always with `-I` | bare `python` hits the Store alias and fails; faster-whisper lives here, `av==14.2.0` pinned, do not upgrade |
| ffmpeg / ffprobe 9.0.2 | `%LOCALAPPDATA%\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin\` | not on PATH; every script hardcodes this |
| scenedetect.exe | `...\Python312\Scripts\scenedetect.exe` | used by watch.py |
| yt-dlp | `%LOCALAPPDATA%\Microsoft\WinGet\Packages\yt-dlp.yt-dlp_Microsoft.Winget.Source_8wekyb3d8bbwe\yt-dlp.exe` | watchlist + reference pulls; `winget upgrade yt-dlp` when TikTok lists come back empty |
| Node 24 + Remotion 4.0.545 | `TOOLS\rival-reels` (`npx remotion ...` from inside it) | chrome headless shell under node_modules/.remotion; `remotion.config.ts` sets jpeg frames, concurrency 8, angle GL |
| venv-voice | `TOOLS\venv-voice` | kokoro-onnx 0.6.1 + onnxruntime + soundfile; only vo_scratch spawns it |
| venv-sfx | `TOOLS\venv-sfx` | Earshot package (`venv-sfx\Scripts\python.exe -I -m earshot ...`), used only to render custom sounds |
| venv-artboard | `TOOLS\venv-artboard` | Pillow only; artboard.py re-launches itself here when Pillow is missing |
| models | `TOOLS\models\` | `face_detection_yunet_2023mar.onnx` (facetrack, dfc_track), `rvm_mobilenetv3_fp32.onnx` (matte), `kokoro\kokoro-v1.0.onnx` + `voices-v1.0.bin` (vo_scratch), `bd.rnnn` + `sh.rnnn` (rnnoise, NOT referenced by any script) |
| bin | `TOOLS\bin\` | `rife-ncnn-vulkan-20221029-windows`, `esrgan` (Real-ESRGAN ncnn). NOT referenced by any script; dormant |
| fonts | `TOOLS\fonts\` (26 ttf) | ASS `fontsdir` for build_reel2/3. Anton, Archivo Black, Bebas, Caveat Brush, Chango, Bagel Fat One, DM Serif Display/Text, Instrument Serif Regular+Italic, Kaushan Script, Montserrat Bold/ExtraBold/SemiBold, Oswald Bold/Medium, Playfair Display VF, Poppins Light/Medium/Italic/MediumItalic/SemiBold/SemiBoldItalic, Rubik Bubbles, Shrikhand, Yellowtail |
| Drive (mirror mode) | `C:\Users\Parts\My Drive\VIDEO\inbox\` raw clips loose; DFC work in `My Drive\VIDEO\DFC\` | G: is only a shortcut; use the C: path. `My Drive\VIDEO\out` exists but is empty and unused |
| OneDrive work area | `...\Desktop\VIDEO\out\` EDLs, gen scripts, `out\renders\` (plates, finals, `.cache-<name>` slot caches), `out\project-files\<folder>\`, `out\dfc\` | nothing here goes to the Drive |
| finished reel folder | `My Drive\VIDEO\inbox\<Name> - completed YYYY-MM-DD\` (DFC: `My Drive\VIDEO\DFC\<Name> - completed YYYY-MM-DD\`) | only POST THIS mp4, no-captions mp4, `README - posting kit.txt` (+ since 11-21 the handoff set: `-EDIT.mp4` crf 14, `.srt`, `-cutout.webm`, `ov-*.png`, `-graphics.webm`, cover still). No raw-clip subfolders, no Unused folders |

## 1. Tool tables

### watch.py (plain python, system)
| | |
|---|---|
| purpose | "let Claude watch it": scene list, one jpg per shot, contact sheets with burned timestamps, Whisper transcript + word timestamps |
| usage | `python -I watch.py <video> [--out DIR] [--model small\|medium] [--no-whisper] [--fps N]` (add `-W ignore`) |
| inputs | any video (iPhone HLG MOV, Sony MP4, yt-dlp pulls) |
| outputs | `<out>/<clipname>/info.txt, scenes.csv, shots/shot-NNN.jpg, sheet-NN.jpg (5x4 tiles, ~60 max), transcript.txt, words.json` (`[{"w":" word","s":0.46,"e":0.80}]`) |
| gotchas | default out = `VIDEO/out/<clip>`; `--model medium` for exact lines (small misheard the Harley line); for one line cut a 16 kHz mono wav and re-run medium; sets HF_HUB_DISABLE_SYMLINKS_WARNING; CPU ~4x realtime |

### build_reel.py (plain python) LEGACY v1
| | |
|---|---|
| purpose | lyric-caption montage renderer (Playfair yellow drawtext, hard cuts) used for the first Rival lyric reel |
| usage | `python -I build_reel.py edl.json` |
| inputs | EDL `{out_dir,name,size,fps,font,font_size,font_color,guide_audio,slots:[{clip,in,dur,caption,cap_from}]}` |
| outputs | `<name>-SILENT.mp4` (post, add song in IG), `<name>-GUIDE.mp4`, contact sheet |
| gotchas | no HDR tone map, no audio pipeline; only still valid for the lyric format (addendum rule 47: Playfair 92 px yellow stays for lyric reels only). Live folder only, not in snapshot, not in skill |

### build_reel2.py (plain python) FALLBACK v2
| | |
|---|---|
| purpose | second renderer: xfade transitions, minterpolate slow-mo, crop zoom, vidstab, karaoke ASS captions, real audio beds, HDR probe + libplacebo tone map |
| usage | `python -I build_reel2.py edl.json [--captions-only]` |
| inputs | EDL with `slots[{clip,in,dur,speed,zoom,stab,xfade{type,dur},grade}]`, `audio[{clip,in,dur,at,gain_db}]`, `loudnorm`, `captions[{style Hook/Cap/Sub/Small,text\|words,start,end,pos}]`, `fontsdir` |
| outputs | `<name>.mp4`, `<name>-NOCAP.mp4`, `<name>.ass`, `<name>-sheet.jpg` |
| gotchas | GRADES warm/punch exist but Jacob rejected grades: leave off. Seven ffmpeg gotchas in memory (settb=AVTB after xfade, setsar=1, aresample after loudnorm, anullsrc base for amix, vidstab relative paths, map `[i:a:0]` on iPhone MOVs, font raw links) |

### build_reel3.py (plain python) CURRENT fast-tier renderer, RENDER_VERSION "3.4-mblur-n"
| | |
|---|---|
| purpose | playbook edition: per-clip HDR probe + HLG tone map + bt709 tags, eased punch-ins (scale eval=frame), speed ramps, whip pans, shake, flash, vidstab, `mblur`, landscape `crop_x`, voice beds with crossfaded joins + cleanup chain, ambience bed ducked under voice, synthesized sfx hooks, ASS caption system, lint, IG export recipe, slot cache |
| usage | `python -I build_reel3.py edl.json [--captions-only]` (captions-only re-burns onto the existing `<name>-NOCAP.mp4` in ~20 s) |
| EDL top level | `name, out_dir, fontsdir, sfxdir, fps (24 allowed), size ([1080,1920] or shorter plate), ambience{clip,in,gain_db}, audio_xfade (0.08), fontmap, slots, audio, sfx, captions` |
| slot keys (from code) | `clip in dur speed ramp[[t,speed]] zoom[a,b] zoom_anchor zoom_ease(inout\|out) stab shake[beats] flash[t] xfade{type fade\|whip_left\|whip_right\|wipe_left,dur} mblur(true\|2\|3) grade(natural\|none) crop_x(0..1 or [x0,x1]) crop_move` |
| audio bed keys | `clip in dur at gain_db clean(true\|"light") fade xfade`; beds sorted by `at`, consecutive beds crossfade (qsin, 80 ms, reads up to 120 ms past the trim), cleanup chain runs once on the mixed voice |
| sfx keys | `kind whoosh\|impact\|riser\|sub\|click\|gap, at, gain_db, file` (`file` wins, else synthesized `tools/sfx/<kind>.wav`; `notify` has no file and is skipped) |
| caption types | `hook{text,accent,start,end,pos,caps}`, `words{words[[w,t]],end,pos,band,show_ahead}`, `cap{text,accent,start,end,pos,band,pop}`, `label{title,sub,pos}`, `tag{text,pos}`, `small{text,pos}`, `serif{text,pos}`, `lockup{script,block,sub,pos,script_dy,block_dy,sub_dy}` (default LOUDER: Kaushan 190 yellow over Anton 380 white + Poppins 46 sub), `lockup preset:"megante"{block,echo,labels,sub}`, `lockup preset:"tropi"{block,sub}` |
| outputs | `out_dir/<name>-NOCAP.mp4` (the plate), `<name>.mp4`, `<name>.ass`, `<name>-sheet.jpg`, `.cache-<name>/` per-slot renders; prints `tags: yuv420p,tv,bt709,bt709,bt709 OK` |
| lint | FAIL (exit 2): no hook caption, hook > 7 words, hook starts after 0.14 s. WARN: slot > 4 s static, > 3 s with no motion, no end line in last 0.6 s, > 60 s |
| export | 1080x1920 30 fps libx264 slow crf 17 maxrate 16M bufsize 32M High 4.2 closed 1 s GOP aq-mode 3, unsharp + deband + grain, AAC 192k, faststart, bt709 tags |
| gotchas | ffmpeg 9 filter file flag is `-/filter_complex`; crop w/h do not animate, use scale eval=frame + crop; ffprobe csv tag order pix_fmt,range,space,transfer,primaries; bump RENDER_VERSION when slot filters change; `fps: 24` for Sony plates (conforming to 30 duplicates frames) and the Remotion comp must then take `fps: 24` from props; mblur ~1 s per frame; `sfx` block is OFF by house rule when a song goes on in IG; the hook/words/cap ASS styles are the legacy Oswald/Montserrat system, the lockup types are the live ones; `.bak-2026-11-21` next to it is the pre-crossfade copy |

### smooth_check.py (plain python)
| | |
|---|---|
| purpose | frame-pacing QA: constant fps, held frames away from cuts, skipped-frame spikes, cut list, per-shot strobe score |
| usage | `python -I tools/smooth_check.py <reel.mp4> [more.mp4 ...]` |
| outputs | stdout only; "<- fast motion: use mblur on this slot" when a shot's motion/frame > 3.5 |
| gotchas | run before EVERY delivery; it cannot see a bad crop (eyeball the sheet); single held frames in a static interview are the subject holding still; smooth handheld drift is not choppiness |

### facetrack.py (plain python, cv2)
| | |
|---|---|
| purpose | YuNet single-face track of a talking-head plate (biggest face = Jacob) |
| usage | `python -I tools/facetrack.py <plate.mp4> <out.face.json> [--hz 10]` |
| outputs | `[[t,x,y,w,h],...]` plate pixels, null box when no face; the format layout.py reads |
| gotchas | OpenCV 5.1 has no CascadeClassifier, YuNet only; detects at half res, ~215 fps |

### matte.py (plain python, onnxruntime CPU)
| | |
|---|---|
| purpose | Robust Video Matting person cutout as VP9 WebM with alpha, so overlays flagged `behind: true` sit behind Jacob |
| usage | `python -I matte.py <plate.mp4> <out.webm> [--ds 0.25]` |
| outputs | `public/cutout.webm` (yuva420p, crf 24) |
| gotchas | ~11 fps for 1080x1920 on CPU; alpha is lumpy at the cap (open item: morphological close); RivalReel only draws the cutout layer when at least one overlay is `behind` |

### layout.py (plain python, import module)
| | |
|---|---|
| purpose | face-aware placement from a face track: `caption_ys(track, windows)` two fixed bands (1230 below chin / 400 above) with hysteresis, `caption_y`, `caption_band`, `card_zone(track,t0,t1,card_h)` -> (y, "below"\|"above"\|"low" 1330), `face_box` |
| usage | `import layout` from gen scripts (sys.path.insert tools); `python -I layout.py face.json` prints a sample |
| constants | IG_TOP 290, IG_BOTTOM_TEXT 1440, PILL_H 90 |

### dfc_track.py (plain python, cv2)
| | |
|---|---|
| purpose | multi-face track (up to 3) + mouth-motion active-speaker guess on a LANDSCAPE interview, for 9:16 reframing |
| usage | `python -I dfc_track.py <video> <out.json> [--hz 10] [--t0 S] [--t1 S]` |
| outputs | `{"hz": true_rate, "hz_requested", "w", "h", "samples":[{"t","faces":[[x,y,w,h,mouth_motion]],"speaker":i\|null}]}` |
| gotchas | tracker steps whole frames so 23.976/2 = 11.99 Hz, not 10: look samples up by timestamp, never by t*hz (7 of 18 reels framed the wrong thing once); consumer must drop faces under 100 px and reject a lone face far from the side's last position |

### vo_scratch.py (system python, spawns venv-voice)
| | |
|---|---|
| purpose | Kokoro SCRATCH voice for timing a script + words.json + pacing report. Timing only, never shipped |
| usage | `python -I vo_scratch.py script.txt out_dir [--voice am_michael] [--speed 1.1] [--takes 2] [--whisper-model small] [--keep-takes]` |
| inputs | script.txt one spoken beat per line (blank and `#` lines skipped, line 1 = hook) |
| outputs | `vo.wav` (48k stereo, ~-16 LUFS), `vo_raw_24k.wav`, `words.json` (watch.py shape, aligned to the script's own spelling), `lines.json`, `report.txt` (wpm, hook check, flags), `takes/` |
| gotchas | targets 150 to 165 wpm, 15-word hook inside 5 s, under 18 s; Kokoro at 1.06 is ~155 wpm so Jacob's read runs longer, cut words; respell odd words ("iss pro"); never pip install into system Python for it; launching from the venv hops back to system Python |

### words_to_props.py (plain python)
| | |
|---|---|
| purpose | generator layer: spec (items + cue words) + words.json -> Remotion props (CardReel or RivalReel) + `.sfx.json`; prints a plan table; lints and refuses to write |
| usage | `python -I words_to_props.py specs\<name>.json <words.json> rival-reels\out\<name>.props.json` |
| inputs | spec (schema in `specs/menu-reel-example.json` `_schema` block and section 5 below); words.json from watch.py or vo_scratch |
| outputs | `<out>.props.json`, `<out>.sfx.json` (`[{at,kind,gain_db,kit,file?}]`, kinds whoosh/pop/stamp/tick/notify) |
| timing constants (code) | LEAD 0.12, OLD_GAP 0.50, HOLD 1.60, IRIS_LEAD 0.40, IRIS_DUR 0.70, CAPTION_GAP 0.55, captions 2 to 4 words / 24 chars, MIN_WINDOW 1.2, MAX_OVERLAP 0.3, TEXT_FLOOR 1440, Y_HUD 300, Y_HEADLINE 440, Y_STRIKE 620, Y_CARD 660, Y_CARD_UNDER_STRIKE 780, Y_GATE 660, Y_GHOST 1000 |
| lint | cue not found, cards overlap > 0.3 s, hook > 7 words, text below 1440, window < 1.2 s or card < 0.6 s, card bottom hits caption line |
| gotchas | README layout numbers (strike 540, card 560/700, captions 2 to 5 words / 28 chars) are STALE; the code moved to 620/660/780 and 2 to 4 / 24 after the dry-run critique. `stickerCue` near a window end gives the sticker a few frames. `gate` only on comment-gated deliverable reels |

### sfx_place.py (plain python, numpy)
| | |
|---|---|
| purpose | place CC0 kit sounds frame-accurately into one 48 kHz stereo 24-bit wav + placement table |
| usage | `python -I sfx_place.py events.json --kit sfx-kit --out sfx_track.wav [--fps 30] [--duration S] [--cuts N] [--style gritty\|neutral\|clean\|any] [--mixed] [--placement placement.txt] [--seed 0] [--voice voice.wav]` |
| inputs | events `[{at,kind,gain_db?,file?,variant?}]` (also `{events:[...]}`, `{sfx:[...]}`, `t`/`time`, `type`) |
| anchors | whoosh peak 2 frames before `at`; hit/stamp peak on `at`; riser ends 2 frames before `at`; pop/tick/click/notify onset on `at` |
| guards | one style per reel (gritty vs clean, refused unless `--mixed`), density (> 1 whoosh per 4 cuts, > 3 sounds in 1 s), clip (scaled under -1 dBFS) |
| outputs | the wav + `placement.txt`; `--voice` prints the exact ffmpeg mix line (sfx bus so the -7 dBFS stamp sits 6 dB under the voice peak, loudnorm I=-14 TP=-1.5 last) |
| gotchas | riser-into-hit wants a hit whose attack is under 2 frames (es_thud_diesel, hit_bong_low, not hit_deep_drop); single-pass loudnorm undershoots on short material, do two-pass on finals |

### sfx_lint.py (plain python, numpy)
| | |
|---|---|
| purpose | independent re-measure of a rendered sfx track against the events; deltas in frames; exit 1 past tolerance |
| usage | `python -I sfx_lint.py events.json sfx_track.wav [--fps 30] [--tol 0.5] [--window 6]` |
| gotchas | 48 kHz wav only; not in the skill (SFX-README only) |

### artboard.py (any python, re-launches in venv-artboard for Pillow)
| | |
|---|---|
| purpose | artboard-before-render: renders only the planned frames (frame 4, each overlay `at` + 0.5 s, last) in one image-sequence pass, labels + 480/1440 safe lines, one contact sheet + lint md |
| usage | `python -I artboard.py <props.json> [--comp CardReel\|RivalReel] [--out dir] [--cols 6] [--max 24] [--extra 0.5] [--tile 320] [--kit dir] [--keep] [--no-pil]` |
| outputs | `<name>-artboard.png`, `<name>-artboard.md` next to the props |
| lint | text below 1440, > 1 hook element on frame 4, overlapping cards, overlay type not in REG, overlay past CardReel end (heights are estimates) |
| gotchas | ~0.7 s per frame, 23 tiles ~20 s; `--comp` auto = RivalReel when props have `plate`; Jacob redlines by tile number, "approved" is the green light; its DEFAULT_Y table must be kept in step with component defaults by hand |

### outlier_watchlist.py (plain python, no packages) GROWTH tool
| | |
|---|---|
| purpose | weekly outlier scan of 40 diesel/7.3/OBS/shop/meme/partner accounts on TikTok + YouTube Shorts mirrors via yt-dlp flat listings; outlier = views / account median |
| usage | `python -I outlier_watchlist.py [--watchlist watchlist\watchlist.json] [--out watchlist] [--limit 60] [--min-outlier 5] [--date YYYY-MM-DD] [--pause 2,4] [--no-enrich] [--only h1,h2]` |
| outputs | `watchlist\<date>-posts.csv, -medians.csv, -outliers.md, -log.txt` (+ copy of watchlist.json) |
| gotchas | Instagram not fetched (login-walled); TikTok share % is roughly 2/3 of an IG sends figure; YouTube listing gives views only, enrichment per outlier; all metadata treated as untrusted; Monday run ~15 min, then hand-fill Format/Subtopic from `research/2026-11-21-OUTLIER-MATRIX.md` |

### Non-script contents of TOOLS
| item | what | status |
|---|---|---|
| `sfx/` | OLD synthesized kit (click, impact, riser, sub, whoosh) made by build_reel3 `ensure_sfx` | not shippable, reference only; still the fallback build_reel3 plays for `.sfx.json` stand-ins |
| `sfx-kit/` | 16 CC0 wavs + `earshot/` 4 renders, `kit.json`, `KIT.md`, `build_kit.py`, `downloads/` (data only, never run), `test/` | the shippable kit |
| `earshot/` | clone of Leonxlnx/earshot v1.0.0 (82 MB) | data only; the package is installed in venv-sfx |
| `specs/` | `menu-reel-example.json` (annotated schema + 3-item Rival example), `nxtlvl-recreate.json` (9-item test), `stock-parts.json` (9-item dry run, `captionY` 1180) | |
| `voice-test/` | sample vo_scratch output (6 lines, 81 words, 32.7 s, 14 takes) | regenerate any time |
| `watchlist/` | `watchlist.json` (40 accounts, window_posts 60) + 2026-11-21 run outputs | |
| `__pycache__/` | build_reel3 + layout pyc | ignore |

## 2. Remotion kit: TOOLS\rival-reels

Deps: remotion, @remotion/cli, captions, fonts, media-utils, motion-blur, paths, transitions (all ^4.0.545), react 18.3. Entry `src/index.ts` -> `src/Root.tsx`.

### Compositions (src/Root.tsx)
| id | component | size / fps | duration | props |
|---|---|---|---|---|
| `RivalReel` | RivalReel | 1080x1920, fps from `props.fps` (default 30) | ffprobe of `public/<plate>` via calculateMetadata | `plate` (public path), `cutout?`, `captions?[]`, `overlays?[]`, `muted?` (true), `captionStyle?` pill\|plain (default pill; talking heads set plain), `fps?`, `frame?{top,h,bg,rule}` (title-band window; Jacob rejected bands, leave unset) |
| `CardReel` | CardReel | 1080x1920, fps from props | `durationSec * fps` | `bg?` ("#0b0b0c" \| "paper" \| still.png \| clip.mp4 blurred), `durationSec`, `fps?`, `overlays?`, `captions?`, `captionStyle?` (default plain), `grain?` (true) |
| `Cover` | Cover | 1080x1920, 1 frame | still | `src` (plate.mp4 or still), `atSec?`, `title` (3 to 4 words), `tag?` ("RIVAL · EP n"), `preset?` block\|megante\|louder, `script?`, `dim?` 0.22, `band?` (cream band, auto on megante) |

Overlay render contract: each overlay becomes `<Sequence from=at*fps dur=dur*fps>` and the component receives `plate, cutout, atF, dur (frames)` plus `...props`. RivalReel draws `behind` overlays, then the cutout (only if any behind), then front overlays, then captions. CardReel stacks in array order (no cutout). Captions: `style==="plain"` -> PlainCaption at `y ?? 1150`, else CaptionPill at `y ?? 1230`.

### Theme tokens (src/theme.ts)
`BRAND` = `REMOTION_BRAND=dfc` at bundle time, else coyote.
- COYOTE colors `C`: black #0b0b0c, ink #141414, cream #efe9dc, tan #c9b38c, oxblood #7a1f1f, oxbloodDeep #5a1515, yellow #f7d43c, white #ffffff, green #1f3a2d, hi #e2543e (caption highlight box).
- DFC colors: black #0A1226, ink #0F1A33, cream #F5EDD8, tan/yellow/hi #C8973A, oxblood #8B1A1A, oxbloodDeep #5a1010, green #1B2A4A.
- COYOTE fonts `F`: block Anton, script Kaushan Script, ui Poppins, uiLight Poppins Light, uiItalic Poppins Italic, uiSemi Poppins SemiBold, serif Instrument Serif (loaded from the Italic file), heavy Archivo Black.
- DFC fonts: block Oswald Bold, script Instrument Serif, ui/uiSemi Montserrat SemiBold, heavy Montserrat ExtraBold.
- `SAFE` = {top 290, bottom 1240, left 72, right 950}; `shadow`, `cardShadow` strings; `loadBrandFonts()` loads the 12 files in public/fonts.
- anim.ts: EASE_OUT, EASE_IN_OUT, prog, pop (spring d16 s170), popSoft (d12), tailFade, backOut(1.70158), expoOut, power4Out, power2In, steps(n), sf.

### Complete overlay-type table (REG in src/RivalReel.tsx, 64 keys)
Common to all: `at`, `dur` (seconds, in the overlay object); `behind: true` puts it under the cutout (RivalReel only). Props listed are the component's own, defaults in parentheses.

| type | component (file) | main props |
|---|---|---|
| kinetic | KineticHook (Text) | words[], y, size, accent, color, align center\|right\|left, pad |
| scriptblock | ScriptBlock (Text) | script, block, sub, y (520), tight |
| stamp | WordStamp (Text) | text, y, size, font, color, echo |
| numeral | Numeral (Text) | n, label, x (760), y (300) |
| titlecard | TitleCard (Text) | title, sub |
| logo | LogoCard (Cards) | src, label, x 120, y 330, w 840, tilt -3 |
| photo | PhotoCard (Cards) | src, caption, x 140, y 300, w 800, tilt 2 |
| spec | SpecCard (Cards) | title, rows[], x 90, y 320, w 900 |
| strike | StrikeList (Cards) | title, items[], x 110, y 340, w 860, strikeFrom 14 |
| browser | BrowserCard (Cards) | src, url, click{x,y,at}, x 60, y 300, w 960 |
| prompt | PromptBar (Cards) | text, label "TO CLAUDE", y 330, sentAt |
| comment | CommentDrop (Cards) | word, y 360, handle "you" |
| count | CountCard (Cards) | n, label, x 90, y 320 |
| plaincap | PlainCaption (Chandler) | text, accent, y 1150, size 68, hiColor, box, variant sans\|serif\|caps\|italic, accentFont serif\|script, ink |
| tooltag | ToolTag (Chandler) | icon, name, y (120), size, iconW, iconH, pill |
| outline | OutlineWord (Chandler) | text, y 400, size 360, stroke 5, color |
| pip | PipCard (Chandler) | src, keys[{at,x,y,w}], startFrom, radius, move, muted, aspect |
| slider | SliderReveal (Chandler) | after, filter, from, to, sweep, hold (uses plate + atF) |
| grid | GridWall (Chandler) | tiles[], gap, radius, shrink, every, bg (uses plate) |
| params | ParamPanel (Chandler) | title "TUNE", rows[{label,from,to,at,min,max,unit}], x 60, y 330, w 960 |
| storyboard | StoryboardCard (Chandler) | title, rows[[a,b,c,d]], x 50, y 300, w 980 |
| badge | LogoBadge (Brand) | src, x 790, y 300, size 170, opacity |
| lowerthird | LowerThird (Brand) | name, title, x 72, y 1300 |
| quote | QuoteBar (Brand) | text, y 330, size 76 |
| corners | CornerLogos (Brand) | left, right (public paths), h 118, margin 56, bottom 96, opacity, maxW 330 |
| hud | ProgressHud (Menu) | count, total, handle, y, variant dots\|bar\|tiles, progress, icons[], ink |
| sidebar | SidebarList (Menu) | items[], current, x, y, cols 1\|2, size, w, scroll |
| phone | PhoneStage (Menu) | count, total, x, y, w, src, bob, label |
| countup | CountUp (Menu) | to, from, prefix, suffix, start, len, size, color, x, y, label, font, group |
| strikestamp | StrikeStamp (Menu) | name, meta, icon, tag, stamp, strikeAt, x, y, w, stampColor |
| item | ItemCard (Menu) | title, sub, icon, count{to,prefix,suffix,label}, tag, chips[{text,at frames}], foot, sticker, stickerAt, x, y, w, ghost, shadow hard\|soft |
| headline | Headline (Menu) | text, accent, y 420, size 60, align |
| ghost | GhostWord (Menu) | text, y 500, size 330, color |
| iris | IrisWipe (Menu) | color oxblood, cx 540, cy 770, grow 9, hold |
| negflash | NegativeFlash (Menu) | frames 2, invert (uses cutout) |
| gate | CommentGate (Menu) | word, reply, items[], y, handle, typeAt, dmAt |
| quad | QuadWall (Menu) | panels[{src,atF}], gap, radius |
| checklist | Checklist (Menu) | title, rows[{text,at,doneAt}], x 72, y 420, w 936, reveal |
| wall | WallBehind (Effects) | tiles[], layout grid\|scatter, cols, tileW, stagger, dim, captions[], seed |
| masthead | Masthead (Effects) | text, y, size, font serif\|block\|heavy, color, lines[], border |
| framebreak | FrameBreak (Effects) | handle, scale, cy, shrink, aspect, muted (uses plate + cutout) |
| vertigo | Vertigo (Effects) | to, anchorY, muted (plate + cutout) |
| bgreplace | BgReplace (Effects) | bg, dim 0.25, blur, kenBurns (cutout) |
| chart | ChartGrow (Effects) | values[], labels[], x, y, w, h, label, drawFrames, color, dim |
| pullback | PullBackWindow (Effects) | title, rows[{text,at}], to, pull, muted (plate) |
| zoomthrough | ZoomThrough (Effects) | cutAt, peak, flash, nextAtF, next, ox, oy, samples (CameraMotionBlur) |
| hudzoom | HudZoom (Effects) | from 1.0, to 1.6, label "REC", color |
| beforeafter | BeforeAfter (Effects) | before, after, sweep 20, hold 6, labels |
| blurword | BlurWord (Effects) | text, y 1000, size 110, color, font |
| orbit | Orbit (Effects) | tiles[], side back\|front, cx, cy, rx, ry, rev, w, dim (list twice: behind+back, front+front) |
| compare | CompareCards (Effects) | before, after, labels, quote, title{small,block,sub}, tag, muted |
| facehud | FaceHud (Effects) | face[[t,x,y,w,h]], color, uiBox, label "FACE" |
| sticker | StickerEdge (Boil) | width, color, paper, shadow, slap (cutout) |
| boil | DoodleBoil (Boil) | stroke, color, boilEvery, amp, doodles[{kind heart\|star\|box\|arrow\|circle,x,y,at,size,rot,color}] (cutout) |
| winstack | WindowStack (Paper) | items[{src,label,title,at}], x, y, w, dx, dy, dark |
| pinthumb | PinThumb (Paper) | src, note, tag, pinAt, corner tr\|tl, bigW, thumbW |
| terminal | Terminal (Paper) | cmd, result, title, x, y, w, typeAt, perChar, prompt, highlight |
| repo | RepoCard (Paper) | owner, name, desc, stars, licence, stamp, credit, x, y, w, stampAt, creditAt |
| specchips | SpecChips (Paper) | chips[{n,unit,at}], x 72, y 1040, size 34 |
| notepill | NotePill (Paper) | text, accent, x 540, y 1000 |
| slotlist | SlotList (Rapid) | title, rows[{text,at}], x, y, w, cols, size, ink, current |
| scorebars | ScoreBars (Rapid) | title, rows[{label,value}], total{label,value,tag}, x, y, w, startAt, stagger, dark |
| duel | DuelStage (Rapid) | left, right, labels, y, w, gap, tilt, muted, winner 0\|1, winAt, ink |
| fill | Fill (Rapid) | color black, fade 6, opacity 1 |

Captions are not overlays: `captions[{text,start,end,accent?,y?,style?,variant?,accentFont?,ink?}]` at the top level of the props (section 5).

### public/
- `fonts/` (12): Anton, Archivo Black, Instrument Serif Italic, Kaushan Script, Montserrat ExtraBold + SemiBold, Oswald Bold + Medium, Poppins Italic/Light/Medium/SemiBold. (No Shrikhand, Bebas, Playfair, Instrument Serif Regular in the kit; those are ASS-only in TOOLS\fonts.)
- `cards/`: drivendiesel-logo, isspro-logo, powerhungry-logo, ppei-logo, movebumpers-logo, reviewdiesel-logo, dfc-coin (2.3 MB), dfc-white, dynamic-diesels, f600.jpg (2.1 MB), tile-1..8 (wall/orbit tiles).
- plates and test clips: `plate.mp4` (63 MB, current Rival plate), `cutout.webm` (66 MB), `fx-plate.mp4` + `fx-cutout.webm` + `fx-after.mp4` (Driven plate for effect tests), `pip-test.mp4` (8.5 MB), `dfc-01..19-*.mp4` (19 DFC plates, 49 to 114 MB each, ~1.5 GB total).
- `out/`: renders, props, face jsons and sheets for driven v2..v5, bumpers, chandler-test, menu/fx/fb/orbit/boil/compare tests, nxtlvl-recreate, cover tests, all 19 dfc reels, and subfolders `stock-parts/`, `paper-test/`, `rapid-test/`.

### Exact render commands (from the two READMEs)
Menu-kit test (research/reel-references/2026-11-21-menu-kit-test/README.md): props `tools-snapshot/rival-reels/menu-test.props.json`, CardReel, 14 s test, 23 s render; effects test on fx-plate + fx-cutout, 16 s, 52 s render; it lists the overlay types registered at that point (hud through blurword) but gives no command line beyond the pattern.

Stock-parts dry run (research/reel-references/2026-11-21-stock-parts-dry-run/README.md), from TOOLS, `PY = %LOCALAPPDATA%\Programs\Python\Python312\python.exe`:
1. `PY -I vo_scratch.py rival-reels\out\stock-parts\script.txt rival-reels\out\stock-parts\vo --voice am_michael --speed 1.1 --takes 2` (132 s)
2. `PY -I words_to_props.py specs\stock-parts.json rival-reels\out\stock-parts\vo\words.json rival-reels\out\stock-parts\stock-parts.props.json`
3. `cd rival-reels && npx remotion render src/index.ts CardReel out/stock-parts/stock-parts-video.mp4 --props=out/stock-parts/stock-parts.props.json --codec=h264 --crf=18` (65 s for 42.7 s)
4. `PY -I sfx_place.py <events.json> --kit sfx-kit --out sfx_track.wav --duration 42.71 --style gritty --voice vo.wav --placement placement.txt`
5. ffmpeg mix: voice + sfx at -6 dB, `loudnorm I=-14 TP=-1.5`, `aformat=sample_fmts=fltp:channel_layouts=stereo`, video copied.

Other exact lines in use: skill `npx remotion render src/index.ts RivalReel out/<name>-video.mp4 --props=... --codec=h264 --crf=17`; cover `npx remotion still src/index.ts Cover out/<name>-cover.jpg --props=out/<name>.cover.json --frame=0`; DFC `REMOTION_BRAND=dfc npx remotion render src/index.ts RivalReel "<video>" --props="<props>" --codec=h264 --crf=17 --concurrency=4 --log=error`; artboard internally `remotion render --image-sequence --frames=a,b,c`.

## 3. Pipeline order per tier

### Fast tier (memes, same-day, music-driven): build_reel3
1. Clips land loose in `My Drive\VIDEO\inbox`. `watch.py <clip> --out out/<folder>`; Read sheets + transcript.
2. Check the last 12 IG posts (Composio `INSTAGRAM_GET_IG_USER_MEDIA`) so the cut does not repeat.
3. Write `out/gen_<name>.py` that builds the EDL from words.json (pattern: out/gen_dougie.py); `zoom` + `zoom_anchor` on Jacob, `mblur` on fast subject motion, `clean: true` beds, `ambience` always, one `lockup` hook, `sfx` off when a song goes on.
4. `python -I tools\build_reel3.py out\<name>.json` -> `out\renders\<name>.mp4` + `-NOCAP.mp4`; lint must pass. `--captions-only` for text fixes.
5. QA: 8 or 9 frame grid, transcribe the output and compare caption times, `tags:` says bt709, ebur128 near -14 LUFS, `smooth_check.py` clean. Show Jacob the grid.
6. Deliver `<Name> - completed YYYY-MM-DD` in inbox with POST THIS, no-captions, README posting kit (+ handoff set), cover still. Song + beat-grid start in the README.

### Motion-graphics tier on a talking head (RivalReel over a plate)
1. Fast tier steps 1 to 4 produce the plate (`-NOCAP.mp4`); handheld talking heads default `stab: true, mblur: 2`.
2. Copy plate to `rival-reels/public/plate.mp4`.
3. `facetrack.py public/plate.mp4 out/<name>.face.json`; `matte.py public/plate.mp4 public/cutout.webm` (~11 fps).
4. Write `out/<name>.props.json`: captions grouped 2 to 5 words (`captionStyle: "plain"`, y from `layout.caption_ys`), one card per spoken noun, `card_zone` for y, hook/stamp `behind: true`, never over the face (selfies: face owns y 150 to 760, cards y ~1300, 760 wide, x 100).
5. `artboard.py out/<name>.props.json` -> show Jacob, apply redlines by tile, repeat until approved.
6. `npx remotion render src/index.ts RivalReel out/<name>-video.mp4 --props=... --codec=h264 --crf=17`.
7. ffmpeg mux: video from the render, audio from the plate, export recipe + bt709 tags (setparams + x264 colorprim/transfer/colormatrix).
8. smooth_check, frame grid, Cover still, Drive folder.

### Menu / card tier (plate-free CardReel, at most one a week): vo_scratch -> words_to_props -> artboard -> render -> sfx_place
1. Script one beat per line: hook under 7 words, items 8 to 12 words, 150 to 165 wpm, under 45 s.
2. `vo_scratch.py script.txt out\<name>\vo` for timing (report.txt); cut words before Jacob records. On his take: `watch.py` -> words.json replaces the scratch one.
3. Write `specs\<name>.json` (items with cue words, `old` for StrikeStamp, chips with cues, partner icon/tag/sticker, optional gate).
4. `words_to_props.py specs\<name>.json <words.json> rival-reels\out\<name>.props.json` -> plan table, lint, props + `.sfx.json`.
5. `artboard.py rival-reels\out\<name>.props.json` -> Jacob approves by tile BEFORE the full render.
6. `npx remotion render src/index.ts CardReel out/<name>-video.mp4 --props=... --codec=h264 --crf=17`.
7. `sfx_place.py <name>.sfx.json --kit sfx-kit --out sfx_track.wav --duration <durationSec> --style gritty --voice vo.wav` (two or three sounds per reel in practice, 10 to 14 dB under voice; prune the 40-event list first); `sfx_lint.py` to confirm.
8. ffmpeg mix voice + sfx (loudnorm last, two-pass on finals), mux with the export recipe + bt709 tags.
9. `npx remotion still ... Cover` (title in the y 480 to 1440 band, `RIVAL · EP n`), smooth_check, frame grid, Drive folder.

### DFC tier (landscape interview -> vertical reels, `REMOTION_BRAND=dfc`)
1. Source in `My Drive\VIDEO\DFC\` (C8429.MP4, 1920x1080 23.976). `dfc_track.py <src> out/dfc/track.json` once.
2. Define reels in `out/dfc/reels.json` (source, track, fps 24, people, corner_logos, per reel: slug, folder, hook words, accent, keep windows, quote, caption).
3. `python -I out/dfc/gen_dfc.py out/dfc/reels.json [slug ...] [--force]` from the VIDEO folder, one reel at a time. Per reel it: builds an EDL with `crop_x` following the declared speaker (`fps: 24`, `size: [1080,1920]`) -> build_reel3 plate -> copies to public -> `watch.py --model medium` on the plate -> `facetrack.py` -> props (kinetic hook over the chest 3 s, plain Montserrat captions at chin+55 with one gold word, lower third on a guest only, `corners` overlay for the whole reel, no badge, no band) -> `REMOTION_BRAND=dfc npx remotion render ... RivalReel ... --concurrency=4` -> mux -> `smooth_check` -> 8x8 sheet -> `DFC\<Name> - completed <date>\`.
4. Eyeball every sheet (smooth_check cannot see a bad crop). Dynamic Diesels corner logo is for the SEMA set only.

## 4. specs/ folder
- `menu-reel-example.json`: `_schema` block documenting every spec key, plus a 3-item Rival example (Driven fuel system, ISSPRO gauges, Power Hungry Hydra, gate RIVAL).
- `nxtlvl-recreate.json`: 9 paid-vs-free items from the @ai.nxtlvl voiceover, `stamp: "FREE"`, gate REPO (test only).
- `stock-parts.json`: 9 Rival items (rods, pistons, cam, head gaskets, Driven fuel, compounds, hybrid injectors, Hydra, ISSPRO), ghost RIVAL, hud dots, sidebar, gate RIVAL, `captionY` 1180.

## 5. Props JSON schema (src/RivalReel.tsx types)
```
Overlay = { type: string, at: number (s), dur: number (s), props?: {...}, behind?: boolean }
Caption = { text, start, end, accent?, y?, style?: "pill"|"plain", variant?: "sans"|"serif"|"caps"|"italic", accentFont?: "serif"|"script", ink?: boolean }
RivalReel props = { plate, cutout?, captions?, overlays?, muted? (true), captionStyle? ("pill"), fps?, frame?{top,h,bg,rule} }
CardReel props  = { bg? ("#0b0b0c"|"paper"|still|clip), durationSec, fps?, overlays?, captions?, captionStyle? ("plain"), grain? (true) }
Cover props     = { src, atSec?, title, tag?, preset?: "block"|"megante"|"louder", script?, dim?, band? }
Spec (words_to_props) = { composition, bg|plate+cutout, fps, handle?, ghost?, hook{text,accent}, hud dots|bar|null, sidebar, captions auto|none, captionStyle, captionY?, items[{name, short?, cue|at, old?, oldTag?, oldMeta?, stamp?, sub?, icon?, tag?, count{to,prefix,suffix,label}?, chips[{text, cue|after}]?, foot?, sticker?, stickerCue?, accent?}], gate{word,reply,items?,cue,handle}? }
words.json = [{"w": " word", "s": 0.46, "e": 0.80}, ...]
face.json  = [[t, x, y, w, h], ...]  (null box when no face)
sfx events = [{at, kind whoosh|pop|stamp|tick|notify|hit|riser|click, gain_db?, file?, variant?}]
```

## 6. Known open build items (addendum section 2 tail, WORDS-TO-PROPS-README, skill, memories)
1. matte.py: morphological close on the alpha (lumpy edge at the cap).
2. CardReel caption at y 360 on paper plates (caption audit).
3. Serif-italic selection-box accent component (not built).
4. PlainCaption y from the face tracker (chin + 120) instead of fixed bands.
5. Mark the legacy ASS styles (hook/words/cap Oswald + Montserrat) in build_reel3 as legacy.
6. `rampable: true` slot flag in build_reel3.
7. Port list items 3 to 7: digital zoom curve, floor timeline, paper desk, 2.5D teardown, split flap. Port item 4 `WordPillCaption` (per-word pill) also not in the kit.
8. ProgressHud bar only moves per item window; ItemCard has no title accent or per-chip color; StrikeStamp/ItemCard cannot hold through a crossfade (hard cut, 6-frame tailFade); CommentGate has no items cap.
9. No pop/stamp/tick/notify wavs in `tools/sfx/`, so a `.sfx.json` fed to build_reel3 plays click/impact stand-ins and skips notify; the shippable path is sfx_place with sfx-kit, which means two audio paths exist for the same events.
10. Face-aware y for `tooltag` and `params` (use layout.card_zone), UI click sounds on cards, first real reaction reel from Jacob (Chandler notes).
11. Jacob-side: Trial Reel toggle, profile spec, shoot the five openers on the Pocket 3; first menu reel on his own voice; Sunday 48 h read; weekly THE BAR + trending-audio + trend-calendar re-pull.
12. Stale docs: WORDS-TO-PROPS-README layout numbers and caption limits (see the tool table), SFX-README still says words_to_props "does not exist yet", the menu-kit README's overlay list predates compare/facehud/sticker/boil/paper/rapid.

## 7. Flags: live folder vs snapshot vs skill
- Live-only, not in the snapshot: `build_reel.py` (v1 lyric renderer), `build_reel3.py.bak-2026-11-21` (pre-crossfade backup), `earshot/` clone, `sfx/` old kit, `bin/` (rife + Real-ESRGAN, wired to nothing), `models/` (incl. two rnnoise files wired to nothing), `fonts/`, the three venvs, `voice-test/takes` + wavs. The snapshot is code + docs only, which is right, but a rebuild needs the model/venv recipe (VOICE-README has it for voice; nothing documents re-fetching YuNet, RVM, rife or esrgan).
- Snapshot-only: gen scripts (`gen_dougie/driven2/3/4/bumpers.py`), pipeline shells (`driven_v4_pipeline.sh`, `bumpers_pipeline.sh`, `bumpers_rerender.sh`), EDLs, `reel-editor-SKILL.md`, 13 test props under `rival-reels/`. These are the only worked examples of the gen-script pattern; the live originals are scattered in `VIDEO/out`.
- Not in the skill at all: `dfc_track.py`, `out/dfc/gen_dfc.py` and the DFC tier (only in `project_dfc_video` memory), `sfx_lint.py`, `outlier_watchlist.py` (growth, WATCHLIST-README only), `build_reel.py`, the `REMOTION_BRAND=dfc` theme switch, `fps: 24` / `size` / `crop_x` EDL overrides, the `audio_xfade` bed crossfade, overlay types `facehud`, `compare`, `badge`, `lowerthird`, `quote`, `corners`, `titlecard`, `kinetic`, `scriptblock`, `plaincap`, `tooltag` defaults, and the RivalReel `frame` prop (title band; Jacob rejected bands twice, so it should be marked do-not-use).
- Skill typos: the menu-tier line reads `toolso_scratch.py` and `toolsrtboard.py` (backslash-v and backslash-a were eaten); they are `tools\vo_scratch.py` and `tools\artboard.py`.
- Doc drift inside TOOLS: words_to_props code vs its README (layout y and caption limits), SFX-README's "does not exist yet" line, addendum section 2 counts Effects.tsx at 12 (live has 14) and says "27 new overlay types" (live REG has 64 keys total).
- Fonts: `public/fonts` (12) is a subset of `TOOLS\fonts` (26); Shrikhand (TROPI) and Bebas exist only for ASS lockups, not in Remotion. Instrument Serif is loaded from the Italic file under the Regular family name.
- `rival-reels/public` carries ~1.5 GB of DFC plates and ~250 MB of test plates; every Remotion bundle copies public/, so renders get slower as it grows.
