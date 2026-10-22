# Notex landing-page QA — full composition revision

final result: passed

The landing page now follows the current Fanout page composition. Notex's original material, free access, artwork, author credit, and working destinations are retained. This is a close visual implementation of the page structure, not a claim that proprietary illustrations, company logos, commercial plans, video, and testimonials are identical.

## Evidence

Directory: `/Users/harshit/.codex/visualizations/2026/10/22/01a164cd-4eb1-7150-a336-3e84e237ec19/landing-v2/`

- Source visual truth: live `https://fanout.sh/` captured in the in-app browser.
- Full-view comparison: `source-full.png` and `notex-full.png`, emitted together for direct comparison.
- Desktop hero: `source-desktop.png`, `notex-desktop.png`.
- Mobile hero: `source-mobile.png`, `notex-mobile.png`, emitted together after correcting the headline wrap.
- Focused navigation: `source-navigation.png`, `notex-navigation.png`; mobile: `notex-navigation-mobile.png`.
- Requested desktop viewport: 1440 × 1000. Source full capture 1437 × 9649; implementation full capture approximately 1425 × 9618.
- Requested mobile viewport: 390 × 844. Source capture 385 × 833; implementation capture 375 × 812.
- The in-app browser's content capture and scrollbar widths differ slightly. Native captures were compared proportionally; no pixel-difference metric or exact-density claim is made.
- State: public light-theme landing, announcement present, source coupon modal dismissed, default FAQ state. Rotating companies and marquee positions vary over time.

## Changes and visual comparison

The earlier simplified landing was replaced with the complete composition: rotating company headline, three floating books, reading card and study checkpoint, two fading lower notes, three marquee rows, eleven topic cards, two preview-card lanes, learning-folder section, eight navigation tiles, three access cards, floating study board, six-item FAQ, final CTA, and multi-column footer/follow strip.

The complete note list and resource lists moved to `library/`. Existing note routes and original source files remain available.

### Required fidelity surfaces

- **Typography:** self-hosted Overused Grotesk and Departure Mono match the reference families. Desktop headline is regular 88px at the captured width. Mobile headline was measured against the source and adjusted to retain the three-line composition and a single `L7 knows. Mapped.` line.
- **Spacing/layout:** full-page order, three-column desktop and two-column mobile topic grids, four-column/two-column navigation grid, wide hero margins, floating reading materials, section rhythm, card radii, and restrained shadows follow the reference. Full desktop page silhouettes are closely aligned in total height.
- **Colors:** pale #f7f7f8 background, #272727 foreground, muted text, blue announcement, rose/sage/yellow/blue/teal/navy/purple topic surfaces, and the eight reference-inspired navigation colors are represented by explicit CSS tokens and values.
- **Images/icons:** original Notex notebook artwork remains local. Phosphor thin icons replace the heavier initial icons in the navigation tiles. The learning folder reproduces the source's native layered-paper treatment with five linked contents. All 35 rendered landing images were checked loaded, with no missing assets. Small SVGs load eagerly so full-page captures and direct section navigation remain complete.
- **Copy/content:** working Notex destinations replace commercial Fanout destinations. Source testimonials are represented by actual note previews; affiliation marquees by the library's technical subjects; paid plans by truthful free-access cards. The demo previews the real library instead of showing Fanout's commercial video. Footer reads “Designed by harshityadav.in”.

## Resolved findings / comparison history

1. **P1: incomplete page composition.** The first version omitted major reference sections. Replaced it with the full sequence and eleven real learning destinations. Full source/implementation screenshots were compared together.
2. **P2: hero spacing and alignment.** Measured the source geometry, then adjusted hero height, center offset, heading size and rotating-word width. Rechecked desktop hero captures together.
3. **P2: mobile headline wrapped to four lines.** Matched the source's inline knowledge line, reduced the mobile monospace scale, and adjusted the notice/hero offsets. The final paired mobile captures show three lines without horizontal overflow.
4. **P2: missing newly added icons.** Python's download path encountered certificate errors; fetched the official assets with curl and expanded the build check to validate image/CSS references. All landing images then loaded. Small icons now load eagerly to avoid blank off-screen graphics in full-page captures.
5. **P2: learning folder contents were too vertically aligned.** Redistributed the five linked items across the folder cover to match the source composition. Replaced heavy tile icons with Phosphor thin variants.

No remaining actionable P0/P1/P2 issues for the Notex landing adaptation. Original artwork and Notex-specific destinations/copy remain expected differences. Source company-logo artwork is not bundled.

## Functional verification

- Header Community dropdown opens and reports expanded state; closing restores it.
- See demo opens a native modal; Close demo works.
- Mobile menu opens; Explore navigates to the eight-tile section and closes the drawer.
- Eight navigation icons load successfully at the mobile section viewport.
- Selecting Notes opens `library/`, containing 22 note links and 11 PDF links.
- Search on the nested Library page resolves the relative search index: `JOIN` returns JavaScript, Python and SQL results.
- FAQ opens the selected question and closes the previously open question.
- Rotating headline updates its company and article; reduced-motion mode stops rotation and marquees.
- Desktop document width equals scroll width (1425px); mobile document width equals scroll width (375px).
- Browser error/warning log checked: none.
- Build, generated-link/UI-asset check and JavaScript syntax check pass.
- Local preview server returns HTTP 200 at `http://127.0.0.1:4173/`.

Two missing legacy note illustrations predate this work and are excluded from the new UI-asset validation; external legacy references were not audited. No remote deployment was performed.
