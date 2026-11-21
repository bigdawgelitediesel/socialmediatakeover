import React from "react";
import { AbsoluteFill, Img, OffthreadVideo, staticFile, useCurrentFrame, useVideoConfig, interpolate } from "remotion";
import { C, F, cardShadow } from "../theme";
import { prog, tailFade, backOut, power4Out, popSoft, pop } from "./anim";
import { mono } from "./Menu";

/*
  Rapid.tsx: learned 2026-11-21 from three reels Jacob sent together
    @rourke        "34 lighting styles" (research/reel-references/2026-11-21-DfXaQcyoaJ5)  -> SlotList (the fill-in skeleton list)
    @_post2all     "5 free Claude skills" (research/reel-references/2026-11-21-DfrvfEtHP8j) -> ScoreBars, Fill (section invert), HUD tiles (in Menu.tsx)
    @justyn.ai     "Opus vs Fable edit battle" (research/reel-references/2026-11-21-DflSIzduyab) -> DuelStage (two clips side by side above the head)
  Palette stays El Coyote. All timings in frames at 30 fps.
*/

/* ---------- SlotList: the whole numbered skeleton is visible from frame 1 (empty slots), names fill in on their words.
   rourke: 34 names in 27 s, two columns, the empty slots are the retention device (the viewer can see how much is left).
   `rows` = [{text, at}] in frames from the overlay start. `cols` 1 or 2. `ink` for paper, default cream on footage. ---------- */
