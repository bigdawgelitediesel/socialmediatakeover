# The voice clone recording: protocol and script (2026-11-28)

For the Professional Voice Clone in `research/2026-11-28-ELEVENLABS.md`. Two parts: how to record, then what to read. The clone copies the sound of these recordings exactly, so the protocol matters more than the words. Swap any line below for your own words at any time; the clone learns the voice, not the script.

## Part 1. The protocol

**Where the training set comes from, in order of value**
1. **Your own cab takes.** Every talking-head take recorded with the DJI mic, engine off, windows up, is already the right style, the right mic and the right room. Pull them from Drive `VIDEO\raw`, strip the video, cut out the restarts and gaps over two seconds, and that is most of the hour.
2. **This script, read in the same seat with the same mic**, to add the words the takes do not contain (the brand names, the numbers, the lists, the quiet register) and to push the total toward the 60 to 90 minutes a reel voice needs. ElevenLabs' minimum is 30 minutes, their best result is two to three hours; more clean audio beats more varied audio.
3. Nothing else. No porch, no shop floor, no phone mic, no old voice memos. One style, one mic, one room.

**The setup, every time**
- Chief's cab, engine off, HVAC off, windows up, phone on silent, nobody else in the truck. If the wind is rocking the truck, wait.
- DJI Mic on the collar, 3 to 5 inches from the mouth, same side every session. Not the Pocket 3's own mic.
- Record 48 kHz, 24 bit, WAV, in the DJI receiver or the phone app. Gain so normal talk peaks around -6 dB and never clips. ElevenLabs' target for the files is -23 to -18 dB RMS with a true peak of -3 dB; that is a normal, steady talking level.
- Thirty seconds of silence first, every session (room tone), so the clean-up has something to measure.
- Record the whole thing within two days, same time of day if you can. A cold morning voice and a tired evening voice are two different voices to the model.

**How to read**
- Talk, do not perform. The target is you on a good reel day: to camera, direct, your pace, your pauses.
- One passage per take. If you flub, stop, two seconds of silence, say the sentence again. The flubs get cut later.
- Leave one to one and a half seconds of silence between paragraphs, half a second between sentences. The clone learns pause length from you.
- No "um" cleanup while you read; a few are fine and they are yours. No throat clearing, no lip smacks if you can help it, water nearby.
- Do not whisper, shout or do voices. Variety comes from the content (a list, a story, a number, a joke, a quiet line), not from acting.

**Before upload**
- Cut restarts, long gaps, coughs, the slate. Keep natural breaths.
- Do not compress, EQ or add anything. Normalize to -3 dBFS peak at most.
- Export MP3 320 kbps (ElevenLabs recommends MP3 at 192 kbps or above and says WAV does not improve the clone and can fail to upload). Keep the WAVs in Drive `VIDEO\raw\voice clone` forever; a clone cannot be exported, and a rebuild on a new model needs the originals.
- Files of about 30 minutes each. Total runtime is what counts, not the number of files.
- Name them `jake-cab-YYYY-MM-DD-01.mp3` and write the mic, the date and the seat in a text file next to them.

**The verification**
- Same cab, same mic, same delivery. Read each line exactly once, then press stop; reading a line twice fails it. Three strikes locks it for 24 hours.

**After training**
- In My Voices, hover the voice: Multilingual v2, Flash v2.5 and Turbo v2.5 tick on their own; if Eleven v4 shows a plus, click it and wait for the email.
- First test, on Eleven v4: stability 50, similarity 75, clone strength 0. Three takes of a real reel script. Then the same at clone strength 50. Pick by ear against the three reference reels. Save the winner as the preset and never touch it per reel.

## Part 2. The script

Two passes. Pass one at your normal reel energy. Pass two the same words, a notch more awake, still you, still talking to one person. Each passage is one take. About 1,850 words a pass plus the three minutes of free talk, roughly 15 minutes at your pace, so the two passes are about 30 minutes; with the cab takes on top that clears an hour.

### Slate (cut before upload)

Jake Dalton. Voice clone recording. Today's date, the DJI mic, Chief's cab, engine off. Pass one.

### Passage 1. Plain talk, the baseline

