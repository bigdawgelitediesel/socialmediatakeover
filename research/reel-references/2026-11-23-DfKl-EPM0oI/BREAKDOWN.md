# @itsaustinmyers, "ungating everything you need to edit videos with Claude" (studied 2026-11-23)

https://www.instagram.com/reel/DfKl-EPM0oI/ . Austin Myers, posted 2026-10-31, 134.5 s, 1440x2560, 3,906 likes, 8,723 comments (comment gate: GUIDE).
Jacob, 2026-11-23: "Study this and do what it asks."

## What it asks, step by step (his words from the transcript, prompts read off the screen in `prompts/`)

1. Make a folder ("AI Video Editor") and open it in Claude Code.
2. **Setup prompt:** four folders (Raw, Projects, Signature Style, Setup) and seven tools (FFmpeg, Python, Node.js, HyperFrames, WhisperX, yt-dlp, Playwright). "Check the tools actually run... Don't call setup finished just because the downloads finished."
3. **Workflow prompt:** save one shared workflow; working helpers, not descriptions; seven steps per reel with approval stops; keep original quality; record completed steps; remember mistakes; careful cleanup; test with disposable files.
4. **Studio-quality Motion Brief:** nine paragraphs on building around the words, handoffs, motion weight, camera versus object movement, phone captions, pace, sound, studying examples, inspecting the real render.
5. **Signature style prompt:** name and handle, three to five of his own edited videos, describe what was observed and what is suggested, ask for feedback before saving.
6. Then per reel: drop the video, "let's edit this reel", rough cut, listen with sound, creative direction, storyboard, 10 to 15 s opening, full edit, tweaks by timestamp, "I approve this", learnings saved.

## What was done here (shop PC, 2026-11-23)

| His step | Result |
|---|---|
| Folder | Already existed: `Desktop/VIDEO`. Added `Setup/`, `Signature Style/`, `Projects/`. Raw stays in `My Drive/VIDEO/raw` and `inbox`. |
| Tools | FFmpeg, Python, Node, yt-dlp run. faster-whisper does WhisperX's job and Remotion does HyperFrames' job, so those two and Playwright were not installed. `Setup/TOOLS.md` says so. |
| Workflow | `Setup/WORKFLOW.md` plus `tools/reel.py` (new, status, step, learn, finish, clean). Tested with disposable files: order enforced, "ok" and "keep going" refused as approval, cleanup touches only `work/tmp`. |
| Motion brief | `Setup/MOTION-BRIEF.md`. |
| Signature style | `Signature Style/SIGNATURE-STYLE.md`, a DRAFT from five of his finished reels. Waiting on his feedback, as the prompt requires. |
| Project instructions | `VIDEO/CLAUDE.md` so a new chat reads all of it first. |
| Learnings | `Setup/LEARNINGS.md`, seeded with six real corrections from 11-22 and 11-23. |

Snapshot of all of it: `research/tools-snapshot/video-setup/` and `research/tools-snapshot/reel.py`.
Not done: the workflow has not been run on a real recording.

## How his reel is made (for the library)

One static seated shot on a staircase for 134 s, no change of framing. Everything else is graphics in the top half: a numbered
step label (a pink 01 to 17 tag plus a serif title), white prompt cards that slide up, folder icons, a waveform for the rough cut,
storyboard tiles. One serif caption word or phrase at chest height. The step counter is what holds a two-minute reel together.
The comment gate has a real deliverable (the written guide).
