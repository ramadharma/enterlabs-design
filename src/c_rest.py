from dsl import *
from icons import I

# ============ FEEDBACK ============
page('alert', 'Alert', 'Feedback',
 'A notice on the page about something that needs attention. Title, one line, and the action at the right. No icon before the title.',
 sec('Notice', 'Neutral by default.', '''
<div class="notice"><div><p class="t">Connect your claims system</p><p class="d">New claims will be scored as soon as they arrive.</p></div><button class="btn btn-outline">Connect</button></div>'''),
 sec('Tinted', 'For status. The tint carries the meaning, so there is no warning icon.', '''
<div class="stack">
 <div class="notice tint hue-amber"><div><p class="t">3 claims need a second reviewer</p><p class="d">They are over the high-value limit.</p></div><button class="btn btn-outline">Review</button></div>
 <div class="notice tint hue-red"><div><p class="t">The claims feed stopped</p><p class="d">Last claim received 2 hours ago. Check the connection.</p></div><button class="btn btn-outline">Check connection</button></div>
 <div class="notice tint hue-blue"><div><p class="t">Fraud model v3 is in beta</p><p class="d">Scores may shift while we tune it.</p></div></div>
</div>'''),
 sec('Inline', 'Small, inside a form or card, right where it applies.', f'''
<div class="stack" style="max-width:440px">
 <div class="inline-alert hue-amber">{I('info')}<span>This client has 2 open claims for the same incident.</span></div>
 <div class="inline-alert hue-green">{I('check')}<span>Bank details verified.</span></div>
</div>'''),
 specs([
  ('Notice', 'Radius 12, 0.5px line, white, table drop', '--radius-feature'),
  ('Padding', '16px × 24px', '–'),
  ('Title', '16/24 ink-12; one 13/20 line under it', '--text-title'),
  ('Tinted', 'hue-3 fill, hue-6 edge, hue-11 text', '--amber-3'),
  ('Inline', 'Radius 6, 10px × 12px, 16px icon', '–'),
  ('Phone', 'The action moves under the text, full width', '–'),
 ]),
 usage(['Say what happened and what to do, in two lines.', 'Show one notice at a time, the most urgent first.'], ['Put a warning icon before the title.', 'Use an alert for a result the person just caused: show it in place.']),
 a11y(['Urgent alerts use <code>role="alert"</code>; others <code>role="status"</code>.']),
 code('''<div class="notice tint hue-amber">
  <div><p class="t">3 claims need a second reviewer</p><p class="d">They are over the limit.</p></div>
  <button class="btn btn-outline">Review</button>
</div>'''))

page('toast', 'Toast', 'Feedback',
 'Tells the person about a result they can\'t otherwise see. One at a time, bottom centre, gone after 6 seconds.',
 sec('Try it', 'A new toast replaces the one on screen.', '''
<div class="row">
 <button class="btn btn-outline" data-toast="Export finished" data-tone="green">Success</button>
 <button class="btn btn-outline" data-toast="Couldn't save the rule" data-tone="red" data-action="Retry">Error with action</button>
 <button class="btn btn-outline" data-toast="Sync paused while offline" data-tone="amber">Warning</button>
</div>'''),
 sec('Anatomy', None, f'''
<div class="stack" style="justify-items:start">
 <div class="toast toast-static hue-green" role="status"><span class="tt">Export finished</span></div>
 <div class="toast toast-static has-action hue-red" role="status"><span class="tt">Couldn't save the rule</span><button class="act">Retry</button></div>
</div>'''),
 specs([
  ('Shape', '48px pill, fully round', '–'),
  ('Colour', 'Tone -3 fill, -6 hairline, -11 title (-9 in dark)', '--green-3'),
  ('Action', '22px solid pill in the tone -9', '–'),
  ('Position', 'Bottom centre, 24px up; above the home bar on phones', '–'),
  ('Timing', 'Auto-dismiss after 6s; in 200ms, out 150ms', '--dur-swap'),
  ('Layer', 'z 120', '–'),
 ]),
 usage(['Toast a background job that finished, or an error from a closed modal.', 'Offer one action at most.'], ['Toast a copy: the icon turns into a tick.', 'Toast anything already visible on screen.', 'Stack toasts.']),
 a11y(['Render in a <code>role="status"</code> live region; errors use <code>role="alert"</code>.', 'Pause the timer while hovered or focused.']),
 code('<div class="toast hue-green" role="status"><span class="tt">Export finished</span></div>'))

