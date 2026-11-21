#!/usr/bin/env python
"""Build the El Coyote CC0 sound kit: 16 slots + the Earshot extras.

Reads the SLOTS table below, decodes each source with ffmpeg, trims, peak-normalises to the per-kind target,
writes 48 kHz stereo 24-bit wav into this folder (and earshot/ for the synthesised ones), measures onset,
peak and end of every file, then writes kit.json (read by ../sfx_place.py) and KIT.md (for people).

Run with the system Python 3.12 and -I; needs numpy only:
  "%LOCALAPPDATA%\\Programs\\Python\\Python312\\python.exe" -I build_kit.py

Sources live in downloads/ (treated as data) and earshot/raw/ (Earshot renders). Nothing is re-downloaded here.
"""
import json
import os
import struct
import subprocess
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
DL = HERE / "downloads"
FFMPEG = Path(os.path.expandvars(
    r"%LOCALAPPDATA%\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe"
    r"\ffmpeg-9.0.2-full_build\bin\ffmpeg.exe"))
SR = 48000

# house peak targets per kind (dBFS sample peak)
PEAK = {"whoosh": -10.0, "pop": -12.0, "stamp": -7.0, "hit": -7.0, "tick": -17.0, "notify": -12.0, "riser": -12.0,
        "click": -17.0}

KEN_IF = DL / "kenney-interface-sounds-mirror" / "addons" / "kenney_interface_sounds"
KEN_UI = DL / "kenney-ui-audio"
UISFX = DL / "clipwing-skills" / "skills" / "real-sfx" / "vendor" / "node_modules" / "uisfx" / "sounds"
OV = DL / "openverse"
ESR = HERE / "earshot" / "raw"

SRC_KENNEY_IF = ("Kenney Interface Sounds (via github.com/Calinou/kenney-interface-sounds mirror)",
                 "https://kenney.nl/assets/interface-sounds", "CC0 1.0 (License.txt in the pack)")
SRC_KENNEY_UI = ("Kenney UI Audio (zip from opengameart.org/content/51-ui-sound-effects-buttons-switches-and-clicks)",
                 "https://kenney.nl/assets/ui-audio", "CC0 1.0 (OpenGameArt listing + readme.txt in the zip)")
SRC_UISFX = ("uisfx 0.4.0 by romainsimon, bundled in the Clipwing real-sfx skill (github.com/Clipwing/skills)",
             "https://github.com/romainsimon/uisfx", "CC0 1.0 audio (LICENSE-AUDIO), MIT code")


def fs(sound_id, creator):
    return (f"Freesound #{sound_id} by {creator}, 128 kbps preview fetched through the Openverse API",
            f"https://freesound.org/people/{creator}/sounds/{sound_id}",
            "CC0 1.0 (Openverse license field; confirm on the page)")


