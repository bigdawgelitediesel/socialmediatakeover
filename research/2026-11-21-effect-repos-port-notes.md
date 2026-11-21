# Effect repos, read as code: port notes for rival-reels and build_reel3

Date: 2026-11-21. Scope: the public code behind @tenfoldmarc's 17 effects (his free skill plus three community rebuilds), the repo packaging @viashaan's nine ANIMATE styles, and HyperFrames' own orbit, matte and text-behind material. Every repo was shallow-cloned into `research/reel-references/2026-11-21-effect-repos/clone/<name>/` (git-ignored, nothing in there was run) and read, not summarised from READMEs. Our side of the comparison: `VIDEO/tools/rival-reels/src/components/Effects.tsx`, `Menu.tsx`, `anim.ts`, `theme.ts`, `RivalReel.tsx`, `VIDEO/tools/matte.py` (RVM ONNX, VP9 alpha WebM), `facetrack.py` (YuNet) and `build_reel3.py` (slots: zoom, ramp, speed, stab, shake, flash, mblur, whip xfade).

Short version: the orbit, the doodle boil, the sticker edge and the HUD are all cheap and all fit what we already have (RVM cutout, face track, behind-overlays in RivalReel, eval=frame scale in build_reel3). The zoom-through is the one thing our kit does wrong today (gaussian blur instead of a zoom streak) and the fix is one wrapper. Map route, teardown and timeline are real builds (three.js or 2.5D CSS), worth it only for the two or three reels a year that earn them.

---

## 1. Repo table

| Repo | URL | License | Stars (2026-11-21) | What it actually contains |
|---|---|---|---|---|
| tenfoldmarc/video-edit-skill | https://github.com/tenfoldmarc/video-edit-skill | none declared (treat as all rights reserved, read only) | 164, 36 forks, last push 2026-10-15 | His free Oct 1 skill. HyperFrames template `assets/template/build.py` (30 KB Python that emits HTML + GSAP), `references/looks.md` (three looks with exact filter strings and type sizes), `layout.md` (safe zones, behind-head formula), `overlays.md` (sub-agent insert pattern), `gotchas.md` (render and Windows traps), `scripts/` (assemble, cutout, headpos, transcribe). Contains the orbit in full. The 17 effects are NOT here. |
| ONIKOSIOLA/video-editing-kit | https://github.com/ONIKOSIOLA/video-editing-kit | none declared | 2, last push 2026-11-20 | `skills/video-overlays/reel-effects-17.md`: build plans for all 17 with layer notes, three render-verified (cover story, paper cut partial, vertigo partial), the HLG trap table and a verified sandwich skeleton for hyperframes 0.8.162. `effects.md`: six render-verified CSS/SVG recipes (glow, dissolve, mask reveal, shimmer, sheen, liquid wipe). Also a 66 KB talking-head-recut skill with 10 HTML style references. |
| Vibha-Ramprakash/claude-video-effects | https://github.com/Vibha-Ramprakash/claude-video-effects | MIT (LICENSE file; GitHub API says NOASSERTION) | 1,116, 261 forks, last push 2026-11-12 | The ffmpeg-only one. `scripts/fx.py` (156 KB, 51 effects as Python functions over numpy frames piped from ffmpeg rawvideo). MediaPipe Selfie Segmenter matte at 540 px with a guided filter, YuNet face track, forward-backward smoothed. Has orbit, scribble, countdown-flip, rabbit-hole, spotlight, LED sign, liquid glass (SDF refraction), swipe before/after, slow push, over-the-shoulder zoom, red render timeline. A `fx_private.py` hook exists for a private studio timeline. |
| Dryxio/effects-skill | https://github.com/Dryxio/effects-skill | MIT | 8, last push 2026-10-26 | The Remotion one (French). 36 effects in three TSX files (`hero.tsx`, `grid.tsx`, `extra.tsx`) plus `kit.tsx` helpers. BiRefNet-portrait cutout to per-frame WebP at 15 fps (30 with `--smooth`), face box from the alpha. Renders 4K by default (`scale: 2`). Closest stack to ours. |
| rajshaikh-ai/claude-animation-styles | https://github.com/rajshaikh-ai/claude-animation-styles | MIT (LICENSE file) | 1, created 2026-11-02 | viashaan's nine styles as Remotion TSX under `skills/<style>/references/<Style>.tsx`, each with a `card.md` spec (palette, fonts, "How it moves", "Never") and an ffmpeg splice script. Map Route, Teardown and App Mockup use `@remotion/three` + `@react-three/fiber`; the rest are DOM/SVG/canvas. 25 MB of demo GIFs. |
| heygen-com/hyperframes | https://github.com/heygen-com/hyperframes | Apache-2.0 | 87,738, 8,164 forks | The renderer tenfoldmarc uses. Sparse-checked `docs/`, `skills/`, `examples/`. Relevant: `docs/guides/remove-background.mdx` (cutout + inverse plate in one pass), `hdr.mdx`, `motion-blur.mdx`, `rendering.mdx` (alpha WebM facts), `4k-rendering.mdx`, `skills/hyperframes/references/captions.md` ("Text behind the speaker" rules), catalog `orbit-card` and `three-orbiting-cards` (three.js orbits driven by a paused GSAP timeline), `reverse-any-video` skill. |

Not cloned: itsCet/Your-AI PR #13 (browser canvas engine, 13 of 17, French) and adamgodigital/claude-reel-effects (email-gated). Nothing in them is likely to beat the five above.

---

## 2. The shared primitive: the matte sandwich, as each stack builds it

Every stack converged on the same four layers. Ours already matches (RivalReel: plate, `behind` overlays, cutout, front overlays).

| Stack | Bottom to top | How the cutout is made | Notes from the code |
|---|---|---|---|
| tenfoldmarc (HyperFrames) | `#bgv` z0 (aroll.mp4) > `.back` words z3 and `.orb.b` z3 (brightness .75) > `#cutwrap` z4 (subject.webm) > `.orb.f` z6 > grade overlays z7 (soft-light tone + vignette + top/bottom gradients) > captions z8 > inserts z9 | `npx hyperframes remove-background assets/aroll.mp4 -o assets/subject.webm --quality best`, after a CFR re-encode (`setpts=N/30/TB -fps_mode cfr -g 30 -keyint_min 30`); `cutout.py` asserts equal frame counts or the cutout drifts | The whole `#stage` (base + back + cutout) is one wrapper so the cut punch (scale 1.05 to 1 over .32 s) moves them together. Grade is CSS `filter` on the `.g` class shared by base and cutout. |
| ONIKOSIOLA (HyperFrames 0.8.162) | `video-wrap` z1 < `plate-wrap` (bgplate.webm, inverse alpha) z2 < `behind-scene` sub-comp z10 < `subject-wrap` z20 < `front-scene` z40 | `remove-background clip.mp4 -o subject.webm -b bgplate.webm` | Sticker border = chained `drop-shadow(±3px 0 0 #fff)` on `#subject-wrap`, verified in render. Vertigo scales `#plate-wrap` only; the hole the matte leaves grows with scale (seam at 1.3x, subtle at 1.16x). |
| Vibha (ffmpeg + numpy) | one float RGB frame `c.img` plus a float mask `c.m`; `comp(layer, behind=True)` multiplies the layer alpha by `(1 - m)`, `guard=True` only hides it inside a face ellipse `((x-fx)/(0.95 fw))^2 + ((y-fy)/(1.35 fw))^2 < 1.2` | MediaPipe Selfie Segmenter at 540 px, `guided()` filter (r=8, eps=2e-3) against the grey frame, contrast `clip((m-0.5)*1.6+0.5)`, temporal `0.65 m + 0.35 prev` | No separate cutout file: "behind" is just alpha times inverse mask. `camera()` warps img AND mask together (capped 2x). |
| Dryxio (Remotion) | `<Cam/>` (per-frame JPG when cut, else OffthreadVideo) > back items > `<Fg/>` (per-frame WebP cutout) > front items | BiRefNet-portrait at 1024 px on GPU, rembg u2net_human_seg fallback; 15 fps cutout, frame index `floor(f*15/30)` | Face from the alpha: head width = mask run at `top + 0.07 H`, cy = top + 0.62 head_w. |
| Ours (rival-reels) | plate > behind overlays > cutout (`OffthreadVideo transparent`, only mounted when a behind overlay exists) > front overlays | `matte.py`: RVM mobilenetv3 ONNX on CPU, downsample 0.25, alpha gaussian 1.2 px, VP9 `yuva420p` crf 24 | Same shape as all four. Missing pieces the others have: an inverse "plate with a hole" for vertigo, a dilated alpha for stickers and boils, and head-top measurement from the alpha (tenfoldmarc `headpos.py`, Dryxio `face_box`). |

Two numbers worth adopting from HyperFrames' captions.md: a word behind the head reads best 30 to 55 percent covered (under 15 floats, over 65 is eaten), and heads move (one clip went y=224 to y=96 in 8 s), so measure the matte per caption window instead of once.

---

## 3. Effects

Format per effect: what the code does (layer order, transforms, easing, durations), what it needs, then a port sketch in our conventions (`useCurrentFrame`, `prog`/`pop`/`backOut` from `anim.ts`, `C`/`F` from `theme.ts`, `mono` from `Menu.tsx`, `tailFade`, overlays flagged `behind: true`) or a filter graph for a build_reel3 slot.

### 3.1 Orbit (two copies per tile, alpha-swapped around an ellipse)

Three independent implementations, same mechanism.

**tenfoldmarc `orbit()` (build.py 172 to 207), the reference values.** Six reel tiles 190x338. Ellipse centre (640, 1110), rx 460, ry 150, one revolution every 5.2 s, keyframes precomputed every 0.1 s, `ease:'none'` between them. Angle `th = 2π (t - t_in)/5.2 + i 2π/n + 0.35`. Position `x = cx + rx cos th`, `y = cy + ry sin th`. Scale `0.6 + 0.4 (sin th + 1)/2` (front = bottom of the ellipse = bigger). Each tile exists twice in the DOM: `#b{i}` with class `.orb.b` (z3, `filter: brightness(.75)`, below the cutout) and `#f{i}` `.orb.f` (z6, above). Visibility is `autoAlpha` 1/0 swapped at the exact keyframe where `sin th` changes sign, so the swap happens at the left and right extremes where the tile is at mid depth and the two copies are at the same scale, so no pop. Each tile also has an inner `.pop` div: `scale 0 to 1, .45 s, back.out(1.8)`, staggered `i * .07 s`; exit `scale 0, .2 s, power2.in` staggered `i * .01`. Creator-card variant 260x462 with white border, tilt -7 or +6 deg, @handle pill.

