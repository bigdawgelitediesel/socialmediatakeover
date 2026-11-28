---
name: project-elevenlabs-voice
description: "ElevenLabs for El Coyote as of 2026-11-28 (cloud session): the connector is attached and works, voice Jake 2.0 (instant clone), Eleven v4, house pace 1.20x; tools voscript.py and vofit.py; three voice-overs made from Jacob's scripts and delivered to Drive VIDEO/finished; his words only, AI label on every post"
metadata:
 node_type: memory
 type: project
 originSessionId: session_01Vdcs8JjbQgcpf8ZNR6A85H
 origin: cloud session (claude.ai/code), written straight to the Drive brain on 2026-11-28; adds only, deletes nothing
 modified: 2026-11-28T07:50:00Z
---

## What is true now (2026-11-28)

- The ElevenLabs connector is attached to the cloud sessions and answers: it listed voices, generated speech, transcribed audio and read usage on 2026-11-28. The memory `workflow_faceless_voice_reels` says ElevenLabs was not connected on 11-27 and Jacob makes the voice by hand. That is still how the shop PC works; a cloud session can now generate the voice itself. The newer entry wins.
- Account: Creator plan, 121,000 credits a month (the account shows a 131,000 limit), one Professional Voice Clone slot, unused; one Instant clone, **Jake 2.0**, voice id `oazMvPRk6xWkjdIIc2Hs`. One credit per character. Two free regenerations within two hours. A one-minute reel is about 900 credits, two takes about 1,400.
- Model: **Eleven v4** (audio tags in brackets, no speed slider, no SSML; start at Stability 50, Similarity 75, Clone Strength 0). Multilingual v2 is the fallback when a line needs a speed setting or an exact pause length.
- The instant clone talks slower than Jacob does because its sample did. **House pace since 2026-11-28 is 1.20x**, applied after generation with `tools/vofit.py` (see `feedback_voice_pace_and_script_loading`). The root fix is a clone rebuilt from 60 to 90 s of him talking at reel pace, or the professional clone.
- Claude cannot hear a take. The check is Scribe (transcription with word timings) plus the durations, and then his ear. Scribe echoes the prompt text, so a mispronounced word can pass it.

## What was built (repo bigdawgelitediesel/socialmediatakeover, branch claude/laughing-lovelace-4j11x4, PR #3)

- `research/2026-11-28-ELEVENLABS.md`: the understanding from ElevenLabs' own docs (models, instant versus professional cloning, settings, prompting, credits per reel, Meta's AI label duty, build order, and the 17 questions he did not want).
- `playbook/14-voice-clone-recording-script.md`: the protocol and 14 passages for the professional clone (cab takes first, DJI mic, 48 kHz 24-bit, two days, MP3 320 upload, the verification read).
- `playbook/15-voice-script-format.md` and `tools/voscript.py`: his plain script (blank line = paragraph; `(beat)` `(sigh)` `(quiet)` `(slow)` `(warm)` and the rest; `*word*` for emphasis; numbers written as spoken) becomes the v4 script with tags. It applies `data/voice/pronounce.tsv` (ISSPRO, FASS, HPOP, SEMA, CP4, Cheyenne, Laramie and more), prints characters, credits and seconds, and flags stage directions and the words a model misreads. Spends no credits.
- `tools/vofit.py`: finishes a take. Trims the ends, 1.20x with the pitch untouched, two-pass loudnorm to -14 LUFS and -1.5 dBTP, writes a 320 kbps MP3 and a 24-bit WAV. `--tempo 1.0` keeps the generated pace, `--pauses 0.5` halves the pauses instead, `--cap 44` warns over a cap.
- `data/voice/log.tsv`: every voice-over made (date, script, voice, model, takes, raw and final seconds, credits, where it went, notes).
- `data/voice/scripts/`: his plain scripts plus the `.v4.txt` that was sent. `data/voice/examples/gratitude.txt` is the worked example in his own words.

## Voice-overs made (2026-11-28, all Jake 2.0, Eleven v4, two takes each, ElevenLabs flow 5Kt24jRmwh7Wh6zvKBP3)

