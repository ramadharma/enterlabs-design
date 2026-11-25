# Enterlabs design system · v0.3

Black acts, orange signs: black (white in dark) is the action colour on every button and control, and brand orange `#FF5E1F` is a rare accent. A 12-step warm-grey neutral builds structure, and the other hues appear only for status. Interfaces are quiet and tactile: white surfaces lift off an off-white ground with a fine ring and a crisp 1px drop. Buttons follow shadcn/ui.

- **Logo kit v1.0** is approved and fixed.
- **UI layer v0.3** builds on it and adds brand orange as an accent. Buttons, checkboxes, switches and active tabs stay black; orange never fills a control and never colours the logo.

The spec is published at `https://enterlabs-design-systems.pages.dev/dist/` (machine-readable, read by the `enterlabs-design` skill) with the browsable docs at `https://enterlabs-design-systems.pages.dev`. `dist/tokens.css` is the complete token file.

**Which skill:** Enterlabs (the renamed Codemasters) uses this skill. Sembuh AI and Flipmaster work uses `codemasters-design` if it is available.

## 1. Workflow

1. **Pin the output.** HTML/CSS page or artifact, React + Tailwind (shadcn), Figma, or a review of existing work. Ask only if it truly isn't clear.
2. **Start from the tokens (section 4) and the component kit (section 8).** For HTML, paste the tokens, the base and the component CSS into the page's `<style>` and use the classes. For React/shadcn, map the tokens onto the shadcn CSS variables (already included in the tokens) and keep each component's spec; translate only the syntax.
3. **Use a documented component before inventing one.** If something has no recipe here, build it from the tokens and say it is new.
4. **Check before you ship** (section 10): both themes, the longest real data, phone width.
5. **Finish with** the version (v0.3), and every deviation or proposal the spec doesn't cover.

Never fill a gap from general knowledge: if a value isn't here, say so and propose one, marked as a proposal.

## 2. Brand and logo

Write the name "Enterlabs" in text. The logo itself is the lowercase wordmark: **enter** drawn from Inter Display 700, **labs** from 300, outlined. It is artwork, never live text.

| Composition | Use | Kit file (Enterlabs_Brand_Assets_v1.0) |
|---|---|---|
| Horizontal (default) | Headers, decks, documents, email, most marketing | `01_VECTOR_MASTER/SVG/enterlabs-horizontal-black.svg` / `-white.svg` |
| Stacked | Tight vertical spaces: posters, covers, square posts | `…/enterlabs-stacked-*.svg` |
| Wordmark | When the symbol already appears nearby | `…/enterlabs-wordmark-*.svg` |
| Symbol | App sidebars, avatars, any slot under 180px wide | `…/enterlabs-symbol-*.svg` |
| Micro | 16 to 32px only (favicons); thicker strokes | `…/enterlabs-micro-*.svg` |

Other kit folders: `02_PRINT` (PDF/EPS for print), `03_DIGITAL/PNG` (1400–2800w for slides and email), `04_ICONS` (favicon, app tiles, avatars, `WebReady/` for a site root), `05_DESIGN_SYSTEM/asset-map.json`.

**Rules**

- Logo ink is only `#000000` on light or `#FFFFFF` on dark. Approved backgrounds: white `#FFFFFF`, off-white `#F5F5F4`, charcoal `#232323`, black `#000000`. They are backgrounds, not logo colours.
- Clear space: at least **x on every side, x = ¼ of the symbol's height**.
- Minimum size: horizontal **180px** wide on screen, **38mm** in print. Smaller than that, use the symbol. 16 to 32px, use the micro mark.
- Never stretch, recolour (not even in brand orange), add shadows/strokes/effects, put black artwork on a dark surface, move or resize *enter* and *labs* apart, or retype the wordmark in a font.

**Artwork.** These are the v1.0 masters with the ink set to `currentColor`: set `color: #000` on light and `color: #fff` on dark. Size with width or height; never both. For the stacked and wordmark compositions, use the kit files.

Horizontal:
```html
<svg role="img" aria-label="Enterlabs" xmlns="http://www.w3.org/2000/svg" viewBox="-14 -14 1370 298"><g><path d="M 58 261 H 288 Q 332 261 332 217 V 42 Q 332 10 299 10 H 193 Q 160 10 160 44 V 97 Q 160 111 145 111 H 60 Q 10 111 10 160 V 211 Q 10 261 58 261 Z" fill="none" stroke="currentColor" stroke-width="18" stroke-linejoin="round" stroke-linecap="round"/><path d="M 203 185 H 81 M 110 157 L 81 185 L 110 213" fill="none" stroke="currentColor" stroke-width="16" stroke-linejoin="round" stroke-linecap="round"/></g><g><g fill="currentColor"><path d="M586 -24C842 -24 1046 122 1085 332H816C789 250 710 197 595 197C440 197 350 298 345 454H1096V533C1096 855 887 1080 576 1080C273 1080 58 849 58 527C58 206 266 -24 586 -24ZM347 642C363 774 450 856 582 856C715 856 803 774 818 642Z" transform="translate(404.6612,201) scale(0.1092900,-0.1092900)"/><path d="M399 587C399 751 484 824 606 824C729 824 800 749 800 607V0H1094V661C1094 928 949 1078 724 1078C572 1078 465 1010 394 890V1056H104V0H399Z" transform="translate(530.3447,201) scale(0.1092900,-0.1092900)"/><path d="M711 1056H495V1344H200V1056H18V825H200V280C200 88 307 0 539 0H711V231H598C518 231 495 254 495 326V825H711Z" transform="translate(661.3834,201) scale(0.1092900,-0.1092900)"/><path d="M586 -24C842 -24 1046 122 1085 332H816C789 250 710 197 595 197C440 197 350 298 345 454H1096V533C1096 855 887 1080 576 1080C273 1080 58 849 58 527C58 206 266 -24 586 -24ZM347 642C363 774 450 856 582 856C715 856 803 774 818 642Z" transform="translate(743.8973,201) scale(0.1092900,-0.1092900)"/><path d="M104 0H399V572C399 731 488 815 609 815C659 815 714 811 736 810V1061C712 1062 683 1063 649 1063C510 1063 430 1003 391 876H388V1056H104Z" transform="translate(869.5808,201) scale(0.1092900,-0.1092900)"/></g><g fill="currentColor"><path d="M257 1490H129V0H257Z" transform="translate(959.5840,201) scale(0.1040000,-0.1040000)"/><path d="M441 -16C631 -16 736 75 782 173H785V0H913V732C913 935 752 1075 517 1075C278 1075 107 931 101 740H231C237 864 355 959 517 959C678 959 785 863 785 732V716C785 633 700 630 503 603C255 571 77 514 77 295C77 88 240 -16 441 -16ZM457 101C311 101 208 168 208 289C208 416 320 466 497 491C636 510 748 528 785 561V413C785 230 668 101 457 101Z" transform="translate(1006.3780,201) scale(0.1040000,-0.1040000)"/><path d="M615 -19C886 -19 1075 201 1075 528C1075 855 885 1075 615 1075C456 1075 317 992 259 857H257V1490H129V0H255V200H256C322 63 456 -19 615 -19ZM597 99C385 99 248 267 248 528C248 789 385 958 597 958C798 958 945 803 945 528C945 253 798 99 597 99Z" transform="translate(1121.2920,201) scale(0.1040000,-0.1040000)"/><path d="M483 -21C712 -21 877 98 877 289C877 437 784 518 593 564L418 605C298 633 229 682 229 774C229 883 326 964 476 964C629 964 723 877 730 740H856C847 950 694 1077 476 1077C253 1077 100 952 100 774C100 625 200 535 391 490L565 449C678 423 748 379 748 287C748 172 645 92 480 92C312 92 215 174 205 316H77C89 97 255 -21 483 -21Z" transform="translate(1247.0220,201) scale(0.1040000,-0.1040000)"/></g></g></svg>
```

Symbol:
```html
<svg role="img" aria-label="Enterlabs" xmlns="http://www.w3.org/2000/svg" viewBox="-14 -14 370 299"><g><path d="M 58 261 H 288 Q 332 261 332 217 V 42 Q 332 10 299 10 H 193 Q 160 10 160 44 V 97 Q 160 111 145 111 H 60 Q 10 111 10 160 V 211 Q 10 261 58 261 Z" fill="none" stroke="currentColor" stroke-width="18" stroke-linejoin="round" stroke-linecap="round"/><path d="M 203 185 H 81 M 110 157 L 81 185 L 110 213" fill="none" stroke="currentColor" stroke-width="16" stroke-linejoin="round" stroke-linecap="round"/></g></svg>
```

Micro (favicons, 16–32px):
```html
<svg role="img" aria-label="Enterlabs" xmlns="http://www.w3.org/2000/svg" viewBox="-17 -17 376 305"><g><path d="M 58 261 H 288 Q 332 261 332 217 V 42 Q 332 10 299 10 H 193 Q 160 10 160 44 V 97 Q 160 111 145 111 H 60 Q 10 111 10 160 V 211 Q 10 261 58 261 Z" fill="none" stroke="currentColor" stroke-width="24" stroke-linejoin="round" stroke-linecap="round"/><path d="M 203 185 H 81 M 108 158 L 81 185 L 108 212" fill="none" stroke="currentColor" stroke-width="22" stroke-linejoin="round" stroke-linecap="round"/></g></svg>
```

Favicon wiring (copy `04_ICONS/WebReady/` to the site root):
```html
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="icon" sizes="any" href="/favicon.ico">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
```

## 3. Principles

When two rules clash, the higher one wins.

1. **Black acts, orange signs.** Every button and active control is black (white in dark). Orange is the one brand colour, kept rare: the focus ring, brand badges, the number that matters, chart series 1. Other hues only mean status: success, danger, warning, info.
2. **One next step.** Each surface has at most one default (black) button. Everything else steps down: outline, then ghost, then link.
3. **Quiet and tactile.** Surfaces lift with a fine ring and a crisp 1px drop. No gradients, glows or big blurry shadows.
4. **Swiss structure.** Inter at one weight (500) on a 4px grid. Hierarchy comes from size and ink step, never from bold or colour. Remove before adding.