**Vibha `fx_orbit` (fx.py 280 to 294).** `K` tiles (default 6), width `0.2 W`. `rx = 0.38 W * intro` where `intro = ease_out(lt/0.4)` (the ring opens from the head outward), `ry = max(1.5 face_w, 0.1 H)`, centre `(fx, fy + 0.9 face_w)` (ring around the neck, not the chin). `th = i 2π/K + lt * 1.9` rad/s (about 3.3 s per rev). Draw order sorted by `sin th` so overlapping tiles stack correctly. Scale `(0.78 + 0.24 (depth+1)/2) * (0.5 + 0.5 intro)`, rotation `-6 cos th` deg (tiles lean into the turn), `behind = depth < 0`, `guard = depth >= 0` (front tiles still never cover the face). Exit fade over the last 0.25 s.

**Dryxio `Orbit` (hero.tsx 144 to 172).** Two rings interleaved (`ring = i % 2`), ten tiles. Outer ring radius (470, 520) at `f * 0.04` rad/frame, inner (420, 450) at `-0.045` and offset 100 px lower, so the two rings counter-rotate. Tiles 190x336 with 5 px white border, radius 18, `rotate(((i%3)-1)*4deg)`. Back tiles `brightness(0.8)`. Scale `0.82 + 0.25 depth`. Rendering is one list filtered twice: `depth < 0` before `<Fg/>`, `depth >= 0` after it.

**HyperFrames catalog `three-orbiting-cards`.** Nine boxes on `x = cos a * 2.15, y = sin a * 2.15 * 0.55, z = sin a * 0.7`, group rotation driven by a `{progress}` object tweened by a paused GSAP timeline (`onUpdate: render`). Useful only as proof that three.js in a seekable timeline is the HyperFrames idiom; not needed for a reel orbit.

**Needs:** cutout WebM, 6 to 10 tile images or muted tile videos (our reels, partner logos, build photos), face centre from `facetrack.py` for the ring height.

**Port (Remotion, rival-reels).** One component, registered as `orbit`, listed TWICE in the EDL at the same `at` with `behind: true, props: {side: "back"}` and `behind: false, props: {side: "front"}`. RivalReel already draws behind overlays under the cutout and front ones over it, so the alpha swap is just "render the tile only when its depth sign matches the side".

```tsx
export const Orbit: React.FC<{ tiles: string[]; dur: number; side: "back" | "front"; cx?: number; cy?: number; rx?: number; ry?: number; rev?: number; w?: number; dim?: number }> = ({
  tiles, dur, side, cx = 540, cy = 1110, rx = 460, ry = 150, rev = 5.2, w = 190, dim = 0.75,
}) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const t = frame / fps; const n = tiles.length; const h = Math.round(w * 16 / 9);
  const open = prog(frame, 0, 12, EASE_OUT);                       // Vibha: the ring opens from the head outward
  const items = tiles.map((src, i) => {
    const th = 2 * Math.PI * (t / rev) + i * 2 * Math.PI / n + 0.35;  // tenfoldmarc phase
    const s = Math.sin(th);
    return { src, i, x: cx + rx * open * Math.cos(th), y: cy + ry * s, sc: 0.6 + 0.4 * (s + 1) / 2, s, rot: -6 * Math.cos(th) };
  }).filter((it) => (side === "front" ? it.s > 0 : it.s <= 0)).sort((a, b) => a.s - b.s);
  return (
    <AbsoluteFill style={{ opacity: tailFade(frame, dur, 6) }}>
      {items.map((it) => {
        const p = prog(frame, Math.round(it.i * 0.07 * fps), Math.round(0.45 * fps), backOut(1.8));
        return (
          <div key={it.i} style={{ position: "absolute", left: it.x - w / 2, top: it.y - h / 2, width: w, height: h, borderRadius: 16, overflow: "hidden", border: `4px solid ${C.cream}`, boxShadow: cardShadow, transform: `scale(${it.sc * p}) rotate(${it.rot}deg)`, filter: side === "back" ? `brightness(${dim})` : undefined }}>
            {/\.(mp4|webm)$/i.test(it.src) ? <OffthreadVideo src={staticFile(it.src)} muted style={{ width: "100%", height: "100%", objectFit: "cover" }} /> : <Img src={staticFile(it.src)} style={{ width: "100%", height: "100%", objectFit: "cover" }} />}
          </div>
        );
      })}
    </AbsoluteFill>
  );
};
```

Keep the ring inside the safe zone (tenfoldmarc: nothing below y 1470, right 100 px column clear from y 1155). With `cy 1110, ry 150` the lowest tile bottom is about 1430 at full scale. If Jacob's head sits high, pass `cy` from the face track (`fy + 0.9 * face_w`, Vibha's number).

**build_reel3 version:** not worth it. Six tiles times two depth states times per-frame positions is a 12-input `overlay` chain with `enable` expressions; doable but brittle. Leave orbit to Remotion.

### 3.2 Doodle boil (edge from the alpha plus stepped jitter)

No repo has a finished boil; three of them agree on the recipe and Vibha's `scribble` has the drawn-on doodles.

**ONIKOSIOLA's build plan (reel-effects-17.md #14 and the "Wobble" primitive).** Outline = alpha dilated minus alpha, OR the stacked `drop-shadow` trick. Jitter = SVG `feTurbulence` + `feDisplacementMap`, animating `baseFrequency` or `seed` in 3 to 4 discrete steps per second with `ease:'steps(1)'`, "never smooth". Doodles = SVG strokes drawn on with `strokeDashoffset`, colour-stepped. The dossier frame read (DOSSIER 5.2) confirms the reel: white chalk outline tracking the hands exactly, position jittering every frame, coloured rings, stars and tally marks, about 1.3 s.

**ONIKOSIOLA `effects.md` #2 (render-verified dissolve)** gives the exact filter markup and the rule that matters: animate the filter PARAM (`attr:{scale}` on `feDisplacementMap`), one filter id per element, never share one filter across elements animated at different times.

**Vibha `fx_scribble` (fx.py 686 to 708), the doodle grammar.** Marker width `max(6, W/130)`. A hand-drawn ring around the head: 70 points on an ellipse `rx = face_w, ry = 1.3 face_w` with wobble `(1 + 0.04 sin 3a)` and `(1 + 0.04 cos 2a)`, drawn with `hand_path()` = `d.line(pts[:n], joint='curve')` where `n = len * ease_inout(lt/0.5)`. Then a bent arrow (quadratic bezier, bend -0.3) from a label point to the ring over 0.35 s, arrow head only once `k2 >= 0.99`, three plus-signs that pop with `ease_back` staggered 0.1 s, a Caveat-style label `me!` at `0.7 to 1.0` with `ease_back` scale 0.7 to 1, rotation 8 deg. Everything in one RGBA layer composited at full alpha, fade out over the last 0.2 s.

**Needs:** cutout WebM (the alpha is the outline source). No face track needed for the outline; doodles use the face box.

**Port (Remotion).** Two layers, both front. (a) `BoilOutline`: a second copy of the cutout drawn white, dilated by four chained `drop-shadow(±3px 0 0 cream)`, passed through an SVG displacement filter whose `seed` changes every 3 frames (10 fps), and placed UNDER the clean cutout in the sandwich. In our RivalReel that means a behind overlay (the clean cutout then covers the interior, leaving only the dilated rim). (b) `Doodles`: SVG paths with `pathLength=1`, `strokeDasharray="1 1"`, `strokeDashoffset = 1 - prog(...)`.

```tsx
// behind: true. The clean cutout drawn by RivalReel covers the middle; only the dilated, displaced rim shows.
export const BoilOutline: React.FC<{ cutout: string; atF?: number; dur: number; color?: string; px?: number; fpsBoil?: number }> = ({ cutout, atF = 0, dur, color = C.cream, px = 4, fpsBoil = 10 }) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const seed = Math.floor(frame / Math.max(1, Math.round(fps / fpsBoil)));         // stepped, never smooth
  const ds = [`${px}px 0`, `-${px}px 0`, `0 ${px}px`, `0 -${px}px`].map((o) => `drop-shadow(${o} 0 ${color})`).join(" ");
  return (
    <AbsoluteFill style={{ opacity: tailFade(frame, dur, 4) }}>
      <svg width={0} height={0} style={{ position: "absolute" }}>
        <filter id={`boil${seed}`} x="-5%" y="-5%" width="110%" height="110%">
          <feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves={2} seed={seed} result="n" />
          <feDisplacementMap in="SourceGraphic" in2="n" scale={6} xChannelSelector="R" yChannelSelector="G" />
        </filter>
      </svg>
      <div style={{ position: "absolute", inset: 0, filter: `url(#boil${seed})` }}>
        <OffthreadVideo src={staticFile(cutout)} startFrom={atF} muted transparent style={{ width: "100%", height: "100%", objectFit: "cover", filter: `brightness(0) invert(1) ${ds}` }} />
      </div>
    </AbsoluteFill>
  );
};
```

`brightness(0) invert(1)` turns the cutout into a white silhouette (cream needs a `sepia()`/`saturate()` tail or just accept white; the dossier says his outline is chalky white). The drop-shadow stack runs on the silhouette, so the rim is `px` wide on each side. Changing the filter id with the seed forces Chrome to rebuild the filter (same-id attribute changes sometimes do not invalidate in headless captures; ONIKOSIOLA animates the attr instead, both work in Remotion).

**build_reel3 version (pure ffmpeg, from the cutout WebM).** Dilate by blur-and-threshold, subtract the original alpha, displace with a 10 fps noise field, overlay on the slot. The `displace` filter takes two map inputs; a single noise source split in two works.

```
ffmpeg -i slot.mp4 -c:v libvpx-vp9 -i cutout.webm -filter_complex "
[1:v]alphaextract,format=gray,split=2[a0][a1];
[a0]boxblur=6:1,geq=lum='if(gt(lum(X,Y),12),255,0)'[dil];
[a1]geq=lum='if(gt(lum(X,Y),128),255,0)'[core];
[dil][core]blend=all_mode=difference,format=gray[rim];
nullsrc=s=1080x1920:r=10,geq=lum='128+40*(random(1)-0.5)',fps=30,format=gray,split=2[nx][ny];
[rim][nx][ny]displace=edge=wrap[rimj];
color=c=0xefe9dc:s=1080x1920:r=30,format=rgba[ink];
[ink][rimj]alphamerge[rimrgba];
[0:v][rimrgba]overlay=0:0:format=auto:enable='between(t,T0,T1)'[v]" -map "[v]" out.mp4
```

`nullsrc ... r=10` then `fps=30` is what makes the jitter stepped (each noise frame holds for three output frames). `boxblur=6` then threshold at 12 is a cheap 6 px dilation. The colour source is cream `#efe9dc`. Slot option name suggestion: `"boil": {"from": T0, "to": T1, "px": 6}`; it needs the slot's cutout path, so it only applies to talking-head slots that already have one.

### 3.3 Paper cut sticker edge

**ONIKOSIOLA (verified, hyperframes 0.8.162).** Sticker border = chained `drop-shadow(3px 0 0 #fff) drop-shadow(-3px 0 0 #fff) drop-shadow(0 3px 0 #fff) drop-shadow(0 -3px 0 #fff)` on the subject wrapper (their plan says four stacked `drop-shadow(0 0 0 #fff)`; the verified skeleton uses the ±3px offsets). Torn edge: a displacement filter must NOT sit on the subject wrapper ("would warp the face; needs a separate outline layer"). Paper = `feTurbulence` texture; scribbles = SVG paths drawn with dashoffset, wobbled at 8 fps; ransom letters = spans with mixed fonts and backgrounds, ±8 deg rotations, `scale 1.8 to 1` stamp ease. Known leak: the matte lets bits of background through at the sticker edge; close the alpha morphologically first.

