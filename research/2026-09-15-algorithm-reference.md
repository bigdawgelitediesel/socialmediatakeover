# Instagram Algorithm Reference

**Compiled 2026-09-15.** Claims are graded: **[T1]** = traceable to Instagram/Mosseri or
major outlet reporting them; **[T2]** = widely repeated across marketing blogs, no primary
source found. Do not cite T2 as "Instagram says."

> Research caveat: `WebFetch` is blocked by this environment's egress proxy. However
> **`COMPOSIO_SEARCH_FETCH_URL_CONTENT` does reach blocked domains** (verified against
> creators.instagram.com) — use it to re-verify anything load-bearing.

## The three ranking signals [T1]

Mosseri, January 2025:
> "Pay close attention to **average watch time, likes per reach, and sends per reach**."

and:
> "**Likes are slightly more important for connected content, and sends are slightly more
> important for unconnected content.**"

**All three are ratios per reach, not volumes.** Note "slightly" — the widely-repeated
"sends are 3–5× likes" multiplier is **[T2]** and contradicts Mosseri's own wording.

Watch time is not a pure completion race [T1]:
> "We don't want to penalize longer videos, which is why we look at not only the percentage
> of a video that was watched, but also the number of seconds."

**Saves are NOT in the named top three.** If forced to choose, optimize sends over saves.

## Direct Mosseri quotes from the April 2025 interview [T1]

From Brock Johnson's on-the-record hour with Adam Mosseri. These are first-party and were
missing from this doc until 2026-09-15.

**What the algorithm actually reads — the most useful quote in the whole corpus:**
> "Right now, it's disproportionately looking at the **caption** relative to the **video**,
> relative to the **audio**, relative to the **comments** — in that order. But that's going
> to change because as we get better at understanding all the pieces, we'll integrate them."

**Caption is weighted above the video itself.** Write captions as if they are the primary
input, because right now they are.

**On shares vs saves:**
> "I think shares, at least algorithmically speaking, of course they're helpful, but it's a
> human sending a post to another human. So even if the algorithm was optimized for saves,
> a share would still be the way to reach another human being."

Note the framing — a *mechanical* argument (a share physically delivers the post to a
person), not a claim about ranking weight.

**On "warming up the algorithm" by engaging before you post:**
> "Not directly. Indirectly, it could happen, right? Cuz if you're on there a bunch…"

**Kills the "engage for 15 minutes before posting" folklore.**

**On whether consuming off-niche content hurts your own distribution:** "Not necessarily."

**On shadowbanning:**
> "It's possible if you write really aggressive content… it might get caught up in, oh, this
> isn't harassment, but it's borderline. It's aggressive and we won't recommend it."

**On reach being down:** "In general, reach is going up for some people and down for other
people. It's much more of a blend."

**On posting many stories in one day (a fix, not a penalty):**
> "People were complaining about getting less reach with their stories if they posted lots
> of stories in the same day. And that is not at all the intended behavior… we've addressed
> the issue."

**On sharing feed posts to stories:**
> "We don't suppress stories about new posts, but in general those kinds of stories are
> often not quite as interesting as other stories."

Not a penalty — a content-quality effect.

**On duplicate trial reels:**
> "Don't try to use them just to pummel the same content over and over and over again.
> We're trying to crack down on that. That's become a bit of a spam vector."

## How small accounts get distributed [T1]

Instagram seeds content to a **small test audience** who may be interested — follower or
not — then expands the top performers, repeating. The stated 2024 intent was to stop large
accounts and reposters monopolizing reach and surface smaller original creators.
Reposted content is removed from recommendations in favor of the original.

**Implication:** @elcoyotediesel gets ~3.8× its follower count in views per post. The
unconnected pipeline already works. Gate 1 (escape velocity) is passing; Gate 2
(reach → profile visit → follow) is failing. No ranking change fixes Gate 2.

Per-surface algorithms: Feed, Stories, Explore and Reels each rank differently. Reels and
Explore are recommendation surfaces where most content is from unfollowed accounts.

## Reel length — sources genuinely conflict

| Finding | Sample | Source |
|---|---|---|
| 45–60s highest engagement, ~2× the views of sub-30s | ~140,000 reels, business accounts | Socialinsider 2026 |
| 12–18s best for most niches; 15s cohort hit 78% median completion | 50 reels, Apr 2026 | CreatorHouse |
| 7–15s entertainment, 20–35s educational | — | OpusClip |

