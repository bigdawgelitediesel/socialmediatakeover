# Lighting (saved 2026-11-23)

Source: @dash.directed reel Dfp6L7lol4F, "34 lighting styles every AI creator should know" (19,262 likes, 6,511 comments).
Jacob, 2026-11-23: "Learn these lighting techniques please."

**What the reel is:** one seated shot of Dash, relit 34 ways in 22 seconds, each look named out loud with a film still beside it.
The relighting is done with AI (the caption sells "prompts"). House rules here are real footage only and no colour grade, so none
of Jacob's footage gets relit. What is taken from it is the names, how to get each one with real light when he films, and how to
read the light in a clip before it is cut (`tools/lightcheck.py`).

## The five that work for his talking heads (use these)

| Look | What it is | How he gets it alone, with a phone |
|---|---|---|
| **Loop light** (6) | Light a little to one side and a little above. One cheek slightly darker, small nose shadow. The standard flattering face light. | In the cab: park so the sun is out the side window, a bit ahead of him, not straight in. In the shop: stand 6 to 10 feet inside the open bay door, turned a quarter away from it. |
| **Soft light** (13) / **Window light** (21) | Big gentle light, no hard shadow edge. | Open shade, an overcast day, or the bay door with no direct sun in it. A dirty windshield is a free diffuser. |
| **Bounce light** (14) | Light hitting a pale surface and coming back to fill the shadow side. | A white truck, a concrete floor, a light shop wall or a sheet of cardboard on the dark side of his face. |
| **Short light** (8) | The side of his face turned AWAY from the camera is the lit one. Slims the face, adds shape. | Turn his nose toward the window, camera on the shadow side. |
| **Golden hour** (17) | Low warm sun in the last hour of the day. | Film the PM talking head 30 to 60 minutes before sunset, sun to the side. Nothing else to do. |

Good for a b-roll or one dramatic beat, not a whole talking head: **Rim light** (11, sun or a shop light behind him, edge of the truck or his shoulders glows),
**Silhouette** (10, him or the F600 against a bright door or sunset sky), **Low key** (2) and **Chiaroscuro** (9, one work light in a dark shop, the block on the stand),
**Practical light** (22, the light source is in the shot: a drop light, the dash lights), **Volumetric light** (26, sun shafts through shop dust or pressure-washer mist),
**Dappled light** (25), **Hard light** (12, noon sun on metal: fine on parts, bad on a face), **Blue hour** (18), **Screen glow** (31, phone or laptop on his face), **Passing light** (32, headlights sweeping the cab at night).

Avoid on his face: **Top light** (15, shop overheads straight down: dark eye sockets), **Under light** (16), **Split light** (5, half the face gone), **Flat light** (27, phone flashlight straight on),
**Broad light** (7, widens the face), direct noon sun (the washed-out post that came down on 2026-11-22), and standing with the open bay door or the sky BEHIND him (backlit, dark face).

Colour looks (teal and orange 29, monochrome red 30, neon 28, day for night 19, moonlight 20, firelight 23, Venetian blinds 24, strobe 33, theatrical 34): only if the light is really there when he films. Never added in the edit.

## All 34, as named in the reel

| # | Name | What it is |
|---|---|---|
| 1 | High key | Bright everywhere, few shadows, light background |
| 2 | Low key | Mostly dark, one small pool of light |
| 3 | Rembrandt | Strong side light from above; a small triangle of light on the shadow cheek |
| 4 | Butterfly | Light straight in front and above; small shadow under the nose |
| 5 | Split light | Light from 90 degrees; half the face lit, half black |
| 6 | Loop light | Light 30 to 45 degrees to the side, a bit above; small nose shadow loop |
| 7 | Broad light | The side of the face toward the camera is lit |
| 8 | Short light | The side of the face away from the camera is lit |
| 9 | Chiaroscuro | Hard contrast between a lit subject and deep black |
| 10 | Silhouette | Subject black against a bright background |
| 11 | Rim light | Light from behind draws a bright edge around the subject |
| 12 | Hard light | Small source, sharp shadow edges (bare sun, bare bulb) |
| 13 | Soft light | Big source, gradual shadow edges (cloud, shade, diffusion) |
| 14 | Bounce light | Light reflected off a surface to fill shadows |
| 15 | Top light | Straight overhead; dark eye sockets |
| 16 | Under light | From below; horror look |
| 17 | Golden hour | Low warm sun near sunrise or sunset |
| 18 | Blue hour | Cool even light just after sunset |
| 19 | Day for night | Daylight footage darkened and cooled to pass for night |
| 20 | Moonlight | Dim cool light from high and to one side |
| 21 | Window light | Soft directional light through a window |
| 22 | Practical light | A light that is visible in the shot does the lighting |
| 23 | Firelight | Warm, low, flickering |
| 24 | Venetian blinds | Striped shadows across subject and wall |
| 25 | Dappled light | Sun broken up by leaves |
| 26 | Volumetric light | Visible beams through dust, smoke or mist |
| 27 | Flat light | Even from the front, no shape |
| 28 | Neon light | Coloured light from signs, two colours on the face |
| 29 | Teal and orange | Warm skin against cool background |
| 30 | Monochrome red | The whole frame in one colour |
| 31 | Screen glow | A screen is the only light on the face |
| 32 | Passing light | Light that moves across the subject (cars, a train) |
| 33 | Strobe light | Flashes |
| 34 | Theatrical light | A hard spotlight circle, shadow thrown on the wall |

## Reading the light before a cut: `tools/lightcheck.py`

`python -I tools/lightcheck.py <clip-or-still> [t1 t2 ...]` finds his face and prints: face brightness, which side is brighter and by how much,
forehead against chin, percent of skin blown out or crushed, background against face, warm or cool. Then the closest name and a verdict.
It measures only. It never changes the picture.

Numbers that mean a talking head is fine: face 95 to 175, side ratio 1.3 to 2.2 (loop range), blown under 2 percent, background not brighter than about 1.25 times the face.
Checked 2026-11-23 against the reel's 34 looks (found the face in 33; the silhouette has no face to find) and four of Jacob's clips:

| Clip | Reading | Verdict |
|---|---|---|
| Stomper announcement (F600 cab) | face 106 to 115, side 1.2 to 1.5 : 1, nothing blown | Loop range. Good. |
| Summit 7.3 (truck cab) | face 99 to 119, side 1.0 : 1 | Flat but clean. Good. A quarter turn toward the side window would add shape. |
| BD Dream | face 156 to 172, side 1.1 : 1 | Flat and on the bright side, nothing blown. Fine. |
| Bed-of-truck selfie (test plate) | middle of the clip: face 74 to 81, background 1.6 to 1.8 times the face, forehead far darker than chin | Backlit by the sky, eyes in the cap shadow. This is the one to avoid. |

Limits: a cap brim reads as "forehead darker than chin", so that line is a hint, not proof of light from below. Thresholds are mine, set from these clips, not from a standard.