**Vibha `fx_bill` (fx.py 339 to 369), the torn paper bottom.** A receipt crops to length `L = height * ease_inout(lt / (0.75 d))` and gets a sawtooth polygon of zig `z = 14 px`, period `2z`, pasted below the crop, then `shadowed(blur 10, dy 6, alpha 90)`. That zig-zag plus shadow is the whole "torn paper" read at reel size.

**Vibha `fx_tape_label` (2075 to 2086).** Tape = rectangle `TAPE` colour with a 4 px dark offset copy behind it (`o = max(4, S/9)`), Caveat-style text, pop `ease_back` 0.25 s, scale 0.85 to 1.

**viashaan Paper Desk `Tape` (PaperDesk.tsx).** Tape `170x52`, `rgba(230,217,180,0.82)`, `clipPath: polygon(2% 8%, 98% 0, 100% 92%, 0 100%)`, slaps on over 6 frames `1.35 to 1` with `Easing.in(quad)`, squash `scaleY 0.96` for frames 6 to 9. Grain = `feTurbulence baseFrequency 0.9, numOctaves 2`, `feColorMatrix saturate 0`, `mixBlendMode: multiply`, opacity 0.16 on paper, 0.18 on the mat.

**Needs:** cutout WebM. Optional: the inverse plate (so the paper background replaces the room entirely; otherwise dim the plate and the sticker floats over the shop, which also reads fine).

**Port (Remotion, front layer, uses our cutout).**

```tsx
export const Sticker: React.FC<{ cutout: string; atF?: number; dur: number; rim?: number; torn?: boolean; paper?: string; words?: string[] }> = ({ cutout, atF = 0, dur, rim = 6, torn = true, paper = C.cream, words = [] }) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const p = prog(frame, 0, 8, backOut(1.6));
  const ds = [`${rim}px 0`, `-${rim}px 0`, `0 ${rim}px`, `0 -${rim}px`, `${rim * .7}px ${rim * .7}px`, `-${rim * .7}px -${rim * .7}px`].map((o) => `drop-shadow(${o} 0 #fff)`).join(" ");
  const seed = Math.floor(frame / 4);                                                  // 7.5 fps wobble on the rim only
  return (
    <AbsoluteFill style={{ opacity: tailFade(frame, dur, 6) }}>
      <svg width={0} height={0} style={{ position: "absolute" }}>
        <filter id="grid"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves={2} seed={4} /><feColorMatrix type="saturate" values="0" /></filter>
        <filter id={`torn${seed}`}><feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves={2} seed={seed} result="n" /><feDisplacementMap in="SourceGraphic" in2="n" scale={torn ? 7 : 0} /></filter>
      </svg>
      <AbsoluteFill style={{ background: paper, backgroundImage: `linear-gradient(${C.ink}22 1px, transparent 1px), linear-gradient(90deg, ${C.ink}22 1px, transparent 1px)`, backgroundSize: "54px 54px" }} />
      <svg width={1080} height={1920} style={{ position: "absolute", inset: 0, opacity: 0.16, mixBlendMode: "multiply" }}><rect width="100%" height="100%" filter="url(#grid)" /></svg>
      {/* white rim: a silhouette copy, dilated and wobbled, under the clean cutout */}
      <div style={{ position: "absolute", inset: 0, filter: `url(#torn${seed})`, transform: `scale(${0.9 + 0.1 * p})`, transformOrigin: "50% 70%" }}>
        <OffthreadVideo src={staticFile(cutout)} startFrom={atF} muted transparent style={{ width: "100%", height: "100%", objectFit: "cover", filter: `brightness(0) invert(1) ${ds}` }} />
      </div>
      <div style={{ position: "absolute", inset: 0, transform: `scale(${0.9 + 0.1 * p})`, transformOrigin: "50% 70%", filter: "drop-shadow(0 18px 24px rgba(0,0,0,0.35))" }}>
        <OffthreadVideo src={staticFile(cutout)} startFrom={atF} muted transparent style={{ width: "100%", height: "100%", objectFit: "cover" }} />
      </div>
      {words.map((w, i) => { const s = prog(frame, 10 + i * 4, 7, power4Out); return <span key={i} style={{ position: "absolute", left: 90 + i * 120, top: 380, fontFamily: i % 2 ? F.heavy : F.serif, fontSize: 96, color: i % 3 ? C.ink : C.cream, background: i % 3 ? C.yellow : C.oxblood, padding: "0 14px", transform: `rotate(${(i % 2 ? 1 : -1) * 8}deg) scale(${1.8 - 0.8 * s})`, opacity: s }}>{w}</span>; })}
    </AbsoluteFill>
  );
};
```

Two layers on purpose: the displaced one is the silhouette (face warping does not matter there), the clean cutout sits on top undistorted. That is ONIKOSIOLA's "separate outline layer" fix. Keep the rim at 6 to 8 px at 1080 wide; their verified build used 3 px per direction and read thin.

**build_reel3 version:** same `[dil]` chain as 3.2 without the subtract and without the displace, alphamerged with a white colour source and overlaid under a re-overlay of the cutout: `[slot][rimrgba]overlay[tmp];[tmp][1:v]overlay`. Cheap, no jitter.

### 3.4 Zoom-through cut with the radial blur done right

**What every repo does.** ONIKOSIOLA #9: A `scale 1 to 3.2` + blur ramp, hard cut at the peak, B `scale 1.5 to 1`, blur 18 to 0; "true radial blur: pre-render the transition with ffmpeg (zoompan + gblur/rgbashift) or stack 4 scaled copies at 25% opacity." Dryxio `ZoomPunch`: `period 40` frames, `punch = exp(-local/5)`, scale `(zoomed ? 1.35 : 1) + 0.18 punch`, `contrast(1 + 0.15 punch)`, white flash `opacity punch * 0.25`, word `scale(1 + 0.35 punch)`, transform-origin on the face. Vibha has no zoom-through; `fx_slow_push` is the slow version (`face_cam` to 1.6 with `ease_inout`, background gaussian `sigma = 0.006 W * p` outside the matte, vignette `0.25 p`). HyperFrames: `data-motion-blur="on"` (shutter 240 deg, at least 32 samples); only the `capture` tier streaks a zoom outward, the default filter tier "only softens turns and zooms".

**Our current `ZoomThrough`** uses `filter: blur(24 tA)` which is a gaussian, so the peak frame is mush, not streaks. The fix is a real shutter: accumulate N copies of the plate at N sub-frame zoom levels. We already have `@remotion/motion-blur` installed and unused.

**Port (Remotion, replace the inner of ZoomThrough).**

```tsx
import { CameraMotionBlur } from "@remotion/motion-blur";
// ... inside ZoomThrough, instead of the blurred OffthreadVideo pair:
<CameraMotionBlur shutterAngle={270} samples={12}>
  <AbsoluteFill style={{ background: "#000" }}>
    {inA
      ? <OffthreadVideo src={staticFile(plate)} startFrom={atF} muted={muted} style={{ width: "100%", height: "100%", objectFit: "cover", transform: `scale(${sA})`, transformOrigin: `${ox}% ${oy}%` }} />
      : <OffthreadVideo src={staticFile(next ?? plate)} startFrom={(nextAtF ?? atF) + (next ? 0 : cutAt)} muted={muted} style={{ width: "100%", height: "100%", objectFit: "cover", transform: `scale(${sB})`, transformOrigin: `${ox}% ${oy}%` }} />}
  </AbsoluteFill>
</CameraMotionBlur>
<AbsoluteFill style={{ background: "#fff", opacity: fl }} />
```

`CameraMotionBlur` re-renders the children at `samples` sub-frame offsets and averages them, so a fast `scale` becomes a radial streak around `transformOrigin` for free. Keep `peak 2.6` over `cutAt 4` frames with `power4Out` on A and `expoOut` on B (already our values; they match ONIKOSIOLA's 3.2 / 1.5 within taste). Put the origin on the detail you are landing on (turbo, gauge) rather than frame centre: that is the "B framed as a detail of A" rule from the dossier. Cost: 12x the frames of a 10-frame window, negligible.

**build_reel3 version (new slot key `zoomthrough`).** Same idea without a compositor: duplicate frames to 120 fps BEFORE the eval=frame zoom so the zoom expression is evaluated at four sub-positions per output frame, then `tmix` averages them. This is a real zoom streak, not gaussian, and it reuses `zoom_filters()`.

```python
def zoomthrough_filters(peak=2.6, dur=0.14, anchor=(0.5, 0.45), sub=4):
    # A-side: out-zoom into the cut. Called on the LAST `dur` seconds of slot A (and mirrored, peak->1.45->1, on the first of B).
    u = f"clip(t/{dur:.3f},0,1)"
    zf = f"(1+({peak}-1)*(1-(1-{u})^4))"                       # power4.out, same as the Remotion side
    return [f"fps={FPS*sub}",                                    # 4 sub-frames per output frame, synthetic (no minterpolate needed)
            f"scale=w='{W}*{zf}':h='{H}*{zf}':eval=frame:flags=bicubic",
            f"crop={W}:{H}:x='(iw-ow)*{anchor[0]}':y='(ih-oh)*{anchor[1]}'",
            f"tmix=frames={sub}", f"fps={FPS}", "setsar=1"]