page('progress', 'Progress', 'Feedback',
 'Shows how far along something is. Segments for steps in a flow, a line for a task with a known end, and a ring when space is tight.',
 sec('Variants', None, '''
<div class="stack" style="gap:28px">
 <div><p class="ink-11" style="margin-bottom:10px">Flow, step 2 of 4</p><div class="progress-seg" role="progressbar" aria-label="Setup progress" aria-valuenow="2" aria-valuemin="0" aria-valuemax="4"><i class="on"></i><i class="on"></i><i></i><i></i></div></div>
 <div><div class="meter-top" style="max-width:360px;margin-bottom:10px"><span class="l">Importing claims</span><span class="a" id="pl-v">40%</span></div><div class="progress-line" role="progressbar" aria-label="Importing claims" aria-valuenow="40"><i id="pl" style="width:40%"></i></div><div class="row" style="margin-top:12px"><button class="btn btn-outline btn-sm" id="pl-btn">Run</button></div></div>
 <div><p class="ink-11" style="margin-bottom:10px">Unknown length</p><div class="progress-line indet" role="progressbar" aria-label="Loading"><i></i></div></div>
 <div class="row"><svg class="ring" viewBox="0 0 32 32" role="progressbar" aria-label="Upload" aria-valuenow="65"><circle class="tr" cx="16" cy="16" r="13"/><circle class="fl" cx="16" cy="16" r="13" stroke-dasharray="81.7" stroke-dashoffset="28.6"/></svg><span class="ink-11">65% uploaded</span></div>
</div>'''),
 specs([
  ('Segments', '6px tall, 6px apart, ink-4 track, ink-12 done', '–'),
  ('Line', '6px, ink-12 fill, eases to each new value', '--dur-move'),
  ('Ring', '32px, 3px stroke', '–'),
  ('Meter', 'Quantity against a limit uses the 10px meter', '–'),
 ]),
 usage(['Let the bar\'s accessible name say the step count.', 'Use a determinate bar whenever the end is known.'], ['Put "Step 1 of 4" above a progress bar.', 'Use red or green for progress.']),
 a11y(['<code>role="progressbar"</code> with <code>aria-valuenow</code>, min and max; omit the value when unknown.', 'The indeterminate bar becomes a static pulse under reduced motion.']),
 code('''<div class="progress-line" role="progressbar" aria-valuenow="40"><i style="width:40%"></i></div>'''))

page('spinner', 'Spinner', 'Feedback',
 'For a short wait inside something: a button saving, a panel loading. For whole layouts, prefer a skeleton.',
 sec('Sizes and places', None, '''
<div class="row" style="gap:32px;align-items:center">
 <span class="spinner" aria-label="Loading"></span><span class="spinner s18" aria-label="Loading"></span><span class="spinner s24" aria-label="Loading"></span>
 <button class="btn btn-default" aria-busy="true" style="min-width:120px"><span class="spinner"></span>Saving…</button>
 <button class="btn btn-outline" aria-busy="true"><span class="spinner"></span>Loading…</button>
</div>'''),
 sec('In an empty layout', 'A spinner in place of the empty-state icon, with no description.', '''
<div class="empty" style="max-width:420px"><span class="spinner s18" style="color:var(--ink-10);margin-bottom:8px"></span><p>Loading projects…</p></div>'''),
 specs([
  ('Size', '14px in buttons, 18px in panels, 24px on phones', '–'),
  ('Stroke', '1.5px, the ink of its container', '–'),
  ('Speed', 'One turn in 700ms, linear', '–'),
  ('Label', 'A verb ending in -ing and "…"', '–'),
 ]),
 usage(['Swap the button label in place: "Saving…".', 'Say honestly what is happening.'], ['Show a spinner over a whole page.', 'Show a wrong label while loading.']),
 a11y(['Set <code>aria-busy="true"</code> on the region; announce completion in a live region.']),
 code('<button class="btn btn-default" aria-busy="true"><span class="spinner"></span>Saving…</button>'))

page('skeleton', 'Skeleton', 'Feedback',
 'Holds the shape of content while it loads, so nothing jumps when it arrives. Labels stay; only values pulse.',
 sec('Card', None, '''
<div class="grid-2"><div class="skel-card surface-raised"><p class="card-title">Processed claims</p><div class="skel"><i class="fig"></i><i style="width:30%"></i></div></div>
<div class="skel-card surface-raised"><p class="card-title">Recent activity</p><div class="skel"><i style="width:90%"></i><i style="width:75%"></i><i style="width:82%"></i></div></div></div>'''),
 sec('List', None, '''
<div class="rows-card surface-raised"><div><span class="avatar-i av-32"></span><div class="grow skel" style="gap:8px"><i style="width:40%"></i><i style="width:60%;height:10px"></i></div></div><div><span class="avatar-i av-32"></span><div class="grow skel" style="gap:8px"><i style="width:52%"></i><i style="width:44%;height:10px"></i></div></div></div>'''),
 specs([
  ('Bar', '12px tall, radius 6, ink-4', '--ink-4'),
  ('Pulse', 'Opacity to 50% and back, 1.6s', '–'),
  ('Rows', 'The page size, at most 10', '–'),
 ]),
 usage(['Keep titles and labels real; skeleton only the values.', 'Match the final widths roughly.'], ['Shimmer gradients across the page.', 'Keep a skeleton up after an error: show the failed state.']),
 a11y(['Mark the region <code>aria-busy="true"</code>; hide skeleton bars from screen readers.', 'Under reduced motion the pulse stops.']),
 code('<div class="skel"><i style="width:40%"></i><i style="width:60%"></i></div>'))

