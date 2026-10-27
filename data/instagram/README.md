# Instagram dataset — @elcoyotediesel

Captured **2026-09-15** from the Instagram Graph API (v21.0) through the Composio
`instagram` toolkit, connection `instagram_metic-mutule`.

## Files

| File | Contents |
|---|---|
| `account-snapshot.json` | Profile, follower counts, publishing quota, and the coverage caveats that matter |
| `posts.tsv` | Per-post joined dataset: 38 posts, Jun 25 – Sep 9 2026, with lifetime insights |
| `follower-demographics.json` | Country / age / gender / city breakdowns |
| `daily-reach-30d.tsv` | Daily reach and net new followers, Aug 17 – Sep 15 |
| `online-followers-hourly.tsv` | Average followers online by hour of day |

## posts.tsv columns

`media_id`, `timestamp_utc`, `format` (REELS / FEED_IMAGE / FEED_CAROUSEL),
`views`, `reach`, `likes`, `comments`, `shares`, `saves`, `interactions`,
`avg_watch_ms` (reels only; 0 for static), `caption_summary`,
**`skip_rate_pct`** (reels only — % who skipped within the first 3 seconds).

## Reading OTHER accounts (added 2026-09-15)

`instagram.com` **profile** URLs are not fetchable — the crawler times out. But individual
**`/reel/<id>/` and `/p/<id>/` permalinks ARE fetchable** via
`COMPOSIO_SEARCH_FETCH_URL_CONTENT`, returning the full caption, hashtags, comment text and
like counts.

Pair it with `WebSearch` using `site:instagram.com/reel <terms>` — Google indexes reel pages
as `Handle on Instagram: "<caption opening>"`, so search alone surfaces competitor hooks, and
snippets return follower counts the profile page won't give up.

## Refreshing this data

Composio tool slugs used, all via `COMPOSIO_MULTI_EXECUTE_TOOL`:

- `INSTAGRAM_GET_USER_INFO` — profile snapshot (`ig_user_id: "me"`)
- `INSTAGRAM_GET_IG_USER_MEDIA` — media list, paginate on `paging.cursors.after`
- `INSTAGRAM_GET_IG_MEDIA_INSIGHTS` — per-post; `metric` must be an array
- `INSTAGRAM_GET_USER_INSIGHTS` — account-level and demographics
- `INSTAGRAM_GET_IG_MEDIA_COMMENTS` — comment threads
- `INSTAGRAM_GET_IG_USER_STORIES`, `INSTAGRAM_GET_IG_USER_CONTENT_PUBLISHING_LIMIT`

### Gotchas that cost time — read before re-pulling

- **`reposts` is rejected at media level** (HTTP 400) and fails the *entire*
  batch it appears in. Media-safe metrics: `views`, `reach`, `saved`, `likes`,
  `comments`, `shares`, `total_interactions`. Reels add
  `ig_reels_avg_watch_time` and `ig_reels_video_view_total_time`.
- **Account-level engagement metrics come back empty**, not zero. Meta silently
  omits them at this follower count. Reconstruct from per-post data.
- Demographics need `period=lifetime` + `timeframe=this_week|this_month`, and
  only **one** `breakdown` per call (country, age, gender, city).
- All metrics in a single `INSTAGRAM_GET_USER_INSIGHTS` call must share a period.
- `day`-period windows are capped at 30 days.
- Hour keys in `online-followers-hourly.tsv` are in the account's reporting
  timezone (day boundary lands at 07:00 UTC), not UTC.

## Refresh 2026-10-06

Followers **228** (was 215). Media count **57** (was 53). Three new posts added to
`posts.tsv`:

| Date | Caption | Format | Views | Reach | Likes | Shares | Saves | Watch | Skip |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-06 | "Who is with me?" | REELS | 246 | 206 | 4 | 0 | 0 | **10.8s** | **32.5%** |
| 2026-09-28 | "...here is a picture of my truck" | FEED_IMAGE | 47 | 24 | 4 | 0 | 0 | — | — |
| 2026-09-16 | "Steel Body baby!" | REELS | 237 | 158 | 1 | 0 | 0 | 6.2s | 45.9% |

