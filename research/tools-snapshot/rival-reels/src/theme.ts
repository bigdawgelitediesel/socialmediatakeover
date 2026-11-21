import { loadFont } from "@remotion/fonts";
import { staticFile } from "remotion";

// El Coyote brand kit (locked 2026-11-20, see socialmediatakeover/research/FONT-LIBRARY.md)
export const C = {
  black: "#0b0b0c",
  ink: "#141414",
  cream: "#efe9dc",
  tan: "#c9b38c",
  oxblood: "#7a1f1f",
  oxbloodDeep: "#5a1515",
  yellow: "#f7d43c",
  white: "#ffffff",
  green: "#1f3a2d",
};

export const F = {
  block: "Anton",
  script: "Kaushan Script",
  ui: "Poppins",
  uiLight: "Poppins Light",
  uiItalic: "Poppins Italic",
  uiSemi: "Poppins SemiBold",
  serif: "Instrument Serif",
  heavy: "Archivo Black",
};

export const SAFE = { top: 290, bottom: 1920 - 680, left: 72, right: 1080 - 130 };

let loaded = false;
export const loadBrandFonts = async () => {
  if (loaded) return;
  loaded = true;
  await Promise.all([
    loadFont({ family: F.block, url: staticFile("fonts/Anton-Regular.ttf") }),
    loadFont({ family: F.script, url: staticFile("fonts/KaushanScript-Regular.ttf") }),
    loadFont({ family: F.ui, url: staticFile("fonts/Poppins-Medium.ttf") }),
    loadFont({ family: F.uiLight, url: staticFile("fonts/Poppins-Light.ttf") }),
    loadFont({ family: F.uiItalic, url: staticFile("fonts/Poppins-Italic.ttf") }),
    loadFont({ family: F.uiSemi, url: staticFile("fonts/Poppins-SemiBold.ttf") }),
    loadFont({ family: F.serif, url: staticFile("fonts/InstrumentSerif-Italic.ttf") }),
    loadFont({ family: F.heavy, url: staticFile("fonts/ArchivoBlack-Regular.ttf") }),
  ]);
};

export const shadow = "0 10px 30px rgba(0,0,0,0.45)";
export const cardShadow = "0 18px 50px rgba(0,0,0,0.55), 0 2px 6px rgba(0,0,0,0.35)";
