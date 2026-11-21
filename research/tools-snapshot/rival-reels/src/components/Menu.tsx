import React from "react";
import { AbsoluteFill, Img, OffthreadVideo, staticFile, useCurrentFrame, useVideoConfig, interpolate } from "remotion";
import { C, F, cardShadow } from "../theme";
import { pop, popSoft, prog, tailFade, backOut, expoOut, power4Out, EASE_OUT, sf } from "./anim";

/*
  Menu.tsx: components learned 2026-11-21 from
    @ai.nxtlvl  "Stop paying for these 9 apps"   (research/reel-references/2026-11-21-DfU2nIgt8XK)
    @tenfoldmarc "17 video effects"               (research/reel-references/2026-11-21-Def9pj5TWtA)
    @ultra.skills "30 Claude animations"          (research/reel-references/2026-11-21-DfcxCxTBVsw)
    @edita.visuals quad showreel                  (research/reel-references/2026-11-21-Df3tIAzhB9h)
    nxtlvl public repo port list                  (research/reel-references/2026-11-21-nxtlvl-repo/PIPELINE-STUDY.md)
  Palette and type stay El Coyote (theme.ts). Every timing below is the shipped value from those studies, in frames at 30 fps.
*/

export const hardShadow = `12px 13px 0 ${C.ink}`;        // the REPO sticker look
export const mono = "JetBrains Mono, Consolas, monospace"; // mono metadata (font file optional; falls back cleanly)

/* ---------- ProgressHud: "3/9" counter + dots (or a bar) + handle. The retention device of every menu reel. ---------- */
export const ProgressHud: React.FC<{ count: number; total: number; handle?: string; dur: number; y?: number; variant?: "dots" | "bar" | "tiles"; progress?: number; icons?: string[]; ink?: boolean }> = ({
  count, total, handle = "@elcoyotediesel", dur, y = 300, variant = "dots", progress, icons = [], ink = false,
}) => {   // tiles (post2all 2026-11-13): numbered tiles, "?" for the current one, the icon + green dot once done. ink: dark chrome on paper.
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const p = pop(frame, fps, 0);
  return (
    <AbsoluteFill style={{ opacity: p }}>
      <div style={{ position: "absolute", left: 72, right: 130, top: y, display: "flex", alignItems: "center", gap: 16 }}>
        <div style={{ fontFamily: mono, fontSize: 30, letterSpacing: 2, color: ink ? C.ink : C.cream, background: ink ? "transparent" : C.ink, border: `3px solid ${ink ? C.ink : C.cream}`, borderRadius: 10, padding: "4px 14px", fontVariantNumeric: "tabular-nums" }}>
          {String(count).padStart(2, "0")}<span style={{ opacity: 0.55 }}>/{total}</span>
        </div>
        {variant === "tiles" ? (
          <div style={{ display: "flex", gap: 8 }}>
            {Array.from({ length: total }).map((_, i) => {
              const done = i < count - 1, cur = i === count - 1;
              const bump = prog(frame, 0, 6, backOut(2));
              const fg = ink ? "#fff" : C.ink, bgTile = ink ? C.ink : C.cream;
              return (
                <div key={i} style={{ position: "relative", width: 44, height: 44, borderRadius: 9, background: cur ? C.hi : done ? "#fff" : bgTile, boxShadow: "0 3px 8px rgba(0,0,0,0.18)", display: "flex", alignItems: "center", justifyContent: "center", fontFamily: mono, fontSize: 22, color: cur ? "#fff" : fg, transform: cur ? `scale(${0.8 + 0.2 * bump}) rotate(${(1 - bump) * -10}deg)` : "none", overflow: "visible" }}>
                  {done && icons[i] ? <Img src={staticFile(icons[i])} style={{ width: 28, height: 28, objectFit: "contain" }} /> : cur ? "?" : i + 1}
                  {done && <span style={{ position: "absolute", right: -4, top: -4, width: 12, height: 12, borderRadius: 6, background: "#3ca865", border: "2px solid #fff" }} />}
                </div>
              );
            })}
          </div>
        ) : variant === "dots" ? (
          <div style={{ display: "flex", gap: 10 }}>
            {Array.from({ length: total }).map((_, i) => (
              <div key={i} style={{ width: 20, height: 20, borderRadius: 5, border: `3px solid ${C.cream}`, background: i < count ? C.tan : "transparent", transition: "none" }} />
            ))}
          </div>
        ) : (
          <div style={{ width: 220, height: 26, border: `3px solid ${C.cream}`, borderRadius: 13, overflow: "hidden" }}>
            <div style={{ width: `${Math.round((progress ?? count / total) * 100)}%`, height: "100%", background: C.tan }} />
          </div>
        )}
        <div style={{ marginLeft: "auto", fontFamily: mono, fontSize: 22, color: ink ? C.ink : C.cream, opacity: 0.7 }}>{handle}</div>
      </div>
    </AbsoluteFill>
  );
};