## 4. Tokens

Components ask for roles (`ink-3`, `--primary`), never hex values. Dark mode: `data-theme="dark"` on `<html>`; without it, follow the system. Wrap each surface in its class (`surface-panel`, `surface-raised`, `surface-overlay`, `surface-rail`, `surface-sunk`) so controls inside borrow fill, edge and drop from it. Load Inter: `https://fonts.googleapis.com/css2?family=Inter:wght@300;500;700&display=swap`.

```css
/* Enterlabs design tokens (UI layer on top of the logo kit v1.0)
   Components use roles, never hex codes. Change a value here, not in a component. */
:root {
  /* Neutral, light. Fixed handles; never remapped. ink-2 is the brand off-white. */
  --root-ink-1: #FBFBFA; --root-ink-2: #F5F5F4; --root-ink-3: #EDEDEC; --root-ink-4: #E5E5E4;
  --root-ink-5: #DEDEDD; --root-ink-6: #D6D6D5; --root-ink-7: #CACAC9; --root-ink-8: #B5B5B4;
  --root-ink-9: #8A8A89; --root-ink-10: #737372; --root-ink-11: #5C5C5B; --root-ink-12: #111111;
  --ink-a3: color-mix(in oklab, var(--root-ink-12) 6%, transparent);
  --ink-a4: color-mix(in oklab, var(--root-ink-12) 10%, transparent);

  /* Working steps: components use these; surfaces remap 1-7. */
  --ink-1: var(--root-ink-1); --ink-2: var(--root-ink-2); --ink-3: var(--root-ink-3);
  --ink-4: var(--root-ink-4); --ink-5: var(--root-ink-5); --ink-6: var(--root-ink-6);
  --ink-7: var(--root-ink-7); --ink-8: var(--root-ink-8); --ink-9: var(--root-ink-9);
  --ink-10: var(--root-ink-10); --ink-11: var(--root-ink-11); --ink-12: var(--root-ink-12);

  /* Brand (logo kit v1.0). Logo ink is only ever these two. */
  --el-brand-ink: #000000;
  --el-brand-inverse: #FFFFFF;
  --el-surface-light: #FFFFFF;
  --el-surface-offwhite: #F5F5F4;
  --el-surface-charcoal: #232323;
  --el-surface-dark: #000000;
  --el-logo-min-width: 180px;

  /* Surfaces */
  --surface-top: #FFFFFF;
  /* shadcn/ui theme, mapped onto the Enterlabs neutral. Buttons use these names. */
  --background: var(--surface-top);
  --foreground: var(--root-ink-12);
  --primary: var(--root-ink-12);
  --primary-foreground: var(--root-ink-1);
  --secondary: var(--root-ink-2);
  --secondary-foreground: var(--root-ink-12);
  --accent: var(--root-ink-2);
  --accent-foreground: var(--root-ink-12);
  --muted-foreground: var(--root-ink-11);
  --destructive: var(--red-solid);
  --border: var(--root-ink-4);
  --input: var(--root-ink-4);
  --ring: var(--focus-ring);
  --radius: var(--radius-control);
  --shadow-xs: 0 1px 2px 0 rgb(0 0 0 / .05);

  --ground: var(--root-ink-2);
  --panel: var(--surface-top);
  --raised: var(--surface-top);
  --overlay: var(--surface-top);
  --control-fill: var(--surface-top);
  --line: var(--ink-6);
  --hairline: 0.5px;
  --switch-on: var(--primary);
  --switch-off: var(--root-ink-7);
  --focus-ring: #E8500E;      /* brand orange, darkened to keep 3:1 on white, ground and wells */

  /* Primary action: black in light, white in dark. No brand accent yet. */
  --primary-bg: var(--ink-12);
  --primary-fg: var(--ink-1);
  --primary-hover: color-mix(in oklab, var(--primary-bg) 93%, var(--primary-fg));

  /* Brand orange: an accent, never an action. Buttons, checks, switches and tabs stay black. */
  --brand-3: #FFEFE9; --brand-4: #FFE2D4; --brand-6: #FFC7B0;
  --brand-9: #FF5E1F; --brand-10: #FF4801; --brand-11: #B83300;
  --brand-text: #D63C01;      /* orange text on white, 4.66:1 */
  --brand-contrast: #050505;  /* type on an orange field: black, 6.7:1 */
  --brand: var(--brand-9);
  --cream: #FFFBF5;           /* warm band, marketing pages */
  --selection: #C82800;
  --link: #193CB8;            /* inline links inside sentences */
  --chart-1: var(--brand-9); --chart-2: #0A95FF; --chart-3: #00BD7D; --chart-4: #EE0DDB; --chart-5: #0D9488;

  /* Illustration: line art in grey, white and orange only. Roles follow the theme on their own. */
  --illo-base: var(--surface-top); --illo-line: var(--root-ink-9); --illo-line-strong: var(--root-ink-12);
  --illo-fill: var(--root-ink-2); --illo-grid: var(--root-ink-5); --illo-label: var(--root-ink-11);
  --illo-accent: var(--brand-9); --illo-accent-fill: var(--brand-3);

  /* Status hues: meaning only, each at least 25 degrees (OKLCH) from brand orange.
     green = success (teal hue), red = danger (ruby hue). -11 passes 4.5:1 on -3. */
  --red-3: #FEEAED; --red-6: #F8BFC8; --red-9: #E54666; --red-11: #CA244D;
  --red-solid: #CA244D; --red-solid-hover: #B61E44; --red-contrast: #FFFFFF;
  --green-3: #E0F8F3; --green-6: #A9DFD3; --green-9: #12A594; --green-11: #00796A;
  --amber-3: #FFF7C2; --amber-6: #F3D673; --amber-9: #FFC53D; --amber-11: #9A5800;
  --blue-3: #E6F4FE; --blue-6: #ACD8FC; --blue-9: #0090FF; --blue-11: #0B68BA;

  /* Shadows: crisp. Ring + 1px drop + at most one tight drop. */
  --shadow-ink: 17 17 17;
  --shadow-button: 0 1px 2px 0 rgb(var(--shadow-ink) / .12), 0 0 0 1px rgb(var(--shadow-ink) / .08);
  --shadow-primary: 0 0 0 1px var(--ink-1);
  --shadow-toggle: var(--shadow-button);
  --shadow-card: 0 0 0 1px rgb(var(--shadow-ink) / .07), 0 1px 2px 0 rgb(var(--shadow-ink) / .12),
                 0 3px 4px -2px rgb(var(--shadow-ink) / .08);
  --shadow-table: 0 1px 2px 0 rgb(var(--shadow-ink) / .12);
  --shadow-panel: 0 0 0 0.5px var(--ink-a4), 0 1px 2px 0 rgb(var(--shadow-ink) / .015),
                  0 3px 4px -2px rgb(var(--shadow-ink) / .025);
  --shadow-menu: 0 0 0 1px rgb(var(--shadow-ink) / .08), 0 1px 2px 0 rgb(var(--shadow-ink) / .12),
                 0 4px 8px -4px rgb(var(--shadow-ink) / .16);
  --shadow-modal: 0 0 0 1px rgb(var(--shadow-ink) / .07), 0 1px 2px 0 rgb(var(--shadow-ink) / .14),
                  0 6px 8px -4px rgb(var(--shadow-ink) / .14);
  --shadow-badge: 0 1px 2px 0 color-mix(in srgb, currentColor 16%, transparent),
                  0 0 0 1px color-mix(in srgb, currentColor 14%, transparent);
  --backdrop: rgb(0 0 0 / .3);

  /* Shape: set --radius-control; the rest follow. */
  --radius-control: 6px;
  --radius-xs: calc(var(--radius-control) / 2);
  --radius-sm: calc(var(--radius-control) - 2px);
  --radius-container: calc(var(--radius-control) + 2px);
  --radius-feature: calc(var(--radius-container) * 1.5);
  --radius-sheet: 14px;

  /* Sizes */
  --control-h: 36px; --control-h-compact: 32px; --control-h-pill: 28px;
  --control-h-inline: 24px; --control-h-icon: 22px; --badge-h: 20px; --key-chip: 18px;
  --row-h: 38px;
  --switch-w: 52px; --switch-h: 26px; --switch-knob: 20px; --switch-inset: 3px;

  /* Type: Inter, one weight. Hierarchy is size + ink, never bold. */
  --font-sans: "Inter", "Helvetica Neue", Arial, sans-serif;
  --font-mono: ui-monospace, "SF Mono", "JetBrains Mono", Menlo, monospace;
  --font-weight-ui: 500;
  --text-meta: 12px;    --leading-meta: 16px;
  --text-body: 13px;    --leading-body: 20px;
  --text-title: 16px;   --leading-title: 24px;
  --text-section: 20px; --leading-section: 28px;
  --text-figure: 24px;  --leading-figure: 32px;
  --text-display: 32px; --leading-display: 40px;
  --text-field: var(--text-body);
  --tracking-label: -0.01em; --tracking-display: -0.02em;

  /* Motion */
  --dur-hover: 150ms; --dur-swap: 200ms; --dur-modal: 240ms; --dur-move: 300ms;
  --ease-out: cubic-bezier(.23, 1, .32, 1);
  --ease-move: cubic-bezier(.22, 1, .36, 1);
  --ease-drawer: cubic-bezier(.32, .72, 0, 1);
  --ease-in-out: cubic-bezier(.77, 0, .175, 1);
}

/* Phone and touch: values only. */
@media screen and (width < 48rem) {
  :root { --control-h: 44px; --row-h: 44px; --text-body: 15px; --leading-body: 24px;
          --text-meta: 15px; --leading-meta: 20px;
          --switch-w: 51px; --switch-h: 31px; --switch-knob: 23px; --switch-inset: 4px; }
}
@media (pointer: coarse) {
  :root { --text-field: 16px; }
}

/* Dark. Colour and shadow only: never padding, height, radius or border width.
   The ground is the brand black; ink-3 is the brand charcoal. */
:root[data-theme="dark"] {
  --root-ink-1: #111111; --root-ink-2: #191919; --root-ink-3: #232323; --root-ink-4: #2B2B2B;
  --root-ink-5: #333333; --root-ink-6: #3D3D3D; --root-ink-7: #4A4A4A; --root-ink-8: #626262;
  --root-ink-9: #737373; --root-ink-10: #868686; --root-ink-11: #B4B4B4; --root-ink-12: #EEEEEE;
  --ink-a3: color-mix(in oklab, var(--root-ink-12) 7%, transparent);
  --ink-a4: color-mix(in oklab, var(--root-ink-12) 11%, transparent);

  --ground: #000000;
  --background: var(--root-ink-1);
  --foreground: var(--root-ink-12);
  --primary: var(--root-ink-12);
  --primary-foreground: var(--root-ink-1);
  --secondary: var(--root-ink-3);
  --secondary-foreground: var(--root-ink-12);
  --accent: var(--root-ink-3);
  --accent-foreground: var(--root-ink-12);
  --muted-foreground: var(--root-ink-11);
  --destructive: #E54666;
  --border: rgb(255 255 255 / .1);
  --input: rgb(255 255 255 / .15);
  --ring: var(--focus-ring);
  --panel: var(--root-ink-1);
  --raised: var(--root-ink-2);
  --overlay: var(--root-ink-2);
  --control-fill: var(--root-ink-3);
  --line: var(--ink-5);
  --switch-off: #343434;
  --illo-base: var(--root-ink-1);

  --brand-3: #391A0F; --brand-4: #4A2112; --brand-6: #6B2A12;
  --brand-9: #FF5E1F; --brand-10: #FF7038; --brand-11: #FF8A5C;
  --brand-text: #FF7038;
  --focus-ring: #FF7038;
  --link: #7DA2FF;
  --chart-1: #FF7038; --chart-2: #3AAEFF; --chart-3: #2BD69A; --chart-4: #F24DE6; --chart-5: #2BB3A3;

  --red-3: #3A141E; --red-6: #6F2539; --red-9: #E54666; --red-11: #FF949D;
  --red-solid: #CA244D; --red-solid-hover: #D63A5E;
  --green-3: #0D2D2A; --green-6: #1C4F4A; --green-9: #12A594; --green-11: #0BD8B6;
  --amber-3: #302008; --amber-6: #5C3D05; --amber-9: #FFC53D; --amber-11: #FFCA16;
  --blue-3: #0D2847; --blue-6: #104D87; --blue-9: #0090FF; --blue-11: #70B8FF;

  --shadow-button: 0 0 0 0.5px var(--root-ink-6), 0 1px 2px 0 rgb(0 0 0 / .5);
  --shadow-toggle: var(--shadow-button);
  --shadow-primary: 0 0 0 0.5px var(--primary-bg), 0 1px 2px 0 rgb(0 0 0 / .5);
  --shadow-card: 0 0 0 0.5px var(--root-ink-6), 0 1px 2px 0 rgb(0 0 0 / .5), 0 3px 4px -2px rgb(0 0 0 / .4);
  --shadow-table: 0 1px 2px 0 rgb(0 0 0 / .5);
  --shadow-panel: 0 0 0 0.5px var(--ink-a3), 0 1px 2px 0 rgb(0 0 0 / .5), 0 3px 4px -2px rgb(0 0 0 / .4);
  --shadow-menu: 0 0 0 0.5px var(--root-ink-7), 0 1px 2px 0 rgb(0 0 0 / .5), 0 4px 8px -4px rgb(0 0 0 / .5);
  --shadow-popover: var(--shadow-menu);
  --shadow-modal: 0 0 0 0.5px var(--root-ink-7), 0 1px 2px 0 rgb(0 0 0 / .5), 0 6px 8px -4px rgb(0 0 0 / .5);
  --shadow-badge: 0 0 0 0.5px color-mix(in srgb, currentColor 34%, #000), 0 1px 2px 0 rgb(0 0 0 / .5);
  --backdrop: rgb(0 0 0 / .9);
}

/* Surfaces. Light: remap steps 1-7 so children keep contrast against their ground. */
:root:not([data-theme="dark"]) :is(.surface-rail, .surface-panel, .surface-overlay, .surface-raised, .surface-sunk) {
  --line: var(--ink-6); --shadow-primary: 0 0 0 1px var(--ink-1); }
:root:not([data-theme="dark"]) :is(.surface-rail, .surface-sunk) {
  --ink-1: var(--root-ink-2); --ink-2: var(--root-ink-3); --ink-3: var(--root-ink-4);
  --ink-4: var(--root-ink-5); --ink-5: var(--root-ink-6); --ink-6: var(--root-ink-7);
  --ink-7: var(--root-ink-8); }
:root:not([data-theme="dark"]) .surface-panel { --ink-1: var(--surface-top); }
:root:not([data-theme="dark"]) .surface-overlay {
  --ink-1: var(--surface-top); --ink-2: var(--surface-top); --ink-3: var(--root-ink-3);
  --ink-4: var(--root-ink-4); --ink-5: var(--root-ink-5); --ink-6: var(--root-ink-6);
  --ink-7: var(--root-ink-7); }
:root:not([data-theme="dark"]) .surface-raised {
  --ink-1: var(--root-ink-1); --ink-2: var(--root-ink-2); --ink-3: var(--root-ink-3);
  --ink-4: var(--root-ink-4); --ink-5: var(--root-ink-5); --ink-6: var(--root-ink-6);
  --ink-7: var(--root-ink-7); }

/* Dark: steps stay root; each surface redeclares the control fill and its outline,
   three steps above the fill. */
:root[data-theme="dark"] :is(.surface-panel, .surface-sunk, .surface-rail) {
  --control-fill: var(--root-ink-3);
  --shadow-button: 0 0 0 0.5px var(--root-ink-6), 0 1px 2px 0 rgb(0 0 0 / .5);
  --shadow-toggle: var(--shadow-button); }
:root[data-theme="dark"] :is(.surface-raised, .surface-overlay) {
  --control-fill: var(--root-ink-4);
  --shadow-button: 0 0 0 0.5px var(--root-ink-7), 0 1px 2px 0 rgb(0 0 0 / .5);
  --shadow-toggle: var(--shadow-button); }
```

