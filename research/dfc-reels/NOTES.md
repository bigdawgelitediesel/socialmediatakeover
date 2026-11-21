
## 2026-11-21 layout v4 (approved) + tracker bug

- Layout that Jacob approved ("This is looking way better"): full-frame 1080x1920 video, no band or blurred top,
  kinetic hook centred over the chest for 3 s, plain white captions (4-6 word phrases, one gold accent) at chin+55,
  Oswald/Montserrat name tag top-left for 4 s on each speaker's first appearance, no coin badge. Rule recorded:
  never put a title band or region above the video.
- Bug found on the sheet pass: 7 of 18 reels framed the wheel display instead of Troy. dfc_track.py steps whole
  frames (23.976/2 = 11.99 Hz) but wrote "hz": 10, and gen_dfc indexed samples by t*hz, so every crop read a face
  from ~17% earlier in the interview (100+ s off by the 10-minute mark). Fix: gen_dfc looks samples up by their own
  timestamp (bisect), the tracker writes the true rate. All 18 re-rendered.
- QA note: single held frames in a static interview are the subject holding still, not judder; the 75-cents reel's
  cluster at 52.6-53.3 s is the dip transition. Compare against the approved pardon reel (one held frame at 40.4 s).
