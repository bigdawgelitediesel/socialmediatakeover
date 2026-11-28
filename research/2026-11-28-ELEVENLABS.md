# ElevenLabs, in and out (2026-11-28)

Jacob: "I need you to understand elevenlabs in and out. And on top of a script give me questions I need to answer to make sure I get the best voice possible for my reels." This file is the understanding, read from ElevenLabs' own docs, blog, pricing page and changelog on 2026-11-28 (hosts elevenlabs.io, help.elevenlabs.io, about.fb.com and help.instagram.com were added to this repo's cloud environment for it; the pages were pulled with curl and the docs' `.md` endpoints). The recording script and protocol are `playbook/14-voice-clone-recording-script.md`. The questions are section 10 here. Sources are at the end; where ElevenLabs' own pages disagree with each other, both are given.

## 1. What is connected, as of today

- The ElevenLabs connector is attached to this cloud session and answers. Account: **Creator plan, active, monthly**, 27 of 131,000 characters used this period (121,000 is the plan quota, so the extra is rollover or a bonus), 1 of 30 custom voice slots used, 0 of 1 Professional Voice Clone slots used, no overage.
- The one custom voice is **"Jake 2.0"**, voice id `oazMvPRk6xWkjdIIc2Hs`, category `cloned`, labels male, middle aged, American English. `cloned` is the API's category for an **Instant** Voice Clone; a Professional clone shows as `professional`. So the professional slot the plan pays for is empty.
- What the connector can do from here: list voices, generate speech (two takes per call by default, every call spends credits, `estimate_only` prices a run first), keep the take you pick, transcribe audio (Scribe), design a voice from a description, generate sound effects, music, images and video (the last four are off by house rule). What it cannot do: create or train a clone, change voice settings on a saved voice, read the docs. Clones are made and trained in the ElevenLabs app, by Jacob, because the verification step needs his live voice.

## 2. The product map (what the words mean)

ElevenLabs is three products on one credit pool. **ElevenCreative** is the app: Text to Speech, Speech to Text (Scribe v3, word timestamps, 90+ languages), Voice Changer (speech to speech: you perform, it re-voices in a chosen voice and keeps your timing), Voice Isolator (strips background from a recording), Voice Cloning (instant and professional), Voice Design (a voice from a text description), Voice Remixing (change a voice you own by prompt), Studio (long-form projects, pronunciation dictionaries), Dubbing (re-voice a video into another language in the same voice), Sound Effects, Music, Image and Video, Ads Engine. **ElevenAgents** is voice agents (phone and web bots). **ElevenAPI** is the same engines by API key; the connector in this session is a client of it.

Credits: Text to Speech costs 1 credit per character in the app on every model (API: v4, v3 and Multilingual v2 cost 1, Flash and Turbo 0.5). Speech to Text 330 per minute. Voice Changer and Voice Isolator 1,000 per minute. Sound Effects 200 per generation. Music about 900 per minute. Dubbing 2,000 to 13,500 per minute. In the web app you get two free regenerations within two hours if text, voice and model stay the same. Credits reset on the subscription day; on paid plans unused credits roll over for up to two months, up to 2x the quota.

## 3. The models that matter (Text to Speech, November 2026)

| Model | What it is | Languages | Limit per request | Tags | Settings |
|---|---|---|---|---|---|
| **Eleven v4** (`eleven_v4`) | The flagship since Sep 28, 2026. "Our most emotive model", best voice-clone accuracy, the one ElevenLabs tells everyone to switch to | 90+ | 100,000 characters, about 100 min | Yes | Stability, Similarity, Clone Strength (PVC only). No Style, no Speed, no SSML |
| Eleven v4 Turbo (`eleven_v4_turbo`) | v4 quality at about 100 ms, built for agents | 90+ | 100,000 | Yes | Same as v4 |
| Eleven v3 (`eleven_v3`) | Previous generation, dramatic delivery | 70+ | 5,000 | Yes | Stability only; no Similarity, Speed or Speaker Boost; no SSML |
| Multilingual v2 (`eleven_multilingual_v2`) | Previous generation, "most stable on long-form", best number reading | 29 | 10,000 | No (speaks brackets as words) | Stability, Similarity, Style, Speaker Boost, Speed 0.7 to 1.2, `<break>` pauses, phoneme tags via dictionaries |
| Flash v2.5 (`eleven_flash_v2_5`) | Fast and half price on the API, normalization off by default | 32 | 40,000 | No | As v2 |
| Turbo v2.5 and v2 | Deprecated; ElevenLabs says use Flash | | | | |