**The Oct 6 reel is the best hook this account has ever produced.** 32.5% skip rate ties
the account best and sits well under the 40% operating-rule line; 10.8s average watch time
is **1.6× the account average of 6.8s**. The hook and the body are working.

**It still got 0 shares and 0 saves.** That is the whole gap. Per the skip-rate analysis,
a reel this far under the median should be pulling ~5× the share rate. It pulled none. So
the problem on this post is not attention — it is that nothing in it gives a viewer a
reason to send it to somebody. No rule, no number, no "you need to see this."

The Sep 28 static post (47 views / 24 reach) is the fourth consecutive data point that
static feed posts are dead on this account.

Note the reach ceiling: 206 reach on a 228-follower account after a three-week posting gap.
Reach recovers with cadence; it is not a content problem.

## Refresh 2026-10-07

New reel, 7 hours old. Oct 6 reel numbers re-pulled at ~42h and now settled.

| Date | Caption | Views | Reach | Likes | Cmts | Shares | Saves | Watch | Skip |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-07 | "What do you think? Am I crazy?..." | 142 | 130 | 3 | 0 | **0** | **0** | **12.2s** | **52.8%** |
| 2026-10-06 | "Who is with me?" (settled) | 323 | 273 | 4 | 0 | **0** | **0** | 10.7s | 35.3% |

**The split on the Oct 7 reel is the useful finding.** Skip rate **52.8%** is *above* the
48.2% account average — the worst hook of the recent run. But average watch time of
**12.2s is the highest this account has ever recorded.** Those two facts together mean the
body of the video is strong and the first three seconds are losing half the audience before
they get to it. This is a front-end problem on an otherwise good video, not a bad video.

**Two reels, 465 combined views, 0 shares and 0 saves between them.** The payoff gap
identified on Oct 6 is now a confirmed pattern, not a one-off.

**Posting time is off-window.** Posted 13:24 UTC = **07:24 Mountain**. The audit's best
window is 16:00–19:00 local, i.e. **22:00–01:00 UTC**. Every recent reel has gone up in the
morning. Reach of 130 vs the Oct 6 reel's 273 is consistent with that.

**A vague question in the caption does not generate comments.** "What do you think? Am I
crazy?" drew 0 comments on 130 reach. Open-ended invitations give a viewer nothing specific
to type. A question that names two options, or asks for a number, is answerable.

## Refresh 2026-10-08 — account-record hook, and a clean natural experiment

"The first Gift from my 2011 F350 🙄" posted 2026-10-07 **21:22 UTC = 15:22 Mountain**,
inside the target window. Numbers at ~22h:

| | Oct 7 **evening** | Oct 7 **morning** | Oct 6 | Account avg |
|---|---|---|---|---|
| Posted (Mountain) | **15:22** | 07:24 | 19:13 | — |
| **Skip rate** | **25.0%** 🏆 | 58.6% | 35.3% | 48.2% |
| **Avg watch** | **16.1s** 🏆 | 11.3s | 10.7s | 6.8s |
| Views | **454** | 150 | 323 | 821 (ex-outlier) |
| Reach | **365** | 144 | 273 | — |
| Likes | 6 | 3 | 4 | — |
| Comments | 0 | 0 | 0 | — |
| Shares | **0** | **0** | **0** | — |
| Saves | **0** | **0** | **0** | — |

**Both all-time records.** 25.0% skip rate beats the previous account best of ~32%. 16.1s
average watch time is **2.4× the 6.8s account average** and beats the prior record of 12.2s
set the same day.

**The two Oct 7 reels are a near-perfect natural experiment on posting time** — same day,
same account, same creator, eight hours apart. Evening took **2.5× the reach** of morning
(365 vs 144) and less than half the skip rate (25.0% vs 58.6%). This is the cleanest
evidence yet for the 16:00–19:00 window and it cost nothing to get.