**Base** (paste once, before the component CSS):

```css
*, *::before, *::after { box-sizing: border-box; }
html { -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; }
body { margin: 0; background: var(--ground); color: var(--ink-12); font-family: var(--font-sans); font-weight: var(--font-weight-ui);
  font-size: var(--text-body); line-height: var(--leading-body); }
h1, h2, h3, h4, p, ul, ol, figure, dl, dd { margin: 0; }
h1, h2, h3, h4, b, strong, th { font-weight: var(--font-weight-ui); }
ul { padding: 0; list-style: none; }
svg { display: block; }
code, .mono { font-family: var(--font-mono); font-size: 0.92em; }
.ink-11 { color: var(--ink-11); } .ink-10 { color: var(--ink-10); } .meta { font-size: var(--text-meta); line-height: var(--leading-meta); color: var(--ink-10); }
.sr-only { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
:root[data-theme="dark"] { color-scheme: dark; }
/* The page body: white panel floating 8px off the ground */
.panel { margin: 8px; border-radius: var(--radius-container); background: var(--panel); box-shadow: var(--shadow-panel); }
```

**Neutral steps by job:** 1–2 grounds · 3 field wells, chips, selected rows · 4 hover/focus fill · 5 pressed · 6 hairline · 7 strong line · 8 disabled text · 9 icons and decoration only · 10 meta, placeholders, table cells · 11 descriptions and body · 12 titles, values, the default button fill.

**Contrast (checked):** ink-12 on ink-3 16.1:1 (dark 13.5) · ink-11 on panel 6.7 (9.1) · ink-10 on panel 4.75 (5.19) · ink-10 on ink-3 4.05, placeholders only · ink-9 on panel 3.46, icons only · status -11 on -3: danger 4.70, success 4.79, amber 5.13, blue 5.06 · white on red-solid 5.43 · brand-11 on brand-3 5.35 · brand-text on white 4.66 · black on orange 6.7 · focus ring 3.76 on white, 3.45 on the ground, 3.21 on a well (dark 5.7–7.6) · white on orange 3.06, so never white text on orange.

## 5. Foundations

**Type** (Inter 500 everywhere; line heights are fixed px):

| Role | Size | Ink |
|---|---|---|
| Display | 32/40, −0.02em; lead words ink-11, key noun ink-12 | 12 |
| Figure | 24/32, tabular | 12 |
| Section / page title | 20/28 | 12 |
| Card, modal title | 16/24 | 12 |
| Body, controls | 13/20 (15/24 on phones) | 12 values, 11 descriptions |
| Meta | 12/16 | 10 |
| Mono | IDs, code, keys only | – |

Fields use 16px text on any touch screen (iOS zoom). Tabular figures wherever numbers line up.

**Spacing:** 4px grid with 2px half-steps: 2, 4, 6, 8, 12, 16, 20, 24, 32, 48, 64. Inside a control 4–8 · between items 8–12 · between fields 16–20 · card padding 16–24 · sections: title, 6px, description, 24px, content, 32px around · 48px above the first title, 64px page foot.

**Radius:** xs 3 · sm 4 · control 6 · container 8 · feature 12 · sheet 14 (top corners) · full for pills, badges, toggles. Nested radius = outer minus the gap or border.

**Elevation:** button = 1px border + shadow-xs · card `--shadow-card` · table `--shadow-table` + 0.5px frame · menu/popover `--shadow-menu` · modal `--shadow-modal`. Structural lines are 0.5px. Dark raises by getting lighter with one solid 0.5px outline and a black drop; never a glow or a lit top edge.

**Motion:** strong ease-out `cubic-bezier(.23,1,.32,1)` for anything the user caused. Hover/press 150ms · menu in 150/out 120 from scale .97 at the trigger · content swap and toast 200 · modal in 240 (16px rise, 4px blur, fade)/out 200 · phone sheet up 320/down 200 · toggle and switch springs 400–450ms with no overshoot past the inset. Exits are faster than entrances. Animate transform and opacity only; never `transition: all`; every transition has a reduced-motion crossfade.