For a reel voice-over in Jacob's own cloned voice the choice is **Eleven v4** with a Professional Voice Clone fine-tuned on it. The docs' own words: "Eleven v4 is a net upgrade over Eleven v3, delivering better results in almost every case", "Professional Voice Clones are fully supported in Eleven v4", and "A clone on Eleven v4 may sound substantially different from the same clone on Eleven v3. Compare both with your own content and keep the version that fits." Multilingual v2 stays the fallback when a line needs an exact `<break>` or a speed change, because v4 has neither.

Two v4 behaviours to know. Accent: same language as the samples keeps his accent; a different language comes out fluent in that language with a native accent, not Wyoming English with Spanish words, and ElevenLabs calls that deliberate. Faithfulness: "Eleven v4 captures the source recording more faithfully than earlier models, including background noise, distortion, and other flaws. Clear training audio matters more with this model."

## 4. Instant versus Professional cloning

**Instant Voice Clone (IVC).** Starter plan and up. 1 to 2 minutes of clean audio recommended, each file at least 5 seconds, 10 seconds total minimum; "avoid recording more than 3 minutes, this will yield little improvement and can, in some cases, even be detrimental." It copies everything it hears: "the speed of the person talking, the inflections, the accent, tonality, breathing pattern and strength, as well as noise and mouth clicks." On v4 ElevenLabs claims a big upgrade ("Instant Voice Clones can now capture voices with high fidelity using just 10 seconds of audio"; the v4 marketing page says v4 instant clones now beat Multilingual v2 professional clones). "Jake 2.0" is one of these; nobody has recorded which audio made it.

**Professional Voice Clone (PVC).** Creator plan and up, one slot on Creator. Your own voice only, verified by reading lines aloud ("Voice Captcha"), with the same mic and the same delivery as the samples, each line read once. Audio: "The bare minimum we recommend is 30 minutes of audio, but for the optimal result and the most accurate clone, we recommend closer to 2-3 hours"; the upload screen says "at least an hour of training audio, and ideally as close to three hours as possible." One speaker, one style ("It is better to just include one style in the uploaded samples"), no music, no reverb, no second voice. The app can remove background noise and separate speakers before training. Fine-tuning takes 3 to 6 hours, sometimes up to 24. A PVC trains automatically on Multilingual v2, Flash v2.5 and Turbo v2.5; **Eleven v4 fine-tuning usually starts on its own, but if the v4 row in My Voices shows a plus instead of a tick, click it** (changelog: "Professional Voice Clone fine-tuning for Eleven v4 and Eleven v4 Turbo is now available to every workspace"). You cannot export a clone; keep the raw samples, because "each clone will sound slightly different, even when you use the same audio." Once a PVC exists, its accent and tone cannot be edited; you change the samples and train again.

**Format.** The FAQ: "We strongly recommend MP3 at 192kbps or above ... Uncompressed formats such as WAV usually do not improve clone quality, and they can cause problems with the upload process." The blog: WAV 44.1 or 48 kHz, 16 or 24 bit is fine. Levels: "between -23dB and -18dB RMS with a true peak of -3dB." If there are hours of audio, split into roughly 30-minute files.

**Clone Strength (v4 PVC only).** A slider in Voice settings: low values smooth the voice slightly and give the delivery more freedom, "which often sounds better overall while still sounding like the original voice"; high values stay closer to the recordings. ElevenLabs recommends 0 percent for most voices and 50 percent for distinctive accents or traits.

## 5. How the voice settings work