page('empty-state', 'Empty state', 'Feedback',
 'Two lines: what\'s missing, then what to do. A failed load uses the same layout with one "Try again".',
 sec('Variants', None, f'''
<div class="grid-2">
 <div class="empty">{I('inbox')}<p>No claims yet</p><p>Claims from connected systems show up here.</p></div>
 <div class="empty">{I('filter')}<p>No claims match</p><p>Try removing a filter, or clear them all.</p><button class="btn btn-outline btn-sm">Clear filters</button></div>
 <div class="empty">{I('return')}<p>Claims didn't load</p><p>Check your connection, then try again.</p><button class="btn btn-outline btn-sm">Try again</button></div>
 <div class="empty">{I('lock')}<p>You can't see this project</p><p>Ask an admin to add you.</p></div>
</div>'''),
 specs([
  ('Panel', 'ink-2, radius 8, 40px padding, no border', '--ink-2'),
  ('Icon', '18px ink-9; 24px on phones; not in a box', '–'),
  ('Lines', 'ink-12 then ink-11, 13/20', '–'),
  ('Action', 'One outline button at most', '--border'),
 ]),
 usage(['Say what to do next in plain words.', 'Hide the table header and pager when there are no rows.'], ['Use illustrations or jokes.', 'Put a primary button in an empty state on a busy page.']),
 a11y(['Announce empty and failed results in a live region after a search or filter.']),
 code('''<div class="empty"><svg>…</svg><p>No claims yet</p><p>Claims from connected systems show up here.</p></div>'''))

# ============ OVERLAYS ============
page('menu', 'Menu', 'Overlays',
 'A short list of actions or choices that opens from a trigger. It stays inside the container it opens in.',
 sec('Action menu', 'Open the ⋯ menu. Destructive items are red and come last.', f'''
<div class="row" style="gap:24px;align-items:flex-start;min-height:220px">
 <div class="menu-anchor"><button class="btn btn-outline btn-icon" data-menu="m1" aria-label="More actions" aria-haspopup="menu" aria-expanded="false">{I('more')}</button>
  <div class="menu surface-overlay" id="m1" role="menu"><button class="mi" role="menuitem">{I('edit')}Rename<span class="kchip">R</span></button><button class="mi" role="menuitem">{I('copy')}Duplicate</button><button class="mi" role="menuitem">{I('external')}Open in new tab</button><div class="sep" role="separator"></div><button class="mi danger" role="menuitem">{I('trash')}Delete project</button></div></div>
 <div class="menu-anchor"><button class="btn btn-outline select-trigger" data-menu="m2" aria-haspopup="menu" aria-expanded="false" style="min-width:0">Sort: <span data-label>Newest</span>{I('chev','chev')}</button>
  <div class="menu surface-overlay" id="m2" role="menu"><button role="menuitemradio" aria-checked="true">Newest</button><button role="menuitemradio" aria-checked="false">Oldest</button><button role="menuitemradio" aria-checked="false">Amount, high to low</button></div></div>
</div>'''),
 specs([
  ('Surface', 'White in light, ink-2 in dark, radius 8', '--overlay'),
  ('Shadow', 'Its ring is the edge; no border', '--shadow-menu'),
  ('Padding', '4px; items 36px, 2px apart', '–'),
  ('Highlight / chosen', 'Ground + 1 / ground + 2, no tick', '--root-ink-2'),
  ('Separator', '0.5px, edge to edge', '--line'),
  ('Motion', 'From scale .97 at the trigger; 150ms in, 120ms out', '--ease-out'),
  ('Layer', 'z 100; 110 when opened from a modal', '–'),
 ]),
 usage(['Keep labels short and verb-first.', 'Close on outside click, Escape or scroll.'], ['Mark the chosen item with a tick.', 'Hide primary actions inside a ⋯ menu.']),
 a11y(['<code>role="menu"</code> with <code>menuitem</code>; arrow keys move, Enter acts, Escape returns focus to the trigger.']),
 code('''<button class="btn btn-outline btn-icon" aria-haspopup="menu" aria-expanded="false">…</button>
<div class="menu" role="menu"><button role="menuitem">Rename</button></div>'''))

