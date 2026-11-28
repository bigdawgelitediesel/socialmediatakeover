import React from "react";
import { AbsoluteFill, OffthreadVideo, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { C, F, cardShadow } from "../theme";
import { prog, popSoft, tailFade, backOut, EASE_OUT } from "./anim";
import { StickerEdge } from "./Boil";

/*
  Studio.tsx (2026-11-23): the four @tenfoldmarc effects the kit did not have yet, so all 17 of his list are callable.
  Source: reel Def_oOUzJeS (2026-10-15) and the earlier study research/reel-references/2026-11-21-Def9pj5TWtA/BREAKDOWN.md.
  ui world (03), headline wall (08), paper cut (13), glass type (17). The other 13 live in Effects.tsx, Menu.tsx and Boil.tsx.
  House rules kept: brand palette, nothing over the face, text inside the rule 120 zones.
*/

const vid: React.CSSProperties = { width: "100%", height: "100%", objectFit: "cover" };
const rnd = (i: number, k: number, seed = 7) => { const x = Math.sin((i + 1) * 9301 + k * 49297 + seed) * 233280; return x - Math.floor(x); };

/* ---------- UiWorld (03 ui world): the frame becomes a cream app screen. A prompt box types `text`, a send button presses,
   and the person sits small at the bottom as a cutout, as if standing inside the interface. Front layer, needs cutout.
   `scale` is the person's size, `title` the small word over the box, `chips` optional pills that pop under the box. ---------- */
export const UiWorld: React.FC<{ cutout: string; atF?: number; dur: number; text: string; title?: string; chips?: string[]; scale?: number; boxY?: number; bg?: string }> = ({
  cutout, atF = 0, dur, text, title = "El Coyote", chips = [], scale = 0.62, boxY = 520, bg = C.cream,
}) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const inP = prog(frame, 0, 8, EASE_OUT);
  const chars = Math.max(0, Math.min(text.length, Math.floor((frame - 6) * 1.1)));
  const done = chars >= text.length;
  const caret = Math.floor(frame / 8) % 2 === 0;
  const press = done ? prog(frame, 6 + Math.ceil(text.length / 1.1) + 4, 6, backOut(2.4)) : 0;
  const s = 1 - (1 - scale) * inP;
  return (
    <AbsoluteFill style={{ opacity: tailFade(frame, dur, 5) }}>
      <AbsoluteFill style={{ background: bg, opacity: inP }} />
      <AbsoluteFill style={{ background: "radial-gradient(ellipse at 50% 100%, rgba(0,0,0,0.16), rgba(0,0,0,0) 60%)", opacity: inP }} />
      <div style={{ position: "absolute", left: 0, right: 0, top: boxY - 120, textAlign: "center", fontFamily: F.serif, fontSize: 64, color: C.ink, opacity: inP }}>{title}</div>
      <div style={{ position: "absolute", left: 90, right: 90, top: boxY, height: 190, borderRadius: 30, background: "#fff", boxShadow: "0 14px 40px rgba(0,0,0,0.16), 0 2px 5px rgba(0,0,0,0.12)", opacity: inP, transform: `translateY(${(1 - inP) * 40}px)` }}>
        <div style={{ position: "absolute", left: 36, top: 30, right: 36, fontFamily: F.ui, fontSize: 40, color: C.ink, whiteSpace: "nowrap", overflow: "hidden" }}>
          {text.slice(0, chars)}<span style={{ opacity: caret && !press ? 1 : 0 }}>|</span>
        </div>
        <div style={{ position: "absolute", left: 36, bottom: 26, fontFamily: F.ui, fontSize: 34, color: "rgba(20,20,20,0.45)" }}>+</div>
        <div style={{ position: "absolute", right: 28, bottom: 22, width: 64, height: 64, borderRadius: 18, background: done ? C.oxblood : C.ink, color: "#fff", fontFamily: F.uiSemi, fontSize: 38, lineHeight: "64px", textAlign: "center", transform: `scale(${1 - 0.14 * Math.sin(press * Math.PI)})` }}>↑</div>
      </div>
      {chips.map((c, i) => {
        const p = popSoft(frame, fps, 14 + i * 4);
        return <div key={i} style={{ position: "absolute", left: 90 + i * 300, top: boxY + 220, fontFamily: F.uiSemi, fontSize: 28, color: C.ink, background: C.tan, borderRadius: 40, padding: "10px 26px", transform: `scale(${0.7 + 0.3 * p})`, opacity: p }}>{c}</div>;
      })}
      <div style={{ position: "absolute", inset: 0, transform: `scale(${s})`, transformOrigin: "50% 100%", filter: "drop-shadow(0 20px 30px rgba(0,0,0,0.28))" }}>
        <OffthreadVideo src={staticFile(cutout)} startFrom={atF} muted transparent style={vid} />
      </div>
    </AbsoluteFill>
  );
};

