# Enterlabs · 5. Foundations (v0.3)

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