page('popover', 'Popover', 'Overlays',
 'Extra information or a small form anchored to its trigger. Opens on click or tap, never on hover alone.',
 sec('Info and form', None, f'''
<div class="row" style="gap:40px;align-items:flex-start;min-height:240px">
 <div class="menu-anchor"><span class="row" style="gap:6px">Fraud score<button class="btn btn-ghost btn-icon-sm" data-pop="pop1" aria-label="About fraud score" aria-expanded="false">{I('info')}</button></span>
  <div class="popover surface-overlay" id="pop1" role="dialog" aria-label="About fraud score"><p class="t">Fraud score</p>A 0 to 100 estimate from the model. Claims above your threshold go to a reviewer.</div></div>
 <div class="menu-anchor"><button class="btn btn-outline" data-pop="pop2" aria-expanded="false">{I('link','ico ico-lead')}Share</button>
  <div class="popover form surface-overlay" id="pop2" role="dialog" aria-label="Share project" style="left:0;transform-origin:top left"><div class="field"><label for="pp-e">Invite by email</label><input id="pp-e" class="input" placeholder="name@enterlabs.id"></div><div class="row" style="justify-content:space-between"><button class="btn btn-outline btn-sm" data-copy="https://app.enterlabs.id/p/481">{I('copy','ico ico-lead')}<span>Copy link</span></button><button class="btn btn-sm btn-default">Invite</button></div></div></div>
</div>'''),
 specs([
  ('Info', '260px, 10px × 12px padding, 12/16 ink-11', '--shadow-popover'),
  ('Form', '300px, 14px padding, 12px gaps', '–'),
  ('Offset', '6px from the trigger', '–'),
  ('Motion', 'As a menu: scale .97 and fade', '--ease-out'),
 ]),
 usage(['Use for detail that would clutter the page.', 'Keep forms in a popover to one or two fields.'], ['Open on hover.', 'Put a long form in a popover: use a modal.']),
 a11y(['Trigger has <code>aria-expanded</code>; focus moves into a form popover and returns on close.']),
 code('<div class="popover" role="dialog" aria-label="About fraud score">…</div>'))

