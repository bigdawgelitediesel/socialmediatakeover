#!/bin/bash
# Move Bumpers giveaway (IMG_4259): plate -> whisper on plate -> cutout -> face track -> props -> Remotion -> mux -> QA
set -e
V="/c/Users/Parts/OneDrive - Elite Diesel Service/Desktop/VIDEO"; PY="$LOCALAPPDATA/Programs/Python/Python312/python.exe"
BIN="$LOCALAPPDATA/Microsoft/WinGet/Packages/Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/ffmpeg-9.0.2-full_build/bin"
cd "$V"
cp -f out/renders/bumpers-plate-NOCAP.mp4 tools/rival-reels/public/plate.mp4
echo "== whisper on plate"; "$PY" -I tools/watch.py tools/rival-reels/public/plate.mp4 --out out/bumpers-watch --model small > out/bumpers-watch.log 2>&1
mv -f out/bumpers-watch/plate out/bumpers-watch/bumpers-plate-NOCAP 2>/dev/null || true
echo "== matte"; "$PY" -I tools/matte.py tools/rival-reels/public/plate.mp4 tools/rival-reels/public/cutout.webm | tail -1
echo "== face"; "$PY" -I tools/facetrack.py tools/rival-reels/public/plate.mp4 tools/rival-reels/out/bumpers.face.json 2>/dev/null
echo "== props"; "$PY" -I out/gen_bumpers.py
cd tools/rival-reels
echo "== render"; npx remotion render src/index.ts RivalReel out/bumpers-video.mp4 --props=out/bumpers.props.json --codec=h264 --crf=17 --log=warn 2>&1 | grep -v "Rendered\|Bundling\|Encoded" | tail -5
echo "== mux"
"$BIN/ffmpeg.exe" -y -v error -i out/bumpers-video.mp4 -i public/plate.mp4 -map 0:v:0 -map 1:a:0 \
  -vf "unsharp=5:5:0.4:3:3:0.0,format=yuv420p,setparams=color_primaries=bt709:color_trc=bt709:colorspace=bt709:range=tv" \
  -c:v libx264 -preset slow -profile:v high -level 4.2 -crf 17 -maxrate 16M -bufsize 32M -g 30 -keyint_min 30 -sc_threshold 0 -bf 2 \
  -x264-params "aq-mode=3:aq-strength=0.9:psy-rd=1.0,0.15:deblock=-1,-1:no-open-gop=1:colorprim=bt709:transfer=bt709:colormatrix=bt709" \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv \
  -c:a aac -b:a 192k -shortest -movflags +faststart out/bumpers-final.mp4
cd "$V"; echo "== QA"; "$PY" -I tools/smooth_check.py tools/rival-reels/out/bumpers-final.mp4 2>&1 | grep "==\|held\|spikes"
"$BIN/ffprobe.exe" -v error -select_streams v:0 -show_entries stream=pix_fmt,color_range,color_space,color_transfer,color_primaries,duration -of csv=p=0 tools/rival-reels/out/bumpers-final.mp4
"$BIN/ffmpeg.exe" -y -v error -i tools/rival-reels/out/bumpers-final.mp4 -vf "fps=2,scale=270:480,tile=8x8:padding=2:margin=2" -frames:v 1 -update 1 tools/rival-reels/out/bumpers-sheet.png
echo "PIPELINE DONE"
