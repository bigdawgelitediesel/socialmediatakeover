"""Append the 80 templates readable on the Will Nelson "200 Reel Ideas" carousel to data/ideas/template-bank.tsv (rows 201 to 280).
usage (from the repo root): python -I research/reel-references/2026-11-23-Dft7WarluAo/add_to_bank.py"""
import csv
P = "data/ideas/template-bank.tsv"
K = {
"Instant hooks": ("An opening line for the first 2 seconds. Say it, then pay it off.", """Everyone told me this wouldn't work, until it did.
If you're new to [thing], you need to hear this.
This is the truth no one tells you about [thing].
I made this mistake for months. Don't do the same.
This small change completely transformed my results.
You're probably doing [thing] wrong (and don't even realize it).
I thought I'd be stuck in [thing] forever until I tried this.
I wish someone had told me this before starting [thing].
If you feel lost in [thing], this is what helped me.
Why your [thing] isn't working (and how to fix it).
This simple adjustment in my routine changed everything.
Why I almost quit [thing] (but didn't).
The advice I ignored for years, and I regret it.
Everyone complicates [thing] too much. This is the real secret.
What I was silently ruining my progress in [thing].
This underestimated tip knocked [thing] out of the park overnight.
The myth about [thing] that keeps most people stuck.
If you're doing [thing], do this instead.
No one told me [thing] was going to be this difficult.
I tried 3 strategies for [thing]. This is what really worked."""),
"Tips and tools": ("Practical value. These get saved and sent.", """5 small habits that improved my [thing] instantly.
The 10-minute routine that changed how I approach [thing].
This app completely simplified my [thing] process.
3 tools for beginners I use daily for [thing].
The checklist I follow before every [thing].
The lazy way I organize my [thing] (but it works).
How to cut your [thing] time in half without losing quality.
My step-by-step system to stay consistent with [thing].
The easiest way to measure progress in [thing].
If you always forget [thing], try this.
My underrated favorite tool for people doing [thing].
Stop overcomplicating [thing]. Here is a simple approach.
The setup I use to record, edit or create [thing].
The shortcut that saves me time when I do [thing].
How I automated part of my [thing] process.
The hack that helps me stay focused on [thing].
3 mistakes that made my [thing] harder than necessary.
The productivity trick I swear by when doing [thing].
How I plan a week of [thing] in 1 hour.
The formula I use every time I create [thing]."""),
"Beginners how-to": ("Teaching plus simplifying equals authority.", """How to start [thing] without getting overwhelmed.
The beginner's guide I wish I had when I started [thing].
The 3-step method I use to simplify [thing].
How I plan my entire [thing] process from start to finish.
My exact workflow for [thing] (you can copy it).
How to build a habit around [thing] that actually sticks.
The mistake every beginner makes in [thing].
How to stay consistent with [thing] without burnout.
The 5 things I wish I'd known before starting [thing].
How to get faster results in [thing] using this method.
How to fix your [thing] routine once and for all.
The tools I use daily to make [thing] easier.
How I organize my week to stay consistent with [thing].
The biggest trap for beginners in [thing] and how to avoid it.
How to plan your first [thing] like a professional.
How to build your first [thing] system.
My simple way to track progress in [thing].
The skill that makes everything in [thing] much easier.
How to bounce back when you fail at [thing].
How to start [thing] even without experience."""),
"Storytelling and mindset": ("Show your human side. Connect deeper.", """When I started [thing], I had no idea what I was doing.
This failure in [thing] taught me more than any success.
I used to think [thing] was selfish. Now I see it as self-care.
This is what I learned by doing [thing] every day for 30 days.
I wish I had known this about [thing] before starting.
The day I almost quit [thing], but didn't.
My biggest revelation after months of [thing].
How I manage burnout while doing [thing].
The hardest lesson about starting [thing] (not what people think).
I thought [thing] would make me happy. I was wrong.
Why I stopped chasing perfection in [thing].
How I turned my worst moment into motivation for [thing].
This mindset shift changed everything in [thing].
This is what real progress in [thing] actually looks like.
No one talks about how lonely [thing] can feel sometimes.
How [thing] helped me rebuild my confidence.
What I learned about patience by doing [thing].
How I found my purpose through [thing].
The lesson that completely changed how I see [thing].
What I tell myself when I want to give up on [thing]."""),
}
rows = list(csv.DictReader(open(P, encoding="utf-8"), delimiter="\t"))
have = {r["template"] for r in rows}
n = max(int(r["n"]) for r in rows)
add = []
for kind, (how, text) in K.items():
    for t in text.split("\n"):
        t = t.strip()
        if t and t not in have:
            n += 1; add.append({"n": n, "kind": kind, "how": how, "template": t})
with open(P, "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    for r in add: w.writerow([r["n"], r["kind"], r["how"], r["template"]])
print("added", len(add), "rows; last n", n)
