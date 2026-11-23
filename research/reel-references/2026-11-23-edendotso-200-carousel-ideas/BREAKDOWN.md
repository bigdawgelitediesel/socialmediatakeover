# @edendotso, "200 carousel ideas so you never run out of things to post" (carousel)

- URL: https://www.instagram.com/p/DfSUtyMmK8n/ (sent by Jacob 2026-11-23: "Add this to your tools box")
- Posted 2026-11-03. 13-slide image carousel, no video. 1,648 likes, 695 comments at the pull.
- Account: eden (eden.so), a content-strategy app. Slides 12 and 13 are the ad for it; the caption is a comment gate ("Comment STRATEGY").
- Slides: `slides-01-04.jpg`, `slides-05-08.jpg`, `slides-09-12.jpg`, `slides-13-13.jpg`.
- How the slides were pulled: `yt-dlp --ignore-no-formats-error --skip-download --dump-single-json <url>`, then each entry's `thumbnail` (1080x1350). The `?img_index=` trick and the embed page both return only slide 1.

## What it is

200 fill-in-the-blank post titles, twenty each in ten kinds. Every title is a sentence with one or two blanks ("The [thing] mistake that cost me [time]."). The promise on the cover: "Fill in the blanks with your own life. Post it today."

| # | Kind | Its one-line rule on the slide |
|---|---|---|
| 1 to 20 | Lists | One item per slide. People save what they can come back to. |
| 21 to 40 | Step by step | One step per slide. The swipe does the teaching. |
| 41 to 60 | Before and after | Slide 1 is the before. The last slide is the after. |
| 61 to 80 | Myths | Put the myth on one slide. Flip it on the next. |
| 81 to 100 | Mistakes | Your mistake is their shortcut. |
| 101 to 120 | Stories | End each slide so they have to swipe. |
| 121 to 140 | Breakdowns | Pick a winner. Show why it won, one part per slide. |
| 141 to 160 | Opinions | Say what you think. Agreement is boring. |
| 161 to 180 | Personal | People follow a person. Show yours. |
| 181 to 200 | Use it | Templates and checklists get saved the most. |

All 200, word for word, are in `data/ideas/template-bank.tsv` (the "how" column is the rule above, reworded from slides to beats). The tool is `tools/idea_templates.py` (kinds, list, pick, find, show).

## What is useful here and what is not

- **Useful: the ten kinds as a variety check.** The two-a-day plan leans on Funny, Relatable and Trust. Against this list it is light on Before and after, Myths, Breakdowns and Use it. When a week reads the same, pull the next episode from a kind that week has not used.
- **Useful: the blanks force his own life in.** "The [thing] mistake that cost me [time]" cannot be filled by anybody but Jacob. That is the opposite of the ideas he said he does not like, which were written for him. Use the templates as questions to him ("what's a mistake that cost you a month?"), not as a way to write for him.
- **Useful: the kinds map onto the two daily jobs.** Send (morning): Lists, Myths, Opinions, Use it. Hold (afternoon): Stories, Mistakes, Before and after, Personal. Step by step and Breakdowns work either way.
- **Not useful as carousels.** On this account a still post averages 116 views and reels are 99.6 percent of views (CLAUDE.md). The titles get spoken as talking heads; "one per slide" becomes one per beat. A carousel stays a once-a-month test.
- **Not ours: the comment gate.** "Comment STRATEGY for the link" is the kind of ask the house rules allow only with a real deliverable, at most one post in four. Nothing to copy there.
- **About twenty templates do not fit a parts manager with a truck** (books, podcasts, apps, journaling, meals and workouts, "what's on my desk"). They stay in the bank for completeness; skip them.

## Design note (for card-tier reels)

Off-white page, one serif display line, grey sans subhead, a pastel pill per kind with the same pastel on the blanks, a slide counter top right, twenty hairline-ruled rows. It reads because every slide is the same grid and only the color and the words change. If a list ever goes on a card, that is the layout: one grid, one color per section, the variable word highlighted.

## Standing rule that still applies

Jacob, 2026-11-23: "I just really don't like most of the ideas you have for filming." Do not turn this bank into another batch of ideas. It is a shelf of shapes to reach for after he says what he wants to film.
