# Earshot renders for the El Coyote kit

Earshot 1.0.0 (github.com/Leonxlnx/earshot, MIT, clone at tools/earshot/) installed from git into
tools/venv-sfx (base extra only, about 400 MB: numpy, scipy, soundfile, soxr, numba). No listening models,
no torch. `earshot doctor` reports "earshot looks healthy".

Entry point (always the venv's python, never bare python):

    "C:\Users\Parts\OneDrive - Elite Diesel Service\Desktop\VIDEO\tools\venv-sfx\Scripts\python.exe" -I -m earshot ...

Raw renders live in raw/ (as Earshot wrote them, -1 dBFS true peak). build_kit.py normalises them to the house
peaks and writes the es_*.wav files next to this file, with their measured onset/peak/end in ../kit.json.

| file | request | Earshot's answer | note |
|---|---|---|---|
| raw/thud.wav | `make "a low heavy diesel thud hit, dark, big, short"` | hit/drop, 0.21 s, peak at 0.09 s, -16 LUFS | "diesel" not understood, "heavy" not followed; too small |
| raw/thud_sub.wav | `sfx render cut_hit/sub -o thud_sub.wav --dur 0.5` | cut_hit/sub, 0.500 s, peak at 0.021 s, -14.9 LUFS, clean | the one shipped as es_thud_diesel.wav (sub hit with a kick) |
| raw/clack.wav | `make "a short hard mechanical clack click, dry, not bright"` | switch/small, 0.28 s, peak at 0.12 s, -18 LUFS | shipped as es_clack.wav |
| raw/clack_push.wav | `make "a switch clack" --sound switch/push` | switch/push, 0.34 s, peak at 0.00 s, -17 LUFS | alternate, brighter |
| raw/riser.wav | `make "a riser building into a cut with a hard stop, 1 s" --dur 1.0` | rise/air, 0.97 s, peak at 0.96 s, -14 LUFS | came out 0.966 s, not exact |
| raw/riser_chop.wav | `sfx render pro_riser/chop -o riser_chop.wav --dur 1.0` | pro_riser/chop, 1.000 s exact, peak at 0.995 s, end 1.000 s | shipped as es_riser_1s.wav (stops on its loudest 5 ms) |
| raw/paper_whoosh.wav | `make "a soft paper whoosh, a page sliding past"` | swipe/paper, 0.67 s, peak at 0.15 s, -14 LUFS | shipped as es_whoosh_paper.wav; alts slide/paper, paper/card |

Useful next time:

- `earshot sfx list` prints the 252 bank members with length, peak time and the kit roles they serve.
- `earshot sfx render whoosh_fast/crisp -o w.wav --dur 0.8 --apex 0.32` makes a whoosh whose loudest moment
  is exactly 0.32 s in (within 2.5 ms per the docs), so a cut whoosh can be built to the move.
- `--seed N` gives another take of the same design (rotate takes on repeated sounds).
- `earshot kit init --preset launch -o kit.json` then `earshot kit render kit.json --out kitdir` makes a whole
  role kit with a kit.lock.json of measured peaks. Not used yet; our kit.json comes from build_kit.py.
- Not available on this box by choice: the listen extra (torch + 1.1 GB of models) and therefore `timeline`,
  `describe`, `match`, `critique` and `build` with ears. `measure` needs librosa (the measure extra), also skipped.
