import React from "react";
import { AbsoluteFill, Img, staticFile, useCurrentFrame, useVideoConfig, interpolate } from "remotion";
import { C, F, cardShadow } from "../theme";
import { pop, tailFade, prog } from "./anim";

const Card: React.FC<{ x: number; y: number; w: number; tilt?: number; delay?: number; dur: number; children: React.ReactNode; bg?: string; pad?: number }> = ({
  x, y, w, tilt = -3, delay = 0, dur, children, bg = C.cream, pad = 28,
}) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const p = pop(frame, fps, delay); const out = tailFade(frame, dur, 8);
  return (
    <div style={{
      position: "absolute", left: x, top: y, width: w, background: bg, borderRadius: 22, padding: pad, boxShadow: cardShadow,
      transform: `translateY(${(1 - p) * 50}px) rotate(${tilt * p}deg) scale(${0.9 + 0.1 * p})`, opacity: p * out,
    }}>{children}</div>
  );
};

/* ---------- Logo card: partner logo on a cream card with a label ---------- */
export const LogoCard: React.FC<{ src: string; label?: string; dur: number; x?: number; y?: number; w?: number; tilt?: number }> = ({ src, label, dur, x = 120, y = 330, w = 840, tilt = -3 }) => (
  <AbsoluteFill>
    <Card x={x} y={y} w={w} tilt={tilt} dur={dur} pad={36}>
      <Img src={staticFile(src)} style={{ width: "100%", display: "block" }} />
      {label && <div style={{ fontFamily: F.ui, fontSize: 30, letterSpacing: 4, color: C.ink, textTransform: "uppercase", marginTop: 22, textAlign: "center" }}>{label}</div>}
    </Card>
  </AbsoluteFill>
);

/* ---------- Photo card: a photo with a caption strip ---------- */
export const PhotoCard: React.FC<{ src: string; caption?: string; dur: number; x?: number; y?: number; w?: number; tilt?: number }> = ({ src, caption, dur, x = 140, y = 300, w = 800, tilt = 2 }) => (
  <AbsoluteFill>
    <Card x={x} y={y} w={w} tilt={tilt} dur={dur} pad={16}>
      <Img src={staticFile(src)} style={{ width: "100%", display: "block", borderRadius: 12 }} />
      {caption && <div style={{ fontFamily: F.uiItalic, fontSize: 32, color: C.ink, marginTop: 14, textAlign: "center" }}>{caption}</div>}
    </Card>
  </AbsoluteFill>
);

/* ---------- Spec card: title + rows that tick in one by one ---------- */
export const SpecCard: React.FC<{ title: string; rows: string[]; dur: number; x?: number; y?: number; w?: number; tilt?: number }> = ({ title, rows, dur, x = 90, y = 320, w = 900, tilt = -2 }) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  return (
    <AbsoluteFill>
      <Card x={x} y={y} w={w} tilt={tilt} dur={dur} pad={34}>
        <div style={{ fontFamily: F.block, fontSize: 64, color: C.oxblood, letterSpacing: 2, textTransform: "uppercase", lineHeight: 1 }}>{title}</div>
        <div style={{ height: 4, width: 70, background: C.tan, margin: "14px 0 18px" }} />
        {rows.map((r, i) => {
          const p = pop(frame, fps, 6 + i * 5);
          return (
            <div key={i} style={{ display: "flex", alignItems: "center", gap: 18, fontFamily: F.ui, fontSize: 40, color: C.ink, lineHeight: 1.5, opacity: p, transform: `translateX(${(1 - p) * -20}px)` }}>
              <div style={{ width: 16, height: 16, borderRadius: 8, background: C.oxblood, flexShrink: 0 }} />
              <span>{r}</span>
            </div>
          );
        })}
      </Card>
    </AbsoluteFill>
  );
};

/* ---------- Strike list: items get crossed out one by one ---------- */
export const StrikeList: React.FC<{ title?: string; items: string[]; dur: number; x?: number; y?: number; w?: number; strikeFrom?: number }> = ({ title, items, dur, x = 110, y = 340, w = 860, strikeFrom = 14 }) => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill>
      <Card x={x} y={y} w={w} tilt={-2} dur={dur} pad={34}>
        {title && <div style={{ fontFamily: F.ui, fontSize: 28, letterSpacing: 5, color: C.oxblood, textTransform: "uppercase", marginBottom: 12 }}>{title}</div>}
        {items.map((it, i) => {
          const s = prog(frame, strikeFrom + i * 9, 7);
          return (
            <div key={i} style={{ position: "relative", fontFamily: F.ui, fontSize: 56, color: C.ink, lineHeight: 1.45, display: "inline-block", marginRight: 30 }}>
              {it}
              <div style={{ position: "absolute", left: -6, top: "52%", height: 7, width: `${s * 104}%`, background: C.oxblood, borderRadius: 4, transform: "rotate(-3deg)" }} />
            </div>
          );
        })}
      </Card>
    </AbsoluteFill>
  );
};

