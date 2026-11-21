import React from "react";
import { AbsoluteFill, Img, OffthreadVideo, staticFile, useCurrentFrame, useVideoConfig, interpolate } from "remotion";
import { C, F, shadow, cardShadow } from "../theme";
import { pop, tailFade, prog, EASE_IN_OUT } from "./anim";

/* Components learned from @chandlerintelligence "Giving away EVERY WORKFLOW" (reel De8SPjEAuV0, studied 2026-11-20).
   See socialmediatakeover/research/reel-references/2026-11-20-chandlerintelligence-every-workflow/BREAKDOWN.md
   Every component receives `dur` (frames), `atF` (absolute start frame of its Sequence) and `plate` (the plate file)
   from RivalReel so video copies can stay in sync with the plate. */

const textShadow = "0 2px 4px rgba(0,0,0,0.6), 0 8px 24px rgba(0,0,0,0.45)";

/* ---------- Plain caption: white bold sans + shadow, no pill ("I'd lose the green box. Plain text with shadow looks way cleaner.") ---------- */
export const PlainCaption: React.FC<{ text: string; accent?: string; dur: number; y?: number; size?: number; hiColor?: string }> = ({
  text, accent, dur, y = 1150, size = 60, hiColor = "#e2543e",
}) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const p = pop(frame, fps, 0);
  const out = tailFade(frame, dur, 3);
  const parts = accent ? text.split(new RegExp(`(${accent.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")})`, "i")) : [text];
  return (
    <AbsoluteFill style={{ alignItems: "center", justifyContent: "flex-start", paddingTop: y, opacity: out }}>
      <div style={{
        fontFamily: F.uiSemi, fontSize: size, color: C.white, textAlign: "center", lineHeight: 1.2, maxWidth: 900, textShadow,
        transform: `translateY(${(1 - p) * 10}px) scale(${0.96 + 0.04 * p})`, opacity: Math.min(1, p * 1.5),
      }}>
        {parts.map((s, i) => (accent && s.toLowerCase() === accent.toLowerCase())
          ? <span key={i} style={{ background: hiColor, padding: "2px 14px", borderRadius: 10, textShadow: "none" }}>{s}</span>
          : <span key={i}>{s}</span>)}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- Tool tag: icon + name at top center the moment a tool/partner is named ---------- */
export const ToolTag: React.FC<{ icon?: string; name: string; dur: number; y?: number; size?: number }> = ({ icon, name, dur, y = 340, size = 92 }) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const pi = pop(frame, fps, 0), pt = pop(frame, fps, 4); const out = tailFade(frame, dur, 6);
  return (
    <AbsoluteFill style={{ alignItems: "center", paddingTop: y, opacity: out }}>
      <div style={{ display: "flex", alignItems: "center", gap: 26 }}>
        {icon && <Img src={staticFile(icon)} style={{ width: size * 1.6, height: size * 1.6, objectFit: "contain", borderRadius: 30, boxShadow: shadow, transform: `scale(${pi})`, opacity: pi }} />}
        <div style={{ fontFamily: F.uiSemi, fontSize: size, color: C.white, textShadow, transform: `translateX(${(1 - pt) * -20}px)`, opacity: pt, whiteSpace: "nowrap" }}>{name}</div>
      </div>
    </AbsoluteFill>
  );
};

/* ---------- Outline word: huge hollow caps, meant to sit BEHIND the head (behind: true) ---------- */
export const OutlineWord: React.FC<{ text: string; dur: number; y?: number; size?: number; stroke?: number; color?: string }> = ({ text, dur, y = 400, size = 360, stroke = 5, color = "rgba(255,255,255,0.85)" }) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const p = pop(frame, fps, 0); const out = tailFade(frame, dur, 8);
  return (
    <AbsoluteFill style={{ alignItems: "center", paddingTop: y, opacity: out }}>
      <div style={{
        fontFamily: F.block, fontSize: size, lineHeight: 0.9, letterSpacing: 6, color: "transparent", WebkitTextStroke: `${stroke}px ${color}`,
        textTransform: "uppercase", transform: `scale(${0.9 + 0.1 * p})`, opacity: p, whiteSpace: "nowrap",
      }}>{text}</div>
    </AbsoluteFill>
  );
};

/* ---------- PiP card: a second video (the thing being reacted to) that moves between keyframes with motion blur ----------
   keys: [{at (sec, relative to overlay start), x, y, w}] ; the card eases between consecutive keys over `move` frames. */
