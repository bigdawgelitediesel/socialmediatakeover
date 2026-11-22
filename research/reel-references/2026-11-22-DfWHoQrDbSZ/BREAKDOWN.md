# @hugh_candoit, "how to remove the AI-ness from claude motion graphics", DfWHoQrDbSZ, 2026-11-04

Carousel (image post), 2,532 likes, 4,912 comments (gate word MOTION). Only slide 1 is reachable logged out (`slide-1.jpg`): "how to remove the 'AI-ness' from claude motion graphics", a Claude mark, an arrow, the After Effects mark, and two phone frames side by side, "claude" on a purple gradient with a glowing ball sliding on a bar, "mine" on flat black with the same ball. The caption is the lesson and the kit it points to is public: github.com/hughminhphan/motion-kit (MIT), the four files are copied here (`README.md`, `SKILL.md`, `LIBRARY.md`, `motion-kit.js`). Hugh makes Instagram reels for hardware, robotics and dev-tool companies; his Instagram profile is login-walled from here and he has no TikTok or YouTube mirror, so the profile read is the repo and this post.

## The lesson, in his words

HyperFrames ships `gsap.defaults({ duration: 0.6, ease: "power3.out" })`, fade up 24 px, staggers 0.08 s apart. Every agent that follows it makes the same video. He replaces it with how an After Effects animator keys things:

1. **A curve per move, named for what the move is.** `kit.land` (0.1, 0.75, 0.15, 1: arrives at speed, long settle, entrances from off frame), `kit.heavy` (0.75, 0, 0.18, 1: slow push off, decisive arrival, big objects and camera), `kit.whip` (0.85, 0, 0.15, 1: hang, snap, hang, state changes), `kit.reveal` (0.22, 1, 0.36, 1: almost all travel in the first third, masked type), `kit.leave` (0.55, 0, 0.9, 0.35: accelerates out, never settles), `kit.wind` (anticipation), `kit.drift` (camera breath). Plus the easings.net, Material 3 and IBM Carbon tables by name.
2. **Duration from distance and weight:** frames = (9 + 1.15 x sqrt(distance px)) x weight at 60 fps, weight 0.7 light, 1 normal, 1.35 heavy. A chip and a full-screen panel do not take the same time.
3. **Exits are quicker than entrances** (about 0.65x) and accelerate out.
4. **One element leads, the rest react at uneven offsets:** 0, 4, 9, 15, 22, 30 frames. Never an even stagger.
5. **Most text just cuts on.** Written text types on. Titles settle their tracking. Masked rises and blur-ins are "the most overused moves in agent video; reach for them last." Opacity fade on everything is the AI tell.
6. **Holds stay alive:** a slow camera drift or a seeded wiggle on a wrapper; nothing dead still for more than about a second.
7. **Springs:** damping 1.0 premium, 0.8 to 0.85 alive, 0.6 to 0.75 physical, under 0.55 cartoon. Transforms only, never opacity. Overshoot is a choice, not a garnish; "bounces read cheap when they are on everything."
8. **Restraint:** about one signature transition per piece. No glow orbs, no shimmer text, no gradient backdrops, no blur-in type.
9. **Check:** scrub frame by frame; any named preset used because it was the default gets replaced; several elements starting on the same frame get a lead and reactions; if most text fades in, cut most of it on; exits faster than entrances; nothing dead still; count the devices.

## Why it got 4,912 comments on 2,532 likes

A before and after of the same scene in the first frame, a claim everyone making AI video already feels ("they all look the same"), the reason given as a quoted line of code, and a deliverable (the kit) behind one word. The content is a diff.

## What this means for our kit (the application; the port spec is research/2026-11-22-motion-rules-port.md)

Our Remotion kit has the exact tells he names. The addendum's shipped timings are "card drop 0.35 s back.out(1.7)", "chips 0.2 to 0.3 s back.out(3) staggered 0.14 s", "count-up power3.out", word-rise-with-blur as the default caption pop, and `pop` springs on most things. That is overshoot on everything, an even stagger, a named preset as the default, and a blur-in. The fix is a day of work on `anim.ts` and `words_to_props.py`, written up in the port spec with his numbers.