```

Apply it as a per-slot tail/head segment the way `prev_whip`/`next_whip` already split blur-in and blur-out, and keep the existing `flash` drawbox for the white hit at the cut. Add a whoosh from `sfx/` on the cut frame (the dossier notes every zoom-through in his reels has one).

### 3.5 Digital zoom HUD (viewfinder overlay on the punch-in)

**Vibha `fx_noise`** is a tile pile, not a HUD; the HUD lives in `red_timeline` (fx.py 970 to 1003): REC dot `0.36 x text height`, blink `int(lt * 2.5) % 2` (1.25 Hz, dim to 0.35 not off), timecode `REC 00:{21 + int(lt*3)}` in mono at `0.032 W`, slide-in `(1 - ease_out(lt/0.35)) * 0.08 W` from the left, all drawn with `guard=True` so they never cross the face. **Dryxio `Noise`** (grid.tsx 259 to 288): mono 46 px `● REC` top-left at (70, 110), dot visible `f % 30 < 18`, timecode `MM:SS:FF` top-right, orange date stamp bottom-right, camera shake `translate((rnd(f)-0.5)*4px)`, grain = `feTurbulence baseFrequency 0.85, seed f % 50`, overlay blend 0.28, scanlines `repeating-linear-gradient(rgba(0,0,0,.12) 0 2px, transparent 2px 5px)`, vignette `radial-gradient(75% 60%, transparent 55%, rgba(0,0,0,.75))`. **Vibha `fx_lean_in`**: the punch itself, `face_cam(1 + (z-1) * ease_out(lt/0.18), head_at 0.42)`, default z 1.45, capped at 2.0 "so it stays sharp". **Vibha `fx_over_the_shoulder_zoom`**: the keyframe table for a two-corner push, `(0, 1.0), (0.30, 1.04), (0.46, z), (0.66, z+0.04), (0.76, 1.05), (0.87, z), (1.0, z+0.04)` with `ease_inout` between, which is the "creep after the hit" that makes a digital zoom feel like a lens: land at z, then drift +0.04 over the hold.

**Our `HudZoom`** already has brackets, REC dot, timecode and the `1.00x to 1.60x` readout. What it lacks is the two-stage zoom shape from the dossier (slow push to about 1.18 across the caption words, then a hard punch to about 1.3 on the emphasis word, then creep) and the readout should be driven by the SAME curve as the plate's zoom so the number matches the picture.

**Port (Remotion).** Add a `curve` prop shared between the plate zoom and the readout:

```tsx
/** two-stage digital zoom: slow push to `mid` by `midAt`, hard punch to `to` in `punch` frames at `hitAt`, then +creep over the hold. */
export const digitalZoom = (frame: number, { from = 1, mid = 1.18, to = 1.3, midAt = 30, hitAt = 30, punch = 4, creep = 0.04, dur = 60 }) => {
  const a = from + (mid - from) * prog(frame, 0, midAt, EASE_IN_OUT);
  const b = (to - mid) * prog(frame, hitAt, punch, power4Out);
  const c = creep * prog(frame, hitAt + punch, Math.max(1, dur - hitAt - punch), (t) => t);
  return a + b + c;
};
// HudZoom: const z = digitalZoom(frame, { dur, ...zoomProps }); readout {z.toFixed(2)}x
// plate: style={{ transform: `scale(${z})`, transformOrigin: `${fx}% ${fy}%` }}  (fx, fy from facetrack.py, Vibha keeps the head at 42% of frame height)
```

Shoot 4K for anything above 1.3x (Vibha caps at 2.0 at 1080 source; Dryxio renders 4K by default for the same reason).

**build_reel3 version (new slot key `hud`).** Our `zoom` slot already does the plate; the HUD is `drawbox` corners + `drawtext` with expressions. All of this is one `-vf` append after `zoom_filters()`:

```python
def hud_filters(dur, z0=1.0, z1=1.6, color="0xefe9dc", font="fonts/JetBrainsMono-Medium.ttf"):
    u = f"clip(t/{dur:.3f},0,1)"; z = f"({z0}+({z1}-{z0})*(1-(1-{u})^3))"
    br = lambda x, y, w, h: f"drawbox=x={x}:y={y}:w={w}:h={h}:c={color}@0.9:t=4"
    return [br(90, 320, 70, 4), br(90, 320, 4, 70), br(920, 320, 70, 4), br(986, 320, 4, 70),          # top brackets
            br(90, 1360, 70, 4), br(90, 1294, 4, 70), br(920, 1360, 70, 4), br(986, 1294, 4, 70),      # bottom brackets
            f"drawbox=x=110:y=342:w=18:h=18:c=0xe0392b@1:t=fill:enable='lt(mod(t,1),0.6)'",            # REC dot, 1 Hz, 60% duty
            f"drawtext=fontfile={font}:text='REC':fontcolor={color}:fontsize=28:x=140:y=336",
            f"drawtext=fontfile={font}:text='%{{pts\\:hms}}':fontcolor={color}:fontsize=28:x=w-150-tw:y=336",
            f"drawtext=fontfile={font}:text='%{{eif\\:{z}*100\\:d}}':fontcolor={color}:fontsize=30:x=(w-tw)/2:y=1400",  # readout as 100x integer (ffmpeg drawtext has no float format)
            ]
```

`drawtext` cannot print `1.51x` directly; the trick is two drawtexts (integer part and `%{eif:mod(Z*100,100):d:2}` for the decimals) or pre-render the readout from Remotion as a transparent WebM. Font paths inside a filter need `C\:/...` escaping on Windows (tenfoldmarc gotcha); keep the font path relative to `cwd=tmp` the way `write_ass` already does.

### 3.6 Glass type (and liquid glass panels)

**ONIKOSIOLA #17 (unverified):** 8 to 12 stacked copies offset 2 px for extrusion, white-to-transparent gradient via `background-clip:text`, 1 px white `-webkit-text-stroke`, a blurred duplicate underneath as caustic; "test backdrop-filter in headless render first"; fallback is a three.js text render. Their own first test says it "reads as frosted white and is subtle on bright skies."

**Dryxio `Glass` (kit.tsx 158 to 183), the cheap panel:** `background rgba(255,248,240,0.26)` (or `rgba(255,255,255,0.92)` light), `backdropFilter: blur(18px)`, `border 2px solid rgba(255,255,255,0.45)`, `boxShadow 0 18px 40px rgba(0,0,0,0.25)`, radius 34, enters `scale(0.8 + 0.2 k)` with `opacity min(1, 1.5 k)` where k is a spring. Renders fine in Remotion (Chrome); it is HyperFrames' screenshot path that goes black with many backdrop-filters.

**Vibha `glass()` / `liquid_glass()` (fx.py 716 to 747, 1874 to 1900), the expensive one, worth stealing the numbers:** rounded-rect signed distance `sdf`, inward distance `d = max(-sdf, 0) / u` (u = W/2160), refraction strength along the outward normal `k = (70 e^(-d/14) + 34 e^(-d/70) + 10 e^(-d/260)) u`, sampled from a lightly blurred copy of the room (`sigma max(3, 0.3 blur)`) with per-channel factors `1.10 / 1.00 / 0.90` (red-blue fringe), tint `0.86 base + 0.06 (1 - 0.3 y/h) - 0.05`, specular rim `e^(-d/5) * clip(0.55 - 0.45 (0.6 nx + 0.8 ny))` lit from top-left plus `0.10 e^(-d/30)` inner glow, alpha `clip(0.5 - sdf)`. Credits liquid-glass-js (dashersw, MIT) and React Bits GlassSurface.

**ONIKOSIOLA `effects.md` #4 shimmer text (verified):** `background: linear-gradient(100deg, gold, cream 20%, teal 40%, gold 60%, cream 80%, gold)`, `background-size 300% 100%`, `background-clip:text`, tween `backgroundPosition 0% to 200%` over 1.8 s linear.

**Is it cheap?** The DOM version is. Full refraction is not (it is a per-pixel remap; in Remotion you would need a WebGL shader or an SVG `feDisplacementMap` driven by a radial gradient map, which only approximates the rim bend).

**Port (Remotion, behind: true so the head overlaps the word; one element only).**

```tsx
export const GlassWord: React.FC<{ text: string; dur: number; y?: number; size?: number; depth?: number }> = ({ text, dur, y = 420, size = 300, depth = 10 }) => {
  const frame = useCurrentFrame();
  const p = prog(frame, 0, 12, expoOut); const sheen = prog(frame, 8, 40, (t) => t);
  const base: React.CSSProperties = { position: "absolute", left: 0, right: 0, top: y, textAlign: "center", fontFamily: F.block, fontSize: size, lineHeight: 0.9, letterSpacing: 4, whiteSpace: "nowrap" };
  return (
    <AbsoluteFill style={{ opacity: p * tailFade(frame, dur, 6), transform: `scale(${1.08 - 0.08 * p})` }}>
      <div style={{ ...base, color: "rgba(255,255,255,0.25)", filter: "blur(22px)" }}>{text}</div>                         {/* caustic */}
      {Array.from({ length: depth }).map((_, i) => (                                                                    /* extrusion */
        <div key={i} style={{ ...base, transform: `translate(${(depth - i) * 1.5}px, ${(depth - i) * 1.5}px)`, color: `rgba(255,255,255,${0.04 + 0.02 * i})`, WebkitTextStroke: "1px rgba(255,255,255,0.25)" }}>{text}</div>
      ))}
      <div style={{ ...base, color: "transparent", WebkitTextStroke: "1.5px rgba(255,255,255,0.85)", backgroundImage: `linear-gradient(100deg, rgba(255,255,255,.75), rgba(255,255,255,.15) 30%, ${C.tan}aa 50%, rgba(255,255,255,.15) 70%, rgba(255,255,255,.75))`, backgroundSize: "300% 100%", backgroundPosition: `${sheen * 200}% 50%`, WebkitBackgroundClip: "text", backgroundClip: "text", backdropFilter: "blur(14px)" }}>{text}</div>
    </AbsoluteFill>
  );
};
```

Keep it to ONE `backdropFilter` element. On Jacob's footage (dark shop, cream type) this will read better than on tenfoldmarc's bright skies; still test a frame against the HLG-fixed plate before committing a reel to it.

### 3.7 Map route (viashaan)

**Mechanism (MapRoute.tsx, 18 KB).** `@remotion/three` `ThreeCanvas` 1080x1920, FOV 36, PCF soft shadows, instanced boxes for an invented city (seeded `rng(7)`, 18x18 blocks of 12 units, street width 2.4, a river row, five parks with sphere trees, one gold main street). Camera: quadratic bezier from `START pos (-12, 4.2, 40)` through `(-30, 46, 78)` to `END` at elevation 55 deg, distance 128, over frames 0 to 112 with `Easing.bezier(0.42, 0, 0.12, 1)`; the look target lags ("lift first, pan after"). Route: six waypoints along the grid; draw progress `0.07 at f<6`, then `6 to 96` with `Easing.bezier(0.33, 0.05, 0.2, 1)`; the ribbon is rebuilt per frame as triangles with half-width `worldPerPx(cam, p) * px / 2` so it is a constant 34 px casing + 22 px blue line on screen (a maps-app trait), round joins as 20-segment discs, drawn with `depthTest false` on `renderOrder 10/11`. 2D overlay: labels pop at frames 30/40/50 with spring `{damping 10, stiffness 240}` placed by `project(cam, p)`; origin dot pulses `(f % 36)/36`; pin at frame 94 falls `-260 to 0` over 8 frames `Easing.in(quad)`, then squash `1 - 0.16 sin(π min(1,(f-102)/6))` with spring `{damping 9, stiffness 260, mass 0.6}`, shadow scales with height; place label at +13 spring `{10, 220}`; trip card at frame 112 spring `{damping 11, stiffness 140, mass 0.9}` from `translateY 520`, odometer counts `minutes+2 to minutes` over 18 frames cubic-out with the next digit sliding in from above. Palette: pale map `#ECEAE4`, route `#1A73E8`, pin `#EA4335`. Card rules: no real map data, no orbiting camera, no fades.

**Needs:** `three`, `@react-three/fiber`, `@remotion/three` (not in rival-reels today), a GPU or `--gl=angle` on Windows, a few minutes of render on CPU. No footage.

**Port note.** For Jacob the two uses are "Cheyenne to Driven Diesel (Phoenix)" and "Cheyenne to SEMA (Las Vegas)". The 3D city is the expensive part and adds little at reel scale; the parts that sell the beat are the constant-width route draw, the pin drop with squash, and the card with the odometer. A 2.5D version in CSS gets all three without three.js:

