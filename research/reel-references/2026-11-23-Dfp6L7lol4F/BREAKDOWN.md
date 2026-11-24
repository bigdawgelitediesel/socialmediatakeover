# @dash.directed, "34 lighting styles every AI creator should know" (studied 2026-11-23)

https://www.instagram.com/reel/Dfp6L7lol4F/ . Dash, posted 2026-11-12, 23.9 s, 1080x1920, 24 fps. 19,262 likes, 6,511 comments.
Caption: "Comment LIGHTS and I'll send you prompts". Jacob, 2026-11-23: "Learn these lighting techniques please."

## What it is

One seated shot (cap, leather jacket, yellow stool, shelf with two practical lamps behind him), relit 34 ways, one look every 0.65 s.
He says each name; a numbered list fills in on screen (two columns, 1 to 24 and 25 to 34); a small film still showing the same look sits at chest height.
The relighting is AI: the same pose, hands and frame under 34 different lights, and the caption sells prompts. The title says "every AI creator".

The 34, in order: high key, low key, Rembrandt, butterfly, split light, loop light, broad light, short light, chiaroscuro, silhouette, rim light,
hard light, soft light, bounce light, top light, under light, golden hour, blue hour, day for night, moonlight, window light, practical light,
firelight, Venetian blinds, dappled light, volumetric light, flat light, neon light, teal and orange, monochrome red, screen glow, passing light,
strobe light, theatrical light. `grid1.jpg` to `grid3.jpg` hold one frame of each, in order.

## What was taken for El Coyote

House rules are real footage only and no colour grade, so nothing of Jacob's gets relit with AI. Taken instead:

1. **The vocabulary**, with what each look is and how he gets it with real light, alone, with a phone: `tools-snapshot/video-setup/LIGHTING.md`
   (the working copy is `Desktop/VIDEO/Setup/LIGHTING.md`). Five are picked for talking heads: loop, soft or window, bounce, short, golden hour.
2. **A way to read light in numbers before a cut**: `tools-snapshot/lightcheck.py`. Face brightness, side ratio, blown and crushed skin,
   background against face, warm or cool, the closest name and a verdict. Checked against all 34 looks here and four of Jacob's clips.
3. **Rule 125** in DIESEL-HOUR.

## The format, for the library

A list reel at its fastest: 34 items in 22 s, the list itself on screen as the progress bar, the same framing every time so only the one variable changes.
The comment gate has a deliverable (the prompts). The same build would work for "34 sounds a diesel makes and what each one costs", real footage, one clip per item.
