# Color pipeline for the Rival reels (iPhone HLG + DJI Pocket 3, ffmpeg on the shop PC)

Date: 2026-11-20. Lane: color. Everything below was checked against the real clips in `C:/Users/Parts/My Drive/VIDEO/inbox` on this machine (ffmpeg 9.0.2 full build, i5-14500, Intel UHD 770, no dGPU). Test renders and contact sheets are in the session scratchpad under `colortest/` (temporary).

## 1. What actually went wrong in render one and render two

Diagnosis from ffprobe on the inbox clips:

- Every iPhone .MOV (IMG_2705 through IMG_4259) and the A263E7B4 .mp4 are HEVC Main 10, `yuv420p10le`, `color_range=tv`, `color_space=bt2020nc`, `color_transfer=arib-std-b67` (HLG), `color_primaries=bt2020`. Stream side data carries a `DOVI configuration record` with `dv_profile=8`, `dv_bl_signal_compatibility_id=4`, i.e. Dolby Vision Profile 8.4 with an HLG base layer and an RPU per frame. That is exactly what Apple documents and what Meta describes for iPhone uploads (Apple TN3145: https://developer.apple.com/documentation/technotes/tn3145-hdr-video-metadata ; Meta engineering, Nov 17 2025: https://engineering.fb.com/2025/11/17/ios/enhancing-hdr-on-instagram-for-ios-with-dolby-vision/ ).
- Every DJI Pocket 3 clip (Video_2626xx and dji_mimo) is HEVC Main 10, `yuv420p10le`, bt709/bt709/bt709, 59.94 fps, 77 to 80 Mbps. So the DJI is already SDR Rec.709 "Normal" profile, 10-bit. No tone map needed, just a dither down to 8-bit.
- IMG_9679.mov (720p) is 8-bit bt709: already SDR.

Both reel renderers (`tools/build_reel.py` and `tools/build_reel2.py`) do `format=yuv420p` with no colorspace conversion. That is the "naive" path: a 10-bit HLG / BT.2020 signal gets reinterpreted as 8-bit gamma 2.4 / BT.709 with the wrong YCbCr matrix and no tags fixed. Measured on IMG_4259: the naive frame is milky (mean luma lifted, 11 percent of pixels at or above 250 in the sky shot), the sky goes pale grey-blue, overall saturation drops to about 60 percent of the correct value, and because the bt2020nc matrix is decoded with bt709 coefficients the hue of reds and oranges skews. That is why render two looked "flat and phone-like", and why render one, which stacked `eq=saturation=1.08,colorbalance` on top of the hue-skewed signal, made the rust look neon while the rest still looked washed out. The output file also kept the HDR tags (`bt2020nc / arib-std-b67 / bt2020`) on 8-bit SDR pixels, so any player or Instagram's transcoder that honors tags applies a second conversion. Sources agreeing on the mechanism: https://dev.to/masonwritescode/ffmpeg-hdr-to-sdr-tone-mapping-that-doesnt-look-washed-out-2026-24ie , https://ffmpeg-cookbook.com/en/articles/hdr-to-sdr/ , https://jimmyhoke.net/wp/?p=412 (the author notes a TikTok upload looked "terrible" until the BT.709 tags were set).

## 2. The tone map tests (what works on this PC)

Timed on 10 s of 1080p30 iPhone HLG, libx264 veryfast:

| path | speed | result |
|---|---|---|
| naive `format=yuv420p` | 5.5x realtime | wrong (above) |
| zscale + tonemap (CPU) | 3.4x realtime | correct, tags come out bt709/bt709/bt709/tv |
| libplacebo via Vulkan on UHD 770 | 2.6x realtime | initialises fine, tags correct, but the frames are corrupt: magenta with shifted chroma planes, for HDR and for plain SDR pass-through, in yuv420p, yuv420p10le, nv12 (green), yuv444p, with and without `disable_multiplane=1`. Do not use on this driver. |
| tonemap_opencl (Intel OpenCL) | 1.3x realtime | correct image but leaves `color_space=bt2020nc` in the tags and is slower than CPU. Not worth it. |

Operator comparison on two clips (sunny truck selfie, shop interior), all with `desat=0`, numbers are mean luma 0-255 / percent of pixels clipped high:

- hable, npl=100: 136 / 0.02 percent. Deepest blue sky, strongest contrast, slightly dark, skin a bit heavy. Good "moody" option.
- mobius: 162 / 0.6 percent. Closest to how the phone shows the clip, natural skin, white shop walls stay white, flag reads. Best default.
- reinhard: 156 / 0.1 percent. Between the two, a touch lower contrast than mobius.
- hable with default desat (2): skin blows to white, 15 to 24 percent clipped. Never leave desat at default.
- direct `zscale=t=bt709` with no tonemap filter: cyan sky, 18 to 63 percent clipped. Do not do this.
- Lower npl (60) or `peak=4` with hable: brighter but starts clipping (2 to 4 percent). Not needed once mobius is the default.

Operator notes match the cookbook (hable keeps shadow and highlight detail but runs dark; mobius keeps in-range colors and contrast intact; reinhard brighter and flatter): https://ffmpeg-cookbook.com/en/articles/hdr-to-sdr/ . libplacebo's bt.2390 would be the broadcast-standard choice (https://www.mpegflow.com/topics/color/hdr-to-sdr-conversion) but it is off the table here until the Intel Vulkan path stops corrupting frames (candidate causes: Intel Windows driver + ffmpeg 9.0.2 Vulkan download; see trac #11229 https://trac.ffmpeg.org/ticket/11229 ). Re-test after a driver or ffmpeg update.

## 3. What Instagram does to the file

- Meta transcodes everything. HDR uploads (HLG or PQ) get an HDR rendition plus an SDR rendition for non-HDR devices; since Nov 2025 Instagram for iOS also keeps Dolby Vision 8.4 metadata in the AV1 rendition. Meta does not publish its SDR tone map, so an HDR upload means Meta decides how the SDR version looks. https://engineering.fb.com/2023/07/17/video-engineering/hdr-video-reels-meta/ and the Nov 2025 post above.
- The common "Reels look brighter / different after upload" complaints trace to (a) HDR source shown on SDR screens or tone mapped by Meta, (b) wrong color tags, (c) 3.5 to 5 Mbps re-encode crushing shadows and lifting mids, (d) comparing on a dim monitor vs a phone at full brightness. Fix list that keeps recurring: shoot or deliver SDR, 1080x1920 H.264 High 8-bit yuv420p, 10 to 16 Mbps, no Instagram filter on top of a graded clip, test to Close Friends first. https://www.lilachbullock.com/why-instagram-reels-look-brighter-than-original-video/ , https://thepostflow.com/post-production/post-production-workflows/export-settings-youtube-instagram-tiktok/ , https://renderio.dev/blogs/instagram-reels-video-format
- Banding in blue skies and smooth shop walls comes from the 8-bit downconvert plus Meta's low bitrate. Dither on the 10 to 8 bit step and a tiny amount of fine grain survive better than a clean gradient. https://www.shutterstock.com/blog/tutorial-reduce-visible-video-compression
- Decision: deliver SDR Rec.709 8-bit, tagged, and keep saturation and contrast slightly under what looks right on the desktop monitor. Jacob's phone will show it brighter and punchier than the PC.

## 4. Grading approach for this subject (rust red truck, steel shop, Wyoming sun)

Pro guidance that applies to this footage (Qazi & Co car grading, Jamie Fenn's SDR/HDR iPhone tutorial, the film-density write-ups):

- Correct first, look second. On SDR-converted phone footage, make small moves; SDR "does not take well to massive changes". Fenn's SDR node order: balance (small lift down, gamma up), contrast around a mid-grey pivot pushed too far and backed off, saturation last and minimal, and on HDR-derived clips turn on saturation compression as a safety net. https://www.youtube.com/watch?v=dfFOtymPIIs
- Car commercials use a "poppy film look" with highlights kept high and contrast kept in check; the grade is built around the product. https://thepostvillage.squarespace.com/blog/cars-commercial-vs-film-grading-davinci-resolve-17-tutorial
- Film density, the thing that reads as "expensive": saturated colors get slightly darker instead of brighter. Cheap video look = bright saturated colors. https://dvresolve.com/tutorial/adding-color-density-to-your-grade/ . In ffmpeg terms: do not raise `eq=saturation`; keep it at 0.92 to 1.0 after the tone map, and let the LUT (print-film style) add density.
- Blacks: lift the toe slightly (black point around 1 percent, not crushed, not milky) so Meta's compression has somewhere to go; roll highlights off (knee at about 0.75) instead of hard white.
- Warmth: a hair of warmth in the mids, not an orange push. Skin must stay skin; watch the fists and faces in the selfie clips. No teal-orange.
- Skies: Wyoming sky after mobius is already a deep blue; do not add blue, and a small desaturation of extreme blue helps banding.

LUT strategy. Apply the LUT at 30 to 45 percent by blending the LUT'd branch with the clean branch. ffmpeg `lut3d` has no strength option; `split` + `lut3d` + `blend=all_mode=normal:all_opacity=X` is the standard workaround and it works on this build (tested on a DJI clip; the 50 percent blend lands visibly half way). Shotcut thread on the idea: https://forum.shotcut.org/t/lut-intensity-or-opacity-strength/10519 . Rec.709-input (not log) LUTs to try:

- Luttie Kodak 2383 for Rec.709 (33-point, free for commercial work, dense blacks, cool shadows, warm highlights): https://luttie.app/luts/kodak-2383 . Luttie Portra 400 (softer contrast, warm skin): https://luttie.app/luts/portra-400 . Both expect normal Rec.709 video; the Resolve-bundled 2383 LUTs expect Cineon log and will crush and oversaturate on this footage.
- Joseph Carey free film looks, 77 LUTs with Rec.709 versions: https://josephcarey.com/luts/
- DJI's own Pocket 3 Rec.709 "Color Grading" LUT pack (v1.1, 2024-11-06, Rec.709 input), download from https://www.dji.com/osmo-pocket-3/downloads (the CDN refuses curl; download in a browser and drop the .cube files in VIDEO/tools/luts).
- Start with 2383 at 0.35. If skin goes brick, swap to Portra at 0.40.

## IMPLEMENT IN OUR STACK

Rule: convert every clip to SDR Rec.709 8-bit ONCE at the start of the per-clip chain (before fps, crop, zoom, xfade, captions), then grade in Rec.709, then tag the output. Never grade on the untagged naive signal again.

### Detection decision tree (per clip, ffprobe)

```
ffprobe -v error -select_streams v:0 -show_entries stream=pix_fmt,color_transfer,color_primaries,color_space,color_range:stream_side_data_list -of json "<clip>"
```

- `color_transfer` in {arib-std-b67, smpte2084} OR `color_primaries == bt2020` OR a `DOVI configuration record` side data -> HDR_HLG (iPhone) -> TONEMAP chain.
- `color_transfer == bt709` and 10-bit (`yuv420p10le`, DJI Normal / iPhone with HDR off on some builds) -> SDR10 -> `zscale=dither=error_diffusion,format=yuv420p` only.
- `color_transfer == bt709` and `yuv420p` -> SDR8 -> pass through, `format=yuv420p`.
- `color_transfer` unknown and `color_primaries` unknown -> treat as SDR8 but force tags with `setparams=color_primaries=bt709:color_trc=bt709:colorspace=bt709`.
- DJI D-Log M (if Jacob ever switches): tagged bt709 but flat; route through `lut3d` with the DJI "D-Log M to Rec.709 V1" cube at 100 percent BEFORE the grade, then continue as SDR.

### Filter graphs (copy-paste)

HDR iPhone -> SDR (default, natural):
```
zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=tonemap=mobius:desat=0,zscale=t=bt709:m=bt709:r=tv:dither=error_diffusion,format=yuv420p
```
Moody variant (deeper sky, more contrast, a touch dark): replace `tonemap=mobius` with `tonemap=hable`. Never drop `desat=0`. Never drop the `zscale=p=bt709` primaries step (that is the neon-saturation bug the guides warn about).

DJI 10-bit SDR -> 8-bit:
```
zscale=dither=error_diffusion,format=yuv420p
```

Natural "expensive" grade (apply after the conversion, same for both cameras, LUT path relative to cwd or escaped as 'C\:/...'):
```
curves=master='0/0.012 0.25/0.235 0.5/0.5 0.75/0.765 1/0.985',eq=saturation=0.95,split[a][b];[b]lut3d=file=luts/kodak2383_rec709.cube:interp=tetrahedral[l];[a][l]blend=all_mode=normal:all_opacity=0.35,noise=alls=3:allf=t+u,format=yuv420p
```
What each piece does: curves lifts the black point to about 1 percent and rolls the top 25 percent off (no hard white), saturation is pulled 5 percent (density comes from the LUT, not from eq), the LUT is mixed at 35 percent, `noise` adds fine temporal grain to fight banding after Meta's re-encode. Drop the warm `colorbalance` from the old GRADES; if warmth is wanted, `colortemperature=temperature=5900` is the honest tool, and only on shop-interior clips that look cold.

Full working example on this build (verified, output tags bt709/bt709/bt709/tv):
```
ffmpeg -i IMG_4259.MOV -vf "zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=tonemap=mobius:desat=0,zscale=t=bt709:m=bt709:r=tv:dither=error_diffusion,format=yuv420p,curves=master='0/0.012 0.25/0.235 0.5/0.5 0.75/0.765 1/0.985',eq=saturation=0.95,split[a][b];[b]lut3d=file=luts/kodak2383_rec709.cube[l];[a][l]blend=all_mode=normal:all_opacity=0.35,noise=alls=3:allf=t+u,format=yuv420p" -c:v libx264 -preset slow -crf 17 -maxrate 16M -bufsize 32M -profile:v high -level 4.2 -g 60 -pix_fmt yuv420p -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv -movflags +faststart -c:a aac -b:a 192k out.mp4
```
Export tags on the encoder line are belt and braces: zscale already sets them, the flags stop a later filter from losing them.

Where it goes in build_reel2.py: in the per-slot `vf` list, insert the conversion string as the FIRST element (before `fps=`, zoom crop, stab, grade), chosen by the probe above; replace the `GRADES` dict entries with the natural grade; add `-colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv` to the final encode. Same for build_reel.py. The xfade/concat stages then see uniform bt709 yuv420p inputs, which also removes a class of "timebase / format" surprises.

Verify after every render:
```
ffprobe -v error -select_streams v:0 -show_entries stream=pix_fmt,color_space,color_transfer,color_primaries,color_range -of default=nw=1 out.mp4
```
Expect `yuv420p bt709 bt709 bt709 tv`. Anything else is a bug.

### Optional Python match step (iPhone vs DJI, clip to clip)

OpenCV 5.1 is installed but without contrib, so no `cv2.xphoto`. A 40-line numpy version is enough: sample 12 frames per clip AFTER the SDR conversion, compute gray-world RGB gains (median of frames, exclude pixels with saturation above 0.6 or luma above 0.9) and mean luma; pick the hero clip as reference; for every other clip emit per-clip ffmpeg params `colorchannelmixer=rr=GR:gg=GG:bb=GB` (gains clamped to 0.9 to 1.1) and `eq=gamma=G` where `G = log(ref_meanY/255)/log(clip_meanY/255)` clamped to 0.85 to 1.15, and store them in the EDL slot as `"match": "..."`. The Reinhard Lab mean/std transfer is the stronger version if gray-world is not enough: https://pyimagesearch.com/2014/06/30/super-fast-color-transfer-images/ and `pip install python-color-transfer` (https://pypi.org/project/python-color-transfer). Keep the gains per clip, not per frame, so there is no flicker. Treat the DJI as the stable reference (fixed WB, 10-bit, 80 Mbps) and nudge the iPhone clips toward it.

### Preview habit

Before a full render, pull one frame per shot through the chain into a contact sheet (the `watch.py` sheet code already does the tiling) and look at skin, the white truck, and the sky. Numbers that flagged problems in testing: clipHi above 2 percent, mean saturation (HSV S) above about 115 on an outdoor shot, mean luma below 130 on a daylight shot.

## SETTINGS TO CHANGE ON CAMERA

iPhone (Settings > Camera > Record Video):
1. HDR Video: OFF. This is the single biggest simplifier: files become bt709, the tone map step disappears, the phone preview matches what Instagram shows on SDR screens, and Meta no longer picks the SDR look. Supported on iPhone 12 and later including the 16 line. Tradeoff: fewer highlight stops in the file, slightly less latitude; for Reels that is fine. https://support.apple.com/guide/iphone/change-video-recording-settings-iphc1827d32f/ios , https://www.lilachbullock.com/why-instagram-reels-look-brighter-than-original-video/ . If HDR stays on, nothing breaks: the pipeline above handles it, the cost is 30 percent slower renders and a look Claude chose rather than Apple.
2. Resolution: 4K 30 if storage allows (crop room for 9:16 punch-ins and stab, downscale hides phone sharpening), otherwise stay 1080p30. 30 fps, not 24: Reels play at 30 and the DJI is at 60 (clean 2:1 drop). (andyescapes transcript: https://www.youtube.com/watch?v=-Wxakox61Lg )
3. Exposure: dial -0.3 to -0.7 EV and turn on Settings > Camera > Preserve Settings > Exposure Adjustment so it sticks. iPhones expose bright by default; protecting highlights is most of the "cinematic" difference on SDR. (andyescapes)
4. Lock AE/AF (long press) before recording, especially in the shop, so white balance and exposure do not drift mid-shot. Use the 1x lens; never pinch-zoom between lenses. (andyescapes, Terry Shiu https://www.youtube.com/watch?v=UvBhNZ8UMuM )
5. Apple Log: only on 15 Pro / 16 Pro / 17 Pro, via Blackmagic Camera app, H.265 at max bitrate; needs a proper log-to-709 LUT (Stalman's or Apple's) before any grade. Great image, more work, large files. Not recommended until the SDR pipeline is boring. (Tyler Stalman https://www.youtube.com/watch?v=s5mr89YuiXk ; Blackmagic app settings in andyescapes). If he does: shutter angle 180, WB fixed around 5500 K outdoors, ND filter, stabilization on.
6. Format: High Efficiency (HEVC) is fine; the pipeline decodes it.

DJI Osmo Pocket 3:
1. Color: stay on Normal (what he is already shooting). It is bt709 10-bit, drops straight into the SDR chain, and the "10-bit Normal" files match the iPhone-with-HDR-off look best. D-Log M gives more latitude but then every DJI clip needs the DJI LUT first and a second look match; HLG on the DJI would recreate the iPhone HDR problem. (https://www.vitikoo.com/blogs/journal/osmo-pocket-3-normal-vs-d-log-m , DJI forum: D-Log M is a flat profile, not a LUT https://forum.dji.com/thread-305935-1-1.html )
2. Keep 10-bit (HEVC) on in Normal.
3. Frame rate: 4K60 only for intended slow-mo; 30 fps for talking shots so motion matches the iPhone. Shutter: 1/60 at 30 fps, 1/120 at 60 fps, which means ND filters outdoors in Wyoming sun (ND16/32 for daylight). Without ND the Pocket 3 goes to 1/1000 and the motion looks strobed next to the iPhone. (https://www.editorskeys.com/blogs/news/how-to-achieve-the-most-cinematic-look-with-the-dji-pocket-3 , https://omgadrian.beehiiv.com/p/the-only-osmo-pocket-3-settings-that-matter )
4. White balance: manual. 5600 K outdoors, 4000 to 4300 K under the shop's LED/fluorescent tubes (check one frame; the shop reads slightly green, so expect to push tint). Same rule on the iPhone via AE/AF lock.
5. Sharpness -1 or -2, noise reduction -1. The DJI's default sharpening is the main tell next to the iPhone. (omgadrian)
6. ISO cap 1600 in the shop; add light rather than ISO.

Matching rule of thumb: both cameras in SDR 709, both with fixed WB in the same scene, DJI as the reference, iPhone nudged by the match step. Then one shared grade.

## Top 5, in order

1. Put the HDR-to-SDR conversion into both renderers today: probe each clip, run the zscale + `tonemap=mobius:desat=0` chain on HLG sources, `zscale=dither=error_diffusion,format=yuv420p` on 10-bit SDR, and tag the output bt709/bt709/bt709/tv. This alone fixes "oversaturated neon rust" and "flat phone look", because both were the same untagged-HLG bug.
2. Have Jacob turn HDR Video off on the iPhone and lock AE/AF with -0.3 to -0.7 EV. Removes the problem at the source and makes his preview match the upload.
3. Replace the warm/punch `eq`+`colorbalance` grades with the natural chain: black point 1 percent, highlight roll-off, saturation 0.95, Rec.709 print LUT (Luttie 2383 or Portra) at 35 percent, fine grain. Keep saturation under what looks right on the PC monitor.
4. Export for Instagram as 1080x1920 H.264 High 8-bit, crf 17 with a 16 Mbps cap, tagged, dithered, and check tags with ffprobe after every render; test to Close Friends before the public post.
5. DJI: Normal 10-bit stays, add ND filters and fixed WB, sharpness down, and treat the DJI as the color reference with a per-clip gray-world/luma match for the iPhone clips. Re-test libplacebo (bt.2390 + peak detect) only after an Intel driver or ffmpeg update; on 9.0.2 with the current driver it corrupts frames.
