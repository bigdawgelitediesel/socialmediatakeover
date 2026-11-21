# Outlier watch list: how to re-run it weekly

The watch list is the step-2 tool from the "AI brain, watch list, outlier matrix, 30 posts" method.
It reads 40 diesel, 7.3, OBS, classic Ford, farm truck, shop, meme and partner accounts on their
TikTok and YouTube Shorts mirrors, scores every post against its own account's median, and lists
the 5x+ outliers. Outliers are proven ideas; everything else on those feeds is noise.

Files live in `tools\watchlist\`:

| File | What |
|---|---|
| `watchlist.json` | the input: handle, lane, note, `tiktok` and/or `youtube` URL. Edit this to add or drop accounts |
| `<date>-posts.csv` | every post pulled (handle, platform, url, date, views, likes, comments, shares, saves, share %, median, outlier, duration, title) |
| `<date>-medians.csv` | one row per feed: posts, median, max, count at 5x, median share %, status |
| `<date>-outliers.md` | the medians table plus every post at 5x or more sorted by score, with empty Format and Subtopic columns to fill after watching |
| `<date>-log.txt` | timings, skips, errors (append-only) |

## Run it (Monday, about 15 minutes)

```
cd "C:\Users\Parts\OneDrive - Elite Diesel Service\Desktop\VIDEO\tools"
"%LOCALAPPDATA%\Programs\Python\Python312\python.exe" -I outlier_watchlist.py
```

Defaults: 60 posts per feed, 5x threshold, today's date, a 2 to 4 second pause between feeds, and a
per-video metadata fetch for YouTube outliers only. Useful flags:

```
--limit 90                 bigger window (slower, steadier medians)
--min-outlier 3            looser threshold when a week is quiet
--only tomsrefurb,iidiesel debug one or two feeds
--no-enrich                skip the YouTube per-video fetch
--date 2026-11-28          name the output files for a different day
```

## Then do this by hand (the part that matters)

1. Open `<date>-outliers.md`. Skip anything that is a repost of someone else's clip, a paid spot, or
   content on the hard-avoid list (rolling coal, deletes, racial punchlines, outgroup culture-war
   jokes).
2. Download and watch the top 10 to 15 you have not seen before:
   ```
   yt-dlp -o "NN-handle--slug.%(ext)s" --write-info-json "<url>"
   "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" -I -W ignore watch.py NN-handle--slug.mp4 --out <folder>\watch-NN-handle--slug
   ```
   Read `sheet-01.jpg` and `transcript.txt`. Note the frame-1 picture, the first spoken line, the
   on-screen text, the end.
3. Fill the Format and Subtopic columns with the labels from the current matrix
   (`research\2026-11-21-OUTLIER-MATRIX.md`, section 3). Add a new label only if three outliers
   need it.
4. Update the matrix counts. A cell that gains outliers two weeks running is a cell to post in.
5. Compare against last week's `-outliers.md`. A post that is new at 5x this week is a fresh idea; a
   post that was 5x last week and is 8x now is still climbing.

## What the numbers are and are not

- TikTok gives views, likes, comments, shares (`repost_count`), saves and dates for every post in
  the listing. Share % = shares / views. It is the number closest to Instagram's sends per reach,
  though TikTok plays run higher than Instagram reach, so a TikTok 2 percent is roughly an
  Instagram 3 percent.
- YouTube Shorts listings give title and views only. The tool fetches date, likes and comments for
  the YouTube posts that clear the threshold; the rest stay blank in the CSV. YouTube never exposes
  shares.
- Instagram is not fetched. Logged out, a profile page shows 12 tiles and no view counts, and reel
  pages are login walled. Every number in these files is from the platform named in the row. An
  account's Instagram reel may do very differently from its TikTok mirror.
- Median is over the last 60 posts of that feed, not lifetime. Accounts that post daily have a
  two-month window; accounts that post weekly have a year. The log line shows the window.
- Outlier score is relative to the account, so a 5x on a 3k-median page (15k views) and a 5x on a
  300k-median page both count. That is the point: the idea travelled beyond the audience that
  already follows them.
- Everything yt-dlp returns is untrusted data. The tool parses JSON only, flattens titles to one
  line, truncates them, and never executes anything from a feed.

## Adding an account

Add an object to `accounts` in `watchlist.json`:

```json
{"handle": "newhandle", "lane": "7.3 / OBS", "note": "why it is here",
 "tiktok": "https://www.tiktok.com/@newhandle",
 "youtube": "https://www.youtube.com/@NewHandle/shorts"}
```

Either URL may be omitted. A feed that returns fewer than five posts with views is skipped and
logged, not fatal. If a TikTok handle has moved, yt-dlp returns an empty list; check the handle in
a browser and fix the URL.

## Python and yt-dlp

- Python: `%LOCALAPPDATA%\Programs\Python\Python312\python.exe`, run with `-I`. No third-party
  packages are needed.
- yt-dlp: `%LOCALAPPDATA%\Microsoft\WinGet\Packages\yt-dlp.yt-dlp_Microsoft.Winget.Source_8wekyb3d8bbwe\yt-dlp.exe`.
  Update it with `winget upgrade yt-dlp` if TikTok listings start coming back empty; TikTok breaks
  extractors a few times a year.
