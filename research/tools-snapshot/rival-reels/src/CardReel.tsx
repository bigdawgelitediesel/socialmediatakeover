import React, { useEffect, useState } from "react";
import { AbsoluteFill, Img, OffthreadVideo, Sequence, staticFile, continueRender, delayRender, useVideoConfig } from "remotion";
import { loadBrandFonts, C } from "./theme";
import { REG, Overlay, Caption } from "./RivalReel";
import { CaptionPill } from "./components/Text";
import { PlainCaption } from "./components/Chandler";

/*
  CardReel (2026-11-21): a plate-free composition for pure motion-graphics reels in the @ai.nxtlvl / @ultra.skills
  menu grammar. Background is a flat brand color, a still, or a blurred video; everything else is overlays from REG
  driven by a props JSON (same schema as RivalReel, plus `bg` and `durationSec`). Audio is muxed afterwards by ffmpeg
  (voice bed + ambience + sfx via build_reel3's audio block), same as every other render.
*/
export type CardReelProps = {
  bg?: string;                 // "#0b0b0c" | "paper" | "image.png" | "clip.mp4" (video is blurred + darkened as paper)
  durationSec: number;
  fps?: number;
  overlays?: Overlay[];
  captions?: Caption[];
  captionStyle?: "pill" | "plain";
  grain?: boolean;
};

const PAPER = "#efe9dc";

export const CardReel: React.FC<CardReelProps> = ({ bg = C.black, durationSec, overlays = [], captions = [], captionStyle = "plain", grain = true }) => {
  const { fps } = useVideoConfig();
  const [handle] = useState(() => delayRender("fonts"));
  useEffect(() => { loadBrandFonts().then(() => continueRender(handle)); }, [handle]);
  const f = (s: number) => Math.round(s * fps);
  const isVideo = /\.(mp4|webm|mov)$/i.test(bg);
  const isImage = /\.(png|jpe?g|webp)$/i.test(bg);
  const color = bg === "paper" ? PAPER : (!isVideo && !isImage ? bg : C.black);
  return (
    <AbsoluteFill style={{ backgroundColor: color }}>
      {isVideo && <OffthreadVideo src={staticFile(bg)} muted style={{ width: "100%", height: "100%", objectFit: "cover", transform: "scale(1.2)", filter: "blur(30px) brightness(0.45) saturate(0.8)" }} />}
      {isImage && <Img src={staticFile(bg)} style={{ width: "100%", height: "100%", objectFit: "cover" }} />}
      {/* soft vignette so cards pop, same on paper and black */}
      <AbsoluteFill style={{ background: "radial-gradient(ellipse at 50% 45%, rgba(0,0,0,0) 55%, rgba(0,0,0,0.28) 100%)" }} />
      {overlays.map((o, i) => {
        const Comp = REG[o.type]; if (!Comp) return null;
        const durF = f(o.dur);
        return (
          <Sequence key={i} from={f(o.at)} durationInFrames={durF} layout="none">
            <Comp atF={f(o.at)} {...(o.props || {})} dur={durF} />
          </Sequence>
        );
      })}
      {captions.map((c, i) => {
        const durF = Math.max(2, f(c.end) - f(c.start));
        const style = c.style ?? captionStyle;
        return (
          <Sequence key={`c${i}`} from={f(c.start)} durationInFrames={durF} layout="none">
            {style === "plain"
              ? <PlainCaption text={c.text} accent={c.accent} dur={durF} y={c.y ?? 1150} variant={c.variant} accentFont={c.accentFont} ink={c.ink} />
              : <CaptionPill text={c.text} accent={c.accent} dur={durF} y={c.y ?? 1230} />}
          </Sequence>
        );
      })}
      {grain && <AbsoluteFill style={{ pointerEvents: "none", opacity: 0.06, backgroundImage: "url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='120' height='120'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2'/></filter><rect width='120' height='120' filter='url(%23n)' opacity='0.9'/></svg>\")" }} />}
    </AbsoluteFill>
  );
};