ElevenLabs' order of importance: **voice first, then model, then settings.** The common start is stability 50, similarity 75, style 0. The engine is non-deterministic: the sliders set how wide the randomness is, so generate a few takes and pick one (the web app gives two free regenerations).

- **Stability**: how much the delivery varies between generations. Too low gives odd, fast performances; too high gives monotone. Lower it for a livelier read and generate several; raise it for a serious, steady read. The blog's ranges: 0.4 to 0.7 for narration, 0.2 to 0.4 for dialogue.
- **Similarity**: how hard it holds to the source voice. Too high on a poor recording reproduces the recording's artifacts and noise. The blog says 0.75 or higher for a branded voice.
- **Style exaggeration** (v2 and Flash only): amplifies the speaker's style, costs stability; "we recommend keeping this setting at 0 at all times."
- **Speaker Boost** (v2 and Flash only): a subtle similarity boost.
- **Speed** (v2 and Flash only): 0.7 to 1.2, default 1.0. On v4 and v3 there is no speed slider; pace comes from punctuation, `[pause]` tags and the training audio itself ("The pacing of the audio is highly influenced by the audio used to create the voice").
- **Clone Strength** (v4 PVC): see above.
- **Audio effects** (after generation, free): Filter, Noise bed, Space (room reverb), Distance (near, medium, far). A clone placed in a small room at near distance can be made to sit under cab footage; a dry studio read will not.

## 6. Writing for the voice (prompting)

- **v4 and v3 take audio tags** in square brackets before the words they colour: emotion (`[tired]`, `[warmly]`, `[sarcastic]`), delivery (`[softly]`, `[slowly]`, `[whispers]`), non-verbal (`[sighs]`, `[laughs]`, `[clears throat]`), pauses (`[short pause]`, `[pause]`, `[long pause]`). Describe how a line is spoken, not what the speaker does; plain words, no hyphens. "Tags land more readily when the delivery is already in the voice's training data." Punctuation does the rest: ellipses add weight, capitals add emphasis. Tags on v2 or Flash are read aloud as words.
- **Pauses on v2 and Flash**: `<break time="1.0s" />`, up to 3 s, a few per script at most; too many make the voice unstable.
- **Pronunciation**: on v4, write the word as IPA between slashes (`/ˈfæs/`); on v2, respell it ("I S S pro") or use a pronunciation dictionary in Studio. ElevenLabs' own rule for a script it writes: only fix a word the voice will very likely misread.
- **Numbers**: v4 reads them as written; Multilingual v2 normalizes numbers best; Flash needs normalization turned on or numbers written out. For a parts guy's reels (years, dollar amounts, part numbers, "6.7", "7.3", "Class 8") this matters: test the exact lines.
- **Length and takes**: longer passages give tags room; for a one-line script generate a few takes. The v4 web limit is 10,000 characters per generation (100,000 by API).

## 7. What a reel costs in credits

A 45 second talking head is about 120 words, about 700 characters, so about 700 credits on v4. The Creator quota of 121,000 characters is roughly 170 reels of that length a month, or about two hours of finished speech. At two reels a day plus retakes the plan covers it several times over; the Voice Changer and Voice Isolator at 1,000 credits a minute are the only features that eat it fast.

## 8. The jobs this can do for the account, and the ones it should not

1. **A voice-over in his voice over b-roll, hook reels and memes** (the text-on-b-roll posts from `workflow_hook_reels_broll_bank`, the recap and explainer shapes). This is the clean fit: no face, so no lip problem, and the line is still his words.
2. **Re-voicing a take whose sound failed.** Voice Changer keeps his timing and performance, so a cab take ruined by wind or a truck going by can be re-voiced with the clone and still match his lips. The Voice Isolator is the gentler first try.
3. **Scratch timing** for `streamline.py` plans and the kit's word timings before he films (the Kokoro scratch voice job, with his own voice instead).
4. **Spanish versions** of the best reels through Dubbing: on v4 the clone speaks fluent Spanish in his timbre. A real reach test for a diesel audience; also a labelled AI post.
5. **Not the daily talking head's voice.** The account's own numbers put human, imperfect talking heads at the top of every grade, Mosseri's 2026 line is that the signs of a human hand are what becomes valuable, and the masterclass research found viewers now assume a voice is a clone until proven otherwise. A synthetic voice on a face-to-camera reel is the one place the clone costs more than it saves.

