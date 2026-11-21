# Skills study: the three repos behind the @_post2all "5 free Claude skills" reel (2026-11-21)

Source reel: `reel.info.json` / `transcript.txt` in this folder. @_post2all ("Claude for Social Media"), 4,159 likes, 5,468 comments (comment-gated: "Comment SKILLS and I'll DM you all 5 links"). The reel names five things; two of them (Remotion's official skills, Anthropic's skill-creator) are not studied here. The three that matter were cloned with `git clone --depth 1` into `clone/` (git-ignored by `research/reel-references/*/clone/`).

| Repo | Clone URL used | Stars (API, 2026-11-21) | Forks | Licence | Last push | What the reel claimed |
|---|---|---|---|---|---|---|
| Jakeschincariol/instagram-agent-skill | as given | 7,932 | 1,466 | MIT | 2026-09-13 | "5.4K stars" (caption), "5,000" (audio) |
| coreyhaines31/marketingskills | as given | 61,862 | 9,027 | MIT | 2026-11-20 | "59K stars", 53 skills (true: 53 folders) |
| Remocn/remocn | as given (case was right) | 1,829 | 101 | MIT | 2026-11-20 | "825 animations" (README now says 933; registry holds 790 + 48 ui + 102 icons + 7 templates) |

All cloned content was treated as untrusted data. The only thing executed was `hookscore.py`, which imports only `argparse, json, re, statistics, sys` and opens only the input file. It was run with `python -I -X utf8 <script path> hooks12.txt` from the scratchpad, outside the clone.

---

## 1. instagram-agent-skill

Thirteen SKILL.md files, five Python tools (hookscore, beats, caption, humanize/detect, swipe), one `hooks.json` (26 formulas), one `voice.md` template. The author's own test (74 YouTube Shorts hooks, five channels) says the scorer separates deliberately bad hooks from real ones (AUC 0.83) and does not pick winners among decent hooks (AUC 0.56). Only SPECIFICITY separated hits from misses on his corpus. STAKES and ADDRESS "measured nothing". He says so in the README and in the script docstring, which is more honest than most of this genre.

### 1a. The 26 hook formulas, with a Rival version

Templates are near-verbatim from `hooks.json`. Diesel lines are in Jacob's voice: plain, spoken, no hashtags, no on-screen ask. Numbers in curly braces are placeholders that need a real figure before they are used; the pack's own rule is the same (`{{your number}}`, never invented).

| # | Formula | Template (from hooks.json) | Rival line |
|---|---|---|---|
| 1 | Cost Confession | {Specific amount} is what {one mistake} cost me. | "{$} is what ordering the wrong 7.3 head gasket set cost me." |
| 2 | Negative Command | Stop {common action}. Do {alternative} instead. | "Stop buying the first lift pump on the page. Buy the one with a return line." |
| 3 | Nobody Tells You | Nobody tells you that {uncomfortable truth}. | "Nobody tells you a '59 F600 cab bolts to nothing built after 1960." |
| 4 | The Replacement | {This thing} replaced {expensive thing} for {price}. | "This $40 relay replaced a {$} no-start diagnosis on my 7.3." |
| 5 | Time Collapse | This used to take me {long time}. It now takes {short time}. | "Pulling a 7.3 used to take me a weekend. The second one took four hours." |
| 6 | The Receipt | I {did thing} for {N days}. Here are the actual numbers. | "I logged every part that left this 7.3 for 90 days. Here's the list and what it cost." |
| 7 | Wrong Way, Right Way | You are doing {thing} wrong, and it is not your fault. {The fix}. | "You're bleeding your 7.3 fuel system wrong, and it's not your fault. Nobody shows the HPOP side." |
| 8 | Insider Leak | I spent {N years} {inside the thing}. Here is what we never said out loud. | "Six years ordering parts for semis. Here's what the counter never tells you about core charges." |
| 9 | The Steal | Steal this {artifact}. It took me {time} to get right. | "Steal this 7.3 torque sheet. Took me three builds to get it on one page." |
| 10 | If This, Then Watch | If you {specific situation}, this {short time} fixes it. | "If your 7.3 idles rough cold and cleans up warm, the next 30 seconds fix it." |
| 11 | Numbered With A Favourite | {N} {things} that {outcome}. Number {k} is the one nobody uses. | "Five parts every 7.3 needs before a tune. Number four is the one everybody skips." |
| 12 | The Objection | "{Objection they actually say}." Fine. Here is the version that works anyway. | "'Should've been a Cummins.' Fine. Here's the 7.3 that's going to SEMA anyway." |
| 13 | Before And After, On Screen | {Show the old thing}. {Show the new thing}. {One sentence on the lever}. | "This was the frame in March. This is it now. One thing changed, it's a Super Duty frame." |
| 14 | The Callout | {Specific group}, this is the one you have been ignoring. | "7.3 guys still on the stock pump, this is the one you've been putting off." |
| 15 | The Flop Record | My first {N} {attempts} did nothing. Here is what changed on {N+1}. | "My first {N} reels averaged {views}. The next one did 10 million. One thing was different." |
| 16 | The Verbatim Question | "{Question exactly as asked}" - I get this every week. | "'Will a 7.3 even fit a 59 F600' I get this one every week." |
| 17 | Head To Head | {A} versus {B}. I ran both for {time} and one of them was not close. | "Stock 7.3 turbo versus the compound set. Same truck, same dyno, and it wasn't close." |
| 18 | Cold Open Demo | {Start mid-action.} Watch what this does. | "Watch what the boost gauge does when I click the Hydra chip to position five." |
| 19 | The Deadline | {Thing} changes on {date}. Do {action} before then. | "SEMA 2027 build applications close {date}. The frame has to roll before then." |
| 20 | Permission | You do not need {the thing everyone says you need}. | "You don't need a Cummins swap. You need five parts on the 7.3 you already own." |
| 21 | Mid-Sentence Start | ...and that is when {the turn}. | "...and that's when the salvage yard told me the frame was a '99, not a '59." |
| 22 | Contrarian Flip | {Well-known saying, inverted.} | "Stock is the expensive way to run a 7.3." |
| 23 | The Statistic | {N}% of {group} {surprising fact}. | "{N} percent of the fuel filters I order for semis go on trucks that never got a water-in-fuel light." (needs a real count from Fullbay; his counter is Class 8, not pickups) |
| 24 | The Reveal | This is the new {thing}. | "This is the new frame under the '59. It's a 1999 Super Duty." |
| 25 | Someone Else's Result | There was one {person} who {outcome} in {time}. | "There's a guy in {state} who put 600 hp through a stock 7.3 bottom end and it's still running." |
| 26 | The Superlative | The {fastest / biggest / only} {thing} is {the answer}. | "The cheapest horsepower on a 7.3 is a tune, and here's what it does to the stock turbo." |