I order parts for semi trucks all day. That is the job. A driver calls, something on the truck quit, and I find the part, price the part, and get it here before the truck costs him another day sitting. Most of what I know about trucks I learned standing at that counter, not under a hood. I learned which parts come back. I learned which ones never do. And I learned that the expensive part is almost never the one that put you on the side of the road. It is the cheap one you were going to get to. So when I talk about my own truck, that is where it comes from. Not from a shop I own. From a counter I work at, and a truck I drive every day, and a whole lot of mistakes I paid for myself.

### Passage 2. A ranked list

Five things that fail on the first cold morning, in order. Number five, the wipers. They froze to the glass and you tore them in half trying to see. Number four, the block heater cord, because it was never plugged in. Number three, the fuel filter, full of water, and water freezes before fuel gels. Number two, the glow plugs, or the grid heater, that nobody tested in October because the truck started fine in October. And number one, the battery. It did not die this morning. It died in July, and it waited until it was nine below to tell you. Do the first two this month. The other three you can do next month. Nobody does all five, and that is fine, just do the top two.

### Passage 3. A story with a turn

Two in the morning, a fuel island outside Rock Springs, and I am doing math on the back of a receipt. The load paid a dollar ninety a mile. Fuel was high. The trailer tire I had just replaced was three hundred and twenty dollars I did not have. And the math said I had just driven eleven hundred miles to lose money. I sat there a long time. I did not quit that night. I finished the run, I got paid, and I took the next one, because that is what you do when the payment is due on the first. I quit about a year later, on purpose, with a plan, which is a different story. But that night is the one I think about when somebody tells me the truck business is easy money. It is money. It is not easy.

### Passage 4. Numbers and prices

The first truck I bought cost forty-three hundred dollars. The first thing I did to it cost eleven hundred, and it broke the truck. Chief, the truck I am sitting in, is a 2011 F-350 with the 6.7. I have put about nineteen thousand miles on it this year. A fuel filter kit is somewhere around eighty dollars. A battery is two hundred and change. A tow is three hundred and fifty, if you are lucky and close to town. A day of downtime for an owner operator is more than all of that put together. Three hundred and thirty-eight days until the target. The F600 is a 1959. The frame under it will be a 2005 to 2007 Super Duty. Five hundred and fifty to six hundred horsepower at the crank. The counter opens at seven. It closes at five. The phone rings at four fifty-five, every day.

### Passage 5. The names and the acronyms

FASS. ISSPRO. CP4. HPOP. EGR. DPF. DEF. OBS. SEMA. Powerstroke. Duramax. Cummins. PACCAR. Kenworth. Peterbilt. Freightliner. International. Detroit. Allison. Cheyenne. Laramie. Rawlins. Rock Springs. Wyoming. Colorado. F600. F-350. The 6.7. The 7.3. Class 8. El Coyote. Elite Diesel. Chief. Rival. Stomper Customs. Fordahl Bilt. Kill Devil Diesel. Industrial Injection. Power Hungry. Axiom. Derale. S and B. Tire Wheel Experts. Harbor Freight. Milwaukee. The 10 millimeter. A gooseneck. A fifth wheel. A hotshot. A CDL. A VIN. An owner operator. A backorder. A core charge. A regulated return. A lift pump. Glow plugs. A grid heater. An air dryer. A turbo. Compounds. A head gasket. Injectors. The water separator. Anti-gel. A block heater.

Now the same ones in sentences. I disabled the CP4 on my 6.7 and ran a FASS. The ISSPRO gauges tell me before it breaks. The Powerstroke guy flinches before I say the price. I know, because I am the Powerstroke guy. If you own a Cummins, you already told me. If you own a Duramax, you brought the part number. Kenworth, Peterbilt, Freightliner, I order for all three before lunch. Cheyenne gets wind. Laramie gets more wind. Rawlins gets the most. SEMA is the target. Not the goal. The target.

### Passage 6. The quiet one

Some weeks are heavy. You know the kind. Nothing is wrong, exactly, and everything is a little too much. I had one of those a couple of weeks ago, and I noticed I had stopped being grateful for anything, because I was too busy carrying it all. So I started small. I was grateful the truck started. I was grateful somebody at the counter said thank you. I was grateful for the people who were in the right place at the right time. That did not fix the week. It made the week carryable. If yours is heavy right now, start with the truck starting. Work up from there.

### Passage 7. The funny one, deadpan

Things truck guys say that mean the opposite. Runs great, needs nothing. That is the most expensive sentence in Wyoming. A little rust. Always garaged. Cold AC. Tires are newer. I am just going to look. Nobody in history has just looked. And my favorite. I will never sell it. That one is in the listing by spring. I have said every one of these. Twice. I am saying one of them right now about the truck I am sitting in, and I know it.

