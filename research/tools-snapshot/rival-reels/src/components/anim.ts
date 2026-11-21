import { interpolate, spring } from "remotion";

export const EASE_OUT = (t: number) => 1 - Math.pow(1 - t, 3);
export const EASE_IN_OUT = (t: number) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);

/** 0..1 progress for a local frame window with ease-out, clamped. */
export const prog = (frame: number, start: number, dur: number, ease = EASE_OUT) =>
  ease(interpolate(frame, [start, start + dur], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }));

/** Spring that settles fast with a small overshoot (card arrivals). */
export const pop = (frame: number, fps: number, delay = 0) =>
  spring({ frame: frame - delay, fps, config: { damping: 16, stiffness: 170, mass: 0.9 } });

/** Fade out over the last `tail` frames of a window of `dur` frames. */
export const tailFade = (frame: number, dur: number, tail = 8) =>
  interpolate(frame, [dur - tail, dur], [1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });

/* ---- added 2026-11-21 from the nxtlvl / tenfoldmarc / ultra.skills studies ---- */
/** GSAP back.out(s): overshoot then settle. s = 1.70158 is GSAP's default, 2 to 3 is bouncier. */
export const backOut = (s = 1.70158) => (t: number) => { const u = t - 1; return 1 + u * u * ((s + 1) * u + s); };
export const expoOut = (t: number) => (t >= 1 ? 1 : 1 - Math.pow(2, -10 * t));
export const power4Out = (t: number) => 1 - Math.pow(1 - t, 4);
export const power2In = (t: number) => t * t;
/** Stepped progress (counters that tick, split-flap boards). */
export const steps = (n: number) => (t: number) => Math.min(1, Math.floor(t * n) / n);
/** Softer spring than pop(): card drops that should feel heavy (0.35 s settle). */
export const popSoft = (frame: number, fps: number, delay = 0) =>
  spring({ frame: frame - delay, fps, config: { damping: 12, stiffness: 170, mass: 0.9 } });
/** Seconds to frames helper for components that take timings in seconds. */
export const sf = (s: number, fps: number) => Math.round(s * fps);