**What the winning hook did:** opened on an inherited grievance ("the first gift from my
2011 F350") rather than on a product or a greeting. Consistent with the skip-rate finding
that low-skip hooks open on *something happening*.

### The remaining gap, now sharply isolated

**Three consecutive reels: 927 views, 782 reach, 13 likes, 0 comments, 0 shares, 0 saves.**

Shares/reach is **0.000%** against a 0.3% target. Attention is no longer the problem — this
account now holds people for 16 seconds and loses only a quarter of them in the first three.
What it does not do is convert that attention into any action:

- **Like rate 1.6%** on the record reel (6 likes / 365 reach), against a 14.80% PERSONAL ER
  historically. People are watching *more* and liking *less*.
- **0 comments** — this one's caption asked nothing at all. The prior one asked "Am I crazy?"
  and also got 0. Vague prompts and no prompt perform identically.
- **0 shares** across the run, which is the metric Mosseri named as governing reach to
  non-followers.

**Diagnosis: the hook problem is solved and the ending problem is untouched.** Every one of
these reels finishes on a vibe rather than on a transferable rule or an answerable question.
See `playbook/02-talking-head.md` ("End every story with a RULE") and the closing lines
drafted in `playbook/06-script-rear-axle.md`.

Note reach is still recovering from the three-week September gap: 365 reach on 228 followers
is 1.6× follower count, against a historical 3.8×.

### Same reel, ~8 hours later — it broke out

| | at ~22h | **now (~30h)** | Change |
|---|---|---|---|
| Views | 454 | **1,302** | **2.9×** |
| Reach | 365 | **1,218** | **3.3×** |
| Likes | 6 | 12 | 2× |
| **Skip rate** | 25.0% | **24.5%** | held |
| **Avg watch** | 16.1s | **16.8s** | held |
| Shares | 0 | **0** | — |
| Saves | 0 | **0** | — |
| Comments | 0 | **0** | — |

**1,218 reach on 228 followers = 5.3× follower count**, above the account's historical 3.8×
and far above anything in the recent run. Instagram is actively pushing this to
non-followers. At 1,302 views it is the account's **best non-outlier reel ever** (prior
baseline: 821 views/post excluding the 260k outlier) and still climbing.

**The finding that matters most: skip rate and watch time HELD while reach tripled.**
24.5% skip and 16.8s watch at 1,218 reach, versus 25.0% and 16.1s at 365 reach. Normally
both degrade as a reel is pushed to colder audiences — the hook stops working on people who
don't know the creator. This one did not degrade. **The hook works on strangers, not just
on followers.** That is the single most valuable thing learned about this account's content
so far, and it is the mechanism the whole conversion problem was waiting on.

**And still 0 shares, 0 saves, 0 comments on 1,218 reach.** Like rate is 0.99%
(12 / 1,218). Instagram distributed this purely on watch-time signal; the engagement
signals that would extend the run are absent. Shares/reach remains 0.000% against the 0.3%
target — at this reach that gap is now ~4 shares' worth of missing signal, not a rounding
error.

**Confirmed, repeatable formula from this reel:**
1. Hook opens on an inherited grievance, something already going wrong — no greeting, no product.
2. Posted mid-afternoon Mountain, not morning.
3. Subject is his own truck.

**Unchanged and now the only open problem:** the video ends without a transferable rule or
an answerable question, so a viewer who watched all 16.8 seconds has nothing to send and
nothing to type.

## Refresh 2026-10-17 — THE SHARES DROUGHT BROKE

Followers **239** (was 230). Three posts since 13 Oct.

| Date | Post | Reach | Likes | Cmts | **Shares** | Saves | Skip | Watch | ER |
|---|---|---|---|---|---|---|---|---|---|
| 10-16 | "The hog for the 7.3 rebuild. This 59 F600 is perfect!" | 276 | 15 | **6** | **7** | **2** | 50.5% | 10.6s | **11.6%** |
| 10-15 | Wheel/tire shout-out to @tirewheelexperts (sponsor) | 179 | 7 | 0 | 0 | 0 | 45.3% | 12.7s | 3.9% |
| 10-13 | Marketplace find, bought for $100 (static) | 123 | 7 | 0 | 1 | 0 | — | — | 8.1% |

