import React from "react";
import { AbsoluteFill, Img, OffthreadVideo, staticFile, useCurrentFrame, useVideoConfig, interpolate } from "remotion";
import { C, F, cardShadow } from "../theme";
import { pop, popSoft, prog, tailFade, backOut, expoOut, power4Out, EASE_OUT, EASE_IN_OUT } from "./anim";
import { mono } from "./Menu";
import { CameraMotionBlur } from "@remotion/motion-blur";

/*
  Effects.tsx (2026-11-21): the @tenfoldmarc "17 video effects" vocabulary, El Coyote edition.
  Source study: research/reel-references/2026-11-21-Def9pj5TWtA/BREAKDOWN.md and
  research/reel-references/2026-11-21-tenfoldmarc-profile/DOSSIER.md (the "matte sandwich": base video,
  back layer, person cutout, front layer). RivalReel already renders overlays flagged `behind: true`
  under the cutout, so every "behind him" effect here is just an overlay with behind: true.
  House rules kept: no grade on Jacob's footage, flat colors, Anton / Poppins / Instrument Serif,
  nothing over his face, one lockup on the hook, no on-screen CTA.
*/

/* ---------- WallBehind: a wall of photos / screenshots / logos pops in behind the subject (couch wall, headline wall).
   Use with behind: true. tiles = image paths; layout "grid" (couch wall) or "scatter" (headline wall). ---------- */
export const WallBehind: React.FC<{ tiles: string[]; dur: number; layout?: "grid" | "scatter"; cols?: number; tileW?: number; stagger?: number; dim?: number; captions?: string[]; seed?: number }> = ({
  tiles, dur, layout = "grid", cols = 4, tileW = 250, stagger = 2.4, dim = 0.35, captions, seed = 7,
}) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const out = tailFade(frame, dur, 6);
  const tileH = Math.round(tileW * 16 / 9);
  // deterministic pseudo-random for scatter
  const rnd = (i: number, k: number) => { const x = Math.sin((i + 1) * 9301 + k * 49297 + seed) * 233280; return x - Math.floor(x); };
  return (
    <AbsoluteFill style={{ opacity: out }}>
      <AbsoluteFill style={{ background: `rgba(0,0,0,${dim})` }} />
      {tiles.map((src, i) => {
        const p = popSoft(frame, fps, Math.round(i * stagger));
        let x: number, y: number, rot: number;
        if (layout === "grid") {
          const gap = 16; const gridW = cols * tileW + (cols - 1) * gap; const x0 = (1080 - gridW) / 2;
          x = x0 + (i % cols) * (tileW + gap); y = 120 + Math.floor(i / cols) * (tileH + gap); rot = 0;
        } else {
          x = 40 + rnd(i, 1) * (1080 - tileW - 80); y = 160 + rnd(i, 2) * (1100 - tileH); rot = -12 + rnd(i, 3) * 24;
        }
        return (
          <div key={i} style={{ position: "absolute", left: x, top: y, width: tileW, height: layout === "grid" ? tileH : "auto", borderRadius: 14, overflow: "hidden", background: C.cream, border: layout === "scatter" ? `4px solid ${C.cream}` : "none", boxShadow: cardShadow, transform: `rotate(${rot}deg) scale(${0.85 + 0.15 * p})`, opacity: p, filter: `blur(${(1 - p) * 8}px)` }}>
            <Img src={staticFile(src)} style={{ width: "100%", height: layout === "grid" ? "100%" : "auto", objectFit: "cover", display: "block" }} />
            {captions && captions[i] && <div style={{ fontFamily: F.uiSemi, fontSize: 22, color: C.ink, padding: "8px 10px", background: C.cream }}>{captions[i]}</div>}
          </div>
        );
      })}
    </AbsoluteFill>
  );
};

