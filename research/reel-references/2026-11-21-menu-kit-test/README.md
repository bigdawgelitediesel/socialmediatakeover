# Menu-grammar kit test (2026-11-21)

First render of the components learned from the @ai.nxtlvl, @tenfoldmarc, @ultra.skills and @edita.visuals studies, in the new plate-free `CardReel` composition (tools/rival-reels/src/CardReel.tsx, components in src/components/Menu.tsx, eases in anim.ts). 14 s test, 23 s render on this CPU. Props: tools-snapshot/rival-reels/menu-test.props.json.

What is in the frames (menu-test-keys.png, left to right): ProgressHud + Headline with the serif accent pill; StrikeStamp (STOCK tag, strike bar, RIVAL stamp); ItemCard with counter, PARTNER tag, chips on words, footnote and the ON THE TRUCK sticker; SidebarList two columns with the current item highlighted; CountUp (year, no grouping) + PhoneStage with the 02/17 badge + Checklist typing rows; IrisWipe into CommentGate (comment typed and hearted, DM preview with numbered chips).

Fixes made after this render: CountUp no longer puts a comma in a year; Headline shrinks instead of wrapping into the card zone.

House-rule reminder: CommentGate is for comment-gated deliverable reels only (Jacob: no on-screen CTA on normal reels). Palette and fonts stayed El Coyote (black, cream, tan, oxblood, Anton / Poppins / Instrument Serif).
