"""cutfind.py - propose the rough cut: dead air, stutters, false starts and repeated takes. It proposes only.
Built 2026-11-24 on Nate Herk's Herk Edit Kit scripts (MIT, copied to tools/herk/ with the licence), from the
"4 free GitHub repos" reel (DfmlI5sNFVa). Nothing is cut here: Jacob approves cuts at step 2 of Setup/WORKFLOW.md.

usage: python -I tools/cutfind.py <words.json> [--gap 0.55] [--out <dir>]
   words.json is the watch.py / reel.py transcript: [{"w": " word", "s": 0.00, "e": 0.32}, ...]

Rules it follows (Herk playbook, and they match rule 115: cut filler, never meaning):
  - cut BETWEEN phrases at real silence, never inside a phrase
  - a pause under the gap is natural rhythm and stays; a trimmed pause keeps a breath (0.14 to 0.24 s)
  - a repeat can be emphasis ("never, never"): every mistake candidate is a question for a person, not a cut
"""
import sys, os, json, subprocess, argparse
HERE = os.path.dirname(os.path.abspath(__file__)); HERK = os.path.join(HERE, "herk")

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("words"); ap.add_argument("--gap", default="0.55"); ap.add_argument("--out")
    a = ap.parse_args()
    out = a.out or os.path.join(os.path.dirname(os.path.abspath(a.words)), "cutfind"); os.makedirs(out, exist_ok=True)
    w = json.load(open(a.words, encoding="utf-8"))
    if isinstance(w, dict): w = w.get("words", [])
    words = [{"text": (x.get("w") or x.get("text") or x.get("word") or "").strip(), "start": x.get("s", x.get("start")), "end": x.get("e", x.get("end"))} for x in w]
    src = os.path.join(out, "raw.json"); json.dump({"words": words}, open(src, "w", encoding="utf-8"))
    r1 = subprocess.run(["node", os.path.join(HERK, "cut-silences.mjs"), src, "--out-dir", out, "--gap", a.gap], capture_output=True, text=True, encoding="utf-8")
    if r1.returncode: sys.exit(r1.stderr or r1.stdout)
    j = json.loads(r1.stdout[r1.stdout.index("{"):])
    print("dead air: %.1f s of %.1f s (%.0f%%) in %d pauses over %s s" % (j["removed"], j["sourceDuration"], j["removedPct"], j["deleteRanges"], a.gap))
    edl = json.load(open(os.path.join(out, "raw.silence-edl.json"), encoding="utf-8"))
    for d in edl.get("delete_ranges", [])[:60]:
        print("   cut %7.2f to %7.2f  (%.2f s)  %s" % (d["start"], d["end"], d["end"] - d["start"], "; ".join(d.get("reasons", []))))
    r2 = subprocess.run(["node", os.path.join(HERK, "find-cut-candidates.mjs"), os.path.join(out, "raw.silence-transcript.json"), "--out-dir", out], capture_output=True, text=True, encoding="utf-8")
    if r2.returncode: sys.exit(r2.stderr or r2.stdout)
    k = json.loads(r2.stdout[r2.stdout.index("{"):])
    print("mistake candidates: %d %s (times are on the pause-trimmed timeline)" % (k["candidates"], k["counts"] or ""))
    md = os.path.join(out, "raw.silence-transcript.cut-candidates.md")
    for f in os.listdir(out):
        if f.endswith("cut-candidates.md"): md = os.path.join(out, f)
    if k["candidates"] and os.path.exists(md): print(open(md, encoding="utf-8").read())
    print("files:", out)

if __name__ == "__main__": main()
