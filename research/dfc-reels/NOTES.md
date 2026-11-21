
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

## 2026-11-21 (later) corner logos, no Troy banner, reel 19, audio joins
- Jacob: Dynamic Diesels logo bottom-left + DFC lockup (white) bottom-right on THIS set only (`corner_logos` in reels.json, `corners` overlay in Brand.tsx). Future DFC reels: white DFC lockup only unless the partner was in the shoot.
- Jacob: "take the Troy Lake Founder banner away, we know it's Troy Lake" -> `lowerthird: false` on people.right. The interviewer's tag stays.
- Reel 19 "It is about food on tables": the interviewer's tribute + "it's about helping people earn a living, getting food to tables". Reel 17 now starts on that line (60 s instead of 86).
- Tracker: bystander faces (40-70 px) in the aisle pulled the "left" crop onto the crowd; faces_at now drops faces under MIN_FACE_W = 100 px.
- Audio joins (Driven + Bumpers complaint, "like a CD that keeps jumping"): build_reel3 beds now crossfade (equal power, 80 ms, up to 120 ms read into trimmed material) and the cleanup chain runs once on the mixed voice. Join hole depth went from 27-41 dB to 4-15 dB. All 19 DFC plates rebuilt with it.