## 9. The rule nobody can skip: Meta's AI label

Meta's own words (about.fb.com, February and April 2024, label renamed "AI info" July 2024, policy still current on the page): "We'll require people to use this disclosure and label tool when they post organic content with a photorealistic video or realistic-sounding audio that was digitally created or altered, and we may apply penalties if they fail to do so." Audio is explicitly in; Meta says it cannot yet detect audio from other companies' tools, so the duty is on the poster. A reel narrated by a clone of Jacob's own voice is realistic-sounding audio that was digitally created. **Every reel that uses the clone gets the AI label turned on in the share sheet**, and the caption can say it plainly ("voice is my clone, words are mine"). Penalties are unpublished (the Oversight Board asked Meta in March 2026 to publish them; Meta said it is "exploring"). This also means the clone should never be the voice on a reel that is sold as him talking live.

House rule, pending Jacob's answers to section 10: the doctrine's "his voice only, no clone, no later voice-over" was written from the research, not from a Jacob instruction. His request today supersedes it for the jobs in section 8; the daily talking head stays his real voice unless he says otherwise. His words only, always: the clone reads what he wrote or said, never a line written for him.

## 10. The questions Jacob answers before the clone is made

The order matters a little: the first four decide whether to build a professional clone at all and from what; the rest decide how it is trained and used. One at a time is fine.

**What it is for**
1. Which jobs from section 8 do you want the clone to do, and is a reel with your face ever one of them? (Decides the model, the training style, and whether the AI label goes on your main format.)
2. Are you fine turning on Instagram's AI label on every post that uses it, and saying in the caption that the voice is your clone? (If not, the clone stays a scratch and rescue tool.)
3. Do you want it to speak Spanish too? (Decides whether we test v4 dubbing and how we write the Spanish captions.)

**Which Jake it clones**
4. Which recordings sound most like the voice you want on the reels: the cab talking heads (DJI mic, engine off, windows up), the porch selfie, or something else? (The clone copies one style; we pick it now.)
5. How many of your cab takes already exist as clean audio, and are they in Drive raw? (If there is 45 to 60 minutes of clean cab audio, most of the training set is already recorded and the script only fills gaps.)
6. Same mic and same seat for every recording session: is the DJI Mic 2 on the collar at 3 to 5 inches the setup you will keep, and will you record all of it within two days? (Mixed mics and mixed rooms are the most common reason a professional clone sounds wrong.)

**How it talks**
7. At your normal pace, or a touch slower than your reels? (v4 has no speed slider; the pace comes from the samples.)
8. Do the reels need laughs, a sigh, a whisper, raised voice, or is it all steady talk to camera? (Tags only land if that delivery is in the training audio; one style per clone, so if you want range, the samples need that range inside your normal register.)
9. Which of your reels is the delivery reference, the one where the voice is exactly right? (Three links or file names; the clone is graded against them.)

**The words it has to get right**
10. Say the list out loud once on a recording: FASS, ISSPRO, CP4, HPOP, EGR, DPF, DEF, OBS, SEMA, Powerstroke, Duramax, Cummins, PACCAR, Kenworth, Peterbilt, Freightliner, Cheyenne, Laramie, Rawlins, Wyoming, F600, 6.7, 7.3, Class 8, El Coyote, Elite Diesel, Chief, Rival, Stomper, Fordahl, Kill Devil. Which others belong on that list? (Every one goes in the training script and the pronunciation list.)
11. How do you say numbers on camera: "sixty-seven hundred" or "six thousand seven hundred", "twenty twenty-seven" or "two thousand twenty-seven", "6.7" as "six seven" or "six point seven"? (v4 reads what is written; we write it the way you say it.)

