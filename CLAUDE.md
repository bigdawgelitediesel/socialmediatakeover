# socialmediatakeover

Growth work for **@elcoyotediesel** ("Jake Dalton"), a diesel creator account in Wyoming.

**Get these three facts right — earlier sessions got them wrong:**

1. **Day job: PARTS MANAGER at a Class 8 / SEMI TRUCK shop.** Heavy-duty, not light-duty.
   He is **not** the mechanic. He has access to the shop and the vehicles.
2. **Personal truck: a 6.7 Powerstroke F350 ("Chief")** that he drives daily and is
   actively building — Halo/Master Chief themed.
3. **Prior experience: drove hotshot.** His one viral reel (260k views) was gooseneck
   trailer loading, so that audience already found him.

So there are two worlds: **heavy-duty Class 8 at work**, **light-duty pickup at home**.
Both are real, and the bridge between them is the differentiator.

## ⚠️ Read these before any strategy, content, or analytics work

1. **`playbook/00-content-plan.md`** — the actual plan. Start here.
2. `analysis/2026-09-15-account-audit.md` — the performance audit
3. `research/` — algorithm, craft, niche and tooling references
4. `data/instagram/README.md` — dataset layout, API gotchas, how to refresh

## THE SINGLE MOST IMPORTANT CONSTRAINT

**Jake is a one-man show.** He works a full day *and* films *and* edits *and* posts. No
camera operator, no editor, no assistant. **Any plan that assumes a second person is
worthless.** Judge every recommendation by "can one guy who's already working a full day
actually do this?"

**He is the PARTS MANAGER, not the mechanic.** Do not write content that requires him to
turn wrenches on camera at the shop. He *does* wrench on his own 6.7. This is an
advantage, not a limitation — see below.

## Account facts (captured 2026-09-15)

| | |
|---|---|
| Handle | **@elcoyotediesel** — "Jake Dalton" |
| Type | Instagram **Creator** (`MEDIA_CREATOR`), **Instagram Login** path |
| IG user ID | `17841415745423249` (app-scoped id is `28260235826936292` — not interchangeable) |
| Followers / Following | **215** / 5 |
| Posts | 53 on profile, **38** retrievable via API |
| Access | Composio `instagram` toolkit, connection `instagram_metic-mutule` |

## The numbers that matter

1. **45,641 reach → 17 new followers in 30 days = 0.037% conversion.**
   **Reach is NOT the bottleneck. Conversion is.** The account gets ~3.8× its follower
   count in views per post — Instagram is already pushing it to strangers. Moving
   conversion to just 0.3% yields ~135 followers/month *with no extra reach*.
2. **290,381 lifetime views, but one reel is 90% of them** (260,008). Baseline without it:
   **821 views/post**. Note: Views counts replays since Apr 2025 — that is not 290,381 humans.
3. **Reels are 99.6% of views. Static posts average 116 views. Stop making them.**
4. **Average watch time 6.8s.** At 30s reels that's ~23% retention — bottom quartile.
   **Cutting to 12–18s is the cheapest available win.**
5. **PERSONAL content = 14.80% ER. SPONSOR content = 1.36% ER — on nearly identical reach**
   (1,127 vs 1,203 avg views). Same eyeballs, **11× difference**. A format problem, not an
   audience problem.
6. **BUILD content averages 206 views** — the worst pillar, and it's what sponsors are
   paying to appear in.

## Pillar performance (this account's own 38 posts)

| Pillar | N | Avg views | ER |
|---|---|---|---|
| PERSONAL | 5 | 1,127 | **14.80%** |
| RELATABLE | 12 | 1,100 | 5.79% |
| MOTIVATION | 7 | 552 | 5.71% |
| BUILD | 8 | **206** | 1.90% |
| SPONSOR | 5 | 1,203 | **1.36%** |

## Audience

87% US · 76% male · 51% aged 25–44 · maximally dispersed rural/small-town (top city has
**3** followers — a *feature* when pitching brands: genuinely national, no bot dilution).
Small but precisely on-target for diesel. **Best posting window: 16:00–19:00.**

## Strategy in one line

**HEAVY-DUTY PARTS KNOWLEDGE applied to a PICKUP BUILD.** That is the whole position, and
nobody else occupies it.

Every successful diesel creator is a **mechanic** — Dave's (1M), Deboss (1M), South Main
(950K), Rainman Ray (663K). Saturated on YouTube, aggregators on Instagram. **The
parts-counter lane is empty on both.** And almost nobody bridges Class 8 and light-duty.

**What only Jake can say:** what actually fails, how often, and what it really costs —
because he orders the replacements. On semis, where a part failure costs an owner-operator
a day of downtime, that knowledge is worth money, not just entertainment.

**The bridge is the hook:** *"I order parts for semis all day. Here's what that taught me
about my own 6.7."* It earns the pickup audience (much larger) using heavy-duty authority
(much rarer), and it makes the Chief build a demonstration of expertise rather than just
another project truck.

**Formats:** "the #1 part I order and why it fails" · real prices, OEM vs aftermarket ·
**"don't buy this"** (he sees return rates — shareable, and credible from nobody else) ·
"what I put on my own truck and why" · unboxings, native to the job · downtime cost math.

He narrates from the counter, not the bay — except on his own 6.7, where he can wrench.

## Hard-won working notes — do not relearn these

- **`WebFetch` is blocked environment-wide.** But **`COMPOSIO_SEARCH_FETCH_URL_CONTENT`
  is NOT** — it routes through Composio and reaches blocked domains. Use it for all web
  research. (Verified against creators.instagram.com.)
- **Instagram publishing already works** via `INSTAGRAM_POST_IG_USER_MEDIA` →
  `INSTAGRAM_POST_IG_USER_MEDIA_PUBLISH`. No new tooling needed.
- **Never request the `reposts` metric at media level** — it 400s and kills the whole batch.
- **Account-level engagement metrics return EMPTY, not zero**, at this follower count.
  Reconstruct from per-post data.
- **Trending audio cannot be applied via API.** Permanent. Sound is a manual in-app step.
- **Cannot initiate DMs** — replies only, 24h window. All brand threads are cold.
- Demographics need `period=lifetime` + `timeframe`, one `breakdown` per call.
- A Composio description claims media insights need 1,000+ followers. **Wrong** — they work
  at 215.
- **This repo is the only durable storage.** Cloud sessions run in ephemeral containers.
  Commit and push anything worth keeping.

## Never recommend (ToS violations, real ban risk)

Engagement pods · follow/unfollow · bought followers · comment bots · private-API libraries
(`instagrapi`) · scraper services (`JUST_ONE_API_*`, Apify IG Scraper).

They're also mechanically self-defeating: every ranking signal Mosseri named is a **ratio**,
so injected engagement inflates numerator and denominator together while polluting the
targeting that is this account's only real asset.

## Open items

- **Trial Reels are locked until 1,000 followers** — treat 1k as a real milestone.
- **`follows`, `profile_visits`, `reels_skip_rate` are missing from `posts.tsv`.** Add them
  to the media-insights metric array (isolated batch first) — they're the two headline
  numbers the plan measures against.
- **Halo/Master Chief IP risk escalates once the truck promotes Elite Diesel commercially.**
  Keep "Chief" a nickname, never reproduce Microsoft marks, never let a sponsor use them.
- **Harbor Freight Creator Program invitation (2026-06-28) was never acted on.**
  FASS states **no follower minimum**. Hot Shot's Secret launched a new ambassador program
  April 2026.