export const SlotList: React.FC<{ title?: string; rows: { text: string; at: number }[]; dur: number; x?: number; y?: number; w?: number; cols?: 1 | 2; size?: number; ink?: boolean; current?: boolean }> = ({
  title, rows, dur, x = 72, y = 330, w = 936, cols = 2, size = 24, ink = false, current = true,
}) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const p = pop(frame, fps, 0); const out = tailFade(frame, dur, 6);
  const color = ink ? C.ink : C.cream;
  const perCol = Math.ceil(rows.length / cols);
  const lineH = size * 1.45;
  const curIdx = rows.reduce((acc, r, i) => (frame >= r.at ? i : acc), -1);
  return (
    <AbsoluteFill style={{ opacity: p * out }}>
      {title && <div style={{ position: "absolute", left: x, width: w, top: y - size * 2.4, textAlign: "center", fontFamily: F.uiSemi, fontSize: size * 1.15, color, textShadow: ink ? "none" : "0 2px 6px rgba(0,0,0,0.6)" }}>{title}</div>}
      <div style={{ position: "absolute", left: x, top: y, width: w, display: "flex", gap: 30 }}>
        {Array.from({ length: cols }).map((_, c) => (
          <div key={c} style={{ flex: 1 }}>
            {rows.slice(c * perCol, (c + 1) * perCol).map((r, i) => {
              const idx = c * perCol + i;
              const rp = prog(frame, r.at, 5, power4Out);
              const on = current && idx === curIdx;
              return (
                <div key={i} style={{ display: "flex", gap: 10, height: lineH, alignItems: "center", fontFamily: F.ui, fontSize: size, color, textShadow: ink ? "none" : "0 2px 6px rgba(0,0,0,0.6)" }}>
                  <span style={{ fontFamily: mono, fontSize: size * 0.8, width: size * 1.5, textAlign: "right", opacity: 0.75 }}>{idx + 1}.</span>
                  {rp > 0
                    ? <span style={{ opacity: rp, transform: `translateX(${(1 - rp) * -8}px)`, fontWeight: on ? 700 : 400, background: on ? (ink ? C.tan : "rgba(201,179,140,0.28)") : "transparent", borderRadius: 6, padding: on ? "0 8px" : 0 }}>{r.text}</span>
                    : <span style={{ width: size * 4.2, height: 2, background: color, opacity: 0.18, borderRadius: 1 }} />}
                </div>
              );
            })}
          </div>
        ))}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- ScoreBars: labelled bars that fill left to right, then a total lands in a pill ("HOOK SCORE 93.8 STRONG").
   post2all 0:11 to 0:14 (the hook scorer terminal). For Rival: a part scored on cost / fitment / support, or a dyno card. ---------- */
export const ScoreBars: React.FC<{ title?: string; rows: { label: string; value: number }[]; total?: { label: string; value: string; tag?: string }; dur: number; x?: number; y?: number; w?: number; startAt?: number; stagger?: number; dark?: boolean }> = ({
  title, rows, total, dur, x = 72, y = 760, w = 936, startAt = 6, stagger = 5, dark = true,
}) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const p = popSoft(frame, fps, 0); const out = tailFade(frame, dur, 6);
  const bg = dark ? C.ink : "#fff", fg = dark ? C.cream : C.ink;
  const lastEnd = startAt + rows.length * stagger + 14;
  const tp = prog(frame, lastEnd, 8, backOut(2));
  return (
    <AbsoluteFill style={{ opacity: out }}>
      <div style={{ position: "absolute", left: x, top: y, width: w, background: bg, borderRadius: 18, boxShadow: cardShadow, padding: "22px 28px", transform: `translateY(${(1 - p) * 40}px) scale(${0.94 + 0.06 * p})`, opacity: p, fontFamily: mono, color: fg }}>
        {title && <div style={{ fontSize: 20, opacity: 0.6, marginBottom: 12 }}>{title}</div>}
        {rows.map((r, i) => {
          const bp = prog(frame, startAt + i * stagger, 14, power4Out);
          const v = Math.round(r.value * bp);
          return (
            <div key={i} style={{ display: "flex", alignItems: "center", gap: 14, height: 40, fontSize: 22 }}>
              <span style={{ width: 190, opacity: 0.85, letterSpacing: 1 }}>{r.label.toUpperCase()}</span>
              <div style={{ flex: 1, height: 14, background: dark ? "#2a2a2d" : "#e8e3d8", borderRadius: 7, overflow: "hidden" }}>
                <div style={{ width: `${v}%`, height: "100%", background: r.value >= 70 ? "#3ca865" : r.value >= 40 ? C.tan : C.hi }} />
              </div>
              <span style={{ width: 70, textAlign: "right", fontVariantNumeric: "tabular-nums" }}>{v.toFixed(0)}</span>
            </div>
          );
        })}
        {total && tp > 0 && (
          <div style={{ display: "flex", alignItems: "center", gap: 14, marginTop: 14, fontSize: 22 }}>
            <span style={{ width: 190, letterSpacing: 1, fontWeight: 700 }}>{total.label.toUpperCase()}</span>
            <span style={{ marginLeft: "auto", fontFamily: F.uiSemi, fontSize: 30, color: "#fff", background: "#3ca865", borderRadius: 10, padding: "4px 16px", transform: `scale(${0.7 + 0.3 * tp})`, opacity: tp, transformOrigin: "right center" }}>{total.value}{total.tag ? <span style={{ fontSize: 18, marginLeft: 10, opacity: 0.9 }}>{total.tag}</span> : null}</span>
          </div>
        )}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- DuelStage: two upright 9:16 clips side by side above the head, both running, a mono label under each, optional tilt.
   justyn.ai: OPUS 5.5 vs FABLE 5.2 for 40 s while he talks; the viewer picks one in the comments. A vote reel: the ask is spoken
   and in caption line 1, never burned in (house rule). For Rival: two parts, two hooks, two wheel setups. ---------- */
export const DuelStage: React.FC<{ left: string; right: string; labels?: [string, string]; dur: number; atF?: number; y?: number; w?: number; gap?: number; tilt?: boolean; muted?: boolean; winner?: 0 | 1; winAt?: number; ink?: boolean }> = ({
  left, right, labels = ["A", "B"], dur, atF = 0, y = 300, w = 400, gap = 40, tilt = false, muted = true, winner, winAt = 9999, ink = false,
}) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const out = tailFade(frame, dur, 6);
  const h = Math.round(w * 16 / 9);
  const x0 = (1080 - (2 * w + gap)) / 2;
  const win = prog(frame, winAt, 10, backOut(1.7));
  const card = (src: string, i: number) => {
    const p = popSoft(frame, fps, i * 4);
    const isWin = winner === i, lose = winner !== undefined && !isWin;
    const scale = 1 + (isWin ? 0.06 * win : 0) - (lose ? 0.06 * win : 0);
    return (
      <div key={i} style={{ position: "absolute", left: x0 + i * (w + gap), top: y, width: w, textAlign: "center", transform: `translateY(${(1 - p) * 50}px) rotate(${tilt ? (i === 0 ? -3 : 3) : 0}deg) scale(${(0.92 + 0.08 * p) * scale})`, opacity: p * (lose ? 1 - 0.5 * win : 1) }}>
        <div style={{ width: w, height: h, borderRadius: 22, overflow: "hidden", background: C.black, boxShadow: cardShadow, border: isWin && win > 0 ? `4px solid ${C.tan}` : "4px solid transparent", filter: lose ? `grayscale(${win})` : undefined }}>
          {/\.(mp4|webm|mov)$/i.test(src)
            ? <OffthreadVideo src={staticFile(src)} startFrom={atF} muted={muted} style={{ width: "100%", height: "100%", objectFit: "cover" }} />
            : <Img src={staticFile(src)} style={{ width: "100%", height: "100%", objectFit: "cover" }} />}
        </div>
        <div style={{ marginTop: 12, fontFamily: mono, fontSize: 22, letterSpacing: 4, color: ink ? C.ink : C.cream, textShadow: ink ? "none" : "0 2px 6px rgba(0,0,0,0.6)" }}>{labels[i]}</div>
      </div>
    );
  };
  return <AbsoluteFill style={{ opacity: out }}>{card(left, 0)}{card(right, 1)}</AbsoluteFill>;
};

/* ---------- Fill: a full-frame colour for a section (post2all flips the paper to black for item 5). List it with `behind: true`
   or first in the overlay order; everything after it sits on top. `fade` frames in and out. ---------- */
export const Fill: React.FC<{ color?: string; dur: number; fade?: number; opacity?: number }> = ({ color = C.black, dur, fade = 6, opacity = 1 }) => {
  const frame = useCurrentFrame();
  const a = interpolate(frame, [0, fade, dur - fade, dur], [0, opacity, opacity, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  return <AbsoluteFill style={{ background: color, opacity: a }} />;
};
