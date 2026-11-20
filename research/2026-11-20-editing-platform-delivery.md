# Platform delivery: how a finished reel should be encoded, framed and uploaded (2026-11-20)

Lane: platform delivery (Instagram Reels first, TikTok / YouTube Shorts / Facebook Reels second).
Renderer context: ffmpeg 9.0.2 full build (libx264, libx265, h264_qsv, libzimg, libplacebo, libvmaf all compiled in), 1080x1920 30 fps, currently libx264 crf 17 preset slow yuv420p high, AAC 192k, faststart. Sources: iPhone HEVC and DJI Osmo Pocket 3. Upload path: Google Drive (mirror) to phone to Instagram app.

## 0. The headline finding (verified on disk, not from the web)

Every iPhone clip in My Drive/VIDEO/inbox probes as HEVC Main 10, yuv420p10le, color_space=bt2020nc, color_transfer=arib-std-b67 (HLG), color_primaries=bt2020. The DJI clips are bt709 10-bit (SDR, fine).

The finished reel that went out, "2026-11-20 Harley Trade - POST THIS.mp4", probes as h264 High, yuv420p, color_space=bt2020nc, color_transfer=arib-std-b67, color_primaries=bt2020. build_reel2.py does `scale,crop,format=yuv420p` and never converts the transfer curve, so libx264 received HLG code values, dropped them to 8-bit, and ffmpeg copied the HDR tags onto an SDR-looking file. That is the textbook cause of "gray, flat, washed out, wrong reds" after upload: Instagram either tone-maps a file it thinks is HLG (dulls it further) or an SDR player ignores the tags and shows the raw HLG curve (gray, low contrast). The Rival lyric reel renders went through the same path. The lettering complaint is partly the same thing (yellow 0xF8D000 captions drawn into an HLG-tagged frame get re-interpreted too) and partly thin strokes at Instagram's 4 to 6 Mbps output.

