# @elcoyotediesel — Account Audit

**Captured 2026-09-15** · 38 posts (Jun 25 – Sep 9, 2026) · 215 followers

---

## Headline

Across 38 posts: **290,381 views · 195,803 reach · 2,839 interactions.**

One reel is 90% of that:

> *"Well it seemed like a good idea…"* (Jul 24) — **260,008 views, 171,025 reach,
> 1,241 likes, 37 comments, 26.9s avg watch time**

Strip it out and the real baseline appears: **37 posts, 30,373 views, 821 views/post.**

## The core problem: reach does not convert

| 30-day window (Aug 17 – Sep 15) | |
|---|---|
| Accounts reached | **45,641** |
| New followers | **17** |
| Conversion | **0.037%** |
| Profile link taps | **0** |

The account reached ~196,000 accounts lifetime and holds 215 followers. Reach is
not the bottleneck. Conversion is.

**Why the viral reel didn't convert:** it showed a *mistake* — a truck loaded on a
gooseneck so the ramps couldn't deploy. The comments are people correcting it
("Won't be able to get the ramps to unload it" — 137 likes; "I don't understand..
it seemed to work 😂" — 340 likes). The 26.9s watch time is people studying the
frame, not admiring it. Its engagement rate was **0.8%** — worst of any post above
200 reach. Correction-bait reaches strangers and converts nobody.

## Format verdict

| | Posts | Views | Avg views | Share |
|---|---|---|---|---|
| **Reels** | 29 | 289,335 | 9,977 | **99.6%** |
| Static / carousel | 9 | 1,046 | **116** | 0.4% |

Nine static posts produced 1,046 views between them. Average reel watch time: **6.8s**.

**Static posts should stop.** They cost the same effort and return ~1% of the reach.

## The template that actually works

> *"It may cost you nothing, but to me. It means everything."* (Jun 30)
> 5,157 views · 3,636 reach · **419 likes, 73 comments, 17 shares, 10 saves → 15.46% ER**

Nearly 20× the engagement rate of the viral post. Two reasons, both repeatable:

1. **Personal and aspirational**, first-person, emotionally direct.
2. **Jake replied to almost every commenter** ("hell yeah brother", "thank you for
   the support"). Highest-value 40 minutes anyone has spent on this account.

Runners-up, same DNA: *"This should explain it"* (10.7%), *"Don't be afraid!"*
(7.7%), *"Yeah that about sums it up"* (6.5%). Short, punchy, first-person.

## The business content is the worst-performing content

The "Chief" F350 build — the entire point of the account — underperforms badly:

| Post | Views |
|---|---|
| "MEET CHIEF" origin story | **57** |
| Chief made it to Wyoming | 138 |
| Leaving Utah heading to Wyoming | 81 |
| Interior teardown | 372 |
| Industrial pump swap | 282 |

And the sponsor posts, where money is involved:

| Partner | Views | Reach | Engagement rate |
|---|---|---|---|
| FASS Fuel Systems | 3,400 | 3,164 | **1.39%** |
| Derale Performance | 404 | 369 | **1.63%** |
| ISSPRO (pillar + gauges) | 336 | 269 | 4.83% |
| Tire Wheel Experts | 117 | 93 | 4.30% |

FASS got the reach but the lowest engagement on the account. Partners are being
delivered impressions, not advocacy. A commenter said it plainly:
*"bro post content not shots of your truck trust there is a way to make it work
but this isn't it."*

**The content that performs and the content that pays are two different accounts
right now.** That gap is the strategic problem.

## Audience — small, but extremely well-targeted

- **Geography:** US **187 (87%)**, Canada 11, then singles across 15 countries.
- **Cities:** maximally dispersed — top city has **3** followers (Syracuse, UT).
  Small-town and rural America: Gretna NE, Ragley LA, Crane TX, Greenleaf ID,
  Rock Springs WY, F.E. Warren AFB WY, Cheyenne WY.
- **Gender:** Male **163 (76%)**, Female 17, Undeclared 37.
- **Age:** 25–34 → 57 · 35–44 → 54 · 45–54 → 35 · 18–24 → 34 · 13–17 → 16 ·
  55–64 → 14 · 65+ → 7. **51% in the 25–44 core** — exactly the diesel-truck
  buying demographic.

This is a *small* audience but a precisely correct one. It is the account's
main asset.

**Best posting window:** hours **16–19** (85–105 followers online), solid plateau
09–15, dead 01–04. Hours are in the account's reporting timezone (day boundary at
07:00 UTC). The two best-performing posts went up at 17:43 and 01:52 — the latter
succeeded *despite* the timing.

## Loose threads

- **0 profile link taps in 30 days.** No conversion path off the account at all.
- **Follows only 5 accounts.** Zero outbound community presence in a niche built
  on reciprocity.
- **Cadence is slipping:** Jun 7 → Jul 13 → Aug 16 → **Sep 2**, then six days dark
  from Sep 9, during the month's best reach stretch.
- **Publishing quota 0/100.** Nothing rate-limits this account but its own output.
- 15 of 53 posts predate the Creator conversion and are API-invisible.

## Bottom line

A precisely targeted audience, a proven engagement formula, and a content strategy
pointed away from both. Growth is not blocked by reach — 195,000 accounts have been
reached. It's blocked because nothing converts reach into followers, and the build
content meant to carry the brand is the content nobody sees.

---

# Addendum — Skip Rate Analysis (2026-09-15, later same day)

Pulled `reels_skip_rate` for all 29 reels: the share of viewers who leave within the first
three seconds. It is the only per-post measure of hook quality the API exposes.

## Skip rate by pillar

| Pillar | Skip rate |
|---|---|
| PERSONAL | **37.3%** |
| RELATABLE | 41.0% |
| MOTIVATION | 44.8% |
| BUILD | 57.8% |
| **SPONSOR** | **72.5%** |

Account average **48.2%**. The four worst hooks on the account are all sponsor or build
posts, topping out at 85.6%.

**This reframes the sponsor problem.** It is not that the audience dislikes brand content —
roughly **two of every three people never see it**. They are gone before the content starts.
A hook problem is far more tractable than an audience problem.

## Does a better hook produce shares? Yes.

Correlations across 22 reels (the 171k outlier removed, and posts under 200 reach excluded
so a single share can't manufacture a 2% rate):

| | r |
|---|---|
| skip rate vs engagement rate | **−0.46** |
| skip rate vs shares/reach | **−0.36** |
| skip rate vs reach | −0.14 |

Split at the median skip rate (43.3%):

| | n | Median reach | Shares/reach | Engagement |
|---|---|---|---|---|
| **Better hooks** (skip < 43.3%) | 11 | **1,155** | **0.492%** | **8.25%** |
| **Worse hooks** (skip ≥ 43.3%) | 11 | 369 | 0.100% | 2.43% |

**5× the share rate. 3.4× the engagement. 3× the median reach.**

And every post that earned 4+ shares had a skip rate under 48% — five of six under 38%:

```
29 shares  skip 32.5%  "Aaaaah yeah so there that"
17 shares  skip 37.3%  "It may cost you nothing, but to me it means everything"
 9 shares  skip 37.8%  "Always make sure you are ready for the job"
 6 shares  skip 32.9%  "Yeah that about sums it up"
 4 shares  skip 47.9%  "Don't be afraid!"
 4 shares  skip 37.5%  "And just like that..."
```

**The low-skip group already hits 0.492% shares/reach — above the 0.3% target.** The
capability is demonstrated. It happens by accident, on the posts that open on something
happening rather than on a product.

**Caveat:** n=22. Correlations of −0.36 and −0.46 at this sample size are suggestive, not
proof. But the direction is consistent, the median split is stark, and the mechanism is
obvious.

## The operating rule this produces

**Get skip rate under 40% and shares follow.** That is a single number, visible per post in
the app, that stands in for the whole strategy.

The pattern separating the two groups: **low-skip hooks open on something happening; high-skip
hooks open on a product.** "Here's a part I got" gives a stranger nothing to resolve in
second one.

FASS at 59% skip becomes *"This $340 part is why your fuel pump died"* — number and problem
in frame one, product second.