/* ---------- Masthead: a giant serif or block word behind the head (cover story). behind: true. Letters wipe in left to right. ---------- */
export const Masthead: React.FC<{ text: string; dur: number; y?: number; size?: number; font?: "serif" | "block" | "heavy"; color?: string; lines?: string[]; border?: boolean }> = ({
  text, dur, y = 260, size = 300, font = "block", color = C.cream, lines, border = false,
}) => {
  const frame = useCurrentFrame();
  const out = tailFade(frame, dur, 6);
  const wipe = prog(frame, 0, 14, EASE_OUT);
  const ff = font === "serif" ? F.serif : font === "heavy" ? F.heavy : F.block;
  return (
    <AbsoluteFill style={{ opacity: out }}>
      {border && <div style={{ position: "absolute", left: 40, top: 200, right: 40, bottom: 500, border: `3px solid ${color}`, opacity: 0.8 }} />}
      <div style={{ position: "absolute", left: 0, right: 0, top: y, textAlign: "center", fontFamily: ff, fontSize: size, lineHeight: 0.9, letterSpacing: font === "block" ? 4 : 0, color, clipPath: `inset(0 ${(1 - wipe) * 100}% 0 0)`, whiteSpace: "nowrap" }}>{text}</div>
      {lines && lines.map((l, i) => {
        const p = prog(frame, 10 + i * 4, 10, EASE_OUT);
        return <div key={i} style={{ position: "absolute", left: 72, top: y + size + 20 + i * 50, fontFamily: F.uiItalic, fontSize: 34, letterSpacing: 3, color, textTransform: "uppercase", opacity: p, transform: `translateX(${(1 - p) * -20}px)` }}>{l}</div>;
      })}
    </AbsoluteFill>
  );
};

/* ---------- FrameBreak: the plate shrinks into a 4:5 social-post card; the cutout is drawn at the same scale but unclipped,
   so head and hands cross the card edge. Front layer. Needs `plate` and `cutout` (RivalReel passes both). ---------- */
export const FrameBreak: React.FC<{ plate: string; cutout: string; atF?: number; dur: number; handle?: string; scale?: number; cy?: number; shrink?: number; aspect?: number; muted?: boolean }> = ({
  plate, cutout, atF = 0, dur, handle = "elcoyotediesel", scale = 0.66, cy = 900, shrink = 10, aspect = 1.25, muted = true,
}) => {
  const frame = useCurrentFrame();
  const t = prog(frame, 0, shrink, backOut(1.4));
  const s = 1 - (1 - scale) * t;
  const pw = 1080 * s, ph = 1920 * s;                       // the scaled plate rect (also the cutout rect)
  const centerY = 960 + (cy - 960) * t;                     // plate centre drifts to cy as it shrinks
  const pl = (1080 - pw) / 2, pt = centerY - ph / 2;
  const ch = Math.min(ph, pw * aspect);                     // card = 4:5 crop of the plate, centred
  const cl = pl, ct = centerY - ch / 2;
  const out = tailFade(frame, dur, 6);
  return (
    <AbsoluteFill style={{ background: `rgba(11,11,12,${t})`, opacity: out }}>
      {/* card: clipped plate */}
      <div style={{ position: "absolute", left: cl, top: ct, width: pw, height: ch, borderRadius: 28 * t, overflow: "hidden", boxShadow: t > 0.2 ? cardShadow : undefined }}>
        <div style={{ position: "absolute", left: 0, top: pt - ct, width: pw, height: ph }}>
          <OffthreadVideo src={staticFile(plate)} startFrom={atF} muted={muted} style={{ width: "100%", height: "100%", objectFit: "cover" }} />
        </div>
      </div>
      {/* IG chrome */}
      <div style={{ position: "absolute", left: cl + 24, top: ct + ch + 24, display: "flex", alignItems: "center", gap: 12, opacity: t }}>
        <div style={{ width: 44, height: 44, borderRadius: 22, background: C.tan }} />
        <div style={{ fontFamily: F.uiSemi, fontSize: 26, color: "#fff" }}>{handle}</div>
        <div style={{ fontFamily: F.ui, fontSize: 20, color: "#fff", border: "2px solid #fff", borderRadius: 8, padding: "2px 12px" }}>Follow</div>
      </div>
      <div style={{ position: "absolute", left: cl + pw + 26, top: ct + ch - 200, display: "flex", flexDirection: "column", gap: 30, opacity: t, color: "#fff", fontSize: 44 }}>
        <div>♡</div><div>◯</div><div>➤</div>
      </div>
      {/* the person, same rect as the plate, unclipped: the break */}
      <div style={{ position: "absolute", left: pl, top: pt, width: pw, height: ph }}>
        <OffthreadVideo src={staticFile(cutout)} startFrom={atF} muted transparent style={{ width: "100%", height: "100%", objectFit: "cover" }} />
      </div>
    </AbsoluteFill>
  );
};

