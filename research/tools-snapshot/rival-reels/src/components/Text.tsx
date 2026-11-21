import React from "react";
import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate } from "remotion";
import { C, F, shadow } from "../theme";
import { prog, pop, tailFade, EASE_IN_OUT } from "./anim";

/* ---------- Kinetic hook: words slam in one at a time (Anton block caps) ---------- */
export const KineticHook: React.FC<{ words: string[]; dur: number; y?: number; size?: number; accent?: string; color?: string; align?: "center" | "right" | "left"; pad?: number }> = ({
  words, dur, y = 560, size = 150, accent, color = C.cream, align = "center", pad = 70,
}) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const step = Math.max(4, Math.floor((fps * 0.14)));
  const out = tailFade(frame, dur, 8);
  return (
    <AbsoluteFill style={{ justifyContent: "flex-start", alignItems: align === "right" ? "flex-end" : align === "left" ? "flex-start" : "center", paddingTop: y, paddingLeft: pad, paddingRight: pad, opacity: out }}>
      <div style={{ display: "flex", flexDirection: "column", alignItems: align === "right" ? "flex-end" : align === "left" ? "flex-start" : "center", gap: 0 }}>
        {words.map((w, i) => {
          const p = pop(frame, fps, i * step);
          const isAcc = accent && w.toUpperCase() === accent.toUpperCase();
          return (
            <div key={i} style={{
              fontFamily: F.block, fontSize: size, lineHeight: 0.92, letterSpacing: 2, color: isAcc ? C.tan : color,
              textTransform: "uppercase", transform: `translateY(${(1 - p) * 60}px) scale(${0.85 + 0.15 * p})`,
              opacity: Math.min(1, p * 1.4), textShadow: shadow,
            }}>{w}</div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- Script over block ("Create LOUDER") ---------- */
export const ScriptBlock: React.FC<{ script: string; block: string; sub?: string; dur: number; y?: number; tight?: boolean }> = ({ script, block, sub, dur, y = 520, tight = false }) => {   // tight: Harrison Niap's "overlap a little and reduce the kerning" (2026-11-21), a test option, the locked default stays
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const pb = pop(frame, fps, 0), ps = pop(frame, fps, 4), pu = pop(frame, fps, 9);
  const out = tailFade(frame, dur, 8);
  return (
    <AbsoluteFill style={{ alignItems: "center", paddingTop: y, opacity: out }}>
      <div style={{ position: "relative", display: "flex", flexDirection: "column", alignItems: "center" }}>
        <div style={{ fontFamily: F.block, fontSize: 380, lineHeight: 0.9, letterSpacing: tight ? -6 : 2, color: C.white, textShadow: shadow,
          transform: `scale(${0.96 + 0.04 * pb})`, opacity: pb, marginTop: 110 }}>{block}</div>
        <div style={{ position: "absolute", top: tight ? 10 : 0, fontFamily: F.script, fontSize: 190, color: C.yellow, textShadow: shadow,
          transform: `rotate(-4deg) scale(${0.92 + 0.08 * ps})`, opacity: ps, whiteSpace: "nowrap" }}>{script}</div>
        {sub && <div style={{ fontFamily: F.uiItalic, fontSize: 46, letterSpacing: 3, color: C.white, textTransform: "uppercase", marginTop: 26,
          opacity: pu, transform: `translateY(${(1 - pu) * 14}px)`, textShadow: shadow }}>{sub}</div>}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- Word stamp: one giant word, letters build in ---------- */
export const WordStamp: React.FC<{ text: string; dur: number; y?: number; size?: number; font?: string; color?: string; echo?: boolean }> = ({
  text, dur, y = 420, size = 230, font = F.block, color = C.cream, echo = false,
}) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const letters = text.split("");
  const out = tailFade(frame, dur, 8);
  return (
    <AbsoluteFill style={{ alignItems: "center", paddingTop: y, opacity: out }}>
      <div style={{ position: "relative" }}>
        {echo && <div style={{ position: "absolute", left: 10, top: 12, fontFamily: font, fontSize: size, color: C.tan, opacity: 0.35, letterSpacing: 2, whiteSpace: "nowrap" }}>{text}</div>}
        <div style={{ fontFamily: font, fontSize: size, color, letterSpacing: 2, whiteSpace: "nowrap", textShadow: shadow, display: "flex", maxWidth: 960, transform: "scale(var(--fit,1))" }}>
          {letters.map((ch, i) => {
            const p = pop(frame, fps, i);
            return <span key={i} style={{ display: "inline-block", transform: `translateY(${(1 - p) * 40}px)`, opacity: p, minWidth: ch === " " ? size * 0.3 : undefined }}>{ch}</span>;
          })}
        </div>
      </div>
    </AbsoluteFill>
  );
};

/* ---------- Caption pill: short phrase, key word in tan italic ---------- */
export const CaptionPill: React.FC<{ text: string; accent?: string; dur: number; y?: number }> = ({ text, accent, dur, y = 1230 }) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const p = pop(frame, fps, 0);
  const out = tailFade(frame, dur, 4);
  const parts = accent ? text.split(new RegExp(`(${accent.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")})`, "i")) : [text];
  return (
    <AbsoluteFill style={{ alignItems: "center", justifyContent: "flex-start", paddingTop: y, opacity: out }}>
      <div style={{
        background: C.oxblood, color: C.cream, fontFamily: F.ui, fontSize: 52, padding: "14px 30px", borderRadius: 14,
        boxShadow: shadow, transform: `translateY(${(1 - p) * 18}px) scale(${0.94 + 0.06 * p})`, opacity: p, maxWidth: 900, textAlign: "center", lineHeight: 1.2,
      }}>
        {parts.map((s, i) => (accent && s.toLowerCase() === accent.toLowerCase())
          ? <span key={i} style={{ fontFamily: F.uiItalic, color: C.tan }}>{s}</span>
          : <span key={i}>{s}</span>)}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- Numeral: giant chapter number with a micro label ---------- */
export const Numeral: React.FC<{ n: string; label?: string; dur: number; x?: number; y?: number }> = ({ n, label, dur, x = 760, y = 300 }) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const p = pop(frame, fps, 0); const out = tailFade(frame, dur, 8);
  return (
    <AbsoluteFill style={{ opacity: out }}>
      <div style={{ position: "absolute", left: x, top: y, textAlign: "center" }}>
        {label && <div style={{ fontFamily: F.ui, fontSize: 26, letterSpacing: 5, color: C.cream, textTransform: "uppercase", opacity: p }}>{label}</div>}
        <div style={{ fontFamily: F.block, fontSize: 300, lineHeight: 0.9, color: C.tan, textShadow: shadow, transform: `translateY(${(1 - p) * -60}px)`, opacity: p }}>{n}</div>
      </div>
    </AbsoluteFill>
  );
};

/* ---------- Title card: full-frame oxblood card ---------- */
export const TitleCard: React.FC<{ title: string; sub?: string; dur: number }> = ({ title, sub, dur }) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const p = pop(frame, fps, 0); const out = tailFade(frame, dur, 6);
  const wipe = interpolate(frame, [0, 6], [0, 1], { extrapolateRight: "clamp" });
  return (
    <AbsoluteFill style={{ opacity: out }}>
      <AbsoluteFill style={{ background: C.oxblood, transform: `scaleY(${wipe})`, transformOrigin: "top" }} />
      <AbsoluteFill style={{ justifyContent: "center", alignItems: "center", padding: 80 }}>
        <div style={{ fontFamily: F.block, fontSize: 170, color: C.cream, textAlign: "center", lineHeight: 0.95, letterSpacing: 2, textTransform: "uppercase", opacity: p, transform: `scale(${0.96 + 0.04 * p})` }}>{title}</div>
        {sub && <div style={{ fontFamily: F.uiItalic, fontSize: 44, color: C.tan, marginTop: 30, letterSpacing: 3, textTransform: "uppercase", opacity: p }}>{sub}</div>}
      </AbsoluteFill>
      <div style={{ position: "absolute", top: 300, left: 72, fontFamily: F.uiLight, fontSize: 24, color: C.tan, letterSpacing: 4 }}>EL COYOTE</div>
    </AbsoluteFill>
  );
};
