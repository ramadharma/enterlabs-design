# Enterlabs · 2. Brand and logo (v0.3)

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
