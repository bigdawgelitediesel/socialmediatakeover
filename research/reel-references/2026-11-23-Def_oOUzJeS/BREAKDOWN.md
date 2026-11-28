# @tenfoldmarc, "17 video effects Claude can create" (second cut, studied 2026-11-23)

https://www.instagram.com/reel/Def_oOUzJeS/ . Marc Cleroux, posted 2026-10-15, 29 s, 3,170 likes, 7,890 comments (comment gate: STUDIO).
Jacob, 2026-11-23: "Create all these skills in this video."

Same 17 effects as his earlier reel (see `../2026-11-21-Def9pj5TWtA/BREAKDOWN.md` for the effect-by-effect description). This cut runs
them faster: 17 effects in 18 s, about one a second, each named out loud with a yellow name and an 01/17 counter, a fixed
"17 video effects claude can create" title on top for the first nine. Then 10 s of talking: "26 video effects" coming, comment STUDIO, follow.

## Where each one lives in the kit (all 17 callable from RivalReel as of 2026-11-23)

| # | His name | Overlay type | File | Built |
|---|---|---|---|---|
| 01 | orbit | `orbit` (list twice, back and front) | Effects.tsx | 11-21 |
| 02 | couch wall | `wall` layout grid, behind | Effects.tsx | 11-21 |
| 03 | ui world | `uiworld` | Studio.tsx | **11-23** |
| 04 | frame break | `framebreak` | Effects.tsx | 11-21 |
| 05 | digital zoom | `hudzoom` (plus a zoom in the cut) | Effects.tsx | 11-21 |
| 06 | phone mockup | `phone` | Menu.tsx | 11-21 |
| 07 | checklist | `checklist` | Menu.tsx | 11-21 |
| 08 | headline wall | `headlinewall`, behind | Studio.tsx | **11-23** |
| 09 | zoom-through cut | `zoomthrough` | Effects.tsx | 11-21 |
| 10 | chart grow | `chart`, behind | Effects.tsx | 11-21 |
| 11 | pull-back reveal | `pullback` | Effects.tsx | 11-21 |
| 12 | green screen | `bgreplace` | Effects.tsx | 11-21 |
| 13 | paper cut | `papercut` | Studio.tsx | **11-23** |
| 14 | doodle boil | `boil` | Boil.tsx | 11-21 |
| 15 | vertigo | `vertigo` | Effects.tsx | 11-21 |
| 16 | cover story | `masthead`, behind | Effects.tsx | 11-21 |
| 17 | glass type | `glass` | Studio.tsx | **11-23** |

## Proof

`proof-01-09.jpg` and `proof-10-17.jpg`: one frame from each effect in a single 30.6 s render on Jacob's footage
(`tools-snapshot/rival-reels/all17.props.json`). `proof-17-glass-fixed.jpg`: glass type after the fix.

What the proof shows, honestly:
- All 17 render without error. One frame of each was looked at. Motion between frames was not checked.
- The test clip is a tight selfie, so he fills the frame and hides most of what sits behind him (couch wall, headline wall,
  chart, cover story, the doodle boil rim). These need a shot where he is a third of the frame or less, like Marc's seated wide shot.
- Glass type first came out as a frosted rectangle (background-clip: text does not clip a backdrop-filter). Fixed with an SVG clipPath
  and re-rendered on its own. The full 17 proof file still holds the old glass frame.
- The old test tiles are shop photos and must not be used in a real El Coyote reel.

House rules still decide what gets used: one device per reel, nothing over the face, no on-screen call to action, real footage only.
