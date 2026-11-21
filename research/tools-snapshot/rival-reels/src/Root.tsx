import React from "react";
import { Composition, staticFile } from "remotion";
import { getVideoMetadata } from "@remotion/media-utils";
import { RivalReel, ReelProps } from "./RivalReel";

const FPS = 30;

export const Root: React.FC = () => (
  <Composition
    id="RivalReel"
    component={RivalReel}
    fps={FPS}
    width={1080}
    height={1920}
    durationInFrames={30 * 30}
    defaultProps={{ plate: "plate.mp4", captions: [], overlays: [], muted: true } as ReelProps}
    calculateMetadata={async ({ props }) => {
      const meta = await getVideoMetadata(staticFile(props.plate));
      return { durationInFrames: Math.ceil(meta.durationInSeconds * FPS), props };
    }}
  />
);
