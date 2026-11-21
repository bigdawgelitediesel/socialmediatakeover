# Measurement protocol (2026-11-21)

What we read, when, and what each number decides. Built from Mosseri's Oct 23 2026 ranking order (sends per reach, likes per reach, average watch time), the 600-clip share measurement (research/2026-11-21-share-engineering.md), the Nov 2026 benchmarks (research/2026-11-21-live-instagram-algorithm.md section 2) and this account's own 20-post pull (analysis/2026-11-21-live-pull-20-posts.md). It extends the Sept rule "get skip rate under 40 percent and shares follow": skip is now solved on the good cuts, so sends are the grade.

## The 48-hour read (every reel)

Pull at 48 h, log in the reel's project folder README and in `data/instagram/posts.tsv`:

| Metric | Source | Formula | Floor | Goal | If it misses |
|---|---|---|---|---|---|
| Sends per reach | `shares` / `reach` | the growth signal | 1.0 percent | 2.0 percent | the format failed (trigger or recipient), not the footage: change who the reel is for and the caption line 1 |
| Skip rate | `reels_skip_rate` | | under 45 | under 35 | first 2 s: open on a person or a move, never a product or a thank-you |
| Average watch | `ig_reels_avg_watch_time` / length | | 50 percent | 60 percent | second promise missing: add the re-hook at 9 to 10 s or cut the length |
| Likes per reach | `likes` / `reach` | | 3 percent | 6 percent | low with high sends is fine; low with low sends means the reel is vanilla |
| Saves | `saved` | | | | high saves with low sends = education; wrap the tip in a tribe or argument frame |
| Comments | `comments` | | | | weakest signal per Mosseri; only matters on a gated reel (comments should exceed likes there) |

Baselines on this account (Nov 2026): memes 1.5 to 2 percent sends, skip 30 to 45; build reels before 11-20: 0 sends, skip 60 to 75, 200 to 500 views; Harley Trade (new renderer): skip 37.8, watch 59 percent, sends 0.06 percent.

## Weekly read (Mondays)

1. Account: followers, 30-day reach, profile visits per 1,000 reach (Insights, by hand; not available per reel), follows per 1,000 reach.
2. Top 3 and bottom 3 reels of the week by sends per reach; one sentence each on why.
3. Trending audio in this order: Professional dashboard Trending audio, Ignix weekly list, CreatorDB for the format each sound carries (research/2026-11-21-audio-trends-and-voice.md).
4. THE BAR weekly re-pull (research/reel-references/2026-11-21-the-bar-weekly/WEEKLY.md format).
5. Trial Reels: if the composer shows the toggle, every build reel goes out as a Trial first with two caption first lines; the winner is shared to followers after 24 h.

## How to pull (Composio, Instagram toolkit, connection instagram_metic-mutule)

One call for the last 20 posts with nested insights (no per-post calls, never request `reposts` or `profile_visits` on reels):

```
INSTAGRAM_GET_IG_USER_MEDIA
  ig_user_id: "me", limit: 20,
  fields: "id,caption,media_type,media_product_type,permalink,timestamp,like_count,comments_count,insights.metric(views,reach,saved,shares,total_interactions,ig_reels_avg_watch_time,reels_skip_rate)"
```

Then in the workbench: for each post, `m = {d.name: d.values[0].value for d in post.insights.data}`; sends per reach = `m.shares / m.reach`; watch share = `m.ig_reels_avg_watch_time / 1000 / duration`. The 2026-11-21 table in analysis/ is the template.

Single reel: `INSTAGRAM_GET_IG_MEDIA_INSIGHTS` with `metric: ["views","reach","saved","likes","comments","shares","total_interactions","ig_reels_avg_watch_time","reels_skip_rate"]` (Harley Trade media id 18146810329717837).

## Post-publish technical check

Download the posted reel with yt-dlp (`yt-dlp.exe https://www.instagram.com/reel/<id>/`), run `tools/smooth_check.py` on it, compare against the master (libvmaf when needed), and log any difference Jacob's finishing pass introduced (research/2026-11-21-capcut-edits-finishing.md handoff rules). Fold repeated differences into the rules.

## Change one thing per post

A reel is an experiment with one variable: the hook move, the caption first line, the length, the format. Two variables changed means nothing was learned. Trial Reels make this cheap once unlocked.