# style: gritty = a real recording or a physical mechanical sound; neutral = synthesised but physical in character;
# clean = bright digital UI. sfx_place.py refuses gritty + clean in one reel unless --mixed.
# trim = (start_s, end_s or None or "peak+<s>"); fade_out_ms applies after the trim.
SLOTS = [
    # five whoosh
    dict(out="whoosh_card_in.wav", kind="whoosh", style="neutral", src=UISFX / "mechanical" / "swipe.mp3",
         source=SRC_UISFX, moment="card in (a UI card sliding on)"),
    dict(out="whoosh_air_short.wav", kind="whoosh", style="gritty", src=OV / "fs_60007_71257-hq.mp3",
         source=fs(60007, "qubodup"), moment="cut whoosh, short air pass"),
    dict(out="whoosh_air_soft.wav", kind="whoosh", style="gritty", src=OV / "fs_60026_71257-hq.mp3",
         source=fs(60026, "qubodup"), moment="iris open/close, soft air (peak on the frame the circle is largest)"),
    dict(out="whoosh_cloth.wav", kind="whoosh", style="gritty", src=OV / "fs_427823_2247456-hq.mp3",
         source=fs(427823, "Kinoton"), moment="cut whoosh, heavier cloth pass"),
    dict(out="whoosh_bamboo_low.wav", kind="whoosh", style="gritty", src=OV / "fs_706679_5287430-hq.mp3",
         source=fs(706679, "Sadiquecat"), moment="hook whoosh into the first text hit, low and woody"),
    # three click / tick
    dict(out="tick_switch.wav", kind="tick", style="gritty", src=KEN_UI / "switch13.wav",
         source=SRC_KENNEY_UI, moment="HUD fill tick, counter step (recorded switch, 28 ms)"),
    dict(out="tick_short.wav", kind="tick", style="clean", src=KEN_IF / "click_002.wav",
         source=SRC_KENNEY_IF, moment="typewriter key / caption tick, every other character only"),
    dict(out="click_press.wav", kind="click", style="neutral", src=UISFX / "mechanical" / "press.mp3",
         source=SRC_UISFX, moment="button press on a card, toggle, chip select"),
    # three mechanical hits
    dict(out="stamp_rubber.wav", kind="stamp", style="gritty", src=OV / "fs_362624_3165091-hq.mp3",
         source=fs(362624, "kermite607"), moment="stamp slap (APPROVED / SOLD / DONE)"),
    dict(out="hit_bong_low.wav", kind="hit", style="clean", src=KEN_IF / "bong_001.wav",
         source=SRC_KENNEY_IF, moment="strike / strike-through, low short thud"),
    dict(out="hit_deep_drop.wav", kind="hit", style="neutral", src=UISFX / "cinematic" / "drop.mp3",
         source=SRC_UISFX, moment="hook impact on the exact frame of a text hit or reveal"),
    # three UI pops (notify is a pop with a tail)
    dict(out="pop_chip.wav", kind="pop", style="neutral", src=UISFX / "organic" / "snap.mp3",
         source=SRC_UISFX, moment="chip pop (a tag or chip appears)"),
    dict(out="pop_select.wav", kind="pop", style="neutral", src=UISFX / "mechanical" / "select.mp3",
         source=SRC_UISFX, moment="list row / card element lands"),
    dict(out="notify_dm.wav", kind="notify", style="neutral", src=UISFX / "studio" / "receive.mp3",
         source=SRC_UISFX, moment="DM notify (a message card arrives)"),
    # two risers
    dict(out="riser_long.wav", kind="riser", style="gritty", src=OV / "fs_561207_10825267-hq.mp3",
         source=fs(561207, "Rizzard"), moment="riser into payoff, 2.0 s, peaks on its last 10 ms"),
    dict(out="riser_energy.wav", kind="riser", style="gritty", src=OV / "fs_522095_11537497-hq.mp3",
         source=fs(522095, "magnuswaker"), trim=(0.0, "peak+0.010"), fade_out_ms=4,
         moment="riser into payoff, short (0.84 s), cut hard at its own peak so it stops dead"),
]

EARSHOT_SRC = ("Earshot 1.0.0 (github.com/Leonxlnx/earshot) synthesised on this box, see earshot/COMMANDS.md",
               "https://github.com/Leonxlnx/earshot", "MIT code; rendered sounds free for any use, no credit")
EARSHOT = [
    dict(out="earshot/es_thud_diesel.wav", kind="hit", style="neutral", src=ESR / "thud_sub.wav", source=EARSHOT_SRC,
         moment="diesel-ish low thud hit (cut_hit/sub, 0.5 s)"),
    dict(out="earshot/es_clack.wav", kind="click", style="neutral", src=ESR / "clack.wav", source=EARSHOT_SRC,
         moment="short mechanical clack click (switch/small)"),
    dict(out="earshot/es_riser_1s.wav", kind="riser", style="neutral", src=ESR / "riser_chop.wav", source=EARSHOT_SRC,
         moment="1 s riser with a hard stop (pro_riser/chop, stops on its loudest 5 ms)"),
    dict(out="earshot/es_whoosh_paper.wav", kind="whoosh", style="neutral", src=ESR / "paper_whoosh.wav",
         source=EARSHOT_SRC, moment="soft paper whoosh (swipe/paper), card in on a quiet reel"),
]


