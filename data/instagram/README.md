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
