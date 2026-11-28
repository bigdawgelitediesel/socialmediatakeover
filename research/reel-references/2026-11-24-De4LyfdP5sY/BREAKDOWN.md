# @buildwithdarius.ai, "This Claude skill makes unlimited reels" (studied 2026-11-24)

https://www.instagram.com/reel/De4LyfdP5sY/ . Darius Mora, posted 2026-10-24, 38 s. 3,027 likes, 16,081 comments (comment gate "edit").
Jacob, 2026-11-24: "Then learn this and apply."

## What it is

A reel with no camera in it. Every frame is drawn from code (his words: "written as code and rendered frame by frame, not guessed by an AI video model"), with a voice over it. Cream paper background, one serif headline with the key word in rust italic, a small pill caption at y 0.77 with one coloured word.

## The build, second by second

| Time | Beat | On screen |
|---|---|---|
| 0 to 6.5 | The claim | Headline holds still. Two small green-tick chips add under it as he says each benefit ("in any style", "no video credits"). Finished reels fly in from the corner. |
| 6.5 to 8 | "Let me show you how it works" | Small caps label, serif line, a rust underline draws. |
| 8 to 14 | How | A code window types itself, five lines, then a row of finished reels slides in under it. "AI video model" appears and is struck through. |
| 14 to 18 | Objection 1 | Small grey "you might be thinking", the doubt in big serif ("the reels must suck"), struck through, a rust button stamps "not at all." |
| 18 to 20 | Proof | A grid of his reels, a green tick lands on each. |
| 20 to 30 | Objection 2 | A question mark, "they won't go viral", then a window of number tiles that count up one at a time as he says each number. |
| 30 to 34.5 | The comparison | Instagram's own chart draws, his typical reel as a grey line under it, a pill "page age: 6 weeks". |
| 34.5 to 38 | The ask | A comment box types the keyword. |

Why it works: he says the viewer's doubt out loud before the viewer can, strikes it, and answers with a number. Each number appears on the word. Nothing moves once it has landed.

## Applied

- Three new overlays in the Remotion kit (`tools-snapshot/rival-reels-src/components/Code.tsx`): `backdrop` (dark floor with a warm pool of light), `objection` (label, the doubt in Impact, red strike, the answer brushed in yellow), `stattiles` (real numbers counting up, two to a row). In Jacob's main fonts and colours, inside the rule 120 zones.
- Sample: `out/code-sample.props.json` in the kit; stills in `code-sample-row.jpg` here. Sample words only, not a post.
- **Rule 127** in DIESEL-HOUR.

## Limits under the house rules

His voice has to be Jacob's real voice. The numbers have to be real. No generated pictures. So for El Coyote this is a way to dress a stretch of a talking head, or a voice-over reel he records, not a faceless channel.
