# Enterlabs · 4. Tokens (v0.3)

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