**Layout:** columns 440 (form, flow) · 800 (reading, settings) · 1200 (data). Actions sit right of the section title, above the data; paging sits below the data, outside its card. Lists and overview tables stop at 5–6 rows, then a pager or "View all".

**Phone (under 768px):** 20px gutters, 44pt touch targets, 15px text floor, fields 44px tall, stacked full-width actions (confirm on top in modals and sheets), every modal becomes a bottom sheet with a grab handle, nothing hover-only.

**Icons:** one outline set (Lucide-style), round caps, ~1.5px rendered at 16px. 14px in pills, 16px in buttons and rows, 18px in empty states. Ink-9 beside a label, ink-10 in rows, ink-12 on hover. Never colour an icon to rank it, and never orange, not even when active. In code, use Lucide (ships with shadcn).

## 6. Colour roles

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

## 7. Components

Names follow shadcn/ui where one exists. Each line is the spec; section 8 has the CSS.

**Actions**
- **Button** (`.btn` + one variant + one size). Variants: `btn-default` (primary fill, hover 90%), `btn-outline` (1px `--border`, `--background`, shadow-xs, hover `--accent`; dark: input at 30%), `btn-secondary` (secondary fill, hover 80%), `btn-ghost` (fill on hover only), `btn-destructive` (destructive fill, white text; dark at 60%), `btn-link` (underline on hover, 4px offset). Sizes: `btn-xs` 24 · `btn-sm` 32 · default 36 · `btn-lg` 40 · `btn-icon-xs` 24 · `btn-icon-sm` 32 · `btn-icon` 36 · `btn-icon-lg` 40. Padding 16 (12 with an icon), sm 12 (10), lg 24 (16), xs 8 (6). Focus: 2px orange ring (`--ring`), 2px off the edge: the one place orange touches a button. Disabled: opacity .5. `rounded-full` for pills; `.btn-group` joins related buttons. Loading = spinner in the icon slot + `disabled` + `aria-busy`. One default per surface; destructive only for deleting or revoking; link only for navigation (`<a class="btn btn-link">`).
- **Icon button:** the icon sizes above, usually ghost (rows, toolbars) or outline (standalone); every one has `aria-label` and a tooltip.