```tsx
export const MapRoute2D: React.FC<{ route: [number, number][]; place: string; minutes: number; distance: string; dur: number }> = ({ route, place, minutes, distance, dur }) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const cam = prog(frame, 0, 112, (t) => t * t * (3 - 2 * t));                                                // lift then settle
  const draw = frame < 6 ? 0.07 : interpolate(frame, [6, 96], [0.07, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.bezier(0.33, 0.05, 0.2, 1) });
  const d = route.map((p, i) => `${i ? "L" : "M"}${p[0]},${p[1]}`).join(" ");
  const [ex, ey] = route[route.length - 1];
  const fall = interpolate(frame, [94, 102], [-260, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.in(Easing.quad) });
  const sq = frame >= 102 ? 1 - 0.16 * Math.sin(Math.min(1, (frame - 102) / 6) * Math.PI) : 1;
  const card = spring({ frame: frame - 112, fps, config: { damping: 11, stiffness: 140, mass: 0.9 } });
  const mins = interpolate(frame, [116, 134], [minutes + 2, minutes], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic) });
  return (
    <AbsoluteFill style={{ background: "#ECEAE4", perspective: 1800, opacity: tailFade(frame, dur, 6) }}>
      <div style={{ position: "absolute", inset: 0, transformOrigin: "50% 60%", transform: `rotateX(${55 - 20 * cam}deg) scale(${1.6 - 0.55 * cam}) translateY(${-200 + 260 * cam}px)` }}>
        <svg width={1080} height={1920}>
          {Array.from({ length: 19 }, (_, i) => <g key={i}><line x1={i * 60} x2={i * 60} y1={0} y2={1920} stroke="#FBFBFA" strokeWidth={10} /><line y1={i * 110} y2={i * 110} x1={0} x2={1080} stroke="#FBFBFA" strokeWidth={10} /></g>)}
          <path d={d} fill="none" stroke="#fff" strokeWidth={34} strokeLinecap="round" strokeLinejoin="round" pathLength={1} strokeDasharray="1 1" strokeDashoffset={1 - draw} />
          <path d={d} fill="none" stroke="#1A73E8" strokeWidth={22} strokeLinecap="round" strokeLinejoin="round" pathLength={1} strokeDasharray="1 1" strokeDashoffset={1 - draw} />
        </svg>
      </div>
      {frame >= 94 && <div style={{ position: "absolute", left: ex - 42, top: ey - 108 + fall, width: 84, height: 112, transformOrigin: "50% 100%", transform: `scale(${2 - sq}, ${sq})`, background: "#EA4335", borderRadius: "50% 50% 50% 50% / 60% 60% 40% 40%", border: "6px solid #fff" }} />}
      <div style={{ position: "absolute", left: 48, right: 48, top: 1176, transform: `translateY(${(1 - card) * 520}px)`, background: "#fff", borderRadius: 44, padding: "40px 48px", boxShadow: cardShadow, fontFamily: F.ui, color: C.ink }}>
        <div style={{ fontFamily: F.block, fontSize: 120, lineHeight: 1 }}>{Math.ceil(mins)} <span style={{ fontSize: 64 }}>min</span></div>
        <div style={{ fontSize: 34, color: "#6B737C", marginTop: 12 }}>{distance} · <span style={{ color: "#1F9D55" }}>Fastest route</span> · to {place}</div>
      </div>
    </AbsoluteFill>
  );
};
```

Pin drop lands at the projected end of the route (in 2.5D, project through the same CSS transform or just place the pin inside the transformed div). A 1,000-mile trip wants the invented-grid look anyway; a real basemap would need OSM tiles and attribution.

### 3.8 Exploded teardown (viashaan)

**Mechanism (Teardown.tsx).** `ThreeCanvas`, FOV 30, camera `az 28 to 38 deg` over 140 frames (`bezier(0.3,0,0.3,1)`), `el 30 to 26`, distance `26 to 47` and target lifting `(0, 0.6) to (2.9, 3.4)` over the first 40 frames (`bezier(0.4,0,0.2,1)`): pull back and slide the product left to clear the label column. Five layers (keycaps, switches, plate, PCB, case) with assembled y `a` and exploded y `e`; `layerY = a + (e - a) * spring({frame: f - 26 - k*10, damping 9, stiffness 150, mass 0.8})`, so lifts start at frame 26, one every 10 frames, top layer first, about 10 percent overshoot. Per layer: a leader line draws from the projected edge point to x=680 over 8 frames cubic-out starting `t0 + 6`; label rises out of an `overflow:hidden` mask at `t0 + 10` with spring `{11, 200}` (`translateY((1-s)*130%)`); label = orange two-digit mono number, Plex Sans 38 name, mono 21 spec. Title at `START + 5*STEP + 12 = 88`: orange bar `width 120 * cubicOut(8f)`, words stagger 3 frames spring `{12, 200}`, spec line +14. Background radial graphite `#2A2D33 to #0A0A0C`, shadow plane `shadowMaterial opacity 0.35`, two directional lights. Card "Never": no fades, no simultaneous lifts, no crossed leaders, no flat cut-outs.

**Needs:** three.js stack as 3.7, plus a model. A keyboard is boxes; a turbo or an injector is not.

**Port note.** The honest version for a diesel account is 2.5D from photographs: shoot the part disassembled on the bench from one fixed camera (compressor housing, compressor wheel, CHRA, turbine wheel, turbine housing), cut each piece out (our `matte.py` is a person model; use rembg `isnet-general-use` or hand-mask five stills once), stack them on one vertical axis and reuse the exact timing. The timing is the effect; the rendering is not.