The large study measures *business accounts* and *engagement rate*; the small one measures
*completion and reach for a small account*. For an account with 6.8s average watch time,
the small-sample finding is the relevant one — you have not earned the right to make 60s
reels yet.

**Recommendation eligibility caps at 3 minutes** [T1] — longer reels stay inside the
follower graph. Raised from 90s in January 2025.

**Retention benchmarks [T2]:** ~60–80% for a 15s reel, ~40–60% for a 60s reel.

## Confirmed 2025–2026 changes

| Date | Change | Grade |
|---|---|---|
| Dec 2024 | Hashtag *following* removed | T2 |
| Dec 2024 | **Trial Reels** launched | T1 |
| Jan 2025 | Reels max length → 3 min, recommendation-eligible | T1 |
| **Jan 2025** | **Mosseri names the three signals** | T1 |
| **Apr 2025** | **Impressions and Plays deprecated; Views becomes the unified metric — and counts replays** | T1 |
| Mid-2025 | Trial Reels gated to **1,000+ followers** | T1 |
| **Dec 2025** | **Hashtags capped at FIVE per post**, down from 30 | T1/T2 |
| Dec 2025 | Mosseri year-end memo: "the polished, perfect aesthetic is dead"; raw/human favored over AI-generated | T2 |
| 2025–26 | **10+ reposts in a rolling 30 days → excluded from recommendations entirely.** Credit/attribution does not make a repost original | T2 |
| Apr 2026 | Anti-aggregator policy extended from Reels to photos and carousels | T2 |
| Jun 2026 | Meta tests **"Series"** — episodic Reels with a profile hub and Watch Next. Limited test only | T1 |

**Views counts replays.** A lifetime "290,381 views" figure is plays-including-loops, not
290,381 humans.

## Myths

**Shadowbanning** — half myth. Mosseri: *"There's no official shadow banning program, but
we are going to limit the reach of certain accounts… if you're posting content that's
violating our community standards or our recommendability standards."* The mechanism
(recommendation ineligibility) is real and **checkable**: Settings → Account → **Account
Status**. Avoid the entire third-party "shadowban checker" industry — most sell engagement
services.

**Hashtags** — Mosseri has repeatedly said they don't meaningfully increase reach; the
ceiling is "ever so slightly on the margins." Capped at 5 since Dec 2025. Replaced by
keyword/semantic search over **handle, name field, bio, captions**, plus alt text and
transcribed audio.

**Posting frequency** — the "posting too much hurts you" claim is false. Each post is
ranked on its own merits. The real cost of volume is quality decay, not penalty.

**Posting time** — real but third-order. Cherry, not cake.

**Paid Partnership label** — Mosseri says it is not an algorithmic penalty. Claims that it
now gets a *boost* have no primary source; disbelieve them. Sponsor posts underperform for
content reasons, not labeling.

## Accounts under 1,000 followers

There is **no confirmed under-1,000 penalty.** The recommendation architecture is
follower-agnostic at the seed stage. The one real gate is **Trial Reels (1,000+)**.
Mosseri has acknowledged "helping small creators break out is technically hard" — an
admission, not a promise. Small accounts typically have *higher* reach-to-follower ratios
than large ones.

## ToS violations — do not use

Engagement pods · follow/unfollow · bought followers · comment bots · private-API
libraries (`instagrapi`, `instagram-private-api`) · scraper services.

Beyond ban risk, they are mechanically self-defeating: every named signal is a **ratio**,
so injected engagement inflates numerator and denominator together while polluting the
interest-prediction model with demographically wrong accounts.

## Primary URLs to re-verify

- https://www.socialmediatoday.com/news/instagram-shares-algorithm-insights-2025/738034/ ← highest priority
- https://creators.instagram.com/blog/tips-for-improving-your-reach ✅ *verified via Composio fetch*
- https://creators.instagram.com/blog/recommendations-and-originality
- https://creators.instagram.com/blog/instagram-trial-reels
- https://about.instagram.com/blog/announcements/instagram-ranking-explained
- https://transparency.meta.com/features/explaining-ranking/ig-feed-recommendations/
- https://techcrunch.com/2024/04/30/instagram-is-updating-its-ranking-systems-to-surface-more-content-from-smaller-original-creators/
- https://www.socialmediatoday.com/news/instagram-implements-new-limits-on-hashtag-use/808309/
- https://techcrunch.com/2026/06/02/meta-tests-series-for-episodic-reels-on-instagram-and-facebook/