page('modal', 'Modal', 'Overlays',
 'Also called a dialog. It pauses the page for one focused task or one decision, then gets out of the way. On phones every modal becomes a bottom sheet.',
 sec('When to use one', 'Pick the lightest surface that does the job. A modal is the heaviest one short of a new page.', """
<div class="table-wrap surface-raised"><table class="tbl doc-tbl"><thead><tr><th>The person needs to…</th><th class="wrap">Use</th></tr></thead><tbody>
 <tr><td>Fill a short form, buy something, reveal a secret</td><td class="wrap">Task modal, 620px</td></tr>
 <tr><td>Confirm, or give something up</td><td class="wrap">Confirm modal, 460px</td></tr>
 <tr><td>Read a short explanation, no decision</td><td class="wrap">Info modal, 440px, with ×</td></tr>
 <tr><td>Inspect or edit one record while the list stays in view</td><td class="wrap"><a class="link" href="#/side-panel">Side panel</a></td></tr>
 <tr><td>See a small detail or set one or two fields</td><td class="wrap"><a class="link" href="#/popover">Popover</a></td></tr>
 <tr><td>Move to a whole new context</td><td class="wrap">A page</td></tr>
</tbody></table></div>""", stage='raw'),
 sec('Anatomy', 'Three parts split by full-width 0.5px hairlines. A confirm drops the body and keeps two.', """
<div class="stage surface-sunk backdrop-stage" style="padding:40px 24px 40px 40px">
 <div class="dialog surface-overlay modal-anat" role="presentation" style="width:min(520px,100%)">
  <span class="anno" style="top:20px">1</span>
  <div class="dialog-head"><p class="dialog-title">Create project</p><p class="ink-11" style="margin-top:4px">Projects group claims from one client.</p></div>
  <span class="anno" style="top:96px">2</span>
  <div class="dialog-body-static"><div class="field"><label>Project name</label><div class="input" style="display:flex;align-items:center;color:var(--ink-10)">E.g. Claims portal</div></div></div>
  <span class="anno" style="bottom:18px">3</span>
  <div class="dialog-foot"><button class="btn btn-outline" tabindex="-1">Cancel</button><button class="btn btn-default" tabindex="-1">Create project</button></div>
 </div>
</div>
<ol class="anatomy" style="margin-top:16px">
 <li><span><b class="ink-12" style="font-weight:inherit">Header band.</b> 16/24 title that asks or names the task, 13/20 description 4px under it. 20px sides, 20 top, 16 bottom.</span></li>
 <li><span><b class="ink-12" style="font-weight:inherit">Body.</b> 16 to 20px padding, 20px between fields; fields fill the width. The only part that scrolls.</span></li>
 <li><span><b class="ink-12" style="font-weight:inherit">Footer.</b> 12px padding, Cancel on the left, the one confirm on the right. Buttons hug their labels.</span></li>
</ol>""", stage='raw'),
 sec('Sizes', None, """
<div class="cols">
 <div class="bar" style="width:63.8%"><b>440</b><span>Info</span></div>
 <div class="bar" style="width:66.7%"><b>460</b><span>Confirm, give something up</span></div>
 <div class="bar" style="width:89.9%"><b>620</b><span>Task: forms, purchases, key reveal</span></div>
</div>
<p class="meta" style="margin-top:10px">Always <code>max-width: 100%</code> with a 16px gutter, and at most the window height minus 32px.</p>""", stage='raw'),
 sec('Variants', 'Open each one. Try Escape, Tab and a click on the backdrop.', f"""
<div class="mvars">
 <div class="mvar"><div><p class="t">Task</p><p class="d">A form with a required field. Create stays disabled until the name is filled, then swaps to "Creating…" in place.</p></div><button class="btn btn-outline" data-open="md-form">Open</button></div>
 <div class="mvar"><div><p class="t">Confirm</p><p class="d">Two parts, no body. Focus starts on the confirm.</p></div><button class="btn btn-outline" data-open="md-confirm">Open</button></div>
 <div class="mvar"><div><p class="t">Destructive confirm</p><p class="d">Title in red; a destructive button that names the action.</p></div><button class="btn btn-destructive" data-open="dlg-del">Open</button></div>
 <div class="mvar"><div><p class="t">Give something up</p><p class="d">Keeping the current state is the primary; leaving is secondary.</p></div><button class="btn btn-outline" data-open="md-downgrade">Open</button></div>
 <div class="mvar"><div><p class="t">Info</p><p class="d">No footer, so it keeps a ghost × button at the top right.</p></div><button class="btn btn-outline" data-open="md-info">Open</button></div>
 <div class="mvar"><div><p class="t">Steps in place</p><p class="d">Form, then progress, then result, in the same card at the same size. Cancel becomes Close.</p></div><button class="btn btn-outline" data-open="md-steps">Open</button></div>
 <div class="mvar"><div><p class="t">Long content</p><p class="d">Header and footer stay put; only the body scrolls.</p></div><button class="btn btn-outline" data-open="md-scroll">Open</button></div>
</div>""", stage='raw'),
 sec('In place, without a backdrop', 'A small confirm can sit right in the page. It is raised like a button, not floating like a modal.', """
<div class="stage surface-sunk"><div class="dialog inplace surface-overlay" role="group" aria-labelledby="ip-t" style="max-width:460px"><div class="dialog-head"><p class="dialog-title" id="ip-t">Remove Dita from this project?</p><p class="ink-11" style="margin-top:4px">She keeps access to the rest of the workspace.</p></div><div class="dialog-foot"><button class="btn btn-outline">Cancel</button><button class="btn btn-default">Remove</button></div></div></div>""", stage='raw'),
 sec('Behaviour', None, """
<div class="table-wrap surface-raised"><table class="tbl doc-tbl"><thead><tr><th>Moment</th><th class="wrap">What happens</th></tr></thead><tbody>
 <tr><td>Open</td><td class="wrap">Over the current page, never by navigating away. Page scroll locks. The backdrop dims: black 30% in light, 90% in dark, 2px blur.</td></tr>
 <tr><td>First focus</td><td class="wrap">The first field. In a two-part confirm, the confirm button. In a destructive confirm, the modal itself, so Enter can't delete by accident. Never Cancel.</td></tr>
 <tr><td>Keyboard</td><td class="wrap">Tab stays inside. Enter submits. Escape closes.</td></tr>
 <tr><td>Backdrop click</td><td class="wrap">Closes it, unless the form has changed. Then only Cancel or Escape close it.</td></tr>
 <tr><td>Submit</td><td class="wrap">The confirm swaps to "Saving…" in place. Errors show on submit, and focus moves to the first invalid field.</td></tr>
 <tr><td>Close</td><td class="wrap">Focus returns to the button that opened it. A result the page doesn't show becomes a toast.</td></tr>
 <tr><td>Inside it</td><td class="wrap">Menus and selects open above it at z 110. Another modal never stacks on top: replace the content in place.</td></tr>
</tbody></table></div>""", stage='raw'),
 sec('Motion', None, """
<div class="table-wrap surface-raised"><table class="tbl doc-tbl"><thead><tr><th>Part</th><th>In</th><th>Out</th><th class="wrap">How</th></tr></thead><tbody>
 <tr><td>Backdrop</td><td>240ms</td><td>200ms</td><td class="wrap">Fade</td></tr>
 <tr><td>Card</td><td>240ms</td><td>200ms</td><td class="wrap">16px rise, 4px blur, fade, strong ease-out</td></tr>
 <tr><td>Steps in place</td><td colspan="2">300ms</td><td class="wrap">Contents crossfade; the card holds its size</td></tr>
 <tr><td>Phone sheet</td><td>320ms</td><td>200ms</td><td class="wrap">Rises from the bottom, solid the whole way</td></tr>
 <tr><td>Reduced motion</td><td colspan="2">200ms</td><td class="wrap">Crossfade only: no rise, no blur</td></tr>
</tbody></table></div>""", stage='raw'),
 sec('On phones', 'Every modal becomes a bottom sheet: full width, 14px top corners, a white grab handle instead of ×, actions stacked full width with the confirm on top. Open any variant above on a phone to see it.', f"""<a class="link" href="#/bottom-sheet">Bottom sheet guidelines</a>""", stage='raw'),
 specs([
  ('Width', '620 task · 460 confirm · 440 info', '–'),
  ('Surface', 'White in light; ink-2 in dark, with an ink-3 header band', '--overlay'),
  ('Edge and shadow', 'The shadow\'s ring is the edge; no border', '--shadow-modal'),
  ('Radius', '8px; header band takes the same top corners', '--radius-container'),
  ('Header', '20 / 20 / 16 padding; 16/24 title; 13/20 description', '--text-title'),
  ('Body', '16 to 20px padding, 20px gaps, scrolls alone', '–'),
  ('Footer', '12px padding, 0.5px rule above, 12px gap', '--line'),
  ('Backdrop', 'Black 30% light, 90% dark, 2px blur', '--backdrop'),
  ('Layer', 'z 100; anything opened from it z 110', '–'),
  ('Phone', 'Bottom sheet, 14px top corners, grab handle', '--radius-sheet'),
 ]),
 usage(['Ask the question in the title; state the consequence plainly in the description.', 'Name the confirm with the action: "Delete project", "Archive project".', 'Keep one primary in the footer.', 'Change the content in place for multi-step tasks.'],
       ['Stack a modal on a modal.', 'Add a × when the footer already has Cancel.', 'Pre-focus Cancel, or make a destructive confirm the default.', 'Use a modal for something that could sit inline.', 'Put full-width buttons in a desktop footer.']),
 a11y(['<code>role="dialog"</code> (or <code>alertdialog</code> for a destructive confirm), <code>aria-modal="true"</code>, <code>aria-labelledby</code> the title and <code>aria-describedby</code> the description.', 'Trap Tab inside, lock page scroll, and return focus to the trigger on close.', 'Escape always closes. The info modal\'s × has the label "Close".', 'Announce a step change inside the modal by moving focus into the new step.']),
 code("""<div class="scrim open"></div>
<div class="modal open" role="dialog" aria-modal="true"
     aria-labelledby="m-title" aria-describedby="m-desc">
  <div class="dialog-head">
    <p class="dialog-title" id="m-title">Create project</p>
    <p class="ink-11" id="m-desc">Projects group claims from one client.</p>
  </div>
  <div class="dialog-body">
    <div class="field"><label for="m-name">Project name</label>
      <input id="m-name" class="input"></div>
  </div>
  <div class="dialog-foot">
    <button class="btn btn-outline">Cancel</button>
    <button class="btn btn-default">Create project</button>
  </div>
</div>"""))