/* ---------- Browser card: a screenshot in a browser frame, optional cursor click ---------- */
export const BrowserCard: React.FC<{ src: string; url: string; dur: number; click?: { x: number; y: number; at: number }; x?: number; y?: number; w?: number }> = ({ src, url, dur, click, x = 60, y = 300, w = 960 }) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const ring = click ? interpolate(frame, [click.at, click.at + 10], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }) : 0;
  return (
    <AbsoluteFill>
      <Card x={x} y={y} w={w} tilt={0} dur={dur} pad={0} bg={C.cream}>
        <div style={{ display: "flex", alignItems: "center", gap: 10, padding: "14px 18px", borderBottom: `2px solid ${C.tan}` }}>
          {[C.oxblood, C.tan, C.ink].map((c, i) => <div key={i} style={{ width: 16, height: 16, borderRadius: 8, background: c, opacity: 0.8 }} />)}
          <div style={{ marginLeft: 16, fontFamily: F.ui, fontSize: 26, color: C.ink, background: "#fff", borderRadius: 10, padding: "6px 16px", flex: 1 }}>{url}</div>
        </div>
        <div style={{ position: "relative" }}>
          <Img src={staticFile(src)} style={{ width: "100%", display: "block", borderRadius: "0 0 22px 22px" }} />
          {click && (
            <>
              <div style={{ position: "absolute", left: click.x - 30, top: click.y - 30, width: 60, height: 60, borderRadius: 30, border: `5px solid ${C.oxblood}`, transform: `scale(${0.4 + ring * 1.2})`, opacity: 1 - ring }} />
              <div style={{ position: "absolute", left: click.x, top: click.y, fontSize: 44, transform: `translate(-6px,-6px) scale(${frame >= click.at ? 0.92 : 1})` }}>🖱</div>
            </>
          )}
        </div>
      </Card>
    </AbsoluteFill>
  );
};

/* ---------- Prompt bar: a chat input that types what he says ---------- */
export const PromptBar: React.FC<{ text: string; label?: string; dur: number; y?: number; sentAt?: number }> = ({ text, label = "TO CLAUDE", dur, y = 330, sentAt }) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const p = pop(frame, fps, 0); const out = tailFade(frame, dur, 6);
  const n = Math.floor(interpolate(frame, [6, 6 + text.length * 1.3], [0, text.length], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }));
  const sent = sentAt !== undefined && frame >= sentAt;
  return (
    <AbsoluteFill style={{ alignItems: "center", paddingTop: y, opacity: out }}>
      <div style={{ width: 760, marginLeft: -200, background: C.cream, borderRadius: 40, padding: "22px 30px", boxShadow: cardShadow, transform: `translateY(${(1 - p) * 30}px)`, opacity: p, display: "flex", alignItems: "center", gap: 20 }}>
        <div style={{ flex: 1 }}>
          <div style={{ fontFamily: F.ui, fontSize: 20, letterSpacing: 4, color: sent ? C.tan : C.oxblood }}>{sent ? "SENT" : label}</div>
          <div style={{ fontFamily: F.ui, fontSize: 40, color: C.ink, minHeight: 50 }}>{text.slice(0, n)}{!sent && frame % 16 < 8 ? "|" : ""}</div>
        </div>
        <div style={{ width: 64, height: 64, borderRadius: 32, background: sent ? C.tan : C.oxblood, color: C.cream, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 34 }}>{sent ? "✓" : "↑"}</div>
      </div>
    </AbsoluteFill>
  );
};

/* ---------- Comment drop: a comment box with a typed word ---------- */
export const CommentDrop: React.FC<{ word: string; dur: number; y?: number; handle?: string }> = ({ word, dur, y = 360, handle = "you" }) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const p = pop(frame, fps, 0); const out = tailFade(frame, dur, 6);
  const n = Math.floor(interpolate(frame, [8, 8 + word.length * 3], [0, word.length], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }));
  return (
    <AbsoluteFill style={{ alignItems: "center", paddingTop: y, opacity: out }}>
      <div style={{ width: 760, marginLeft: -200, background: "#fff", borderRadius: 24, padding: "20px 26px", boxShadow: cardShadow, transform: `translateY(${(1 - p) * 30}px)`, opacity: p, display: "flex", alignItems: "center", gap: 18 }}>
        <div style={{ width: 56, height: 56, borderRadius: 28, background: C.oxblood }} />
        <div style={{ flex: 1 }}>
          <div style={{ fontFamily: F.ui, fontSize: 22, color: "#777" }}>{handle} · now</div>
          <div style={{ fontFamily: F.uiSemi, fontSize: 40, color: C.ink }}>{word.slice(0, n)}</div>
        </div>
        <div style={{ fontFamily: F.ui, fontSize: 22, color: C.oxblood, border: `2px solid ${C.oxblood}`, borderRadius: 14, padding: "6px 16px" }}>Post</div>
      </div>
    </AbsoluteFill>
  );
};

/* ---------- Countdown card: big number + label (SEMA days) ---------- */
export const CountCard: React.FC<{ n: number; label: string; dur: number; x?: number; y?: number }> = ({ n, label, dur, x = 90, y = 320 }) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const p = pop(frame, fps, 0);
  const v = Math.round(interpolate(frame, [4, 26], [0, n], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }));
  return (
    <AbsoluteFill>
      <Card x={x} y={y} w={900} tilt={-2} dur={dur} bg={C.oxblood} pad={36}>
        <div style={{ fontFamily: F.block, fontSize: 260, lineHeight: 0.9, color: C.cream, opacity: p }}>{v}</div>
        <div style={{ fontFamily: F.uiItalic, fontSize: 38, letterSpacing: 4, color: C.tan, textTransform: "uppercase", marginTop: 10 }}>{label}</div>
      </Card>
    </AbsoluteFill>
  );
};
