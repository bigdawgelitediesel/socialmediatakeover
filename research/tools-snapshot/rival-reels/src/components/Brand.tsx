import React from "react";
import { AbsoluteFill, Img, staticFile, useCurrentFrame, useVideoConfig, interpolate } from "remotion";
import { C, F, shadow, cardShadow } from "../theme";
import { pop, tailFade } from "./anim";

/* ---------- Logo badge: a small persistent brand mark (top-right by default, inside the IG safe zone) ---------- */
export const LogoBadge: React.FC<{ src: string; dur: number; x?: number; y?: number; size?: number; opacity?: number }> = ({ src, dur, x = 790, y = 300, size = 170, opacity = 0.95 }) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const p = pop(frame, fps, 0); const out = tailFade(frame, dur, 6);
  return (
    <AbsoluteFill style={{ opacity: out }}>
      <Img src={staticFile(src)} style={{ position: "absolute", left: x, top: y, width: size, height: size, objectFit: "contain", opacity: opacity * p, transform: `scale(${0.9 + 0.1 * p})`, filter: "drop-shadow(0 8px 20px rgba(0,0,0,0.45))" }} />
    </AbsoluteFill>
  );
};

/* ---------- Lower third: name + title on a brand bar, slides in from the left ---------- */
export const LowerThird: React.FC<{ name: string; title?: string; dur: number; x?: number; y?: number }> = ({ name, title, dur, x = 72, y = 1300 }) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const p = pop(frame, fps, 0), pt = pop(frame, fps, 5); const out = tailFade(frame, dur, 8);
  const slide = interpolate(p, [0, 1], [-60, 0]);
  return (
    <AbsoluteFill style={{ opacity: out }}>
      <div style={{ position: "absolute", left: x, top: y, transform: `translateX(${slide}px)`, opacity: p, display: "flex", alignItems: "stretch", boxShadow: cardShadow }}>
        <div style={{ width: 14, background: C.tan }} />
        <div style={{ background: "rgba(10,18,38,0.88)", padding: "16px 34px 18px 26px" }}>
          <div style={{ fontFamily: F.block, fontSize: 58, lineHeight: 1, color: C.cream, letterSpacing: 1, textTransform: "uppercase", textShadow: shadow }}>{name}</div>
          {title && <div style={{ fontFamily: F.ui, fontSize: 26, letterSpacing: 4, color: C.tan, textTransform: "uppercase", marginTop: 10, opacity: pt }}>{title}</div>}
        </div>
      </div>
    </AbsoluteFill>
  );
};

/* ---------- Quote bar: a short pull-quote with a gold rule, for the one line that matters ---------- */
export const QuoteBar: React.FC<{ text: string; dur: number; y?: number; size?: number }> = ({ text, dur, y = 330, size = 76 }) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const p = pop(frame, fps, 0); const out = tailFade(frame, dur, 8);
  return (
    <AbsoluteFill style={{ alignItems: "flex-start", paddingTop: y, paddingLeft: 72, paddingRight: 150, opacity: out }}>
      <div style={{ borderLeft: `12px solid ${C.tan}`, paddingLeft: 26, transform: `translateY(${(1 - p) * 20}px)`, opacity: p }}>
        <div style={{ fontFamily: F.block, fontSize: size, lineHeight: 1.02, color: C.cream, textTransform: "uppercase", textShadow: shadow, letterSpacing: 1 }}>{text}</div>
      </div>
    </AbsoluteFill>
  );
};
