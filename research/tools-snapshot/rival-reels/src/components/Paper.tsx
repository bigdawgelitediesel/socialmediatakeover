import React from "react";
import { AbsoluteFill, Img, OffthreadVideo, staticFile, useCurrentFrame, useVideoConfig, interpolate } from "remotion";
import { C, F, cardShadow } from "../theme";
import { prog, tailFade, backOut, power4Out, popSoft } from "./anim";
import { mono } from "./Menu";

/*
  Paper.tsx: the paper-background explainer grammar learned 2026-11-21 from
    @guipaulinooo "Teardown" reel (research/reel-references/2026-11-21-DfLmQwWp5E8)
  Cream paper, window-chrome cards with a floating shadow, one clause per scene, cursor-driven screen captures.
  Palette stays El Coyote. Use with CardReel bg "paper" (or a blurred plate) and PlainCaption variant "sans" + accentFont "serif".
*/

const WIN_LIGHT = { bg: "#fbf8f1", bar: "#ece6d8", text: "#6b665c" };
const WIN_DARK = { bg: C.ink, bar: "#1f1f21", text: "#9a948a" };
const winShadow = "0 24px 60px rgba(20,20,20,0.22), 0 2px 6px rgba(20,20,20,0.12)";

/* Window chrome (three dots + a title) around an image or a clip. */
const Window: React.FC<{ title?: string; dark?: boolean; w: number; h?: number; src?: string; atF?: number; children?: React.ReactNode; radius?: number }> = ({ title, dark = false, w, h, src, atF = 0, children, radius = 18 }) => {
  const t = dark ? WIN_DARK : WIN_LIGHT;
  return (
    <div style={{ width: w, borderRadius: radius, background: t.bg, boxShadow: winShadow, overflow: "hidden" }}>
      <div style={{ height: 34, background: t.bar, display: "flex", alignItems: "center", padding: "0 14px", gap: 7 }}>
        <span style={{ width: 10, height: 10, borderRadius: 5, background: "#e2543e" }} /><span style={{ width: 10, height: 10, borderRadius: 5, background: "#f7d43c" }} /><span style={{ width: 10, height: 10, borderRadius: 5, background: "#7bb36a" }} />
        {title && <span style={{ marginLeft: "auto", marginRight: "auto", fontFamily: mono, fontSize: 15, color: t.text }}>{title}</span>}
      </div>
      <div style={{ position: "relative", width: w, height: h ?? Math.round(w * 9 / 16), overflow: "hidden" }}>
        {src && (/\.(mp4|webm|mov)$/i.test(src)
          ? <OffthreadVideo src={staticFile(src)} startFrom={atF} muted style={{ width: "100%", height: "100%", objectFit: "cover" }} />
          : <Img src={staticFile(src)} style={{ width: "100%", height: "100%", objectFit: "cover" }} />)}
        {children}
      </div>
    </div>
  );
};

/* ---------- WindowStack: windows fan in one at a time (each on its word), offset down-right, with a label pill in the corner.
   guipaulinooo 0:14 to 0:16: "a V8 engine" / "a landing gear" / "a walking robot", each new window lands 0.35 s back.out and the older ones stay. ---------- */
export const WindowStack: React.FC<{ items: { src: string; label?: string; title?: string; at: number; atF?: number }[]; dur: number; x?: number; y?: number; w?: number; dx?: number; dy?: number; dark?: boolean }> = ({
  items, dur, x = 60, y = 560, w = 600, dx = 120, dy = 170, dark = false,   // 3 windows end at x 900, inside the right safe line (950)
}) => {
  const frame = useCurrentFrame(); const out = tailFade(frame, dur, 6);
  return (
    <AbsoluteFill style={{ opacity: out }}>
      {items.map((it, i) => {
        const p = prog(frame, it.at, 11, backOut(1.7));
        if (p <= 0) return null;
        const pill = prog(frame, it.at + 8, 7, backOut(2));
        return (
          <div key={i} style={{ position: "absolute", left: x + i * dx, top: y + i * dy, transform: `translateY(${(1 - p) * 60}px) scale(${0.92 + 0.08 * p})`, opacity: Math.min(1, p * 1.4) }}>
            <Window w={w} src={it.src} atF={it.atF} title={it.title} dark={dark} />
            {it.label && (
              <div style={{ position: "absolute", left: 16, bottom: 16, fontFamily: F.uiSemi, fontSize: 22, color: C.cream, background: C.ink, borderRadius: 14, padding: "6px 14px", transform: `scale(${0.6 + 0.4 * pill})`, opacity: pill, transformOrigin: "left bottom" }}>{it.label}</div>
            )}
          </div>
        );
      })}
    </AbsoluteFill>
  );
};

