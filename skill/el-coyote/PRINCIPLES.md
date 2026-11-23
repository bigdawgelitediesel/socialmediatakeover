# Principles, not steps (2026-11-23)

Why this file exists. Remy (@aiwithremy, reel DeeroIoRpnr): "all Claude takes from those videos is the steps. Step one, bold claim. Step two, numbered list. Step three, CTA. It blindly copies the steps but completely misses the thinking behind them." The library has 114 numbered rules and a doctrine. Applied as steps they produce the same reel every day, and sameness is the loudest AI tell there is. Applied as thinking they produce a different reel from the same seat. So every principle below carries three parts: the thinking (why it works), the step-copy (what it looks like when the shape is copied without the why, which is what to catch in an audit), and the challenge (the question that tests whether this reel actually has it). `tools/streamline.py challenge` asks these; EDITOR, MANAGER and GROWTH audit against them.

## 1. One person
- Thinking: a reel is a message to one viewer, and the viewer decides in a second whether it is to them. "You" plus a concrete thing is the fastest way to say so. Content Labs: "you" lines ran 9.6x an account's norm against 6.2x for "I".
- Step-copy: "you" bolted onto the first sentence while the rest of the reel is about Jacob. A name-call lockup over a video that never turns to the viewer.
- Challenge: who, exactly, and what does he already think that this says out loud?

## 2. The loop
- Thinking: curiosity is the gap between what the viewer knows and what he now wants to know. Open it with the first line, pay it with the last; the pull to resume is real, the memory effect is not, so loops bring people back between episodes and do not carry a dull middle inside one.
- Step-copy: "wait for it", a teased reveal with nothing behind it, three loops stacked so none closes, a question hook with no answer.
- Challenge: what is the last line, and is the first line its opposite? Does the reel pay the open?

## 3. Specificity
- Thinking: the mind renders the concrete and skips the general. Humm's five (where, the verb, the raw thought, the body, the exact words) are five ways to be concrete; the noun by 0.9 s is the same rule measured.
- Step-copy: a number in every hook because "numbers work" (they add about five percent unless the number is the story); a part number instead of the thing the stranger owns; detail that is specific to Jacob but not vivid to anyone else.
- Challenge: which three of Humm's five are in the first 20 s, and would a stranger with no truck see the picture?

## 4. Line one sells line two
- Thinking: every sentence either earns the next or loses the viewer. "But" and "therefore" create a reason to keep watching; "and then" does not. This is pacing by information, which is why a one-take reel can hold and a fast-cut reel can die.
- Step-copy: cutting every three seconds to make a flat script feel urgent; a re-hook at a third and two thirds because a YouTube video did it.
- Challenge: read it aloud and strike every "and then". Where does the retention chart sag, and what information was missing there?

## 5. Change, not cut
- Thinking: the viewer stays for a change he cares about. A cut is one way to make a change and the most expensive, because every unmotivated cut costs a little trust. Across 131 studied reels cut rate does not sort winners from losers; what is changing does.
- Step-copy: jump cuts on a clock, punch-ins to hide them, a whoosh on each, B-roll that repeats the words.
- Challenge: what changes every five to eight seconds without a cut, what is the one physical device, and can every cut be named for what it removes?

## 6. The human reads as human
- Thinking: the tells of a template are uniformity (same framing, same cadence, same caption flash, same hook shape) and the absence of accident (no breath, no dog, no stumble, no weather). The receipts are Mariah's 50K-like one-shot and this account's 14.8 versus 1.4 percent.
- Step-copy: "keep it raw" as a style: fake stumbles, a deliberately bad frame, imperfection as a costume.
- Challenge: what in this reel could only have happened to Jacob on this day in this place? What is different from yesterday's episode (one axis, never all)? And the picture: open a full-size frame from the first shot and the middle; skin natural, blacks black, nothing blown (the look guide, research/2026-11-23-LOOK-GUIDE.md). A cut that passes every principle and ships washed out still gets taken down; it did on 2026-11-22.

## 7. The credential before the mistake
- Thinking: a blunder makes the competent more likeable and the unproven less; the auto audience's prior is that the trade hides cost. So the proof comes first, then the failure, then the downside said out loud.
- Step-copy: self-deprecation as a tic; "I'm just a parts guy" in every reel until it reads as false modesty; a sponsor named with no downside.
- Challenge: where is the proof in this reel, and what is the one thing the part does not do?

## 8. Recognition over news
- Thinking: the most sent line names a thought the viewer has had and never said. Teaching something nobody has felt earns a save; naming something everybody has felt earns a send.
- Step-copy: a "did you know" fact per reel; the counter story told as news to pickup owners who were never at the counter.
- Challenge: what is the sentence a viewer would text to his buddy, and is it caption line 1?

## 9. The set is the brand, the content is the change
- Thinking: a fixed seat, distance and ritual let the audience stop re-learning the frame and start listening; the change then comes from what is said and shown. Keith Lee, Reesa, Fisher, Mariah.
- Step-copy: a fixed set and a fixed script shape, so nothing changes at all; or a new set every day so the series never forms.
- Challenge: same seat, and which one axis rotated today?

## 10. Match the sample
- Thinking: every post is tested on about 200 strangers chosen by what the last posts were about. The same kind of video for the same one person is the only lever on who gets sampled; November's shout-outs sampled to the wrong 200 and cost the next week.
- Step-copy: "niche down" into the 7.3 until nobody without one is in the room; or "go broad" into memes about nothing so the sample has no shape.
- Challenge: broad emotion, diesel proof: would the same 200 who liked yesterday's reel be the right 200 for this one?

## 11. Grade by job
- Thinking: holding and sending are different skills and on this account they run inversely. A talking head is graded on watch share and likes per reach; a meme on sends; everything on skip under 40.
- Step-copy: one scoreboard for everything, so the talking heads look like failures and the memes look like the whole strategy.
- Challenge: what is this reel for, and what number will say it worked?

## 12. Sell nothing for a long time
- Thinking: trust is the asset and every ask spends it. Caleb, Ronny, Kallaway and Trinder say the same thing from four directions: share the knowledge, document the goal, let the content do the selling, and when something is sold it is the execution, not the knowledge.
- Step-copy: a comment gate on every post because it "drives engagement"; a partner part in week two; "link in bio".
- Challenge: does this reel ask for anything, and would it be better if it did not?

## How to use this file
- Before a script: answer the twelve challenges in one line each. If three are blank, it is not ready.
- Before a render: `python -I tools/streamline.py challenge plan.json` prints the counter-arguments, the sameness warnings and the thinking test.
- After a post: the number from principle 11 goes in reads-48h.tsv; the axis rotated goes in data/edits/ledger.tsv.