I tested the fix on IMG_3773.MOV: a zscale linear-light tone map (hable, desat=0, npl=100) to BT.709 took 0.9 s for 3 s of footage; the output frame shows the orange door post, yellow forklift and red forks at proper saturation where the pass-through frame is milky gray. Sources for why this happens: ffmpeg-micro HDR to SDR note (https://www.ffmpeg-micro.com/blog/ffmpeg-hdr-to-sdr-stop-iphone-uploads-coming-out-gray), Mux on color tags (https://www.mux.com/blog/your-browser-and-my-browser-see-different-colors).

## 1. Instagram Reels ingest in 2026

Official spec (Meta Graph API reel media doc, https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/media): MP4 or MOV, moov atom first, no edit lists; H.264 or HEVC, progressive, closed GOP, 4:2:0; 23 to 60 fps; max width 1920; VBR up to 25 Mbps; AAC up to 48 kHz, mono or stereo, 128 kbps; 3 s to 15 min; 300 MB. No HDR or color space language for video. Meta ads guide (https://www.facebook.com/business/ads-guide/update/video/instagram-reels): 9:16, H.264, square pixels, fixed frame rate, stereo AAC 128 kbps+, safe margins 14% top / 35% bottom / 6% sides.

What the re-encode does (measured, not guessed): the only controlled test found (lpic.cc, March to April 2026, same 12 Mbps 1080x1920 H.264 file via MD5-identical uploads, three runs each, https://lpic.cc/en/blog/meta-reels-threads-ig-quality-test) got Reels back at 5.8 Mbps / SSIM 0.951 from the iPhone app, 5.4 Mbps / 0.948 from Meta Business Suite, 4.6 Mbps / 0.937 from desktop web, 3.4 Mbps / 0.912 from a Buffer scheduler. For Stories, "Upload at highest quality" ON vs default was 4.8 vs 3.1 Mbps (SSIM 0.942 vs 0.918). Android flagship hardware encoders were within 5% of iPhone; budget Androids lost another 10 to 15%. Output is always yuv420p 8-bit. The author notes banding in sky gradients appears around SSIM 0.92 and that HDR10 Stories were tone-mapped to SDR server side.

Takeaways:
- Instagram's output budget is roughly 4 to 6 Mbps. Anything you give it above about 10 to 16 Mbps is wasted bits; the gain from 16 to 30 Mbps is nil, and the YouTube "6 reasons" transcript (Stanislav Rassokhin, https://www.youtube.com/watch?v=tfSsrs1wv_E) makes the same point: judge bitrate, not file size, and Instagram's budget per frame is fixed, so 60 fps halves per-frame data. Deliver 30 fps for shop footage. Mid-2025 Instagram started honoring 24 and 60 fps natively (Matt Johnson transcripts), so 30 fps masters play as 30.
- HDR: Meta says the Edits app can export SDR or HDR and "Instagram will prioritize playback up to 2K, HDR, 60 fps" when shared straight from Edits (https://creators.instagram.com/blog/best-camera-settings-instagram-reels). MakeHDR's August 2026 tests say HDR survives only from the iPhone app and is stripped on web upload (https://makehdr.com/how-to/how-to-post-hdr-on-instagram). Croma reported Meta adding Dolby Vision passthrough on iOS in 2025. Conclusion for us: deliver SDR BT.709. We cannot author real HLG from a mixed iPhone + DJI SDR timeline inside ffmpeg reliably, Android viewers get inconsistent results, and a half-HDR file is exactly what produced the gray reel. SDR done right looks correct on every phone.
- Color tags: always write `-color_primaries bt709 -color_trc bt709 -colorspace bt709 -color_range tv` AND actually convert the pixels. Tagging alone relabels gray as gray (ffmpeg-micro). Keep limited (tv) range; converting to full range invites double conversion (VideoHelp thread). YouTube explicitly converts full range to limited and BT.2020-without-HDR to 8-bit BT.709, so tag honestly (https://support.google.com/youtube/answer/1722171).
- Known "colors shift after upload" causes, in order of likelihood for us: (1) HLG source not tone-mapped (our case); (2) missing or mismatched bt709/bt601 tags so the player guesses (Mux: Safari assumes 601, Chrome/Firefox 709 for HD); (3) DaVinci/Premiere gamma tag mismatch (Rassokhin mistake 6); (4) 4:2:0 chroma bleed on saturated red or yellow lettering, which no setting fixes, only bolder strokes and an outline.

## 2. The export recipe

Principles, with sources: CRF is better than 2-pass for quality-per-file because size is not our constraint (300 MB cap, 60 s at 16 Mbps is 120 MB). Add a VBV cap (maxrate/bufsize) so a grain-heavy shot cannot spike past what the uploader accepts cleanly. Closed GOP of 1 second (keyint 30 at 30 fps, no scene cut keyframes) matches Meta's "closed GOP" and YouTube's "GOP half the frame rate" guidance and gives Instagram's transcoder regular clean I-frames. High profile level 4.2, 2 B-frames (YouTube rec). yuv420p is non-negotiable (ffmpeg-micro Reels preset, https://www.ffmpeg-micro.com/blog/best-video-settings-for-instagram-reels-bitrate-resolution-ffmpeg-preset). x264 tune: no `tune film` or `tune grain` (grain tune inflates bitrate and adds fake grain at slow presets per Doom9; film tune lowers deblock and raises psy which Instagram's second encode then smears). Use aq-mode 3 at strength 0.8 to 0.9 for dark shop interiors (lowers QP near black, reduces banding/blocking in shadows, silentaperture x264 guide https://silentaperture.gitlab.io/mdbook-guide/encoding/x264.html), psy-rd 1.0:0.15 (default psy, tiny psy-trellis to keep texture without ringing on text), deblock -1:-1 (slightly less smoothing so edges of lettering stay crisp). Banding: run `deband` at light thresholds on the SDR frame plus a very light temporal `noise` (alls=3 to 4) so skies and gray shop walls dither instead of stepping; the lpic test shows gradient banding is the first thing Instagram's 5 Mbps encode exposes. Sharpen lightly before upload (unsharp 5:5:0.5) because the server transcode softens; stronger than about 0.8 produces halos that compress badly (Creator Lane: sharpening is not a color fix, https://creatorlanehq.com/blog/instagram-reels-blurry-after-upload). Tested on this machine: the full chain below runs 10 s of HLG iPhone footage in 16 s at preset slow and lands around 15 to 17 Mbps at crf 17; use crf 18 if files feel big.

### Final Instagram command (single source clip, HLG iPhone in, SDR BT.709 out)

```
ffmpeg -y -i IN.MOV ^
 -vf "zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p,scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920,setsar=1,unsharp=5:5:0.5:3:3:0.0,deband=1thr=0.02:2thr=0.02:3thr=0.02:range=16:blur=1,noise=alls=3:allf=t,fps=30,format=yuv420p" ^
 -c:v libx264 -preset slow -crf 17 -maxrate 16M -bufsize 32M -profile:v high -level 4.2 -pix_fmt yuv420p ^
 -g 30 -keyint_min 30 -sc_threshold 0 -bf 2 ^
 -x264-params "aq-mode=3:aq-strength=0.9:psy-rd=1.0,0.15:deblock=-1,-1:no-open-gop=1" ^
 -color_primaries bt709 -color_trc bt709 -colorspace bt709 -color_range tv ^
 -af "loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo" ^
 -c:a aac -b:a 192k -ar 48000 -ac 2 -movflags +faststart OUT-IG.mp4
```

Rules for build_reel2.py: run the zscale tone map block on each iPhone slot (branch on ffprobe color_transfer == arib-std-b67; DJI bt709 clips skip it) BEFORE scale/crop/grade/captions, so grades and the yellow captions are applied in BT.709. Keep intermediates 10-bit or at least do the tone map in the slot pass, not after concat. Put the four color tags on the slot encodes, the NOCAP encode and the final caption burn. The GPU path (`-init_hw_device vulkan`, `format=yuv420p10,hwupload,libplacebo=tonemapping=bt.2390:colorspace=bt709:color_primaries=bt709:color_trc=bt709:range=tv:format=yuv420p,hwdownload,format=yuv420p`) also works on the UHD 770 (note `format=yuv420p` must be inside the libplacebo filter or hwdownload errors); zscale is fast enough and deterministic, so prefer it.

### TikTok variant
Same filter chain. Change only: `-crf 18 -maxrate 12M -bufsize 24M -level 4.1`, audio `-b:a 192k`. TikTok recompresses to roughly 1 to 2 Mbps and tone-maps HDR badly, so SDR BT.709 again (ffmpeg-micro TikTok spec https://www.ffmpeg-micro.com/blog/tiktok-video-specs-that-survive-the-upload-and-the-posting-api). 30 fps.

### YouTube Shorts variant
Shorts cap at 1080p per Google (https://support.google.com/youtube/answer/10059070: "maximum resolution of 1080p", up to 3 minutes), so the 4K upscale trick for VP9 does not apply to Shorts; it only helps long-form 16:9. Deliver the same 1080x1920 master at `-crf 16 -maxrate 20M -bufsize 40M` (YouTube's 1080p SDR reference is 8 Mbps, 12 at 60 fps, and it keeps more than Instagram does), audio `-b:a 256k`. Do not upscale.

### Facebook Reels
Crosspost from the Instagram share sheet; same file. Meta's FB Reels API wants AAC-LC 48 kHz stereo 128 kbps+, which the master already satisfies.

## 3. Safe zones (1080x1920), text diagram

Instagram Reels, Meta ads guide margins (14 / 35 / 6 percent) plus the measured button column (Mark Studios, https://www.markstudios.com/tools/instagram-reels-safe-zone):

```
y=0     +--------------------------------------------+
        |  TOP 269 px: status bar, "Reels" header     |
y=269   +--------------------------------------------+
        | 65 |                              | 65 |    |
        | px |   SAFE 950 x 979             | px |    |
        |    |   (x 65..1015, y 269..1248)  |    |    |
        |    |   keep text LEFT of x=880    |    |    |
        |    |   once y > 970 (button col)  |    |    |
y=970   |    |                       +------+    |    |
        |    |                       | like |    |    |   button column
        |    |                       | cmnt | x 880..970
        |    |                       | shre | y 970..1670
y=1248  +----+-----------------------+      +----+    |
        |  BOTTOM 672 px: caption, handle, audio tile  |
        |  (1700..1712 progress bar, 1740..1870 tabs)  |
y=1920  +--------------------------------------------+
```

Crops to design for: feed/explore shows 4:5 = center 1080x1350 (285 px trimmed top and bottom); profile grid since Jan 2025 is 3:4 = center 1080x1440 (240 px trimmed each end), and the Reels tab shows the full 9:16 (Hootsuite / Later cover guides). So the hook text and the hero subject belong inside y 285 to 1635, and the cover frame's title inside y 240 to 1680, horizontally centered. Pick the cover from the video at a frame with the truck large and no caption, or upload a dedicated 1080x1920 cover with the title in the middle 1080x1440; preview with "Crop profile image" before posting.

TikTok (ffmpeg-micro mid-2026 measurement; Revid and Clipzi give wider numbers): top 108 to 240 px, bottom 320 to 660 px (grows with caption length), left 60 to 120 px, right 120 to 140 px. The right column is taller and the bottom caption block is bigger than Instagram's, so keep TikTok text above y=1260 and left of x=940.

YouTube Shorts (Google vertical ad template reading, repeated by Zeely, Kreatli, Clipzi): top 288, bottom 672, left 48, right 192. Shorts covers more of the right side (subscribe button and channel chip) than Instagram, so Shorts text should sit left of x=888. A single conservative template that clears all three: top 290, bottom 680, left 120, right 200 (Clipzi, https://clipzi.app/en/blog/shorts-tiktok-reels-safe-zones), which is a 760x950 box. That is tight; use it only for the hook line and brand lockup, and let b-roll fill the frame.

Lettering rules that survive the transcode: minimum 44 px cap height for small text, 72 px+ for anything that must be read in the feed, heavy weights (Anton, Oswald Bold), 3 to 4 px dark outline or soft shadow on yellow/red text, no thin strokes, no 1 px drop shadows. Saturated pure red text on a dark background bleeds at 4:2:0; add a thin lighter outline or use the Coyote tan.

## 4. Upload path and phone settings

- Instagram app: Profile > menu > "Your app and media" > Media quality > "Upload at highest quality" ON (Instagram Help, https://help.instagram.com/1038071743007909; on Android the screen is "Data usage and media quality"). Data Saver OFF. Measured effect: about 1.5x the output bitrate (lpic Stories test).
- Strong Wi-Fi, do not background the app or switch networks during upload; the app downgrades the encode on a weak link (Rassokhin, Creator Lane).
- Google Drive stores and serves the original bytes (Compresto, Filerev); only the in-browser preview player is compressed. On iPhone use Drive > three dots > "Send a copy" > "Save video" so the exact MP4 lands in Photos; do NOT screen-record, AirDrop-to-self is fine, and never send the file through Messages, WhatsApp or email, which re-encode (MakeHDR, Creator Lane). Mirror mode means Claude writes the file and the phone pulls the original.
- iPhone vs Android: flagship Androids are within 5% of iPhone; the app itself does a client-side encode before upload, so the "highest quality" toggle matters more on Android.
- Desktop: Meta Business Suite upload measured 5.4 Mbps vs 5.8 from the iPhone app (both better than instagram.com web at 4.6); third-party schedulers were worst (3.4). So phone app or Business Suite, never a scheduler, for anything we care about.
- The Edits app route: Meta says Reels shared directly from Edits get "priority processing" and playback prioritized up to 2K/HDR/60. All three Matt Johnson transcripts recommend importing the finished master into Edits, exporting 4K, and tapping the Instagram button (not Download). The 4K step just raises the bitrate Edits hands over; our master is already SDR 1080p at 16 Mbps, so try Edits export at 1080p/30 SDR once as an A/B and keep it only if the posted reel measures better.
- HEVC vs H.264 upload: Meta accepts both; H.264 High 8-bit is the cleanest input for its transcoder and removes a client-side conversion on Android. Stay on H.264.

## 5. Audio delivery

- Target -14 LUFS integrated, true peak -1 to -1.5 dBTP; Instagram normalizes DOWN toward about -14 and will not raise quiet audio (Cutscore, https://cutscore.io/blog/loudness-for-instagram-reels; AudioForgePro). Our loudnorm I=-14 TP=-1.5 LRA=11 is right; keep it after amix and before the aresample 48000 fix.
- Stereo, 48 kHz, AAC-LC 192k in the master (Instagram serves about 128k; TikTok 128 to 192k; YouTube 384k stereo). Keep the mix mono-compatible (phones collapse to one speaker).
- Music added in-app: the Reels editor has separate sliders for original audio and the library track; start music at 20 to 30% under speech, 100% for montage reels (Veed, Hollyland). Adding the song inside Instagram keeps the song page attribution and avoids copyright muting; music burned into the upload gets detected and the whole reel can be muted or blocked regionally (Soundstripe). Creator (not business) accounts see the full licensed library; business accounts get Meta Sound Collection only (Foximusic, Ootto). Keep posting the SILENT/NOCAP-style master with a -14 LUFS dialogue bed and add the track in-app, as already planned.

## 6. Cross-posting summary

Instagram: 1080x1920, 30 fps, 10 to 16 Mbps H.264 High 8-bit BT.709, 192k AAC. TikTok: same, 8 to 12 Mbps is plenty, bigger bottom and right dead zones, 10 min max, HD toggle on at post time. Shorts: same master, 1080p is the ceiling, 3 min max, keep right 192 px clear; 4K upscaling buys nothing on Shorts (Google) and even on long-form the VP9 gain is small on a phone (Everpop). Facebook Reels: crosspost from the IG share sheet.

## 7. Verification loop Claude can run

1. Get the served file: Jacob opens the posted reel > share > Download (saves the transcoded MP4 to Photos; it syncs to Drive inbox), or Claude runs `yt-dlp.exe "https://www.instagram.com/reel/<id>/"` (yt-dlp is installed in the WinGet packages folder; append `?utm_source=ig_embed` to get the 1080x1920 version instead of the 1080x1350 feed copy, per lpic). Fallback: Chrome DevTools, Network, filter .mp4.
2. Probe: `ffprobe -show_entries stream=codec_name,width,height,pix_fmt,color_space,color_transfer,bit_rate,r_frame_rate` on the download. Expect h264 1080x1920 yuv420p bt709 4 to 6 Mbps.
3. Score against the master (both already 1080x1920 30 fps; align start, lanczos scale if not):
```
ffmpeg -i served.mp4 -i master.mp4 -lavfi "[0:v]settb=AVTB,setpts=PTS-STARTPTS[d];[1:v]settb=AVTB,setpts=PTS-STARTPTS[r];[d][r]libvmaf=feature=name=float_ssim|name=psnr:log_fmt=json:log_path=vmaf.json" -f null -
```
Tested here against a simulated 4.5 Mbps re-encode of the new recipe: VMAF 94.4, SSIM 0.995, PSNR-Y 39.4. Real Instagram numbers will be lower (lpic saw SSIM 0.95 at best); log each posted reel's SSIM/VMAF and bitrate in a table and change one export variable at a time.
4. Visual check: pull the same timestamp from both files (`-ss T -frames:v 1`) and Read the two JPGs; look at the sky gradient, the darkest shop corner, and the caption edges, in that order.
5. For a screenshot from Jacob instead of the file: screenshot is the phone's display (device tone mapping, brightness), so only use it for color sanity (is the red red), not for sharpness.

## Upload checklist for Jacob's phone

1. Instagram > Profile > menu > Media quality > "Upload at highest quality" ON; Data Saver OFF. One-time.
2. On strong Wi-Fi. Phone not in Low Power Mode.
3. Open the "<Reel> - completed <date>" folder in Drive, long-press the POST THIS mp4 > Send a copy > Save video. Do not play-and-screen-record, do not forward through Messages.
4. Instagram > + > Reel > pick the saved file from Recents. Do not apply IG filters or "Enhance". Do not trim in-app (forces a client re-encode).
5. Add the song inside Instagram; set original audio 100, music 20 to 30 under talking, music 100 on montage.
6. Cover: pick a frame with the truck centered and no text, or "Add from camera roll" with the title inside the middle 1080x1440. Tap "Crop profile image" and check the 3:4 grid preview.
7. Post, keep the app open until the progress bar finishes, then wait 10 to 15 minutes before judging; HD versions finish processing after publish.
8. Share > Download the posted reel, it lands back in Drive, Claude scores it.
9. Optional A/B once: import the same master into Edits, export 1080p/30 SDR, share via the Instagram button; compare bitrate and SSIM against step 8.

## Prioritized top 5

1. Tone-map every iPhone HLG clip to SDR BT.709 (zscale chain) inside build_reel2.py before grade and captions, and tag bt709/tv on every encode. This is the color complaint. Re-render Harley Trade and the Rival lyric reel before anything else is posted.
2. Lock the export recipe above: crf 17 to 18, maxrate 16M, closed 1 s GOP, High 4.2, aq-mode 3, deband plus light grain, unsharp 0.5. Stop at 30 fps.
3. Lettering: Anton/Oswald heavy weights at 72 px+ for feed-read text, 44 px floor, outline or shadow on yellow and red, everything inside x 65 to 880 and y 285 to 1248; cover title inside the middle 1080x1440.
4. Phone side: "Upload at highest quality" ON, Save-video from Drive (no messaging apps), no in-app trim or filters, song added in-app, wait for processing. Business Suite is the only acceptable desktop route; never a scheduler.
5. Close the loop: download each posted reel, ffprobe plus libvmaf SSIM/VMAF against the master, log it, and change one variable per post. First experiment: Edits-app share vs direct upload of the same master.

## Sources (all fetched 2026-11-20)
- Meta Graph API reel specs: https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/media
- Meta ads guide Instagram Reels (safe margins 14/35/6): https://www.facebook.com/business/ads-guide/update/video/instagram-reels
- Instagram Help, media quality setting: https://help.instagram.com/1038071743007909
- Meta Creators blog, Edits export and playback prioritization: https://creators.instagram.com/blog/best-camera-settings-instagram-reels
- lpic.cc upload path SSIM test (4 Meta paths, March to April 2026): https://lpic.cc/en/blog/meta-reels-threads-ig-quality-test
- MakeHDR HDR on Instagram tests (Aug 2026): https://makehdr.com/how-to/how-to-post-hdr-on-instagram
- ffmpeg-micro, HDR to SDR for iPhone uploads: https://www.ffmpeg-micro.com/blog/ffmpeg-hdr-to-sdr-stop-iphone-uploads-coming-out-gray
- ffmpeg-micro, Reels preset: https://www.ffmpeg-micro.com/blog/best-video-settings-for-instagram-reels-bitrate-resolution-ffmpeg-preset
- ffmpeg-micro, TikTok specs and safe zone: https://www.ffmpeg-micro.com/blog/tiktok-video-specs-that-survive-the-upload-and-the-posting-api
- Mux, color tags and browser behavior: https://www.mux.com/blog/your-browser-and-my-browser-see-different-colors
- Mark Studios safe zone measurements: https://www.markstudios.com/tools/instagram-reels-safe-zone
- Clipzi combined Reels/TikTok/Shorts safe zones: https://clipzi.app/en/blog/shorts-tiktok-reels-safe-zones
- Kreatli and Filmscribe Reels overlays: https://kreatli.com/guides/instagram-reels-safe-zone , https://filmscribe.ai/en/tools/instagram-reels-safe-zone
- YouTube recommended upload encoding: https://support.google.com/youtube/answer/1722171
- YouTube Shorts requirements (1080p max, 3 min): https://support.google.com/youtube/answer/10059070
- x264 settings guide (aq-mode 3, deblock, psy): https://silentaperture.gitlab.io/mdbook-guide/encoding/x264.html
- Doom9 on tune grain cost: https://forum.doom9.org/archive/index.php/t-175735.html
- Cutscore loudness for Reels: https://cutscore.io/blog/loudness-for-instagram-reels
- Soundstripe / Foximusic / Ootto on music licensing and muting: https://www.soundstripe.com/blogs/how-to-add-music-to-instagram-posts , https://www.foximusic.com/blog/instagram-reels-music-copyright-legal-guide/ , https://www.ootto.ai/blog/instagram-business-account-music-reels
- Veed / Hollyland on in-app music sliders: https://www.veed.io/learn/how-to-add-music-to-instagram-posts , https://www.hollyland.com/blog/tips/keep-original-audio-on-reels-with-music
- Creator Lane, blurry after upload: https://creatorlanehq.com/blog/instagram-reels-blurry-after-upload
- Google Drive stores originals: https://compresto.app/blog/compress-video-for-google-drive
- Grid 3:4 and cover guidance: https://blog.hootsuite.com/instagram-reels-cover/ , https://later.com/blog/instagram-reels-cover-photo/
- VMAF/SSIM with ffmpeg: https://github.com/stoyanovgeorge/ffmpeg/wiki/How-to-Compare-Video , https://github.com/slhck/ffmpeg-quality-metrics
- YouTube transcripts in scratchpad: Rassokhin "6 Reasons Your Reels Pixelated" (tfSsrs1wv_E); Matt Johnson Premiere (4rG_ZxpjIKs), Resolve (_Gh1dhb9jGk), Final Cut (752eo20M1lk) 2026 export guides.
