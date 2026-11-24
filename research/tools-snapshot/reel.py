"""reel.py - the project helper for the seven-step editing workflow (Setup/WORKFLOW.md, 2026-11-23).
One folder per reel in VIDEO/Projects. Originals are never moved or changed: the project stores their paths.

  python -I tools/reel.py new "<name>" <clip> [<clip> ...] [--no-transcribe]
  python -I tools/reel.py status [<project>]
  python -I tools/reel.py step <project> <1-7> [--note "..."] [--approved "Jacob's words"]
  python -I tools/reel.py learn "<what went wrong and the fix>"
  python -I tools/reel.py finish <project> <final.mp4> --approved "Jacob's words" [--drive "<folder name>"]
  python -I tools/reel.py clean <project>

<project> is the folder name or any unique part of it. Steps must be done in order. Steps 2, 4, 5 and 7 are stops:
they cannot be recorded without --approved, and "keep going" does not count as approval."""
import sys, os, json, shutil, subprocess, datetime, argparse
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJ = os.path.join(ROOT, "Projects")
LEARN = os.path.join(ROOT, "Setup", "LEARNINGS.md")
DRIVE = "C:/Users/Parts/My Drive/VIDEO/finished"
STEPS = {1: "Project and transcript", 2: "Rough cut (he listens, approves)", 3: "Creative direction (his)",
         4: "Beat plan / storyboard (approves)", 5: "Opening, 10 to 15 s (approves)", 6: "Full video, checked",
         7: "Final approval, saved, notes, cleanup"}
STOPS = (2, 4, 5, 7)
NOT_APPROVAL = ("keep going", "continue", "go on", "ok", "okay", "next")
def now(): return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
def find(name):
    if not os.path.isdir(PROJ): raise SystemExit("no Projects folder yet")
    hits = [d for d in sorted(os.listdir(PROJ)) if name.lower() in d.lower() and os.path.isdir(os.path.join(PROJ, d))]
    if len(hits) != 1: raise SystemExit("project '%s' matches %d folders: %s" % (name, len(hits), hits))
    return os.path.join(PROJ, hits[0])
def load(p): return json.load(open(os.path.join(p, "project.json"), encoding="utf-8"))
def save(p, d): json.dump(d, open(os.path.join(p, "project.json"), "w", encoding="utf-8"), indent=1)
def note(p, line): open(os.path.join(p, "notes.md"), "a", encoding="utf-8").write("- %s  %s\n" % (now(), line))
def show(p):
    d = load(p); print(os.path.basename(p))
    for k in range(1, 8):
        s = d["steps"].get(str(k))
        print("  %s %d. %s%s" % ("[x]" if s else "[ ]", k, STEPS[k], ("   " + s["at"] + ("  approved: \"%s\"" % s["approved"] if s.get("approved") else "") + ("  " + s["note"] if s.get("note") else "")) if s else ""))
    nxt = next((k for k in range(1, 8) if str(k) not in d["steps"]), None)
    print("  next:", "%d. %s" % (nxt, STEPS[nxt]) if nxt else "done" + (", final: " + d.get("final", "") if d.get("final") else ""))
def cmd_new(a):
    for c in a.clips:
        if not os.path.isfile(c): raise SystemExit("clip not found: " + c)
    p = os.path.join(PROJ, "%s %s" % (datetime.date.today().isoformat(), a.name))
    if os.path.exists(p): raise SystemExit("project already exists: " + p)
    for sub in ("work", "work/tmp", "exports"): os.makedirs(os.path.join(p, sub))
    d = {"name": a.name, "created": now(), "sources": [os.path.abspath(c) for c in a.clips], "steps": {}}
    open(os.path.join(p, "notes.md"), "w", encoding="utf-8").write("# %s\n\nSources (never moved or changed):\n%s\n\n## Log\n" % (a.name, "\n".join("- " + s for s in d["sources"])))
    if not a.no_transcribe:
        for c in d["sources"]:
            subprocess.run([sys.executable, "-I", os.path.join(ROOT, "tools", "watch.py"), c, "--out", os.path.join(p, "work")], check=True)
        d["steps"]["1"] = {"at": now(), "note": "transcribed with word timings"};
    save(p, d); note(p, "project created" + ("" if a.no_transcribe else ", transcribed")); show(p)
