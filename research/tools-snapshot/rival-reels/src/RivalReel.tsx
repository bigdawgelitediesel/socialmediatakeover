import React, { useEffect, useState } from "react";
import { AbsoluteFill, OffthreadVideo, Sequence, staticFile, continueRender, delayRender, useVideoConfig } from "remotion";
import { loadBrandFonts } from "./theme";
import { KineticHook, ScriptBlock, WordStamp, CaptionPill, Numeral, TitleCard } from "./components/Text";
import { LogoCard, PhotoCard, SpecCard, StrikeList, BrowserCard, PromptBar, CommentDrop, CountCard } from "./components/Cards";
import { PlainCaption, ToolTag, OutlineWord, PipCard, SliderReveal, GridWall, ParamPanel, StoryboardCard } from "./components/Chandler";
import { LogoBadge, LowerThird, QuoteBar, CornerLogos } from "./components/Brand";
import { ProgressHud, SidebarList, PhoneStage, CountUp, StrikeStamp, ItemCard, Headline, GhostWord, IrisWipe, NegativeFlash, CommentGate, QuadWall, Checklist } from "./components/Menu";
import { WallBehind, Masthead, FrameBreak, Vertigo, BgReplace, ChartGrow, PullBackWindow, ZoomThrough, HudZoom, BeforeAfter, BlurWord, Orbit, CompareCards, FaceHud } from "./components/Effects";
import { StickerEdge, DoodleBoil } from "./components/Boil";
import { WindowStack, PinThumb, Terminal, RepoCard, SpecChips, NotePill } from "./components/Paper";

export type Overlay = { type: string; at: number; dur: number; props?: Record<string, any>; behind?: boolean };
export type Caption = { text: string; start: number; end: number; accent?: string; y?: number; style?: "pill" | "plain"; variant?: "sans" | "serif" | "caps" | "italic"; accentFont?: "serif" | "script"; ink?: boolean };
export type Frame = { top: number; h: number; bg?: string; rule?: string };   // place the plate in a window (title band above it)
export type ReelProps = { plate: string; cutout?: string; captions?: Caption[]; overlays?: Overlay[]; muted?: boolean; captionStyle?: "pill" | "plain"; fps?: number; frame?: Frame };

export const REG: Record<string, React.FC<any>> = {
  kinetic: KineticHook, scriptblock: ScriptBlock, stamp: WordStamp, numeral: Numeral, titlecard: TitleCard,
  logo: LogoCard, photo: PhotoCard, spec: SpecCard, strike: StrikeList, browser: BrowserCard, prompt: PromptBar, comment: CommentDrop, count: CountCard,
  // learned from @chandlerintelligence 2026-11-20
  plaincap: PlainCaption, tooltag: ToolTag, outline: OutlineWord, pip: PipCard, slider: SliderReveal, grid: GridWall, params: ParamPanel, storyboard: StoryboardCard,
  // brand pieces (DFC interview reels 2026-11-21)
  badge: LogoBadge, lowerthird: LowerThird, quote: QuoteBar, corners: CornerLogos,
  // menu-reel grammar (2026-11-21: nxtlvl, tenfoldmarc, ultra.skills, edita.visuals studies)
  hud: ProgressHud, sidebar: SidebarList, phone: PhoneStage, countup: CountUp, strikestamp: StrikeStamp, item: ItemCard, headline: Headline, ghost: GhostWord, iris: IrisWipe, negflash: NegativeFlash, gate: CommentGate, quad: QuadWall, checklist: Checklist,
  // tenfoldmarc effect vocabulary (2026-11-21)
  wall: WallBehind, masthead: Masthead, framebreak: FrameBreak, vertigo: Vertigo, bgreplace: BgReplace, chart: ChartGrow, pullback: PullBackWindow, zoomthrough: ZoomThrough, hudzoom: HudZoom, beforeafter: BeforeAfter, blurword: BlurWord, orbit: Orbit, compare: CompareCards, facehud: FaceHud,
  // silhouette effects (2026-11-21 port notes 3.2 / 3.3)
  sticker: StickerEdge, boil: DoodleBoil,
  // paper explainer grammar (2026-11-21 guipaulinooo Teardown study)
  winstack: WindowStack, pinthumb: PinThumb, terminal: Terminal, repo: RepoCard, specchips: SpecChips, notepill: NotePill,
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
        <Comp plate={plate} cutout={cutout} atF={f(o.at)} {...(o.props || {})} dur={durF} />
      </Sequence>
    );
  };
  const behind = overlays.filter((o) => o.behind);
  const front = overlays.filter((o) => !o.behind);

  return (
    <AbsoluteFill style={{ backgroundColor: frame?.bg && frame.bg !== "blur" ? frame.bg : "#000" }}>
      {frame ? (
        <>
          {frame.bg === "blur" && (
            // the top region is the shot itself, blurred and darkened, so the frame reads as one image (no color block)
            <AbsoluteFill style={{ overflow: "hidden" }}>
              <OffthreadVideo src={staticFile(plate)} muted style={{ width: "100%", height: "100%", objectFit: "cover", transform: "scale(1.35)", filter: "blur(38px) brightness(0.42) saturate(0.85)" }} />
              <AbsoluteFill style={{ background: "linear-gradient(180deg, rgba(0,0,0,0.35) 0%, rgba(0,0,0,0.05) 60%, rgba(0,0,0,0) 100%)" }} />
            </AbsoluteFill>
          )}
          <div style={{ position: "absolute", left: 0, top: frame.top, width: 1080, height: frame.h, overflow: "hidden", boxShadow: frame.bg === "blur" ? "0 -18px 50px rgba(0,0,0,0.45)" : undefined }}>
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
              ? <PlainCaption text={c.text} accent={c.accent} dur={durF} y={c.y ?? 1150} variant={c.variant} accentFont={c.accentFont} ink={c.ink} />
              : <CaptionPill text={c.text} accent={c.accent} dur={durF} y={c.y ?? 1230} />}
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};