| Script (his words) | His cap | Finished | Credits | Drive folder in VIDEO/finished |
|---|---|---|---|---|
| "Two fifteen to six hundred" (215 to 600) | 44 s | 43.4 and 43.9 s with pauses scaled; 1.20x versions 40.3 and 40.9 s | 1,384 | `Two fifteen to six hundred - VO - completed 2026-11-28` (id 18B7Y_Xx7BqyoqS328kHzBYlIHjGXqXsU) |
| "Compounds, one feeding the other" (single versus compound turbos) | under a minute | 49.0 and 48.9 s; 1.20x versions 40.9 and 40.8 s | 1,406 | `Compounds, one feeding the other - VO - completed 2026-11-28` (id 1Bi8AaNg0p02Xjf8UOHDs0qgFpnw1pn3T) |
| "Glow plugs, no spark" (spark plug versus glow plug) | 1.20x asked for | 43.3 and 43.6 s at 1.20x | 1,470 | `Glow plugs, no spark - VO - completed 2026-11-28` (id 1YlYjbtsrjas5B7VaGfVNscnUL5dC3SoB) |

- Each folder holds the MP3 takes and `README - posting kit.txt`. The WAV masters stayed in the repo `outbox/` (gitignored) because a Drive connector call caps at about 4 MB. He also got file cards in the chat.
- These three are the voices for the three `voreel.py` shows (`215`, `turbo`, `plug`) in `workflow_faceless_voice_reels`. The shop PC picked up the first two the same night and rendered `215 TO 600 - with voice 2026-11-27` and `SINGLE VS COMPOUND - with voice 2026-11-27` (four looks each: dyno, blueprint, paper, bold) into VIDEO/finished. `SPARK VS GLOW PLUG - drafts 2026-11-28` was still the silent draft when the glow plugs voice landed at 07:28Z.
- The voice files live in **VIDEO/finished**, not VIDEO/inbox. The inbox was retired 2026-11-22: `raw` for footage, `finished` for deliveries.

## The loop that works now

1. Jacob pastes the script in the chat with the cap ("I need it to be 44 secs long don't go over") and the destination ("upload it to the drive").
2. The cloud session saves it to `data/voice/scripts/`, runs `voscript.py`, generates two takes with `creative_generate_speech` (voice Jake 2.0, model eleven_v4), waits on `creative_get_flow_run_status`, downloads the MP3s (elevenlabsusercontent.com), runs `vofit.py` at 1.20x, checks the words with `creative_transcribe_audio`, uploads the MP3s and the posting kit to `VIDEO/finished/<Name> - VO - completed <date>`, sends the file cards, logs the row in `data/voice/log.tsv`, commits.
3. The shop PC session runs `voreel.py --voice` on the MP3 and renders the four looks.

## Rules that do not move

- The clone reads his words only. Never a line written for him.
- Every post that uses the clone gets Instagram's AI label in the share sheet and one caption line that says the voice is his clone. Meta: "realistic-sounding audio that was digitally created or altered" must be disclosed, and "we may apply penalties".
- The daily talking head stays his real voice. The clone is for faceless graphic reels, voice-over, rescue of a failed take, scratch timing and Spanish dubs. His 11-28 ask supersedes the doctrine's "no clone" line, which was research, not his instruction.
- No customer names, plates, faces, invoices or vendor cost in a script. Every number true (`reference_point_check`).

## Open

- SEMA was sent as "see-ma" (/ˈsiːmə/); he has to confirm it sounds right.
- Whether he wants the WAV masters, or the MP3s are enough (the reels use the MP3s).
- Rebuild the instant clone from a brisk 60 to 90 s sample, or record the professional clone (`playbook/14`). Then `vofit.py` goes back to 1.0.
- Cloud environment network, allowed 11-28: elevenlabs.io, help.elevenlabs.io, elevenlabsusercontent.com, about.fb.com, help.instagram.com. Fetch the docs with curl and the `.md` endpoints; the WebFetch agent's DNS fails there.
