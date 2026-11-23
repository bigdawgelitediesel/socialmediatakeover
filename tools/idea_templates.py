"""The 200 fill-in-the-blank post templates (data/ideas/template-bank.tsv), ten kinds of twenty.

Source: @edendotso carousel, 2026-11-03, sent by Jacob 2026-11-23 ("add this to your tools box").
Breakdown: research/reel-references/2026-11-23-edendotso-200-carousel-ideas/BREAKDOWN.md

  python -I tools/idea_templates.py kinds            the ten kinds and the one-line rule for each
  python -I tools/idea_templates.py list Mistakes    the twenty templates of one kind
  python -I tools/idea_templates.py pick 5           five at random, one per kind where possible
  python -I tools/idea_templates.py find money       every template containing a word
  python -I tools/idea_templates.py show 87          one template by number

These are SHAPES, not finished ideas. A blank only gets filled with something Jacob said, did, bought or
got wrong. Nothing from here goes on the calendar until he picks it (CLAUDE.md, "idea list is under review").
"""
from __future__ import annotations
import csv, random, sys
from pathlib import Path

BANK = Path(__file__).resolve().parents[1] / "data" / "ideas" / "template-bank.tsv"


def load() -> list[dict]:
    with BANK.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def show(rows: list[dict]) -> None:
    for r in rows:
        print(f"{int(r['n']):>3}  {r['kind']:<16} {r['template']}")


def main(argv: list[str]) -> int:
    rows = load()
    cmd = argv[0] if argv else "kinds"
    arg = " ".join(argv[1:])
    if cmd == "kinds":
        seen = {}
        for r in rows:
            seen.setdefault(r["kind"], r["how"])
        for k, how in seen.items():
            print(f"{k:<16} {how}")
    elif cmd == "list":
        hit = [r for r in rows if r["kind"].lower().startswith(arg.lower())] if arg else rows
        show(hit)
    elif cmd == "find":
        show([r for r in rows if arg.lower() in r["template"].lower()])
    elif cmd == "show":
        show([r for r in rows if r["n"] == arg])
    elif cmd == "pick":
        n = int(arg or 5)
        kinds = list(dict.fromkeys(r["kind"] for r in rows))
        random.shuffle(kinds)
        out = [random.choice([r for r in rows if r["kind"] == kinds[i % len(kinds)]]) for i in range(n)]
        show(sorted(out, key=lambda r: int(r["n"])))
    else:
        print(__doc__)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