```tsx
export type Layer = { img: string; name: string; spec: string; lift: number };   // lift = exploded offset in px, top layer largest
export const Teardown2D: React.FC<{ layers: Layer[]; title: string; dur: number; x?: number; y?: number }> = ({ layers, title, dur, x = 120, y = 700 }) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const START = 26, STEP = 10;
  const pull = prog(frame, 0, 40, EASE_IN_OUT);                                                          // camera pulls back, slides left
  const titleT = START + layers.length * STEP + 12; const bar = prog(frame, titleT, 8, EASE_OUT);
  return (
    <AbsoluteFill style={{ background: `radial-gradient(ellipse 70% 50% at 40% 45%, #2A2D33 0%, #16181c 60%, ${C.black} 100%)`, opacity: tailFade(frame, dur, 6) }}>
      <div style={{ position: "absolute", left: x - 120 * pull, top: y, width: 600, transform: `scale(${1.2 - 0.3 * pull}) perspective(1400px) rotateX(${18 - 4 * pull}deg)`, transformOrigin: "50% 50%" }}>
        {layers.map((l, k) => {
          const s = spring({ frame: frame - START - k * STEP, fps, config: { damping: 9, stiffness: 150, mass: 0.8 } });
          return <Img key={k} src={staticFile(l.img)} style={{ position: "absolute", left: 0, top: -l.lift * s, width: 600, filter: "drop-shadow(0 30px 24px rgba(0,0,0,0.55))" }} />;
        })}
      </div>
      <svg width={1080} height={1920} style={{ position: "absolute", inset: 0 }}>
        {layers.map((l, k) => { const t0 = START + k * STEP + 6; if (frame < t0) return null; const ln = prog(frame, t0, 8, EASE_OUT); const py = y + 300 - l.lift; return <g key={k}><line x1={x + 520} y1={py} x2={x + 520 + 140 * ln} y2={py} stroke="#6F747C" strokeWidth={2} /><circle cx={x + 520} cy={py} r={7} fill="#fff" /></g>; })}
      </svg>
      {layers.map((l, k) => { const t0 = START + k * STEP + 10; const s = spring({ frame: frame - t0, fps, config: { damping: 11, stiffness: 200 } }); const py = y + 300 - l.lift; return frame < t0 ? null : (
        <div key={k} style={{ position: "absolute", left: x + 680, top: py - 30, height: 100, overflow: "hidden" }}><div style={{ transform: `translateY(${(1 - s) * 130}%)`, display: "flex", gap: 14, alignItems: "baseline" }}><span style={{ fontFamily: mono, fontSize: 28, color: C.tan }}>{String(k + 1).padStart(2, "0")}</span><div><div style={{ fontFamily: F.uiSemi, fontSize: 38, color: C.cream }}>{l.name}</div><div style={{ fontFamily: mono, fontSize: 21, color: "#A3A8B0", letterSpacing: 1.5 }}>{l.spec}</div></div></div></div>); })}
      <div style={{ position: "absolute", left: 80, top: 1390 }}><div style={{ width: 120 * bar, height: 8, background: C.tan, marginBottom: 26 }} />
        <div style={{ display: "flex", gap: 20, overflow: "hidden" }}>{title.split(" ").map((w, i) => <span key={i} style={{ fontFamily: F.block, fontSize: 92, color: C.cream, display: "inline-block", transform: `translateY(${(1 - spring({ frame: frame - titleT - 4 - i * 3, fps, config: { damping: 12, stiffness: 200 } })) * 110}%)` }}>{w}</span>)}</div></div>
    </AbsoluteFill>
  );
};
```

Each lift should get a click SFX (the card says so, and our `sfx_place.py` can take the frame list `START + k*STEP`).

### 3.9 Split flap / flip counter

**Vibha `fx_countdown` ("Countdown Flip", fx.py 608 to 629).** Tile `0.3 W x 0.38 W`, dark `(30,30,34)`, digit at `0.62` tile height, a 4 px black seam line across the middle. Per step (0.3 s): top half shows the NEW digit from frame one; bottom half shows the OLD digit until the flip completes; for `f < 0.5` the OLD top half is squashed to height `th/2 * (1 - 2f)` hanging from the seam; for `0.5 <= f < 1` the NEW bottom half grows from the seam to `th/2 * (2f - 1)`. Pop-in `0.7 + 0.3 ease_back(lt/0.3)`, placed above the head `max(th/2 + 0.05 H, fy - 2.3 fw)`, `behind=True`, shadow `blur 16, dy 10, alpha 120`. **Dryxio `Countdown`** is a ring countdown, not a flap (dasharray `1885 * (1 - local)` on r=300, digit `scale 1.25 to 1` spring `{10, 260}` per second). **Our `anim.ts`** already has `steps(n)` for exactly this.

**Port (Remotion, front or behind).** Use real `rotateX` with perspective instead of the squash; it is the same cost and reads as a mechanical flap.

```tsx
export const FlipDigit: React.FC<{ values: string[]; dur: number; every?: number; flip?: number; x?: number; y?: number; w?: number }> = ({ values, dur, every = 9, flip = 9, x = 390, y = 520, w = 300 }) => {
  const frame = useCurrentFrame(); const h = Math.round(w * 1.27);
  const i = Math.min(values.length - 1, Math.floor(frame / every)); const f = prog(frame, i * every, flip, EASE_IN_OUT);
  const cur = values[i], prev = values[Math.max(0, i - 1)];
  const half = (v: string, top: boolean) => (
    <div style={{ position: "absolute", left: 0, width: w, height: h / 2, top: top ? 0 : h / 2, overflow: "hidden", background: "#1e1e22", borderRadius: top ? "16px 16px 0 0" : "0 0 16px 16px" }}>
      <div style={{ position: "absolute", left: 0, width: w, height: h, top: top ? 0 : -h / 2, display: "flex", alignItems: "center", justifyContent: "center", fontFamily: F.block, fontSize: h * 0.62, color: C.cream, fontVariantNumeric: "tabular-nums" }}>{v}</div>
    </div>
  );
  const topFlap = f < 0.5 ? { v: prev, rot: -90 * (f / 0.5), top: true } : { v: cur, rot: 90 * (1 - (f - 0.5) / 0.5), top: false };
  return (
    <AbsoluteFill style={{ opacity: tailFade(frame, dur, 6) }}>
      <div style={{ position: "absolute", left: x, top: y, width: w, height: h, perspective: 900, filter: "drop-shadow(0 10px 16px rgba(0,0,0,0.5))" }}>
        {half(cur, true)}{half(i > 0 && f < 1 ? prev : cur, false)}
        {i > 0 && f < 1 && <div style={{ position: "absolute", left: 0, top: 0, width: w, height: h, transformOrigin: "50% 50%", transform: `rotateX(${topFlap.rot}deg)`, backfaceVisibility: "hidden" }}>{half(topFlap.v, topFlap.top)}</div>}
        <div style={{ position: "absolute", left: 0, top: h / 2 - 2, width: w, height: 4, background: "#000" }} />
      </div>
    </AbsoluteFill>
  );
};
```

Uses: horsepower `450 to 600`, year `2026 to 2027`, SEMA countdown. One flap per beat, not a continuous roll (the dossier's split-flap read is one flip per word).

### 3.10 Ink wash (viashaan)

**Mechanism (InkWash.tsx).** A 1080x1920 `<canvas>` redrawn each frame in `useLayoutEffect([f])` (Remotion renders this deterministically because nothing depends on wall-clock time). Three mountain ranges, each a ridge `base - amp * fbm(x * freq + seed)^1.6 * 1.6 + 40` with 1D value-noise `fbm = 0.6 n(x) + 0.28 n(2.3x+7) + 0.12 n(5.1x+3)`. The wash "paints itself" left to right: a ragged front `front = -80 + p (W + 200)`, per 3 px column skip if `x > front + (fbm(...) - 0.5) * 120`; a wet edge `wet = clip(1 - (front - x)/70) * 0.5 * (1 - 0.6p)` brightens alpha near the front; each column is a vertical gradient from `rgba(ink, a)` to transparent over `mist` px. Ranges start at frames -6, 6, 18 and finish at 34, 48, 60 with cubic-out. Dry-brush ridge line: 5 px dashes, skipped where `hash < 0.22`, width `1 + hash * (1.5 + ri)`. Red sun spring at 34 `{9, 120}` with a jittered radius. Cliff fills downward frames 28 to 62, outline draws 26 to 46, 46 dry-brush texture strokes 48 to 82, pine trunk and needle clusters 66 to 97, river as 34 broken strokes 50 to 92, boat drifting `380 + 0.35 f`, three mist blobs scrolling, a cached half-res grain canvas (binary noise, alpha up to 34, plus 260 fibre curves) drawn on top. Titles are DOM with a brush-edge mask: `WebkitMaskImage: linear-gradient(180deg, #000 pct%, rgba(0,0,0,0.4) pct+6%, transparent pct+14%)` with `pct = p * 130 - 15`, vertical `writingMode: vertical-rl`, Cormorant SC 64 letter-spacing 22, frames 84 to 114; red seal `#B8352A` 96 px spring at 112 `{11, 260}` scale 1.6 to 1 rotate -8 to -3, cream inner border + red outline.

**Needs:** nothing but fonts. CPU-cheap.

**Port note.** Low fit for El Coyote (Chinese ink landscape). Two pieces transfer: (1) the `Brush` mask reveal is the right way to bring in the Kaushan Script lockup or Instrument Serif lines "as if painted" (CSS masks work in Remotion; it is HyperFrames' renderer that drops `-webkit-mask-image`, per tenfoldmarc's gotchas), and (2) the canvas-per-frame pattern is the escape hatch for anything procedural (smoke, oil, weld sparks) without three.js.

```tsx
export const BrushIn: React.FC<{ dur: number; at?: number; len?: number; dir?: "down" | "right"; children: React.ReactNode; style?: React.CSSProperties }> = ({ dur, at = 0, len = 16, dir = "right", children, style }) => {
  const frame = useCurrentFrame(); const p = prog(frame, at, len, (t) => t);
  const pct = p * 130 - 15;
  const mask = `linear-gradient(${dir === "down" ? "180deg" : "90deg"}, #000 ${pct}%, rgba(0,0,0,0.4) ${pct + 6}%, transparent ${pct + 14}%)`;
  return <div style={{ ...style, WebkitMaskImage: mask, maskImage: mask, opacity: tailFade(frame, dur, 6) }}>{children}</div>;
};
```

### 3.11 Timeline (viashaan floor timeline, plus the two "render timeline" panels)

**viashaan `Timeline.tsx` (the one Jacob wants for Road to SEMA).** A 2.5D floor: wrapper `perspective: 1600`, inner `transformOrigin 50% 60%`, `rotateX(52 to 40 deg) scale(1.45 to 1.05) translateY(-260 to 80 px) rotateZ(-8 to 0 deg)` with `cam = bezier(0.4,0,0.2,1)(f/120)`: opens low and close, cranes up and squares off, lands a second after the playhead stops. On the floor: a 90 px grid, a grey rail from A (230, 380) to B (600, 1500), a blue fill to `head = pt(p)` where `p = 0.04 to 0.93` over 100 frames with `bezier(0.35,0.05,0.25,1)` (fast through the middle, brakes into now), 7 year ticks at `u = 0.12 + 0.13 i` that turn blue and whose labels darken as `p >= u` (alternating 64 px and 34 px year labels), a head dot r 16 with an r 30 halo. Milestone cards are DOM (not on the floor, so they stay legible): `transformOrigin 50% 100%`, `perspective(900px) rotateX((1 - s) * 85deg)` with `s = spring({frame: f - tf, damping 9, stiffness 150})`, `tf = at * 0.72 + 8` (mapped from the progress), positioned `x = 360 + 120 i, y = 540 + 270 i`, white card radius 20 with a 92 px thumbnail square, mono year, 34 px title, 22 px sub; the last card is `now`: blue `#2442F5`, `scale 1.08`, width 470, and a black `NOW` pill springing 5 frames later. Card "Never": constant-speed fill, second accent colour, camera still drifting at the end, NOW card landing before the line reaches it.

**Vibha `red_timeline` (fx.py 970 to 1003) and Dryxio `Timeline` (hero.tsx 286 to 330)** are the other sense of "timeline": an editor render panel. Vibha: red duotone grade on the room only (`bg = lum * (1.05, 0.3, 0.27) * 0.85`, you stay in colour), REC + timecode top-left, a `0.9 W x 0.19 H` dark panel sliding up from `H*0.755 + 0.3 H`, three tracks of rounded clips that light red as the playhead `p = 0.04 + 0.92 lt/(0.95 d)` passes, playhead white line with a blurred glow layer. Dryxio: purple `#2a1533` panel with a 170x300 live camera thumb, five mono rows that tick `✓` every `max(4, min(20, 0.5 dur / 5))` frames, a 10-still filmstrip with yellow borders. Both are "AI edited this" props; our `Checklist` and `PullBackWindow` already cover that beat, so only the floor timeline is new.

**Port (Remotion, front, no footage).**

```tsx
export type Milestone = { year: string; title: string; sub: string; at: number; now?: boolean; img?: string };
export const FloorTimeline: React.FC<{ items: Milestone[]; dur: number; title?: string; accent?: string }> = ({ items, dur, title = "ROAD TO SEMA 2027", accent = C.oxblood }) => {
  const frame = useCurrentFrame(); const { fps } = useVideoConfig();
  const p = interpolate(frame, [0, 100], [0.04, 0.93], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.bezier(0.35, 0.05, 0.25, 1) });
  const cam = Easing.bezier(0.4, 0, 0.2, 1)(Math.min(1, frame / 120));
  const A = { x: 230, y: 380 }, B = { x: 600, y: 1500 }; const pt = (u: number) => ({ x: A.x + (B.x - A.x) * u, y: A.y + (B.y - A.y) * u }); const head = pt(p);
  return (
    <AbsoluteFill style={{ background: C.cream, overflow: "hidden", opacity: tailFade(frame, dur, 6) }}>
      <div style={{ position: "absolute", left: 70, top: 110, fontFamily: mono, fontSize: 22, letterSpacing: 3, color: "#6A717C" }}>■ {title}</div>
      <div style={{ position: "absolute", inset: 0, perspective: 1600 }}>
        <div style={{ position: "absolute", inset: 0, transformOrigin: "50% 60%", transform: `rotateX(${52 - 12 * cam}deg) scale(${1.45 - 0.4 * cam}) translateY(${-260 + 340 * cam}px) rotateZ(${-8 + 8 * cam}deg)` }}>
          <svg width={1080} height={1920}>
            {Array.from({ length: 24 }, (_, i) => <line key={i} x1={0} x2={1080} y1={i * 90} y2={i * 90} stroke={C.ink} strokeOpacity={0.08} />)}
            <line x1={A.x} y1={A.y} x2={B.x} y2={B.y} stroke="#B7BEC8" strokeWidth={10} strokeLinecap="round" />
            <line x1={A.x} y1={A.y} x2={head.x} y2={head.y} stroke={accent} strokeWidth={10} strokeLinecap="round" />
            {items.map((m, i) => { const q = pt(m.at); const done = p >= m.at; return <g key={i}><line x1={q.x - 26} x2={q.x + 26} y1={q.y} y2={q.y} stroke={done ? accent : "#B7BEC8"} strokeWidth={5} /><text x={q.x - 50} y={q.y + 22} textAnchor="end" fontFamily={F.block} fontSize={64} fill={done ? C.ink : "#9aa1ab"}>{m.year}</text></g>; })}
            <circle cx={head.x} cy={head.y} r={16} fill={accent} /><circle cx={head.x} cy={head.y} r={30} fill={accent} fillOpacity={0.18} />
          </svg>
        </div>
      </div>
      {items.map((m, i) => { const tf = interpolate(m.at, [0.04, 0.93], [0, 100]) * 0.72 + 8; const s = spring({ frame: frame - tf, fps, config: { damping: 9, stiffness: 150 } }); const now = !!m.now; return (
        <div key={i} style={{ position: "absolute", left: 360 + i * 120, top: 540 + i * 270, width: now ? 470 : 400, transformOrigin: "50% 100%", transform: `perspective(900px) rotateX(${(1 - s) * 85}deg) scale(${now ? 1.08 : 1})`, background: now ? accent : "#fff", color: now ? C.cream : C.ink, borderRadius: 20, padding: 20, display: "flex", gap: 18, boxShadow: cardShadow, opacity: frame >= tf ? 1 : 0 }}>
          {m.img ? <Img src={staticFile(m.img)} style={{ width: 92, height: 92, borderRadius: 14, objectFit: "cover" }} /> : <div style={{ width: 92, height: 92, borderRadius: 14, background: now ? "rgba(255,255,255,0.25)" : C.tan }} />}
          <div><div style={{ fontFamily: mono, fontSize: 20, letterSpacing: 2, opacity: 0.7 }}>{m.year}</div><div style={{ fontFamily: F.uiSemi, fontSize: 34 }}>{m.title}</div><div style={{ fontFamily: F.ui, fontSize: 22, opacity: 0.75 }}>{m.sub}</div></div>
          {now && <div style={{ position: "absolute", top: -18, right: -14, background: C.ink, color: C.cream, fontFamily: mono, fontSize: 20, padding: "6px 14px", borderRadius: 14, transform: `scale(${spring({ frame: frame - tf - 5, fps, config: { damping: 9 } })})` }}>NOW</div>}
        </div>); })}
    </AbsoluteFill>
  );
};
```

Milestones for us: frame swap, 7.3 in, compounds, fuel system (Driven Diesel), paint, SEMA 2027 as the NOW/last card. One click per hinge.

### 3.12 Shorter notes on the rest of what was read

- **Paper Desk (viashaan).** The landing physics is the keeper: `t = clip((f - start)/13)`, `fall = t²`, position `from * (1 - fall) + skid` where `skid = (1 - e^(-0.5 a)) * 6` after landing, hop `max(0, sin(0.9a) e^(-0.45a)) * 0.012` added to scale, rotation overshoot `rot * (1 + 0.1 e^(-0.35a) cos(0.6a))`, scale `1 + 0.14 lift + hop`, shadow `(4 + 40 lift)px (6 + 60 lift)px (10 + 50 lift)px rgba(0,0,0, 0.35 - 0.15 lift)`. Camera: push 1 to 1.07 over 118 frames plus jolts `e^(-0.5 (f-t)) sin(1.6 (f-t)) * 4` at each landing frame (15, 25, 37), roll -0.5 to 0.5 deg, drift `3 sin(0.05 f)`, frozen for the last second. Highlighter: per line, width `calc(p*100% + 12px)`, yellow `#FFE024`, `mixBlendMode multiply`, chisel `clipPath polygon(1% 0, 100% 6%, 98% 100%, 0 94%)`, lines staggered 9 frames, 8 frames each. Marker circle and arrow: `pathLength 1` dashoffset. This is the natural home for invoices, dyno sheets and the parts list on the bench mat; port the `land()` helper into `anim.ts` as is.
- **Stat Chart (viashaan).** Tip index `interpolate(f, [0, 52, 66, 112], [3, EV-1.5, EV+2.5, N-1])` with `bezier(0.3,0.1,0.35,1)`: slows into the event and out of it. Line is white before the event, 7 px orange after; event ring spring `{8, 200}`, leader line 10 frames, three callout lines rise from masks 4 frames apart `{14, 220}`; at landing the chip springs `{9, 220}`, a ping ring `r = 12 + 50 ping`, the value tag slides in `{14, 180}`. Our `ChartGrow` has the draw and the pill; it lacks the colour split at an event and the slow-in. Cheap upgrade.
- **Screen-Recording Zoom (viashaan).** Zoom `1 + spring({frame: f-20, damping 30, stiffness 50})` (a slow, heavy spring, no overshoot) with `transformOrigin` at the click target and a translate that keeps the target at (540, 1000); cursor bezier `(0.45,0,0.2,1)` over 40 frames with a sine arc `+120 sin(πt)` so it curves; press scale 0.95 for 8 frames, ring `40 + 140 ring` px fading. Use for portal walkthroughs (elcoyotediesel.com). Replace `PullBackWindow` rows with this when the beat is "click here".
- **Headline Highlight (viashaan).** Page flies in with spring `{damping 14, stiffness 70, mass 1.4}`: `translate(520 to 0, 1500 to 0) rotateX(58 to 14) rotateY(-30 to -9) rotateZ(14 to 3)`, blur fades with velocity (`s - sPrev`); camera `scale 0.92 to 1.42`, `translateY 0 to -230` over frames 18 to 100 `bezier(0.45,0,0.2,1)`; a background of blurred rotated cards at opacity 0.32; highlighter uses an SVG `rough` filter (`feTurbulence baseFrequency "0.04 0.5"`, `feDisplacementMap scale 9`) on a multiply gradient. For Jacob: magazine mentions, the Diesel World interview. Our `Masthead` is the behind-head cousin; this is the front-layer document version.
- **Vibha `fx_rabbit_hole` / Dryxio `RabbitHole`.** Droste: 7 copies at `s = r^(lev - z)` with `r 0.62`, phase `z = (lt * 0.8) % 1`, spin `(lev - z) * 10 deg`, white border on each, the person stays in front via the mask. Dryxio: 8 copies `0.7^(i + 1 - phase)`, `phase = (f/45) % 1`, each offset `+80 s` down. A one-off; Remotion version is 15 lines.
- **Vibha `fx_spotlight` / Dryxio `Spotlight`.** Vibha: pool `clip(1 - d, 0, 1)^1.6` around the face (`rx 0.5 W, ry 0.46 H`, centred 0.2 H below the face), room darkens to `0.2 + 0.45 pool`, the person lifts `1 + 0.04 k`, optional serif word behind the head with glow radius 26. Dryxio: 8-frame flicker array `[1, .2, 1, .4, 1, 1, .6, 1]` on the neon word, room `brightness(0.38) saturate(0.8)`, four stacked text-shadows for the glow. Our `BgReplace` + `GhostWord` get close; the flicker array is worth copying.
- **Vibha `fx_led_sign`.** Text rasterised to an 11-row dot matrix (`resize BOX, threshold 0.42`), sweep lit left to right over 0.75 s, flicker `0.82 + 0.18 sin(rnd*50 + 30 lt)`, glow `GaussianBlur(cell*0.9) * 1.6`, tucked behind the head so hair overlaps the bottom edge. A shop-sign gag; skip unless a reel calls for it.
- **Vibha `fx_swipe`.** Before/after with a slanted line `line = sp * W + 0.22 (y - H/2)`, 3 px white edge, a `< >` handle at 0.62 H, labels in pills at 0.14 W and 0.86 W; the sweep is `1.05 to 0.1` in the first half then `0.1 to 0.5` (overshoot and settle). Our `BeforeAfter` is vertical and linear; add the slant and the overshoot.
- **Vertigo seam.** ONIKOSIOLA measured it: subtle at 1.16x, obvious at 1.3x, blur makes it worse, real fix is an inpainted clean plate. Our `Vertigo` default `to 1.35` is past the seam point; drop the default to 1.18 or inpaint the plate once per shot (`cv2.inpaint` on the dilated alpha, a 20-line addition to `matte.py`).
- **Cut punch.** tenfoldmarc: `#stage scale 1.05 to 1 over .32 s` on every cut (base + back + cutout together). Our `prog(frame, 0, 10, EASE_OUT)` punch should wrap plate AND cutout in the same transform or they separate for a frame.
- **Word pop.** `scale 1.22 + blur 22px to 1, .2 s, power3.out`, exit `scale .96 blur 16px, .12 s, power2.in` then hard `tl.set` off. Our `BlurWord` matches the entrance; it has no exit blur.

---

## 4. Gotchas the repos document (and which ones apply to us)

**HLG / BT.2020 iPhone and Pocket 3 footage.**
- ONIKOSIOLA (verified): a clip tagged `color_transfer=arib-std-b67` re-encoded without conversion keeps the tag; HyperFrames then logs `hasHdrContent:true`, switches to `capture_hdr_layered`, the transparent WebM LOSES ITS ALPHA (the subject layer renders opaque, everything behind it disappears), colours wash out and the render takes 4x longer (3m11s vs 44s). Fix before matting: `-vf "colorspace=all=bt709:iall=bt2020:fast=1,format=yuv420p" -color_primaries bt709 -color_trc bt709 -colorspace bt709`, then confirm `hasHdrContent:false`. Our `build_reel3.py` already tonemaps with `libplacebo` and tags BT.709 (`TONEMAP`, `COLOR_TAGS`); the thing to check is that `matte.py` is fed the tonemapped plate, never the camera file. (`cv2.VideoCapture` decodes HLG as if it were 709, which is the washed look.)
- HyperFrames `hdr.mdx`: HDR output is MP4 only; "MOV, WebM, GIF, PNG sequence, and alpha output fall back to SDR"; HDR and `--resolution` supersampling cannot combine; motion blur is off for HDR renders. So any HyperFrames insert must be SDR BT.709 end to end.
- HyperFrames `media-effects.mdx`: LUTs are applied in Rec.709 with no LOG conversion first ("a LOG clip ... comes out wrong"). Same rule as ours: no grade on Jacob's footage, and never a LUT on D-Log.

**Alpha WebM.**
- tenfoldmarc: CSS `-webkit-mask-image` does not survive the HyperFrames renderer; bake alpha into VP9 WebM with ffmpeg `alphamerge`. (Remotion is fine with CSS masks.)
- HyperFrames `rendering.mdx`: `ffprobe` reporting `pix_fmt=yuv420p` on a VP9 WebM does not mean alpha was lost; FFmpeg's default VP9 decoder returns opaque frames. Inspect with the alpha-aware decoder before the input: `ffmpeg -c:v libvpx-vp9 -i overlay.webm -frames:v 1 -pix_fmt rgba frame.png`. Our `headpos`-style checks and any `alphaextract` in build_reel3 must pass `-c:v libvpx-vp9` BEFORE `-i` (tenfoldmarc's `headpos.py` does exactly this).
- HyperFrames: "transparent WebM: only browsers decode the alpha, every video editor renders the transparent areas black"; for CapCut hand-off use MOV ProRes 4444 (`--prores-profile` other than 4444 has no alpha). Relevant if Jacob wants a cutout layer in CapCut: give him ProRes 4444, not our VP9.
- tenfoldmarc: ffmpeg concat leaves a 0.033 s start offset and VFR gaps; `remove-background` then duplicates frames and the cutout drifts (two copies of the speaker after a cut by 20 s). Re-encode CFR first (`setpts=N/30/TB -fps_mode cfr -g 30 -keyint_min 30`) and assert equal frame counts. Our `matte.py` reads with OpenCV and writes `-r fps`; if the plate is VFR the same drift happens. Run the plate through build_reel3's CFR slot render before matting, or add a frame-count assert.
- HyperFrames remove-background: `--background-output plate.webm` gives the inverse-alpha plate in one pass (a hole, not an inpaint); `--quality best` avoids the colour halo when layering over the original; the model drops held objects (dark mic, phone), flickers on fast motion, about 2 fps at 1080p on CPU, 168 MB first download. RVM (ours) is better on held objects; same CPU speed class.
- ONIKOSIOLA matte trap: burned-in captions and dark backlit clothes punch holes in the u2net mask (white blotches on sticker and outline effects); fix with a morphological close on the alpha. Add `cv2.morphologyEx(a, MORPH_CLOSE, 7x7)` as an option in `matte.py` for sticker/boil shots.

