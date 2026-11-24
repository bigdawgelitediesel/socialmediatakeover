import React from "react";
import { AbsoluteFill, useCurrentFrame, useVideoConfig } from "remotion";
import { F } from "../theme";
import { prog, popSoft, tailFade, backOut, EASE_OUT } from "./anim";

/*
  Main.tsx (2026-11-23): Jacob's main title style, after @kalylsfilms DcBwAjvoEqI.
  Jacob: "I love these fonts and want them as my main fonts in my style guide!"
  Fonts: Impact (exact), round hand = Pinyon Script (stand-in for Snell Roundhand), brush = Permanent Marker (stand-in for Rocktown).
  Look: stacked Impact caps in yellow and red, one brush word in white laid across them at an angle, optional round-hand line on top.
  Everything stays in the rule 120 hook zone (y 0 to 620). Lines pop in one after another with a small overshoot;
  the brush word lands last, a touch late, like it was painted on.
*/

export const MAIN = { yellow: "#FDC43A", red: "#F04625", white: "#ffffff" };
type Col = "yellow" | "red" | "white";

/* lines: [{ text, color }]. cross: the brush word across the block. script: the round-hand line on top. hold: no fade out. */
export const MainLockup: React.FC<{ lines: { text: string; color?: Col }[]; cross?: string; script?: string; dur: number; y?: number; size?: number; maxW?: number; crossColor?: Col; hold?: boolean }> = ({
  lines, cross, script, dur, y = 110, size = 250, maxW = 900, crossColor = "white", hold = false,
}) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const fit = (t: string) => Math.min(size, Math.floor(maxW / (Math.max(1, t.length) * 0.5)));
  const sizes = lines.map((l) => fit(l.text));
  const y0 = y + (script ? 96 : 0);
  let top = y0; const tops = sizes.map((sz) => { const t = top; top += sz * 0.92; return t; });
  const blockH = top - y0;
  const cp = popSoft(frame, fps, 4 + lines.length * 3);
  const csz = Math.min(190, Math.floor(maxW / (Math.max(1, (cross || "").length) * 0.62)));
  const sh = "0 6px 24px rgba(0,0,0,0.45)";
  return (
    <AbsoluteFill style={{ opacity: hold ? 1 : tailFade(frame, dur, 6) }}>
      {script && <div style={{ position: "absolute", left: 0, right: 0, top: y - 14, textAlign: "center", fontFamily: F.round, fontSize: 104, lineHeight: 1, color: MAIN.yellow, textShadow: sh, opacity: prog(frame, 0, 8, EASE_OUT) }}>{script}</div>}
      {lines.map((l, i) => {
        const p = prog(frame, i * 3, 9, backOut(1.6));
        return <div key={i} style={{ position: "absolute", left: 0, right: 0, top: tops[i], textAlign: "center", fontFamily: F.impact, fontSize: sizes[i], lineHeight: 0.92, color: MAIN[l.color ?? (i % 2 ? "red" : "yellow")], textShadow: sh, whiteSpace: "nowrap", transform: `translateY(${(1 - p) * 60}px) scale(${0.9 + 0.1 * p})`, opacity: Math.min(1, p * 1.4) }}>{l.text}</div>;
      })}
      {cross && <div style={{ position: "absolute", left: 0, right: 0, top: y0 + blockH / 2 - csz * 0.62, textAlign: "center", fontFamily: F.brush, fontSize: csz, lineHeight: 1, color: MAIN[crossColor], whiteSpace: "nowrap", textShadow: "0 5px 0 rgba(0,0,0,0.35), 0 10px 26px rgba(0,0,0,0.5)", transform: `rotate(${-7 - (1 - cp) * 6}deg) skewX(-10deg) scale(${1.25 - 0.25 * cp})`, opacity: cp }}>{cross}</div>}
    </AbsoluteFill>
  );
};
