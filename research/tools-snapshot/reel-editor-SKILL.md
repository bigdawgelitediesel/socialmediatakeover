---
name: reel-editor
description: Cut an Instagram Reel for Jacob (@elcoyotediesel, Project Rival) from raw clips in Google Drive VIDEO/inbox using the El Coyote editing playbook and tools/build_reel3.py. Use whenever Jacob asks for a reel, a cut, a video, or to "edit this", or drops clips in the inbox. Loads the house rules so no step back is taken between sessions.
---

# El Coyote reel editor

Read first, every time: `C:\Users\Parts\Desktop\socialmediatakeover\research\2026-11-20-EDITING-MASTER-PLAYBOOK.md` (the rules) and the memory `project_editing_mastery`. Lane reports with the evidence sit next to the playbook (`2026-11-20-editing-*.md`). Jacob's verdict history: v1 "crap, oversaturated, lettering bad, flow great"; the fixes are baked into build_reel3.

## Pipeline (all paths are real on this PC)
1. Footage: `C:\Users\Parts\My Drive\VIDEO\inbox\` (Drive mirror). Watch a clip: `python -I "<OneDrive>\Desktop\VIDEO\tools\watch.py" <clip> --out out/<folder>` then Read the sheet jpgs and transcript. iPhone clips are HLG HDR; the renderer tone-maps them automatically.
2. Check Instagram first (Composio `INSTAGRAM_GET_IG_USER_MEDIA`, limit 12) so the cut does not repeat something already posted. Jacob posts several times a day.
3. Write a generator script (`out/gen_<name>.py`) that builds the EDL JSON from `words.json` timestamps, then render: `python -I tools\build_reel3.py out\<name>.json` (add `--captions-only` to re-burn text in seconds). Renders land in OneDrive `Desktop\VIDEO\out\renders\`, slots are cached in `.cache-<name>`.
4. QA before calling it done: grab 8 to 9 frames into one grid and Read it; transcribe the output audio and compare to caption times; check the `tags:` line says bt709; ebur128 near -14 LUFS. Show Jacob a frame grid.
5. Deliver: ONE folder per finished reel in `My Drive\VIDEO\inbox\` named `<Name> - completed YYYY-MM-DD` containing only the POST THIS mp4, the no-captions mp4 and `README - posting kit.txt` (caption, song + start offset, slider settings, checklist). Nothing else goes in the Drive. Never put raw clips in subfolders.

## Non-negotiable rules (short form)
- Hook text on by frame 4, 3 to 7 words, one tan accent word, inside y 285 to 1248. Motion in frame 1 (push-in or flash-forward). First payoff by 4 to 5 s.
- No visual unchanged over 3 s: every static shot gets an eased `zoom`. One speed ramp or half-speed moment per reel on real motion. Whip pans (`whip_left/right`) between locations, hard cuts otherwise, dissolve only at the loop seam.
- Dialogue: `clean: true` beds, J-cut (audio 0.2 to 0.4 s before picture), trim pauses over 0.35 s, keep the breath before a punchline. Never ship digital silence: `ambience` bed always set.
- SFX: whoosh on at most one cut in four, impact on the exact frame of the reveal or hook hit, riser 1 s before the payoff, click on text pops. Keep gains between -8 and -16 dB.
- Text: build_reel3 styles only (Oswald Bold hook, Montserrat SemiBold per-word captions with blurred shadow layer, Label, Tag pill, Small, Serif). No strokes, no new fonts, no more than one accent color.
- Color: no grade beyond "natural". Never add saturation. Verify bt709 tags.
- End within 1.5 s of the payoff with a send line ("send this to the guy who...") plus the handle or series tag. No outro, no fade to black. Last frame rhymes with the first when possible.
- Export is fixed in the tool (1080x1920, 30 fps, crf 17, 16 Mbps cap, closed 1 s GOP). Song is added inside Instagram; give Jacob the song and the beat grid start time.
- Keep lint clean. If lint fails, fix the EDL, do not bypass.

## Voice and brand
Plain blue-collar wording, no em-dashes, no AI tells. El Coyote only (never Elite Diesel or 307 branding on Rival content). SEMA is a "target". Partners get a Tag pill and a thank-you, never a hard sell. Jacob is "Jake, aka El Coyote" in public copy.

## When footage is weak
Say so. The playbook's shooting brief (five-shot sequence, low angles, foreground, one continuous move per reel, HDR Video off, lav mic) is the fix; the edit cannot invent camera moves.
