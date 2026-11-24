# @omgadrian, "safe zones for vertical video" (studied 2026-11-23)

https://www.instagram.com/reel/DdOy0cnI10R/ . Adrian Per, posted 2026-09-13, 73.6 s, 1080x1920, 24 fps. 11,712 likes, 1,018 comments (read 2026-11-23, no view count public). Caption: "Comment 'grid' and I'll send you my safe zones overlay. These zones are something I keep in mind with every single shot when it comes to filming my videos."

Jacob, 2026-11-23: "Study this." Sheets, transcript and the measured frame (`zones.jpg`) are in this folder. The video stays local.

## What he says (Whisper transcript, checked against his burned-in captions)

1. The top third is "the most important area when it comes to filming vertical."
2. Why: most people watch on mute ("studies show about 75%", his number, no source given). So the visual text hook goes "big and up here, easily readable."
3. Subtitles go in the lower third, but above the bottom strip, because the username and caption cover it.
4. Push subtitles slightly left, because likes, comments and shares sit down the right side.
5. "Most importantly": the eye line sits on the upper third line, in a medium shot, a wide shot or a high angle. Keep it the same from shot to shot so the viewer's eye never has to hunt.

## The zones, measured off his frames (on a 1080x1920 frame)

| Zone | Pixels | Share of frame |
|---|---|---|
| Hook text (green) | y 0 to 620 | top 32 % |
| Eye line (green line) | y 625 | 32.5 % down |
| Subtitles (green) | y 1293 to 1572 | 67 to 82 % down |
| Covered by username and caption (red) | y 1572 to 1920 | bottom 18 % |
| Covered by like, comment, share (red) | x 855 to 1080, from y 640 down | right 21 % |
| His grid | lines at x 345, 729 and y 624, 1285 | thirds |

His red zones are his own drawing, not an Instagram spec. They are a little generous, which is the safe direction.

## How the reel is made

- 12 shots in 73 s, one location (a park), four framings: wide standing, medium, seated wide, high angle. Every framing puts his eyes on the same line, which is the lesson shown and told at once.
- The grid draws on at 6 s and stays for most of the reel. Zones wipe on as coloured blocks while he points at them (he points at empty air; the graphic lands on his hand).
- At 32 s the frame shrinks into a phone mockup on cream, with a fake Instagram bar and buttons, to show what gets covered. Back to full frame at 44 s.
- Two type faces only: a condensed heavy yellow sans for the one key word per beat (THIS, DEEPER, WHY?, 75%, ABOVE, WIDE, SAFE ZONES) with a small yellow italic serif lead-in above it ("and to dive even", "you stay", "most"). Words blur in. Same grammar as rule 117.
- Small yellow serif subtitles with a thin dark edge, a few words at a time, sitting at about y 1480: inside his own subtitle zone.
- Ends on a spoken sign-off, no card. The ask is in the caption only (comment gate with a real file to send).

## Jacob's reels checked against the zones (`check/`, drawn with `tools/safezone.py`)

| Reel | Title | Captions | Eye line |
|---|---|---|---|
| Six Companies trials | In the top zone, but small (64 px) | In the zone (y 1345). Long phrases reach the button column: "professional companies out there" ends near x 1000 | Eyes at about y 830, 200 px under the line |
| Stomper announcement | In the top zone, good size | In the zone | Eyes at about y 830, 200 px low |
| Summit 7.3 BOGO | In the top zone | In the zone | Eyes at about y 780, 150 px low |
| Bro to Bro trials | Middle of the frame, same as the reel it copies. The end of line 3 ("I'm at") reaches x 960, in his button column | none | no face |

So: text placement was already right. Two misses. The eye line is low on every cab talking head (the top third is mostly headliner), and wide caption phrases run under the buttons.

## What to take

- Eye line on y 625 for every talking head. In the edit that is a crop move (`pre_y` lower, or a little more `pre_zoom`), free on 4K source. At the shoot: tilt the phone down a touch so the eyes are a third of the way down the screen.
- Caption box: centre x 460, max width 760 px (x 80 to 840), y 1293 to 1572. Break phrases shorter before letting one run wide.
- Hook lockup: top third, and bigger. It is the only thing a muted viewer reads.
- Run `python -I tools/safezone.py <video> <out.jpg> t1 t2 ...` on the first frame, a wide caption and the middle before delivery.
- Not taken: the comment gate (house ceiling is one post in four, and only with a real deliverable), the phone mockup (nothing of Jacob's needs it).
