# Enterlabs · 7. Components (v0.3)

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