**Headless Chrome and the renderers.**
- tenfoldmarc: heavy `backdrop-filter`/blur on many elements can make HyperFrames captures go black; keep it to a few. `autoAlpha:1` overrides a CSS opacity (a "3% grain" layer ran at 100%). Every `<video>` needs an id or it renders frozen; overlapping media need separate `data-track-index`. Never tween opacity on an element with `data-start`; wrap it. Lint rejects `letterSpacing` tweens (fake tracking with `scaleX`). `fromTo` needs `immediateRender:false` for hidden-until-time elements. Element ids cannot contain apostrophes. `tl.set` at a rounded cut time fires a frame late: use `frame/30 - 0.002`.
- ONIKOSIOLA: two sub-comps need distinct root ids; stale `public/.transcode-cache` and `.hyperframes` reuse old footage after a re-encode; `check` flags intentional occlusion (`text_occluded`), add `data-layout-allow-occlusion`. Verified-to-animate properties in HyperFrames renders: `opacity`, `x/y/scale/rotation`, `filter` string to string (same function list both ends), `attr:{}` on SVG filter params, `webkitMaskSize`, `backgroundPosition`, `clipPath` with equal vertex counts.
- HyperFrames `motion-blur.mdx`: opt-in `data-motion-blur="on"`, default shutter 240 deg, at least 32 samples; the default filter tier softens zooms, only the `capture` tier (Chrome HTML-in-Canvas, flag needed before Chrome 157) streaks them, and capture draws movers above static content. Render cost 1.6x to 2.9x. Not a concern for Remotion, where `@remotion/motion-blur` does the same thing per component.
- rajshaikh SKILL.md (Remotion + three.js): on a WebGL context error add `--gl=angle` on Windows and Mac (`--gl=swangle` on Linux); without a GPU the 3D styles "take a few minutes"; Remotion downloads headless Chrome on first render; fonts from Google Fonts need internet at bundle time (ours are local via `loadBrandFonts`, good).
- Dryxio: Remotion free up to 3 people (company licence beyond); renders 4K via `scale: 2` with `--hd` for 1080; cutout at 15 fps by default and indexed `floor(f * 15 / 30)` (a 30 fps cutout doubles the time).
- HyperFrames vs Remotion, from their own comparison page: Remotion is "one pure function of the frame number, no timeline to register, no contract to get subtly wrong"; HyperFrames "asks you to follow rules ... and breaks quietly if you don't." That is the reason to stay on Remotion for rival-reels and only borrow HyperFrames' numbers.

