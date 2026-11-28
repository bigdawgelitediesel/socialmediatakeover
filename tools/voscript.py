#!/usr/bin/env python
"""
voscript.py: turn a plain script in Jacob's words into an ElevenLabs script with the right directions.

  python -I tools/voscript.py script.txt                 -> script.v4.txt for Eleven v4 (the default)
  python -I tools/voscript.py script.txt --model v2      -> script.v2.txt for Multilingual v2 / Flash
  python -I tools/voscript.py script.txt --out other.txt
  python -I tools/voscript.py --card                     -> prints the one-page format card

How to write the plain script (playbook/15-voice-script-format.md has the same with an example):
  - A blank line is a new paragraph. The tool puts a [pause] at the start of each new paragraph.
  - Directions go in parentheses, at the start of a line or inside it:
      (beat) (pause) (long pause) (sigh) (exhale) (laugh) (chuckle) (quiet) (slow)
      (warm) (tired) (curious) (sarcastic) (excited) (whisper) (clear throat)
  - *word* makes the voice lean on that word (it becomes WORD). Use it on one word a sentence at most.
  - Write numbers the way you say them ("sixty-seven hundred", "six seven", "twenty twenty-seven");
    Eleven v4 reads exactly what is written.
  - Em-dashes become commas. "..." stays and adds weight.
  - Anything already in [brackets] passes through if it is a known ElevenLabs tag; stage directions
    like [grinning] are flagged, because the voice cannot perform them.
  - Words in data/voice/pronounce.tsv are swapped for their spoken form (IPA on v4, a respelling on v2).

Stdlib only. Spends no credits; it only writes text.
"""
from __future__ import annotations
import argparse, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRON = ROOT / "data" / "voice" / "pronounce.tsv"

# what Jacob writes in parentheses -> the Eleven v4 audio tag
DIRECTIONS = {
    "beat": "short pause", "short pause": "short pause", "pause": "pause", "long pause": "long pause",
    "sigh": "sighs", "sighs": "sighs", "exhale": "exhales", "exhales": "exhales",
    "laugh": "laughs", "laughs": "laughs", "chuckle": "chuckles", "chuckles": "chuckles",
    "quiet": "softly", "soft": "softly", "softly": "softly", "slow": "slowly", "slowly": "slowly",
    "warm": "warmly", "warmly": "warmly", "tired": "tired", "curious": "curious",
    "sarcastic": "sarcastic", "deadpan": "sarcastic", "excited": "excited",
    "whisper": "whispers", "whispers": "whispers", "clear throat": "clears throat", "clears throat": "clears throat",
    "surprised": "surprised", "happy": "happy", "sad": "sad", "nervous": "nervous",
}
# tags ElevenLabs documents for v4 and v3; anything else in brackets gets a warning
KNOWN_TAGS = set(DIRECTIONS.values()) | {
    "laughs harder", "starts laughing", "giggles", "gasps", "crying", "snorts", "mischievously",
    "dramatically", "cautiously", "shouting", "deep voice", "high voice", "raspy", "breathless",
    "interrupting", "jumping in", "overlapping", "angry", "frustrated sigh", "laughs softly",
}
STAGE = {"grinning", "pacing", "standing", "music", "smiling", "nodding", "looking at camera", "beat drops"}
OPENERS = ["hey guys", "hey everyone", "what's up guys", "so today", "today we", "in this video", "welcome back"]
TEST_WORDS = ["ISSPRO", "HPOP", "SEMA", "OBS", "F600", "F-600", "CP4", "6.7", "7.3", "PACCAR", "Cheyenne", "Laramie", "Coyote", "FASS", "DEF", "DPF", "EGR"]
WEB_LIMIT = {"v4": 10000, "v3": 5000, "v2": 5000}

CARD = """THE SCRIPT FORMAT (Eleven v4, your clone)

Write it the way you would say it to one person. Then:
  blank line            = new paragraph, the voice takes a breath there
  (beat)                = short pause          (pause) / (long pause) = longer
  (sigh) (laugh) (chuckle) (exhale) (clear throat)   = the sound, right where it happens
  (quiet) (slow) (warm) (tired) (curious) (sarcastic) (excited) = how the next words are said,
                          it holds until the next direction, so change it only where the delivery changes
  *word*                = lean on this word (one a sentence at most)
  numbers               = write them the way you say them: "sixty-seven hundred", "six seven", "twenty twenty-seven"
  "..."                 = weight before the next words
  no stage directions   = (grinning), (looking at camera) do nothing; describe the voice, not the body
  few directions        = one every 20 words or less; the model does the rest from punctuation

Load it: ElevenLabs app > Text to Speech > voice Jake 2.0 (the professional clone when it exists)
> model Eleven v4 > Stability 50, Similarity 75, Clone Strength 0 > paste the .v4.txt > Generate.
Two free regenerations within two hours. Pick by ear. Download MP3.
Or send me the plain script and I generate two takes with the connector and you pick.

Rules: your words only. The AI label goes on in the share sheet on every post that uses the voice.
"""


def load_pron() -> list[tuple[str, str, str]]:
    rows = []
    if not PRON.exists():
        return rows
    for line in PRON.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#") or line.lower().startswith("word\t"):
            continue
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        rows.append((parts[0].strip(), parts[1].strip(), parts[2].strip()))
    return rows