/* ---------- HeadlineWall (08 headline wall): newspaper-clipping cards made from TEXT (no screenshots needed) fly in and pin
   to the wall around the head. Use with behind: true so the cutout sits in front. Slots run down both sides and across the top,
   so the centre (the face) stays clear. `notes` = the lines; `kicker` = small caps over each one. ---------- */
const SLOTS: [number, number, number][] = [   // x, y, width
  [40, 250, 330], [700, 300, 340], [380, 130, 320], [30, 640, 300], [740, 720, 310], [60, 1010, 300], [720, 1100, 320], [400, 400, 280],
];
export const HeadlineWall: React.FC<{ notes: string[]; dur: number; kicker?: string; stagger?: number; dim?: number; seed?: number }> = ({
  notes, dur, kicker = "EL COYOTE DIESEL", stagger = 3, dim = 0.25, seed = 7,
}) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  return (
    <AbsoluteFill style={{ opacity: tailFade(frame, dur, 6) }}>
      <AbsoluteFill style={{ background: `rgba(0,0,0,${dim})` }} />
      {notes.slice(0, SLOTS.length).map((n, i) => {
        const [x, y, w] = SLOTS[i]; const p = popSoft(frame, fps, Math.round(i * stagger));
        const rot = -7 + rnd(i, 3, seed) * 14;
        const fromX = x < 400 ? -60 : 60;
        return (
          <div key={i} style={{ position: "absolute", left: x, top: y, width: w, background: "#f6f2e6", padding: "16px 18px 18px", boxShadow: cardShadow, transform: `translate(${(1 - p) * fromX}px, ${(1 - p) * -40}px) rotate(${rot + (1 - p) * 10}deg) scale(${0.8 + 0.2 * p})`, opacity: p }}>
            <div style={{ fontFamily: F.uiSemi, fontSize: 15, letterSpacing: 2.5, color: C.oxblood, borderBottom: `2px solid ${C.ink}`, paddingBottom: 6, marginBottom: 8 }}>{kicker}</div>
            <div style={{ fontFamily: F.serif, fontStyle: "normal", fontSize: 44, lineHeight: 1.0, color: C.ink }}>{n}</div>
            <div style={{ position: "absolute", left: "50%", top: -9, width: 18, height: 18, marginLeft: -9, borderRadius: 9, background: C.oxblood, boxShadow: "0 3px 5px rgba(0,0,0,0.4)" }} />
          </div>
        );
      })}
    </AbsoluteFill>
  );
};

/* ---------- PaperCut (13 paper cut): zine collage. Cream paper with a torn yellow sheet, a scribble and a pencil grid; the person
   becomes a die-cut sticker (StickerEdge) that slaps on; `letters` drop in one at a time as ransom-note tiles. Front layer, needs cutout. ---------- */
export const PaperCut: React.FC<{ cutout: string; atF?: number; dur: number; letters?: string; paper?: string; accent?: string; lettersY?: number; scale?: number }> = ({
  cutout, atF = 0, dur, letters = "RIVAL", paper = "#ece4d2", accent = C.yellow, lettersY = 250, scale = 0.86,
}) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const tear = "polygon(0% 8%, 6% 3%, 13% 9%, 21% 2%, 30% 8%, 39% 3%, 48% 9%, 57% 2%, 66% 8%, 75% 3%, 84% 9%, 93% 3%, 100% 8%, 100% 94%, 92% 99%, 83% 93%, 74% 99%, 64% 94%, 55% 99%, 45% 93%, 36% 99%, 27% 94%, 17% 99%, 8% 93%, 0% 98%)";
  const sheet = prog(frame, 2, 10, backOut(1.4));
  const draw = prog(frame, 6, 16, EASE_OUT);
  const tiles = [C.ink, "#fff", accent, C.oxblood, "#fff", C.ink, accent];
  const tw = Math.min(150, Math.floor(860 / Math.max(1, letters.length)));
  const x0 = (1080 - letters.length * (tw + 10)) / 2;
  return (
    <AbsoluteFill style={{ opacity: tailFade(frame, dur, 5) }}>
      <AbsoluteFill style={{ background: paper }} />
      <AbsoluteFill style={{ backgroundImage: "linear-gradient(rgba(20,20,20,0.07) 2px, transparent 2px), linear-gradient(90deg, rgba(20,20,20,0.07) 2px, transparent 2px)", backgroundSize: "90px 90px" }} />
      <div style={{ position: "absolute", left: 430, top: 760, width: 720, height: 560, background: accent, clipPath: tear, transform: `rotate(-4deg) translateX(${(1 - sheet) * 500}px)` }} />
      <div style={{ position: "absolute", left: -60, top: 1240, width: 520, height: 420, background: "#d8c7a2", clipPath: tear, transform: `rotate(5deg) translateX(${(1 - sheet) * -400}px)` }} />
      <svg width={1080} height={1920} style={{ position: "absolute", inset: 0 }}>
        <path d="M150 640 l40 150 l40 -150 l40 150 l40 -150 l40 150 l40 -150 l40 150" fill="none" stroke={C.oxblood} strokeWidth={12} strokeLinecap="round" strokeLinejoin="round" pathLength={1} strokeDasharray={1} strokeDashoffset={1 - draw} opacity={0.85} />
        <path d="M820 520 l90 90 M910 520 l-90 90" fill="none" stroke={C.ink} strokeWidth={14} strokeLinecap="round" pathLength={1} strokeDasharray={1} strokeDashoffset={1 - draw} />
      </svg>
      <div style={{ position: "absolute", inset: 0, transform: `scale(${scale})`, transformOrigin: "50% 100%" }}>
        <StickerEdge cutout={cutout} atF={atF} dur={dur + 99} width={18} color="#ffffff" slap />
      </div>
      {letters.split("").map((ch, i) => {
        if (ch === " ") return null;
        const p = popSoft(frame, fps, 8 + i * 3);
        const bg = tiles[i % tiles.length]; const dark = bg === C.ink || bg === C.oxblood;
        return (
          <div key={i} style={{ position: "absolute", left: x0 + i * (tw + 10), top: lettersY + (rnd(i, 1) - 0.5) * 30, width: tw, height: tw * 1.18, background: bg, color: dark ? "#fff" : C.ink, fontFamily: i % 2 ? F.heavy : F.block, fontSize: tw * 0.92, lineHeight: `${tw * 1.18}px`, textAlign: "center", boxShadow: "0 8px 14px rgba(0,0,0,0.3)", transform: `translateY(${(1 - p) * -160}px) rotate(${(rnd(i, 2) - 0.5) * 16}deg)`, opacity: p }}>{ch}</div>
        );
      })}
    </AbsoluteFill>
  );
};