/* ---------- PinThumb: a real photo lands big as a polaroid with a handwritten line, then shrinks into a corner and stays as a "reference" chip.
   guipaulinooo 0:19 to 0:27: "one real picture" polaroid, then a 150 px thumb top right with a ✓ reference tag for the next 7 s.
   For Rival: the real photo of the part stays pinned while the explanation runs. ---------- */
export const PinThumb: React.FC<{ src: string; note?: string; tag?: string; dur: number; pinAt?: number; corner?: "tr" | "tl"; bigW?: number; thumbW?: number }> = ({
  src, note = "one real picture", tag = "reference", dur, pinAt = 60, corner = "tr", bigW = 600, thumbW = 170,   // 600 wide: a 4:5 photo ends near y 1260, clear of a caption at 1400+
}) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig(); const out = tailFade(frame, dur, 6);
  const land = popSoft(frame, fps, 0);
  const pin = prog(frame, pinAt, 14, power4Out);
  const bigX = (1080 - bigW) / 2, bigY = 440;
  const thumbX = corner === "tr" ? 1080 - 130 - thumbW : 72, thumbY = 300;
  const w = interpolate(pin, [0, 1], [bigW, thumbW]);
  const x = interpolate(pin, [0, 1], [bigX, thumbX]);
  const yy = interpolate(pin, [0, 1], [bigY, thumbY]);
  const rot = interpolate(pin, [0, 1], [-3, 0]);
  const pad = interpolate(pin, [0, 1], [18, 6]);
  const noteOp = 1 - prog(frame, pinAt, 6);
  const tagP = prog(frame, pinAt + 12, 7, backOut(2));
  return (
    <AbsoluteFill style={{ opacity: out }}>
      <div style={{ position: "absolute", left: x, top: yy, width: w, padding: pad, paddingBottom: pad + (1 - pin) * 70, background: "#fff", boxShadow: cardShadow, transform: `rotate(${rot}deg) translateY(${(1 - land) * 50}px) scale(${0.9 + 0.1 * land})`, opacity: land }}>
        <Img src={staticFile(src)} style={{ width: "100%", display: "block" }} />
        {noteOp > 0 && <div style={{ position: "absolute", left: 0, right: 0, bottom: 18, textAlign: "center", fontFamily: F.script, fontSize: 38, color: C.hi, opacity: noteOp }}>{note}</div>}
        {tagP > 0 && (
          <div style={{ position: "absolute", right: -22, bottom: -16, fontFamily: F.uiSemi, fontSize: 20, color: C.ink, background: "#fff", borderRadius: 12, padding: "4px 12px", boxShadow: "0 4px 14px rgba(0,0,0,0.18)", transform: `scale(${0.6 + 0.4 * tagP})`, opacity: tagP, whiteSpace: "nowrap" }}>
            <span style={{ color: "#2f8f4e", marginRight: 6 }}>✓</span>{tag}
          </div>
        )}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- Terminal: a dark window, a command types out 0.07 s per character behind a prompt, then a green result line lands.
   guipaulinooo 0:09 to 0:11 ("npx skills add ... / ✓ teardown installed") and 0:12 to 0:13 ("/teardown build a V8 engine"). ---------- */
export const Terminal: React.FC<{ cmd: string; result?: string; title?: string; dur: number; x?: number; y?: number; w?: number; typeAt?: number; perChar?: number; prompt?: string; highlight?: string }> = ({
  cmd, result, title = "Terminal", dur, x = 72, y = 640, w = 936, typeAt = 6, perChar = 2, prompt = "$", highlight,
}) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig(); const out = tailFade(frame, dur, 6);
  const p = popSoft(frame, fps, 0);
  const n = Math.max(0, Math.min(cmd.length, Math.floor((frame - typeAt) / perChar)));
  const done = typeAt + cmd.length * perChar;
  const typed = frame >= done;
  const res = prog(frame, done + 8, 6);
  const shown = cmd.slice(0, n);
  const hiIdx = highlight ? shown.toLowerCase().indexOf(highlight.toLowerCase()) : -1;
  const lines = 1 + (result ? 1 : 0);
  return (
    <AbsoluteFill style={{ opacity: out }}>
      <div style={{ position: "absolute", left: x, top: y, transform: `translateY(${(1 - p) * 40}px) scale(${0.94 + 0.06 * p})`, opacity: p }}>
        <Window w={w} h={70 + lines * 46} title={title} dark>
          <div style={{ padding: "22px 26px", fontFamily: mono, fontSize: 27, color: C.cream, lineHeight: 1.7, whiteSpace: "pre" }}>
            <span style={{ color: C.hi }}>{prompt} </span>
            {hiIdx >= 0 ? (<>{shown.slice(0, hiIdx)}<span style={{ background: "rgba(226,84,62,0.28)", borderRadius: 6, padding: "0 6px" }}>{shown.slice(hiIdx, hiIdx + highlight!.length)}</span>{shown.slice(hiIdx + highlight!.length)}</>) : shown}
            <span style={{ opacity: typed ? 0 : (Math.floor(frame / 4) % 2), color: C.hi }}>▌</span>
            {result && res > 0 && <div style={{ color: "#7bb36a", opacity: res, transform: `translateY(${(1 - res) * 8}px)` }}>✓ {result}</div>}
          </div>
        </Window>
      </div>
    </AbsoluteFill>
  );
};