**How it gets used**
12. Who presses generate: you in the app, or me from here with the connector? (Settles where the takes land and who logs the credits.)
13. Do you want the clone's reads mixed to sit in the cab (small room, near) or clean like a studio? (The audio effects and the loudness chain are set once.)
14. A fixed sign-off and a fixed first line: do you have them yet? (If yes, they go in the training script so the clone says them exactly.)
15. Who may hear the raw training audio besides you and ElevenLabs? (Nothing personal goes in the samples; the free-talk passages should be shop and truck talk only.)
16. The verification step needs you at a computer with the same mic for about five minutes, reading lines once each: when? (Failing it locks verification for 24 hours.)

**The budget line**
17. Keep the Creator plan at $22 a month (121,000 credits, one professional slot, 192 kbps audio), or is the Black Friday annual at $99 for the first year worth taking before December 1? (Pro at $99 a month only adds 44.1 kHz PCM by API and more credits, which the reels do not need.)

## 11. What to do once the answers are in

1. Gather the cab takes (Drive raw), run the Voice Isolator or the app's noise removal only on takes that need it, cut out restarts and long gaps, export MP3 320 kbps in 30-minute files, keep the WAVs.
2. Record the script in `playbook/14-voice-clone-recording-script.md` in one sitting, two passes, same mic and seat, levels at -23 to -18 dB RMS.
3. Create the Professional Voice Clone in the app with the whole set, verify, wait for the fine-tune, then check in My Voices that Eleven v4 shows a tick; click the plus if it shows one.
4. Test with three real scripts from his own reels on v4 at stability 50, similarity 75, clone strength 0, then again at clone strength 50; generate three takes each; pick by ear against the reference reels; save the winning settings as the house preset.
5. Keep "Jake 2.0" as the instant fallback until the professional one beats it on the same three scripts, then retire it.
6. Every reel that uses the clone: AI label on, one caption line that says so, logged in the posting kit.

## Sources (read 2026-11-28)

- ElevenLabs docs, Professional Voice Cloning: https://elevenlabs.io/docs/eleven-creative/voices/voice-cloning/professional-voice-cloning
- ElevenLabs docs, Instant Voice Cloning: https://elevenlabs.io/docs/eleven-creative/voices/voice-cloning/instant-voice-cloning
- ElevenLabs docs, Voice Cloning overview: https://elevenlabs.io/docs/eleven-creative/voices/voice-cloning
- ElevenLabs docs, file FAQ: https://elevenlabs.io/docs/help-center/product/voices/voice-cloning/what-files-do-you-accept-for-voice-cloning
- ElevenLabs docs, Models: https://elevenlabs.io/docs/overview/models
- ElevenLabs docs, Eleven v4: https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4
- ElevenLabs docs, Text to Speech product guide (voice settings): https://elevenlabs.io/docs/product-guides/playground/text-to-speech
- ElevenLabs docs, Best practices and Prompting Eleven v4: https://elevenlabs.io/docs/best-practices/prompting
- ElevenLabs docs, Changelog (PVC on v4, clone_strength): https://elevenlabs.io/docs/changelog
- ElevenLabs blog, Introducing Eleven v4 (Sep 28, 2026): https://elevenlabs.io/blog/eleven-v4
- ElevenLabs blog, 7 tips for a professional-grade voice clone (updated Sep 22, 2026): https://elevenlabs.io/blog/7-tips-for-creating-a-professional-grade-voice-clone-in-elevenlabs
- ElevenLabs pricing (Black Friday page, Nov 2026): https://elevenlabs.io/pricing
- Meta, Labeling AI-Generated Images on Facebook, Instagram and Threads (Feb 2024): https://about.fb.com/news/2024/02/labeling-ai-generated-images-on-facebook-instagram-and-threads/
- Meta, Our Approach to Labeling AI-Generated Content and Manipulated Media (Apr 2024, updated Jul and Sep 2024): https://about.fb.com/news/2024/04/metas-approach-to-labeling-ai-generated-content-and-manipulated-media/
- The connector's own model guide and "make-voiceover" guide, read in this session.
- Not reachable from here: help.instagram.com returned an error page for the AI label article, and transparency.meta.com is not on the allowed hosts; the Oversight Board note on penalties comes from search results, not a primary page.
