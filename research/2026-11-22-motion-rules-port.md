# Motion rules port: taking the AI-ness out of the Remotion kit (from @hugh_candoit's motion-kit, 2026-11-22)

Source: research/reel-references/2026-11-22-DfWHoQrDbSZ (SKILL.md, LIBRARY.md, motion-kit.js, MIT). Applies to `VIDEO/tools/rival-reels/src/components/anim.ts`, every component that calls `pop`, `popSoft`, `backOut`, `power4Out`, `expoOut`, and `tools/words_to_props.py` timing constants. The kit lives on Jacob's PC; this is the spec for the next kit session, written so it can be done in one sitting.

## What we do today that reads as AI, by his checklist

| Ours (addendum rule 11, 36; anim.ts) | His diagnosis |
|---|---|
| Card drop 0.35 s back.out(1.7) from y+40, scale .92 | overshoot as garnish; same duration whatever the distance |
| Chips 0.2 to 0.3 s back.out(3), staggered 0.14 s | even stagger ("reads like a loop, not a chain of causes") plus a cartoon overshoot on small objects |
| Count-up power3.out | the house preset |
| Word-rise-with-blur as the default caption pop | "masked rises from below and blur-ins are the most overused moves in agent video" |
| `pop` spring (damping 16, stiffness 170) on most entrances | springs on everything; he keeps damping 1 for editorial, 0.8 "alive" at most |
| Static holds between elements on card reels | "the frame dies between moves" |
| Elements leave by tailFade | fades out are the same tell as fades in |

## The port, in order (about a day)

1. **anim.ts: add the curves by name.** `land` (0.1, 0.75, 0.15, 1), `heavy` (0.75, 0, 0.18, 1), `whip` (0.85, 0, 0.15, 1), `reveal` (0.22, 1, 0.36, 1), `leave` (0.55, 0, 0.9, 0.35), `wind` (0.45, 0, 0.55, 1), `drift` (0.4, 0, 0.6, 1), plus `m3.emphasizedDecelerate` (0.05, 0.7, 0.1, 1) and `carbon.expressive.entrance` (0, 0, 0.3, 1). Remotion: `Easing.bezier(x1, y1, x2, y2)`; keep the names in the code so the choice is visible.
2. **anim.ts: `dur(px, weight)`** = round((9 + 1.15 x sqrt(px)) x weight x fps / 60) frames; weight 0.7 light (chips, pills), 1 cards, 1.35 full panels and camera. Replace every hard-coded 0.2 / 0.35 / 0.6 s with it.
3. **anim.ts: `react(i)`** = [0, 4, 9, 15, 22, 30][i] frames (scale by fps / 60). Replace the 0.14 s chip stagger and any `i * k` offset in ItemCard, SidebarList, Checklist, SlotList, SpecChips, ScoreBars.
4. **Exits:** every tailFade becomes a move out on `leave` at 0.65 x the entrance duration, or a hard cut. Keep fades only where "becomes" is the meaning.
5. **Text:** supporting captions cut on (PlainCaption default: no rise, no blur); the hook title may settle its tracking (`trackIn`, letter-spacing from 0.3 em to set over `dur(200, 1)`); typed text (Terminal, PromptBar, CommentGate's typed comment) stays type-on. Retire word-rise-with-blur as the default (addendum rule 36 amended; keep it as an opt-in).
6. **Springs:** `pop` stays only for comedic beats (the LOUDER tier memes). Cards and chips get `land` or a spring at damping 1.0 to 0.85 ("alive, overshoot felt not seen").
7. **Holds alive:** CardReel gets a wrapper with a seeded wiggle (x 6, y 4, rotation 0.5 at about 0.4 Hz) or a 1.00 to 1.03 drift over the whole reel; RivalReel plates already move because they are footage.
8. **One signature device per reel.** IrisWipe, ZoomThrough, Orbit, FrameBreak, Vertigo: pick one per reel, not several. Lint it in words_to_props (count the device overlays, warn above one).
9. **words_to_props.py:** replace LEAD 0.12 / HOLD / the chip stagger with `dur` and `react`; emit the curve name per overlay so the artboard lint can show it.
10. **Check (his section 8) added to the delivery gate:** no preset used because it was the default; no two elements starting on the same frame or in an even line; most text cuts on; exits faster than entrances; nothing dead still over a second; devices counted.

## What not to port

His register table and the glow-free palette rule are already ours (flat colours, no gradients, no sheen). His 60 fps timing base needs the fps scale above (we render 30, sometimes 24). Nothing in his kit touches the fast tier: a song-driven meme with one lockup has no motion graphics to fix.
