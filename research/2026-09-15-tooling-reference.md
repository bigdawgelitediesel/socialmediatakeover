# Tooling Reference — what this environment can and cannot do

**Compiled 2026-09-15.**

## THE BIG ONE: Instagram publishing already works

Live introspection found publishing tools that were not previously known to be available.
**Nothing needs to be installed to publish to this account right now.**

| Tool | What it does |
|---|---|
| `INSTAGRAM_POST_IG_USER_MEDIA` | Creates the media container. Accepts `video_url`/`image_url`, `media_type` ∈ {REELS, CAROUSEL, STORIES}, `caption`, `cover_url`, `share_to_feed`, `user_tags`, `location_id`, `alt_text`. Also accepts `video_file`/`image_file` — **Composio hosts the file for Meta to fetch**, removing the public-URL requirement. |
| `INSTAGRAM_POST_IG_USER_MEDIA_PUBLISH` | Publishes it. Auto-polls for FINISHED. Error 9007 = published too early. |
| `INSTAGRAM_CREATE_CAROUSEL_CONTAINER` | One-shot carousel, 2–10 items. |
| `INSTAGRAM_POST_IG_COMMENT_REPLIES` | Reply to comments. ≤300 chars, ≤4 hashtags, ≤1 URL. |
| `INSTAGRAM_POST_IG_MEDIA_COMMENTS` | Comment on own media (pinned-first-comment pattern). |
| `INSTAGRAM_GET_IG_COMMENT_REPLIES` | Needed to detect unanswered threads. |

**The comment-reply loop is fully automatable today with zero new tooling:**
`GET_IG_USER_MEDIA` → `GET_IG_MEDIA_COMMENTS` → `GET_IG_COMMENT_REPLIES` → diff for
unanswered → draft → **human approves** → `POST_IG_COMMENT_REPLIES`.

## Hard API limits worth knowing

- **No trending/licensed audio via API.** Reels published through the API carry original
  audio only. Trending sounds must be applied in-app before export. **This is permanent —
  design the workflow so the API handles everything up to export and a human does the sound.**
- **No interactive Story stickers** (polls, questions, link stickers, music).
- **No native scheduling endpoint.** Every scheduler implements its own timer. Since this
  container is ephemeral, scheduling requires an external service.
- **No editing after publish.** Captions and media are immutable.
- **Cannot initiate a DM** — replies only, inside a 24-hour window (7 days with the
  HUMAN_AGENT tag). Fails with `error_subcode 2534022` outside it; do not retry.
- **Publishing quota: 100 posts per rolling 24h.** Irrelevant at this cadence. Read live
  with `INSTAGRAM_GET_IG_USER_CONTENT_PUBLISHING_LIMIT`.
- **Never request `reposts` at media level** — 400s and fails the entire batch.
- Reels: MP4/H.264/AAC, 9:16, 1080×1920, ≤1GB. ⚠️ Sources disagree on the length ceiling
  for Reels-tab eligibility (90s vs 3min) — verify before planning around it.

## Instagram Login vs Facebook Login

This account is on **Instagram Login** (`graph.instagram.com`). That costs:
**Hashtag Search**, **Business Discovery** (public competitor profiles + recent media), and
**tagged media**. Switching to Facebook Login unlocks them but requires a linked Facebook
Page and a re-auth. Worth it only when competitor benchmarking becomes a real workstream.

⚠️ A Composio tool description claims media insights need 1,000+ followers. **That is
wrong** — this repo pulled per-post insights at 215 followers. Don't let it stop a call.

## Working around the egress block

`WebFetch` is blocked environment-wide. **`COMPOSIO_SEARCH_FETCH_URL_CONTENT` is not** —
it routes through Composio and successfully fetched `creators.instagram.com`, which the
local proxy blocks. It requires no authentication. **Use it for all web research.**

## Connected vs available

**Connected now:** `instagram` · `composio_search` (no auth needed) · `youtube` (Data API) ·
Gmail, Google Calendar, Google Drive, Slack, GitHub.

**One `COMPOSIO_MANAGE_CONNECTIONS` call away** (no MCP install needed):
`youtube_transcript` · `tiktok` · `groqcloud` (transcription ~$0.02/hr) · `openai` ·
`buffer` · `ayrshare` · `hypeauditor`.

## Recommended additions, ranked

1. **`youtube_transcript`** — pending. Needed for creator-education research.
2. **A persistent scheduler — Buffer MCP or Metricool MCP, both free-tier.** Both are
   official vendor-maintained MCP servers with OAuth and Instagram Reels support. This is
   the one gap the Graph API structurally cannot close. Postiz (AGPL, self-hosted) if the
   token should never leave your infrastructure.
3. **`youtube` Analytics for the retention curve.** Not for YouTube's audience — for
   **audience-retention data**, the single most valuable metric Instagram refuses to
   expose. Cross-post the same 9:16 file as a Short and you finally learn *where* viewers
   leave.
4. **`groqcloud` + local ffmpeg** for auto-captions. ~$0.02/hr of video. Captions lift
   watch-through on muted autoplay, which is most of the feed.

**Do NOT add:** community Instagram MCP servers (0–24 stars, duplicate Composio, hold
publish rights) · Hootsuite/Sprout ($249/mo+ at 215 followers) · any `JUST_ONE_API_*` or
scraper-backed tool Composio's search suggests.

## Metrics the API will never give you

- **Per-second retention curve.** You get `reels_skip_rate` and `ig_reels_avg_watch_time` —
  two scalars, not a curve. In-app only. (YouTube Analytics *will* give you this.)
- **Follower attribution per post.** You can never say "this reel got 9 of the 17 follows."
- **Non-follower vs follower reach split** — in-app only.
- **Historical backfill.** Insights cap at 2 years and cannot be fetched retroactively for
  a metric you didn't record. **This is why `data/instagram/` matters — the repo is the
  only long-horizon store.**
- Rejected by Meta, never request: `impressions`, `email_contacts`, `phone_call_clicks`,
  `text_message_clicks`, `get_directions_clicks`.

## Not yet instrumented — add these

Media-level insights expose **`follows`**, **`profile_visits`** and **`reels_skip_rate`**,
which are missing from `posts.tsv`. Add them to the metric array (test in an isolated batch
first) and backfill. These are the two headline numbers the content plan measures against.

## Policy risk register — do not use

**Engagement automation** (auto-like/follow/comment, cold mass DMs, pods, bought
followers) · **private APIs** (`instagrapi`, `instagram-private-api` — these get accounts
challenged and banned) · **scraper services** (Apify IG Scraper, Bright Data, SocialCrawl,
`JUST_ONE_API_*`).

**Fine and encouraged:** publishing your own content via the Graph API; replying to
comments and DMs you received at human cadence; reading your own insights; official-API
schedulers.

**Grey zone:** AI-drafted comment replies are permitted — it's your account, your API. But
volume and sameness trip spam detection, and the 15.46% post worked *because the replies
were personal*. Draft-then-human-approve preserves both.
