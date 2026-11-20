# Motion, speed ramps and transitions for @elcoyotediesel Reels
Research lane: MOTION. Date: 2026-11-20. Target stack: ffmpeg 9.0.2 (gyan full build), Python 3.12 + OpenCV + numpy, i5-14500, UHD 770 iGPU (QuickSync + Vulkan), no dGPU.
Everything in IMPLEMENT was rendered and checked on this PC today on synthetic 1080x1920 clips (scratch folder motiontest). Render costs quoted are measured, not guessed.

## 1. What the viral car-edit tutorials actually do (transcript extraction)

Matt Loui, Viral Speed Ramp (CapCut, 219k views) https://www.youtube.com/watch?v=_e0Pk65yPg8
- Beat drop must land inside the first 2 to 3 s; trim the song so the ramp-up is only a couple of seconds.
- Shot order wide to close. Stabilize with "minimum crop" before ramping.
- Curve: preset "Flash in", drag first point to 10x, delete the second point, drag the curve out for a softer ramp. Duplicate the clip, reverse it, and NOTE: CapCut does not mirror the speed curve on reverse; re-draw it so the pair reads fast-in, slow, slow, fast-out (yo-yo / rebound). Compound clips to exceed the 10x cap.
- Match motion direction across the cut (track-in into track-in, left-right into left-right). This is the single biggest "smooth as butter" factor.
- Motion blur: 100 is too much, default to 35; drop to 12 on shots with fine detail (chandelier, chrome). Blur produces a black edge on fast motion; scale the clip in a couple percent and apply the same percent to the matching clip.
- Deep whoosh SFX (not high pitched) on each ramp, pulled down from 0 dB, with reverb. Camera-shutter white flash exactly on the slow point.

Ka Production, Speed Ramp in CapCut (880k) https://www.youtube.com/watch?v=_77hOByZFA4
- Shooting rule: phone "glued" to the hands and never stop moving; one continuous move per clip (left to right in one go). Stop-start footage cannot be ramped.
- Curve: custom, pull the centre point down and both ends up: fast, slow, fast. Delete unused points. The slow point goes "wherever suits the clip", not necessarily centre. "Smooth slow motion: better quality" always on (optical flow).
- Export first, re-import, then motion blur 10 to 20 (used 13-14), blend about 50, times 2x. Applying blur in the same project "gets messy".

SHAILESH, Smooth Slow Reverse Car Edit (994k) https://www.youtube.com/watch?v=N9j46zUiN8Y
- Auto beats, delete every beat before the drop. Each beat interval holds TWO clips: the clip with a two-point curve (top about 6x, up to 10x on long clips; bottom 0.3x to 0.4x) then its duplicate, reversed, with the curve inverted (0.3x bottom, 6-10x top). Both halves fit inside one beat. Optical flow "better quality" on both.
- Freeze-frame cutout overlay about 0.4 s long slides in from off-screen with a hand-drawn graph (not linear). Layer order so the new cutout sits on top.

Adobe Simplified, Smooth Movement Car Edit (AE, 256k) https://www.youtube.com/watch?v=H7sKE4l9hP8
- 1080x1920 at 59.94 fps. Marker on every beat. Time remap, keyframes copied beat to beat so the clip oscillates. Easy Ease on everything, then ONE bezier applied to every keyframe in the piece: cubic-bezier(0.6, 0, 0.4, 1). "Keep this curve in mind, it is our secret sauce."
- The peak of the speed graph (the fastest moment) is the thing you align to the beat marker.
- Reveal: roto the car (feather 15), scale 0 to 100 with the same bezier, motion blur on; background comes in behind with Gradient Wipe softness 40, completion 100 to 0. Alternate clips use position (slide from off-screen) instead of scale.

MR Rahul, AE-like Car Edit in CapCut (223k) https://www.youtube.com/watch?v=29c88t_WVW4
- Feathered inverted linear mask that slides across the frame between keyframes (a mask wipe), freeze frames pushed to overlays, small rotate plus zoom keyframes on every clip with the "Flow 2" / "Quad in" graphs, circle mask "ring" reveal, "Pull in / Pull out" movement transitions, speed presets Hero and Montage, motion blur 100 both directions 4x, sharpen 40, clarity 10, vignette.

Zeven 7, Keyframe Mastery (928k) https://www.youtube.com/watch?v=fKNDlT5JbTY
- Keyframe distance is speed. Families: in (ease, quad, cubic), out, ease (quad/cubic/circular), rebound. Bounce = repeated keyframes every 20 frames with decaying curve height and the left bezier handle collapsed.