/* ---------- Vertigo: dolly zoom in post. Background (plate) scales up while the cutout holds size. Front layer, needs cutout. ---------- */
export const Vertigo: React.FC<{ plate: string; cutout: string; atF?: number; dur: number; to?: number; anchorY?: number; muted?: boolean }> = ({
  plate, cutout, atF = 0, dur, to = 1.35, anchorY = 45, muted = true,
}) => {
  const frame = useCurrentFrame();
  const t = prog(frame, 0, dur, EASE_IN_OUT);
  const s = 1 + (to - 1) * t;
  return (
    <AbsoluteFill>
      <OffthreadVideo src={staticFile(plate)} startFrom={atF} muted={muted} style={{ width: "100%", height: "100%", objectFit: "cover", transform: `scale(${s})`, transformOrigin: `50% ${anchorY}%` }} />
      <OffthreadVideo src={staticFile(cutout)} startFrom={atF} muted transparent style={{ position: "absolute", left: 0, top: 0, width: "100%", height: "100%", objectFit: "cover" }} />
    </AbsoluteFill>
  );
};

/* ---------- BgReplace: green screen without a green screen. A still or video behind the cutout (dimmed), optional label. Front layer. ---------- */
export const BgReplace: React.FC<{ cutout: string; bg: string; atF?: number; dur: number; dim?: number; blur?: number; kenBurns?: boolean }> = ({ cutout, bg, atF = 0, dur, dim = 0.25, blur = 0, kenBurns = true }) => {
  const frame = useCurrentFrame();
  const s = kenBurns ? 1.04 + 0.06 * prog(frame, 0, dur, (t) => t) : 1;
  const isVideo = /\.(mp4|webm|mov)$/i.test(bg);
  return (
    <AbsoluteFill style={{ background: C.black }}>
      <AbsoluteFill style={{ transform: `scale(${s})`, filter: blur ? `blur(${blur}px)` : undefined }}>
        {isVideo ? <OffthreadVideo src={staticFile(bg)} muted style={{ width: "100%", height: "100%", objectFit: "cover" }} /> : <Img src={staticFile(bg)} style={{ width: "100%", height: "100%", objectFit: "cover" }} />}
      </AbsoluteFill>
      <AbsoluteFill style={{ background: `rgba(0,0,0,${dim})` }} />
      <OffthreadVideo src={staticFile(cutout)} startFrom={atF} muted transparent style={{ position: "absolute", left: 0, top: 0, width: "100%", height: "100%", objectFit: "cover" }} />
    </AbsoluteFill>
  );
};

/* ---------- ChartGrow: a line draws across a labelled axis, points pop, a tan label pill lands on the last point. behind: true or front. ---------- */
export const ChartGrow: React.FC<{ values: number[]; labels?: string[]; dur: number; x?: number; y?: number; w?: number; h?: number; label?: string; drawFrames?: number; color?: string; dim?: number }> = ({
  values, labels, dur, x = 90, y = 500, w = 900, h = 420, label, drawFrames = 30, color = C.tan, dim = 0.3,
}) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const out = tailFade(frame, dur, 6);
  const max = Math.max(...values), min = Math.min(...values);
  const pts = values.map((v, i) => [x + (i / (values.length - 1)) * w, y + h - ((v - min) / (max - min || 1)) * h]);
  const d = pts.map((p, i) => `${i ? "L" : "M"}${p[0]},${p[1]}`).join(" ");
  const total = pts.slice(1).reduce((a, p, i) => a + Math.hypot(p[0] - pts[i][0], p[1] - pts[i][1]), 0);
  const t = prog(frame, 0, drawFrames, EASE_IN_OUT);
  const lp = pop(frame, fps, drawFrames);
  const last = pts[pts.length - 1];
  return (
    <AbsoluteFill style={{ opacity: out }}>
      <AbsoluteFill style={{ background: `rgba(0,0,0,${dim})` }} />
      <svg width={1080} height={1920} style={{ position: "absolute", left: 0, top: 0 }}>
        {labels && labels.map((l, i) => <text key={i} x={pts[i][0]} y={y + h + 50} textAnchor="middle" fontFamily={mono} fontSize={26} fill={C.cream} opacity={0.7}>{l}</text>)}
        {pts.map((p, i) => <line key={`g${i}`} x1={p[0]} y1={y} x2={p[0]} y2={y + h} stroke={C.cream} strokeOpacity={0.12} strokeDasharray="4 8" />)}
        <path d={d} fill="none" stroke={color} strokeWidth={8} strokeLinecap="round" strokeLinejoin="round" strokeDasharray={total} strokeDashoffset={total * (1 - t)} style={{ filter: `drop-shadow(0 0 12px ${color})` }} />
        {pts.map((p, i) => { const vis = t * (values.length - 1) >= i - 0.01; return vis ? <circle key={`c${i}`} cx={p[0]} cy={p[1]} r={12} fill={C.cream} stroke={color} strokeWidth={5} /> : null; })}
      </svg>
      {label && <div style={{ position: "absolute", left: Math.min(last[0] - 60, 1080 - 320), top: last[1] - 90, fontFamily: F.heavy, fontSize: 30, letterSpacing: 2, color: C.ink, background: color, borderRadius: 10, padding: "6px 16px", transform: `scale(${lp})`, opacity: lp }}>{label} ↗</div>}
    </AbsoluteFill>
  );
};

