import React from "react";
import { AbsoluteFill, useCurrentFrame, useVideoConfig } from "remotion";
import { F } from "../theme";
import { prog, popSoft, tailFade, backOut, EASE_OUT } from "./anim";

/*
  Main.tsx (2026-11-23): Jacob's main title style.
  Fonts: his pick from @kalylsfilms DcBwAjvoEqI. Impact (exact), round hand = Pinyon Script (stand-in for Snell Roundhand),
  brush = Permanent Marker (stand-in for Rocktown).

  PAIRING RULES (rule 123, after the @david_knowsai profile study and Jacob's "you need to learn how to properly pair text"):
   1. One loud, one quiet. Impact is the loud one. The partner is never louder than about half of the Impact height.
   2. The partner never covers the letters of the loud word. The brush word sits ON THE SEAM between two Impact lines
      (or hangs off the bottom edge of a single line), so both stay readable.
   3. One axis. Every line is centred on the same x, and the partner is centred on it too.
   4. Two colours plus white, the same three every time: yellow first line, red second line, white partner.
   5. Same place every reel: the top third (rule 120 zone, y 0 to 620).

  BEHIND-THE-BODY RULE (rule 124, Jacob 2026-11-23: "if my body is in the way of what you are going to post you need to
  put the title text behind me"): when his head or body reaches into the title area, list this overlay with behind: true
  (RivalReel draws it under the person cutout, so run tools/matte.py for the plate first). Never draw a title over him.
  Behind him the word must still read: keep the first and last letters clear of his head, and prefer `behind` on the
  Impact lines with the partner line placed in clear space above.
*/

export const MAIN = { yellow: "#FDC43A", red: "#F04625", white: "#ffffff" };
type Col = "yellow" | "red" | "white";

/* lines: [{ text, color }]. cross: the brush word on the seam. script: the round-hand line on top. hold: no fade out.
   part: draw only the Impact block ("block"), only the partners ("partners") or everything ("all"), so the block can go
   behind the person while the partner stays in front in clear space (list the overlay twice with the same props). */
export const MainLockup: React.FC<{ lines: { text: string; color?: Col }[]; cross?: string; script?: string; dur: number; y?: number; size?: number; maxW?: number; crossColor?: Col; hold?: boolean; part?: "all" | "block" | "partners" }> = ({
  lines, cross, script, dur, y = 110, size = 250, maxW = 900, crossColor = "white", hold = false, part = "all",
}) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const fit = (t: string) => Math.min(size, Math.floor(maxW / (Math.max(1, t.length) * 0.5)));
  const sizes = lines.map((l) => fit(l.text));
  const scriptSz = Math.min(104, Math.round(Math.max(...sizes) * 0.45) + 30);
  const y0 = y + (script ? scriptSz * 0.92 : 0);
  // a brush word on the seam needs room: open the gap between line 1 and line 2 a little
  const csz = cross ? Math.min(Math.round(Math.min(...sizes) * 0.52), Math.floor(maxW / (Math.max(1, cross.length) * 0.64))) : 0;
  const seamGap = cross && lines.length > 1 ? Math.round(csz * 0.42) : 0;
  let top = y0; const tops = sizes.map((sz, i) => { const t = top; top += sz * 0.92 + (i === 0 ? seamGap : 0); return t; });
  const seamY = lines.length > 1 ? tops[1] - seamGap / 2 - sizes[0] * 0.02 : top - sizes[0] * 0.06;
  const cp = popSoft(frame, fps, 4 + lines.length * 3);
  const sh = "0 6px 24px rgba(0,0,0,0.45)";
  const showBlock = part !== "partners", showPartners = part !== "block";
  return (
    <AbsoluteFill style={{ opacity: hold ? 1 : tailFade(frame, dur, 6) }}>
      {showPartners && script && <div style={{ position: "absolute", left: 0, right: 0, top: y - 14, textAlign: "center", fontFamily: F.round, fontSize: scriptSz, lineHeight: 1, color: MAIN.yellow, textShadow: sh, opacity: prog(frame, 0, 8, EASE_OUT) }}>{script}</div>}
      {showBlock && lines.map((l, i) => {
        const p = prog(frame, i * 3, 9, backOut(1.6));
        return <div key={i} style={{ position: "absolute", left: 0, right: 0, top: tops[i], textAlign: "center", fontFamily: F.impact, fontSize: sizes[i], lineHeight: 0.92, color: MAIN[l.color ?? (i % 2 ? "red" : "yellow")], textShadow: sh, whiteSpace: "nowrap", transform: `translateY(${(1 - p) * 60}px) scale(${0.9 + 0.1 * p})`, opacity: Math.min(1, p * 1.4) }}>{l.text}</div>;
      })}
      {showPartners && cross && <div style={{ position: "absolute", left: 0, right: 0, top: seamY - csz * 0.56, textAlign: "center", fontFamily: F.brush, fontSize: csz, lineHeight: 1, color: MAIN[crossColor], whiteSpace: "nowrap", textShadow: "0 4px 0 rgba(0,0,0,0.4), 0 10px 24px rgba(0,0,0,0.55)", transform: `rotate(${-4 - (1 - cp) * 5}deg) skewX(-8deg) scale(${1.2 - 0.2 * cp})`, opacity: cp }}>{cross}</div>}
    </AbsoluteFill>
  );
};
