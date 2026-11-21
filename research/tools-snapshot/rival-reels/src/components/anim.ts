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
