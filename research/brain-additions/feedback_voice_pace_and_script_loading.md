---
name: feedback-voice-pace-and-script-loading
description: "Jacob on the ElevenLabs voice, 2026-11-28: 'This voice seems sluggish', 'I like the 1.20 speed fyi' (house pace 1.20x), 'I just want to be able to load a script with the right directions' (no questionnaires: one tool, paste, go); he gives a hard cap in seconds and names Drive as the destination; the brain gets additions only"
metadata:
 node_type: memory
 type: feedback
 originSessionId: session_01Vdcs8JjbQgcpf8ZNR6A85H
 origin: cloud session (claude.ai/code), written straight to the Drive brain on 2026-11-28; adds only, deletes nothing
 modified: 2026-11-28T07:50:00Z
---

## What he said, in order (2026-11-28, cloud session)

- Asked for ElevenLabs "in and out" plus "questions I need to answer to make sure I get the best voice possible for my reels". Given the research and a list of 17 questions, he answered: **"I just want to be able to load a script with the right directions."** The questions were parked. He wants to write a script in his words and have the directions (pauses, tone, emphasis, pronunciation) handled for him. `tools/voscript.py` and `playbook/15-voice-script-format.md` are the answer.
- With the first script: **"Here is the script I need it to be 44 secs long don't go over. Please get it made in ElevenLabs."** Then: **"Then upload it to the Google Drive."** The cap is a hard number. He names the destination.
- After hearing the first two voice-overs: **"This voice seems sluggish"** and **"Doesn't it? Are we able to train the voice at all? Like speed etc?"** Previews at 1.10x and 1.20x were made. **"I like the 1.20 speed fyi."** With the third script: **"get it made and upload a 1.20 speed version to the drive."**
- **"Please make sure to write what we have done and are doing to the Claude brain in the Google Drive as well only adding and never deleting."** This file is part of that.

## Rule

- Every finished ElevenLabs take goes out at **1.20x**, pitch untouched (`tools/vofit.py`, the default), until the clone is rebuilt from a sample at his real pace. Then back to 1.0.
- Give him the loading path, not a questionnaire: script in, directions applied, two takes out, he picks by ear.
- A cap he gives is to the second. Report the raw and the finished length.
- Deliver where he says (Drive `VIDEO/finished/<Name> - VO - completed <date>`), plus file cards in the chat, and log it in `data/voice/log.tsv`.
- Cloud sessions write what they did and are doing to the Drive brain as **new files**. Never edit or delete what is there.

## Why

The instant clone copies the pace of its training sample, and that sample was slow. He wants to hear himself at reel pace. He asked for understanding "in and out", but what he wanted out of it was one simple action he can repeat on his phone. Same pattern as `feedback_conversational_pace`: one step, no menus.

## How to apply

- When he sends a script: save it, convert it, generate two takes, finish at 1.20x, upload, send the cards, log. Do not ask him to choose settings.
- If a take sounds wrong to him, change one thing (a direction in the script, or Stability by 10) and generate again. Not both.
- When the clone is rebuilt or the professional clone exists, test one take at 1.0 and ask him once whether 1.20x stays.