/* ---------- GlassType (17 glass type): one big word as frosted glass. The letters blur and brighten whatever is behind them
   (backdrop-filter clipped to the text), with a bright rim, and drift slowly sideways. Front layer for the whole-frame look,
   or behind: true so it passes behind the head. Keep it to one short word. ---------- */
export const GlassType: React.FC<{ text: string; dur: number; y?: number; size?: number; drift?: number; blur?: number; font?: "heavy" | "block" }> = ({
  text, dur, y = 330, size = 330, drift = 140, blur = 16, font = "heavy",
}) => {
  const frame = useCurrentFrame();
  const inP = prog(frame, 0, 10, EASE_OUT);
  const x = drift / 2 - drift * (frame / Math.max(1, dur));
  const ff = font === "block" ? F.block : F.heavy; const cid = `glass${Math.round(y)}-${text.length}`;
  const base: React.CSSProperties = { position: "absolute", left: -200, right: -200, top: y, textAlign: "center", fontFamily: ff, fontSize: size, lineHeight: 1, letterSpacing: -4, whiteSpace: "nowrap", transform: `translateX(${x}px)` };
  return (
    <AbsoluteFill style={{ opacity: inP * tailFade(frame, dur, 6) }}>
      {/* soft shadow so the glass lifts off the picture */}
      <div style={{ ...base, color: "rgba(0,0,0,0.28)", filter: "blur(18px)", top: y + 16 }}>{text}</div>
      {/* the glass: backdrop blur + brighten over the whole frame, clipped to the letter shapes by an SVG clipPath
          (background-clip: text does not clip a backdrop-filter, it leaves a frosted rectangle) */}
      <svg width={0} height={0} style={{ position: "absolute" }}>
        <clipPath id={cid} clipPathUnits="userSpaceOnUse">
          <text x={540 + x} y={y + size * 0.86} textAnchor="middle" fontFamily={ff} fontSize={size} letterSpacing={-4}>{text}</text>
        </clipPath>
      </svg>
      <AbsoluteFill style={{ clipPath: `url(#${cid})`, backgroundColor: "rgba(255,255,255,0.20)", backdropFilter: `blur(${blur}px) brightness(1.25) saturate(1.2)`, WebkitBackdropFilter: `blur(${blur}px) brightness(1.25) saturate(1.2)` }} />
      {/* rim light and a top-left sheen */}
      <div style={{ ...base, color: "transparent", WebkitTextStroke: "3px rgba(255,255,255,0.75)" }}>{text}</div>
      <div style={{ ...base, color: "transparent", backgroundImage: "linear-gradient(160deg, rgba(255,255,255,0.75) 0%, rgba(255,255,255,0.05) 38%, rgba(255,255,255,0) 60%, rgba(255,255,255,0.22) 100%)", WebkitBackgroundClip: "text", backgroundClip: "text" }}>{text}</div>
    </AbsoluteFill>
  );
};
