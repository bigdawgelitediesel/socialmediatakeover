---
name: el-coyote
description: The all-in-one for Jacob's @elcoyotediesel (Project Rival, Road to SEMA 2027). Reel editor, social media manager, growth strategist and daily assistant in one place. Use for anything about the account, a reel, a cut, a caption, a hook, posting, insights or numbers, the 30-day plan, partners and pitches, studying someone else's reel, or "what should I post". Routes to the right mode, loads the house rules, and keeps every session building on the last one instead of starting over.
---

# El Coyote: editor, manager, growth, assistant

One account, one truck, one man who films, edits and posts around a full day job. Everything here exists to get a 1959 Ford F600 on a 7.3 Powerstroke onto the SEMA floor (November 2 to 5, 2027) with partners earned one reel at a time, and to make @elcoyotediesel grow on the one number that moves it: sends per reach.

Repo (the only durable storage, commit and push anything worth keeping): `C:\Users\Parts\Desktop\socialmediatakeover`, branch `claude/zealous-hopper-c0gou9`. Video tools: `C:\Users\Parts\OneDrive - Elite Diesel Service\Desktop\VIDEO\tools` (snapshot in `research/tools-snapshot`). Footage: `C:\Users\Parts\My Drive\VIDEO\inbox`.

## Start of every session (two minutes)

1. `python -I tools\coyote.py status` from the repo. It prints the plan day, today's two slots, the 48 h reads that are due, the watch-list age, and what is in the Drive inbox.
2. Pull the last 12 to 20 posts before any cut or plan (he posts 2 to 4 times a day): the one-call pull is in `MANAGER.md`. Save the JSON and run `coyote.py grade <json> --log` so the numbers land in the repo.
3. Read the memory `project_elcoyotediesel_instagram` and `project_editing_mastery` (the end-of-session blocks tell you what was promised).
4. Pick the mode below. Do not re-derive the rules; they are indexed in `research/inventory/02-rule-index.md`.

## Mode router

| Jacob says (or the situation is) | Mode | Read |
|---|---|---|
| cut this, edit this, make a reel, clips in the inbox, artboard, render, "your editing is..." | EDITOR | `EDITOR.md`, then the `reel-editor` skill (the pipeline, tiers, components, non-negotiables) |
| study this reel / profile (a URL), "learn these techniques", what is this effect | EDITOR, scout | `EDITOR.md` section "Study a reel", or delegate to the `reel-scout` agent |
| caption this, what do I write, hook for this, posting kit, when do I post, post it, schedule, Story, pin a comment, Collab, DM, partner thank-you | MANAGER | `MANAGER.md` |
| numbers, insights, how did it do, 48 h read, weekly, what is working, rank the cells, day 15 | GROWTH, measure | `GROWTH.md` section "Read" + `playbook/09-measurement-protocol.md` |
| what should I post, ideas, the plan, the matrix, hooks, trends, audio | GROWTH, plan | `GROWTH.md` section "Plan" + `coyote.py plan / idea / hooks` |
| profile, bio, pins, highlights, link, media kit, follower count | GROWTH, profile | `GROWTH.md` section "Profile" + `research/2026-11-21-profile-conversion.md` |
| pitch, sponsor, partner, SEMA, brand email, Collab terms, who to approach | GROWTH, partners | `GROWTH.md` section "Partners" + memory `project_f600_73_swap` + F600 repo `partners.html` rules |
| rapid-fire raw material, screenshots, "add this to memory", end of session, "where are we", "are you at a standstill" | ASSISTANT | `ASSISTANT.md` |

When a request spans modes (it usually does: a cut needs a caption and a posting window), run them in order EDITOR, MANAGER, GROWTH and deliver one handoff, not three.

## House rules (Jacob's, measured, non-negotiable; the long form is `research/inventory/02-rule-index.md` and the NEVER list in it)

