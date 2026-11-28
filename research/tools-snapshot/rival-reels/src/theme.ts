import { loadFont } from "@remotion/fonts";
import { staticFile } from "remotion";

// Brand switch at bundle time: `REMOTION_BRAND=dfc npx remotion render ...` (default = El Coyote).
export const BRAND: "coyote" | "dfc" = (process.env.REMOTION_BRAND === "dfc" ? "dfc" : "coyote");

// El Coyote brand kit (locked 2026-11-20, see socialmediatakeover/research/FONT-LIBRARY.md)
const COYOTE = {
  black: "#0b0b0c",
  ink: "#141414",
  cream: "#efe9dc",
  tan: "#c9b38c",
  oxblood: "#7a1f1f",
  oxbloodDeep: "#5a1515",
  yellow: "#f7d43c",
  white: "#ffffff",
  green: "#1f3a2d",
  hi: "#e2543e",          // caption highlight box
};
// Diesel Freedom Coalition (dfc-web globals.css: navy / cream / oxblood / gold)
const DFC = {
  black: "#0A1226",
  ink: "#0F1A33",
  cream: "#F5EDD8",
  tan: "#C8973A",
  oxblood: "#8B1A1A",
  oxbloodDeep: "#5a1010",
  yellow: "#C8973A",
  white: "#ffffff",
  green: "#1B2A4A",
  hi: "#C8973A",
};
export const C = BRAND === "dfc" ? DFC : COYOTE;

const F_COYOTE = {
  block: "Anton",
  script: "Kaushan Script",
  ui: "Poppins",
  uiLight: "Poppins Light",
  uiItalic: "Poppins Italic",
  uiSemi: "Poppins SemiBold",
  serif: "Instrument Serif",
  heavy: "Archivo Black",
  // Jacob's main fonts, picked 2026-11-23 from @kalylsfilms DcBwAjvoEqI:
  // Impact (exact), Snell Roundhand (stand-in Pinyon Script), Rocktown (stand-in Permanent Marker)
  impact: "Impact",
  round: "Pinyon Script",
  brush: "Permanent Marker",
};
const F_DFC = {
  block: "Oswald Bold",
  script: "Instrument Serif",
  ui: "Montserrat SemiBold",
  uiLight: "Poppins Light",
  uiItalic: "Poppins Italic",
  uiSemi: "Montserrat SemiBold",
  serif: "Instrument Serif",
  heavy: "Montserrat ExtraBold",
  impact: "Oswald Bold",
  round: "Instrument Serif",
  brush: "Instrument Serif",
};
export const F = BRAND === "dfc" ? F_DFC : F_COYOTE;

export const SAFE = { top: 290, bottom: 1920 - 680, left: 72, right: 1080 - 130 };

let loaded = false;
export const loadBrandFonts = async () => {
  if (loaded) return;
  loaded = true;
  await Promise.all([
    loadFont({ family: "Anton", url: staticFile("fonts/Anton-Regular.ttf") }),
    loadFont({ family: "Kaushan Script", url: staticFile("fonts/KaushanScript-Regular.ttf") }),
    loadFont({ family: "Poppins", url: staticFile("fonts/Poppins-Medium.ttf") }),
    loadFont({ family: "Poppins Light", url: staticFile("fonts/Poppins-Light.ttf") }),
    loadFont({ family: "Poppins Italic", url: staticFile("fonts/Poppins-Italic.ttf") }),
    loadFont({ family: "Poppins SemiBold", url: staticFile("fonts/Poppins-SemiBold.ttf") }),
    loadFont({ family: "Instrument Serif", url: staticFile("fonts/InstrumentSerif-Italic.ttf") }),
    loadFont({ family: "Archivo Black", url: staticFile("fonts/ArchivoBlack-Regular.ttf") }),
    loadFont({ family: "Impact", url: staticFile("fonts/impact.ttf") }),
    loadFont({ family: "Pinyon Script", url: staticFile("fonts/PinyonScript-Regular.ttf") }),
    loadFont({ family: "Permanent Marker", url: staticFile("fonts/PermanentMarker-Regular.ttf") }),
    loadFont({ family: "Oswald Bold", url: staticFile("fonts/Oswald-Bold.ttf") }),
    loadFont({ family: "Oswald Medium", url: staticFile("fonts/Oswald-Medium.ttf") }),
    loadFont({ family: "Montserrat SemiBold", url: staticFile("fonts/Montserrat-SemiBold.ttf") }),
    loadFont({ family: "Montserrat ExtraBold", url: staticFile("fonts/Montserrat-ExtraBold.ttf") }),
  ]);
};

export const shadow = "0 10px 30px rgba(0,0,0,0.45)";
export const cardShadow = "0 18px 50px rgba(0,0,0,0.55), 0 2px 6px rgba(0,0,0,0.35)";