def decode(path):
    cmd = [str(FFMPEG), "-v", "error", "-i", str(path), "-f", "f32le", "-ac", "2", "-ar", str(SR), "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).reshape(-1, 2).astype(np.float64)


def measure(x):
    mono = x.mean(axis=1)
    w = int(0.005 * SR)
    env = np.sqrt(np.convolve(mono ** 2, np.ones(w) / w, mode="same"))
    pk_i = int(env.argmax())
    pk_db = 20 * np.log10(max(float(np.abs(x).max()), 1e-9))
    w1 = int(0.001 * SR)
    env1 = np.sqrt(np.convolve(mono ** 2, np.ones(w1) / w1, mode="same"))
    top = env1.max()
    above30 = np.nonzero(env1 >= top * 10 ** (-30 / 20))[0]
    above50 = np.nonzero(env1 >= top * 10 ** (-50 / 20))[0]
    onset = int(above30[0]) if len(above30) else 0
    end = int(above50[-1]) if len(above50) else len(mono) - 1
    return dict(duration_s=round(len(mono) / SR, 4), onset_s=round(onset / SR, 4), peak_s=round(pk_i / SR, 4),
                end_s=round(end / SR, 4), peak_dbfs=round(pk_db, 2))


def write_wav24(path, x):
    x = np.clip(x, -1.0, 1.0)
    ints = np.round(x * 8388607.0).astype("<i4")
    arr = np.frombuffer(ints.tobytes(), dtype=np.uint8).reshape(-1, 4)[:, :3].tobytes()
    n = len(arr)
    hdr = (b"RIFF" + struct.pack("<I", 36 + n) + b"WAVE" + b"fmt "
           + struct.pack("<IHHIIHH", 16, 1, 2, SR, SR * 6, 6, 24))
    path.write_bytes(hdr + b"data" + struct.pack("<I", n) + arr)


def build(slot):
    x = decode(slot["src"])
    m0 = measure(x)
    trim = slot.get("trim")
    if trim:
        s, e = trim
        if isinstance(e, str) and e.startswith("peak+"):
            e = m0["peak_s"] + float(e[5:])
        a = int(s * SR)
        b = int(e * SR) if e is not None else len(x)
        x = x[a:b]
    # leading silence: cut anything more than 5 ms before the onset so "start at" means something
    m1 = measure(x)
    lead = int(max(0.0, m1["onset_s"] - 0.005) * SR)
    if lead > 0:
        x = x[lead:]
    x = x.copy()
    fo = slot.get("fade_out_ms")
    if fo:
        n = int(fo / 1000 * SR)
        x[-n:] *= np.linspace(1, 0, n)[:, None]
    fi = int(0.002 * SR)
    x[:fi] *= np.linspace(0, 1, fi)[:, None]
    x = x - x.mean(axis=0)  # DC
    target = 10 ** (PEAK[slot["kind"]] / 20)
    x = x / max(float(np.abs(x).max()), 1e-9) * target
    out = HERE / slot["out"]
    out.parent.mkdir(parents=True, exist_ok=True)
    write_wav24(out, x)
    m = measure(x)
    return dict(file=slot["out"].replace("\\", "/"), kind=slot["kind"], style=slot["style"], moment=slot["moment"],
                target_peak_dbfs=PEAK[slot["kind"]], source=slot["source"][0], source_url=slot["source"][1],
                license=slot["source"][2], source_file=str(slot["src"].relative_to(HERE)).replace("\\", "/"), **m)


def main():
    rows = [build(s) for s in SLOTS + EARSHOT]
    kit = {"name": "El Coyote SFX kit", "built": "2026-11-21", "sample_rate": SR, "channels": 2, "bits": 24,
           "peak_targets_dbfs": PEAK, "files": rows}
    (HERE / "kit.json").write_text(json.dumps(kit, indent=1), encoding="utf-8")
    md = ["# El Coyote SFX kit (KIT.md)", "",
          "Built 2026-11-21 by build_kit.py. 16 CC0 slots in five families plus four Earshot renders in earshot/.",
          "Every file is 48 kHz stereo 24-bit wav, DC removed, leading silence cut to 5 ms before the onset, "
          "peak-normalised to the house target for its kind.", "",
          "Peak targets (dBFS sample peak): whoosh -10, pop -12, stamp/hit -7, tick/click -17, notify -12, riser -12.",
          "Styles: gritty = real recording or physical mechanical sound, neutral = synthesised but physical in character, "
          "clean = bright digital UI. sfx_place.py refuses gritty + clean in one reel unless --mixed.", "",
          "Times are seconds inside the file. peak = loudest 5 ms, onset = first 1 ms within 30 dB of the peak, "
          "end = last 1 ms within 50 dB of the peak. sfx_place.py uses these to land each sound.", "",
          "| file | kind | style | moment | len s | onset s | peak s | end s | peak dBFS | source | license |",
          "|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        md.append(f"| {r['file']} | {r['kind']} | {r['style']} | {r['moment']} | {r['duration_s']:.3f} | "
                  f"{r['onset_s']:.3f} | {r['peak_s']:.3f} | {r['end_s']:.3f} | {r['peak_dbfs']:.1f} | "
                  f"[{r['source']}]({r['source_url']}) | {r['license']} |")
    md += ["", "## Moments to slots", "",
           "| moment | first pick | rotate with |", "|---|---|---|",
           "| card in | whoosh_card_in | earshot/es_whoosh_paper |",
           "| chip pop | pop_chip | pop_select |",
           "| stamp | stamp_rubber | (none, one stamp per reel) |",
           "| strike / strike-through | hit_bong_low | earshot/es_thud_diesel |",
           "| iris | whoosh_air_soft | whoosh_air_short |",
           "| DM notify | notify_dm | (none) |",
           "| cut whoosh | whoosh_air_short | whoosh_cloth, whoosh_air_soft |",
           "| hook impact | hit_deep_drop | earshot/es_thud_diesel |",
           "| riser into payoff | riser_long | riser_energy, earshot/es_riser_1s |",
           "| HUD tick / counter | tick_switch | tick_short (clean, do not mix with gritty) |",
           "| button / toggle click | click_press | earshot/es_clack |", "",
           "## Sources and licences", "",
           "- Kenney Interface Sounds, CC0, https://kenney.nl/assets/interface-sounds. Fetched from the GitHub mirror "
           "github.com/Calinou/kenney-interface-sounds (License.txt: Creative Commons Zero). The kenney.nl download "
           "button is JavaScript-gated (initiateDownload), so the mirror was used.",
           "- Kenney UI Audio, CC0, https://kenney.nl/assets/ui-audio. Fetched as UI_SFX_Set.zip from "
           "opengameart.org/content/51-ui-sound-effects-buttons-switches-and-clicks (listed CC0, uploader Kenney).",
           "- uisfx 0.4.0 (romainsimon), CC0 audio, bundled as vendor/node_modules/uisfx inside the Clipwing real-sfx "
           "skill (github.com/Clipwing/skills, scripts MIT). Note: uisfx sounds are deterministic synthesis, not "
           "recordings; the mechanical, organic, cinematic and studio packs read physical enough for us and are tagged "
           "neutral.",
           "- Freesound CC0 previews (128 kbps mp3) found through the Openverse API (api.openverse.org/v1/audio/, "
           "license=cc0). Credits in downloads/openverse/credits.txt. Confirm the licence on each Freesound page before "
           "a sponsor reel; the original wav needs a Freesound login.",
           "- Earshot renders: code MIT, output free for any use. Commands in earshot/COMMANDS.md.", ""]
    (HERE / "KIT.md").write_text("\n".join(md), encoding="utf-8")
    for r in rows:
        print(f"{r['file']:32} {r['kind']:7} {r['style']:8} len {r['duration_s']:.3f} onset {r['onset_s']:.3f} "
              f"peak {r['peak_s']:.3f} end {r['end_s']:.3f} {r['peak_dbfs']:+.1f} dBFS")


if __name__ == "__main__":
    main()
