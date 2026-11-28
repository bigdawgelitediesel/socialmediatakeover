import React from "react";
import { AbsoluteFill, useCurrentFrame, useVideoConfig } from "remotion";
import { F } from "../theme";
import { prog, tailFade, expoOut, power2In, backOut } from "./anim";
import { MAIN } from "./Main";

/*
  Code.tsx (2026-11-24): beats for a reel, or a stretch of a reel, that is drawn from code with no footage under it.
  Source: @buildwithdarius.ai De4LyfdP5sY ("reels written as code and rendered frame by frame"). His build:
  claim, how it works, the objection typed out and struck through, the answer, real numbers counting up, the ask.
  Redrawn here in the El Coyote main fonts and colours (Impact, brush, yellow / red / white on black).

  Motion rules used (read from the HyperFrames motion notes, 2026-11-24, rewritten for this kit):
   - arrivals ease out hard (expoOut); exits are about half as long as arrivals and ease in
   - words arrive 2 frames apart, each from a 6 px blur to sharp in 4 frames
   - once a line has landed it does not move again; only the next thing moves
   - nothing readable below y 1572, nothing right of x 855 below y 640 (rule 120)
  House rules still apply: real numbers only, his real voice under it, no AI voice, no generated pictures.
*/

const SH = "0 6px 24px rgba(0,0,0,0.45)";
const exitOp = (frame: number, dur: number, n = 5) => 1 - power2In(Math.max(0, Math.min(1, (frame - (dur - n)) / n)));

/* A dark shop-floor backdrop for footage-free beats: near black, a warm pool of light, faint blueprint lines. */
export const Backdrop: React.FC<{ dur: number; glow?: string; grid?: boolean; hold?: boolean }> = ({ dur, glow = "rgba(201,179,140,0.16)", grid = true, hold = true }) => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill style={{ backgroundColor: "#0b0b0c", opacity: hold ? 1 : tailFade(frame, dur, 6) }}>
      <AbsoluteFill style={{ background: `radial-gradient(900px 760px at 50% 26%, ${glow}, rgba(0,0,0,0) 70%)` }} />
      {grid && <AbsoluteFill style={{ opacity: 0.07, backgroundImage: "linear-gradient(#c9b38c 1px, transparent 1px), linear-gradient(90deg, #c9b38c 1px, transparent 1px)", backgroundSize: "90px 90px" }} />}
      <AbsoluteFill style={{ background: "radial-gradient(1200px 1500px at 50% 45%, rgba(0,0,0,0) 55%, rgba(0,0,0,0.6) 100%)" }} />
    </AbsoluteFill>
  );
};

/* The objection: a quiet label, the doubt in Impact, a red line through it, then the answer brushed on.
   strikeAt and answerAt are seconds from the start of the beat. */