### The F600 reel is the first real share event this account has produced

**7 shares on 276 reach = 2.54% shares/reach.** The target in `playbook/02-talking-head.md`
is 0.3%. The account's historical rate is 0.045%. This post beat the target by **8×** and
its own history by **56×**. It also took the first comments (6) and first saves (2) of the
entire October run, for an **11.6% engagement rate** — within reach of the 14.80% PERSONAL
best.

### The two halves of the formula now exist in separate videos

| | 7 Oct reel | 16 Oct reel |
|---|---|---|
| Skip rate | **24.5%** (best ever) | 50.5% (poor) |
| Watch time | **16.8s** (best ever) | 10.6s |
| Reach | **1,218** | 276 |
| **Shares** | **0** | **7** |
| Comments | 0 | **6** |

**The hook governs reach. The subject governs shares.** The 7 Oct reel was opened
beautifully and had nothing to pass on; the 16 Oct reel opened badly and people sent it
anyway, because a $100 Marketplace 1959 F600 bought as a parts hog for a 7.3 rebuild is a
thing a guy forwards to his buddy. Neither reel did both. **Combining them — the 7 Oct open
on the 16 Oct kind of subject — is the whole remaining play.**

Note also that 10-13 (static teaser) and 10-16 (the reel) are the same story in two parts,
and part two is what worked. Sequencing a setup post into a payoff reel is now evidence-backed
on this account.

### The sponsor post ran true to form

The wheel/tire shout-out took the lowest reach of the three and zero shares, which is the
documented sponsor pattern (1.36% ER, 72.5% skip across the prior five). Two things worth
keeping: watch time was **12.7s**, so the people who stayed watched nearly the whole thing,
and ER at 3.9% is almost 3× the sponsor average. The caption led with "I'm in love with
this wheel and tire set up! Huge shout out to…" — the thank-you framing that
`playbook/07-script-tire-wheel-shoutout.md` specifically warns against, rather than the
price-forward open. The post did its job for the relationship; it did not earn reach.

## Refresh 2026-10-20 — the naming reel worked, and double-posting cost a reel

Followers **244** (was 239). Three reels since 18 Oct.

| Posted (MT) | Caption | Reach | Likes | **Cmts** | Shares | Saves | Skip | Watch | ER |
|---|---|---|---|---|---|---|---|---|---|
| 10-18 14:08 | "Top comment in a week names the truck! 59 F600" | 361 | 9 | **8** | 2 | 0 | 49.1% | 8.2s | 6.1% |
| 10-19 16:07 | "Hard to come to this conclusion…" | **456** | **21** | 4 | 2 | 1 | **23.9%** | 12.9s | 6.1% |
| 10-19 17:00 | "I hope you're ready to walk down this road" | 111 | 4 | 0 | 1 | 0 | 64.7% | 3.8s | 4.5% |

### The naming reel set a comment record

**8 comments** beats the previous best of 6. Comments/reach of 2.2% matches the F600
announcement's rate but on 31% more reach. The crowdsourced-name format does what it was
picked to do, and it generated a real decision for Jake rather than just engagement.

Submitted names, with likes: **Clifford ❤️ (2)** · an "I agree with this" reply (2) ·
**Red Bed Betty (1)** · **Big Red Booty Betty / BRBB (1)** · **The Red Baron (1)** ·
**Harrison (1)** · "an ode to Betty Ford" (0) · Skrunt (0). **Betty is the emergent
favourite** — three independent people arrived at a Betty variant unprompted. Contest closes
25 Oct per the caption.

### Second-best skip rate ever