export type PipKey = { at: number; x: number; y: number; w: number };
export const PipCard: React.FC<{ src: string; keys: PipKey[]; dur: number; startFrom?: number; radius?: number; move?: number; muted?: boolean; aspect?: number }> = ({
  src, keys, dur, startFrom = 0, radius = 34, move = 10, muted = true, aspect = 9 / 16,
}) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const ks = keys.map((k) => ({ ...k, f: Math.round(k.at * fps) }));
  let cur = ks[0], next: typeof cur | undefined;
  for (let i = 0; i < ks.length; i++) { if (frame >= ks[i].f) { cur = ks[i]; next = ks[i + 1]; } }
  let x = cur.x, y = cur.y, w = cur.w, blur = 0;
  if (next && frame >= next.f - move) {
    const t = EASE_IN_OUT(interpolate(frame, [next.f - move, next.f], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }));
    x = cur.x + (next.x - cur.x) * t; y = cur.y + (next.y - cur.y) * t; w = cur.w + (next.w - cur.w) * t;
    const vel = Math.hypot(next.x - cur.x, next.y - cur.y) / move;          // px per frame
    blur = Math.min(14, vel * 0.12) * Math.sin(Math.PI * t);               // peak blur mid-move, none at rest
  }
  const pIn = pop(frame, fps, 0); const out = tailFade(frame, dur, 6);
  return (
    <AbsoluteFill style={{ opacity: out }}>
      <div style={{ position: "absolute", left: x, top: y, width: w, height: w / aspect, borderRadius: radius, overflow: "hidden", boxShadow: cardShadow, filter: blur > 0.3 ? `blur(${blur}px)` : undefined, transform: `scale(${0.94 + 0.06 * pIn})`, opacity: pIn, background: "#000" }}>
        <OffthreadVideo src={staticFile(src)} startFrom={startFrom} muted={muted} style={{ width: "100%", height: "100%", objectFit: "cover" }} />
      </div>
    </AbsoluteFill>
  );
};