/* ---------- SidebarList: the tenfoldmarc / ultra.skills numbered menu. `current` turns tan and bold; `cols` 1 or 2. ---------- */
export const SidebarList: React.FC<{ items: string[]; current: number; dur: number; x?: number; y?: number; cols?: 1 | 2; size?: number; w?: number; scroll?: boolean }> = ({
  items, current, dur, x = 72, y = 420, cols = 2, size = 24, w = 936, scroll = false,
}) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const p = pop(frame, fps, 0);
  const perCol = Math.ceil(items.length / cols);
  const lineH = size * 1.55;
  // ultra.skills: a single column that auto-scrolls so the current item sits mid-list
  const offset = scroll && cols === 1 ? Math.max(0, (current - 3)) * lineH : 0;
  return (
    <AbsoluteFill style={{ opacity: p }}>
      <div style={{ position: "absolute", left: x, top: y, width: w, display: "flex", gap: 24, overflow: "hidden", height: scroll ? lineH * 8 : undefined }}>
        {Array.from({ length: cols }).map((_, c) => (
          <div key={c} style={{ flex: 1, transform: `translateY(${-offset}px)` }}>
            {items.slice(c * perCol, (c + 1) * perCol).map((it, i) => {
              const idx = c * perCol + i + 1; const on = idx === current; const done = idx < current;
              return (
                <div key={i} style={{ display: "flex", gap: 12, height: lineH, alignItems: "center", fontFamily: F.ui, fontSize: size, color: on ? C.ink : C.cream, opacity: on ? 1 : done ? 0.45 : 0.6, fontWeight: on ? 700 : 400 }}>
                  <span style={{ fontFamily: mono, fontSize: size * 0.8, opacity: 0.8, width: size * 1.6, color: on ? C.ink : C.tan }}>{String(idx).padStart(2, "0")}</span>
                  <span style={{ background: on ? C.tan : "transparent", borderRadius: 8, padding: on ? "2px 12px" : 0 }}>{it}</span>
                  {done && <span style={{ color: C.tan, fontSize: size * 0.85, marginLeft: 2 }}>✓</span>}
                </div>
              );
            })}
          </div>
        ))}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- PhoneStage: the floating 9:16 card that plays one demo per item (tenfoldmarc). Children = the demo; badge = "01/17". ---------- */
export const PhoneStage: React.FC<{ count?: number; total?: number; dur: number; x?: number; y?: number; w?: number; src?: string; atF?: number; children?: React.ReactNode; bob?: boolean; label?: string }> = ({
  count, total, dur, x = 375, y = 690, w = 330, src, atF = 0, children, bob = true, label,
}) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const p = popSoft(frame, fps, 0); const out = tailFade(frame, dur, 6);
  const h = Math.round(w * 16 / 9);
  const dy = bob ? Math.sin(frame / fps * 1.6) * 2 : 0;
  return (
    <AbsoluteFill style={{ opacity: out }}>
      <div style={{ position: "absolute", left: x, top: y + dy, width: w, height: h, borderRadius: 34, border: "6px solid #fff", overflow: "hidden", background: C.black, boxShadow: cardShadow, transform: `translateY(${(1 - p) * 40}px) scale(${0.9 + 0.1 * p})`, opacity: p }}>
        {src && (src.endsWith(".mp4") || src.endsWith(".webm")
          ? <OffthreadVideo src={staticFile(src)} startFrom={atF} muted style={{ width: "100%", height: "100%", objectFit: "cover" }} />
          : <Img src={staticFile(src)} style={{ width: "100%", height: "100%", objectFit: "cover" }} />)}
        {children}
        {count !== undefined && (
          <div style={{ position: "absolute", left: 14, top: 14, fontFamily: mono, fontSize: 20, color: "#fff", background: "rgba(20,20,20,0.85)", borderRadius: 10, padding: "4px 10px", fontVariantNumeric: "tabular-nums" }}>
            {String(count).padStart(2, "0")}<span style={{ opacity: 0.55 }}>/{total}</span>
          </div>
        )}
      </div>
      {label && (
        <div style={{ position: "absolute", left: x, width: w, top: y + h + 14 + dy, textAlign: "center", opacity: p }}>
          <span style={{ fontFamily: F.uiSemi, fontSize: 24, color: C.ink, background: C.tan, borderRadius: 20, padding: "6px 18px" }}>{label}</span>
        </div>
      )}
    </AbsoluteFill>
  );
};

