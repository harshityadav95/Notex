# Notex cloud & infrastructure section — design QA

final result: passed

Scope: add Cloudflare, Azure, and Kubernetes beneath the existing learning paths, matching the Fanout learning-card design and the existing Notex typography. This review covers the new section and its interactions; the earlier full-page review is retained below.

## Findings

No remaining actionable P0/P1/P2 findings for the new section. The three paths are design previews with four topic summaries and official guide links, not newly authored courses. Their labels make this explicit.

## Source and comparison evidence

All current evidence is local in `/Volumes/skynetevo/github/Notex/.design-evidence/` (ignored by Git).

- Source visual truth: live `https://fanout.sh/`, learning-card directory, captured in the in-app browser.
- Source desktop: `fanout-cards-desktop.jpg` (1435 × 997 pixels).
- Implementation desktop: `notex-cloud-desktop.jpg` (1425 × 950 pixels).
- Source mobile: `fanout-cards-mobile.jpg` (385 × 833 pixels).
- Implementation mobile: `notex-cloud-mobile.jpg` (375 × 812 pixels).
- Requested CSS viewports: 1440 × 1000 desktop and 390 × 844 mobile. Device pixel ratio: 1. Browser-native captures have different content/scrollbar crops; compare card proportions at native size rather than claiming a pixel-identical full-page diff.
- State: public light landing page, learning cards visible, dialogs closed. The source directory and new cloud section have different content and scroll positions. The mobile implementation capture retains a pointer hover on Azure. Those are expected differences, not layout failures.
- Source and implementation desktop screenshots were opened together in one comparison input, followed by both mobile screenshots, before and after the alignment correction.
- The full section captures show headings, artwork, bullets, badges, and card footers at readable resolution, so additional detail crops were unnecessary for this scoped comparison. This was not a new audit of every existing page section.
- Additional states: `notex-cloudflare-dialog.jpg` (desktop) and `notex-azure-mobile-dialog.jpg` (mobile).

## Required fidelity surfaces

- **Fonts and typography:** reuse the existing self-hosted Overused Grotesk for headings/body text and Departure Mono for eyebrows and badges. Match the 22px section heading, 20px desktop card titles, compact list hierarchy, and mobile wrapping. The serif lettering belongs to the generated notebook illustrations, matching the reference's printed-book direction.
- **Spacing and layout:** use the existing 968px learning grid, three desktop columns, two mobile columns, 20px desktop gaps, 12px mobile gaps, 24px desktop card padding, 12px radii, restrained shadows, and the existing vertical section rhythm. Desktop cards measure approximately 309 × 536 CSS pixels. The third mobile card continues on the next row at the same width.
- **Colors:** retain the #f7f7f8 background and #272727 text; introduce provider-specific apricot, dusty blue, and lavender card surfaces within the reference's muted palette. Expected adaptation, not an exact copy of unrelated course colors.
- **Image quality:** three separate generated illustrations, each a locally bundled 800 × 800 transparent PNG. Complete book edges, legible provider names, technical line drawings, tactile covers, consistent index tabs and shadows. Images use `object-fit: contain`; no sprite crops or source hotlinks.
- **Copy and content:** concise provider-specific learning themes, honest PATH PREVIEW badges, four-topic dialogs, official documentation links, and a working system-design link. No invented course completion, free lesson, or enrollment claims.

## Comparison history

1. **[P2] Notebook alignment drift.** Initial desktop/mobile comparisons showed the books centered more than the source's left-aligned covers. Corrected `.cloud-art` with a 20px desktop and 10px mobile left translation. Before: `notex-cloud-desktop-initial.jpg` and `notex-cloud-mobile-before-alignment.jpg`. After: `notex-cloud-desktop.jpg` and `notex-cloud-mobile.jpg`, opened alongside the source again. The revised books align with the card text inset while preserving uncropped shadows.
2. A screenshot immediately after resizing captured a stale scaled viewport. Verified the actual CSS viewport, reloaded, and recaptured after layout settled. The stale screenshot is excluded from the final comparison evidence.

## Functional verification

- All three path buttons open the correctly named native dialog, each with four topics and the corresponding official-guide URL.
- Close buttons and Escape dismiss dialogs; focus returns to the triggering card.
- Mobile dialog fits the viewport (354px dialog within a 390px viewport), readable without horizontal clipping.
- Mobile menu includes Cloud & infrastructure, navigates to the section, and closes.
- Desktop Explore menu includes Cloud & infrastructure and navigates to the section.
- All three card images loaded at their expected 800px natural width.
- Desktop and mobile document scroll width equal document client width; no horizontal overflow.
- Browser error logs: none in the local preview.
- Python static build, generated-link/UI-asset validation, JavaScript syntax check, and `git diff --check` passed.
- Local server responds HTTP 200 at `http://127.0.0.1:4173/`. Preview: `http://127.0.0.1:4173/#cloud`.

## Implementation checklist

- [x] Generate and bundle three original notebook illustrations.
- [x] Add matching cloud learning cards and functional path dialogs.
- [x] Add desktop/mobile/footer navigation.
- [x] Compare desktop/mobile captures with the reference and correct alignment.
- [x] Verify interactions, overflow, image loading, console, build, and links.
- [x] Keep a local preview running for design review.

No deployment was performed. User design approval remains the next decision.

---

## Prior full landing-page QA (retained history)

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
