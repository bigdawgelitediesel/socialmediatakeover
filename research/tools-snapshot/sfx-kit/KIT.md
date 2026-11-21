# El Coyote SFX kit (KIT.md)

Built 2026-11-21 by build_kit.py. 16 CC0 slots in five families plus four Earshot renders in earshot/.
Every file is 48 kHz stereo 24-bit wav, DC removed, leading silence cut to 5 ms before the onset, peak-normalised to the house target for its kind.

Peak targets (dBFS sample peak): whoosh -10, pop -12, stamp/hit -7, tick/click -17, notify -12, riser -12.
Styles: gritty = real recording or physical mechanical sound, neutral = synthesised but physical in character, clean = bright digital UI. sfx_place.py refuses gritty + clean in one reel unless --mixed.

Times are seconds inside the file. peak = loudest 5 ms, onset = first 1 ms within 30 dB of the peak, end = last 1 ms within 50 dB of the peak. sfx_place.py uses these to land each sound.

| file | kind | style | moment | len s | onset s | peak s | end s | peak dBFS | source | license |
|---|---|---|---|---|---|---|---|---|---|---|
| whoosh_card_in.wav | whoosh | neutral | card in (a UI card sliding on) | 0.243 | 0.005 | 0.009 | 0.243 | -10.0 | [uisfx 0.4.0 by romainsimon, bundled in the Clipwing real-sfx skill (github.com/Clipwing/skills)](https://github.com/romainsimon/uisfx) | CC0 1.0 audio (LICENSE-AUDIO), MIT code |
| whoosh_air_short.wav | whoosh | gritty | cut whoosh, short air pass | 0.428 | 0.005 | 0.039 | 0.418 | -10.0 | [Freesound #60007 by qubodup, 128 kbps preview fetched through the Openverse API](https://freesound.org/people/qubodup/sounds/60007) | CC0 1.0 (Openverse license field; confirm on the page) |
| whoosh_air_soft.wav | whoosh | gritty | iris open/close, soft air (peak on the frame the circle is largest) | 0.484 | 0.006 | 0.062 | 0.484 | -10.0 | [Freesound #60026 by qubodup, 128 kbps preview fetched through the Openverse API](https://freesound.org/people/qubodup/sounds/60026) | CC0 1.0 (Openverse license field; confirm on the page) |
| whoosh_cloth.wav | whoosh | gritty | cut whoosh, heavier cloth pass | 0.651 | 0.005 | 0.059 | 0.346 | -10.0 | [Freesound #427823 by Kinoton, 128 kbps preview fetched through the Openverse API](https://freesound.org/people/Kinoton/sounds/427823) | CC0 1.0 (Openverse license field; confirm on the page) |
| whoosh_bamboo_low.wav | whoosh | gritty | hook whoosh into the first text hit, low and woody | 0.711 | 0.005 | 0.193 | 0.671 | -10.0 | [Freesound #706679 by Sadiquecat, 128 kbps preview fetched through the Openverse API](https://freesound.org/people/Sadiquecat/sounds/706679) | CC0 1.0 (Openverse license field; confirm on the page) |
| tick_switch.wav | tick | gritty | HUD fill tick, counter step (recorded switch, 28 ms) | 0.028 | 0.004 | 0.007 | 0.028 | -17.0 | [Kenney UI Audio (zip from opengameart.org/content/51-ui-sound-effects-buttons-switches-and-clicks)](https://kenney.nl/assets/ui-audio) | CC0 1.0 (OpenGameArt listing + readme.txt in the zip) |
| tick_short.wav | tick | clean | typewriter key / caption tick, every other character only | 0.012 | 0.000 | 0.003 | 0.012 | -17.0 | [Kenney Interface Sounds (via github.com/Calinou/kenney-interface-sounds mirror)](https://kenney.nl/assets/interface-sounds) | CC0 1.0 (License.txt in the pack) |
| click_press.wav | click | neutral | button press on a card, toggle, chip select | 0.163 | 0.000 | 0.004 | 0.163 | -17.0 | [uisfx 0.4.0 by romainsimon, bundled in the Clipwing real-sfx skill (github.com/Clipwing/skills)](https://github.com/romainsimon/uisfx) | CC0 1.0 audio (LICENSE-AUDIO), MIT code |
| stamp_rubber.wav | stamp | gritty | stamp slap (APPROVED / SOLD / DONE) | 0.535 | 0.005 | 0.042 | 0.503 | -7.0 | [Freesound #362624 by kermite607, 128 kbps preview fetched through the Openverse API](https://freesound.org/people/kermite607/sounds/362624) | CC0 1.0 (Openverse license field; confirm on the page) |
| hit_bong_low.wav | hit | clean | strike / strike-through, low short thud | 0.132 | 0.000 | 0.004 | 0.132 | -7.0 | [Kenney Interface Sounds (via github.com/Calinou/kenney-interface-sounds mirror)](https://kenney.nl/assets/interface-sounds) | CC0 1.0 (License.txt in the pack) |
| hit_deep_drop.wav | hit | neutral | hook impact on the exact frame of a text hit or reveal | 0.584 | 0.001 | 0.073 | 0.557 | -7.0 | [uisfx 0.4.0 by romainsimon, bundled in the Clipwing real-sfx skill (github.com/Clipwing/skills)](https://github.com/romainsimon/uisfx) | CC0 1.0 audio (LICENSE-AUDIO), MIT code |
| pop_chip.wav | pop | neutral | chip pop (a tag or chip appears) | 0.291 | 0.001 | 0.010 | 0.190 | -12.0 | [uisfx 0.4.0 by romainsimon, bundled in the Clipwing real-sfx skill (github.com/Clipwing/skills)](https://github.com/romainsimon/uisfx) | CC0 1.0 audio (LICENSE-AUDIO), MIT code |
| pop_select.wav | pop | neutral | list row / card element lands | 0.244 | 0.000 | 0.068 | 0.244 | -12.0 | [uisfx 0.4.0 by romainsimon, bundled in the Clipwing real-sfx skill (github.com/Clipwing/skills)](https://github.com/romainsimon/uisfx) | CC0 1.0 audio (LICENSE-AUDIO), MIT code |
| notify_dm.wav | notify | neutral | DM notify (a message card arrives) | 0.427 | 0.001 | 0.090 | 0.316 | -12.0 | [uisfx 0.4.0 by romainsimon, bundled in the Clipwing real-sfx skill (github.com/Clipwing/skills)](https://github.com/romainsimon/uisfx) | CC0 1.0 audio (LICENSE-AUDIO), MIT code |
| riser_long.wav | riser | gritty | riser into payoff, 2.0 s, peaks on its last 10 ms | 1.546 | 0.005 | 1.526 | 1.545 | -12.0 | [Freesound #561207 by Rizzard, 128 kbps preview fetched through the Openverse API](https://freesound.org/people/Rizzard/sounds/561207) | CC0 1.0 (Openverse license field; confirm on the page) |
| riser_energy.wav | riser | gritty | riser into payoff, short (0.84 s), cut hard at its own peak so it stops dead | 0.721 | 0.005 | 0.711 | 0.721 | -12.0 | [Freesound #522095 by magnuswaker, 128 kbps preview fetched through the Openverse API](https://freesound.org/people/magnuswaker/sounds/522095) | CC0 1.0 (Openverse license field; confirm on the page) |
| earshot/es_thud_diesel.wav | hit | neutral | diesel-ish low thud hit (cut_hit/sub, 0.5 s) | 0.500 | 0.000 | 0.021 | 0.260 | -7.0 | [Earshot 1.0.0 (github.com/Leonxlnx/earshot) synthesised on this box, see earshot/COMMANDS.md](https://github.com/Leonxlnx/earshot) | MIT code; rendered sounds free for any use, no credit |
| earshot/es_clack.wav | click | neutral | short mechanical clack click (switch/small) | 0.280 | 0.005 | 0.113 | 0.260 | -17.0 | [Earshot 1.0.0 (github.com/Leonxlnx/earshot) synthesised on this box, see earshot/COMMANDS.md](https://github.com/Leonxlnx/earshot) | MIT code; rendered sounds free for any use, no credit |
| earshot/es_riser_1s.wav | riser | neutral | 1 s riser with a hard stop (pro_riser/chop, stops on its loudest 5 ms) | 1.000 | 0.002 | 0.994 | 1.000 | -12.0 | [Earshot 1.0.0 (github.com/Leonxlnx/earshot) synthesised on this box, see earshot/COMMANDS.md](https://github.com/Leonxlnx/earshot) | MIT code; rendered sounds free for any use, no credit |
| earshot/es_whoosh_paper.wav | whoosh | neutral | soft paper whoosh (swipe/paper), card in on a quiet reel | 0.650 | 0.005 | 0.135 | 0.522 | -10.0 | [Earshot 1.0.0 (github.com/Leonxlnx/earshot) synthesised on this box, see earshot/COMMANDS.md](https://github.com/Leonxlnx/earshot) | MIT code; rendered sounds free for any use, no credit |

## Moments to slots

| moment | first pick | rotate with |
|---|---|---|
| card in | whoosh_card_in | earshot/es_whoosh_paper |
| chip pop | pop_chip | pop_select |
| stamp | stamp_rubber | (none, one stamp per reel) |
| strike / strike-through | hit_bong_low | earshot/es_thud_diesel |
| iris | whoosh_air_soft | whoosh_air_short |
| DM notify | notify_dm | (none) |
| cut whoosh | whoosh_air_short | whoosh_cloth, whoosh_air_soft |
| hook impact | hit_deep_drop | earshot/es_thud_diesel |
| riser into payoff | riser_long | riser_energy, earshot/es_riser_1s |
| HUD tick / counter | tick_switch | tick_short (clean, do not mix with gritty) |
| button / toggle click | click_press | earshot/es_clack |

## Sources and licences

- Kenney Interface Sounds, CC0, https://kenney.nl/assets/interface-sounds. Fetched from the GitHub mirror github.com/Calinou/kenney-interface-sounds (License.txt: Creative Commons Zero). The kenney.nl download button is JavaScript-gated (initiateDownload), so the mirror was used.
- Kenney UI Audio, CC0, https://kenney.nl/assets/ui-audio. Fetched as UI_SFX_Set.zip from opengameart.org/content/51-ui-sound-effects-buttons-switches-and-clicks (listed CC0, uploader Kenney).
- uisfx 0.4.0 (romainsimon), CC0 audio, bundled as vendor/node_modules/uisfx inside the Clipwing real-sfx skill (github.com/Clipwing/skills, scripts MIT). Note: uisfx sounds are deterministic synthesis, not recordings; the mechanical, organic, cinematic and studio packs read physical enough for us and are tagged neutral.
- Freesound CC0 previews (128 kbps mp3) found through the Openverse API (api.openverse.org/v1/audio/, license=cc0). Credits in downloads/openverse/credits.txt. Confirm the licence on each Freesound page before a sponsor reel; the original wav needs a Freesound login.
- Earshot renders: code MIT, output free for any use. Commands in earshot/COMMANDS.md.
