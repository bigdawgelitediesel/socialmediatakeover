# @itsmariahbrunner, "4 free GitHub repos for editing videos with AI" (studied 2026-11-24)

https://www.instagram.com/reel/DfmlI5sNFVa/ . Mariah Brunner, posted 2026-11-11, 43 s. 1,797 likes, 2,477 comments (comment gate "4").
Jacob, 2026-11-24: "Watch this and go through all the repos it suggests and clone them for yourself."

## The four, cloned to `clone/` here (ignored by git, about 1.5 GB, this PC only)

| Repo | Stars 11-24 | Licence | What it is |
|---|---|---|---|
| nateherkai/herk-edit-kit | 3,132 | MIT (AIS brand files excluded) | 15 skills for Claude Code or Codex on top of HyperFrames: cut silences, cut mistakes (review-gated), short-form edit, storytelling, a measured playbook from 27 of Nate Herk's reels |
| openfilm/openfilm | 9,261 | MIT | A film as a folder (`film.html`, clips as trimmed sources), a browser timeline editor, local Whisper, Chromium plus ffmpeg render |
| OpenMontageInc/OpenMontage | 83,005 | AGPL 3.0 | Agent instructions plus Python tools, 12 pipelines (talking-head, clip-factory, podcast-repurpose and nine that lean on AI media) |
| heygen-com/hyperframes | 89,403 | Apache 2.0 | HTML, CSS and GSAP rendered frame by frame by headless Chrome; about 450 ready blocks; alpha output; telemetry on by default |

The reel says "over 158,000 stars combined"; the four add to about 184,800 on the day they were cloned.

## What was taken

1. **A rough-cut proposer.** Herk's three cutting scripts (MIT) are in `VIDEO/tools/herk/`, wrapped by `tools/cutfind.py` (snapshot in `tools-snapshot/`). It lists every pause over 0.55 s and every stutter, false start or repeated take. It proposes; Jacob approves.
2. **Numbers** for cutting speech, motion, captions and checks, written into `VIDEO/Setup/MOTION-BRIEF.md` ("Numbers to work to").
3. **Rule 126** in DIESEL-HOUR.

## What was left, and why

None of the four is installed. HyperFrames has telemetry on by default and its skill pulls a CLI from npm at run time; the Remotion kit already draws titles behind the cutout. OpenFilm's skill runs the newest npm version each time and its library search calls their server. OpenMontage is AGPL, so only ideas were taken, in new words. All four push AI pictures, voices, music or colour grades, which the house rules rule out.

## The reel itself

Talking head with a split: four small tool cards float around her at the start (the list shown early as an open loop), each item gets a name card on her chest, then a full-screen red paper beat with a screen clip and two or three caption words. Serif italic for soft words, bold sans caps for the loud ones.