page('side-panel', 'Side panel', 'Overlays',
 'Inspect or edit one record while the list stays in view. A task or a confirm is still a modal; a whole new context is a page.',
 sec('Open one', 'The page stays visible and usable; no dim.', '''
<div class="row"><button class="btn btn-outline" data-open="panel1">View CLM-1044</button></div>'''),
 specs([
  ('Width', '400 to 480px, full height inside the 8px float', '–'),
  ('Structure', 'Head, scrolling body, foot, like a modal', '–'),
  ('Shadow', 'Overlay surface, modal shadow', '--shadow-modal'),
  ('Motion', 'Slides in 240ms, out 200ms', '--dur-modal'),
  ('Phone', 'Becomes a bottom sheet', '–'),
 ]),
 usage(['Keep the list behind it clickable to switch records.'], ['Dim the page unless the panel is fullscreen.', 'Open a modal on top of a side panel.']),
 a11y(['<code>role="dialog"</code> with a label; Escape closes; focus returns to the row that opened it.']),
 code('''<aside class="side-panel" role="dialog" aria-labelledby="t">…</aside>'''))

page('bottom-sheet', 'Bottom sheet', 'Overlays',
 'Every modal becomes a sheet on phones. A white grab handle replaces the ×. Drag down or tap the handle to close.',
 sec('On a phone', 'Open the sheet, then drag it down or tap the handle.', f'''
<div class="phone-frame surface-panel" id="pf">
 <div class="pf-bar"><span class="crumbs"><span class="lm logo">[[svg:symbol]]</span>{I('chev-r')}<span aria-current="page">CLM-1044</span></span></div>
 <div class="pf-body"><p class="ink-11">Bumi Proteksi · Rp 87.000.000</p><button class="btn btn-default" id="pf-open">Review claim</button><button class="btn btn-outline">Add note</button></div>
 <div class="pf-scrim" id="pf-scrim"></div>
 <div class="sheet surface-overlay" id="pf-sheet" role="dialog" aria-labelledby="pf-t" aria-modal="true">
  <button class="sheet-grab" id="pf-grab" aria-label="Close"><i></i></button>
  <h4 id="pf-t">Review claim</h4><p class="d">Flagged by the fraud model at 86.</p>
  <div class="rc"><div><span>Amount</span><span class="v">Rp 87.000.000</span></div><div><span>Incident</span><span class="v">12 Nov 2026</span></div><div><span>Hospital</span><span class="v">RS Medika</span></div></div>
  <div class="acts"><button class="btn btn-default">Approve</button><button class="btn btn-outline">Send to reviewer</button></div>
 </div>
</div>''', extra='', stage=True),
 specs([
  ('Shape', 'Full width, 14px top corners, top hairline only', '--radius-sheet'),
  ('Handle', '36 × 5 white pill, 12px above the sheet, 88 × 44 hit area', '–'),
  ('Rows', 'One raised card of 48pt rows, 0.5px rules', '–'),
  ('Buttons', 'Below the card, full width, 44pt, 8px apart', '--control-h'),
  ('Motion', 'Up 320ms, down 200ms; closes past 64px or a quick flick', '--ease-drawer'),
 ]),
 usage(['Put related details in one raised card.', 'Stack actions full width, confirm on top.'], ['Put buttons inside the details card.', 'Add a × as well as the handle.']),
 a11y(['The handle is a button labelled "Close"; Enter and Space close the sheet.', 'Trap focus inside while open.']),
 code('''<div class="sheet" role="dialog" aria-modal="true">
  <button class="sheet-grab" aria-label="Close"><i></i></button>
  …
</div>'''))

