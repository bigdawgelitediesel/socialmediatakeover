# Menu-grammar kit test (2026-11-21)

First render of the components learned from the @ai.nxtlvl, @tenfoldmarc, @ultra.skills and @edita.visuals studies, in the new plate-free `CardReel` composition (tools/rival-reels/src/CardReel.tsx, components in src/components/Menu.tsx, eases in anim.ts). 14 s test, 23 s render on this CPU. Props: tools-snapshot/rival-reels/menu-test.props.json.

What is in the frames (menu-test-keys.png, left to right): ProgressHud + Headline with the serif accent pill; StrikeStamp (STOCK tag, strike bar, RIVAL stamp); ItemCard with counter, PARTNER tag, chips on words, footnote and the ON THE TRUCK sticker; SidebarList two columns with the current item highlighted; CountUp (year, no grouping) + PhoneStage with the 02/17 badge + Checklist typing rows; IrisWipe into CommentGate (comment typed and hearted, DM preview with numbered chips).

Fixes made after this render: CountUp no longer puts a comma in a year; Headline shrinks instead of wrapping into the card zone.

House-rule reminder: CommentGate is for comment-gated deliverable reels only (Jacob: no on-screen CTA on normal reels). Palette and fonts stayed El Coyote (black, cream, tan, oxblood, Anton / Poppins / Instrument Serif).

## Effects test (same day, 09:00)

`src/components/Effects.tsx`: the tenfoldmarc vocabulary on the Driven plate + RVM cutout that already lived in public/ (fx-plate.mp4 / fx-cutout.webm, 16 s). Render 52 s. Frames in fx-test-keys.png: Masthead RIVAL behind the head with sub lines; WallBehind scatter (tiles behind him); FrameBreak v1 (wrong: nothing crossed the card); Vertigo (background grows, he holds); BgReplace (the F600 behind him, Ken Burns); PullBackWindow (clip revealed inside a browser window with a ticking list); ZoomThrough flash frame; HudZoom brackets + REC + readout with BlurWord "video".

fb-test-keys.png: FrameBreak v2 after the fix (card is a 4:5 crop of the plate, cutout drawn at the same rect unclipped, so the hand crosses the right edge), plus ChartGrow in front with the 1K label pill on the last point.

Overlay types now registered in RivalReel/CardReel: hud, sidebar, phone, countup, strikestamp, item, headline, ghost, iris, negflash, gate, quad, checklist, wall, masthead, framebreak, vertigo, bgreplace, chart, pullback, zoomthrough, hudzoom, beforeafter, blurword. RivalReel passes `plate` and `cutout` to every overlay, so matte effects need no extra props.
