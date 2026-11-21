# @rourke "34 lighting styles every AI filmmaker should know" (DfXaQcyoaJ5)

Sent by Jacob 2026-11-21. Rourke Sefton-Minns, posted 2026-11-05, 30.4 s, 63,961 likes, 34,268 comments (gate "Comment AI" for a PDF of the 34 styles with prompts). The biggest of the three reels he sent together. Files: reel.info.json, scenes.csv, sheet-01 and 02, transcript, words.json, shots/. reel.mp4 local only.

## What is on screen
One shot for 30 s: him on a couch, talking to camera. Three layers never leave:
- **A numbered skeleton list at the top** from frame 1: "34 lighting styles every AI filmmaker should know", two columns, slots 1 to 24 and 25 to 34, every number visible and empty. Each name fills in the moment he says it (High key, Low key, Rembrandt, Butterfly... Theatrical light). One name every 0.75 s. The viewer can see how much is left, which is the retention device.
- **The room relights per style.** The whole frame changes with each name: green, teal, warm key, split, silhouette, orange golden hour, blue hour, moonlight, neon pinks, venetian-blind stripes, volumetric beams. The caption says it is all generated in Higgsfield, so the relight is AI applied to his footage, not practical lights.
- **A 16:9 example clip bottom left** with a "video generated with Higgsfield" credit under it, one clip per style, every 0.75 s.
- 26.7 to 30.0: the list is full, the room goes neutral, "comment "AI" for a PDF with all of these + the prompts" burned in under his chin.
No cuts, no music audible under the voice in the sheets, no captions for the words (the list is the caption). 34 beats in 27 s is the fastest pacing of anything studied today.

## What to take
1. **The fill-in skeleton list is the strongest retention device of the day** and it costs nothing. Ported as `SlotList` (components/Rapid.tsx): numbered empty slots from frame 1, one or two columns, each name lands on its word with a 5-frame power4 slide, the current one highlighted, `ink` for paper. Rows come straight from words.json cue words through words_to_props.
2. **The rapid list is a save-and-send utility.** 34 items in 30 s is a reference, not a story; people save it and send it to the friend who films. Diesel version that fits the tribe cells in the outlier matrix: **"Every 7.3 acronym in 30 seconds"** (CPS, UVCH, HPOP, IPR, ICP, EBPV, CAC, IDM, PCM, GPR, EOT, MAP, BARO, VSS, EBP, FPR, DTC, KOEO, KOER, CCV, PMR, FICM is a 6.0 trap and gets struck out) with the real part in the bottom-left window instead of an AI clip, and a one-page glossary PDF as a real gate deliverable. Second: "34 parts on the Rival list in 30 s" with the part photos pinned.
3. **The room relight is not for us** (AI applied to his face; real footage only). The real version exists already in the Boris lighting reel notes (DeEkY1tz4SL): change the actual light per item (bay door, work light, flashlight, welder flash), which is slower but is ours. The rule stands: the change per item must be visible in the frame, not only in the list.
4. **The example window bottom left with a credit line** is the PinThumb idea in motion: the small window shows the thing named while the big frame stays on the person. Our `phone` or `pip` already does it; the credit under it is the partner line.
5. Gate shape: a real PDF, 34,268 comments on 63,961 likes. The ask is burned in for 3 s at the end, which we do not do; ours goes in caption line 1 and in the voice.