export const Objection: React.FC<{ label?: string; lines: string[]; answer: string; strikeAt?: number; answerAt?: number; dur: number; y?: number; size?: number; maxW?: number }> = ({
  label = "you might be thinking", lines, answer, strikeAt = 1.1, answerAt, dur, y = 150, size = 150, maxW = 940,
}) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const sF = Math.round(strikeAt * fps), aF = Math.round((answerAt ?? strikeAt + 0.35) * fps);
  const sz = Math.min(size, ...lines.map((l) => Math.floor(maxW / (Math.max(1, l.length) * 0.5))));
  const lh = sz * 0.96; const top = y + 74;
  const struck = prog(frame, sF, 7, expoOut);
  const ap = prog(frame, aF, 8, backOut(1.5));
  const asz = Math.min(Math.round(sz * 0.62), Math.floor(maxW / (Math.max(1, answer.length) * 0.66)));
  let wi = 0;
  return (
    <AbsoluteFill style={{ opacity: exitOp(frame, dur) }}>
      <div style={{ position: "absolute", left: 0, right: 0, top: y, textAlign: "center", fontFamily: F.ui, fontSize: 40, letterSpacing: 1, color: "#c9b38c", opacity: prog(frame, 0, 8, expoOut) }}>{label}</div>
      {lines.map((l, i) => (
        <div key={i} style={{ position: "absolute", left: 0, right: 0, top: top + i * lh, textAlign: "center", fontFamily: F.impact, fontSize: sz, lineHeight: 0.96, whiteSpace: "nowrap", textShadow: SH, color: "#fff", opacity: 1 - 0.55 * struck }}>
          <span style={{ position: "relative", display: "inline-block" }}>
            {l.split(" ").map((w, k) => { const p = prog(frame, 4 + (wi++) * 2, 4, expoOut); return <span key={k} style={{ display: "inline-block", marginRight: "0.22em", opacity: p, filter: `blur(${(1 - p) * 6}px)`, transform: `translateY(${(1 - p) * 14}px)` }}>{w}</span>; })}
            <span style={{ position: "absolute", left: "-2%", top: "47%", height: Math.max(8, sz * 0.085), width: `${struck * 102}%`, background: MAIN.red, borderRadius: 6, boxShadow: "0 3px 10px rgba(0,0,0,0.5)" }} />
          </span>
        </div>
      ))}
      <div style={{ position: "absolute", left: 0, right: 0, top: top + lines.length * lh + 26, textAlign: "center", fontFamily: F.brush, fontSize: asz, lineHeight: 1, whiteSpace: "nowrap", color: MAIN.yellow, textShadow: "0 4px 0 rgba(0,0,0,0.4), 0 10px 24px rgba(0,0,0,0.55)", transform: `rotate(${-4 - (1 - ap) * 4}deg) skewX(-8deg) scale(${1.18 - 0.18 * ap})`, opacity: Math.min(1, ap * 1.5) }}>{answer}</div>
    </AbsoluteFill>
  );
};

/* Real numbers, counting up, two to a row. Every number has to be one he can stand behind. */
export const StatTiles: React.FC<{ tiles: { to: number; label: string; prefix?: string; suffix?: string; color?: "yellow" | "red" | "white"; decimals?: number; group?: boolean }[]; dur: number; x?: number; y?: number; w?: number; every?: number; title?: string }> = ({
  tiles, dur, x = 80, y = 690, w = 760, every = 0.45, title,
}) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const gap = 20, tw = (w - gap) / 2, th = 250;
  return (
    <AbsoluteFill style={{ opacity: exitOp(frame, dur) }}>
      {title && <div style={{ position: "absolute", left: x, top: y - 62, width: w, fontFamily: F.ui, fontSize: 34, letterSpacing: 3, textTransform: "uppercase", color: "#c9b38c", opacity: prog(frame, 0, 8, expoOut) }}>{title}</div>}
      {tiles.map((t, i) => {
        const at = Math.round(i * every * fps); const p = prog(frame, at, 9, expoOut); const c = prog(frame, at + 2, 16, expoOut);
        const v = t.to * c; const txt = (t.decimals ? v.toFixed(t.decimals) : t.group === false ? String(Math.round(v)) : Math.round(v).toLocaleString("en-US"));
        return (
          <div key={i} style={{ position: "absolute", left: x + (i % 2) * (tw + gap), top: y + Math.floor(i / 2) * (th + gap), width: tw, height: th, borderRadius: 26, background: "rgba(28,28,31,0.94)", border: "2px solid rgba(201,179,140,0.35)", boxShadow: "0 18px 40px rgba(0,0,0,0.5)", opacity: p, transform: `translateY(${(1 - p) * 36}px)` }}>
            <div style={{ position: "absolute", left: 26, top: 22, fontFamily: F.ui, fontSize: 28, letterSpacing: 2, textTransform: "uppercase", color: "#a79f91" }}>{t.label}</div>
            <div style={{ position: "absolute", left: 24, right: 12, bottom: 14, fontFamily: F.impact, fontSize: 132, lineHeight: 1, color: MAIN[t.color ?? "yellow"], whiteSpace: "nowrap" }}>{t.prefix ?? ""}{txt}{t.suffix ?? ""}</div>
          </div>
        );
      })}
    </AbsoluteFill>
  );
};
