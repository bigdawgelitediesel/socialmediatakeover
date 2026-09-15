# Build Your Tribe — video index

Channel: [@BuildYourTribePodcast](https://www.youtube.com/@BuildYourTribePodcast)
Channel ID: `UC8eDDKjBAUWjXGDTimwPVQA` · **1,018 videos** enumerated 2026-09-15 (21 pages, no gaps).

Host of the Instagram material is **Brock Johnson** (Chalene Johnson's son). He publishes
Instagram strategy content roughly weekly.

## What the full set looks like

- **437** videos have "Instagram" in the title — but ~140 of those are 2022-era hashtag
  shorts (`#instagramstrategy`, `#instagramgrowth`) with no real content.
- **107** more cover Instagram growth without the word in the title (hooks, reels,
  algorithm, followers, stories, carousels).

Transcribing all 437 is waste. `build-your-tribe-index.tsv` holds the **48 that matter**,
priority-ranked, all from 2025–2026.

## Priority tiers

- **1** — the ten to transcribe first. Recent, substantive, directly on the problems this
  account has: hooks, retention, algorithm changes, why viral posts don't convert.
- **2** — second wave. Algorithm updates, editing, shares, going from zero.
- **3** — reference. Trial Reels (locked until 1k followers), SEO, shadowban, the Mosseri
  interview episodes.

## How to pull transcripts

Requires the Composio `youtube_transcript` toolkit (a **separate** connection from the
`youtube` Data API toolkit — connecting one does not connect the other).

```
COMPOSIO_MANAGE_CONNECTIONS toolkits=[{"name":"youtube_transcript","action":"add"}]
# then, max 10 ids per call:
YOUTUBE_TRANSCRIPT_GET_VIDEO_TRANSCRIPTS_BATCH
  video_ids=[...], language="en", source="auto"
```

## ⚠️ One thing to skip

This channel has an episode promoting **Instagram engagement pods**. Pods are a Terms of
Service violation with real ban risk, and they are mechanically self-defeating now that
every ranking signal Mosseri named is a per-reach *ratio*. Take the rest of the channel;
ignore that.