Common thread: every move is eased (never linear), the slow point or the speed peak is pinned to a beat, direction is matched across cuts, motion blur is added last and kept moderate, and whooshes sell it.

## 2. Research findings

Speed ramp physics
- Slowest frame goes on the contact / apex of the action and on the beat; ramp in over at least 6 frames so it does not snap. https://usenarrative.ai/blog/add-slow-motion-and-speed-ramps-to-a-video
- Two schools on the beat: peak slow-mo exactly on the beat with the ramp happening during the beat before it (https://try.wideframe.com/blog/how-to-speed-ramp-videos-with-ai-timing/) vs. beat marks where acceleration starts and the slow point lands a few frames later on the movement (https://capcutguide.com/capcut-velocity-edit/). Adobe Simplified pins the FAST peak to the beat. Practical rule: the discontinuity the ear hears (beat) should coincide with the discontinuity the eye sees (the knee of the curve), whichever side of the ramp that is.
- Interpolation: frame blending dissolves neighbours (ghosting), optical flow warps pixels along motion vectors (tearing at edges, worst with long shutter blur in the source). Optical flow best for 30 to 60 percent slow-downs; shoot 60 or 120 fps so real frames exist and interpolation is only the last resort. https://www.aiarty.com/knowledge-base/frame-blending-vs-optical-flow.htm https://loopdesk.ai/blog/speed-ramping-explained https://www.dpreview.com/forums/threads/frame-sampling-vs-optical-flow.4817574/
- Audio: duck music 1 to 2 dB under the slow segment, riser on approach, whoosh/impact on exit. https://biztipper.com/video-editing-tips-speed-ramping-tutorial-for-cinematic-slow-motion/
- "Velocity edit" = the TikTok name for a multi-point speed curve cut to beats; presets Montage, Hero, Bullet, Jump Cut, Flash In/Out. https://capcutguide.com/capcut-velocity-edit/

Smooth zoom
- Ease-in-out on scale, small range (100 to 110 percent is the tutorial norm; 120 only for a hard "hit"). ffmpeg zoompan jitters because it rounds the crop window to whole pixels; fix is upscale 4x to 8x first, or avoid zoompan. https://www.ffmpeg-micro.com/blog/ffmpeg-zoompan-filter-ken-burns-zoom-and-pan-without-the-jitter
- Verified today: crop w/h expressions are evaluated once at init (t is NaN, filter errors), so the old linear crop punch-in is not a keyframe tool. scale=...:eval=frame followed by a fixed centre crop gives sub-pixel smooth zoom at 1 s per 3 s of 1080x1920 footage.

Whip pan and directional blur
- Real whip: blur-out at the end of A and blur-in at the start of B in the SAME direction, cut inside the blur; mismatched direction or brightness exposes the seam. https://morphic.com/ai-glossary/whip-pan https://www.miracamp.com/learn/premiere-pro/whip-transition
- Faked in the edit: 10-frame Push plus Directional Blur, length 50 to 100, angle matching the motion (90 deg for horizontal in Premiere terms). https://adobebasics.com/blogs/news/whip-pan-transition-premiere-pro
- ffmpeg has dblur (angle, radius up to 8192) and all three params accept runtime commands, so sendcmd can keyframe the radius with [expr] and TI (0 to 1 over the command interval).

Mask / object wipes
- "Natural wipe": a foreground object that fully covers the frame (pole, person, the truck's own fender) is masked frame by frame and the next shot shows through. https://www.premiumbeat.com/blog/create-moving-object-premiere-pro https://adobe.com/creativecloud/video/hub/ideas/what-is-natural-wipe-in-video-editing.html
- Luma wipe = use the image's own brightness as the matte (darks or brights flip first), feathered. In ffmpeg: geq builds the matte with T in the expression, maskedmerge composites.
- xfade custom expressions give any soft geometric wipe; variables P (1 to 0), X, Y, W, H, PLANE, A, B. The scriptituk/xfade-easing project ports Penner easings and about 50 GL Transitions to stock-ffmpeg expressions; it needs -filter_complex_threads 1 because st()/ld() are shared between slices. https://github.com/scriptituk/xfade-easing
- ffmpeg-gl-transition needs a source build and has no Windows binary (2018 linker issues). Skip it. https://github.com/transitive-bullshit/ffmpeg-gl-transition frei0r is compiled into our build but no plugin DLLs are installed (FREI0R_PATH empty); not worth chasing, xfade custom covers it.

Camera shake on beat
- Constant wiggle looks like a cheap plugin. A hit is a sharp spike with fast decay, peaks lined up with audio hits, motion blur on, applied LAST after stabilisation. Typical: 8 to 15 Hz, 15 to 40 px at 1080 wide, decay to zero in 0.3 to 0.5 s, a touch of rotation (under 0.5 deg). https://schoolofmotion.com/blog/how-to-simulate-camera-shake-adobe-after-effects https://djordanmedia.com/blogs/news/after-effects-camera-shake-effect

Motion blur
- Real blur comes from a 180 degree shutter (shutter = half the frame interval). Faking it: tmix averages N successive frames; at a 4x oversampled framerate, mixing half the sub-frames of each output frame approximates 180 degrees. tblend=average plus framestep is the time-lapse version. minterpolate is for new frames, not blur. https://alessandrofarandagancio.medium.com/elevating-video-creativity-kill-the-boring-unleashing-motion-blur-with-ffmpeg-c25306ca53b2 http://social.d-e.gr/techblog/posts/12-smoother-timelapses-ffmpeg https://en.wikipedia.org/wiki/Rotary_disc_shutter
- Long-shutter source footage hurts optical flow; shoot ramps at 1/120 or faster and add blur in post.

Light leaks and flash frames
- One or two leaks per edit add character; more reads as "a filter stuck on repeat". Too strong, unnatural colours, static non-drifting leaks are the cheap tells. Flash frames are fine on the slow point of a ramp (Matt Loui's shutter flash) and cheap as a generic transition. Default is still the hard cut. https://www.insta360.com/blog/tips/how-to-create-film-transitions.html https://www.epidemicsound.com/blog/worst-video-editing-mistakes/

Cinematic truck shot language
- Camera at headlight or bumper height for mass; rolling shots at 1/40 to 1/60 from a chase vehicle; fly-by with the camera static, pre-focused, pan continuing after the truck leaves; polariser to control paint reflections; rack focus to redirect; parallax = foreground passing faster than background (shoot through a wheel, a tool, a door frame). Five to eight angles per piece: wide establish, elevated, tight nose, low three-quarter, detail, one moving shot, fly-by ender. https://www.modmycar.app/blog/how-to-shoot-cinematic-car-video https://carjourney.io/blog/photo-shoot-tips-for-cars https://www.hagerty.com/media/advice/car-cinematography-101-how-to-make-great-car-movies-with-your-phone/ https://www.car-editor.com/how-to-make-cinematic-car-reels/

Interpolation engines on this PC
- minterpolate measured: 1 s of 1080x1920 at 30 fps to 120 fps with mci/aobmc/bidir/vsbmc = 41 s. To 60 fps with obmc/bilat/epzs/search_param=16 = 7 s. Keep scd=fdiff (default) when the clip contains cuts; scd=none only for a single continuous shot. https://ffmpeg.org/pipermail/ffmpeg-user/2021-January/051566.html http://www.ffmpeglab.com/articles/ffmpeg-optical-flow-motion-interpolation.html
- RIFE: sharper than minterpolate, which smears; still fails on very fast motion. rife-ncnn-vulkan is a single Windows binary that runs on Intel/AMD/Nvidia Vulkan GPUs including iGPUs (-g -1 = CPU), image-dir in, image-dir out, -n target frame count or -s time step 0..1, models up to rife-v4.6. No UHD 770 benchmark exists; test it on a 2 s clip before adopting. https://redeyeautomations.com/notes/rife-vs-minterpolate https://github.com/nihui/rife-ncnn-vulkan https://nmkd.itch.io/flowframes

## 3. Motion vocabulary table

| Move | Use it when | Parameters that work | Cheap-looking failure |
|---|---|---|---|
| Speed ramp fast-slow-fast | one continuous camera move, truck rolling, wrench hit, door slam | 3x to 6x into 0.25x to 0.4x, ramps 6 to 15 frames, smoothstep/cubic ease, slow point on the action, knee on the beat | linear ramps, slow point in dead air, ramping stop-start footage, blended ghosting |
| Reverse-forward rebound | fill one beat with one clip, "breathing" hero shot | clip + reversed duplicate, mirrored curves, both inside one beat, optical flow on | curve not mirrored (CapCut bug), rebound on anything with people or smoke moving |
| Eased punch-in | emphasis on a word, a part number, a reveal | 1.00 to 1.08 over 1 to 2 s cubic in-out for slow; 1.00 to 1.15 over 6 frames out-ease for a hit | linear zoom, zoompan integer jitter, zoom past 1.2 on 1080p |
| Whip pan | change location or time with energy | 8 to 12 frames total, dblur radius 0 to 60-80 and back, same direction both sides, slide or hard cut inside | opposite directions, blur on a static tripod shot, used on every cut |
| Soft directional wipe | two shots of the same object, product reveal | 0.4 to 0.6 s, 10 to 20 percent feather, eased progress, direction follows motion in frame | hard-edged wipe, star/clock wipes, wipe against the motion |
| Luma / object wipe | something dark or bright crosses frame (door, hood, fender, shadow) | feather 40 to 80 luma levels, 0.5 to 0.8 s, dark-first for interiors | matte crawling on noise, object not covering full frame |
| Shake on beat | bass hit, torque wrench click, engine fire | 8 to 15 Hz, 20 to 35 px, exp decay 8 to 12 per s, 6 percent oversize, 0.3 deg rotate optional | constant wiggle, shake on calm audio, shake before stabilising |
| Motion blur | after any ramp or whip | 180 deg equivalent: tmix of half the sub-frames at 4x framerate; CapCut 30-40, 12 on detail | 100 blur smearing chrome and text, black edges (scale in 2 percent) |
| Flash frame / shutter | the slow point of a ramp, one per reel | 1 to 2 frames white at 60 to 80 percent, shutter SFX | flash on every cut, light leak every 3 s |
| Rack focus / parallax (shot, not edit) | detail to context | shoot through foreground, pull focus on the beat | faked blur masks with wobbling edges |

## 4. IMPLEMENT IN OUR STACK

Math used everywhere. With u in [0,1]:
- ease-in-out cubic: E(u) = u < 0.5 ? 4u^3 : 1 - (-2u + 2)^3 / 2
- ffmpeg expression form: if(lt(u,0.5),4*u^3,1-(-2*u+2)^3/2)
- smoothstep (used for the ramp because its integral is closed form): S(u) = 3u^2 - 2u^3, integral = u^3 - u^4/2
- ease-out cubic (for hits): 1 - (1-u)^3 ; ease-out expo: 1 - 2^(-10u)
- the Adobe Simplified "secret sauce" cubic-bezier(0.6,0,0.4,1) is a slightly sharper-shouldered ease-in-out; E(u) above is a fine stand-in. Reference https://easings.net/
Expression trick: ffmpeg has no local variables, so compute u into st(1,...) and read it with ld(1); the `*0+` in the graphs below is how a store is chained into the same expression.
All graphs are written for a -/filter_complex file (ffmpeg 7+ syntax). Prefix: FF="%LOCALAPPDATA%\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin\ffmpeg.exe"

A. Eased punch-in, 1.00 to 1.10 over 2 s (tested, 1.3 s render for 3 s)
```
[0:v]scale=w='1080*(1+0.10*(st(1,clip(t/2,0,1))*0+if(lt(ld(1),0.5),4*ld(1)^3,1-(-2*ld(1)+2)^3/2)))':h='1920*(1+0.10*(st(1,clip(t/2,0,1))*0+if(lt(ld(1),0.5),4*ld(1)^3,1-(-2*ld(1)+2)^3/2)))':eval=frame:flags=bicubic,crop=1080:1920,setsar=1[v]
```
Off-centre zoom: replace crop=1080:1920 with crop=1080:1920:x='(iw-ow)*0.5':y='(ih-oh)*0.35' (0.35 keeps the hood in frame). Hit zoom: change clip(t/2,...) to clip((t-TB_HIT)/0.2,0,1) and the ease to 1-(1-ld(1))^3. zoompan alternative (needs 4x upscale to stop jitter): scale=4320:7680,zoompan=z='1+0.1*(...same with on/60...)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30 (tested, works, slower).

B. Eased speed ramp: 3x, smoothstep down to 0.3x, hold, back to 3x (tested; output 4.33 s matches the integral exactly)
Model: r(t) = 1/speed = output seconds per input second. Output time T_out(t) is the integral of r. For a segment t0..t1 ramping r0 to r1 with smoothstep, with u=(t-t0)/(t1-t0):
T_out = T0 + r0*(t-t0) + (r1-r0)*(t1-t0)*(u^3 - u^4/2), and T1 = T0 + (t1-t0)*(r0+r1)/2.
Knots used: r=1/3 for 0..1.0 s, ramp to r=3.333 over 1.0..1.5, hold to 2.0, ramp back over 2.0..2.5, hold. Computed T at knots: 0.3333, 1.25, 2.9167, 3.8333.
```
[0:v]minterpolate=fps=120:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1,setpts='(if(lt(T,1.0), T/3, if(lt(T,1.5), 0.33333+(T-1.0)/3+(3.33333-0.33333)*0.5*(st(1,(T-1.0)/0.5)*0+ld(1)^3-ld(1)^4/2), if(lt(T,2.0), 1.25+(T-1.5)*3.33333, if(lt(T,2.5), 2.91667+(T-2.0)*3.33333+(0.33333-3.33333)*0.5*(st(1,(T-2.0)/0.5)*0+ld(1)^3-ld(1)^4/2), 3.83333+(T-2.5)/3)))))/TB',tmix=frames=2,fps=30,format=yuv420p[v]
```
Why this shape: minterpolate first makes 120 real-looking frames per second so the 0.3x section has frames to show; setpts bends time; tmix=2 adds a hair of shutter; fps=30 drops the surplus in the fast sections. Cost: 41 s per source second at 1080x1920 (7 s with fps=60:mc_mode=obmc:me_mode=bilat:me=epzs:search_param=16, fine for 0.5x floors). Do the ramp on the trimmed 2 to 4 s slot only, never the whole clip. iPhone 60 fps source halves the interpolation need: shoot ramps at 60 or 120.
Reverse-forward rebound: [0:v]split[f][r];[r]reverse[r2];[f][r2]concat=n=2:v=1 then run the ramp graph on the concat with the slow knot at the join.

C. Whip pan transition (tested; 3.7 s for two 4 s clips)
whipcmd.txt:
```
3.70-4.00 [expr] dblur@a radius 'TI*TI*70';
0.00-0.30 [expr] dblur@b radius '(1-TI)*(1-TI)*70';
```
graph:
```
[0:v]fps=30,settb=AVTB,sendcmd=f=whipcmd.txt,dblur@a=angle=0:radius=0[a];
[1:v]fps=30,settb=AVTB,sendcmd=f=whipcmd.txt,dblur@b=angle=0:radius=0[b];
[a][b]xfade=transition=slideleft:duration=0.2:offset=3.8,settb=AVTB[v]
```
angle=0 for horizontal whips, 90 for vertical, and pick slideleft/slideright to match the camera motion. TI runs 0 to 1 across the interval; squaring it makes the blur ease in. sendcmd [expr] works on any option flagged T in `ffmpeg -h filter=NAME`: dblur, rotate angle, crop x/y/w/h, scale w/h, tmix weights, eq brightness, hue. That is our generic keyframer.

D. Soft eased wipe as an xfade custom expression (tested; 18 s for a 0.5 s transition at 1080x1920 because st/ld forces -filter_complex_threads 1)
```
[0:v]fps=30,settb=AVTB[a];[1:v]fps=30,settb=AVTB[b];
[a][b]xfade=transition=custom:duration=0.5:offset=3.5:expr='st(0,1-P);st(0,if(lt(ld(0),0.5),4*ld(0)^3,1-(-2*ld(0)+2)^3/2));st(1,clip((X/W+0.15-ld(0)*1.15)/0.15,0,1));A*ld(1)+B*(1-ld(1))',settb=AVTB[v]
```
Run with -filter_complex_threads 1. Swap X/W for Y/H for a vertical wipe, (X/W+Y/H)/2 for diagonal, hypot(X-W/2,Y-H/2)/hypot(W/2,H/2) for an iris. 0.15 is the feather fraction. Render the transition on a 1 s window and concat, not on the full timeline, to keep single-thread time down.

E. Luma / object wipe using the outgoing shot's own brightness as the matte (tested, 6 s)
```
[0:v]fps=30,settb=AVTB,split=3[a0][a1][am];
[am]format=gray,geq=lum='st(0,clip((T-3.4)/0.6,0,1));st(0,if(lt(ld(0),0.5),4*ld(0)^3,1-(-2*ld(0)+2)^3/2));clip((ld(0)*315-lum(X,Y))/60,0,1)*255'[m];
[1:v]fps=30,settb=AVTB,setpts=PTS+3.4/TB[b0];
[a1][b0]overlay=eof_action=pass[bfull];
[a0][bfull][m]maskedmerge[v]
```
Darks flip first (good when the hood or a shadow crosses the lens); for brights-first use (lum(X,Y)-(255-ld(0)*315)). 60 is the feather in luma levels. Object wipe variant: replace [m] with a matte movie (PNG sequence or an mp4) produced in Python (OpenCV grabCut, or rembg for the truck) and the same maskedmerge line.

F. Shake on beats (tested, 0.3 s render). Beats at 0.5, 1.5, 2.5 s; 28 px, 12 Hz, decay 10 per s; y at 60 percent amplitude on a different frequency so it is not a straight line.
```
[0:v]scale=iw*1.06:ih*1.06:flags=bicubic,crop=1080:1920:x='(iw-ow)/2 + 28*( gte(t,0.5)*exp(-10*(t-0.5))*sin(2*PI*12*(t-0.5)) + gte(t,1.5)*exp(-10*(t-1.5))*sin(2*PI*12*(t-1.5)) + gte(t,2.5)*exp(-10*(t-2.5))*sin(2*PI*12*(t-2.5)) )':y='(ih-oh)/2 + 17*( gte(t,0.5)*exp(-10*(t-0.5))*cos(2*PI*9*(t-0.5)) + gte(t,1.5)*exp(-10*(t-1.5))*cos(2*PI*9*(t-1.5)) + gte(t,2.5)*exp(-10*(t-2.5))*cos(2*PI*9*(t-2.5)) )',setsar=1[v]
```
Python generates the sum from the beat list (librosa or CapCut's beat export). Add rotate='0.004*exp(-10*(t-b))*sin(...)':fillcolor=none between the scale and crop for the rotational component.

G. Speed-curve abstraction (design)
Input: list of (t_in, speed, ease) knots, e.g. [(0,3,'smooth'),(1.0,3,'smooth'),(1.5,0.3,'hold'),(2.0,0.3,'smooth'),(2.5,3,'hold')]. Steps: convert speed to r=1/speed; for each segment emit either the linear-integral or smoothstep-integral term and accumulate T at the knots; emit the nested if() for setpts; choose the interpolation fps as 30/min(speed) rounded to 60/90/120; emit the minterpolate + setpts + tmix + fps graph or, for a per-frame backend, the array src_time[k] = inverse of T_out at k/30 (numpy interp over a dense sample of T_out). Also return beat-knot check: the time of each curve knee in OUTPUT seconds so it can be snapped to the beat grid before rendering.

H. Python per-frame fallback (when ffmpeg expressions get in the way)
cv2.VideoCapture reads at native rate into a ring buffer; for each output frame k: s = src_time[k]; take the two bracketing frames and either pick nearest (fast parts), blend by fraction (cheap), or call rife-ncnn-vulkan on the pair with -s fraction (slow parts, iGPU). Then cv2.warpAffine with an eased 2x3 matrix (scale about an anchor, translate for shake, rotate) built from the same E(u); directional motion blur with cv2.filter2D using a 1xN line kernel rotated to the motion angle, N proportional to the frame-to-frame displacement; write frames as PNG into a dir and let ffmpeg encode with h264_qsv. This path is where cutout overlays, mask wipes from rembg mattes, and transforms with motion blur live.

Pipeline notes for build_reel2.py: replace the crop-expression zoom with graph A; add `ramp` (knot list) that compiles to graph B on the slot; add `whip`/`wipe` as xfade types that expand to C/D/E; add `shake` beats list to F; keep settb=AVTB after every xfade and setsar=1 after any scale (already learned). Always stabilise before ramping, blur after.

## 5. Top 5 for diesel truck content, in order

1. The eased fast-slow-fast ramp on one continuous move (walk-up to the F600 grille, pan down the frame rail, roll-in on the turbo), slow point on the hero detail, knee on the beat, tmix blur, deep whoosh. This is the signature of every viral car edit in the set.
2. Eased punch-ins on every static talking or wrenching shot (1.00 to 1.08 over the shot, out-ease hit to 1.12 on a key word). Costs nothing to render and kills the "hard cuts only" verdict immediately.
3. Whip pans between shop locations and between parts (same direction, 10 frames, dblur). Matches how the shop footage is already shot handheld.
4. Rebound (forward-reverse) on one hero shot per reel, inside a single beat, never on people or smoke.
5. Shake on the bass hit plus one shutter flash on the slow point, once per reel. More than once and it reads like a template.
Shoot list that makes all five possible: 60 fps minimum for anything that will be ramped, one continuous move per clip, start and end each move still, bumper-height low angles, one fly-by, one through-foreground parallax shot.