**23.9%** on the 10-19 16:07 reel. The account best is still **21.0%** (24 Jul, "Well it
seemed like a good idea…"); this is second, ahead of the 24.5% from 7 Oct. It also took
**21 likes**, the highest like count in the October run, on 456 reach — the best reach since
the 7 Oct breakout.

### ⚠️ New finding: do not post two reels within an hour

The 17:00 reel went up **53 minutes after** the 16:07 reel and collapsed:

| | 16:07 reel | 17:00 reel |
|---|---|---|
| Reach | 456 | **111** |
| Skip rate | 23.9% | **64.7%** |
| Watch time | 12.9s | **3.8s** |

111 reach is the lowest of any reel in the October run, 64.7% skip is the worst, and 3.8s
is the shortest average watch this account has ever recorded. Both were inside the
16:00–19:00 window, so timing is not the explanation — the first reel was still being
distributed and the second competed with it for the same audience. **One reel per day.**
A second reel does not add a second audience; it splits the first one.

## Correction + refresh 2026-10-22 — the 17 Oct reel is the account's best hook ever

**The 2026-10-20 entry above missed a reel.** A 3-post pull skipped over 17 Oct. Numbers
have also settled upward on several posts since that entry; the table below supersedes it.

| Posted (MT) | Caption | Reach | Likes | Cmts | Shares | Saves | Skip | Watch |
|---|---|---|---|---|---|---|---|---|
| 10-16 13:46 | "The hog for the 7.3 rebuild" | 373 | 20 | 6 | **10** | 2 | 46.6% | 12.1s |
| 10-17 16:49 | **"Glimpse into the past of this old 59 F600"** | **1,284** | 12 | 2 | 0 | 2 | **20.3%** 🏆 | **18.6s** |
| 10-18 14:08 | "Top comment names the truck" | 374 | 9 | **10** | 2 | 0 | 48.8% | 8.2s |
| 10-19 16:07 | "A man's gotta do what a man's gotta do" | **1,354** | **45** | 7 | 4 | 1 | 23.6% | 12.9s |
| 10-19 17:00 | "Ready to walk down this road" | 111 | 4 | 0 | 1 | 0 | 64.7% | 3.8s |

### New account record: 20.3% skip rate

The 17 Oct reel beats the previous best of 21.0% (24 Jul) and takes **18.6s average watch
time**, second all-time only to that same July reel's 26.9s. On **1,284 reach** — far more
than July's — which makes it the strongest hook this account has produced against a cold
audience.

**What it was:** the truck's history. The payoff is in its comments — someone wrote *"I'm
also buddies with that guy. He got it out of Laramie and ended up trading it. Pretty cool
to see someone else putting work into it."* A stranger who knew the truck's previous owner
turned up. Provenance content pulls a local network that build content does not.

### The 19 Oct 16:07 reel tripled after the last check

456 reach → **1,354**. 21 likes → **45**, the highest like count in the run. 57 interactions.
Lesson for future checks: **reel numbers at 24h understate by 2–3×.** Do not call a reel
settled before about 72 hours.

### The double-post finding got worse, not better

The 17:00 reel sat at 111 reach while the 16:07 reel it followed grew to 1,354 — a **12×**
gap between two reels posted 53 minutes apart. One reel per day stands.

### The F600 arc, five reels total

**3,496 reach · 142 interactions · 25 comments · 17 shares.** Against a historical baseline
of 821 views per post, one $100 engine and the donor truck around it produced the best week
this account has had. The sequence — find it → its history → name it → the decision — is the
repeatable structure, not any single reel.

## Refresh 2026-10-23 — the shop dog reel, and a reminder the account used to do better

Followers **247**. Three reels since 19 Oct.

| Posted (MT) | Caption | Reach | Likes | Cmts | Shares | Saves | Skip | Watch |
|---|---|---|---|---|---|---|---|---|
| 10-20 13:50 | "The inside" | 233 | 9 | 0 | 0 | 0 | 41.2% | 7.2s |
| 10-21 17:00 | "Yeah? Can I have a hand? Just for a minute…" | 162 | 4 | 0 | 0 | 2 | 30.2% | 5.9s |
| 10-22 18:35 | **"What a shop dog actually looks like…."** | **1,855** | **120** | 0 | 7 | 0 | 26.6% | 13.1s |

### The dog reel in correct context

**1,855 reach and 120 likes is the best this account has done since August — not its best
ever.** Ranked all-time it is **6th** on reach (behind 171,025 / 3,636 / 3,164 / 3,037 /
2,110) and **4th** on likes (behind 1,241 / 419 / 124). It is nonetheless far and away the
best post of the September–October period, at **7.5× follower count in reach** and a **6.5%
like rate** against a usual ~1%.

**What it did not do: 0 comments, 0 saves.** All the engagement is likes, the weakest
signal. Shares were 7, which is **0.38% of reach** — above the 0.3% target but well below
the 16 Oct F600 reel's 2.68%.

**The honest caution:** a dog reel reaches a general audience, not a diesel-buying one. It
is excellent for momentum and it is genuinely on-brand (a shop dog, not a pet account), but
followers earned this way are less likely to care about fuel systems. Worth repeating
occasionally; not worth becoming.

### The two reels before it are the weak pattern, again

"The inside" (233 reach) and "Yeah? Can I have a hand?" (162 reach) both took **0 comments
and 0 shares**. Both captions are fragments that name nothing and ask nothing. "The inside"
also went up at 13:50, outside the 16:00–19:00 window. This is the same shape as every
other low performer in the file.

### Naming contest — 10 comments, closes 25 Oct

By likes: **Clifford ❤️ (2)** and an "I agree with this" reply (2) are tied at the top; then
**The Fifty-Niner, Red Bed Betty, Big Red Booty Betty (BRBB), The Red Baron, Harrison** at 1
each; **an ode to Betty Ford** and **Skrunt** at 0. Clifford is the top actual name
submission. The Betty family has three separate entries and is the strongest cluster even
though no single Betty leads.

### Note on a past high performer

The 29 Aug **FASS fuel system install** reel took **3,164 reach** — worth revisiting when
picking the next sponsor-adjacent subject, since FASS remains an existing relationship with
no follower minimum.

## Refresh 2026-10-24 — three big reels in one day, and two of my rules need softening

Followers **251**. Three reels on 23 Oct, all of them large.

| Posted (MT) | Caption | Reach | Likes | Cmts | Shares | Saves | Skip | Watch | ER |
|---|---|---|---|---|---|---|---|---|---|
| 10-22 18:35 | "What a shop dog actually looks like" (settled) | **2,545** | 165 | 2 | 17 | 3 | 26.3% | 13.3s | 7.4% |
| 10-23 08:50 | **"Go so hard it even makes me worried."** | **2,521** | **278** | 1 | **18** | **13** | 35.8% | 7.7s | **12.8%** |
| 10-23 15:41 | "Oh yall gonna love this one" (@iidiesel) | 1,266 | 76 | 0 | 3 | 0 | 27.3% | **16.1s** | 6.2% |

**"Go so hard it even makes me worried" is the best-engaging post of the whole period:**
278 likes, 18 shares, 13 saves, **12.8% engagement rate** — within range of the 14.80%
PERSONAL pillar best, on 2,521 reach. Shares/reach **0.71%**, more than double the 0.3%
target. Saves of 13 are the most in the October run by a wide margin.

The dog reel also kept climbing: 1,855 → **2,545 reach**, 120 → **165 likes**, 7 → **17
shares**. Again: reels are not settled before ~72 hours.

### ⚠️ Correction — the 16:00–19:00 window is weaker than this file has claimed

**"Go so hard" was posted at 08:50 Mountain and took 2,521 reach.** That is a morning post
outperforming almost everything in the window. Earlier entries here treated the posting
window as a primary lever on the strength of the 7 Oct morning/evening pair (144 vs 1,218).
That pair is now better explained by the content than the clock. The window remains a
reasonable default from the audience-online data in CLAUDE.md, but **it is a tiebreaker, not
a driver** — do not tell Jake a good reel will fail because of the hour.

### ⚠️ Correction — "one reel per day" was too strong; the real variable is spacing

Two reels went up on 23 Oct **about seven hours apart** (08:50 and 15:41) and both performed
(2,521 and 1,266 reach). The 19 Oct collapse involved two reels **53 minutes apart** (1,354
vs 111). The rule should be **leave several hours between reels**, not one per day.

### What the last week actually shows

Nine reels since 17 Oct. The five that cleared 1,200 reach each had a clear subject — the
truck's history, the decision, the dog, the "go so hard" moment. The four that died
("The inside" 233, "Can I have a hand?" 162, "walk down this road" 111) had fragment
captions naming nothing. **Subject clarity is the variable that keeps showing up, not
timing.**

## Refresh 2026-10-26 — third-best reach ever, and ask-posts measured

Followers **262** (was 251, +11 in two days — the best two-day gain on record).

| Posted (MT) | Caption | Reach | Likes | Cmts | Shares | Saves | Skip | Watch |
|---|---|---|---|---|---|---|---|---|
| 10-23 08:50 | **"Go so hard it even makes me worried."** | **3,329** | **354** | 1 | 19 | 19 | 39.2% | 7.7s |
| 10-22 18:35 | Shop dog | 2,545 | 170 | 2 | 17 | 3 | 26.3% | 13.3s |
| 10-23 15:41 | "Oh yall gonna love this one" (@iidiesel) | 1,307 | 78 | 0 | 3 | 0 | 28.4% | 16.1s |
| 10-24 13:45 | **"I need your help!"** | 1,064 | 68 | 4 | **0** | 1 | 32.5% | 15.0s |
| 10-25 10:33 | **"Would love your support…"** | **229** | 32 | 2 | 1 | 0 | 40.7% | 6.2s |

**"Go so hard" is the account's third-best reach ever** (171,025 / 3,636 / **3,329**) and
third-best likes (1,241 / 419 / **354**). 19 shares and 19 saves, a **12.3% engagement
rate** on 3,329 reach. It is the best non-outlier post this account has produced.

### ⚠️ Ask-posts measured: they do not travel

Two posts this week asked the audience for support rather than giving them something.

| | Reach | Shares | Saves |
|---|---|---|---|
| "Go so hard" (subject) | **3,329** | 19 | 19 |
| "I need your help!" | 1,064 | **0** | 1 |
| "Would love your support…" | **229** | 1 | 0 |

**"Would love your support" took 229 reach — roughly the follower count, meaning it reached
almost no non-followers at all,** two days after a 3,329-reach post. It is the lowest-reach
reel since the 19 Oct double-post collapse. "I need your help!" held 15.0s of watch time and
still took **zero shares**.

The mechanism is simple: an ask gives a viewer nothing to pass on, so sends/reach goes to
zero, and sends/reach is the signal Mosseri named as governing distribution to non-followers.
These posts are shown to existing followers and stop there.

**They are not neutral — they spend momentum.** The account went 3,329 → 1,064 → 229 across
three consecutive posts as the subject drained out of them.

Note on the +11 followers: media-level `follows` does not exist (see Open Items in
CLAUDE.md), so no post can be credited. The 3,329-reach reel is the likeliest driver on
reach alone, but this is inference, not attribution.

### Bearing on the planned Industrial Injection series

Jake wants a "Day One of pitching Industrial Injection" series. The ask-post data above is
the direct evidence for the warning already given: **a series built as "Day X of asking"
is the same genre as "I need your help!" and will behave the same way** — reach confined to
existing followers, near-zero shares, momentum spent.

The series only works if every episode carries a subject that stands on its own (a real
build step, a real reason, a real number) and the pitch is the frame around it rather than
the content of it. See `playbook/07-script-tire-wheel-shoutout.md` for the same principle
applied to sponsor content.

## 2026-10-27 — VIRAL. 182,141 reach, 8,303 shares, and the conversion problem at full scale

Followers **342** (was 262, **+80**). A reel posted 26 Oct 17:00 MT went wide.

| | "Yo! Where the 10 mil @?!" |
|---|---|
| Views | **226,847** |
| Reach | **182,141** |
| Likes | **33,968** |
| Comments | 34 |
| **Shares** | **8,303** |
| Saves | **1,676** |
| Interactions | **46,088** |
| Engagement rate | **25.3%** |
| Skip rate | 35.3% |
| Watch | 8.0s |

**Shares/reach is 4.56%** — against a 0.3% target and a 0.045% account history. That is
roughly **100× the historical share rate** and the single best signal this account has ever
produced. Reach exceeds the July 2026 outlier (182,141 vs 171,025), making this the biggest
post in the account's history.

### ⚠️ The sobering half: 182,141 reach produced 80 followers

**0.044% conversion.** The CLAUDE.md baseline is 0.037%. **Virality did not fix the
conversion problem — it restated it at 400× the scale.** This is the second time the account
has been handed six-figure reach (Jul 2026: 171,025 reach) and converted almost none of it.

### This audience is not the diesel audience

Comments on the viral reel reference DrDisrespect, "burnt peanut", gaming and meme culture:
*"It's ironic because fan base is DrDisrespects fans"*, *"Dude not even funny with his 12
year old fan base"*, *"I'm from Israel and I LOVE burnt peanut"*, *"FB25 POWERRR"*. Only one
comment is trade-adjacent (a lube tech). **The reel traveled on a meme, not on diesel.**

**Likes-to-comments is 999:1.** That ratio is characteristic of passive scroll-by consumption
rather than an audience that cares who posted it.

### The static post that followed reached 64 accounts

A FEED image went up 27 Oct 03:56 MT, hours after the viral reel, and reached **64**. With
the account's distribution at its hottest point ever, the next thing posted was the format
that performs worst here. The 7.3 build questions in its caption are good content in the
wrong wrapper.

### What this makes urgent

1. **The profile is the leak.** 182,141 people looked and 80 followed. Bio, pinned grid and
   the first three reels a visitor sees are now the highest-leverage thing on the account.
2. **The next 48 hours carry inflated distribution.** What gets posted now decides how much
   of the lift is retained — it should be the F600 7.3 build, in reel form, so the traffic
   sees what this account actually is.
3. **Do not chase the meme.** Reach of this kind is not repeatable on demand and the audience
   it brings does not buy fuel systems. The 23 Oct reel (3,329 reach, 12.3% ER, diesel
   audience) is still the more valuable template.

## Refresh 2026-10-27 ~21:00 UTC (local session)

Followers **384**. Media count 78. Viral reel re-pulled at ~22h; new reel pulled at 35 min.

| Date | Caption | Views | Reach | Likes | Cmts | Shares | Saves | Watch | Skip |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-27 20:25 | "You know when the build just isn't going as quickly..." (35 min) | 1,228 | 726 | 94 | 1 | 0 | 0 | 6.4s | **20.3%** |
| 2026-10-27 03:56 | 7.3 build carousel "where do I get this machined" | 166 | 81 | 6 | 0 | 1 | 0 | — | — |
| 2026-10-26 23:00 | "Yo! Where the 10 mil @?!" (22h, still climbing) | 342,222 | 284,911 | 50,358 | 81 | 11,273 | 2,550 | 8.1s | 36.6% |

- Viral reel grew from 182,141 to 284,911 reach in the ~3h between the cloud log and this pull. Share rate 3.96% of reach, interactions 23.6% of reach.
- Daily account reach: 31,543 (bucket ending 10-26 07:00 UTC) then **251,644** (bucket ending 10-27 07:00 UTC). Daily `follower_count` lags; the last bucket reads 0 while the profile shows 384. Use the profile number.
- New reel: **20.3% skip rate is the lowest in account history** (prior best 28.4%). 726 reach in 35 min is roughly 10x the normal first-hour pace. Views/reach 1.69 = replays. Zero shares and saves at pull; the share column decides whether it travels.
- The carousel reached 81 while sitting directly under a 285k-reach reel. Static is dead even with a hot profile.
