# Four viral memes recreated from Drive footage (2026-11-24)

Jacob: "Find 4 viral meme reels like 3M views and up and recreate them with videos in my Drive."

TikTok video downloads failed all day ("No video formats found", even on clips that downloaded on 11-21), so the sources are YouTube Shorts found through hashtag pages (view counts from yt-dlp), plus one clip already studied in `2026-11-21-diesel-viral-alltime`. Source mp4s stay local (`src/`, not in git).

| # | Source | Views | What it is | Recreation (Drive `finished/MEMES x4 - drafts 2026-11-24`) | Footage |
|---|---|---|---|---|---|
| 1 | Shayna Laliberte, "The car I spent $40k on" (Shorts QdD8M80lPRo) | 3.15M | One line of text, her dancing in front of the car, song | "Standing in the shop where the truck I'm taking to SEMA still can't move", 6.4 s | the shop dance clip (A263E7B4), 4.6 to 11.0 s |
| 2 | Mechanical Nightmare Shorts, "Customer States: my engine is knocking" (VcviAMyHTDU) | 4.06M | The customer's quote in the title, then what the tech found | "Customer states: it ran when parked" over the block being steam cleaned, 9 s | DJI 0033, 4.5 to 13.5 s |
| 3 | C.Z TUNES, "The Definition Of A True Project Car Budget" (agyzLfUaSMM) | 14.1M | Fixed header, a list of what the truck does not have, then where the money went | Header + PAINT NO, A/C NO, BED NO, 7.3 POWERSTROKE YES, 9.2 s | IMG_3861, 3859, 3862, DJI 0030 |
| 4 | Tom's Refurb, "Just a little 331 stroker" | 5.0M TikTok, 6.5M Shorts | The caption undersells, the picture oversells | "Just a little surface rust" over the hood and the lumber-yard door, 8 s | IMG_3857, 3861 |

Built with `build_memes4.py` (ffmpeg + PIL, Impact from the system font, text in the top zone, HLG tone-mapped with libplacebo, no grade). First pass used the zscale / mobius chain and turned the rust bright red; libplacebo matches the phone.

Not checked: sound (Claude cannot hear), motion at full speed. Open with Jacob: the shop dance clip has its own audio (possibly a song); the engine under the red cover in meme 3 is assumed to be the 7.3; "can't move" and "taking to SEMA" are his facts as of 11-22.
