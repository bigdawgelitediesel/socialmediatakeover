import React, { useEffect, useState } from "react";
import { AbsoluteFill, OffthreadVideo, Sequence, staticFile, continueRender, delayRender, useVideoConfig } from "remotion";
import { loadBrandFonts } from "./theme";
import { KineticHook, ScriptBlock, WordStamp, CaptionPill, Numeral, TitleCard } from "./components/Text";
import { LogoCard, PhotoCard, SpecCard, StrikeList, BrowserCard, PromptBar, CommentDrop, CountCard } from "./components/Cards";
import { PlainCaption, ToolTag, OutlineWord, PipCard, SliderReveal, GridWall, ParamPanel, StoryboardCard } from "./components/Chandler";
import { LogoBadge, LowerThird, QuoteBar } from "./components/Brand";

export type Overlay = { type: string; at: number; dur: number; props?: Record<string, any>; behind?: boolean };
export type Caption = { text: string; start: number; end: number; accent?: string; y?: number; style?: "pill" | "plain" };
export type Frame = { top: number; h: number; bg?: string; rule?: string };   // place the plate in a window (title band above it)
export type ReelProps = { plate: string; cutout?: string; captions?: Caption[]; overlays?: Overlay[]; muted?: boolean; captionStyle?: "pill" | "plain"; fps?: number; frame?: Frame };

const REG: Record<string, React.FC<any>> = {
  kinetic: KineticHook, scriptblock: ScriptBlock, stamp: WordStamp, numeral: Numeral, titlecard: TitleCard,
  logo: LogoCard, photo: PhotoCard, spec: SpecCard, strike: StrikeList, browser: BrowserCard, prompt: PromptBar, comment: CommentDrop, count: CountCard,
  // learned from @chandlerintelligence 2026-11-20
  plaincap: PlainCaption, tooltag: ToolTag, outline: OutlineWord, pip: PipCard, slider: SliderReveal, grid: GridWall, params: ParamPanel, storyboard: StoryboardCard,
  // brand pieces (DFC interview reels 2026-11-21)
  badge: LogoBadge, lowerthird: LowerThird, quote: QuoteBar,
};

export const RivalReel: React.FC<ReelProps> = ({ plate, cutout, captions = [], overlays = [], muted = true, captionStyle = "pill", frame }) => {
  const { fps } = useVideoConfig();
  const [handle] = useState(() => delayRender("fonts"));
  useEffect(() => { loadBrandFonts().then(() => continueRender(handle)); }, [handle]);
  const f = (s: number) => Math.round(s * fps);

  const renderOverlay = (o: Overlay, i: number) => {
    const Comp = REG[o.type]; if (!Comp) return null;
    const durF = f(o.dur);
    return (
      <Sequence key={i} from={f(o.at)} durationInFrames={durF} layout="none">
        <Comp plate={plate} atF={f(o.at)} {...(o.props || {})} dur={durF} />
      </Sequence>
    );
  };
  const behind = overlays.filter((o) => o.behind);
  const front = overlays.filter((o) => !o.behind);

  return (
    <AbsoluteFill style={{ backgroundColor: frame?.bg ?? "#000" }}>
      {frame ? (
        <>
          <div style={{ position: "absolute", left: 0, top: frame.top, width: 1080, height: frame.h, overflow: "hidden" }}>
            <OffthreadVideo src={staticFile(plate)} muted={muted} style={{ width: 1080, height: frame.h, objectFit: "cover" }} />
          </div>
          {frame.rule && <div style={{ position: "absolute", left: 0, top: frame.top - 6, width: 1080, height: 6, background: frame.rule }} />}
        </>
      ) : (
        <OffthreadVideo src={staticFile(plate)} muted={muted} />
      )}
      {behind.map(renderOverlay)}
      {cutout && behind.length > 0 && (
        <AbsoluteFill>
          <OffthreadVideo src={staticFile(cutout)} muted transparent />
        </AbsoluteFill>
      )}
      {front.map(renderOverlay)}
      {captions.map((c, i) => {
        const durF = Math.max(2, f(c.end) - f(c.start));
        const style = c.style ?? captionStyle;
        return (
          <Sequence key={`c${i}`} from={f(c.start)} durationInFrames={durF} layout="none">
            {style === "plain"
              ? <PlainCaption text={c.text} accent={c.accent} dur={durF} y={c.y ?? 1150} />
              : <CaptionPill text={c.text} accent={c.accent} dur={durF} y={c.y ?? 1230} />}
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};