/* ---------- Slider reveal: a vertical line sweeps across and reveals the "after" (a CSS-filtered copy of the plate, or an image) ---------- */
export const SliderReveal: React.FC<{ plate?: string; atF?: number; after?: string; filter?: string; dur: number; from?: number; to?: number; sweep?: number; hold?: boolean }> = ({
  plate, atF = 0, after, filter = "sepia(0.25) saturate(1.15) brightness(1.04) contrast(1.03)", dur, from = -40, to = 1120, sweep = 36, hold = true,
}) => {
  const frame = useCurrentFrame();
  const t = prog(frame, 4, sweep, EASE_IN_OUT);
  const x = from + (to - from) * t;
  const out = tailFade(frame, dur, 6);
  const lineOpacity = hold ? 1 : interpolate(frame, [4 + sweep, 4 + sweep + 8], [1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  return (
    <AbsoluteFill style={{ opacity: out }}>
      <AbsoluteFill style={{ clipPath: `inset(0 ${Math.max(0, 1080 - x)}px 0 0)` }}>
        {after
          ? <Img src={staticFile(after)} style={{ width: "100%", height: "100%", objectFit: "cover" }} />
          : plate && <OffthreadVideo src={staticFile(plate)} startFrom={atF} muted style={{ width: "100%", height: "100%", objectFit: "cover", filter }} />}
      </AbsoluteFill>
      <div style={{ position: "absolute", left: x - 2, top: 0, width: 4, height: "100%", background: C.white, opacity: lineOpacity, boxShadow: "0 0 18px rgba(0,0,0,0.5)" }} />
      <div style={{ position: "absolute", left: x - 42, top: 960 - 42, width: 84, height: 84, borderRadius: 42, background: C.white, opacity: lineOpacity, boxShadow: cardShadow, display: "flex", alignItems: "center", justifyContent: "center", fontFamily: F.uiSemi, fontSize: 40, color: C.ink, letterSpacing: -4 }}>{"<>"}</div>
    </AbsoluteFill>
  );
};

/* ---------- Grid wall: the plate shrinks into the centre tile of a 3x3 and 8 tiles pop in around it one per `every` frames ---------- */
export const GridWall: React.FC<{ plate: string; atF?: number; tiles: string[]; dur: number; gap?: number; radius?: number; shrink?: number; every?: number; bg?: string }> = ({
  plate, atF = 0, tiles, dur, gap = 14, radius = 18, shrink = 12, every = 3, bg = C.black,
}) => {
  const frame = useCurrentFrame();
  const t = prog(frame, 0, shrink, EASE_IN_OUT);
  const cellW = (1080 - 2 * gap) / 3, cellH = (1920 - 2 * gap) / 3;
  const cx = gap + cellW, cy = gap + cellH;                                   // centre tile origin
  const x = cx * t, y = cy * t, w = 1080 - (1080 - cellW) * t, h = 1920 - (1920 - cellH) * t;
  const out = tailFade(frame, dur, 6);
  const order = [4, 0, 8, 2, 6, 1, 7, 3, 5];                                   // spiral-ish pop order around the centre (index 4 is the plate)
  let n = 0;
  return (
    <AbsoluteFill style={{ background: bg, opacity: out }}>
      {order.map((cell) => {
        if (cell === 4) return null;
        const col = cell % 3, row = Math.floor(cell / 3);
        const src = tiles[n++];
        const delay = shrink + 2 + (n - 1) * every;
        const vis = frame >= delay ? 1 : 0; const s = vis ? 0.92 + 0.08 * Math.min(1, (frame - delay + 1) / 3) : 0.9;
        return src ? (
          <div key={cell} style={{ position: "absolute", left: gap + col * cellW + (col ? gap * col / 3 : 0), top: gap + row * cellH + (row ? gap * row / 3 : 0), width: cellW - gap, height: cellH - gap, borderRadius: radius, overflow: "hidden", opacity: vis, transform: `scale(${s})`, background: "#111" }}>
            <Img src={staticFile(src)} style={{ width: "100%", height: "100%", objectFit: "cover" }} />
          </div>
        ) : null;
      })}
      <div style={{ position: "absolute", left: x, top: y, width: w, height: h, borderRadius: radius * t, overflow: "hidden" }}>
        <OffthreadVideo src={staticFile(plate)} startFrom={atF} muted style={{ width: "100%", height: "100%", objectFit: "cover" }} />
      </div>
    </AbsoluteFill>
  );
};

/* ---------- Param panel: dark panel, rows of label + slider + value that move to targets when he says them ---------- */
export type ParamRow = { label: string; from?: number; to: number; at: number; min?: number; max?: number; unit?: string };
export const ParamPanel: React.FC<{ title?: string; rows: ParamRow[]; dur: number; x?: number; y?: number; w?: number }> = ({ title = "TUNE", rows, dur, x = 60, y = 330, w = 960 }) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const p = pop(frame, fps, 0); const out = tailFade(frame, dur, 8);
  return (
    <AbsoluteFill style={{ opacity: out }}>
      <div style={{ position: "absolute", left: x, top: y, width: w, background: "rgba(18,18,20,0.92)", borderRadius: 26, padding: "26px 34px", boxShadow: cardShadow, transform: `translateY(${(1 - p) * 30}px)`, opacity: p }}>
        <div style={{ fontFamily: F.ui, fontSize: 24, letterSpacing: 6, color: C.tan, textTransform: "uppercase", marginBottom: 14 }}>{title}</div>
        {rows.map((r, i) => {
          const f0 = Math.round(r.at * fps);
          const v = interpolate(frame, [f0, f0 + 14], [r.from ?? 0, r.to], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
          const min = r.min ?? -100, max = r.max ?? 100;
          const k = (v - min) / (max - min);
          return (
            <div key={i} style={{ display: "flex", alignItems: "center", gap: 22, padding: "10px 0", fontFamily: F.ui, color: C.cream }}>
              <div style={{ width: 230, fontSize: 32 }}>{r.label}</div>
              <div style={{ flex: 1, height: 6, background: "rgba(255,255,255,0.18)", borderRadius: 3, position: "relative" }}>
                <div style={{ position: "absolute", left: `${k * 100}%`, top: -11, width: 28, height: 28, borderRadius: 14, background: C.white, marginLeft: -14, boxShadow: shadow }} />
              </div>
              <div style={{ width: 130, textAlign: "right", fontSize: 34, fontFamily: F.uiSemi, color: Math.abs(v - (r.from ?? 0)) > 0.01 ? C.tan : C.cream }}>{(v > 0 ? "+" : "") + Math.round(v)}{r.unit ?? ""}</div>
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- Storyboard card: the "what Claude is thinking" table (time | say | on screen | tool), rows type in ---------- */
export const StoryboardCard: React.FC<{ title: string; rows: [string, string, string, string][]; dur: number; x?: number; y?: number; w?: number }> = ({ title, rows, dur, x = 50, y = 300, w = 980 }) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const p = pop(frame, fps, 0); const out = tailFade(frame, dur, 8);
  return (
    <AbsoluteFill style={{ opacity: out }}>
      <div style={{ position: "absolute", left: x, top: y, width: w, background: C.cream, borderRadius: 20, padding: "26px 30px", boxShadow: cardShadow, transform: `translateY(${(1 - p) * 30}px) rotate(${-1.5 * p}deg)`, opacity: p, fontFamily: F.ui, color: C.ink }}>
        <div style={{ fontFamily: F.uiSemi, fontSize: 34, marginBottom: 6 }}>{title}</div>
        <div style={{ fontSize: 20, letterSpacing: 4, color: C.oxblood, textTransform: "uppercase", marginBottom: 12 }}>Storyboard</div>
        <div style={{ display: "grid", gridTemplateColumns: "70px 1.4fr 1.2fr 0.8fr", gap: "6px 14px", fontSize: 22, lineHeight: 1.25 }}>
          {["#", "He says", "On screen", "Tool"].map((h) => <div key={h} style={{ color: "#777", fontSize: 18, letterSpacing: 2, textTransform: "uppercase" }}>{h}</div>)}
          {rows.map((r, i) => {
            const pr = pop(frame, fps, 6 + i * 4);
            return r.map((cell, j) => <div key={`${i}-${j}`} style={{ opacity: pr, transform: `translateY(${(1 - pr) * 8}px)`, fontFamily: j === 3 ? F.uiSemi : F.ui, color: j === 3 ? C.oxblood : C.ink }}>{cell}</div>);
          })}
        </div>
      </div>
    </AbsoluteFill>
  );
};