/* ---------- PullBackWindow: the plate pulls back to reveal it was a window inside an app (the shop camera, the portal, a phone). Front layer. ---------- */
export const PullBackWindow: React.FC<{ plate: string; atF?: number; dur: number; title?: string; rows?: { text: string; at: number }[]; to?: number; pull?: number; muted?: boolean }> = ({
  plate, atF = 0, dur, title = "elcoyotediesel.com", rows = [], to = 0.56, pull = 14, muted = true,
}) => {
  const frame = useCurrentFrame();
  const t = prog(frame, 0, pull, expoOut);
  const s = 1 - (1 - to) * t; const w = 1080 * s, h = 1920 * s;
  const left = (1080 - w) / 2 - 150 * t, top = 300 * t + (1920 - h) / 2 * (1 - t);
  const out = tailFade(frame, dur, 6);
  return (
    <AbsoluteFill style={{ background: `rgba(239,233,220,${t})`, opacity: out }}>
      {/* window chrome */}
      <div style={{ position: "absolute", left: left - 24, top: top - 70, width: w + 48 + 300, height: h + 100, borderRadius: 24, background: "#fff", border: `3px solid ${C.ink}`, boxShadow: `12px 13px 0 ${C.ink}`, opacity: t }}>
        <div style={{ display: "flex", gap: 10, padding: "16px 20px", alignItems: "center" }}>
          <div style={{ width: 16, height: 16, borderRadius: 8, background: "#e25" }} /><div style={{ width: 16, height: 16, borderRadius: 8, background: "#ec2" }} /><div style={{ width: 16, height: 16, borderRadius: 8, background: "#4c4" }} />
          <div style={{ marginLeft: 20, fontFamily: mono, fontSize: 22, color: "#666" }}>{title}</div>
        </div>
      </div>
      <div style={{ position: "absolute", left, top, width: w, height: h, borderRadius: 16 * t, overflow: "hidden" }}>
        <OffthreadVideo src={staticFile(plate)} startFrom={atF} muted={muted} style={{ width: "100%", height: "100%", objectFit: "cover" }} />
      </div>
      <div style={{ position: "absolute", left: left + w + 30, top: top + 10, width: 260, opacity: t }}>
        {rows.map((r, i) => {
          const on = frame >= r.at; const p = prog(frame, r.at, 8, backOut(2));
          return (
            <div key={i} style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 14, opacity: on ? 1 : 0.35 }}>
              <div style={{ width: 26, height: 26, borderRadius: 13, background: on ? C.green : "#ddd", transform: `scale(${on ? 0.8 + 0.2 * p : 1})`, color: "#fff", fontSize: 18, display: "flex", alignItems: "center", justifyContent: "center" }}>{on ? "✓" : ""}</div>
              <div style={{ fontFamily: F.ui, fontSize: 22, color: C.ink }}>{r.text}</div>
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- ZoomThrough: zoom transition with a REAL radial streak (CameraMotionBlur accumulates 12 sub-frame zooms around the
   anchor, per the 2026-11-21 effect-repo port notes; the old gaussian blur made mush). Anchor on the detail you land on. ---------- */
export const ZoomThrough: React.FC<{ plate: string; atF?: number; dur: number; cutAt?: number; peak?: number; flash?: boolean; muted?: boolean; nextAtF?: number; next?: string; ox?: number; oy?: number; samples?: number }> = ({
  plate, atF = 0, dur, cutAt = 4, peak = 2.6, flash = true, muted = true, next, nextAtF, ox = 50, oy = 45, samples = 12,
}) => {
  const frame = useCurrentFrame();
  const inA = frame < cutAt;
  const tA = prog(frame, 0, cutAt, power4Out); const tB = prog(frame, cutAt, dur - cutAt, expoOut);
  const sA = 1 + (peak - 1) * tA; const sB = 1.45 - 0.45 * tB;
  const fl = flash ? interpolate(frame, [cutAt - 1, cutAt, cutAt + 5], [0, 0.85, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }) : 0;
  return (
    <AbsoluteFill style={{ background: "#000" }}>
      <CameraMotionBlur shutterAngle={270} samples={samples}>
        <AbsoluteFill style={{ background: "#000" }}>
          {inA
            ? <OffthreadVideo src={staticFile(plate)} startFrom={atF} muted={muted} style={{ width: "100%", height: "100%", objectFit: "cover", transform: `scale(${sA})`, transformOrigin: `${ox}% ${oy}%` }} />
            : <OffthreadVideo src={staticFile(next ?? plate)} startFrom={(nextAtF ?? atF) + (next ? 0 : cutAt)} muted={muted} style={{ width: "100%", height: "100%", objectFit: "cover", transform: `scale(${sB})`, transformOrigin: `${ox}% ${oy}%` }} />}
        </AbsoluteFill>
      </CameraMotionBlur>
      <AbsoluteFill style={{ background: "#fff", opacity: fl }} />
    </AbsoluteFill>
  );
};

/* ---------- Orbit: tiles circle the head on a tilted ellipse (tenfoldmarc #1). List it TWICE in the EDL at the same `at`:
   once with behind: true, props { side: "back" } and once in front with { side: "front" }; RivalReel's cutout does the depth swap.
   Reference values: centre (540, 1110), rx 460, ry 150, 5.2 s per revolution, tiles 190 wide, back copies at 75 percent brightness. ---------- */
export const Orbit: React.FC<{ tiles: string[]; dur: number; side?: "back" | "front"; cx?: number; cy?: number; rx?: number; ry?: number; rev?: number; w?: number; dim?: number }> = ({
  tiles, dur, side = "front", cx = 540, cy = 1110, rx = 460, ry = 150, rev = 5.2, w = 190, dim = 0.75,
}) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const t = frame / fps; const n = tiles.length; const h = Math.round(w * 16 / 9);
  const open = prog(frame, 0, 12, EASE_OUT);
  const items = tiles.map((src, i) => {
    const th = 2 * Math.PI * (t / rev) + (i * 2 * Math.PI) / n + 0.35;
    const s = Math.sin(th);
    return { src, i, x: cx + rx * open * Math.cos(th), y: cy + ry * s, sc: 0.6 + 0.4 * (s + 1) / 2, s, rot: -6 * Math.cos(th) };
  }).filter((it) => (side === "front" ? it.s > 0 : it.s <= 0)).sort((a, b) => a.s - b.s);
  return (
    <AbsoluteFill style={{ opacity: tailFade(frame, dur, 6) }}>
      {items.map((it) => {
        const p = prog(frame, Math.round(it.i * 0.07 * fps), Math.round(0.45 * fps), backOut(1.8));
        return (
          <div key={it.i} style={{ position: "absolute", left: it.x - w / 2, top: it.y - h / 2, width: w, height: h, borderRadius: 16, overflow: "hidden", border: `4px solid ${C.cream}`, boxShadow: cardShadow, transform: `scale(${it.sc * p}) rotate(${it.rot}deg)`, filter: side === "back" ? `brightness(${dim})` : undefined }}>
            {/\.(mp4|webm)$/i.test(it.src)
              ? <OffthreadVideo src={staticFile(it.src)} muted style={{ width: "100%", height: "100%", objectFit: "cover" }} />
              : <Img src={staticFile(it.src)} style={{ width: "100%", height: "100%", objectFit: "cover" }} />}
          </div>
        );
      })}
    </AbsoluteFill>
  );
};

/* ---------- HudZoom: viewfinder overlay (REC dot, timecode, corner brackets, zoom readout) for the digital-zoom beat. Front layer, no plate needed. ---------- */
export const HudZoom: React.FC<{ dur: number; from?: number; to?: number; label?: string; color?: string }> = ({ dur, from = 1.0, to = 1.6, label = "REC", color = C.cream }) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const z = from + (to - from) * prog(frame, 0, dur, EASE_OUT);
  const blink = Math.floor(frame / Math.round(fps / 2)) % 2 === 0;
  const tc = (f: number) => { const s = Math.floor(f / fps); return `${String(Math.floor(s / 60)).padStart(2, "0")}:${String(s % 60).padStart(2, "0")}:${String(f % fps).padStart(2, "0")}`; };
  const br = (x: number, y: number, fx: number, fy: number) => (
    <div style={{ position: "absolute", left: x, top: y, width: 70, height: 70, borderTop: fy < 0 ? `4px solid ${color}` : undefined, borderBottom: fy > 0 ? `4px solid ${color}` : undefined, borderLeft: fx < 0 ? `4px solid ${color}` : undefined, borderRight: fx > 0 ? `4px solid ${color}` : undefined, opacity: 0.9 }} />
  );
  return (
    <AbsoluteFill style={{ opacity: tailFade(frame, dur, 4) }}>
      {br(90, 320, -1, -1)}{br(1080 - 160, 320, 1, -1)}{br(90, 1920 - 560, -1, 1)}{br(1080 - 160, 1920 - 560, 1, 1)}
      <div style={{ position: "absolute", left: 110, top: 340, display: "flex", alignItems: "center", gap: 12, fontFamily: mono, fontSize: 28, color, opacity: 0.9 }}>
        <div style={{ width: 18, height: 18, borderRadius: 9, background: "#e0392b", opacity: blink ? 1 : 0.2 }} />{label}
      </div>
      <div style={{ position: "absolute", right: 150, top: 340, fontFamily: mono, fontSize: 28, color, opacity: 0.9, fontVariantNumeric: "tabular-nums" }}>{tc(frame)}</div>
      <div style={{ position: "absolute", left: 0, right: 0, top: 1920 - 520, textAlign: "center", fontFamily: mono, fontSize: 30, color, opacity: 0.9, fontVariantNumeric: "tabular-nums" }}>{z.toFixed(2)}x</div>
    </AbsoluteFill>
  );
};

/* ---------- BeforeAfter: a vertical wipe with a light bar between two stills or clips. Labels in Oswald-style caps (F.uiSemi here). Front layer. ---------- */
export const BeforeAfter: React.FC<{ before: string; after: string; dur: number; sweep?: number; hold?: number; labels?: [string, string]; atF?: number }> = ({ before, after, dur, sweep = 20, hold = 6, labels = ["BEFORE", "AFTER"], atF = 0 }) => {
  const frame = useCurrentFrame();
  const t = prog(frame, hold, sweep, EASE_IN_OUT);
  const x = 1080 * t;
  const media = (src: string) => (/\.(mp4|webm|mov)$/i.test(src)
    ? <OffthreadVideo src={staticFile(src)} startFrom={atF} muted style={{ width: 1080, height: 1920, objectFit: "cover" }} />
    : <Img src={staticFile(src)} style={{ width: 1080, height: 1920, objectFit: "cover" }} />);
  return (
    <AbsoluteFill style={{ opacity: tailFade(frame, dur, 6) }}>
      <AbsoluteFill>{media(before)}</AbsoluteFill>
      <div style={{ position: "absolute", left: 0, top: 0, width: x, height: 1920, overflow: "hidden" }}>{media(after)}</div>
      <div style={{ position: "absolute", left: x - 3, top: 0, width: 6, height: 1920, background: C.cream, boxShadow: "0 0 24px rgba(255,255,255,0.8)" }} />
      <div style={{ position: "absolute", left: 72, top: 360, fontFamily: F.uiSemi, fontSize: 30, letterSpacing: 4, color: C.cream, opacity: 1 - t, textShadow: "0 4px 16px rgba(0,0,0,0.6)" }}>{labels[0]}</div>
      <div style={{ position: "absolute", right: 150, top: 360, fontFamily: F.uiSemi, fontSize: 30, letterSpacing: 4, color: C.tan, opacity: t, textShadow: "0 4px 16px rgba(0,0,0,0.6)" }}>{labels[1]}</div>
    </AbsoluteFill>
  );
};

/* ---------- BlurWord: one word blur-pops in big (digital zoom emphasis word). scale 1.22 + 22 px blur to 1 in 6 frames. ---------- */
export const BlurWord: React.FC<{ text: string; dur: number; y?: number; size?: number; color?: string; font?: string }> = ({ text, dur, y = 1000, size = 110, color = C.cream, font }) => {
  const frame = useCurrentFrame();
  const p = prog(frame, 0, 6, EASE_OUT);
  return (
    <AbsoluteFill style={{ alignItems: "center", paddingTop: y, opacity: tailFade(frame, dur, 4) }}>
      <div style={{ fontFamily: font ?? F.uiSemi, fontSize: size, color, transform: `scale(${1.22 - 0.22 * p})`, filter: `blur(${(1 - p) * 22}px)`, opacity: p, textShadow: "0 8px 30px rgba(0,0,0,0.6)" }}>{text}</div>
    </AbsoluteFill>
  );
};
