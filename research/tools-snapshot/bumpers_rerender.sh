#!/bin/bash
set -e
V="/c/Users/Parts/OneDrive - Elite Diesel Service/Desktop/VIDEO"; PY="$LOCALAPPDATA/Programs/Python/Python312/python.exe"
BIN="$LOCALAPPDATA/Microsoft/WinGet/Packages/Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/ffmpeg-9.0.2-full_build/bin"
cd "$V"; "$PY" -I out/gen_bumpers.py
cd tools/rival-reels
npx remotion render src/index.ts RivalReel out/bumpers-video.mp4 --props=out/bumpers.props.json --codec=h264 --crf=17 --log=error 2>&1 | tail -2
"$BIN/ffmpeg.exe" -y -v error -i out/bumpers-video.mp4 -i public/plate.mp4 -map 0:v:0 -map 1:a:0 \
  -vf "unsharp=5:5:0.4:3:3:0.0,format=yuv420p,setparams=color_primaries=bt709:color_trc=bt709:colorspace=bt709:range=tv" \
  -c:v libx264 -preset slow -profile:v high -level 4.2 -crf 17 -maxrate 16M -bufsize 32M -g 30 -keyint_min 30 -sc_threshold 0 -bf 2 \
  -x264-params "aq-mode=3:aq-strength=0.9:psy-rd=1.0,0.15:deblock=-1,-1:no-open-gop=1:colorprim=bt709:transfer=bt709:colormatrix=bt709" \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv -c:a aac -b:a 192k -shortest -movflags +faststart out/bumpers-final.mp4
cd "$V"; "$PY" -I tools/smooth_check.py tools/rival-reels/out/bumpers-final.mp4 2>&1 | grep "==\|held\|spikes"
"$BIN/ffmpeg.exe" -y -v error -i tools/rival-reels/out/bumpers-final.mp4 -vf "fps=2,scale=270:480,tile=8x8:padding=2:margin=2" -frames:v 1 -update 1 tools/rival-reels/out/bumpers-sheet.png
echo RERENDER DONE
