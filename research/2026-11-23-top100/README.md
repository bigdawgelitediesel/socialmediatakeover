# The 100: ten accounts, their ten biggest posts, and why each one worked (2026-11-23)

Jacob sent https://www.instagram.com/reel/Dff_sAnxFjr/ (BOSSBABE, Natalie Ellis, posted 2026-11-09, 8,784 likes) and said "Do what this reel says." What it says: research 10 people who have the audience you want, pick each one's 10 most viral posts, put the link in a spreadsheet and write why you think it went viral, then make those hundred posts. Her promise is "you will go viral within a hundred days"; that is her claim, not a measured one.

## What was done

- **Ten accounts** picked from the 41 on the watch list for the audience Jacob wants (anyone with a truck, blue-collar, 7.3 and old-truck people): bensdiesels, dom_obs7.3, jeff.salv, gas_guzzlin_obs, tomsrefurb, davesautocenter, zac.lucarz, topherolive, joegotti96, bluecollar.memes. The pick is mine; swap any of them and re-run.
- **Their ten most-viewed posts each**, from a fresh pull of up to 400 posts per account on TikTok (`2026-11-23-posts.csv`, 3,054 posts). Instagram hides view counts logged out, so every number here is the TikTok mirror, as in the outlier matrix. "Most viewed" is over the posts the listing returned: all-time for the smaller accounts, the last 400 for the five that have more.
- **98 of the 100 were watched** (downloaded, transcribed, contact sheet read) by five workers; 2 are photo slideshows that only returned audio and are judged from caption and numbers. Each row has the first three seconds, the format, the hook, why it went viral, who sends it to whom, and the shape Jacob can borrow alone.
- Files: `top100.tsv` and `top100.xlsx` (three tabs: 100 posts, By format, Most sent), source rows `top100-input.csv`, worker sheets `why-A.tsv` to `why-E.tsv`, `build_sheet.py`. Jacob's copy: Drive `EL COYOTE/100 viral posts - why they worked (2026-11-23).xlsx`.

## What the 100 say

"Sent %" is TikTok shares divided by views. Sends are this account's grade, so that is the column to sort by.

| Format | Posts | Typical sent % | Typical views |
|---|---|---|---|
| meme (text over clip) | 23 | 2.79 | 306,600 |
| talking head | 5 | 2.39 | 1,200,000 |
| list | 3 | 1.94 | 886,500 |
| walkaround or showcase | 25 | 0.94 | 517,700 |
| skit | 23 | 0.71 | 4,300,000 |
| roller or driving | 3 | 0.38 | 1,200,000 |
| cold start or sound clip | 5 | 0.36 | 419,900 |
| story | 3 | 0.04 | 2,000,000 |

1. **Views and sends come from different posts.** Skits, stunts, sound clips and stories pull the most views and the fewest sends. Memes and talking-head warnings pull fewer views and three to four times the sends. Every one of the five workers found this independently on their own accounts.
2. **What gets sent names a person.** "POV: that one coworker at 6:30am" (4.73), "When 7.3 owners add a KC Turbo and Hydra" (8.18), "Boss: who wants to come in on Saturday?" (4.33). The viewer knows exactly who to send it to. A pretty truck with a song (dom_obs7.3, jeff.salv) gets the same views at 0.1 to 1.1.
3. **The talking heads that get sent are warnings with the proof in hand** (davesautocenter): DEF crystals 1.88, the blocked radiator and weak AC 2.39 with 84.5k saves, DEF in the fuel tank. First sentence is the cost, then he holds the evidence. Only five of the 100 are talking heads, so this is a thin sample, but it is the closest model for Jacob's format.
4. **News an owner passes along beats the stunt** (zac.lucarz): the King Ranch Taurus 2.81, "legal to delete" 2.48, 2027 engines 1.94, against 0.02 to 0.08 for his builds and stunts. Two of those claims are overstated or thinly sourced; the shape is what transfers, not the claim.
5. **Asking the audience gets comments, not sends.** "Guess what's wrong" drew 3,704 comments at 0.09; the answer video did about half the views of the question.
6. **Pain framed as a joke outsends the same pain framed as politics.** Red-diesel jokes 3.7 to 5.5; the tire-ban meme 0.9 at 88 times median; the pump clip with a politician's audio 0.1.
7. **One man can play two people.** topherolive is ten for ten with a calm line, then the same man in sunglasses overreacting; joegotti96 puts the phone where the clerk or boss stands. Both are solo. The widest targets (weather, the DMV) shared best.
8. **A question on screen with a two or three word answer** ("How much can a 7.3L tow? All of it.", 3.06) and **the critic's line quoted on screen, answered by a shot of the truck** (the mpg question, "that is so tacky", the swampers) are both filmable alone on a tripod.

## What this confirms and what it corrects

- Confirms the repo's split: memes are graded on sends, talking heads on watch time and likes (doctrine), and the 10-mil meme is the account's real record.
- Corrects a habit: the long one-take skit (55 to 70 s) has been treated as a send format. In this sample skits are the views format (median 0.71), unless the skit names a tribe (bensdiesels 8.18 and 4.70, tomsrefurb 6.36).
- Adds: a talking head can be a send format when it is a warning with physical proof in hand.

## Avoid rows (kept in the sheet, shaded, nothing to borrow)

bensdiesels-02 and -03 (a reaction clip of a real person who appears to have a disability), bluecollar.memes-10 (the gag leans on a man with dwarfism). Noted but kept for structure only: bluecollar.memes-04 (slur-heavy audio), dom_obs7.3-06 (a joke at women's expense), zac.lucarz Flock plate spray (illegal in most states), davesautocenter-07 (sponsored demo, not organic).

## What was NOT done, on purpose

The reel's last step is "do those hundred posts." The sheet has a "shape you can borrow alone" column: the structure only, one man, no script. It is not a list of 100 ideas for Jacob. He said on 2026-11-23 that he does not like most of the ideas written for him, so the next step is his: he marks the rows he would be glad to film, and those get written up with him.
