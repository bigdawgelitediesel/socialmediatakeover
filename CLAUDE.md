# socialmediatakeover

Growth work for the Instagram account **@elcoyotediesel** ("Jake Dalton") — a
diesel-truck creator account documenting the **"Chief"** F350 build.

## Read this first

Before any strategy, content, or analytics work on this account, read:

- **`analysis/2026-09-15-account-audit.md`** — the full audit. Start here.
- **`data/instagram/README.md`** — dataset layout, API gotchas, how to refresh.

## Account facts (captured 2026-09-15)

| | |
|---|---|
| Handle | **@elcoyotediesel** — "Jake Dalton" |
| Type | Instagram **Creator** (`MEDIA_CREATOR`) |
| IG user ID | `17841415745423249` |
| Followers / Following | **215** / 5 |
| Posts | 53 on profile, **38** retrievable via API |
| Access | Composio `instagram` toolkit, connection `instagram_metic-mutule` |

## The five numbers that matter

1. **290,381 lifetime views**, but **one reel is 90% of them** (260,008 views).
   Baseline without it: **821 views/post**.
2. **45,641 reach → 17 new followers** over 30 days = **0.037% conversion**.
   Reach is not the bottleneck. Conversion is.
3. **Reels are 99.6% of all views.** Static posts average **116 views**. Stop
   making them.
4. **Best post ever: 15.46% engagement** — personal, first-person, and Jake
   replied to nearly every comment. That is the template.
5. **The build content and sponsor posts are the worst performers.** The content
   that performs and the content that pays are currently two different accounts.

## Audience

87% US · 76% male · 51% aged 25–44 · maximally dispersed small-town/rural
(top city has 3 followers). Small but precisely on-target for diesel trucks.
**Best posting window: hours 16–19** in the account's reporting timezone.

## Working notes

- **Never request the `reposts` metric at media level** — it 400s and fails the
  whole batch. See `data/instagram/README.md` for the full gotcha list.
- Account-level engagement metrics return **empty, not zero**, at this follower
  count. Reconstruct from per-post data.
- This repo is the only durable storage — cloud sessions run in ephemeral
  containers. Commit and push anything worth keeping.