Each entry in `hooks.json` also carries an `on_screen` version, a `best_for`, a `trap` (how the formula gets ruined) and a `match` regex used by `swipe.py` to classify captured hooks. The traps are the most useful column: "a fake cost", "a situation so broad it qualifies nobody", "the artifact not being on screen", "refusing to pick".

### 1b. How hookscore.py scores

Five checks, each 0 to 100. Overall = mean x 0.6 + weakest check x 0.4, minus 15 per dealbreaker, clamped. STRONG needs overall >= 70, every check >= 55, no flags. OK is >= 50. Else WEAK.

| Check | What it computes |
|---|---|
| LENGTH | Word count at 2.75 words/s (165 wpm). 5 to 12 words = 100. Under 5: minus 20 per missing word. Over 12: minus 11 per extra word. Over 60 characters: minus 12 (two lines of big on-screen text). |
| SPECIFICITY | Counts concrete markers: digits/money/units by regex, capitalised words not at sentence start (treated as proper nouns), spoken numbers (zero, two, ten, hundred, grand, bucks, percent...). "one" and "first" are deliberately excluded. 0 markers = 15. Otherwise 45 + 30 per marker, capped at 100. |
| STAKES | Counts words from a tension list (stop, never, wrong, lost, cost, broke, nobody, no, not, don't, can't, free, paid, first, worst, hate, wasted, secret, before, until, instead, but, only, without, versus, still, already, actually...). A `$` figure adds "a price". 0 = 20, 1 = 70, 2+ = 100. |
| FRONTLOAD | Position of the first payload word (a stakes word, a number, a proper noun). Word 1 to 4 = 100, 5 to 7 = 70, later = 40, none = 30. Minus 30 if the first two words start with a weak opener (so, ok, hey, guys, today, basically, honestly, just, let's, I wanted, have you, do you, in this, this is, it is, you know...). |
| ADDRESS | "you / your / yourself" anywhere = 100. First word is an imperative (stop, steal, don't, never, watch, try, check...) = 90. "I / my / we / our" = 70. None = 35 ("third person, nobody in the room"). |

Dealbreakers (minus 15 each, and no STRONG): opens with "stop scrolling"; video preamble ("in this video", "I'm going to show you"); greeting ("hey", "hi", "what's up", "welcome"); a hashtag; an emoji.

Two implementation quirks that bit our hooks: the weak-opener test uses `startswith`, so "Someone" matches "so" and "Your" matches "yo" (both lost 30 FRONTLOAD points for nothing); and a capitalised word after a period ("Here's") counts as a proper noun. Read the detail line, not just the number.

### 1c. Jacob's 12 hooks through the scorer

Run: `python -I -X utf8 clone/instagram-agent-skill/skills/ig-reel/hookscore.py hooks12.txt --json`. L/S/T/F/A = LENGTH, SPECIFICITY, STAKES, FRONTLOAD, ADDRESS.

| Score | Verdict | L | S | T | F | A | Hook | Scorer's weakest, and the real read |
|---|---|---|---|---|---|---|---|---|
| 80.8 | STRONG | 100 | 100 | 70 | 70 | 100 | Your 7.3 can make 550 without a Cummins swap | FRONTLOAD docked by the "yo" prefix bug; true score about 93 |
| 63.2 | OK | 100 | 75 | 100 | 100 | 35 | 10 mil views and still no shop | ADDRESS. Nobody addressed. Fine for us: it is the series tag line, not a viewer hook |
| 59.6 | OK | 100 | 75 | 70 | 100 | 35 | The $59 fix every OBS owner skips | ADDRESS. "every OBS owner" is a callout but the regex only sees "you" |
| 55.4 | OK | 100 | 75 | 20 | 100 | 100 | 7.3 guys, this one's for you | STAKES. A callout with nothing at stake; works as caption line 1, weak as the spoken opener |
| 51.0 | OK | 100 | 15 | 70 | 100 | 90 | Don't buy this lift pump | SPECIFICITY. No brand, no price. "Don't buy the $89 lift pump" would clear 70 |
| 47.0 | WEAK | 100 | 100 | 20 | 70 | 35 | Someone just put 600 hp through a stock 7.3 bottom end | STAKES. Also hit by the "so" prefix bug. 12 words is the ceiling |
| 44.0 | WEAK | 100 | 75 | 20 | 70 | 35 | Every stock part leaving this 7.3 | STAKES. Payload at word 6. A menu title, not a spoken hook; the counter on screen does the work |
| 43.4 | WEAK | 100 | 75 | 20 | 30 | 70 | Traded my Harley for this | STAKES. No payload word by the regex (Harley counts for specificity but not frontload). Our control reel: 0.05 percent sends, so the scorer and the data agree |
| 39.6 | WEAK | 33 | 100 | 20 | 40 | 70 | I order parts for semis all day. Here's what that taught me about my own 6.7 | LENGTH. 17 words, 6.2 s. Cut to "I order semi parts all day. Here's what it taught me about my 6.7" |
| 36.8 | WEAK | 80 | 75 | 20 | 30 | 35 | Leave the '59 alone | STAKES. Four words, no viewer. As a hater quote on a pill it is a visual, not a line |
| 33.0 | WEAK | 0 | 100 | 70 | 70 | 35 | How a parts manager with no shop of his own is getting a '59 F600 to SEMA 2027 on a 7.3 | LENGTH. 22 words, 8 s spoken. Bio line, not a hook |
| 9.6 | WEAK | 100 | 15 | 20 | 0 | 70 | Hey guys, today we're working on the truck | Greeting dealbreaker, weak opener, nothing concrete. The control |

Best: "Your 7.3 can make 550 without a Cummins swap" (number, name, viewer, tension word, 10 words). Worst real candidate: the parts-manager bio line (length). The control "Hey guys" scored 9.6, which matches the reel's "scored 0" claim closely enough.

What the scorer is good for here: it kills the long ones and the greeting, and it catches "no number, no name" (lift pump). What it is wrong about for diesel: ADDRESS punishes every object-first and hater-quote opener (35), and the hook atlas measured those as the two highest share ratios in the whole set (FASS 2.95 percent, Dirty Diesel 2.25 percent, neither says "you"). STAKES rewards "don't / stop / wrong" openers, and our atlas has FIX as the worst share type (0.00 percent median). Use LENGTH, SPECIFICITY and the dealbreakers. Ignore ADDRESS and STAKES for Rival; the author's own AUC 0.56 says the same.

### 1d. Overlap with our hook atlas (research/reel-references/2026-11-21-hook-atlas)

The atlas is built from 73 measured reels and sorts openers into 13 types with share ratios. The 26 formulas are a writing menu with no measurement attached. Mapping:

| Atlas type (median share) | Formulas that produce it |
|---|---|
| NUM, number or spec (0.76 percent, best 2.95) | 1 Cost Confession, 4 Replacement, 5 Time Collapse, 6 Receipt, 23 Statistic, 25 Someone Else's Result |
| LIST, menu (0.94 percent) | 11 Numbered With A Favourite, 9 Steal |
| RESULT, finished thing first (0.78 percent) | 24 Reveal, 13 Before/After, 15 Flop Record |
| HQ, hater quote (views type, 0.16 to 0.39) | 12 Objection |
| Q, versus (0.31, best 0.91) | 17 Head To Head |
| STORY, mid-sentence cold open (best 2.25) | 21 Mid-Sentence Start, 18 Cold Open Demo |
| BELIEF, contrarian (0.26) | 3 Nobody Tells You, 20 Permission, 22 Contrarian Flip, 26 Superlative |
| FIX, stop doing X (0.00) | 2 Negative Command, 7 Wrong Way |
| TRIBE, callout (weak on screen, strong in caption) | 14 Callout, 10 If This Then Watch |
| NEWS (views, 0.25) | 19 Deadline |
| QD, quoted dialogue | 16 Verbatim Question |
| SOUND, GRID, walk-in title | none. The formulas are all spoken-word shapes |

What the formulas add to the atlas: the 26 are phrased as sentences Jacob can say at 0.0 s, which the atlas only gives for its 12 templates. The `trap` column is new (the atlas has measurements, not failure modes). Formulas 8 (Insider Leak) and 16 (Verbatim Question) are a clean fit for the parts-counter lane and the atlas has nothing for them. What the atlas adds back: the formulas have no idea what frame 1 is. Nine of fourteen diesel winners had no burned text and the subject did the hooking. Pair every formula with an atlas frame-1 template (truck, part, hand, smoke) and keep the formula as the spoken line.

Top five formulas for Rival, filtered by the atlas: 24 Reveal (object first, RESULT), 1 Cost Confession (NUM), 12 Objection (the hater-quote title card already in the addendum, rule 5), 17 Head To Head (versus, objects sliding in), 18 Cold Open Demo (hand on the part, voice at zero). 14 Callout is the caption-line-1 person type and should stay there.

### 1e. The other twelve skills, filtered by our standing rules

**ig-caption** (plus `caption.py`). Two jobs: Job A, the reel already hooked them, so the caption is the ask, context and search terms; Job B, the caption is the content. Prints the 125-character feed window as a box, counts asks (one max), caps hashtags at five (Instagram cut 30 to 5 on 18 Dec 2025, with a Mosseri quote that hashtags are labels, not reach), flags more than 4 emoji per 100 characters, and checks that two or three search phrases appear as normal sentences. Take: the 125-character box as a lint on our person-type line 1 (our share line has to survive the cut), the search-phrase idea ("7.3 Powerstroke lift pump" as words in line 3), and five tags max. Leave: "say the keyword out loud in the video too", which is an on-screen or spoken CTA and is out under Jacob's rule.

**ig-plan.** Four to five posts a week, at least three Reels, never two of a type back to back, a mix of Proof / Teach / Opinion / Story / Offer, each slot tagged with a hook formula number. Says plainly that posting time matters far less than the first two seconds. A daily 20-minute engagement round on a list of 10 accounts (5 reach, 3 peers, 2 buyers) done by hand. Nothing here breaks ToS. Take: the "angle, not topic" discipline and the formula number on every planned slot. Our 30-day outlier matrix already sets cadence, so this is a check on it, not a replacement.

**ig-audit.** Ranks by outlier multiple (views over the account's own median) and sends per reach, which is our grade already. Adds hold at 3 s as "the hook's grade", and one distinction worth keeping: views with no follows is a profile problem, no views is a hook problem. Checks day and time last and only if nothing else shows. Take: hold-at-3s next to sends per reach in our weekly outlier_watchlist readout.

**ig-viral** (plus `swipe.py`). Collect 6 to 12 accounts within about 10x of our size, eyeball each account's median, log hook verbatim, rank by multiple, classify with the 26 regexes, read the unclassified rows by hand (that is where new formulas come from). Reading at human speed in Jacob's own browser, no login by the agent, no scraper. The YouTube Shorts fallback with yt-dlp auto-captions under 3.0 s is a real second corpus for spoken hooks. Take: the TSV shape and `swipe.py` as a classifier over our atlas manifest, to see how many of our 73 hooks the regexes name.

**ig-human** (plus `humanize.py`, `detect.py`, `slop.json`). Strips zero-width and format characters, em dashes to commas, curly quotes to straight, and 154 stock terms including an Instagram block ("stop scrolling", "follow for more", "tag someone who needs this", "run don't walk"). Flags but does not rewrite: "not just X, it's Y", triads, "The result?", preambles, emoji bullets, three shouted words in a row, hashtag walls, follow bait. Five checks (burstiness, specificity, slop density, fingerprint, voice), same 60/40 mean/weakest rule. Take: run `detect.py` on every caption before delivery; the invisible-character pass is a real check we do not have.

**ig-profile** (plus `rubric.json`, 12 items, 100 points). The profile is a decision screen reached from one reel. Fix order: name field (30 characters, searched words, "{Name} | {what you do}"), bio line 1 (who it is for and what changes), the pinned three (best proof, clearest offer, best introduction), four to six highlights named for buyer questions, one link, grid covers with four words readable at thumbnail. Take: the pinned three and the cover rule, which match addendum rule 30 (cover = lockup frame so the grid is the episode guide).

**ig-story.** Three to seven frames, face or hand in frame 1, the one sticker at frame 4 not frame 7, question box as the best idea harvester (feed answers to formula 16), text inside y 250 to 1600. "They act first, then you reply" for DMs. Take: question box for partner and parts questions, and the story as where the offer lives so the feed stays clean.

**ig-dm.** Three DMs worth writing: reply to a raised hand, a warm approach after weeks of real comments, and the collab or brand pitch (four lines: what you have watched them do, the specific idea, what they get, what you need). Two follow-ups only, +4 days with something new and +10 days closing the loop. No automation, no bulk sends. Take: the four-line pitch shape for Rival partners and the two-follow-up cap. It also says the keyword delivery goes in message one with no gate, which matches our "real deliverable" rule.

**ig-reply.** Triage comments into KEYWORD / LEAD / SUBSTANCE / QUESTION / SUPPORT / NOISE and write in that order. A question many people ask becomes a Reel reply (Instagram pins the comment as a sticker on the new video). Haters get nothing, critics get the true part conceded first. Take: the reply-with-a-Reel move for the "will a 7.3 fit" class of question.

**ig-comment.** Nine comment types (add a datum, missing case, respectful disagree, extend one line, the real question, the receipt, correction, reframe, one-liner). One to three sentences, never "Great post", no pitching, early matters most. Commenting on the same three accounts daily looks like what it is. Nothing here is a pod. Take: the receipt and datum types, which Jacob can fill from the counter.

**ig-carousel.** 6 to 10 slides at 1080x1350, cover of six words legible at thumbnail, slide 2 is a second cover, numbered slides, the recap slide is the one people screenshot and send, handle small on every slide. Take: the recap-as-send-object idea for a parts list carousel. The closing CTA slide is theirs, not ours.

**ig-repurpose.** Extract claims, numbers, stories, mechanisms, mistakes and quotable lines from one long asset, count them before writing, assign a different formula to each post, use the real footage. Take: the extraction table as a pass over any long shop or SEMA interview footage.

Across all thirteen: nothing posts, follows, likes or DMs. Every skill ends with a copy-ready block and "the user posts it". No pods, no bots, no follow/unfollow. The pack is ToS-clean by design.

---

## 2. marketingskills

53 skill folders. `skills/social/SKILL.md` (version 2.6.0) is the one the reel means. Its "No AI Tells" section, verbatim:

> ### No AI Tells
>
> Readers scroll past posts that read as generated, and on LinkedIn they say so in the comments. A hook formula is a starting shape. Fill it with a specific fact, number, or story.
>
> Never write these:
> - **Contrast reveals**: "It's not X, it's Y." "Not because X. Because Y." State Y directly, with the reason.
> - **Negation lists**: "No X, no Y, no Z." Say what does happen. One plain absence ("No card required") is fine.
> - **Trailing pile-ons**: a full claim, then a comma and more restating clauses. End the sentence at the claim.
> - **Self-answered questions and colon reveals**: "The result? 3x faster." "The best part: it learns." FAQ questions and a question in the reader's own voice are fine.
> - **Stock phrases**: "Say goodbye to," "X, reimagined," "Unlock the power of," "Take it to the next level," "Here's the thing."
> - **Em dashes** in posts. Use a period or a line break.
>
> Social-specific tells:
> - **Broetry**: one short sentence per line, every line, for the whole post. Write paragraphs and break lines where a person would pause.
> - **Engagement bait**: "Agree?" "Thoughts?" "Let that sink in." "Read that again." End on the point, or a real question you want answered.
> - **Manufactured vulnerability**: "I'll be honest, I was terrified..." with no real story behind it.
> - **Emoji as bullets**: 🚀 ✅ 💡 leading every line.
>
> Keep fragments and lists of three to one per post. For the full blacklist, use the **copywriting** skill's AI-tells reference.

The fuller list is `skills/copywriting/references/ai-tells.md`: 13 structural patterns with Ban/Cap confidence, banned openers and closers, marketing phrases, vocabulary (ban: delve, tapestry, testament to, leverage as a verb, supercharge, game-changer; cap: seamless, robust, streamline, empower, elevate, journey...), hedges and weasels, tone, formatting, and a "second-generation tells" table for copy that has already been de-slopped.

### What we already have

`feedback_no_em_dashes.md`: no em dashes anywhere; also watch parallel structure, "It's not X, it's Y", hedging, repeated three-part rhythms. `2026-11-21-PLAYBOOK-ADDENDUM.md` caption rules are structural (person type in line 1, no ask on screen or in audio, one serif-italic accent word per phrase, five tags cap implied by "no hashtag walls"), not a tells list.

### New to us

1. Negation lists ("no shop, no lift, no budget") as a named ban. We have written that shape.
2. Trailing pile-ons: end the sentence at the claim.
3. Self-answered questions and colon reveals ("The fix? A $40 relay." / "The catch: it's a '99 frame"). Not in our rules and easy to slip into a caption.
4. Broetry as a format tell. Our captions are short, but the one-line-per-sentence habit is the same thing.
5. Engagement bait list: "Read that again", "Let that sink in", "Agree?" This is adjacent to the no-CTA rule and worth adding to it as caption-side bait.
6. Manufactured vulnerability. The honest version for Jacob is a real cost with a number, which is formula 1.
7. Second-generation tells: wisdom-shaped sentences ("Speed is a feature"), tidy quotable closers, self-narration ("Here's why this matters"), perfect balance across sections, reflexive round-number specificity. These are what remains after the em dashes are gone.
8. Fragment and triad caps, one each per post. We said "watch for" and they give a number.
9. Rewrite rule 1: rewrite from the fact, never swap synonyms; and `[NEED: proof]` instead of an invented number. Same as the IG pack's `{{your number}}`.

### Five of the other 52 that fit a one-man creator account with a partner program

| Skill | Why it fits |
|---|---|
| `influencer-marketing` | Written from the brand side (which creators fit, what to pay, what deliverables). Read it backwards to see what Power Hungry, ISSPRO, Strictly Diesel and BD Diesel's marketing people are scoring us on. |
| `co-marketing` | Joint campaigns, partner fit, whether a size mismatch matters. The Collab-post mechanic in addendum rule 42 is co-marketing; this gives the pitch structure. |
| `offers` | How to build the offer itself and add urgency without faking it. Useful for the partner packet (what a sponsor gets, by when). |
| `public-relations` | What makes a story newsworthy, what to say to a reporter. Diesel Army, Diesel World and the SEMA 2027 angle. |
| `sales-enablement` | One-page collateral, objection answers. The partners.html page is sales enablement for a creator. |

`marketing-council` (several named-marketer takes on one decision) is a fun sixth for the "do we gate this post" question. `video` is a tooling comparison (screen recording, AI avatar, code) and adds nothing to our Remotion kit.

Flags from the social skill that contradict our measured rules: its short-form section lists "No CTA" as a mistake and asks for a CTA in the last 3 to 5 s; its subtitle spec says "bold sans-serif with black outline, highlight key words in a different color", which is the exact look the caption audit (55 reels, zero strokes, one accent colour) retired; its posting ladder scales to three posts a day. Its own ban on "Read that again" is funny next to remocn's `double-take` component, whose default copy is "Read that again."

---

## 3. remocn

MIT. 892 doc pages; registry: 790 components in `registry/remocn`, 48 UI primitives, 102 animated icons, 7 full templates, 919 presets. Each component is a folder with `index.tsx` and `config.ts`; `length` in the doc frontmatter is the component's own motion in frames at 30 fps (the floor for a `Sequence`), `durationInFrames` in config is the demo length with hold.

Categories by doc count: typography 257, numbers 125, product-scenes 67, transitions 60, shaders 60, ui 46, logo-stings 46, ui-blocks 34, captions 34, guides 30, motion-graphics 22, social 19, graphic-looks 14, effects 12, media 11, filters 11, camera 10, ai 7, templates 6, layout 5, craft 4, compositions 4, icons 1 (gallery).

Their craft rules (README): no glow halos, no gradient-filled text, no decorative all caps or wide tracking, one accent colour, staggered entrances, no clipped animations, no `Math.random()`, no invented props. Two of their own hook components (crash-zoom, hook-punch) ship with gradient payoff text, which they exempt as "the effect is the point". For us the gradient goes; 307 red stays flat (feedback_307_no_sheen).

Our kit exports (research/tools-snapshot/rival-reels/src/components): Menu (ProgressHud, SidebarList, PhoneStage, CountUp, StrikeStamp, ItemCard, Headline, GhostWord, IrisWipe, NegativeFlash, CommentGate, QuadWall, Checklist), Effects (WallBehind, Masthead, FrameBreak, Vertigo, BgReplace, ChartGrow, PullBackWindow, ZoomThrough, Orbit, HudZoom, BeforeAfter, BlurWord, CompareCards, FaceHud), Paper (WindowStack, PinThumb, Terminal, RepoCard, SpecChips, NotePill), Chandler (PlainCaption, ToolTag, OutlineWord, PipCard, SliderReveal, GridWall, ParamPanel, StoryboardCard), Text (KineticHook, ScriptBlock, WordStamp, CaptionPill, Numeral, TitleCard), Cards (LogoCard, PhotoCard, SpecCard, StrikeList, BrowserCard, PromptBar, CommentDrop, CountCard), Brand (LogoBadge, LowerThird, QuoteBar, CornerLogos), Boil (StickerEdge, DoodleBoil).

### Fifteen ports that add something we do not have

Paths are under `clone/remocn/registry/remocn/<name>/index.tsx`; docs under `clone/remocn/content/docs/<category>/<name>.mdx`. Frames at 30 fps; our reels run 24 fps, so scale by 0.8 or pass `speed`.

| # | Name | Path (index.tsx) | What it does | Rival use | Timing and easing from source |
|---|---|---|---|---|---|
| 1 | exploded-view | camera/exploded-view | Isometric stack of slabs springs apart with leader lines and labels, holds, clicks back together | The 2.5D teardown on our port list: cab / bed / Super Duty frame / 7.3, or a turbo in four layers | OPEN at frame 3, CLOSE at 38, length 50. Open spring damping 12 stiffness 110 (per slab offset 1.5 frames from the top), close spring damping 26 stiffness 320 mass 0.8. Labels draw 19 to 27 frames (+2.5 per slab) with Easing.out(cubic); label out over CLOSE-5 to CLOSE |
| 2 | caption-split-flap | captions/components/caption-split-flap | Each letter on its own flap tile clatters through characters and lands when the word is spoken | The split-flap on our port list, transcript-driven: episode numbers, part names in the menu reel | FLIP_MS 60, 3 to 6 flips per word (seeded, `3 + floor(random * 4)`), flips end on the word's spoken time, MIN_SETTLE_MS 350, ENTER_MS 160, EXIT_MS 220, enter easing bezier(0.2, 0.8, 0.2, 1) |
| 3 | blueprint | graphic-looks/blueprint | A photo wipes left to right into a technical drawing: grid, white linework, dimension lines, one red callout | Frame-swap explainer: the F600 photo wipes to a drawing with the 1999 wheelbase and the cab mount dimensions | length 45. Wipe frames 6 to 24, from -0.04 to 1.04, Easing.inOut(cubic). Callout bubble 36 to 42 with Easing.out(Easing.back(2)) |
| 4 | x-ray-scan | graphic-looks/x-ray-scan | A scanner bar sweeps across an object and reveals white-line internals, one part in red | The 7.3 block: sweep reveals the bottom end, the stock rod in red | length 32. Bar sweeps frames 5 to 32 with Easing.inOut(sin). Accent default #E5322D, strokeWidth 2.4 units |
| 5 | price-slate | numbers/price-slate | Old price reels in, gets struck through, steps aside; new price spins in on digit reels | Parts-counter lane: dealer price struck, our price spins in ("The $59 fix") | Beat sheet: 0 to 22 old price reels in; STRIKE_AT 22 (12 frames, bezier(0.6, 0, 0.25, 1)); MOVE_AT 34 for 18; REEL_AT 47 for 24, digits 3 frames apart, EASE_REEL bezier(0.12, 0.6, 0.18, 1); note rises 71 to 99. Drop their halo gradient sweep (69 to 91) |
| 6 | rotary-dial | ui-blocks/rotary-dial | A knurled dial is grabbed and turned, value counts with it, clicks into a detent | The Hydra chip positions 1 to 5, or a boost target, turned on screen | length 90. HEAVY spring mass 1 damping 26 stiffness 120 for the body, CHIP spring mass 0.5 damping 12 stiffness 200 for the detent click; turn moves 0 to 1.025 then springs back; camera settles over 54 frames from scale 1.08; sweep angle 135 degrees |
| 7 | number-wheel | typography/number-wheel | Odometer that rolls from one value to another, direction inferred, each place a drum | Odometer on the '59, hp before and after, days to SEMA | SPRING_FRAMES 30 with damping 200 stiffness 100 mass 1 per place; overall progress uses Easing.bezier(0.5, 1, 0.5, 1) over the count portion of 112 frames |
| 8 | ruler-scrub | numbers/ruler-scrub | A ruler scrubs past ticks and decelerates until the year lands as a numeral | "2027" landing for the SEMA deadline, or a wheelbase number | SCRUB_END 70, SUBDIV 10 (major tick every 10), EASE_IO bezier(0.65, 0, 0.35, 1), EASE_OUT bezier(0.22, 1, 0.36, 1); velocity ghosting fades in between 8 and 60 units of speed; hero lifts 6 to 38 frames after the scrub, weight 450 to 500, tracking -0.005em to -0.05em |
| 9 | crash-zoom | social/crash-zoom | Calm serif tease (dots type in), crash zoom with 72 speed lines, big payoff card | The hater quote as the tease, the truck or the number as the slam | BEAT crash 36, crashLen 6, impact 42, length 66. Push scale 1 to 1.28 during the crash; CARD spring mass 0.8 damping 18 stiffness 160; ENTER bezier(0.32, 0.72, 0, 1), EXIT bezier(0.55, 0, 1, 0.45). Replace the gradient payoff with flat red |
| 10 | impact-shake | camera/impact-shake | Content slams down from above with squash, damped camera jolt, two-frame RGB split, 36 dust puffs | A number or a part photo landing with weight ("600 HP") | impact default frame 7, length 30. Fall from -0.85 height with Easing.in(quad), stretch 1 to 1.18; jolt spring damping 9 stiffness 260; flash 0 to 0.12 over 2.5 frames; split colours #FF2A2A / #2A6BFF; intensity 0 to 2 |
| 11 | paper-tear | transitions/paper-tear | Frame rips down the middle, halves fling apart with fibrous edges and 28 debris pieces | The reveal cut in Paper reels: spec sheet tears to the real part | length 36. STRAIN to 0.2, IMPACT at 0.28 of progress, rip Easing.in(quad), 44 edge segments; halves peel with spring damping 15 stiffness 150 mass 0.8 over 30 frames; incoming scene scales from 1.1 to 1 with Easing.out(cubic) |
| 12 | whip-pan | transitions/whip-pan | Camera whips sideways with motion blur, both scenes fly through in one move | Montage joins between parts shots in the menu reel | length 26, 64 lines of code. travel bezier(0.7, 0, 0.2, 1), offset 110 percent, blur = sin(pi x travel) x 24 px, scale smear tied to velocity; direction left/right/up/down |
| 13 | scribble-circle | effects/scribble-circle | A brush circle sweeps around a region, thin to thick, in stepped poses | Circle the one part in a photo (the relay, the gasket) | 48 samples per lap, stepped ramp with `durationSteps` default 10 and a `step` size (stop-motion clock), delay prop |
| 14 | ink-arrow | effects/ink-arrow | Hand-drawn arrow draws itself from one point to another in stop-motion poses | Point from the '59 cab mount to the '99 rail; from a price to a part | shaft 40 samples, arm 10 samples; `steppedRamp` over `drawDur` then the head starts at delay + drawDur; same stop-motion step as scribble-circle |
| 15 | caption-label-maker | captions/components/caption-label-maker | Each phrase punched letter by letter into embossing tape at spoken pace, tape feeding out | Parts-shelf captions for the counter lane; the tape is the legibility over footage | PRESS_MS 50 per letter, ENTER_MS 160, EXIT_MS 220, enter easing bezier(0.2, 0.8, 0.2, 1); transcript-driven |

Bench (next five if the fifteen land): `timer-duel` (two stopwatches, 138 frames, quoted time vs real time), `tally-marks` (hand-drawn tallies resolve into a total, 152 frames, parts count), `speed-lines` (element flies in with streaks, lands with squash, 31 frames), `turntable` (card with thickness spins through front, edge, back, 64 frames), `kill-feed` (game-style feed of eliminations, 69 frames, "every stock part leaving this 7.3", minus the gradient banner). `security-cam` (macroblocks, crushed blacks) is a filter on footage and sits under the no-grade rule; skip unless a one-beat shop-cam gag is approved.

Already covered by our kit, so not ported: before-after, versus-split, duet-split (BeforeAfter, CompareCards), countdown and rolling counts (CountUp), strikethrough-replace (StrikeStamp), iris-wipe (IrisWipe), terminal-simulator (Terminal), caption-stamp (WordStamp), said-who and overheard (QuoteBar), paper-sticker (NotePill, StickerEdge), dolly-zoom (Vertigo), spec-sheet (SpecCard).

Licence note: MIT across all 933 components, copyright 2026 Remocn. Their CLAUDE.md says they rewrite from scratch on the Remotion API and do not copy reactbits (MIT + Commons Clause), so porting is clean. Remotion itself keeps its own company licence terms.

---

## 4. Where the three repos contradict our rules

1. **CTA.** ig-reel ("one ask at the end: comment a keyword, save it, or follow"), ig-caption ("say the keyword out loud in the video too") and the marketingskills short-form section ("No CTA" listed as a mistake) all want a spoken or on-screen ask. Our rule is measured (0.03 percent sends with a spoken "tag him", 2.4 percent with a truck and a caption) and stands. The share line stays in caption line 1.
2. **Hook address.** The scorer gives 35 to any hook without "you" or an imperative. Our two best measured diesel share ratios had neither. Do not chase ADDRESS.
3. **Stop-doing-X hooks.** Formulas 2 and 7 and the STAKES check reward them; the atlas has FIX at 0.00 percent median sends. Comments type, not a sends type, and only with a real deliverable, one post in four.
4. **Captions.** marketingskills wants bold sans with a black outline and multi-colour keyword highlights. The caption audit retired both (zero strokes, one accent across 55 reels). PlainCaption v2 stands.
5. **All caps and gradients.** remocn bans decorative all caps and gradient text, then ships gradient payoffs in its hook components. Our MEGANTE and Anton lockups are all caps by brand choice and stay; their gradient goes; 307 red flat.
6. **Cadence.** marketingskills scales to three posts a day once a format clears a view floor; ig-plan says four to five a week. Our 30-day outlier matrix sets our cadence; neither repo has diesel data.
7. **Hashtags.** Both repos now say five max and treat them as labels. Agrees with "no hashtag walls".
8. **Em dashes.** All three agree with Jacob. ig-human strips them mechanically; marketingskills bans them in short copy outright.

## 5. What to actually take, in order

1. Run `detect.py` and `hookscore.py` (LENGTH, SPECIFICITY, dealbreakers only) on every caption and spoken opener before delivery. Both are stdlib Python, no network, run with `-I` from outside the clone.
2. Add the nine "new to us" tells in section 2 to the caption checklist, especially negation lists, colon reveals and "Read that again" bait.
3. Port exploded-view and caption-split-flap first (already on our list), then blueprint, price-slate, rotary-dial.
4. Use the 26 formulas as the spoken-line menu and the atlas as the frame-1 menu; never one without the other.
5. Feed our 73 atlas hooks through `swipe.py` to see which formulas the regexes name and which rows are unclassified; the unclassified diesel rows are our own formula list.