def convert(text: str, model: str = "v4") -> tuple[str, list[str], dict]:
    warnings: list[str] = []
    text = text.replace("\r\n", "\n").replace("\u2014", ", ").replace("\u2013", ", ").replace("\u2026", "...")
    text = re.sub(r" ,", ",", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    out_paras: list[str] = []
    tag_count = 0
    for i, p in enumerate(paras):
        p = " ".join(line.strip() for line in p.splitlines())
        # (direction) -> [tag]
        def sub_dir(m: re.Match) -> str:
            nonlocal tag_count
            key = m.group(1).strip().lower()
            if key in DIRECTIONS:
                tag_count += 1
                return "[" + DIRECTIONS[key] + "]"
            warnings.append(f'paragraph {i + 1}: unknown direction "({m.group(1)})" left as written; use one from the card')
            return m.group(0)
        p = re.sub(r"\(([a-zA-Z ]{3,20})\)", sub_dir, p)
        # [tags] already written: check them
        for t in re.findall(r"\[([^\]]+)\]", p):
            key = t.strip().lower()
            if key in STAGE:
                warnings.append(f'paragraph {i + 1}: "[{t}]" is a stage direction, the voice cannot perform it; describe the voice instead')
            elif "-" in key:
                warnings.append(f'paragraph {i + 1}: "[{t}]" has a hyphen; ElevenLabs wants plain words ("[high voice]", not "[high-pitched]")')
            elif key not in KNOWN_TAGS and key not in DIRECTIONS.values():
                warnings.append(f'paragraph {i + 1}: "[{t}]" is not a documented tag; it may be read as a sound effect or ignored')
        # <break> is v2 only
        if model == "v4" and "<break" in p:
            p = re.sub(r"<break[^>]*>", "[pause]", p)
            warnings.append(f"paragraph {i + 1}: <break> replaced with [pause]; v4 has no SSML")
        # *word* -> WORD
        p = re.sub(r"\*([^*\n]{1,40})\*", lambda m: m.group(1).upper(), p)
        # paragraph pause
        if i > 0 and not p.startswith("["):
            p = "[pause] " + p
        out_paras.append(p)

    # pronunciation map
    applied = []
    for word, v4, v2 in load_pron():
        rep = v4 if model == "v4" else v2
        if not rep:
            continue
        pat = re.compile(r"(?<![\w/])" + re.escape(word) + r"(?![\w/])")
        new_paras = [pat.sub(rep, p) for p in out_paras]
        if new_paras != out_paras:
            applied.append(f"{word} -> {rep}")
        out_paras = new_paras

    if model != "v4":
        # v2 and Flash speak brackets as words: strip the tags, use <break> between paragraphs
        cleaned = []
        for p in out_paras:
            p = re.sub(r"\[(short pause|pause|long pause)\]\s*", "", p)
            p = re.sub(r"\[[^\]]+\]\s*", "", p)
            cleaned.append(p)
        body = '\n\n<break time="0.7s" />\n\n'.join(cleaned)
    else:
        body = "\n\n".join(out_paras)

    plain = re.sub(r"<break[^>]*>", "", re.sub(r"\[[^\]]+\]", "", body))
    words = len(plain.split())
    chars = len(body)
    low = plain.lower()
    for o in OPENERS:
        if low.lstrip().startswith(o):
            warnings.append(f'opens on "{o}": the house rule is first noun by 0.9 s, no greeting')
    if tag_count and words and tag_count > max(1, words // 20):
        warnings.append(f"{tag_count} directions in {words} words; one every 20 words is the ceiling, the model does the rest")
    if chars > WEB_LIMIT.get(model, 10000):
        warnings.append(f"{chars} characters is over the web app limit for {model} ({WEB_LIMIT.get(model)}); split it")
    pron_words = {w for w, _, _ in load_pron()}
    untested = [t for t in TEST_WORDS if re.search(r"(?<![\w/])" + re.escape(t) + r"(?![\w/])", plain) and t not in pron_words]
    if untested:
        warnings.append("listen for these words, they are the ones a model misreads: " + ", ".join(untested) + " (add a line to data/voice/pronounce.tsv if one is wrong)")
    if re.search(r"\d", plain):
        warnings.append("digits are in the script; v4 reads them as written, so write them the way you say them if a take gets one wrong")
    stats = {"words": words, "chars": chars, "credits": chars, "seconds": round(words / 160 * 60), "tags": tag_count, "pronounced": applied}
    return body, warnings, stats


def main() -> None:
    ap = argparse.ArgumentParser(description="plain script -> ElevenLabs script with directions")
    ap.add_argument("script", nargs="?", help="plain .txt or .md in Jacob's words, or - for stdin")
    ap.add_argument("--model", choices=["v4", "v2"], default="v4")
    ap.add_argument("--out")
    ap.add_argument("--card", action="store_true", help="print the format card and exit")
    a = ap.parse_args()
    if a.card or not a.script:
        print(CARD)
        return
    text = sys.stdin.read() if a.script == "-" else Path(a.script).read_text(encoding="utf-8")
    body, warnings, st = convert(text, a.model)
    out = Path(a.out) if a.out else (Path("script") if a.script == "-" else Path(a.script)).with_suffix(f".{a.model}.txt")
    out.write_text(body + "\n", encoding="utf-8")
    print(f"wrote {out}")
    print(f"{st['words']} words, {st['chars']} characters = about {st['credits']} credits, about {st['seconds']} s of speech, {st['tags']} directions")
    if st["pronounced"]:
        print("pronunciation applied: " + "; ".join(st["pronounced"]))
    for w in warnings:
        print("  ! " + w)
    print("next: paste the file into Text to Speech (voice Jake 2.0, model Eleven v4, stability 50, similarity 75), or send it to me to generate")


if __name__ == "__main__":
    main()