### Passage 8. Reading the comments

Makes a noise sometimes. Okay. What kind of noise, and when? Because sometimes is not a symptom, sometimes is a schedule. Zero reason to upgrade a lift pump unless you are over seven fifty. He is right that you do not need it for power yet. He is wrong about why you would want it. It is not either or. It protects the pump now, and it is already there when the power comes. Should I let it idle? Plug it in, start it when you need it, drive it to warm it up. Idle is for when there is no other choice. What would you do first, engine, frame or brakes? Brakes. Always brakes. Which one are you? Be honest.

### Passage 9. Trust, the instruction

A code is not a diagnosis. That little reader tells you what noticed the problem. It does not tell you what the problem is. The code names a sensor. The sensor was doing its job. Something upstream made it read wrong. So before you buy the part the code named, do the free thing. Clear it. Drive it. Write down when it comes back, cold or hot, loaded or empty, idle or highway. Then take that sentence to someone who can test, not guess. I am the guy who sells the part the code named. I would rather sell you the right one once.

### Passage 10. Short lines, the openers

Number five. It just started doing that today.
Forty-eight hours until somebody asks if it is done yet.
This is the part that comes back the most, and I am the guy it comes back to.
Nobody in history has just looked.
Nine dollars. That is the part that took out the engine.
Twenty dollars. This is what parks a semi.
I can tell what you drive before you say it.
My truck has a name, and I am not sorry.
It is a twenty-minute job. It just takes all day.
Parts guys are thankful for four things, and none of them are parts.
The part that died is the victim.
Friday is a direction, not a day.
Silence is a five. Noise means it is trying.
So why aren't you a tech? I get asked that about once a week, usually by a tech.
Ten dollars and two minutes tells you whether your battery makes it to January.

### Passage 11. The long flowing one

The thing about working a parts counter at a semi shop is that you see the whole county's trucks come through one phone line, which means you stop believing in luck pretty fast, because the same five parts fail on the same five schedules whether the driver is careful or not, and the only difference between the guy who loses a day and the guy who loses an hour is which of them replaced the cheap part in October when it was a nuisance instead of in January when it was an emergency, and once you see that pattern a few hundred times you cannot unsee it, so you go home and you look at your own truck differently, and you start doing the boring thing first, the filter, the battery, the terminals, the belt, and you stop buying the fun thing until the boring list is done, and that, more than any part I could sell you, is what the counter taught me.

### Passage 12. Days, dates, times and places

Tuesday morning. Wednesday afternoon. Thursday night. Friday at four fifty-five. Saturday in the driveway. Sunday afternoon. November twenty-fourth. December eighth. December twenty-third. January. The second of November, twenty twenty-seven. Nine a.m. Four p.m. Six thirty. A quarter to five. Minus twelve this morning. Forty below with the wind. Interstate 80. Highway 85. The counter. The bay. The parts room. The yard. The driveway. The porch. Main Street. The fuel island. The shop, where I work.

### Passage 13. The lines that repeat

For whoever is about to buy their first truck this winter. Send this to your dad before the first cold morning. Tag the customer who says it just started doing that today. For the parts guy who gets asked why he is not a tech. Send this to whoever has been waiting on a part since October. For everyone building something after work that nobody asked for. I work there. I am not the mechanic. I am the guy the mechanic calls. See you tomorrow. That is the whole job.

If you have picked a sign-off, say it here five times, with a breath between each one, the way you will say it on the reels.

### Passage 14. Free talk, three minutes, no script

Tell the camera what happened at the counter today. Who called first, what they needed, what you could not get, the one that made you laugh. No names, no plates, no prices for the business. Talk until the three minutes are up, then stop. If today was quiet, tell the story of the day the F600 came home.

### Pass two

Read passages 1 through 13 again, a notch more energy, same seat, same mic. Skip the free talk, or do a new one about your own truck. Slate it "Pass two."

## What this gets you

With about 45 minutes of cab takes plus two passes of this script, the set is about 75 minutes of one voice, one mic, one room, one style, with every brand name, number and recurring line the reels use. That is past ElevenLabs' minimum and on the way to their best range. If the cab takes are fewer, read the script a third time the next day at the same hour, and add another three minutes of free talk each time.
