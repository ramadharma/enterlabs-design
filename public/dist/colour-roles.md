# Enterlabs · 6. Colour roles (v0.3)

- **Brand:** orange `#FF5E1F` (accent), ink `#000000`, inverse `#FFFFFF`, off-white `#F5F5F4` (light ground, ink-2), charcoal `#232323` (dark ink-3), black (dark ground).
- **Orange goes on:** the focus ring of every control (`--focus-ring`, 2px, 2px offset) · brand badges (`.badge.brand`: "New", "Recommended") · the one figure or word that matters (`.text-brand`) · chart series 1 (everything else grey) · text selection · marketing pages: an orange field with black type and a black button (6.7:1).
- **Orange never goes on:** buttons, checkboxes, radios, switches, active tabs or segmented thumbs, selected rows, links, body text, the logo, shadows or tints behind cards, or anything that means a status. White text on orange fails (3.06:1).
- **Status** (meaning only, always the tint pattern: `-3` fill with `-11` text, edge from its own colour): success teal (`green-*`) · danger ruby (`red-*`) · warning amber · info blue · inactive neutral (white badge with the button shadow). Each status hue sits at least 25° from orange so it never reads as brand; never put danger right next to orange.
- **Other:** `--link` for inline links in sentences (link buttons stay ink) · `--chart-2…5` only when categories must be told apart · `--cream` for warm bands on marketing pages only, never product UI. No gradients anywhere.
- Hue never ranks importance and never decorates.

**Illustration and imagery** (sleek SaaS line art)

- Show the product working first: live diagrams, demo widgets, real screens. Draw only what can't be shown that way.
- Line art only: 1.5px strokes, round caps and joins, flat. Grey, white and orange, nothing else: no status hues, no other colours, no gradients, glows, shadows or 3D.
- Diagrams: white nodes (`--illo-base`) with a `--illo-line` edge, radius 8; groups as `--illo-fill` areas with no edge; optional faint dot grid (`--illo-grid`, 1px dots every 16px) and dashed rings behind. Solid line = main path; dashed = optional, waiting, async or blocked.
- Orange (`--illo-accent`) once per picture, on the thing it is about: an orange-stroked node or icon, or one small orange dot for data on the move.
- Meaning without colour: success = solid node + tick + word in strong ink; blocked or failed = dashed node and path + cross + word in grey (never red, never orange). Labels Inter 500 12px in `--illo-label`, the focus in ink-12. Alt text on anything that carries meaning.
- Spot illustrations: 96–160px, marketing pages only (features, empty states); in product UI use an 18px icon. Isometric line drawings only when depth explains the idea, same stroke, no shading.
- On phones, redraw a wide diagram vertically so labels stay about 12px.
- Photography and video: prefer real product footage. Hero video full-bleed with an AVIF poster, still for reduced motion or low data. People only as real customer headshots, cropped in circles, in testimonials; no stock photos. AVIF/WebP with 1x/2x, hero eager, below the fold lazy, `aspect-ratio` set first.
- Customer logos: monochrome SVG in `currentColor` (ink-10), same optical height 24–32px, 48–64px apart.
- Marketing pages: orange in every layout, as a small accent or a flat full-bleed field with black type. Product UI keeps it rare.
- The Enterlabs mark appears only as the logo, under the logo rules: never cropped, tiled or layered into a decorative shape.