# ============ NAVIGATION ============
page('sidebar-nav', 'Sidebar', 'Navigation',
 'The rail on the ground beside the floating panel. Groups are always open; space separates them, not lines.',
 sec('Shell', 'Click rows to move the current page.', f'''
<div class="mini-app">
 <nav class="mini-rail surface-rail" aria-label="Demo">
  <div class="ws logo">[[svg:horizontal]]</div>
  <a href="#/sidebar-nav" onclick="return false" aria-current="true">{I('home')}Overview</a>
  <a href="#/sidebar-nav" onclick="return false">{I('inbox')}Claims<span class="count">86</span></a>
  <a href="#/sidebar-nav" onclick="return false">{I('shield')}Fraud review<span class="count">3</span></a>
  <p class="g">Workspace</p>
  <a href="#/sidebar-nav" onclick="return false">{I('users')}Members</a>
  <a href="#/sidebar-nav" onclick="return false">{I('sliders')}Settings</a>
 </nav>
 <div class="mini-panel surface-panel"><div class="mini-strip"><span class="crumbs"><span aria-current="page">Overview</span></span><button class="btn btn-outline btn-sm">Export</button></div><div class="mini-content"><p class="section-title" id="mini-title">Overview</p><p class="ink-11">The panel floats 8px off the window on the ground.</p></div></div>
</div>'''),
 specs([
  ('Rows', '36px, radius 6, 16px icon, 6px gap, 1px apart', '--control-h'),
  ('Ink', 'ink-11 rest; ink-12 hover and current', '–'),
  ('Current', 'ink-3 fill (ink-2 in dark), no edge', '--ink-3'),
  ('Group title', '13/20 ink-9, 16px space above', '–'),
  ('Panel', 'Floats 8px off the window, radius 8', '--shadow-panel'),
  ('Phone', 'Becomes a top bar with a menu', '–'),
 ]),
 usage(['Keep labels to one or two words.', 'Show counts only when they need action.'], ['Collapse groups behind chevrons.', 'Draw rules between groups.']),
 a11y(['A <code>&lt;nav&gt;</code> with a label; the current row has <code>aria-current="page"</code>.']),
 code('''<nav class="rail" aria-label="Main">
  <a href="/" aria-current="page"><svg class="ico">…</svg>Overview</a>
</nav>'''))

page('top-bar', 'Top bar', 'Navigation',
 'The strip at the top of the panel: breadcrumbs left, page actions right. On phones it becomes a 56px bar with a menu.',
 sec('Desktop strip', None, f'''
<div class="mini-panel surface-panel" style="margin:0"><div class="mini-strip"><span class="crumbs"><a href="#/top-bar" onclick="return false">Claims</a>{I('chev-r')}<span aria-current="page">CLM-1044</span></span><span class="ctr">CLM-1044</span><div class="row" style="gap:8px"><button class="btn btn-outline btn-sm">Add note</button><button class="btn btn-sm btn-default">Approve</button></div></div><div class="mini-content"><p class="ink-11">Page content</p></div></div>'''),
 sec('Phone bar', 'Tap the menu: its two lines turn into a ×.', f'''
<div class="phone-bar"><span class="crumbs"><span class="lm">[[svg:symbol]]</span>{I('chev-r')}<span aria-current="page">Claims</span></span><button class="burger" aria-label="Menu" aria-expanded="false" id="burger"><span><i></i><i></i></span></button></div>'''),
 specs([
  ('Desktop', '52px: a 36px control + 8px inset', '–'),
  ('Title', '13/20 ink-12, centred', '--text-body'),
  ('Rule', '0.5px at its foot', '--line'),
  ('Phone', '56px + safe area, 15px crumbs, 44px menu button', '–'),
  ('Menu icon', 'Two lines to ×, 160ms', '–'),
 ]),
 usage(['Use breadcrumbs instead of a back button.', 'Keep page actions at the right; one primary at most.'], ['Repeat the page title in the breadcrumb and a heading below.']),
 a11y(['Wrap in <code>&lt;header&gt;</code>; the menu button has <code>aria-expanded</code>.']),
 code('''<header class="strip">
  <nav class="crumbs" aria-label="Breadcrumb">…</nav>
  <div><button class="btn btn-default">Approve</button></div>
</header>'''))

