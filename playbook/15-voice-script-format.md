# Load a script with the right directions (2026-11-28)

Jacob: "I just want to be able to load a script with the right directions." This page is that, and nothing else. Write the script in your words, run it through one command, paste the result into ElevenLabs. The clone reads it the way you marked it.

## 1. Write it like this

Plain text, in your words, the way you would say it to one person.

- A **blank line** is a new paragraph. The voice takes a breath there.
- **(beat)** is a short pause. **(pause)** and **(long pause)** are longer.
- **(sigh) (exhale) (laugh) (chuckle) (clear throat)** put that sound right where you write it.
- **(quiet) (slow) (warm) (tired) (curious) (sarcastic) (excited) (whisper)** change how the next words are said. It holds until the next direction, so mark it only where the delivery changes.
- **\*word\*** leans on that word. One a sentence at most.
- **Numbers** are read exactly as written, so write them the way you say them: "sixty-seven hundred", "six seven", "twenty twenty-seven", "four fifty-five".
- **"..."** adds weight before the next words. Commas are breaths. A period ends the thought.
- No stage directions. "(grinning)" and "(looking at camera)" do nothing; the voice can only do what a voice does.
- Few directions. One every twenty words or less. Punctuation does most of the work on Eleven v4.

## 2. Run it

```
python -I tools/voscript.py my-script.txt
```

It writes `my-script.v4.txt` next to the script, prints the character count (one credit per character), the length in seconds, and a short list of things to listen for. It swaps the words the model misreads (ISSPRO, FASS, HPOP, SEMA, CP4, Cheyenne, Laramie and the rest in `data/voice/pronounce.tsv`) for a spelling the voice gets right. If a take says a word wrong, add a line to that file and run it again. `--model v2` makes the Multilingual v2 version instead (no tags, `<break>` pauses) for the day a line needs a speed change or an exact pause length.

## 3. Load it

1. ElevenLabs app, Text to Speech.
2. Voice: **Jake 2.0** (the instant clone that exists today). When the professional clone is trained, switch to it; the script does not change.
3. Model: **Eleven v4**.
4. Settings: Stability 50, Similarity 75, Clone Strength 0 (the slider only appears with the professional clone). Leave them there; change the words, not the sliders.
5. Paste the whole `.v4.txt`. Generate. Two free regenerations within two hours if nothing changes. Listen to all three, keep one.
6. Download the MP3. Put it in Drive `VIDEO\raw` with the same name as the script, and the posting kit says the voice is the clone.

Or send me the plain script. I run the tool, generate two takes through the connector in this session, and you pick. It spends your credits either way; a one-minute reel is about 900.

## 4. Two rules that do not move

- The clone reads your words. Never a line written for you.
- Any post that uses the voice gets Instagram's AI label turned on in the share sheet, and one caption line that says the voice is your clone. Meta's rule covers "realistic-sounding audio that was digitally created or altered", and they say they "may apply penalties" when it is missing.

## 5. The example, in your words

Your gratitude take, written plain with four directions (`data/voice/examples/gratitude.txt`):

```
(quiet) Even if life is really hard right now, there's a lot of hard choices... you should find some kind of gratitude buried within those hard choices.

One of the best things I love about a good Sunday is the reflection of what's been going on. Especially with Thanksgiving coming up, you have a lot to be thankful for. I have a lot to be thankful for.

But mainly, being in the right place, at the right time, with the right *people* in my life has been such a blessing. Coming into this next week, it just feels different than any other time in my life. The people that I get to communicate with and talk to on a daily basis.

(beat) I really challenge you guys this week to really understand gratitude. Because there's a lot of big things coming up in my life. Doing the build, personal life, everything. (exhale) It's stressful, and there's big challenges.

(warm) I'm grateful for that.
```

What the tool hands to ElevenLabs (`gratitude.v4.txt`, 159 words, 918 characters, about 60 seconds):

```
[softly] Even if life is really hard right now, there's a lot of hard choices... you should find some kind of gratitude buried within those hard choices.

[pause] One of the best things I love about a good Sunday is the reflection of what's been going on. Especially with Thanksgiving coming up, you have a lot to be thankful for. I have a lot to be thankful for.

[pause] But mainly, being in the right place, at the right time, with the right PEOPLE in my life has been such a blessing. Coming into this next week, it just feels different than any other time in my life. The people that I get to communicate with and talk to on a daily basis.

[short pause] I really challenge you guys this week to really understand gratitude. Because there's a lot of big things coming up in my life. Doing the build, personal life, everything. [exhales] It's stressful, and there's big challenges.

[warmly] I'm grateful for that.
```

## 6. When a take is not right

- Too flat: lower Stability to 40 and generate again, or add one direction where the feeling turns. Not both.
- Too much, over-acted: raise Stability to 60, take out a direction.
- A word said wrong: a line in `data/voice/pronounce.tsv`, run the tool again.
- Pace wrong: v4 has no speed slider. Shorter sentences and a (beat) slow it down; fewer commas speed it up. The professional clone fixes pace at the root, because it learns yours.
- The voice itself is not you enough: that is the instant clone's ceiling. The professional clone is the answer (`playbook/14-voice-clone-recording-script.md`), and the script stays the same.