/* ---------- CountUp: a number that counts to `to` over `dur` frames, tabular, suffix lands after the count. ---------- */
export const useCountUp = (frame: number, to: number, from = 0, start = 0, len = 22, ease = (t: number) => 1 - Math.pow(1 - t, 3)) => {
  const t = ease(interpolate(frame, [start, start + len], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }));
  return Math.round(from + (to - from) * t);
};
export const CountUp: React.FC<{ to: number; from?: number; prefix?: string; suffix?: string; dur: number; start?: number; len?: number; size?: number; color?: string; x?: number; y?: number; label?: string; font?: string; group?: boolean }> = ({
  to, from = 0, prefix = "", suffix = "", dur, start = 2, len = 22, size = 200, color = C.cream, x = 72, y = 700, label, font, group,
}) => {
  const frame = useCurrentFrame();
  const v = useCountUp(frame, to, from, start, len);
  const done = frame >= start + len; const out = tailFade(frame, dur, 6);
  return (
    <AbsoluteFill style={{ opacity: out }}>
      <div style={{ position: "absolute", left: x, top: y }}>
        <div style={{ fontFamily: font ?? F.block, fontSize: size, lineHeight: 0.9, color, fontVariantNumeric: "tabular-nums", textShadow: "0 10px 30px rgba(0,0,0,0.45)" }}>
          {prefix}{(group ?? !(to >= 1900 && to <= 2100)) ? v.toLocaleString("en-US") : String(v)}<span style={{ opacity: done ? 1 : 0, fontSize: size * 0.5, marginLeft: 10, color: C.tan }}>{suffix}</span>
        </div>
        {label && <div style={{ fontFamily: F.uiItalic, fontSize: 38, letterSpacing: 4, color: C.tan, textTransform: "uppercase", marginTop: 8 }}>{label}</div>}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- StrikeStamp: a row (icon + name + meta) gets a strike bar then a rotated stamp slaps on. nxtlvl's PAID -> FREE beat. ---------- */
export const StrikeStamp: React.FC<{ name: string; meta?: string; icon?: string; tag?: string; stamp?: string; strikeAt?: number; dur: number; x?: number; y?: number; w?: number; stampColor?: string }> = ({
  name, meta = "", icon, tag = "STOCK", stamp = "RIVAL", strikeAt = 12, dur, x = 72, y = 560, w = 936, stampColor = C.oxblood,
}) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const p = popSoft(frame, fps, 0); const out = tailFade(frame, dur, 6);
  const strike = prog(frame, strikeAt, 9, EASE_OUT);                       // 0.3 s power3.out
  const st = prog(frame, strikeAt + 4, 8, power4Out);                       // stamp 0.12 s after the strike, 0.25 s power4.out
  return (
    <AbsoluteFill style={{ opacity: out }}>
      <div style={{ position: "absolute", left: x, top: y, width: w, background: C.cream, border: `3px solid ${C.ink}`, borderRadius: 20, padding: "18px 24px", display: "flex", alignItems: "center", gap: 18, boxShadow: hardShadow, transform: `translateY(${(1 - p) * 40}px) scale(${0.92 + 0.08 * p})`, opacity: p }}>
        <div style={{ fontFamily: mono, fontSize: 20, letterSpacing: 2, color: C.oxblood, border: `2px solid ${C.oxblood}`, borderRadius: 8, padding: "4px 10px" }}>{tag}</div>
        {icon && <Img src={staticFile(icon)} style={{ height: 56, width: "auto" }} />}
        <div style={{ position: "relative", flex: 1 }}>
          <div style={{ fontFamily: F.uiSemi, fontSize: 44, color: C.ink, opacity: 1 - 0.55 * strike }}>{name}</div>
          <div style={{ position: "absolute", left: -6, top: "50%", height: 12, borderRadius: 6, width: "calc(100% + 12px)", background: C.oxblood, transformOrigin: "0 50%", transform: `translateY(-50%) scaleX(${strike})` }} />
        </div>
        <div style={{ fontFamily: mono, fontSize: 22, color: "#777" }}>{meta}</div>
        <div style={{ position: "absolute", right: 28, top: -26, fontFamily: F.heavy, fontSize: 60, letterSpacing: 2, color: stampColor, border: `8px solid ${stampColor}`, borderRadius: 16, padding: "2px 18px", background: "rgba(239,233,220,0.92)", transform: `rotate(${-20 + 12 * st}deg) scale(${2.4 - 1.4 * st})`, opacity: st, transformOrigin: "50% 50%" }}>{stamp}</div>
      </div>
    </AbsoluteFill>
  );
};

/* ---------- ItemCard: the swap card (icon tile, name, mono sub-line, counter, tag, chips that pop on their words, footnote, corner sticker). ---------- */
export type Chip = { text: string; at: number };   // at = frames after the card appears
export const ItemCard: React.FC<{ title: string; sub?: string; icon?: string; count?: { to: number; prefix?: string; suffix?: string; label?: string }; tag?: string; chips?: Chip[]; foot?: string; sticker?: string; stickerAt?: number; dur: number; x?: number; y?: number; w?: number; ghost?: boolean; shadow?: "hard" | "soft" }> = ({
  title, sub, icon, count, tag, chips = [], foot, sticker, stickerAt = 24, dur, x = 72, y = 760, w = 936, ghost = false, shadow = "hard",
}) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const p = popSoft(frame, fps, ghost ? 9 : 0);
  const ghostOp = ghost ? (frame < 9 ? 0.3 : 1) : 1;
  const out = tailFade(frame, dur, 6);
  const v = count ? useCountUp(frame, count.to, 0, 6, 20) : 0;
  const stp = prog(frame, stickerAt, 8, power4Out);
  return (
    <AbsoluteFill style={{ opacity: out }}>
      <div style={{ position: "absolute", left: x, top: y, width: w, background: C.cream, border: `3px solid ${C.ink}`, borderRadius: 28, padding: 30, boxShadow: shadow === "hard" ? hardShadow : "0 18px 40px rgba(0,0,0,0.35)", transform: `translateY(${(1 - p) * 40}px) scale(${0.92 + 0.08 * p})`, opacity: Math.min(p, 1) * ghostOp }}>
        <div style={{ display: "flex", alignItems: "center", gap: 22 }}>
          {icon && <div style={{ width: 110, height: 110, borderRadius: 22, background: C.oxblood, display: "flex", alignItems: "center", justifyContent: "center", overflow: "hidden" }}><Img src={staticFile(icon)} style={{ width: "80%", height: "80%", objectFit: "contain" }} /></div>}
          <div style={{ flex: 1 }}>
            <div style={{ fontFamily: F.block, fontSize: 64, lineHeight: 1, color: C.ink, letterSpacing: 1 }}>{title}</div>
            {sub && <div style={{ fontFamily: mono, fontSize: 22, color: "#666", marginTop: 6 }}>{sub}</div>}
          </div>
        </div>
        {(count || tag) && (
          <div style={{ display: "flex", gap: 14, marginTop: 22, alignItems: "center" }}>
            {count && <div style={{ fontFamily: mono, fontSize: 26, color: C.ink, border: `2px solid ${C.ink}`, borderRadius: 10, padding: "6px 14px", fontVariantNumeric: "tabular-nums" }}>{count.prefix ?? ""}{v.toLocaleString("en-US")}{count.suffix ?? ""}{count.label ? ` ${count.label}` : ""}</div>}
            {tag && <div style={{ fontFamily: mono, fontSize: 22, letterSpacing: 2, color: C.green, border: `2px solid ${C.green}`, borderRadius: 10, padding: "6px 14px" }}>{tag}</div>}
          </div>
        )}
        {chips.length > 0 && (
          <div style={{ display: "flex", flexWrap: "wrap", gap: 12, marginTop: 22 }}>
            {chips.map((c, i) => {
              const cp = pop(frame, fps, c.at);
              return <div key={i} style={{ fontFamily: F.uiSemi, fontSize: 30, color: C.ink, background: C.tan, borderRadius: 30, padding: "8px 18px", border: `2px solid ${C.ink}`, transform: `scale(${cp})`, opacity: cp }}>{c.text}</div>;
            })}
          </div>
        )}
        {foot && <div style={{ fontFamily: mono, fontSize: 20, color: "#777", marginTop: 20 }}>{foot}</div>}
        {sticker && (
          <div style={{ position: "absolute", right: -18, bottom: -22, fontFamily: F.heavy, fontSize: 34, letterSpacing: 2, color: C.cream, background: C.green, border: `4px solid ${C.cream}`, borderRadius: 10, padding: "6px 18px", transform: `rotate(${-8 + 4 * stp}deg) scale(${2 - stp})`, opacity: stp, boxShadow: "0 6px 0 rgba(0,0,0,0.4)" }}>{sticker}</div>
        )}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- Headline: one phrase, words rise in, one accent word in serif italic on a tan pill (nxtlvl caption grammar). ---------- */
export const Headline: React.FC<{ text: string; accent?: string; dur: number; y?: number; size?: number; align?: "center" | "left" }> = ({ text, accent, dur, y = 420, size = 60, align = "center" }) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const words = text.split(" "); const out = tailFade(frame, dur, 6);
  const fit = Math.max(0.68, Math.min(1, 24 / text.length)); size = size * fit;   // one line up to ~24 chars at full size, then shrink
  return (
    <AbsoluteFill style={{ opacity: out }}>
      <div style={{ position: "absolute", left: 72, right: 130, top: y, display: "flex", flexWrap: "wrap", gap: "0 14px", justifyContent: align === "center" ? "center" : "flex-start", alignItems: "baseline" }}>
        {words.map((w, i) => {
          const isAcc = accent && w.replace(/[.,!?]/g, "").toLowerCase() === accent.toLowerCase();
          const p = prog(frame, i * 2, 10, backOut(2));
          const ap = prog(frame, 9 + i * 2, 14, backOut(2.4));
          return isAcc ? (
            <span key={i} style={{ fontFamily: F.serif, fontSize: size * 1.35, color: C.ink, background: C.tan, borderRadius: 10, padding: "0 16px 4px", transform: `scale(${0.6 + 0.4 * ap}) rotate(${-6 + 6 * ap}deg)`, opacity: ap, display: "inline-block" }}>{w}</span>
          ) : (
            <span key={i} style={{ fontFamily: F.ui, fontSize: size, color: C.cream, textShadow: "0 6px 20px rgba(0,0,0,0.5)", transform: `translateY(${(1 - p) * 40}px)`, opacity: p, display: "inline-block" }}>{w}</span>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- GhostWord: a giant outline word behind the scene (Anton 330, 8 percent stroke). ---------- */
export const GhostWord: React.FC<{ text: string; dur: number; y?: number; size?: number; color?: string }> = ({ text, dur, y = 500, size = 330, color = "rgba(239,233,220,0.10)" }) => {
  const frame = useCurrentFrame();
  const p = prog(frame, 0, 15, EASE_OUT); const out = tailFade(frame, dur, 5);
  return (
    <AbsoluteFill style={{ alignItems: "center", paddingTop: y, opacity: p * out }}>
      <div style={{ fontFamily: F.block, fontSize: size, letterSpacing: -10, lineHeight: 0.9, color: "transparent", WebkitTextStroke: `4px ${color}`, transform: `scale(${1.25 - 0.25 * p})`, whiteSpace: "nowrap" }}>{text}</div>
    </AbsoluteFill>
  );
};

/* ---------- IrisWipe: a solid circle grows from a point to cover the frame then shrinks (0.6 s + 0.6 s). The one full-frame transition. ---------- */
export const IrisWipe: React.FC<{ dur: number; color?: string; cx?: number; cy?: number; grow?: number; hold?: number }> = ({ dur, color = C.oxblood, cx = 540, cy = 770, grow = 9, hold = 0 }) => {
  const frame = useCurrentFrame();
  const up = prog(frame, 0, grow, expoOut); const down = prog(frame, grow + hold, grow, power4Out);
  const r = 2400 * (up - down);
  return (
    <AbsoluteFill>
      <div style={{ position: "absolute", left: cx - r / 2, top: cy - r / 2, width: r, height: r, borderRadius: "50%", background: color }} />
    </AbsoluteFill>
  );
};

/* ---------- NegativeFlash: 2 frames of a white cutout silhouette on a hit (edita.visuals). Needs the RVM cutout webm. ---------- */
export const NegativeFlash: React.FC<{ cutout: string; atF?: number; dur: number; frames?: number; invert?: boolean }> = ({ cutout, atF = 0, dur, frames = 2, invert = false }) => {   // invert + frames 30 = the 1 s cream poster beat with a black silhouette (viashaan)
  const frame = useCurrentFrame();
  if (frame >= frames) return null;
  return (
    <AbsoluteFill style={{ background: C.cream }}>
      <OffthreadVideo src={staticFile(cutout)} startFrom={atF} muted transparent style={{ width: "100%", height: "100%", filter: invert ? "brightness(0)" : "brightness(0) invert(1)" }} />
    </AbsoluteFill>
  );
};

/* ---------- CommentGate: fake comment box, keyword typed and hearted, then a DM preview card with numbered chips.
   HOUSE RULE: Jacob allows no on-screen CTA on normal reels. Use ONLY on a comment-gated deliverable reel (parts list PDF, checklist). ---------- */
export const CommentGate: React.FC<{ word: string; reply: string; items?: string[]; dur: number; y?: number; handle?: string; typeAt?: number; dmAt?: number }> = ({
  word, reply, items = [], dur, y = 620, handle = "you", typeAt = 6, dmAt = 36,
}) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const p = popSoft(frame, fps, 0); const out = tailFade(frame, dur, 4);
  const perChar = 3; // 0.1 s per letter
  const n = Math.max(0, Math.min(word.length, Math.floor((frame - typeAt) / perChar)));
  const typed = frame >= typeAt + word.length * perChar;
  const heart = prog(frame, typeAt + word.length * perChar + 3, 9, backOut(2));
  const dm = prog(frame, dmAt, 15, backOut(1.5));
  return (
    <AbsoluteFill style={{ opacity: out }}>
      <div style={{ position: "absolute", left: 100, width: 880, top: y, background: "#fff", border: `3px solid ${C.ink}`, borderRadius: 26, boxShadow: "6px 7px 0 " + C.ink, padding: "18px 24px", transform: `translateY(${(1 - p) * 30}px)`, opacity: p }}>
        <div style={{ textAlign: "center", fontFamily: F.uiSemi, fontSize: 22, color: C.ink, marginBottom: 12 }}>Comments</div>
        <div style={{ display: "flex", alignItems: "center", gap: 16 }}>
          <div style={{ width: 52, height: 52, borderRadius: 26, background: `linear-gradient(135deg, ${C.oxblood}, ${C.tan})` }} />
          <div style={{ flex: 1 }}>
            <div style={{ fontFamily: mono, fontSize: 18, color: "#777" }}>{handle} · now</div>
            <div style={{ fontFamily: F.uiSemi, fontSize: 40, color: C.ink, minHeight: 48 }}>{word.slice(0, n)}<span style={{ opacity: typed ? 0 : (Math.floor(frame / 4) % 2), color: C.oxblood }}>|</span></div>
          </div>
          <div style={{ fontSize: 44, color: heart > 0 ? C.oxblood : "#bbb", transform: `scale(${1 + 0.5 * Math.sin(heart * Math.PI)})` }}>♥</div>
        </div>
        <div style={{ marginTop: 14, border: "2px solid #ddd", borderRadius: 30, padding: "10px 20px", fontFamily: F.ui, fontSize: 24, color: "#999" }}>Add a comment…</div>
      </div>
      {frame >= dmAt && (
        <div style={{ position: "absolute", left: 100, width: 880, top: y + 250, background: "#fff", border: `3px solid ${C.ink}`, borderRadius: 30, boxShadow: "6px 7px 0 " + C.ink, padding: "20px 26px", transform: `translateY(${(1 - dm) * -160}px) scale(${0.9 + 0.1 * dm})`, opacity: dm }}>
          <div style={{ fontFamily: mono, fontSize: 18, color: "#777" }}>Messages · now</div>
          <div style={{ fontFamily: F.uiSemi, fontSize: 32, color: C.ink, marginTop: 4 }}>{reply}</div>
          {items.length > 0 && (
            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 10, marginTop: 14 }}>
              {items.map((it, i) => {
                const cp = prog(frame, dmAt + 15 + Math.floor(i / 2) * 8, 6, backOut(1.7));
                return <div key={i} style={{ fontFamily: mono, fontSize: 20, color: C.ink, border: `2px solid ${C.ink}`, borderRadius: 8, padding: "6px 12px", opacity: cp, transform: `scale(${0.9 + 0.1 * cp})` }}>{i + 1} · {it}</div>;
              })}
            </div>
          )}
        </div>
      )}
    </AbsoluteFill>
  );
};

/* ---------- QuadWall: four independent 9:16 panels at once (edita.visuals). Each panel = a video/image src with optional startFrom. ---------- */
export const QuadWall: React.FC<{ panels: { src: string; atF?: number }[]; dur: number; gap?: number; radius?: number }> = ({ panels, dur, gap = 10, radius = 18 }) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const out = tailFade(frame, dur, 6);
  const w = (1080 - gap) / 2, h = (1920 - gap) / 2;
  return (
    <AbsoluteFill style={{ background: C.black, opacity: out }}>
      {panels.slice(0, 4).map((pn, i) => {
        const p = popSoft(frame, fps, i * 3);
        const col = i % 2, row = Math.floor(i / 2);
        return (
          <div key={i} style={{ position: "absolute", left: col * (w + gap), top: row * (h + gap), width: w, height: h, borderRadius: radius, overflow: "hidden", opacity: p, transform: `scale(${0.96 + 0.04 * p})` }}>
            {pn.src.endsWith(".mp4") || pn.src.endsWith(".webm")
              ? <OffthreadVideo src={staticFile(pn.src)} startFrom={pn.atF ?? 0} muted style={{ width: "100%", height: "100%", objectFit: "cover" }} />
              : <Img src={staticFile(pn.src)} style={{ width: "100%", height: "100%", objectFit: "cover" }} />}
          </div>
        );
      })}
    </AbsoluteFill>
  );
};

/* ---------- Checklist: dark task card, rows type in, a tan check fills, "1 of 3" counter and bar (tenfoldmarc #07). ---------- */
export const Checklist: React.FC<{ title?: string; rows: { text: string; at: number; doneAt?: number }[]; dur: number; x?: number; y?: number; w?: number; reveal?: boolean }> = ({ title = "ALL YOU NEED TO DO", rows, dur, x = 72, y = 420, w = 936, reveal = false }) => {   // reveal: future rows shown blurred (kallaway), not empty
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const p = popSoft(frame, fps, 0); const out = tailFade(frame, dur, 6);
  const done = rows.filter((r) => r.doneAt !== undefined && frame >= r.doneAt).length;
  return (
    <AbsoluteFill style={{ opacity: out }}>
      <div style={{ position: "absolute", left: x, top: y, width: w, background: C.ink, borderRadius: 24, padding: "22px 28px", boxShadow: cardShadow, transform: `translateY(${(1 - p) * 40}px)`, opacity: p }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
          <div style={{ fontFamily: mono, fontSize: 20, letterSpacing: 3, color: C.tan }}>■ {title}</div>
          <div style={{ fontFamily: mono, fontSize: 22, color: C.cream, fontVariantNumeric: "tabular-nums" }}>{done} of {rows.length}</div>
        </div>
        <div style={{ height: 6, background: "#333", borderRadius: 3, marginTop: 10, overflow: "hidden" }}><div style={{ width: `${(done / rows.length) * 100}%`, height: "100%", background: C.tan }} /></div>
        {rows.map((r, i) => {
          const n = Math.max(0, Math.min(r.text.length, Math.floor((frame - r.at) / 2)));
          const isDone = r.doneAt !== undefined && frame >= r.doneAt;
          const cp = r.doneAt !== undefined ? prog(frame, r.doneAt, 8, backOut(3)) : 0;
          return (
            <div key={i} style={{ display: "flex", alignItems: "center", gap: 18, marginTop: 18, opacity: frame >= r.at ? 1 : 0.35 }}>
              <div style={{ width: 40, height: 40, borderRadius: 20, border: `3px solid ${isDone ? C.tan : "#666"}`, background: isDone ? C.tan : "transparent", display: "flex", alignItems: "center", justifyContent: "center", color: C.ink, fontSize: 26, transform: `scale(${isDone ? 0.8 + 0.2 * cp : 1})` }}>{isDone ? "✓" : ""}</div>
              <div style={{ fontFamily: F.uiSemi, fontSize: 36, color: isDone ? C.tan : C.cream, flex: 1, filter: reveal && frame < r.at ? "blur(7px)" : undefined, opacity: reveal && frame < r.at ? 0.5 : 1 }}>{frame >= r.at ? r.text.slice(0, n) : (reveal ? r.text : "")}</div>
              {!reveal && !isDone && frame < r.at && <div style={{ flex: 1, height: 8, background: "#333", borderRadius: 4 }} />}
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};
