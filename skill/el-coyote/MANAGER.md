# MANAGER mode

Everything between a finished render and a logged 48 h read, plus the account's daily and weekly upkeep. Account facts and API gotchas: repo `CLAUDE.md` and `research/inventory/01-playbook-data-analysis.md`.

## Access

Composio `instagram` toolkit, connection `instagram_metic-mutule`, account `@elcoyotediesel` (IG user id `17841415745423249`, creator account, Instagram Login path). Everything is scoped to this account: no business_discovery, no other accounts, no DMs initiated (replies only inside 24 h), no audio via API. Media insights work at this follower count. Never request `reposts` or `profile_visits` at media level (400s the batch). Account-level engagement metrics come back empty, rebuild from per-post data.

## The pull (one call, then grade)

```
INSTAGRAM_GET_IG_USER_MEDIA
  ig_user_id: "me", limit: 20,
  fields: "id,caption,media_type,media_product_type,permalink,timestamp,like_count,comments_count,insights.metric(views,reach,saved,shares,total_interactions,ig_reels_avg_watch_time,reels_skip_rate)"
```
Save the response as JSON (scratchpad), then `python -I tools\coyote.py grade <file> --log` (add `--durations d.json` with `{media_id: seconds}` when you know lengths; watch share needs it). It prints the table with sends per reach, skip, watch, likes per reach and a grade (GOAL 2 percent, FLOOR 1 percent, MISS), appends `data/instagram/reads-48h.tsv`, adds new rows to `posts.tsv`, and clears pending reads that are past 44 h.

Single reel: `INSTAGRAM_GET_IG_MEDIA_INSIGHTS` with `metric: ["views","reach","saved","likes","comments","shares","total_interactions","ig_reels_avg_watch_time","reels_skip_rate"]`.

Account 30-day: `INSTAGRAM_GET_USER_INSIGHTS` period=day, 30-day windows; `follows_and_unfollows` with `breakdown=follow_type` (FOLLOWER gained, NON_FOLLOWER lost). Demographics need `period=lifetime` + `timeframe`, one breakdown per call.

## Caption (every post)

1. Line 1 names a person type and is the sentence a sender would type. Formats that have shared on this account and in the niche: "Send this to your 7.3 brother", "For whoever is pulling a cab off a 67 year old frame this weekend", "Every service writer has this customer. Send it to yours", "7.3 guys, this one's for you". The tribe name in the first five words when the reel is tribe news.
2. Lines 2 to 4: the fact, the cost, the failure, in his voice. One real number. No "it's not X, it's Y", no negation lists, no colon reveals, no "read that again", no em-dashes.
3. No follow ask ever. A comment gate only when a real deliverable exists (PDF, list, link, the nine prompts), spelled as `Comment WORD and I'll send you <thing>`, at most one post in four, never on a fast-tier meme.
4. Five hashtags max, never in line 1. Partners get a tag in the caption and a Collab invite when the reel is built to be sent; never a hard sell.
5. `python -I tools\coyote.py lint caption "<text>"` must say SHIP. Fix, do not bypass.
6. Pinned comment repeats the person type. Story share uses the same line.

## Posting kit (`README - posting kit.txt` in the Drive folder)

Caption (line 1 first), song and downbeat offset (song added in-app), cover frame, slot (AM 09:00 to 11:00 MT for memes, skits, rollers, question clips; PM 16:00 to 19:00 for build, credential, story; the 11-03 note in data/instagram/README.md preferred 8 to 10 and 13 to 15 and avoided 16 to 20, so log the posted time on every read and let day 15 settle it), Trial Reel yes/no with the two caption first lines to test, pinned comment, Story line, the one variable this post tests, partner tags and Collab invite, "do not" list (no in-app filters, no text added in-app, no trending-template overlays). CapCut or Edits finishing: 1080p30 H.264 16,000 kbps, share to Instagram from the app, never download and re-upload. After it is live: `coyote.py pending add <media_id> "<label>" <posted_iso>`.

## Publishing through the API (only when he asks)

`INSTAGRAM_POST_IG_USER_MEDIA` (video_url must be public, media_type REELS, caption, cover) then `INSTAGRAM_POST_IG_USER_MEDIA_PUBLISH`. Audio cannot be attached by API, so anything with a song is posted in-app by Jacob. Quota 100 per 24 h.

## Replies, DMs, partners

- Comments: he answers; replying to nearly every comment on a post was the best follower driver the account ever had (June 2026). Flag posts with comments above likes (argument or gated lane).
- DMs: replies only, 24 h window. Partner threads are cold by default; the warm ones and owed replies live in memory (`reference_strictly_diesel_dennis` owes a reply; `reference_bd_diesel_pt`, `reference_scott_dana_industrial_injection`, `reference_power_hungry_performance`, `reference_isspro`, `reference_axiom_supply`, `reference_cnc_fabrication`). Never give out the shop name on Rival threads; his phone is fine in partner emails.
- Thank-yous go to Story, not the grid (shout-out reels run 195 to 347 views, 66 to 75 percent skip, 0 shares). A partner part appears as the payoff of a real episode, spoken, with a Tag pill at most.
- Collab invites on reels built to be sent; sponsored Collabs reach 1.00x vs 0.78x for plain sponsored posts; organic Collabs 1.52x.
- Repostability kit for partners: 12 files (vertical master, cover, three stills, caption, credit line), from `research/2026-11-21-partner-repostability.md`.

## Weekly and monthly

`coyote.py week` prints the Monday list. Monthly: profile spec (name field `Jake Dalton | 7.3 Diesel Builds`, bio first line "Building a 1959 Ford F600 on a 7.3 Powerstroke", no shop line, pins Harley Trade + "Why companies hate your truck" + the current Rival episode, highlights RIVAL / PARTS / CHIEF / JAKE, cover on every reel), `site/media-kit.html` numbers, F600 portal partner numbers (that repo: `git fetch` first, builder voice, run build.mjs and deploy).

## Cross-posting (decided 2026-11-21, made mandatory the same afternoon by the million-view rule)

Every post goes to TikTok and YouTube Shorts the same day as Instagram, from the same master (the millions in the watch list are TikTok and YouTube; DriveHub's 14K-median channel got 5.76M on Shorts). Shorts via Buffer Free or by hand, Facebook toggle on. Instagram is the home; nothing is edited differently for the mirrors. The posting kit lists all three with the same caption line 1. YouTube channel exists for the Shorts mirror and milestone episodes only (`research/2026-11-21-youtube-decision.md`).