/* ---------- RepoCard: the open-source credit card. Dark sticker: "owner / name", one-line description, star count, licence, a tilted FREE stamp
   and a "built by @handle" credit pill. The credit pill is the repostability move: the builder gets named on screen, so he reshares.
   guipaulinooo 0:07 to 0:11. For Rival, the same card credits a partner's product page or a fabricator. ---------- */
export const RepoCard: React.FC<{ owner: string; name: string; desc?: string; stars?: string; licence?: string; stamp?: string; credit?: string; dur: number; x?: number; y?: number; w?: number; stampAt?: number; creditAt?: number }> = ({
  owner, name, desc, stars, licence, stamp, credit, dur, x = 72, y = 560, w = 936, stampAt = 50, creditAt = 70,
}) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig(); const out = tailFade(frame, dur, 6);
  const p = popSoft(frame, fps, 0);
  const st = prog(frame, stampAt, 8, power4Out);
  const cr = prog(frame, creditAt, 9, backOut(1.7));
  return (
    <AbsoluteFill style={{ opacity: out }}>
      <div style={{ position: "absolute", left: x, top: y, width: w, transform: `translateY(${(1 - p) * 40}px) scale(${0.94 + 0.06 * p})`, opacity: p }}>
        <div style={{ borderRadius: 18, background: C.ink, boxShadow: winShadow, padding: "28px 32px", color: C.cream }}>
          <div style={{ fontFamily: mono, fontSize: 20, color: "#9a948a" }}>{owner} /</div>
          <div style={{ fontFamily: F.uiSemi, fontSize: 56, lineHeight: 1.1, marginTop: 4 }}>{name}</div>
          {desc && <div style={{ fontFamily: F.ui, fontSize: 24, color: "#cfc8ba", marginTop: 10, lineHeight: 1.35 }}>{desc}</div>}
          {(stars || licence) && (
            <div style={{ display: "flex", gap: 10, marginTop: 18 }}>
              {stars && <span style={{ fontFamily: mono, fontSize: 18, border: "1px solid #4a4742", borderRadius: 8, padding: "4px 10px" }}>★ {stars}</span>}
              {licence && <span style={{ fontFamily: mono, fontSize: 18, border: "1px solid #4a4742", borderRadius: 8, padding: "4px 10px" }}>{licence}</span>}
            </div>
          )}
        </div>
        {stamp && st > 0 && (
          <div style={{ position: "absolute", right: -16, top: -26, fontFamily: F.heavy, fontSize: 34, letterSpacing: 2, color: "#2f8f4e", border: "4px solid #2f8f4e", borderRadius: 10, padding: "4px 14px", background: "rgba(251,248,241,0.92)", transform: `rotate(${-14 + 4 * st}deg) scale(${2.2 - 1.2 * st})`, opacity: st, transformOrigin: "center" }}>{stamp}</div>
        )}
        {credit && cr > 0 && (
          <div style={{ position: "absolute", left: 0, bottom: -52, fontFamily: F.uiSemi, fontSize: 20, color: C.cream, background: C.ink, borderRadius: 12, padding: "6px 14px", transform: `translateY(${(1 - cr) * 16}px)`, opacity: cr }}>built by <span style={{ color: C.hi }}>{credit}</span></div>
        )}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- SpecChips: a row of white chips, bold number + serif italic unit, each popping on its word. The "from real numbers" proof.
   guipaulinooo 0:26 to 0:27: "32 teeth" "108 mm" "201 mm" "177°". For Rival: "0.030 over" "275 cc" "38R" "7,400 rpm" under the part window. ---------- */
export const SpecChips: React.FC<{ chips: { n: string; unit?: string; at: number }[]; dur: number; x?: number; y?: number; size?: number }> = ({ chips, dur, x = 72, y = 1040, size = 34 }) => {
  const frame = useCurrentFrame(); const out = tailFade(frame, dur, 6);
  return (
    <AbsoluteFill style={{ opacity: out }}>
      <div style={{ position: "absolute", left: x, top: y, display: "flex", gap: 14, flexWrap: "wrap", width: 1080 - x - 72 }}>
        {chips.map((c, i) => {
          const p = prog(frame, c.at, 8, backOut(3));
          if (p <= 0) return null;
          return (
            <div key={i} style={{ background: "#fff", borderRadius: 14, padding: "8px 18px", boxShadow: "0 6px 18px rgba(20,20,20,0.14)", transform: `scale(${0.7 + 0.3 * p}) translateY(${(1 - p) * 10}px)`, opacity: p, display: "flex", alignItems: "baseline", gap: 8 }}>
              <span style={{ fontFamily: F.uiSemi, fontSize: size, color: C.ink, fontVariantNumeric: "tabular-nums" }}>{c.n}</span>
              {c.unit && <span style={{ fontFamily: F.serif, fontSize: size * 1.05, color: C.hi }}>{c.unit}</span>}
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- NotePill: one small dark annotation under a window ("every gauge = live"). The = sign is the joke: label equals state. ---------- */
export const NotePill: React.FC<{ text: string; accent?: string; dur: number; x?: number; y?: number }> = ({ text, accent, dur, x = 540, y = 1000 }) => {
  const frame = useCurrentFrame(); const out = tailFade(frame, dur, 5);
  const p = prog(frame, 0, 8, backOut(2));
  const parts = accent ? text.split(accent) : [text];
  return (
    <AbsoluteFill style={{ opacity: out }}>
      <div style={{ position: "absolute", left: x, top: y, transform: `translate(-50%, 0) scale(${0.7 + 0.3 * p})`, opacity: p, fontFamily: F.uiSemi, fontSize: 22, color: C.cream, background: C.ink, borderRadius: 12, padding: "6px 14px", whiteSpace: "nowrap" }}>
        {parts.length > 1 ? (<>{parts[0]}<span style={{ color: C.hi, background: "rgba(226,84,62,0.18)", borderRadius: 6, padding: "0 6px" }}>{accent}</span>{parts[1]}</>) : text}
      </div>
    </AbsoluteFill>
  );
};