**Inputs**
- **Text field:** a well: ink-3 fill, no border, 36px, 12px padding; focus ink-4 + 2px orange focus ring. Label 13/20 ink-12 6px above; help 12/16 ink-10 below; "(optional)" in ink-10 on the optional field only. Error: 1px red-11 ring as a box-shadow + 12/16 red-11 message, on blur or submit only. Read-only keeps its fill; disabled .6.
- **Textarea:** same well, min 84px, 8px vertical padding; counter 12/16 ink-10 only when a limit exists.
- **Select:** outline button trigger (min 200px, 12px sides) with a 16px chevron at 50% that turns over while open; the list is a menu. A native `<select>` in a form wears the well.
- **Search:** trigger looks like a field: white with a 0.5px ink-6 inset line and a ⌘K key pill. Inline: well with a 16px ink-9 leading icon; results in a menu; matches underlined, never coloured.
- **Checkbox / Radio:** in lists the row is the control (36px, 8px padding, 2px apart, no lines), mark at the far right; hover ink-2, selected ink-3. Marks 18px, 1.5px ink-6 ring; checked box ink-12 with an ink-1 tick; radio = 8px ink-12 dot in a white well. Inline checkbox leads its label. Radio tiles: 2 columns, 10px gap, ink-2 → ink-3. Selection cards (124px min) look pressed in when picked.
- **Switch:** 52×26 track, 20px white knob 3px in (51×31 / 23px / 4px on phones); on = primary (black; white in dark, with a dark knob), off ink-7 (dark #343434). Never orange. Takes effect at once; label names the setting.
- **Segmented control** (also the tab pattern; no underline tabs): fully round track one step darker than its surface, 4px inset, 28px options, white raised thumb that slides; 2–5 options; hugs its content.
- **Slider:** 6px track ink-4, ink-12 fill, 20px white knob; always show the value as text.
- **Date picker:** field with a calendar icon opening a 280px popover; 34px days; today = 1px ink-7 ring; selected = primary fill; typed dates accepted.
- **File upload:** ink-2 drop area with a dashed edge, also a button; files as raised rows with a 4px progress bar; failures stay listed with the reason in red-11.
- **Filter pill:** 28px, white + toggle shadow, label ink-10, value ink-12 (truncates at 180px), 20px × to clear; one row, scroll sideways on phones.

**Data display**
- **Badge:** 20px, fully round, `hue-3` fill + `hue-11` text + `--shadow-badge`; neutral = white with the button shadow; `brand` = brand-3 fill + brand-11 text, for New/Recommended only, never a status; 24px beside a 20px title; 22px on phones. Status dot (8px + word) replaces badges in tables; ongoing states pulse.
- **Avatar:** circle, ink-3 fill, ink-11 initials, 0.5px inner ring; 20/24/32/40/56; stacks overlap 6px with a 2px surface ring; "+N" after 3–4.
- **Card:** one unit of related data: `--raised` + `--shadow-card`, radius 8, 20–24px padding; optional 46px header strip with a 0.5px rule; clickable cards hover ink-2 and press to .99. Section headings sit outside the card.
- **Stat / meter:** figure 24/32 ink-12 with a 13/20 ink-10 label directly under it; meter bar 10px, red only for something running out; over 6 digits go compact (1.2M); missing = ink-9 en dash.
- **Table:** 38px rows (44 on phones), 0.5px frame and column dividers, radius 8, `--shadow-table`, 14px cells, all left-aligned, one typeface, tabular figures. Header and identifying column ink-12, other cells ink-10. Status as a dot. Hover +1, selected +2. Optional selection column: checkbox 16px in, 12px to the next cell, **no divider**; inactive rows 50% with no checkbox. Sortable headers are buttons with `aria-sort`. Free text truncates at 30–32ch with a tooltip. Actions above (swap to bulk actions when rows are selected), pager below, outside the frame.
- **List:** plain rows for navigation (36px, fill on hover, current ink-3, no lines); grouped records in one raised card of 52px rows with 0.5px rules.
- **Accordion:** 48px rows, ink-12 question, 16px chevron that turns, 0.5px dividers, 300ms height.
- **Tooltip:** ink-12 fill, ink-1 text, 12/16, radius 6, 4×8 padding, 6px offset, no delay; shows on focus too; never the only place information lives.
- **Key chip:** 18px mono chip on the page's default button only; 20px ⌘K pill in search; hidden on touch.

**Feedback**
- **Alert:** notice radius 12, 0.5px line, white, `--shadow-table`, 16×24 padding, 16/24 title + one 13/20 line, action at the right (under it on phones). Tinted: hue-3 / hue-6 / hue-11. No warning icon before the title. Inline alert: radius 6, 10×12, 16px icon.
- **Toast:** one at a time, bottom centre 24px up, 48px pill in the tone's -3 with a -6 hairline and -11 title, optional 22px solid action; 6s; never for a copy or anything already on screen.
- **Progress:** flow segments 6px, 6px apart; line 6px with ink-12 fill; ring 32px. Never "Step 1 of 4" above a bar.
- **Spinner:** 16px in buttons, 18px in panels; with a verb in -ing and "…".
- **Skeleton:** 12px ink-4 bars, radius 6, pulsing; keep labels and widths real.
- **Empty state:** bare ink-2 panel, radius 8, 40px padding, 18px icon, two lines (what's missing, what to do), at most one outline button; a failed load is the same with "Try again".

**Overlays**
- **Menu:** white (ink-2 in dark), radius 8, `--shadow-menu`, 4px padding, 36px items 2px apart; highlighted ground +1, chosen ground +2 in ink-12, **no tick**; destructive items red and last; opens from scale .97 at the trigger.
- **Popover:** 260px info (12/16 ink-11) or 300px small form, `--shadow-menu`, opens on click.
- **Modal** (dialog): 620 task · 460 confirm · 440 info. Header band 20/20/16 with a 16/24 title that asks the question + 13/20 description; body 16–20px, the only part that scrolls; footer 12px under a 0.5px rule, Cancel left, confirm right, buttons hug. Backdrop black 30% light / 90% dark with 2px blur. First focus: first field; in a confirm, the confirm; in a destructive confirm (`role="alertdialog"`, red title), the modal itself. Trap Tab, lock scroll, Escape closes, a backdrop click closes unless the form changed, focus returns to the trigger. No × when the footer has Cancel. Never stack modals; change content in place for steps, holding the size. Give-something-up: keeping is the default button. A small confirm can sit in the page without a backdrop, raised like a button.
- **Side panel:** 400–480px, full height inside an 8px float, modal structure, no dim; inspect or edit one record while the list stays usable.
- **Bottom sheet** (phones): full width, 14px top corners, top hairline only, white 36×5 grab handle 12px above it instead of ×; related details in one raised card of 48pt rows; buttons below it, full width, 8px apart; up 320ms, down 200ms; drag down past 64px to close.

**Navigation**
- **Sidebar:** rail on the ground; 36px rows, radius 6, 16px icon, ink-11 → ink-12, current ink-3 (dark ink-2); group titles 13/20 ink-9 with 16px above, no rules or chevrons; the panel floats 8px off the window, radius 8.
- **Top bar:** 52px strip in the panel: breadcrumb left, page actions right, 0.5px rule at its foot; phones: 56px bar, logo-mark breadcrumb, 44px menu button.
- **Breadcrumb:** parents ink-10 (hover ink-12), current ink-12, 14px ink-8 chevrons; replaces back buttons.
- **Pagination:** count left in ink-10 ("Showing 1 to 10 of 48"), Previous/Next outline sm right; below the data, outside the card; only when there is another page.
- **Stepper:** 32px raised discs, done = success (teal) with a white tick, waiting at 50%, 0.5px connector, 16px to the text, 32px between steps.

## 8. Component CSS

Paste after the tokens and base. Class names match section 7. This covers the core components; build the others (popover, side panel, progress, meter, accordion, selection cards, radio tiles, avatar stacks, sortable headers) from their specs in section 7 and the tokens.

```css
.logo { color: var(--el-brand-ink); }
:root[data-theme="dark"] .logo { color: var(--el-brand-inverse); }
.figure-n { font-size: var(--text-figure); line-height: var(--leading-figure); color: var(--ink-12); font-variant-numeric: tabular-nums; }
.figure-l { color: var(--ink-10); }
.spinner { width: 14px; height: 14px; border-radius: 50%; border: 1.5px solid currentColor; border-top-color: transparent; animation: spin 700ms linear infinite; }
.field { display: grid; gap: 6px; }
.field label { color: var(--ink-12); }
.field .opt { color: var(--ink-10); }
.input { appearance: none; width: 100%; height: var(--control-h); border: 0; border-radius: var(--radius-control); background: var(--ink-3); padding: 0 12px; font: inherit; font-size: var(--text-field); color: var(--ink-12); outline: none; transition: background-color var(--dur-hover) var(--ease-out), box-shadow var(--dur-hover) var(--ease-out); }
.input::placeholder { color: var(--ink-10); }
.input:focus { background: var(--ink-4); }
.input:focus-visible { box-shadow: 0 0 0 2px var(--focus-ring); }
.input[aria-invalid="true"] { box-shadow: 0 0 0 1px var(--red-11); }
.input[aria-invalid="true"]:focus-visible { box-shadow: 0 0 0 1px var(--red-11), 0 0 0 3px color-mix(in srgb, var(--red-11) 30%, transparent); }
.input:disabled { opacity: .6; cursor: not-allowed; }
.input[readonly]:focus { background: var(--ink-3); }
textarea.input { height: auto; min-height: 84px; padding: 8px 12px; resize: vertical; line-height: var(--leading-body); display: block; }
.input-wrap { position: relative; }
.input-wrap > .lead { position: absolute; left: 10px; top: 50%; width: 16px; height: 16px; margin-top: -8px; color: var(--ink-9); pointer-events: none; }
.input-wrap > .input.has-lead { padding-left: 34px; }
.input-wrap > .suffix { position: absolute; right: 12px; top: 50%; transform: translateY(-50%); color: var(--ink-10); pointer-events: none; }
.input-wrap > .input.has-suffix { padding-right: 48px; }
.select-wrap { position: relative; }
.select-wrap svg { position: absolute; right: 10px; top: 50%; width: 16px; height: 16px; margin-top: -8px; color: var(--ink-10); pointer-events: none; }
.select-wrap .input { padding-right: 32px; cursor: pointer; }
.hint { font-size: var(--text-meta); line-height: var(--leading-meta); color: var(--ink-10); }
.err { font-size: var(--text-meta); line-height: var(--leading-meta); color: var(--red-11); }
.field-foot { display: flex; justify-content: space-between; gap: 12px; }
.counter { font-size: var(--text-meta); line-height: var(--leading-meta); color: var(--ink-10); font-variant-numeric: tabular-nums; margin-left: auto; }
.select-trigger { justify-content: space-between; min-width: 200px; padding: 0 12px !important; }
.select-trigger .chev { width: 16px; height: 16px; color: var(--muted-foreground); opacity: .5; transition: transform var(--dur-swap) var(--ease-out); }
.select-trigger[aria-expanded="true"] .chev { transform: rotate(180deg); }
.select-trigger .ph { color: var(--ink-10); }
.select-trigger[aria-invalid="true"] { box-shadow: 0 0 0 1px var(--red-11); }
.kpill { display: inline-grid; place-items: center; min-width: var(--badge-h); height: var(--badge-h); padding: 0 6px; border-radius: var(--radius-xs); background: color-mix(in srgb, currentColor 14%, transparent); font-size: 12px; line-height: 16px; color: var(--ink-11); }
.choices { display: grid; gap: 2px; max-width: 360px; }
.choice { position: relative; display: flex; align-items: center; gap: 6px; min-height: 36px; padding: 0 8px; border-radius: var(--radius-control); cursor: pointer; color: var(--ink-12); transition: background-color var(--dur-hover) var(--ease-out); user-select: none; }
.choice .lbl { flex: 1; min-width: 0; }
.choice .lbl small { display: block; color: var(--ink-11); font-size: var(--text-body); }
.choice.tall { padding: 8px; align-items: flex-start; }
.choice.tall .mark { margin-top: 1px; }
.choice input { position: absolute; opacity: 0; pointer-events: none; width: 1px; height: 1px; }
.choice:has(input:checked) { background: var(--ink-3); }
.choice:has(input:disabled) { opacity: .6; cursor: not-allowed; }
.choice:has(input:focus-visible) { outline: 2px solid var(--focus-ring); outline-offset: 0; }
:root[data-theme="dark"] .choice:has(input:checked) { background: var(--root-ink-3); }
:root[data-theme="dark"] .surface-raised .choice:has(input:checked) { background: var(--root-ink-4); }
.mark { flex: none; position: relative; width: 18px; height: 18px; box-shadow: inset 0 0 0 1.5px var(--ink-6); background: var(--surface-top); transition: background-color var(--dur-hover) var(--ease-out), box-shadow var(--dur-hover) var(--ease-out); }
:root[data-theme="dark"] .mark { background: transparent; box-shadow: inset 0 0 0 1.5px var(--root-ink-7); }
.mark.box { border-radius: var(--radius-sm); }
.mark.dot { border-radius: 50%; }
.mark::after { content: ""; position: absolute; opacity: 0; transform: scale(.9); transition: opacity 150ms var(--ease-out), transform 150ms var(--ease-out); }
.mark.box::after { inset: 0; background: var(--primary-fg); -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 18 18'%3E%3Cpath d='M4.5 9.4l2.9 2.9 6-6.3' fill='none' stroke='black' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center / 18px no-repeat; mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 18 18'%3E%3Cpath d='M4.5 9.4l2.9 2.9 6-6.3' fill='none' stroke='black' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center / 18px no-repeat; }
.mark.dot::after { left: 5px; top: 5px; width: 8px; height: 8px; border-radius: 50%; background: var(--ink-12); }
input:checked + .mark.box, input:indeterminate + .mark.box { background: var(--ink-12); box-shadow: none; }
input:checked + .mark::after { opacity: 1; transform: none; }
input:indeterminate + .mark.box::after { opacity: 1; transform: none; -webkit-mask: none; mask: none; inset: 8px 4px; border-radius: 1px; }
input:checked + .mark.dot { background: var(--surface-top); box-shadow: inset 0 0 0 1.5px var(--ink-6); }
:root[data-theme="dark"] input:checked + .mark.dot { background: var(--root-ink-6); box-shadow: none; }
.switch { position: relative; flex: none; width: var(--switch-w); height: var(--switch-h); padding: var(--switch-inset); border: 0; border-radius: 999px; background: var(--switch-off); cursor: pointer; transition: background-color var(--dur-hover) var(--ease-out); display: inline-flex; justify-content: flex-start; align-items: center; }
.switch[aria-checked="true"] { background: var(--switch-on); }
.switch:focus-visible { outline: 2px solid var(--focus-ring); outline-offset: 2px; }
.switch:disabled { opacity: .6; cursor: not-allowed; }
.switch::before { content: ""; position: absolute; inset: -9px -4px; }
.switch .knob { width: var(--switch-knob); height: var(--switch-knob); border-radius: 50%; background: #FFFFFF; box-shadow: 0 1px 2px 0 rgb(0 0 0 / .2), 0 0 0 0.5px rgb(0 0 0 / .08); transform: translateX(0); transition: transform 450ms cubic-bezier(.3, 1.15, .5, 1); }
.switch[aria-checked="true"] .knob { transform: translateX(calc(var(--switch-w) - var(--switch-knob) - var(--switch-inset) * 2)); }
:root[data-theme="dark"] .switch[aria-checked="true"] .knob { background: var(--root-ink-1); }
.seg { --seg-track: var(--ink-3); position: relative; display: inline-grid; grid-auto-flow: column; grid-auto-columns: 1fr; padding: 4px; height: 36px; border-radius: 999px; background: var(--seg-track); gap: 4px; }
:root[data-theme="dark"] .seg { --seg-track: var(--root-ink-2); --control-fill: var(--root-ink-4); --shadow-toggle: 0 0 0 0.5px var(--root-ink-7), 0 1px 2px 0 rgb(0 0 0 / .5); }
.seg button { position: relative; z-index: 1; height: 28px; padding: 0 11px; border: 0; border-radius: 999px; background: none; font: inherit; letter-spacing: var(--tracking-label); color: var(--ink-11); cursor: pointer; transition: color var(--dur-hover) var(--ease-out); display: inline-flex; align-items: center; justify-content: center; gap: 4px; }
.seg button svg { width: 14px; height: 14px; }
.seg button[aria-pressed="true"] { color: var(--ink-12); }
.seg button:focus-visible { outline: 2px solid var(--focus-ring); outline-offset: 0; }
.seg .thumb { position: absolute; z-index: 0; top: 4px; left: 0; height: 28px; width: 0; border-radius: 999px; background: var(--control-fill); box-shadow: var(--shadow-toggle); transition: transform 400ms cubic-bezier(.3, 1.12, .5, 1), width 400ms cubic-bezier(.3, 1.12, .5, 1); }
.seg.no-anim .thumb { transition: none; }
.badge { display: inline-flex; align-items: center; gap: 6px; height: var(--badge-h); padding: 0 8px; border-radius: 999px; font-size: 12px; line-height: 20px; white-space: nowrap; box-shadow: var(--shadow-badge); }
.badge .dot { width: 6px; height: 6px; }
.badge.green { background: var(--green-3); color: var(--green-11); }
.badge.red { background: var(--red-3); color: var(--red-11); }
.badge.amber { background: var(--amber-3); color: var(--amber-11); }
.badge.blue { background: var(--blue-3); color: var(--blue-11); }
.badge.neutral { background: var(--control-fill); color: var(--ink-11); box-shadow: var(--shadow-button); }
.badge.brand { background: var(--brand-3); color: var(--brand-11); }
.text-brand { color: var(--brand-text); }
::selection { background: var(--selection); color: #FFFFFF; }
.badge-lg { height: 24px; font-size: 13px; line-height: 24px; padding: 0 10px; }
.dot { display: inline-block; width: 6px; height: 6px; border-radius: 50%; background: currentColor; flex: none; }
.status-dot { display: inline-flex; align-items: center; gap: 8px; color: var(--ink-11); }
.status-dot .dot { width: 8px; height: 8px; position: relative; }
.status-dot.green .dot { color: var(--green-9); }
.status-dot.red .dot { color: var(--red-9); }
.status-dot.amber .dot { color: var(--amber-9); }
.status-dot.blue .dot { color: var(--blue-9); }
.status-dot.neutral .dot { color: var(--ink-8); }
.status-dot.ping .dot::after { content: ""; position: absolute; inset: 0; border-radius: 50%; background: currentColor; animation: ping 1.6s cubic-bezier(0, 0, .2, 1) infinite; }
.avatar-i { display: inline-grid; place-items: center; flex: none; border-radius: 50%; background: var(--ink-3); color: var(--ink-11); overflow: hidden; box-shadow: inset 0 0 0 0.5px rgb(var(--shadow-ink) / .08); font-variant-numeric: tabular-nums; }
:root[data-theme="dark"] .avatar-i { background: var(--root-ink-4); box-shadow: inset 0 0 0 0.5px rgb(255 255 255 / .06); }
.avatar-i img { width: 100%; height: 100%; object-fit: cover; }
.av-20 { width: 20px; height: 20px; font-size: 10px; }
.av-24 { width: 24px; height: 24px; font-size: 11px; }
.av-32 { width: 32px; height: 32px; font-size: 12px; }
.av-40 { width: 40px; height: 40px; font-size: 14px; }
.av-56 { width: 56px; height: 56px; font-size: 18px; }
.card { background: var(--raised); border-radius: var(--radius-container); box-shadow: var(--shadow-card); padding: 20px; }
.card-title { font-size: var(--text-title); line-height: var(--leading-title); color: var(--ink-12); }
.card-head { display: flex; align-items: flex-start; justify-content: space-between; gap: 12px; }
.table-wrap { position: relative; border-radius: var(--radius-container); background: var(--raised); box-shadow: 0 0 0 var(--hairline) var(--line), var(--shadow-table); overflow-x: auto; }
.tbl { width: 100%; border-collapse: collapse; font-variant-numeric: tabular-nums; }
.tbl th, .tbl td { height: var(--row-h); padding: 0 14px; text-align: left; vertical-align: middle; white-space: nowrap; box-shadow: inset calc(var(--hairline) * -1) calc(var(--hairline) * -1) 0 0 var(--line); }
.tbl tr > :last-child { box-shadow: inset 0 calc(var(--hairline) * -1) 0 0 var(--line); }
.tbl tbody tr:last-child > * { box-shadow: inset calc(var(--hairline) * -1) 0 0 0 var(--line); }
.tbl tbody tr:last-child > :last-child { box-shadow: none; }
.tbl th { color: var(--ink-12); }
.tbl td { color: var(--ink-10); }
.tbl td:first-child { color: var(--ink-12); }
.tbl td.wrap, .tbl th.wrap { white-space: normal; padding-top: 9px; padding-bottom: 9px; }
.tbl .status { display: inline-flex; align-items: center; gap: 8px; color: var(--ink-11); }
.tbl td > .status { display: flex; }
.tbl .status .dot { width: 8px; height: 8px; }
.tbl .status.green .dot { color: var(--green-9); }
.tbl .status.amber .dot { color: var(--amber-9); }
.tbl .status.red .dot { color: var(--red-9); }
.tbl .status.neutral .dot { color: var(--ink-8); }
.tbl tbody tr { transition: background-color var(--dur-hover) var(--ease-out); }
.tbl tbody tr[aria-selected="true"] { background: var(--ink-3); }
:root[data-theme="dark"] .tbl tbody tr[aria-selected="true"] { background: var(--root-ink-4); }
.tbl .trunc { max-width: 30ch; overflow: hidden; text-overflow: ellipsis; }
.tbl td.act, .tbl th.act { width: 1%; padding: 0 8px; }
.tbl td.act .btn { vertical-align: middle; margin: -4px 0; }
.tbl .inactive td { opacity: .5; }
.tbl.sel tbody td:nth-child(2), .tbl.sel thead th:nth-child(2) { padding-left: 12px; }
.tbl.sel tbody td:nth-child(2) { color: var(--ink-12); }
.tbl.sel tbody td:first-child { color: inherit; }
.tbl th.chk, .tbl td.chk { width: 1%; padding: 0 0 0 16px; box-shadow: inset 0 calc(var(--hairline) * -1) 0 0 var(--line); }
.tbl tbody tr:last-child > td.chk { box-shadow: none; }
.tbl .row-check { position: relative; display: flex; align-items: center; justify-content: center; width: 18px; height: var(--row-h); cursor: pointer; }
.tbl .row-check::after { content: ""; position: absolute; inset: 0 -8px; }
.tbl .row-check input { position: absolute; opacity: 0; width: 1px; height: 1px; }
.tbl .row-check:has(input:focus-visible) .mark { outline: 2px solid var(--focus-ring); outline-offset: 2px; }
.skel-bar { display: inline-block; height: 12px; border-radius: var(--radius-control); background: var(--ink-4); animation: pulse 1.6s ease-in-out infinite; vertical-align: middle; }
.skel { display: grid; gap: 10px; }
.skel i { display: block; height: 12px; border-radius: var(--radius-control); background: var(--ink-4); animation: pulse 1.6s ease-in-out infinite; }
:root[data-theme="dark"] .skel i, :root[data-theme="dark"] .skel-bar { background: var(--root-ink-4); }
.dash { color: var(--ink-9); }
.menu-anchor { position: relative; display: inline-block; }
.menu { --menu-hover: var(--root-ink-2); --menu-chosen: var(--root-ink-3); position: absolute; top: calc(100% + 6px); left: 0; z-index: 100; min-width: 200px; padding: 4px; display: grid; gap: 2px; background: var(--overlay); border-radius: var(--radius-container); box-shadow: var(--shadow-menu); transform-origin: top left; opacity: 0; transform: scale(.97); pointer-events: none; visibility: hidden; transition: opacity 120ms var(--ease-out), transform 120ms var(--ease-out), visibility 0s linear 120ms; }
:root[data-theme="dark"] .menu { --menu-hover: var(--root-ink-3); --menu-chosen: var(--root-ink-4); }
.menu.open { opacity: 1; transform: none; pointer-events: auto; visibility: visible; transition: opacity 150ms var(--ease-out), transform 150ms var(--ease-out), visibility 0s; }
.menu button { height: 36px; padding: 0 10px; border: 0; border-radius: var(--radius-control); background: none; text-align: left; font: inherit; color: var(--ink-11); cursor: pointer; transition: background-color var(--dur-hover) var(--ease-out); }
.menu button:focus-visible { background: var(--menu-hover); color: var(--ink-12); outline: none; }
.menu button[aria-checked="true"] { background: var(--menu-chosen); color: var(--ink-12); }
.menu .sep { height: var(--hairline); background: var(--line); margin: 4px -4px; }
.menu .danger { color: var(--red-11); }
.menu .mi { display: flex; align-items: center; gap: 8px; }
.menu .mi svg { width: 16px; height: 16px; color: var(--ink-10); }
.menu .mi.danger svg { color: inherit; }
.menu .mi .kchip { margin-left: auto; }
.scrim { position: fixed; inset: 0; z-index: 100; background: var(--backdrop); backdrop-filter: blur(2px); -webkit-backdrop-filter: blur(2px); opacity: 0; visibility: hidden; transition: opacity 200ms var(--ease-out), visibility 0s linear 200ms; }
.scrim.open { opacity: 1; visibility: visible; transition: opacity 240ms var(--ease-out), visibility 0s; }
.dialog { width: min(460px, 100%); background: var(--overlay); border-radius: var(--radius-container); box-shadow: var(--shadow-modal); }
.dialog-head { padding: 20px 20px 16px; }
.dialog-title { font-size: var(--text-title); line-height: var(--leading-title); color: var(--ink-12); }
.dialog-title.danger { color: var(--red-11); }
.dialog-foot { display: flex; justify-content: space-between; gap: 8px; padding: 12px; box-shadow: 0 calc(var(--hairline) * -1) 0 0 var(--line); }
.dialog .dialog-head + .dialog-foot { box-shadow: 0 calc(var(--hairline) * -1) 0 0 var(--line); }
.modal { position: fixed; left: 50%; top: 50%; z-index: 101; width: min(620px, calc(100vw - 32px)); max-height: calc(100dvh - 32px); display: flex; flex-direction: column; background: var(--overlay); border-radius: var(--radius-container); box-shadow: var(--shadow-modal); opacity: 0; visibility: hidden; transform: translate(-50%, calc(-50% + 16px)); filter: blur(4px); transition: opacity 200ms var(--ease-out), transform 200ms var(--ease-out), filter 200ms var(--ease-out), visibility 0s linear 200ms; }
.modal.sm { width: min(460px, calc(100vw - 32px)); }
.modal.info { width: min(440px, calc(100vw - 32px)); }
.modal.open { opacity: 1; visibility: visible; transform: translate(-50%, -50%); filter: none; transition: opacity 240ms var(--ease-out), transform 240ms var(--ease-out), filter 240ms var(--ease-out), visibility 0s; }
.modal:focus { outline: none; }
.modal .dialog-head { flex: none; position: relative; }
.modal .dialog-body { padding: 16px 20px 20px; overflow: auto; display: grid; gap: 20px; box-shadow: 0 calc(var(--hairline) * -1) 0 0 var(--line); }
.modal .dialog-foot { flex: none; }
.modal .x-close { position: absolute; top: 16px; right: 12px; }
.modal.info .dialog-head { padding-right: 48px; }
:root[data-theme="dark"] .modal .dialog-head, :root[data-theme="dark"] .dialog .dialog-head { background: var(--root-ink-3); border-radius: var(--radius-container) var(--radius-container) 0 0; }
.toast { position: fixed; left: 50%; bottom: calc(24px + env(safe-area-inset-bottom)); z-index: 120; display: flex; align-items: center; gap: 12px; height: 48px; padding: 0 20px; border-radius: 999px; background: var(--hue-3, var(--green-3)); color: var(--hue-11, var(--green-11)); box-shadow: 0 0 0 var(--hairline) var(--hue-6, var(--green-6)), var(--shadow-badge); opacity: 0; transform: translate(-50%, 8px); pointer-events: auto; transition: opacity 150ms var(--ease-out), transform 150ms var(--ease-out); }
.toast.show { opacity: 1; transform: translate(-50%, 0); transition-duration: 200ms; }
.toast svg { width: 16px; height: 16px; }
.toast.has-action { padding-right: 13px; }
:root[data-theme="dark"] .toast .tt { color: var(--hue-9, var(--green-9)); }
.toast .act { height: 22px; padding: 0 8px; border: 0; border-radius: 999px; background: var(--hue-9, var(--green-9)); color: #FFFFFF; font: inherit; font-size: 12px; cursor: pointer; }
.toast.hue-amber .act { color: #111111; }
.notice { display: flex; align-items: center; justify-content: space-between; gap: 16px; padding: 16px 24px; border-radius: var(--radius-feature); background: var(--raised); box-shadow: 0 0 0 var(--hairline) var(--line), var(--shadow-table); }
.notice .t { font-size: var(--text-title); line-height: var(--leading-title); color: var(--ink-12); }
.notice .d { color: var(--ink-11); }
.notice.tint { box-shadow: 0 0 0 var(--hairline) var(--hue-6); background: var(--hue-3); }
.notice.tint .t, .notice.tint .d { color: var(--hue-11); }
.notice.tint .d { opacity: .9; }
.hue-red { --hue-3: var(--red-3); --hue-6: var(--red-6); --hue-11: var(--red-11); --hue-9: var(--red-9); }
.hue-green { --hue-3: var(--green-3); --hue-6: var(--green-6); --hue-11: var(--green-11); --hue-9: var(--green-9); }
.hue-amber { --hue-3: var(--amber-3); --hue-6: var(--amber-6); --hue-11: var(--amber-11); --hue-9: var(--amber-9); }
.hue-blue { --hue-3: var(--blue-3); --hue-6: var(--blue-6); --hue-11: var(--blue-11); --hue-9: var(--blue-9); }
.inline-alert { display: flex; gap: 8px; align-items: flex-start; padding: 10px 12px; border-radius: var(--radius-control); background: var(--hue-3); color: var(--hue-11); box-shadow: 0 0 0 var(--hairline) var(--hue-6); }
.inline-alert svg { width: 16px; height: 16px; margin-top: 2px; flex: none; }
.empty { display: grid; justify-items: center; align-content: center; gap: 2px; padding: 40px 24px; border-radius: var(--radius-container); background: var(--ink-2); text-align: center; }
:root[data-theme="dark"] .empty { background: var(--root-ink-2); }
.empty svg { width: 18px; height: 18px; color: var(--ink-9); margin-bottom: 8px; }
.empty p { color: var(--ink-11); }
.empty p:first-of-type { color: var(--ink-12); }
.empty .btn { margin-top: 12px; }
.tip-wrap { position: relative; display: inline-flex; }
.tip { position: absolute; left: 50%; bottom: calc(100% + 6px); transform: translateX(-50%); z-index: 120; padding: 4px 8px; border-radius: var(--radius-control); background: var(--ink-12); color: var(--ink-1); font-size: 12px; line-height: 16px; white-space: nowrap; pointer-events: none; opacity: 0; visibility: hidden; }
:root:not([data-theme="dark"]) .tip { color: #FFFFFF; }
.tip.bottom { bottom: auto; top: calc(100% + 6px); }
.tip-wrap:hover .tip, .tip-wrap:focus-within .tip, .tip.show { opacity: 1; visibility: visible; }
.tip .kpill { color: inherit; height: 16px; min-width: 16px; padding: 0 4px; font-size: 11px; margin-left: 6px; }
.kchip { display: inline-grid; place-items: center; min-width: var(--key-chip); height: var(--key-chip); padding: 0 4px; border-radius: var(--radius-xs); background: color-mix(in srgb, currentColor 14%, transparent); font-family: var(--font-mono); font-size: 11px; line-height: 1; color: var(--ink-11); }
.keys { display: inline-flex; gap: 4px; align-items: center; }
.crumbs { display: flex; align-items: center; gap: 4px; min-width: 0; color: var(--ink-10); white-space: nowrap; }
.crumbs a, .crumbs span { overflow: hidden; text-overflow: ellipsis; text-decoration: none; }
.crumbs a { color: var(--ink-10); border-radius: var(--radius-xs); transition: color var(--dur-hover) var(--ease-out); }
.crumbs a:focus-visible { outline: 2px solid var(--focus-ring); outline-offset: 2px; }
.crumbs [aria-current="page"] { color: var(--ink-12); }
.crumbs svg { width: 14px; height: 14px; flex: none; color: var(--ink-8); }
.pager { display: flex; align-items: center; justify-content: space-between; gap: 12px; }
.pager .count { color: var(--ink-10); font-variant-numeric: tabular-nums; }
.pager .btns { display: flex; gap: 8px; }

/* Button (shadcn/ui): variant = default | outline | secondary | ghost | destructive | link;
   size = default | xs | sm | lg | icon | icon-xs | icon-sm | icon-lg */
.btn { appearance: none; margin: 0; display: inline-flex; flex-shrink: 0; align-items: center; justify-content: center; gap: 8px; height: 36px; padding: 0 16px; border: 1px solid transparent; border-radius: var(--radius); font: inherit; font-size: var(--text-body); line-height: var(--leading-body); font-weight: var(--font-weight-ui); letter-spacing: normal; white-space: nowrap; text-decoration: none; cursor: pointer; user-select: none; -webkit-tap-highlight-color: transparent; outline: none; background: var(--primary); color: var(--primary-foreground); box-shadow: none; transition: color 150ms, background-color 150ms, border-color 150ms, box-shadow 150ms, opacity 150ms; }
.btn svg { width: 16px; height: 16px; flex-shrink: 0; pointer-events: none; }
.btn:has(> svg, > .spinner) { padding-inline: 12px; }
.btn:focus-visible { outline: 2px solid var(--ring); outline-offset: 2px; }
.btn:disabled, .btn[aria-disabled="true"] { opacity: .5; pointer-events: none; cursor: default; }
.btn[aria-invalid="true"] { border-color: var(--destructive); box-shadow: 0 0 0 3px color-mix(in srgb, var(--destructive) 20%, transparent); }
.btn .spinner { width: 16px; height: 16px; }
.btn .kbd { display: inline-grid; place-items: center; min-width: var(--key-chip); height: var(--key-chip); padding: 0 4px; border-radius: var(--radius-xs); background: color-mix(in srgb, currentColor 14%, transparent); font-family: var(--font-mono); font-size: 11px; line-height: 1; letter-spacing: 0; }
.btn-default { background: var(--primary); color: var(--primary-foreground); }
.btn-default:hover { background: color-mix(in srgb, var(--primary) 90%, transparent); }
.btn-outline { background: var(--background); color: var(--foreground); border-color: var(--border); box-shadow: var(--shadow-xs); }
.btn-outline:hover { background: var(--accent); color: var(--accent-foreground); }
:root[data-theme="dark"] .btn-outline { background: color-mix(in srgb, var(--input) 30%, transparent); border-color: var(--input); }
:root[data-theme="dark"] .btn-outline:hover { background: color-mix(in srgb, var(--input) 50%, transparent); }
.btn-secondary { background: var(--secondary); color: var(--secondary-foreground); }
.btn-secondary:hover { background: color-mix(in srgb, var(--secondary) 80%, transparent); }
.btn-ghost { background: transparent; color: var(--foreground); }
.btn-ghost:hover { background: var(--accent); color: var(--accent-foreground); }
:root[data-theme="dark"] .btn-ghost:hover { background: color-mix(in srgb, var(--accent) 50%, transparent); }
.btn-destructive { background: var(--destructive); color: #FFFFFF; }
.btn-destructive:hover { background: color-mix(in srgb, var(--destructive) 90%, transparent); }
:root[data-theme="dark"] .btn-destructive { background: color-mix(in srgb, var(--destructive) 60%, transparent); }
.btn-link { background: transparent; color: var(--primary); text-underline-offset: 4px; }
.btn-link:hover { text-decoration: underline; }
.text-destructive { color: var(--destructive) !important; }
.btn-ghost.text-destructive:hover { background: color-mix(in srgb, var(--destructive) 10%, transparent); }
:root[data-theme="dark"] .text-destructive { color: var(--red-11) !important; }
.btn-xs { height: 24px; gap: 4px; padding: 0 8px; font-size: 12px; line-height: 16px; }
.btn-xs:has(> svg) { padding-inline: 6px; }
.btn-xs svg { width: 12px; height: 12px; }
.btn-sm { height: 32px; gap: 6px; padding: 0 12px; }
.btn-sm:has(> svg, > .spinner) { padding-inline: 10px; }
.btn-lg { height: 40px; padding: 0 24px; }
.btn-lg:has(> svg, > .spinner) { padding-inline: 16px; }
.btn-icon, .btn-icon-xs, .btn-icon-sm, .btn-icon-lg { padding: 0 !important; }
.btn-icon { width: 36px; height: 36px; }
.btn-icon-xs { width: 24px; height: 24px; }
.btn-icon-xs svg { width: 12px; height: 12px; }
.btn-icon-sm { width: 32px; height: 32px; }
.btn-icon-lg { width: 40px; height: 40px; }
.btn-block { width: 100%; }
.rounded-full { border-radius: 999px !important; }
.btn-group { display: inline-flex; align-items: stretch; width: fit-content; }
.btn-group > .btn:not(:first-child) { border-top-left-radius: 0; border-bottom-left-radius: 0; border-left-width: 0; }
.btn-group > .btn:not(:last-child) { border-top-right-radius: 0; border-bottom-right-radius: 0; }
.btn-group > .btn:focus-visible { position: relative; z-index: 1; }
.btn-group > .btn-default:not(:first-child), .btn-group > .btn-secondary:not(:first-child) { border-left: 1px solid color-mix(in srgb, currentColor 20%, transparent); }

@media (hover: hover) and (pointer: fine) {
  .menu button:hover:not([aria-checked="true"]) { background: var(--menu-hover); color: var(--ink-12); }
  .menu .danger:hover { background: var(--red-3); color: var(--red-11); }
  .crumbs a:hover { color: var(--ink-12); }
  .choice:hover:not(:has(input:checked)):not(:has(input:disabled)) { background: var(--ink-2); }
  :root[data-theme="dark"] .choice:hover:not(:has(input:checked)):not(:has(input:disabled)) { background: var(--root-ink-2); }
  :root[data-theme="dark"] .surface-raised .choice:hover:not(:has(input:checked)):not(:has(input:disabled)) { background: var(--root-ink-3); }
  .tbl.hoverable tbody tr:hover:not([aria-selected="true"]) { background: var(--ink-2); }
  :root[data-theme="dark"] .tbl.hoverable tbody tr:hover:not([aria-selected="true"]) { background: var(--root-ink-3); }
}
@media screen and (width < 48rem) {
  .badge { height: 22px; font-size: 14px; line-height: 22px; }
  .seg { height: 42px; }
  .seg button, .seg .thumb { height: 34px; }
  .tbl th, .tbl td { font-size: 15px; }
  .tbl .row-check { height: 44px; }
  .notice { flex-direction: column; align-items: stretch; }
  .select-trigger { width: 100%; }
  /* Modals become bottom sheets */
  .modal, .modal.sm, .modal.info { left: 0; right: 0; top: auto; bottom: 0; width: 100%; max-height: calc(100dvh - 48px); border-radius: var(--radius-sheet) var(--radius-sheet) 0 0; transform: translateY(calc(100% + 48px)); filter: none; }
  .modal.open { transform: none; transition: transform 320ms var(--ease-drawer), opacity 200ms, visibility 0s; }
  .modal .dialog-head { padding-top: 24px; }
  .modal .dialog-title { font-size: 20px; line-height: 28px; }
  .modal .dialog-foot { flex-direction: column-reverse; gap: 8px; padding: 12px 20px calc(20px + env(safe-area-inset-bottom)); box-shadow: none; }
  .modal .dialog-foot .btn { width: 100%; }
  .modal .x-close { display: none; }
  .modal.info .dialog-head { padding-right: 20px; }
}
@media (prefers-reduced-motion: reduce) {
  .seg .thumb { transition: none; }
  .menu, .menu.open { transform: none; }
  .toast, .toast.show { transform: translate(-50%, 0); }
  .modal, .modal.open { transform: translate(-50%, -50%); filter: none; transition: opacity 200ms var(--ease-out), visibility 0s; }
  .btn { transition: none; }
}
@media (prefers-reduced-motion: reduce) and (width < 48rem) {
  .modal, .modal.open { transform: none; }
}
@media (hover: none) {
  .tip-wrap:hover .tip { opacity: 0; visibility: hidden; }
}
@media (pointer: coarse) {
  .btn .kbd { display: none; }
}
@keyframes spin { to { transform: rotate(360deg); } }
@keyframes ping { 75%, 100% { transform: scale(2.2); opacity: 0; } }
@keyframes pulse { 50% { opacity: .5; } }
```

**Markup recipes**

```html
<!-- Buttons -->
<button class="btn btn-default">Create project</button>
<button class="btn btn-outline btn-sm"><svg>…</svg>New project</button>
<button class="btn btn-ghost btn-icon-sm" aria-label="Edit"><svg>…</svg></button>
<button class="btn btn-default" disabled aria-busy="true"><span class="spinner"></span>Saving…</button>

<!-- Field -->
<div class="field">
  <label for="name">Project name</label>
  <input id="name" class="input" placeholder="E.g. Claims portal" aria-describedby="name-h">
  <p class="hint" id="name-h">Everyone in the workspace sees this name.</p>
</div>

<!-- Choice row and switch -->
<label class="choice"><span class="lbl">Email</span><input type="checkbox" checked><span class="mark box"></span></label>
<button class="switch" role="switch" aria-checked="true" aria-label="Email alerts"><span class="knob"></span></button>

<!-- Segmented control (JS sets the thumb's width and translateX to the pressed option) -->
<div class="seg" role="radiogroup" aria-label="Range"><span class="thumb"></span>
  <button role="radio" aria-pressed="true">Week</button><button role="radio" aria-pressed="false">Month</button></div>

<!-- Badge and status dot -->
<span class="badge green"><span class="dot"></span>Live</span>
<span class="status-dot amber"><span class="dot"></span>In review</span>

<!-- Card -->
<div class="card surface-raised"><p class="card-title">Processed claims</p><p class="figure-n">12,480</p><p class="figure-l">Last 7 days</p></div>

<!-- Table with selection -->
<div class="table-wrap surface-raised"><table class="tbl hoverable sel" aria-label="Claims">
  <thead><tr><th class="chk"><label class="row-check"><input type="checkbox" aria-label="Select all"><span class="mark box"></span></label></th><th>Claim</th><th>Status</th></tr></thead>
  <tbody><tr><td class="chk"><label class="row-check"><input type="checkbox" aria-label="Select CLM-1042"><span class="mark box"></span></label></td><td>CLM-1042</td><td><span class="status green"><span class="dot"></span>Approved</span></td></tr></tbody>
</table></div>
<div class="pager"><span class="count">Showing 1 to 10 of 48</span><div class="btns"><button class="btn btn-outline btn-sm" disabled>Previous</button><button class="btn btn-outline btn-sm">Next</button></div></div>

<!-- Menu -->
<div class="menu-anchor"><button class="btn btn-outline select-trigger" aria-haspopup="menu" aria-expanded="false">Sort: Newest<svg class="chev">…</svg></button>
  <div class="menu surface-overlay" role="menu"><button role="menuitemradio" aria-checked="true">Newest</button><button role="menuitemradio" aria-checked="false">Oldest</button></div></div>

<!-- Modal (add .open to both to show) -->
<div class="scrim"></div>
<div class="modal surface-overlay" role="dialog" aria-modal="true" aria-labelledby="t" aria-describedby="d">
  <div class="dialog-head"><p class="dialog-title" id="t">Create project</p><p class="ink-11" id="d">Projects group claims from one client.</p></div>
  <div class="dialog-body">…fields…</div>
  <div class="dialog-foot"><button class="btn btn-outline">Cancel</button><button class="btn btn-default">Create project</button></div>
</div>

<!-- Alert, toast, empty -->
<div class="notice tint hue-amber"><div><p class="t">3 claims need a second reviewer</p><p class="d">They are over the high-value limit.</p></div><button class="btn btn-outline">Review</button></div>
<div class="toast hue-green show" role="status"><span class="tt">Export finished</span></div>
<div class="empty"><svg>…</svg><p>No claims yet</p><p>Claims from connected systems show up here.</p></div>
```

**Behaviour the CSS expects**

```js
// Segmented control: slide the thumb under the pressed option (instant on first paint).
function placeThumb(seg, instant) {
  const on = seg.querySelector('[aria-pressed="true"]'), th = seg.querySelector('.thumb');
  if (instant) seg.classList.add('no-anim');
  th.style.width = on.offsetWidth + 'px';
  th.style.transform = `translateX(${on.offsetLeft}px)`;
  if (instant) { th.offsetWidth; seg.classList.remove('no-anim'); }
}
// Menus, modals and toasts show with the `.open` / `.show` class.
// Switch: toggle aria-checked. Modal: add .open to .scrim and .modal, focus per section 7, trap Tab,
// Escape closes, return focus to the trigger.
```

## 9. Copy

Sentence case everywhere (labels, buttons, titles). Verb-first button labels that name the action ("Delete project", not "OK"). The real ellipsis "…", never three dots; loading labels use the -ing form ("Saving…"). No em dashes in interface copy. Descriptions are one sentence that explains, not one that repeats the title. Missing values are an en dash. Format money and dates with the user's locale (Indonesian Rupiah: "Rp 12.900.000").

## 10. Before you ship

None of these may be true:

- The logo is recoloured, stretched, retyped, given effects, below 180px wide, or black on a dark surface.
- Two default buttons side by side, or a destructive button on something that doesn't delete or revoke.
- Orange on a button, checkbox, switch, active tab, selected row, link, the logo or body text.
- A status hue used for decoration or importance, or orange used to mean a status.
- A gradient anywhere, an illustration in any colour but grey, white and orange, or the logo used as decoration.
- Hierarchy made with bold or colour instead of size and ink.
- Text someone must read below 4.5:1 contrast.
- Structural lines thicker than 0.5px, double borders, mismatched nested radii.
- Big soft shadows; in dark, a glow, a lit top edge or an outline over 0.5px.
- Dark mode that changes padding, height, radius or border width.
- Actions below the data they act on, or a pager inside a table's frame.
- Layout that jumps when data or a loading state arrives.
- Title Case labels, three dots instead of "…", em dashes in interface copy.
- A toast for a copy, or a tick on the chosen menu item.
- A transition with no reduced-motion version, or hover-only information.
- Touch targets under 44pt, or fields under 16px on touch screens.

Check at 4–8× zoom, in both themes, with the longest real data, at phone width.

## 11. Review mode

When asked to make existing work match Enterlabs: inventory its colours, type, spacing, radius, shadows, components and copy; compare each with this file; report a table of findings (what, where, expected, fix) first; then apply the fixes the user agrees to (or all of them when the user asked for the fix outright) and report what changed.