**Windows.**
- tenfoldmarc `gotchas.md` and `WINDOWS_TEST.md`: `python3` is a Store stub (use `python` or `py -3`); `npx` is `npx.cmd` and cannot be started by bare name from Python (start through node directly); a program installed while Claude Code is open is not on PATH until it is fully restarted; every `open()` needs `encoding='utf-8'` or captions with curly quotes break; file paths inside an ffmpeg FILTER (`subtitles=`, `movie=`, font files) need `C\:/...` escaping, so pass files with `-i` and keep filter-side paths relative; Git Bash rewrites arguments starting with `/` (set `MSYS_NO_PATHCONV=1` for flags); Smart App Control can block `sharp` (used for snapshots and by the cutout); antivirus can make ffmpeg fail once with `spawn EBUSY` (retry once); faster-whisper picks CUDA on an NVIDIA machine without the toolkit (`cublas64_12.dll` error) so pass `device='cpu'`; no GPU matte path on Windows without `HYPERFRAMES_CUDA=1` and a CUDA onnxruntime; Windows on ARM has no Whisper build. Expected cutout time on a PC: "many minutes", report only if over 15 min for a 10 s reel.
- HyperFrames `rendering.mdx`: the 4:4:4 MP4 option does not play in Windows Media Player or Firefox on Windows (Chrome, Edge and VLC do); keep deliverables 4:2:0 as build_reel3 already does.
- rajshaikh and Dryxio: `python` not `python3`; venv at `.venv\Scripts\python.exe`.

**Design rules worth keeping on the wall (from the code, not the captions).**
- tenfoldmarc safe zone: top 220 px, bottom 450 px (nothing below y 1470), 35 px sides, right 100 px column clear from y 1155. Lead-in captions centred in the chest band y 950 to 1300, never over the face. Cards scaled so the bottom edge is at or above 1470. Our `SAFE` in theme.ts (`top 290, bottom 1240`) is stricter at the bottom and looser at the top; fine.
- Behind-head word: `top = head_top + 0.15 S - 0.72 S` (baseline 30 percent of the x-height below the head top); only the bottom 25 to 30 percent of the letters may be hidden or it "reads as broken". HyperFrames says 30 to 55 percent covered is the sweet spot. Measure per word window from the matte, not once.
- One-second effect samples: entrances 0.2 to 0.4 s, holds 0.6 s. Every cut gets a stage punch.
- viashaan cards, all nine: no fades (things pop, drop, slide, hinge, draw), seeded randomness only, one accent colour, camera never drifts at the end, bottom fifth kept calm, hold for the last second.

---

## 5. Ranked port list

Ranking weighs: fits a diesel build account (north star: attention to the shop), cost in hours, reuse across reels, and whether the kit already has the inputs (cutout, face track, 4K plate).

### rival-reels (Remotion)

1. **ZoomThrough fix with `CameraMotionBlur`** (3.4). One wrapper, already installed, fixes the one effect we render wrong. Use on every talking-head-to-truck-detail cut. Under an hour.
2. **Orbit** (3.1). Two EDL entries, one component, all inputs exist. First use: partner logos (Power Hungry, ISSPRO, Strictly Diesel, CNC Fab, II) orbiting Jacob on the "who is in" reel; second: our own reel tiles. Two hours including a safe-zone check.
3. **digitalZoom curve shared by plate and HudZoom** (3.5). Half an hour; makes the readout honest and adds the push-punch-creep shape.
4. **Sticker + BoilOutline** (3.2, 3.3). Same silhouette trick, two components. Boil is the dossier's "my favourite" bait effect; the sticker is the paper-cut collage. Needs the morphological close option in `matte.py` first (20 lines). Half a day for both.
5. **FloorTimeline** (3.11). Road to SEMA milestones, reusable every month as the build advances. Half a day.
6. **Paper Desk `land()` + Tape + highlighter** (3.12). Invoices, dyno sheets, the parts list on the bench. Port the helper into `anim.ts`, build one `PaperSheet` component. Half a day.
7. **Teardown2D** (3.8). Turbo or injector in layers from bench photos. The shoot is the cost (five clean stills on a fixed tripod), the component is two hours.
8. **StatChart upgrades to ChartGrow** (3.12): slow-in to the event, colour split after it, callout masks. Two hours.
9. **FlipDigit** (3.9). Horsepower and year beats. Two hours.
10. **GlassWord** (3.6). Test on one dark-shop frame first; ship only if it reads.
11. **ScreenZoom** for portal walkthroughs, **BrushIn** for the lockup, **Spotlight flicker array**, **slanted BeforeAfter**, **Vertigo default to 1.18 or inpainted plate**. Small, do them when a reel asks.
12. **MapRoute2D** (3.7). Only for the Phoenix (Driven Diesel) and Las Vegas (SEMA) trips. The three.js original is not worth adding the dependency for.
13. **Ink wash, LED sign, rabbit hole.** Off-brand or one-off; not planned.

### build_reel3 (ffmpeg)

1. **`zoomthrough` slot** (3.4): `fps=120` before the eval=frame scale, then `tmix=frames=4`, `fps=30`. Real zoom streak with filters already in the file; bump `RENDER_VERSION`. One to two hours including the A-tail/B-head split (copy the `prev_whip`/`next_whip` pattern).
2. **`hud` slot** (3.5): drawbox brackets, blinking REC via `enable='lt(mod(t,1),0.6)'`, `%{pts:hms}` timecode, readout via `%{eif}`. Two hours; the only snag is the float readout formatting and font path escaping on Windows.
3. **`sticker` / `boil` on cutout slots** (3.2, 3.3): `alphaextract`, `boxblur` + `geq` threshold dilation, `difference` blend, 10 fps `nullsrc` noise through `displace`, `alphamerge` with a cream colour source, `overlay`. Half a day; only for slots that already have a cutout WebM.
4. **Slanted before/after wipe** (3.12, Vibha `fx_swipe`): `geq` or two `crop` + `overlay` with `x` as an expression of `t` and `Y`; plus the 3 px white edge. Two hours.
5. **Two-stage digital zoom** in `zoom_filters()` (3.5): accept a knot list `[[0, 1.0], [1.0, 1.18], [1.13, 1.3], [2.0, 1.34]]` the way `ramp` already does for speed. One hour.

Not for ffmpeg: orbit, timeline, teardown, map, glass, flip. Those are compositor work and Remotion already has the plumbing.

---

## 6. Files

- This note: `C:\Users\Parts\Desktop\socialmediatakeover\research\2026-11-21-effect-repos-port-notes.md`
- Clones (git-ignored, read only): `C:\Users\Parts\Desktop\socialmediatakeover\research\reel-references\2026-11-21-effect-repos\clone\{video-edit-skill, video-editing-kit, claude-video-effects, effects-skill, claude-animation-styles, hyperframes}`
- Key source files read: `video-edit-skill/assets/template/build.py` (orbit at lines 172 to 207, stage layers at 437 to 500), `video-edit-skill/references/{looks,layout,overlays,gotchas}.md`, `video-edit-skill/scripts/{cutout,headpos,assemble}.py`; `video-editing-kit/skills/video-overlays/{reel-effects-17,effects}.md`; `claude-video-effects/scripts/fx.py` (comp/place/camera 118 to 162, orbit 280, scribble 686, countdown 608, rabbit hole 632, glass 716, liquid_glass 1874, spotlight 320, swipe 379, led 1659, red_timeline 970, slow push 1700, OTS zoom 1956, tape 2075, matte/tracker 2172 to 2250, main 2267); `effects-skill/src/{kit.tsx, effects/hero.tsx, effects/grid.tsx, effects/extra.tsx}`, `effects-skill/scripts/{cutout.py, effects.mjs}`; `claude-animation-styles/skills/*/references/*.tsx` and `card.md`; `hyperframes/docs/guides/{remove-background,hdr,motion-blur,rendering,4k-rendering,media-effects,hyperframes-vs-remotion,gsap-animation}.mdx`, `hyperframes/skills/hyperframes/references/captions.md`, `hyperframes/docs/catalog/{blocks/orbit-card,components/three-orbiting-cards}.mdx`.
- Earlier context these notes build on: `research/reel-references/2026-11-21-tenfoldmarc-profile/DOSSIER.md` (sections 3, 4, 5), `research/reel-references/2026-11-21-the-bar-weekly/WEEKLY.md` (section 2).