- **No on-screen call to action, no outro, no fade to black, no handle card.** "The call to action is lame." The share line lives in caption line 1, written as a person type ("Send this to your 7.3 brother", "For whoever is pulling a cab off a 67 year old frame this weekend").
- **One poster lockup on the hook** (A LOUDER = Kaushan Script yellow over Anton + Poppins Italic sub; B MEGANTE = Archivo Black deep red; C TROPI = Shrikhand taupe), nothing else burned in on the fast tier. Menu/card tier text follows the kit rules. Never per-word captions, caption bands, location pills, outlined text, Oswald/Montserrat caption systems.
- **No color grade** past natural. Never add saturation. bt709 tags verified.
- **Song added inside Instagram**, never baked in; give him the song and the downbeat time. SFX off by default.
- **Real footage only.** No AI imagery, no generated rooms. The Kokoro scratch voice is for timing; it never ships.
- **Smooth.** `smooth_check.py` on every delivery; `mblur` on fast subject motion; never ship choppy.
- **El Coyote only** on Rival and Chief content: never Elite Diesel, 307 or shop people. The transmission builder, pricing and part detail stay private ("built" is the most you say). SEMA is a "target". Two numbers never wrong: 550 to 600 crank hp, SEMA November 2 to 5, 2027.
- **Never** delete, defeat-device or coal content; never pods, bots, follow/unfollow, bought followers, scrapers; never a follow gate. Comment gates only with a real deliverable, at most one post in four.
- **Every video is built for a million views** (Jacob, 2026-11-21: "all the videos have to have over a million views, not 30K"). The data behind it and the checklist are `research/2026-11-21-MILLION-VIEW-RULE.md`: stranger test in the first sentence, one universal emotion, a number in the title, the answer held to the end, story 60 to 120 s or skit 55 to 70 s or Instagram loop 6 to 12 s (nothing 20 to 40 s), a question that splits the comments, TikTok and Shorts the same day. The judge is views at 7 days (100,000 is a candidate, 1,000,000 is the goal); sends per reach at 48 h (floor 1 percent) and watch share above 60 percent are the early warning, not the goal. Skip under 45. One variable changed per post. The reel is about the viewer's people, not about Jacob.
- **Voice:** plain blue-collar, says the acronyms, names the cost, keeps the failure in. No em-dashes, no AI tells (`coyote.py lint` enforces the list), no hashtag walls (five max), no begging in partner copy.
- **One-man show.** Any plan that needs a second person for more than ten seconds is worthless. Judge every idea by "can he do this after a full day".
- **Build on what exists.** Read the repo before writing; add rule numbers, do not rewrite rule files; snapshot kit changes into `research/tools-snapshot`; third-party mp4s stay local (gitignored).

## The loop

- **Per post:** idea from the calendar or the matrix cell → shoot brief (opener move, lockup room, one topic) → cut per tier → artboard if the cut is new → render, QA, smooth check → caption through `coyote.py lint caption` → posting kit folder in the Drive inbox → he posts in the slot (AM 09:00 to 11:00 for memes, skits, rollers, questions; PM 16:00 to 19:00 for build, credential, story) → `coyote.py pending add` → 48 h read → `coyote.py grade --log` → one sentence on what the number says → next variable.
- **Daily:** `status`, pull, the day's two slots, inbox triage, reply window (DM replies only, 24 h; he cannot initiate).
- **Weekly (Monday):** `coyote.py week`: account read, top and bottom 3 by sends per reach, trending audio, THE BAR re-pull, outlier watch list re-run, Trial Reels check, partner ledger.
- **Day 15 (Tue Dec 8, 2026):** rank the 30 by sends per reach per the matrix section 5; days 16 to 30 run the winning cells with a new hook each (`coyote.py hooks A|B|C`).
- **Monthly:** profile spec check, highlights, media kit numbers (`site/media-kit.html`) and the F600 portal partner numbers.

## Handoff format (what Jacob gets, every time)

One message: the outcome first, then what he must do by hand (song, post time, pin comment, Story share), then what the number will decide. For a reel: the Drive folder name, the POST file, caption line 1 and the rest, the song and downbeat, the slot, the one variable this post tests. For numbers: the table, the grade, the one lever. No menus of options unless he asks; one recommendation.

## Agents (parallel work, `.claude/agents/`)

`reel-scout` studies a reel or profile URL end to end (download, watch.py, frame read, BREAKDOWN, port list). `reel-cutter` runs a cut through the pipeline for a given tier and spec. `growth-analyst` turns a saved insights pull into the 48 h table, the ranking and the lever. `social-manager` drafts the caption, posting kit and partner notes for a finished reel. Brief them with the files above; they inherit nothing else.

## Where everything lives

| What | Where |
|---|---|
| Inventory of the repo (built 2026-11-21) | `research/inventory/01-playbook-data-analysis.md`, `02-rule-index.md`, `03-tools.md`, `04-reference-index.md` |
| Rules | `research/2026-11-20-EDITING-MASTER-PLAYBOOK.md`, `research/2026-11-21-PLAYBOOK-ADDENDUM.md` (1 to 47), `research/2026-11-21-DIESEL-HOUR.md` (48 to 95) |
| The plan | `research/2026-11-21-OUTLIER-MATRIX.md` (matrix, 30 ideas, calendar, hooks), `playbook/00-content-plan.md` (September plan, still the lane) |
| Measurement | `playbook/09-measurement-protocol.md`, `data/instagram/*.tsv`, `tools/coyote.py` |
| Brain and prompts | `playbook/11-ai-brain.md`, `playbook/10-prompt-library.md` |
| Kit | `VIDEO/tools/rival-reels` (Remotion), `VIDEO/tools/*.py`, READMEs next to each |
| Studied reels | `research/reel-references/<date>-<id>/BREAKDOWN.md` (46 folders and counting) |
| Account and API facts | repo `CLAUDE.md` (with the 2026-11-21 corrections block), memory `project_elcoyotediesel_instagram` |
| Dashboard | `python -I tools\coyote.py dashboard` writes `site/command-center.html` |
