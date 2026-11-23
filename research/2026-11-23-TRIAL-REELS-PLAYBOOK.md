# Trial Reels playbook for @elcoyotediesel (2026-11-23)

Built from Instagram's Help Center and Meta's launch post (searched 2026-11-23), two studied posts (`reel-references/2026-11-23-Dc_qJnCopL_` heyDominik "Trial Reel Ads", `reel-references/2026-11-23-amyjames-trial-reels-carousel`), the Brock digest and algorithm reference from September, and a round of secondhand guides. Tiers: T1 = Instagram or Meta's own pages, T2 = Mosseri quoted secondhand, T3 = creator and vendor blogs.

## 1. Correction to the repo

**Trial Reels are open to this account now.** Help Center "About trial reels on Instagram" (help.instagram.com/1013292530224018), as returned by search on 2026-11-23: a professional (business or creator) account needs at least 200 followers, a personal account needs 1,000. The account is a Creator account at 577 (2026-11-21). The "locked until 1,000" line in CLAUDE.md and the September digest is out of date. Not yet seen with our own eyes: Jacob confirms the Trial toggle on the Reels share screen, and that settles it.

## 2. How it works (T1 unless marked)

- Toggle "Trial" on the share screen before posting. The account must be public and eligible for recommendations; lose recommendation eligibility and the toggle goes away.
- The reel is shown to non-followers only. It does not appear in followers' Feed or Reels tab and stays off the profile grid and Reels tab unless shared to everyone.
- About 24 hours after posting, views, likes, comments and shares show in the reels viewer, with a comparison against earlier trials.
- "Share to everyone" puts the same reel on the grid and makes it eligible for followers. An automatic option shares it if it performs well early (the launch post said within 72 hours on views). The threshold is not published.
- Trials are ranked independently and do not affect the ranking of standard reels. This is what makes them safe to test with.
- Trials can take longer to pick up views, since the audience is cold.
- Scheduling for trials was added in 2026 (T3, two guides, dates disagree).
- No published daily limit. Creators report a cap near 20 a day and a 30-day lockout for going over (T3, unconfirmed). Mosseri, June 2026 Q&A (T2): ten a day "is a lot".
- Duplicates: Mosseri called duplicate trial reels "a spam vector that we are addressing" (T2, September digest). Variants must be different cuts with different hooks, not the same file with new words.

## 3. What the outside numbers say (weak evidence, treat as direction)

- Meta: 40 percent of creators who tried trials posted more often after; of those, 80 percent saw more non-follower reach (T1 claim, no study behind it).
- One 14-day test on one account (T3): trials got 2.3x the non-follower reach and 0.6x the engagement of normal reels, and more new followers per reel (12.4 vs 8.8).
- No independent data for accounts under 1,000 followers. Our own reads will be the first real numbers.

## 4. Why this fits this account

The audit's finding stands: reach is not the bottleneck, conversion is (45,641 reach to 17 followers in the September window). Trials add cold reach, so on their own they feed the wrong end. They pay off here in three specific jobs:

**Job A, hook test before the main-feed post.** One story, two hooks, each as a trial. The better one at 24 to 48 h becomes the main-feed post (share to everyone, so the views carry). This is the "one variable per post" rule run in parallel instead of in series, and it costs the followers nothing.

**Job B, second life for proven winners.** The 10-mil meme, Harley Trade, the gooseneck loader: re-cut (new open, new length) and run as trials so strangers see the best work without the followers seeing it twice. Different cut every time; never the same file.

**Job C, the recruiting reel ("trial reel ad", heyDominik).** 15 to 25 s to strangers only: name the tribe in the first second, name the itch, tease what the page is, point at the page. Needs Jacob's decision, since his rule is no follow ask ever. Proposed trial-only version: spoken, no burned-in text ask, the word "follow" left out, ending on "it's all on the page". Only worth running after the profile spec is finished, because the profile does the converting.

Sample scripts for Job C (his voice, to be re-said his way):
1. "If you're a 7.3 guy, this page is for you. I'm putting a built 7.3 Powerstroke in a 1959 F600 on a Super Duty frame, and I show what every piece costs. It's all on the page."
2. "If you've ever been told a frame swap is cheap, come look at the receipts. 1959 F600, Super Duty frame, 7.3. Target is the SEMA floor in 2027. It's all on the page."
3. "I order parts for semis all day. Here's what that taught me about building my own truck: the cheap part is never the cheap part. The whole build is on the page."

## 5. Rules for running them

1. Volume: one a day to start, two at most. One-man show; six a day (the Amy James method) is not this account. Never more than two variants of one clip.
2. Variants differ in the footage or the cut and the hook, not only the words on screen.
3. Automatic share OFF. A trial reaches the grid only when Jacob picks it. Winners get shared by hand.
4. Length: Job A matches the planned post (story 60 to 120 s, skit 55 to 70 s, loop 6 to 12 s). Job B loops 6 to 12 s. Job C 15 to 25 s, logged as its own cell, since the 20 to 40 s ban is a main-feed rule.
5. House rules hold: real footage, no grade, one lockup at most, song in-app, El Coyote only, no gate on a trial.
6. Do not trial posts that need the followers to act (the BD tag reel, giveaways, partner thank-yous). Those are for the people already here.
7. Post trials in the AM slot so the 24 h read lands before the PM main-feed post it informs.

## 6. Measuring

- Per trial at 24 h and 72 h: views, sends per reach, skip rate, average watch time, plus Instagram's "vs your other trials" line. Log `trial=1` in posts.tsv (new column) so trials never mix into the main-feed averages.
- Follows cannot be tied to a single reel through the API. Read follower change by day against the days a Job C trial ran; a run of five is the smallest test worth reading.
- Promotion rule for Job A: the variant with the lower skip rate and higher sends per reach wins; ties go to the higher watch share.
- Stop rule: if ten trials in a row sit under the main-feed median for sends per reach and the follower line does not move, drop to Job A only.
- Unknown until tried: whether the Graph API can publish a trial (assume in-app only), and whether trial insights come back through `INSTAGRAM_GET_IG_MEDIA_INSIGHTS`.

## 7. First week (starts the day the toggle is confirmed)

| Day | Trial (AM) | Job |
|---|---|---|
| 1 | Hook B of that day's PM story post | A |
| 2 | 10-mil meme, re-cut to a 6 to 12 s loop with a new open | B |
| 3 | Recruiting reel script 1 (if Jacob approves the trial-only invite) | C |
| 4 | Hook B of that day's PM post | A |
| 5 | Harley Trade re-cut | B |
| 6 | Recruiting reel script 2 | C |
| 7 | Read all six, write one sentence each, pick the job that earned the next week | read |

## Sources

- Instagram Help Center, About trial reels: https://help.instagram.com/1013292530224018
- Instagram for Creators, trial reels: https://creators.instagram.com/blog/instagram-trial-reels
- Meta newsroom, 2024-12: https://about.fb.com/news/2024/12/trial-reels-try-content-non-followers-first-see-what-perfoms-best/
- 14-day single-account test: https://creatorhouse.app/blog/trial-reels-14-day-test-2026
- Mosseri volume quote and reported caps (secondhand): https://lesliemlyon.com/how-many-trial-reels-per-day/ , https://crownmediacreative.com/instagram-trials-growth-tool/
- Eligibility cross-check: https://flowgent.ai/blog/instagram-trial-reels , https://postfa.st/blog/instagram-trial-reels
