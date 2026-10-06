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