page('breadcrumb', 'Breadcrumb', 'Navigation',
 'Shows where the page sits and replaces back buttons. Parents are quiet; the current page leads.',
 sec('Default', None, f'''
<div class="stack" style="gap:16px">
 <nav class="crumbs" aria-label="Breadcrumb"><a href="#/breadcrumb" onclick="return false">Workspace</a>{I('chev-r')}<a href="#/breadcrumb" onclick="return false">Claims</a>{I('chev-r')}<span aria-current="page">CLM-1044</span></nav>
 <nav class="crumbs" aria-label="Breadcrumb" style="max-width:320px"><a href="#/breadcrumb" onclick="return false">Projects</a>{I('chev-r')}<span aria-current="page">PT Asuransi Jiwa Sejahtera Bersama Indonesia</span></nav>
</div>'''),
 specs([
  ('Text', '13/20; 15px on phones', '–'),
  ('Parents', 'ink-10, ink-12 on hover', '--ink-10'),
  ('Current', 'ink-12, not a link', '--ink-12'),
  ('Chevron', '14px ink-8', '--ink-8'),
  ('Long names', 'Truncate with "…" at the container width', '–'),
 ]),
 usage(['Start from the logo mark on phones.'], ['Show more than 4 levels: collapse the middle.']),
 a11y(['<code>&lt;nav aria-label="Breadcrumb"&gt;</code>; the last item has <code>aria-current="page"</code>.']),
 code('''<nav class="crumbs" aria-label="Breadcrumb">
  <a href="/claims">Claims</a><svg>…</svg><span aria-current="page">CLM-1044</span>
</nav>'''))

page('pagination', 'Pagination', 'Navigation',
 'Below the data, outside its card: the count on the left, Previous and Next on the right.',
 sec('Default', 'Try the buttons.', '''
<div class="pager" id="pgr" style="max-width:560px"><span class="count" aria-live="polite">Showing 1 to 10 of 48</span><div class="btns"><button class="btn btn-outline btn-sm" data-pg="-1" disabled>Previous</button><button class="btn btn-outline btn-sm" data-pg="1">Next</button></div></div>'''),
 sec('View all', 'On overview pages, stop at 5 or 6 rows and link to the full list.', f'''
<a class="link" href="#/pagination" onclick="return false">View all 48 claims</a>'''),
 specs([
  ('Gap', '12px under the card', '–'),
  ('Count', 'ink-10, tabular figures', '--ink-10'),
  ('Buttons', 'Secondary, 32px; half and half on phones', '--control-h-compact'),
  ('Disabled', 'At the first and last page', '–'),
 ]),
 usage(['Show it only when there is another page.'], ['Put the pager inside the table frame.', 'Use numbered page links for long lists.']),
 a11y(['Wrap in <code>&lt;nav aria-label="Pagination"&gt;</code>; announce the new range.']),
 code('''<div class="pager"><span class="count">Showing 1 to 10 of 48</span>
  <div class="btns"><button class="btn btn-outline btn-sm" disabled>Previous</button><button class="btn btn-outline btn-sm">Next</button></div></div>'''))

page('stepper', 'Stepper', 'Navigation',
 'Guides someone through a setup in order. Done steps turn teal (success); steps that can\'t start yet wait at half opacity.',
 sec('Vertical', 'Click Continue to finish the current step.', f'''
<div class="steps" id="stp">
 <div class="step done"><span class="marker">{I('check')}</span><div class="txt"><p class="t">Create a workspace</p><p class="d">Claims portal</p></div><span class="line"></span></div>
 <div class="step"><span class="marker">2</span><div class="txt"><p class="t">Connect your claims system</p><p class="d">Paste the API key from your core system.</p><button class="btn btn-default btn-sm" data-step-next>Continue</button></div><span class="line"></span></div>
 <div class="step wait"><span class="marker">3</span><div class="txt"><p class="t">Invite reviewers</p><p class="d">They get an email with a sign-in link.</p></div></div>
</div>'''),
 sec('Horizontal', 'For short flows in a modal header.', f'''
<div class="hsteps"><span class="hs done"><span class="n">{I('check')}</span>Details</span><span class="sepl"></span><span class="hs cur"><span class="n">2</span>Documents</span><span class="sepl"></span><span class="hs"><span class="n">3</span>Review</span></div>'''),
 specs([
  ('Marker', '32px disc, raised like a button, 16/24 number', '--shadow-button'),
  ('Done', 'Success (teal) disc with a white tick', '--green-9'),
  ('Connector', '0.5px ink-6, 8px under the marker', '--line'),
  ('Spacing', '16px marker to text; 32px between steps', '–'),
  ('Waiting', '50% opacity', '–'),
 ]),
 usage(['Show the next step only once the current one is chosen.', 'Hide the stepper when the setup is complete.'], ['Write "Step 1 of 4" above the steps.', 'Let people skip required steps silently.']),
 a11y(['Use an ordered list; the current step has <code>aria-current="step"</code>.']),
 code('''<ol class="steps">
  <li class="step done">…</li><li class="step" aria-current="step">…</li>
</ol>'''))
