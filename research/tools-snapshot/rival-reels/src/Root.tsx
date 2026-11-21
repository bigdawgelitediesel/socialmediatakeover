import React from "react";
import { Composition, staticFile } from "remotion";
import { getVideoMetadata } from "@remotion/media-utils";
import { RivalReel, ReelProps } from "./RivalReel";
import { CardReel, CardReelProps } from "./CardReel";
import { Cover, CoverProps } from "./Cover";

const FPS = 30;

export const Root: React.FC = () => (
  <>
  <Composition
    id="RivalReel"
    component={RivalReel}
    fps={FPS}
    width={1080}
    height={1920}
    durationInFrames={30 * 30}
    defaultProps={{ plate: "plate.mp4", captions: [], overlays: [], muted: true } as ReelProps}
    calculateMetadata={async ({ props }) => {
      // the composition runs at the PLATE's frame rate (props.fps, default 30): a 24 fps plate rendered at 30 would duplicate every 4th frame
      const fps = (props as ReelProps).fps ?? FPS;
      const meta = await getVideoMetadata(staticFile(props.plate));
      return { durationInFrames: Math.ceil(meta.durationInSeconds * fps), fps, props };
    }}
  />

  <Composition
    id="CardReel"
    component={CardReel}
    fps={FPS}
    width={1080}
    height={1920}
    durationInFrames={30 * 10}
    defaultProps={{ bg: "#0b0b0c", durationSec: 10, overlays: [], captions: [] } as CardReelProps}
    calculateMetadata={async ({ props }) => {
      const p = props as CardReelProps; const fps = p.fps ?? FPS;
      return { durationInFrames: Math.ceil(p.durationSec * fps), fps, props };
    }}
  />
  <Composition
    id="Cover"
    component={Cover}
    fps={FPS}
    width={1080}
    height={1920}
    durationInFrames={1}
    defaultProps={{ src: "cards/f600.jpg", title: "FRAME SWAP", tag: "RIVAL · EP 01" } as CoverProps}
  />
  </>
);
