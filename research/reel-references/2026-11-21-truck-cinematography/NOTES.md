# 2026-11-21 truck cinematography references

Downloaded with yt-dlp (Instagram via `/p/<code>/`, YouTube Shorts via `--extractor-args youtube:player_client=web_embedded`, which was the only client serving above 360p on 2026-11-21). Each clip has an `.info.json` and a `watch-<slug>/` folder from watch.py (contact sheets, scenes.csv, transcript). The reading of every sheet is in `research/2026-11-21-truck-cinematography.md`, section 1a.

| File | Source | What it is | Why it is here |
|---|---|---|---|
| ig-1689907668-Df8bS5XxAcy | @fatfendergarage | '59 F100 "The Train", Kaase 572, rollers + lot statics, 19 s, 1.2K likes | Closest analog to Rival: 1959 Ford, grey body on black |
| ig-1689907668-Df-0qp8PJ00 | @fatfendergarage | '66 F100 "Psycho" one-take walkaround at Goodguys, 18 s, 714 likes | The failure mode: parked walkaround in noon sun |
| ig-1689907668-Df8B7lczNZo | @fatfendergarage | "One click at a time" interior hands-on ASMR, 37 s, 10.5K likes | Best truck reel in the set; the clicks format |
| ig-1689907668-Df-mHUmy8cR | @fatfendergarage | Revival convoy, morning test miles, 35 s, 606 likes | Drive-throughs from the shoulder, windshield POV |
| ig-1689907668-Df5sVb7hD7g | @fatfendergarage | '56 twin-turbo, "Built to drive, not to park", 32 s, 6.9K likes | Dark truck against a white wall, smoke |
| ig-1689907668-Df5UFMnRcnn | @fatfendergarage | Megazilla + Whipple unboxing and install, 16 s, 828 likes | Unboxing grammar |
| ig-16843889-Df0hfRUPs22 | @mister_zachary via @squarebodysyndicate | Blazer donuts, one take, 13 s, 7.8K likes | One moment + one line; backlit dust |
| ig-3441184141-Df8FSlpzxY9 | @autotopiala | 740 hp squarebody C10 rollers, 34 s, 14.3K likes | Owner audio over exterior footage (crew shots) |
| ig-258413545-Df-JqYZzl2d | @icon4x4 | "EPIC" Defender listing walkaround, 48 s, 205 likes | Catalogue walkaround: the worst ratio in the set |
| ig-258413545-DflQKnJTy5f | @icon4x4 (shot by @itsmariogarza) | Shop tour, 3 m 44 s, 712 likes | Operator walking backward; not solo-copyable |
| ig-6611718724-Df8VV8WvMTf | @classicridesonly | Kindig CF1 nine-second half-orbit, 39K likes | The highest number: one short smooth move |
| yt-@FatFenderGarage-WJUFlDCUK6Q | Fat Fender Garage YouTube | "This 1959 truck is full of surprises", 41 s, 10.7K views | Point at it, cut to it; floor-level phone under the truck |
| yt-@FatFenderGarage-yCoTSXemIIA | Fat Fender Garage YouTube | "Driving an 800 hp classic truck", 68 s, 6.2K views | Three suction-mount positions in rotation |
| yt-@VelocityRestorations-a0AAyRR5Gvs | Velocity YouTube | 1970 F150 Heritage, Copper Metallic, 42 s, 3.1K views | Dark-studio beauty, light sweep on warm paint |
| yt-@osmo_global-6rNfl5MymcE | DJI Osmo YouTube | "4K cinematic car rolling shots with Pocket 3", 21 s | Rig positions; recipe: ND, 1/30, 4K 10-bit |

Pruned after download (not truck cinematography): Classic Car Studio Viper auction reel, Velocity Mustang reel, AkzoNobel paint launch, three Kindig All Access teasers, two Ringbrothers SEMA reposts, Know How TV GTO door video, ICON gas-station post, and the image-only posts.

Tooling notes for next time: the logged-out profile page does not expose post ids, but `instagram.com/<handle>/embed/` does (grep `shortcode`); `/p/<code>/` with a crawler UA returns og:title and og:description for roughly half the posts before Instagram rate-limits; yt-dlp on `/p/<code>/` succeeds on videos and fails fast on images, so trying every code is the cheapest filter.
