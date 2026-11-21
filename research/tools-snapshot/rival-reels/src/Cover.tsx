import React, { useEffect, useState } from "react";
import { AbsoluteFill, Img, OffthreadVideo, staticFile, continueRender, delayRender } from "remotion";
import { loadBrandFonts, C, F } from "./theme";

/*
  Cover (2026-11-21): the reel cover frame. Profile-conversion finding: seven of seven growing build accounts carry
  a text title on every grid tile; ours had none. Rule: a frame with Jake or the truck in it, a 3 to 4 word title in
  the middle band (nothing in the top or bottom 480 px of 1080x1920, so it survives the 3:4 grid crop), and the small
  series tag "RIVAL · EP n" on build reels. Render as a still:
    npx remotion still src/index.ts Cover out/<name>-cover.jpg --props=out/<name>.cover.json --frame=0
  Props: { src: "plate.mp4" | "still.jpg", atSec?: number, title: "FRAME SWAP", tag?: "RIVAL · EP 03", preset?: "block" | "megante" | "louder", script?: "Teach me how to" }
*/
export type CoverProps = { src: string; atSec?: number; title: string; tag?: string; preset?: "block" | "megante" | "louder"; script?: string; dim?: number; band?: boolean };

export const Cover: React.FC<CoverProps> = ({ src, atSec = 0, title, tag, preset = "block", script, dim = 0.22, band }) => {
  const showBand = band ?? preset === "megante";   // deep red needs a cream field on red or dark trucks
  const [handle] = useState(() => delayRender("fonts"));
  useEffect(() => { loadBrandFonts().then(() => continueRender(handle)); }, [handle]);
  const isVideo = /\.(mp4|webm|mov)$/i.test(src);
  const titleStyle: React.CSSProperties =
    preset === "megante" ? { fontFamily: F.heavy, fontSize: 150, color: "#8E1010", letterSpacing: 4 }
    : preset === "louder" ? { fontFamily: F.block, fontSize: 250, color: C.white, letterSpacing: 2 }
    : { fontFamily: F.block, fontSize: 170, color: C.cream, letterSpacing: 3 };
  return (
    <AbsoluteFill style={{ background: C.black }}>
      {isVideo
        ? <OffthreadVideo src={staticFile(src)} startFrom={Math.round(atSec * 30)} muted style={{ width: "100%", height: "100%", objectFit: "cover" }} />
        : <Img src={staticFile(src)} style={{ width: "100%", height: "100%", objectFit: "cover" }} />}
      <AbsoluteFill style={{ background: `linear-gradient(180deg, rgba(0,0,0,0) 30%, rgba(0,0,0,${dim}) 50%, rgba(0,0,0,0) 72%)` }} />
      {showBand && <div style={{ position: "absolute", left: 0, right: 0, top: 660, height: 440, background: "rgba(239,233,220,0.90)" }} />}
      {/* middle band: y 480 to 1440 is what the 3:4 grid crop keeps; title sits at the centre of it */}
      <div style={{ position: "absolute", left: 60, right: 60, top: preset === "megante" ? 740 : 700, textAlign: "center", lineHeight: 0.95, textTransform: "uppercase", textShadow: preset === "megante" ? "none" : "0 12px 40px rgba(0,0,0,0.6)", ...titleStyle }}>
        {script && <div style={{ fontFamily: F.script, fontSize: 120, color: C.yellow, textTransform: "none", transform: "rotate(-4deg)", marginBottom: -40, textShadow: "0 8px 30px rgba(0,0,0,0.6)" }}>{script}</div>}
        {title}
      </div>
      {tag && (
        <div style={{ position: "absolute", left: 0, right: 0, top: 1040, textAlign: "center" }}>
          <span style={{ fontFamily: F.uiItalic, fontSize: 36, letterSpacing: 5, color: preset === "megante" ? "#8E1010" : C.tan, textTransform: "uppercase", textShadow: "0 6px 20px rgba(0,0,0,0.6)" }}>{tag}</span>
        </div>
      )}
    </AbsoluteFill>
  );
};
