import React from "react";
import { AbsoluteFill, Img, OffthreadVideo, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { C } from "../theme";
import { pop, prog, tailFade, backOut } from "./anim";

/*
  Boil.tsx (2026-11-21): the two silhouette effects from research/2026-11-21-effect-repos-port-notes.md, sections 3.2 and 3.3.
  Both use the same trick: a second copy of the cutout turned into a flat silhouette, grown outward, drawn UNDER the clean
  cutout so only the rim shows. The clean cutout never goes through a displacement filter (that would warp the face).
  Headless Chrome gotcha: heavy CSS filters on many elements can turn captures black, so each component keeps the filtered
  elements to two at most (the silhouette layer, and in DoodleBoil the one doodle svg).
  Palette: cream / tan / oxblood from theme.ts, nothing neon.
*/

const isImage = (s: string) => /\.(png|jpe?g|webp|gif|avif)$/i.test(s);
const vid: React.CSSProperties = { width: "100%", height: "100%", objectFit: "cover" };

/* ---------- StickerEdge: paper-cut sticker. A cream die-cut rim `width` px around the person. Front layer, needs cutout.
   Rim = the cutout tinted flat (feFlood + feComposite on SourceAlpha, so the core is the rim colour, no dark fringe) then dilated by
   eight chained zero-blur drop-shadows (4 axis + 4 diagonal). Eight short offsets sum to a near-round octagon, so the rim is the
   same thickness on a shoulder slope as on a vertical edge; four axis shadows alone give a square dilation that reads 40 percent
   fatter on diagonals. `paper` fills the back (a colour or an image in public/). `shadow` drops a soft shadow under the whole sticker.
   `slap` scales the sticker 0.92 to 1 over 8 frames with a back-out (the sticker slaps on). ---------- */
export const StickerEdge: React.FC<{ cutout: string; atF?: number; dur: number; width?: number; color?: string; paper?: string; shadow?: boolean; slap?: boolean }> = ({
  cutout, atF = 0, dur, width = 14, color = C.cream, paper, shadow = true, slap = false,
}) => {
  const frame = useCurrentFrame();
  const id = `stk${atF}-${dur}`;
  const a = width * 0.4, d = width * 0.283;                                   // axis and diagonal offsets, see header note
  const ds = [`${a}px 0`, `-${a}px 0`, `0 ${a}px`, `0 -${a}px`, `${d}px ${d}px`, `-${d}px -${d}px`, `${d}px -${d}px`, `-${d}px ${d}px`]
    .map((o) => `drop-shadow(${o} 0 ${color})`).join(" ");
  const sh = shadow ? " drop-shadow(0 18px 22px rgba(0,0,0,0.38))" : "";
  const s = slap ? 0.92 + 0.08 * prog(frame, 0, 8, backOut(1.8)) : 1;
  const xf: React.CSSProperties = { transform: `scale(${s})`, transformOrigin: "50% 70%" };
  return (
    <AbsoluteFill style={{ opacity: tailFade(frame, dur, 6) }}>
      <svg width={0} height={0} style={{ position: "absolute" }}>
        <filter id={id} x="-5%" y="-5%" width="110%" height="110%" colorInterpolationFilters="sRGB">
          <feFlood floodColor={color} result="ink" />
          <feComposite in="ink" in2="SourceAlpha" operator="in" />
        </filter>
      </svg>
      {paper && (isImage(paper)
        ? <Img src={staticFile(paper)} style={{ position: "absolute", inset: 0, ...vid }} />
        : <AbsoluteFill style={{ background: paper }} />)}
      {/* 1 of 2 filtered elements: flat silhouette, dilated into the rim */}
      <div style={{ position: "absolute", inset: 0, ...xf, filter: `url(#${id}) ${ds}${sh}` }}>
        <OffthreadVideo src={staticFile(cutout)} startFrom={atF} muted transparent style={vid} />
      </div>
      {/* the clean cutout on top, untouched */}
      <div style={{ position: "absolute", inset: 0, ...xf }}>
        <OffthreadVideo src={staticFile(cutout)} startFrom={atF} muted transparent style={vid} />
      </div>
    </AbsoluteFill>
  );
};

/* ---------- DoodleBoil: hand-drawn chalk outline that redraws every `boilEvery` frames, plus optional doodle sprites.
   Front layer, needs cutout. One SVG filter does the whole rim: SourceAlpha dilated by `stroke` (feMorphology), minus the plain
   SourceAlpha (feComposite out) so only the edge is left, flooded `color`, then pushed through feTurbulence + feDisplacementMap
   whose seed steps with floor(frame / boilEvery). The filter id carries the seed so Chrome rebuilds it on every step (same-id attribute
   changes do not always invalidate in headless captures). The clean cutout sits on top, so the rim jitters around a steady face.
   Doodles: hand-drawn svg paths (heart, star, box, arrow, circle) at (x, y), popping in at local frame `at` with the kit's pop spring,
   boiled by a second filter tuned for small shapes. The doodle svg is the second (and last) filtered element. ---------- */
export type Doodle = { kind: "heart" | "star" | "box" | "arrow" | "circle"; x: number; y: number; at: number; size?: number; rot?: number; color?: string };

const doodlePath = (kind: Doodle["kind"], s: number) => {
  const h = s / 2;
  switch (kind) {
    case "circle": {
      // wobbly ellipse, 1.06 turns so the ends overlap like a marker ring (Vibha fx_scribble numbers)
      const pts: string[] = [];
      for (let i = 0; i <= 72; i++) {
        const a = (i / 68) * Math.PI * 2;
        const w = (1 + 0.04 * Math.sin(3 * a)) * (1 + 0.04 * Math.cos(2 * a));
        pts.push(`${(h * 1.05 * w * Math.cos(a)).toFixed(1)} ${(h * 0.8 * w * Math.sin(a)).toFixed(1)}`);
      }
      return `M ${pts.join(" L ")}`;
    }
    case "star": {
      const pts: string[] = [];
      for (let i = 0; i <= 10; i++) {
        const r = i % 2 ? h * 0.45 : h; const a = -Math.PI / 2 + (i * Math.PI) / 5;
        pts.push(`${(r * Math.cos(a)).toFixed(1)} ${(r * Math.sin(a)).toFixed(1)}`);
      }
      return `M ${pts.join(" L ")} L ${(h * 0.45 * Math.cos(-Math.PI / 2 + Math.PI / 5)).toFixed(1)} ${(h * 0.45 * Math.sin(-Math.PI / 2 + Math.PI / 5)).toFixed(1)}`;
    }
    case "box":
      // corners overshoot a touch, like a quick marker box
      return `M ${-h - 6} ${-h} L ${h + 4} ${-h - 2} L ${h} ${h + 5} L ${-h - 3} ${h} L ${-h} ${-h - 8}`;
    case "arrow":
      // bent arrow, tail bottom-left to head top-right, head drawn as two strokes
      return `M ${-h} ${h * 0.8} Q ${-h * 0.1} ${h * 0.9} ${h * 0.85} ${-h * 0.75} M ${h * 0.85} ${-h * 0.75} L ${h * 0.25} ${-h * 0.7} M ${h * 0.85} ${-h * 0.75} L ${h * 0.75} ${-h * 0.15}`;
    case "heart":
    default:
      return `M 0 ${h * 0.75} C ${-h * 1.3} ${-h * 0.1} ${-h * 0.6} ${-h * 1.05} 0 ${-h * 0.4} C ${h * 0.6} ${-h * 1.05} ${h * 1.3} ${-h * 0.1} 0 ${h * 0.75} Z`;
  }
};

export const DoodleBoil: React.FC<{ cutout: string; atF?: number; dur: number; stroke?: number; color?: string; boilEvery?: number; amp?: number; doodles?: Doodle[] }> = ({
  cutout, atF = 0, dur, stroke = 6, color = C.cream, boilEvery = 3, amp = 3, doodles = [],
}) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const seed = Math.floor(frame / Math.max(1, boilEvery));                   // stepped, never smooth
  const base = `boil${atF}-${dur}`;
  const rimId = `${base}r${seed}`, dooId = `${base}d${seed}`;
  const draw = prog(frame, 0, 5);                                             // the chalk line draws itself on over 5 frames (rim grows 0 to stroke)
  // per-step whole-rim offset: a hand retracing the line never lands in the same place. Deterministic hash of the seed, a transform not a filter.
  const hash = (k: number) => { const x = Math.sin(k * 127.1 + 311.7) * 43758.5453; return x - Math.floor(x); };
  const jx = (hash(seed) - 0.5) * 2 * amp * 0.8, jy = (hash(seed + 57) - 0.5) * 2 * amp * 0.8;
  return (
    <AbsoluteFill style={{ opacity: tailFade(frame, dur, 4) }}>
      <svg width={0} height={0} style={{ position: "absolute" }}>
        {/* rim filter: dilate, subtract the body, tint, wobble */}
        <filter id={rimId} x="-5%" y="-5%" width="110%" height="110%" colorInterpolationFilters="sRGB">
          <feMorphology in="SourceAlpha" operator="dilate" radius={Math.max(0.5, stroke * draw)} result="fat" />
          <feComposite in="fat" in2="SourceAlpha" operator="out" result="ring" />
          <feFlood floodColor={color} result="ink" />
          <feComposite in="ink" in2="ring" operator="in" result="rim" />
          {/* low frequency (about 90 px waves) so the line bows and shifts as a whole instead of fizzing; fine noise averages out at reel size */}
          <feTurbulence type="fractalNoise" baseFrequency="0.011" numOctaves={2} seed={seed} result="n" />
          <feDisplacementMap in="rim" in2="n" scale={amp * 2.4} xChannelSelector="R" yChannelSelector="G" />
        </filter>
        {/* doodle filter: the same boil, higher frequency so small shapes wobble along their length */}
        <filter id={dooId} x="-20%" y="-20%" width="140%" height="140%" colorInterpolationFilters="sRGB">
          <feTurbulence type="fractalNoise" baseFrequency="0.04" numOctaves={2} seed={seed + 101} result="n" />
          <feDisplacementMap in="SourceGraphic" in2="n" scale={amp * 2} xChannelSelector="R" yChannelSelector="G" />
        </filter>
      </svg>
      {/* 1 of 2 filtered elements: the boiled rim */}
      <div style={{ position: "absolute", inset: 0, transform: `translate(${jx.toFixed(1)}px, ${jy.toFixed(1)}px)`, filter: `url(#${rimId})` }}>
        <OffthreadVideo src={staticFile(cutout)} startFrom={atF} muted transparent style={vid} />
      </div>
      {/* the clean cutout on top, untouched */}
      <div style={{ position: "absolute", inset: 0 }}>
        <OffthreadVideo src={staticFile(cutout)} startFrom={atF} muted transparent style={vid} />
      </div>
      {/* 2 of 2 filtered elements: doodles */}
      {doodles.length > 0 && (
        <svg width={1080} height={1920} viewBox="0 0 1080 1920" style={{ position: "absolute", left: 0, top: 0, filter: `url(#${dooId})` }}>
          {doodles.map((dd, i) => {
            if (frame < dd.at) return null;
            const p = pop(frame, fps, dd.at);
            const size = dd.size ?? 120; const rot = dd.rot ?? (i % 2 ? 9 : -7);
            return (
              <g key={i} transform={`translate(${dd.x} ${dd.y}) rotate(${rot}) scale(${p})`} opacity={Math.min(1, p * 1.5)}>
                <path d={doodlePath(dd.kind, size)} fill="none" stroke={dd.color ?? color} strokeWidth={stroke} strokeLinecap="round" strokeLinejoin="round" />
              </g>
            );
          })}
        </svg>
      )}
    </AbsoluteFill>
  );
};
