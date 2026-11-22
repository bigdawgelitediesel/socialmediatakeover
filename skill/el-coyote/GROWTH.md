# GROWTH mode

The strategist. Four jobs: read the numbers and name the lever, plan what to post, keep the profile converting, and land partners for SEMA. Rules by tag: `research/inventory/02-rule-index.md` (HOOK, SENDS, MEASURE, TRIBE, MEME, GATE, PROFILE, PARTNER, CALENDAR).

## The objective (changed 2026-11-21 afternoon)

Jacob: "I'm changing the game. All the videos have to have over a million views, not 30K." Read `research/2026-11-21-MILLION-VIEW-RULE.md` before planning anything. In the 2,286-post watch list only 32 posts (1.4 percent) cleared a million; their median length is 68 s, none under 10 s on TikTok or YouTube, and they come from two shapes: the narrated story (60 to 120 s: Oversteer, DriveHub whose 14K-median channel got 5.76M on "Rare 7.3 Won't Start", Dave's) and the two-man skit (55 to 70 s: joegotti, 9 millions in 60 posts). Instagram adds the closed loop (6 to 12 s, replays counted; Jacob's own 506K). Everything 20 to 40 s and everything that needs a 7.3 to be understood is cut from the grid. The calendar in that file replaces the matrix calendar; `coyote.py plan` already reads it. Ranking at day 15 is by 7-day views; sends per reach and watch share at 48 h are the early warning. The paragraph below is still the mechanism that gets a post moving in its first two days.

## The diagnosis in one paragraph (2026-11-21 morning)

Reach is not the bottleneck and never was: the account gets 3 to 4 times its follower count in views per post and 99 percent of reach is non-followers. Hooks are fixed on the good cuts (Harley Trade 37.8 percent skip, 59 percent watch). Sends are not: build reels send at 0 to 0.06 percent of reach, memes at 1.5 to 4.9 percent, the 10-mil meme at 4.05 percent of views (506,827 views, 20,552 shares). Identity tests, inside jokes and named-tribe news get sent; spectacle and thank-yous get views or nothing. So the grade is sends per reach at 48 h (floor 1, goal 2), the lever is who the reel is for, and the method is the 5 x 6 matrix run two posts a day for 15 days then winners only.

## Read (every 48 h, every Monday)

`coyote.py grade <json> --log` applies `playbook/09-measurement-protocol.md`:

| Number | Floor / goal | If it misses |
|---|---|---|
| Sends per reach | 1 / 2 percent | the format failed (trigger or recipient): change the person type and caption line 1, not the footage |
| Skip | under 45 / 35 | first 2 s opened on a product or a thank-you; open on a person or a move |
| Watch share | 50 / 60 percent | second promise missing: re-hook at 9 to 10 s or cut the length |
| Likes per reach | 3 / 6 percent | low with low sends = vanilla; low with high sends is fine |
| Saves above sends | | education; wrap the tip in a tribe or argument frame |
| Comments above likes | | gated or argument lane; read it as that |

Under 500 reach at 48 h = no read, does not rank. One variable per post or nothing was learned. Views and likes rank nothing.

## Plan (the 30-day run, starts Tue Nov 24, 2026; moved from Nov 22 by Jacob)

- Every afternoon is the talking head in the truck (Jacob, 2026-11-22), 60 to 120 s, rotation Relatable, Trust, Funny with the shop and trucks as backdrop; Rival is two honest check-ins in fifteen days because the build is just starting (Jacob: "jumping the gun", barely any parts bought); format in `playbook/12-talking-head-in-the-truck.md`. Mornings stay the loop, skit or question clip from the shop playground.
- `coyote.py plan` prints today's two slots with the full idea rows; `--week` for seven days; `idea <n>` or `idea shop meme` for a cell; `hooks A|B|C` for the pre-written variants (A Shop x Meme, B Shop x Skit, C Numbers x Named-tribe news).
- The matrix: rows fails/fixes, shop life, tribe identity, old truck nostalgia, numbers; columns roller, narrated story-fix, cutout meme, two-man skit, named-tribe news, clip + question. Send cells: Shop x Meme (2.30 median share), Shop x Skit (1.79). View cells: Fails x Story, Fails x Question-clip. Both: Numbers x Named-tribe news. Eight empty cells are week-two bets.
- Day 15 (Tue Dec 8): rank by sends per reach, ties by lower skip then saves per reach; the winning cell plus a second cell from a different column; keep a build cell in the afternoon if any clears 1 percent, else the build goes to Stories for two weeks. Days 16 to 30: winners only, a new hook every post, a cell is spent after three posts under the day-15 median.
- Weekly re-run of `outlier_watchlist.py` (40 accounts, outlier = views over the account median, 5x flags) files new outliers into cells.
- Trend calendar: `research/2026-11-21-trend-calendar-30d.md` (PRI Dec 10 to 12, holiday shop memes, the Jan "new year new build" slot). Audio: trending check Monday in the order dashboard, Ignix, CreatorDB; the song is chosen for the format it carries, added in-app.
- Cadence: two posts a day is the bounded 15-day sprint the matrix needs for clean reads; after day 30 the floor is 3 to 4 reels a week (research/2026-11-21-live-instagram-algorithm.md), with the mirrors on TikTok and Shorts carrying the extra. Do not run two a day forever.
- Shooting batches that make the plan one-man: five skits in one lunch break with one coworker, five memes in one cutout session against the flat wall, rollers one take each, stories the only evening work.

