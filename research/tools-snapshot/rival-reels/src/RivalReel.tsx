import React, { useEffect, useState } from "react";
import { AbsoluteFill, OffthreadVideo, Sequence, staticFile, continueRender, delayRender, useVideoConfig } from "remotion";
import { loadBrandFonts } from "./theme";
import { KineticHook, ScriptBlock, WordStamp, CaptionPill, Numeral, TitleCard } from "./components/Text";
import { LogoCard, PhotoCard, SpecCard, StrikeList, BrowserCard, PromptBar, CommentDrop, CountCard } from "./components/Cards";

export type Overlay = { type: string; at: number; dur: number; props?: Record<string, any> };
export type Caption = { text: string; start: number; end: number; accent?: string };
export type ReelProps = { plate: string; captions?: Caption[]; overlays?: Overlay[]; muted?: boolean };

const REG: Record<string, React.FC<any>> = {
  kinetic: KineticHook, scriptblock: ScriptBlock, stamp: WordStamp, numeral: Numeral, titlecard: TitleCard,
  logo: LogoCard, photo: PhotoCard, spec: SpecCard, strike: StrikeList, browser: BrowserCard, prompt: PromptBar, comment: CommentDrop, count: CountCard,
};

export const RivalReel: React.FC<ReelProps> = ({ plate, captions = [], overlays = [], muted = true }) => {
  const { fps } = useVideoConfig();
  const [handle] = useState(() => delayRender("fonts"));
  useEffect(() => { loadBrandFonts().then(() => continueRender(handle)); }, [handle]);
  const f = (s: number) => Math.round(s * fps);
  return (
    <AbsoluteFill style={{ backgroundColor: "#000" }}>
      <OffthreadVideo src={staticFile(plate)} muted={muted} />
      {overlays.map((o, i) => {
        const Comp = REG[o.type]; if (!Comp) return null;
        const durF = f(o.dur);
        return (
          <Sequence key={i} from={f(o.at)} durationInFrames={durF} layout="none">
            <Comp {...(o.props || {})} dur={durF} />
          </Sequence>
        );
      })}
      {captions.map((c, i) => {
        const durF = Math.max(2, f(c.end) - f(c.start));
        return (
          <Sequence key={`c${i}`} from={f(c.start)} durationInFrames={durF} layout="none">
            <CaptionPill text={c.text} accent={c.accent} dur={durF} />
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};