def cmd_step(a):
    p = find(a.project); d = load(p); n = a.n
    if n not in STEPS: raise SystemExit("step must be 1 to 7")
    if n == 7: raise SystemExit("step 7 is recorded by: reel.py finish <project> <final.mp4> --approved \"...\"")
    for k in range(1, n):
        if str(k) not in d["steps"]: raise SystemExit("step %d (%s) is not done yet" % (k, STEPS[k]))
    if n in STOPS:
        if not a.approved: raise SystemExit("step %d is a stop: it needs --approved with Jacob's own words" % n)
        if a.approved.strip().lower().strip(".!") in NOT_APPROVAL: raise SystemExit("'%s' is not approval of a specific thing" % a.approved)
    d["steps"][str(n)] = {"at": now(), **({"note": a.note} if a.note else {}), **({"approved": a.approved} if a.approved else {})}
    save(p, d); note(p, "step %d done: %s%s%s" % (n, STEPS[n], (" | " + a.note) if a.note else "", (" | approved: \"%s\"" % a.approved) if a.approved else "")); show(p)
def cmd_learn(a):
    open(LEARN, "a", encoding="utf-8").write("- %s: %s\n" % (datetime.date.today().isoformat(), a.text)); print("saved to", LEARN)
def clean(p):
    t = os.path.join(p, "work", "tmp"); n = 0
    if os.path.isdir(t):
        for f in os.listdir(t):
            q = os.path.join(t, f); n += 1
            shutil.rmtree(q) if os.path.isdir(q) else os.remove(q)
    return n
def cmd_finish(a):
    p = find(a.project); d = load(p)
    if not os.path.isfile(a.video): raise SystemExit("video not found: " + a.video)
    for k in range(1, 7):
        if str(k) not in d["steps"]: raise SystemExit("step %d (%s) is not done yet" % (k, STEPS[k]))
    if a.approved.strip().lower().strip(".!") in NOT_APPROVAL: raise SystemExit("'%s' is not approval of a specific video" % a.approved)
    dst = os.path.join(p, "exports", "FINAL - %s.mp4" % d["name"]); shutil.copy2(a.video, dst)
    d["final"] = dst; d["steps"]["7"] = {"at": now(), "approved": a.approved}
    if a.drive:
        dd = os.path.join(DRIVE, a.drive); os.makedirs(dd, exist_ok=True); shutil.copy2(a.video, os.path.join(dd, "%s - POST THIS.mp4" % d["name"])); d["drive"] = dd
    n = clean(p); save(p, d); note(p, "FINAL saved (%s), approved: \"%s\", %d temp items removed" % (os.path.basename(a.video), a.approved, n)); show(p)
def cmd_clean(a):
    p = find(a.project); print("removed %d temp items from work/tmp (nothing else is touched)" % clean(p))
def cmd_status(a):
    if a.project: show(find(a.project)); return
    if not os.path.isdir(PROJ) or not os.listdir(PROJ): print("no projects yet"); return
    for dn in sorted(os.listdir(PROJ)):
        if os.path.isfile(os.path.join(PROJ, dn, "project.json")): show(os.path.join(PROJ, dn))
if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter); sp = ap.add_subparsers(dest="cmd", required=True)
    s = sp.add_parser("new"); s.add_argument("name"); s.add_argument("clips", nargs="+"); s.add_argument("--no-transcribe", action="store_true"); s.set_defaults(f=cmd_new)
    s = sp.add_parser("status"); s.add_argument("project", nargs="?"); s.set_defaults(f=cmd_status)
    s = sp.add_parser("step"); s.add_argument("project"); s.add_argument("n", type=int); s.add_argument("--note"); s.add_argument("--approved"); s.set_defaults(f=cmd_step)
    s = sp.add_parser("learn"); s.add_argument("text"); s.set_defaults(f=cmd_learn)
    s = sp.add_parser("finish"); s.add_argument("project"); s.add_argument("video"); s.add_argument("--approved", required=True); s.add_argument("--drive"); s.set_defaults(f=cmd_finish)
    s = sp.add_parser("clean"); s.add_argument("project"); s.set_defaults(f=cmd_clean)
    a = ap.parse_args(); a.f(a)