## Hooks and sends (the rules that moved numbers)

Move on frame 1; first noun by 0.9 s; first payoff by 4 to 5 s; end within 1.5 s of the payoff. Named tribe in the first five words for news. Hater quote on screen for the argument lane ("Leave the '59 alone"), the answer in the back half, countdown in the caption. Desire hook: outcome first, then a character (the viewer, Jacob, the truck). Third-party news framing ("Someone just...") with the builder credited on screen. Caption line 1 is the share line. The hook atlas (73 reels) and the 26 formulas from instagram-agent-skill (`research/reel-references/2026-11-21-DfrvfEtHP8j/SKILLS-STUDY.md`) are the reference; the scorer's LENGTH, SPECIFICITY and dealbreakers are worth using, STAKES and ADDRESS are not. `coyote.py lint hook` is our lint.

## Profile (conversion)

Profile views to follows ran 38 percent during the viral wave; the gate is tapping the name from inside the reel. Spec (`research/2026-11-21-profile-conversion.md`): name field `Jake Dalton | 7.3 Diesel Builds`; bio line 1 "Building a 1959 Ford F600 on a 7.3 Powerstroke", line 2 the parts-counter credential, line 3 the SEMA target; no shop line; pins Harley Trade, "Why companies hate your truck", the current Rival episode; highlights RIVAL / PARTS / CHIEF / JAKE; a text cover on every reel (`Cover` composition); link to elcoyotediesel.com. Trial Reels: check the composer toggle (may be open at 200 followers); every build reel goes out as a Trial with two caption first lines once it is.

## Partners and SEMA

- The partner gets a part that is the payoff of a real episode (spoken, not burned in), a Collab invite on a reel built to be sent, a Story thank-you, the 12-file repost kit, and a place on the truck. SEMA exhibitor rule: exhibiting partners first; non-exhibitors get two marks of 50 square inches max. Pitch ranking and the exhibitor rule are in memory `project_f600_73_swap`; the hard-hitting copy lives on the F600 repo's `partners.html`, the main page stays classy; imply, never beg.
- Every decided Rival part is a fallback; re-spec around partners (non-negotiables: reliability, finish, daily and tow drivability).
- Pitch assets a brand actually reads: the sends and reach numbers of the last 30 days, the audience (76 to 88 percent male, 25 to 44, rural, national), the one viral meme, the Harley Trade skip number, the plan to SEMA with dates, what they get on screen and when. `site/media-kit.html` holds the kit; refresh the numbers monthly.
- Vetting: middlemen and "build managers" are not sponsors (memory `reference_andrew_lavender_build_manager`). Creator programs with no follower minimum: FASS; Harbor Freight invited in June 2026 and was never answered; Hot Shot's Secret ambassador program (April 2026); BD Diesel at bddiesel.com/pages/collab.

## Lanes (September plan, still true)

Pickup is the lane, the Class 8 parts counter is the credential, roughly two pickup posts to one semi post; the truck is now the F600 and Chief (the 6.7) is the second highlight. Counter stories are semi stories; never write them as if pickup owners walked up to it. Principles over anecdotes: what fails, how often, what it costs, because he orders the replacements. He disabled the CP4 and runs a FASS (both jobs: clean feed now, volume later), not a CP3 or DCR conversion.
