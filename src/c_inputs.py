from dsl import *
from icons import I

# ============ ACTIONS ============
page('button', 'Button', 'Actions',
 'Styled like shadcn/ui: six variants, eight sizes, the same class names. Colours come from the Enterlabs neutral, so default is black in light and white in dark.',
 sec('Variants', None, f"""
<div class="row" style="gap:8px">
 <button class="btn btn-default">Default</button>
 <button class="btn btn-outline">Outline</button>
 <button class="btn btn-secondary">Secondary</button>
 <button class="btn btn-ghost">Ghost</button>
 <button class="btn btn-destructive">Destructive</button>
 <button class="btn btn-link">Link</button>
</div>"""),
 sec('Sizes', 'xs, sm, default and lg. Text buttons only; icon-only buttons have their own sizes below.', f"""
<div class="row" style="gap:8px;align-items:center">
 <button class="btn btn-outline btn-xs">Extra small</button>
 <button class="btn btn-outline btn-sm">Small</button>
 <button class="btn btn-outline">Default</button>
 <button class="btn btn-outline btn-lg">Large</button>
</div>
<div class="row" style="gap:8px;align-items:center;margin-top:12px">
 <button class="btn btn-default btn-xs">Extra small</button>
 <button class="btn btn-default btn-sm">Small</button>
 <button class="btn btn-default">Default</button>
 <button class="btn btn-default btn-lg">Large</button>
</div>"""),
 sec('Icon', 'Square sizes for icon-only buttons: icon-xs, icon-sm, icon and icon-lg. Each needs an accessible name.', f"""
<div class="row" style="gap:8px;align-items:center">
 <button class="btn btn-outline btn-icon-xs" aria-label="Add">{I('plus')}</button>
 <button class="btn btn-outline btn-icon-sm" aria-label="Add">{I('plus')}</button>
 <button class="btn btn-outline btn-icon" aria-label="Add">{I('plus')}</button>
 <button class="btn btn-outline btn-icon-lg" aria-label="Add">{I('plus')}</button>
</div>"""),
 sec('With icon', 'Mark the icon with data-icon="inline-start" or "inline-end"; the button tightens its padding on that side.', f"""
<div class="row" style="gap:8px">
 <button class="btn btn-outline btn-sm">{I('plus')}<span>New project</span></button>
 <button class="btn btn-default btn-sm">{I('down')}<span>Download</span></button>
 <button class="btn btn-outline btn-sm"><span>Next</span>{I('arrow-r')}</button>
 <button class="btn btn-secondary btn-sm">{I('filter')}<span>Filter</span></button>
</div>"""),
 sec('Spinner', 'There is no loading prop. Put a spinner in the icon slot and disable the button while it works. Click Save to try it.', f"""
<div class="row" style="gap:8px">
 <button class="btn btn-outline btn-sm" disabled><span class="spinner"></span>Generating</button>
 <button class="btn btn-secondary btn-sm" disabled><span class="spinner"></span>Downloading</button>
 <button class="btn btn-default btn-sm" data-busy-label="Saving…">Save changes</button>
</div>"""),
 sec('Rounded', 'Add rounded-full for a pill.', f"""
<div class="row" style="gap:8px">
 <button class="btn btn-outline rounded-full">Get started</button>
 <button class="btn btn-default rounded-full">{I('arrow-r')}<span>Continue</span></button>
 <button class="btn btn-outline btn-icon rounded-full" aria-label="Scroll up">{I('chev')}</button>
</div>"""),
 sec('Button group', 'Related actions joined into one control. Inner corners and the shared borders drop away.', f"""
<div class="row" style="gap:12px">
 <div class="btn-group" role="group" aria-label="Claim actions"><button class="btn btn-outline">Archive</button><button class="btn btn-outline">Report</button><button class="btn btn-outline">Snooze</button></div>
 <div class="btn-group" role="group" aria-label="Pagination"><button class="btn btn-outline btn-icon" aria-label="Previous">{I('chev-l')}</button><button class="btn btn-outline btn-icon" aria-label="Next">{I('chev-r')}</button></div>
 <div class="btn-group" role="group" aria-label="Export"><button class="btn btn-default">Export</button><button class="btn btn-default btn-icon" aria-label="More export options">{I('chev')}</button></div>
</div>"""),
 sec('As a link', 'For navigation, put the button classes on an <code>&lt;a&gt;</code> rather than wrapping a link in a button.', f"""
<div class="row" style="gap:8px"><a class="btn btn-outline" href="#/components">Browse components</a><a class="btn btn-link" href="#/tokens">View tokens</a></div>"""),
 sec('Disabled', None, """
<div class="row" style="gap:8px"><button class="btn btn-default" disabled>Default</button><button class="btn btn-outline" disabled>Outline</button><button class="btn btn-secondary" disabled>Secondary</button><button class="btn btn-ghost" disabled>Ghost</button><button class="btn btn-destructive" disabled>Destructive</button></div>"""),
 specs([
  ('default', 'Primary fill, primary-foreground text; hover at 90%', '--primary'),
  ('outline', '1px border, background fill, shadow-xs; hover accent. Dark: input at 30%', '--border'),
  ('secondary', 'Secondary fill; hover at 80%', '--secondary'),
  ('ghost', 'No fill until hover, then accent', '--accent'),
  ('destructive', 'Destructive fill, white text; dark at 60%', '--destructive'),
  ('link', 'Primary text, underline on hover, 4px offset', '--primary'),
  ('Focus', '2px orange ring, 2px off the edge: the one place orange touches a button', '--ring'),
  ('Disabled', 'opacity .5, no pointer events', '–'),
  ('Radius', '6px; rounded-full for pills', '--radius'),
 ], head=('Variant', 'Look', 'Token')),
 specs([
  ('xs', '24px · 8px sides (6px with icon) · 12px text · 12px icon', '–'),
  ('sm', '32px · 12px sides (10px with icon) · gap 6', '–'),
  ('default', '36px · 16px sides (12px with icon) · gap 8', '–'),
  ('lg', '40px · 24px sides (16px with icon)', '–'),
  ('icon-xs · icon-sm · icon · icon-lg', '24 · 32 · 36 · 40px square', '–'),
 ], head=('Size', 'Measurements', 'Token')),
 usage(['Use one default button for the main action of a section or modal.', 'Use outline for the other actions beside it, ghost for quiet ones in toolbars and rows.', 'Name the action with a verb: "Create project", "Delete project".', 'Use destructive only for actions that delete or revoke.'],
       ['Put two default buttons side by side.', 'Use destructive to make something look important.', 'Use link for actions; it is for navigation.', 'Add your own loading prop: compose a spinner and disabled.']),
 a11y(['Use <code>&lt;button&gt;</code> for actions and <code>&lt;a class="btn …"&gt;</code> for navigation.', 'Icon-only buttons need an <code>aria-label</code>.', 'While working, set <code>disabled</code> and <code>aria-busy="true"</code>, and keep the label meaningful ("Saving…").', 'Group joined buttons with <code>role="group"</code> and a label.']),
 code("""<!-- shadcn/ui (React) -->
<Button>Create project</Button>
<Button variant="outline" size="sm">
  <PlusIcon data-icon="inline-start" /> New project
</Button>
<Button variant="destructive">Delete project</Button>
<Button variant="outline" size="icon" aria-label="Add"><PlusIcon /></Button>
<Button disabled><Spinner data-icon="inline-start" /> Generating</Button>

<!-- Plain HTML with this page's CSS -->
<button class="btn btn-default">Create project</button>
<button class="btn btn-outline btn-sm"><svg>…</svg>New project</button>
<button class="btn btn-destructive">Delete project</button>
<div class="btn-group" role="group"><button class="btn btn-outline">Archive</button>…</div>"""))

page('icon-button', 'Icon button', 'Actions',
 'A button with only an icon: the icon sizes of Button, usually in the ghost or outline variant. Every one has a name, shown as a tooltip on hover.',
 sec('Variants', 'Ghost for row and toolbar tools, outline when the button stands on its own.', f"""
<div class="row" style="gap:16px;align-items:center;padding-top:24px">
 <span class="tip-wrap"><button class="btn btn-ghost btn-icon-sm" aria-label="Edit">{I('edit')}</button><span class="tip" role="tooltip">Edit</span></span>
 <span class="tip-wrap"><button class="btn btn-ghost btn-icon-sm text-destructive" aria-label="Delete">{I('trash')}</button><span class="tip" role="tooltip">Delete</span></span>
 <span class="tip-wrap"><button class="btn btn-ghost btn-icon-sm" aria-label="More">{I('more')}</button><span class="tip" role="tooltip">More</span></span>
 <span class="tip-wrap"><button class="btn btn-outline btn-icon-sm" aria-label="Copy" data-copy="EL-00481">{I('copy')}</button><span class="tip" role="tooltip">Copy</span></span>
 <span class="tip-wrap"><button class="btn btn-outline btn-icon" aria-label="Filter">{I('filter')}</button><span class="tip" role="tooltip">Filter</span></span>
 <span class="tip-wrap"><button class="btn btn-secondary btn-icon" aria-label="Settings">{I('sliders')}</button><span class="tip" role="tooltip">Settings</span></span>
 <span class="tip-wrap"><button class="btn btn-default btn-icon rounded-full" aria-label="New project">{I('plus')}</button><span class="tip" role="tooltip">New project</span></span>
 <span class="tip-wrap"><button class="btn btn-outline btn-icon" aria-label="Settings" disabled>{I('sliders')}</button><span class="tip" role="tooltip">Settings</span></span>
</div>"""),
 sec('In a row', 'Row tools are ghost icon-sm at the end of the row.', f"""
<div class="rows-card surface-raised">
 <div><div class="grow"><p class="t">Production key</p><p class="d mono">el_live_8f2c…91ab</p></div>
  <span class="tip-wrap"><button class="btn btn-ghost btn-icon-sm" aria-label="Copy key" data-copy="el_live_8f2c91ab">{I('copy')}</button><span class="tip">Copy</span></span>
  <span class="tip-wrap"><button class="btn btn-ghost btn-icon-sm text-destructive" aria-label="Revoke key">{I('trash')}</button><span class="tip">Revoke</span></span></div>
</div>"""),
 specs([
  ('icon-xs', '24px square, 12px icon', '–'),
  ('icon-sm', '32px square, 16px icon: rows and toolbars', '–'),
  ('icon', '36px square, 16px icon: beside default buttons', '–'),
  ('icon-lg', '40px square, 16px icon', '–'),
  ('Destructive tool', 'Ghost with destructive text; hover tints 10%', '--destructive'),
  ('Disabled', 'opacity .5', '–'),
 ], head=('Size', 'Use', 'Token')),
 usage(['Use only glyphs people already know.', 'Pair every icon button with a tooltip naming it.', 'Match the icon size to the buttons next to it.'],
       ['Hide the only way to do something behind an unlabelled icon.', 'Use a solid destructive icon button in a list of rows.']),
 a11y(['Give every icon button an <code>aria-label</code>; the tooltip repeats it visually.', 'The tooltip shows on keyboard focus too, with no delay.']),
 code("""<Button variant="ghost" size="icon-sm" aria-label="Edit"><PencilIcon /></Button>

<button class="btn btn-ghost btn-icon-sm" aria-label="Edit"><svg>…</svg></button>"""))

# ============ INPUTS ============
page('text-field', 'Text field', 'Inputs',
 'Fields are wells: sunk into their surface with a quiet fill and no border. Buttons are raised; fields never look like buttons.',
 sec('States', 'Errors show on blur or submit, never on each keystroke. Try the email field.', f'''
<div class="card surface-raised form-grid">
 <div class="field"><label for="tf1">Project name</label><input id="tf1" class="input" placeholder="E.g. Claims portal"></div>
 <div class="field"><label for="tf2">Work email</label><input id="tf2" class="input" type="email" data-validate="email" placeholder="name@enterlabs.id" aria-describedby="tf2-m"><p class="hint" id="tf2-m">We send the invite here.</p></div>
 <div class="field"><label for="tf3">Workspace URL</label><div class="input-wrap"><input id="tf3" class="input has-suffix" value="claims" ><span class="suffix">.enterlabs.id</span></div></div>
 <div class="field"><label for="tf4">Search members</label><div class="input-wrap">{I('search','lead')}<input id="tf4" class="input has-lead" placeholder="Name or email"></div></div>
 <div class="field"><label for="tf5">Project ID <span class="opt">(read-only)</span></label><input id="tf5" class="input mono" readonly value="EL-2026-00481"></div>
 <div class="field"><label for="tf6">Region</label><input id="tf6" class="input" disabled value="Jakarta"></div>
</div>'''),
 sec('Error', 'A 1px red ring drawn as a shadow, so nothing moves. The message says what to do.', '''
<div class="field" style="max-width:440px"><label for="tf7">API key name</label><input id="tf7" class="input" value="Production" aria-invalid="true" aria-describedby="tf7-e"><p class="err" id="tf7-e" role="alert">That name already exists. Pick another name.</p></div>'''),
 anatomy(['Label, 13/20 ink-12, 6px above', 'Well: ink-3 fill, no border', 'Optional icon or suffix inside', 'Help text 12/16 ink-10, or the error in red-11']),
 specs([
  ('Height', '36px; 44pt on phone', '--control-h'),
  ('Fill', 'ink-3; ink-4 on focus', '--ink-3'),
  ('Text', '13px; 16px on any touch screen', '--text-field'),
  ('Padding', '12px; 34px on the icon side', '–'),
  ('Focus', 'Fill deepens + 2px orange focus ring', '--focus-ring'),
  ('Error', '1px red-11 ring, message under', '--red-11'),
  ('Spacing', '20px between fields', '–'),
 ]),
 usage(['Put the label above the field, always visible.', 'Start placeholders with a capital: "E.g. Claims portal".', 'Mark the optional field, not the required ones.'],
       ['Use the placeholder as the label.', 'Validate while the person is still typing.', 'Add a border or shadow to a field.']),
 a11y(['Link the label with <code>for</code>, and help or error text with <code>aria-describedby</code>.', 'Set <code>aria-invalid="true"</code> on an invalid field; give the message <code>role="alert"</code>.', 'On submit, move focus to the first invalid field.']),
 code('''<div class="field">
  <label for="name">Project name</label>
  <input id="name" class="input" placeholder="E.g. Claims portal">
  <p class="hint">Shown to everyone in the workspace.</p>
</div>'''))

page('textarea', 'Textarea', 'Inputs',
 'The same well as the text field, for several lines. Three lines tall to start, and it grows by drag.',
 sec('Default', 'A counter appears only when there is a limit.', '''
<div class="card surface-raised form-grid">
 <div class="field"><label for="ta1">Description <span class="opt">(optional)</span></label><textarea id="ta1" class="input" placeholder="What is this project for?" maxlength="200" data-counter="ta1-c"></textarea><div class="field-foot"><p class="hint">Shown on the project card.</p><span class="counter" id="ta1-c">0 / 200</span></div></div>
 <div class="field"><label for="ta2">Rejection note</label><textarea id="ta2" class="input" aria-invalid="true" aria-describedby="ta2-e"></textarea><p class="err" id="ta2-e" role="alert">Add a short note so the claimant knows why.</p></div>
</div>'''),
 specs([
  ('Min height', '84px, three lines', '–'),
  ('Padding', '8px top and bottom, 12px sides', '–'),
  ('Fill', 'ink-3; ink-4 on focus', '--ink-3'),
  ('Counter', '12/16 ink-10, tabular figures, right', '--text-meta'),
  ('Resize', 'Vertical only', '–'),
 ]),
 usage(['Use for free text longer than one line.', 'Show a counter only when a limit exists.'], ['Use a textarea for a single value like a name.', 'Block typing at the limit without saying why.']),
 a11y(['Announce the counter with <code>aria-describedby</code> so screen readers hear the limit.']),
 code('<textarea class="input" placeholder="What is this project for?"></textarea>'))

page('select', 'Select', 'Inputs',
 'A dropdown trigger is an outline button with a chevron that turns over while open. The list is a menu.',
 sec('Default', 'The chosen item is a darker fill in full ink. No tick.', f'''
<div class="row" style="align-items:flex-start;gap:24px">
 <div class="field"><span id="sel1-l">Status</span>
  <div class="menu-anchor"><button class="btn btn-outline select-trigger" data-menu="sel1" aria-haspopup="listbox" aria-expanded="false" aria-labelledby="sel1-l"><span data-label>Any status</span>{I('chev','chev')}</button>
   <div class="menu surface-overlay" id="sel1" role="listbox"><button role="option" aria-checked="true">Any status</button><button role="option" aria-checked="false">Live</button><button role="option" aria-checked="false">In review</button><button role="option" aria-checked="false">Paused</button><button role="option" aria-checked="false">Failed</button></div></div></div>
 <div class="field"><span id="sel2-l">Owner</span>
  <div class="menu-anchor"><button class="btn btn-outline select-trigger" data-menu="sel2" aria-haspopup="listbox" aria-expanded="false" aria-labelledby="sel2-l" aria-invalid="true"><span data-label class="ph">Pick an owner</span>{I('chev','chev')}</button>
   <div class="menu surface-overlay" id="sel2" role="listbox"><button role="option" aria-checked="false">Rama</button><button role="option" aria-checked="false">Dita</button><button role="option" aria-checked="false">Bayu</button></div></div><p class="err">Pick an owner to continue.</p></div>
</div>'''),
 sec('Native, in forms', 'A plain <code>&lt;select&gt;</code> wears the well look when it is one field among many.', f'''
<div class="field" style="max-width:300px"><label for="ns">Region</label><div class="select-wrap"><select id="ns" class="input"><option>Jakarta</option><option>Surabaya</option><option>Singapore</option></select>{I('chev')}</div></div>'''),
 specs([
  ('Trigger', 'Outline button, 36px, 12px sides, min 200px', '--border'),
  ('Chevron', '16px ink-9, rotates 180° while open', '–'),
  ('Menu', '6px below, radius 8, 4px padding', '--shadow-menu'),
  ('Item', '36px, 2px apart, ink-11', '--control-h'),
  ('Highlight / chosen', 'Ground + 1 / ground + 2', '--root-ink-2'),
  ('Motion', 'In 150ms from scale .97, out 120ms', '--ease-out'),
 ]),
 usage(['Show the current value in the trigger.', 'Use a segmented control instead when there are 2 to 4 options.'], ['Add a tick to the chosen item.', 'Let the menu cross the edge of its modal or card.']),
 a11y(['Trigger has <code>aria-haspopup</code> and <code>aria-expanded</code>.', 'Arrow keys move, Enter picks, Escape closes and returns focus.']),
 code('''<button class="btn btn-outline select-trigger" aria-haspopup="listbox" aria-expanded="false">
  Any status <svg class="chev">…</svg>
</button>
<div class="menu" role="listbox">
  <button role="option" aria-checked="true">Any status</button>
</div>'''))

page('search', 'Search', 'Inputs',
 'A button that opens search wears a field look with a key hint. Inline search is a well with a leading icon and live results.',
 sec('Search trigger', 'White with a 0.5px line, not raised. The key pill hides on touch.', f'''
<button class="search-trigger">{I('search')}<span class="grow">Search projects…</span><span class="kpill">⌘K</span></button>'''),
 sec('Inline search', 'Type to filter. Arrow keys move through results, Enter picks.', f'''
<div class="search-box">
 <div class="input-wrap">{I('search','lead')}<input class="input has-lead" id="srch" placeholder="Search projects" role="combobox" aria-expanded="false" aria-controls="srch-r" autocomplete="off"></div>
 <div class="search-results surface-overlay" id="srch-r" role="listbox"></div>
</div>'''),
 specs([
  ('Trigger', '36px, white, 0.5px ink-6 inset line', '--ink-6'),
  ('Key pill', '20px, 12/16, 14% of its ink', '--badge-h'),
  ('Inline field', 'Well with 16px ink-9 icon, 10px in', '--ink-3'),
  ('Results', 'Menu surface, 36px rows', '--shadow-menu'),
  ('Match', 'Underlined in ink-12, not coloured', '–'),
 ]),
 usage(['Show what can be searched in the placeholder.', 'Say "No projects match" with the query when empty.'], ['Highlight matches with colour.', 'Open results before the person types.']),
 a11y(['Use <code>role="combobox"</code> with <code>aria-expanded</code> and <code>aria-activedescendant</code>.', '⌘K focuses search from anywhere.']),
 code('''<div class="input-wrap">
  <svg class="lead">…</svg>
  <input class="input has-lead" role="combobox" placeholder="Search projects">
</div>'''))

page('checkbox', 'Checkbox', 'Inputs',
 'For several independent choices. In a list the row is the control and the square mark sits at the far right.',
 sec('Choice list', 'Rows have no box and no lines between them. Selected rows take a quiet fill.', f'''
<div class="choices" role="group" aria-label="Notifications">
 <label class="choice">{I('mail')}<span class="lbl">Email</span><input type="checkbox" checked><span class="mark box"></span></label>
 <label class="choice">{I('bell')}<span class="lbl">In-app</span><input type="checkbox" checked><span class="mark box"></span></label>
 <label class="choice">{I('users')}<span class="lbl">Weekly digest to admins</span><input type="checkbox"><span class="mark box"></span></label>
 <label class="choice">{I('lock')}<span class="lbl">Security alerts</span><input type="checkbox" checked disabled><span class="mark box"></span></label>
</div>'''),
 sec('Inline and indeterminate', 'Inline checkboxes lead their label. "Select all" shows a dash when only some are on.', '''
<div class="stack" style="gap:12px">
 <label class="inline-check"><input type="checkbox" id="cb-all"><span class="mark box"></span><span>Select all claims</span></label>
 <div style="display:grid;gap:8px;padding-left:26px">
  <label class="inline-check"><input type="checkbox" class="cb-item" checked><span class="mark box"></span><span>CLM-1042</span></label>
  <label class="inline-check"><input type="checkbox" class="cb-item"><span class="mark box"></span><span>CLM-1043</span></label>
  <label class="inline-check"><input type="checkbox" class="cb-item"><span class="mark box"></span><span>CLM-1044</span></label>
 </div>
 <label class="inline-check"><input type="checkbox"><span class="mark box"></span><span>I agree to the <a class="link" href="#/checkbox" onclick="return false">data processing terms</a></span></label>
</div>'''),
 specs([
  ('Row', '36px, 8px padding, 2px apart', '--control-h'),
  ('Hover / selected', 'ink-2 / ink-3; ground +1 / +2 in dark', '–'),
  ('Mark', '18px, 1.5px ink-6 ring, radius 4', '--radius-sm'),
  ('Checked', 'ink-12 fill, ink-1 tick', '--ink-12'),
  ('Enter', 'Tick from scale .9 and transparent, 150ms', '--ease-out'),
  ('Disabled', 'opacity .6', '–'),
 ]),
 usage(['Use squares for many-of, circles for one-of.', 'Let the whole row toggle, not just the mark.'], ['Draw lines or boxes between choice rows.', 'Use a checkbox for a setting that takes effect at once: use a switch.']),
 a11y(['Wrap the input in its <code>&lt;label&gt;</code>; keep the native input for keyboard and screen readers.', 'Set <code>indeterminate</code> in script for partial selection.']),
 code('''<label class="choice">
  <span class="lbl">Email</span>
  <input type="checkbox" checked><span class="mark box"></span>
</label>'''))

page('radio', 'Radio', 'Inputs',
 'For one choice from a short list. Rows in a modal, tiles in a grid on a page, or cards when each option needs a description.',
 sec('Choice rows', None, '''
<div class="choices" role="radiogroup" aria-label="Plan">
 <label class="choice tall"><span class="lbl">Monthly<small>Billed every month, cancel any time</small></span><input type="radio" name="r1" checked><span class="mark dot"></span></label>
 <label class="choice tall"><span class="lbl">Yearly<small>Two months free</small></span><input type="radio" name="r1"><span class="mark dot"></span></label>
 <label class="choice"><span class="lbl">Other</span><input type="radio" name="r1"><span class="mark dot"></span></label>
</div>'''),
 sec('Tiles', 'Two columns with a 10px gap; one column on phones.', '''
<div class="tiles" role="radiogroup" aria-label="Region">
 <label class="tile"><span class="lbl">Jakarta</span><input type="radio" name="r2" checked><span class="mark dot"></span></label>
 <label class="tile"><span class="lbl">Surabaya</span><input type="radio" name="r2"><span class="mark dot"></span></label>
 <label class="tile"><span class="lbl">Singapore</span><input type="radio" name="r2"><span class="mark dot"></span></label>
 <label class="tile"><span class="lbl">Sydney</span><input type="radio" name="r2"><span class="mark dot"></span></label>
</div>'''),
 sec('Selection cards', 'Picked cards look pressed in, not raised.', '''
<div class="grid-3">
 <label class="sel-card"><input type="radio" name="r3" checked><span class="top">Starter<span class="mark dot"></span></span><span class="d">Up to 5 people and 1,000 claims a month.</span></label>
 <label class="sel-card"><input type="radio" name="r3"><span class="top">Team<span class="mark dot"></span></span><span class="d">Up to 50 people, audit log and SSO.</span></label>
 <label class="sel-card"><input type="radio" name="r3"><span class="top">Enterprise<span class="mark dot"></span></span><span class="d">Custom limits and a dedicated contact.</span></label>
</div>'''),
 specs([
  ('Mark', '18px circle, 1.5px ink-6 ring', '–'),
  ('Selected', 'White well around an 8px ink-12 dot', '--ink-12'),
  ('Tile', '12px padding, 44px min, ink-2 rest, ink-3 picked', '--root-ink-2'),
  ('Card', '124px min, 14px padding; picked = ink-3 + hairline', '–'),
 ]),
 usage(['Preselect the safest or most common option.', 'Put "Other" last; picking it opens a field below.'], ['Use radios for more than 6 options: use a select.', 'Raise the picked card with a bigger shadow.']),
 a11y(['Group with <code>role="radiogroup"</code> and a label.', 'Arrow keys move between options; one tab stop for the group.']),
 code('''<label class="choice"><span class="lbl">Monthly</span>
  <input type="radio" name="plan" checked><span class="mark dot"></span></label>'''))

page('switch', 'Switch', 'Inputs',
 'Turns one setting on or off, and takes effect at once. If the change needs a Save, use a checkbox.',
 sec('In settings', 'Black means on, like every control (white in dark). Orange never fills a switch.', '''
<div class="settings surface-raised">
 <div><div><p>Email alerts</p><p class="ink-11">When a claim needs review</p></div><button class="switch" role="switch" aria-checked="true" aria-label="Email alerts"><span class="knob"></span></button></div>
 <div><div><p>Auto-approve small claims</p><p class="ink-11">Under Rp 1.000.000</p></div><button class="switch" role="switch" aria-checked="false" aria-label="Auto-approve small claims"><span class="knob"></span></button></div>
 <div><div><p>Two-step sign in</p><p class="ink-11">Required by your admin</p></div><button class="switch" role="switch" aria-checked="true" aria-label="Two-step sign in" disabled><span class="knob"></span></button></div>
</div>'''),
 sec('Single row', 'A switch alone in a form sits in a raised row.', '''
<div class="switch-row" style="display:flex;justify-content:space-between;align-items:center;gap:16px"><span>Share with the whole workspace</span><button class="switch" role="switch" aria-checked="false" aria-label="Share with the whole workspace"><span class="knob"></span></button></div>'''),
 specs([
  ('Track', '52 × 26 desktop; 51 × 31 on phone', '--switch-w'),
  ('Knob', '20px, 3px in; 23px, 4px in on phone', '--switch-knob'),
  ('On / off', 'Primary (black; white in dark) / ink-7; #343434 in dark', '--switch-on'),
  ('Motion', 'Knob springs, 450ms, no overshoot past the inset', '–'),
  ('Disabled', 'opacity .6', '–'),
 ]),
 usage(['Write the label as the setting, not the action: "Email alerts".', 'Apply the change immediately.'], ['Pair a switch with a Save button.', 'Use a switch for a choice between two options: use a segmented control.']),
 a11y(['<code>role="switch"</code> with <code>aria-checked</code>.', 'Space and Enter toggle it. Under reduced motion the knob moves at once.']),
 code('''<button class="switch" role="switch" aria-checked="true" aria-label="Email alerts">
  <span class="knob"></span>
</button>'''))

page('segmented', 'Segmented control', 'Inputs',
 'Switches views inside a page, like Day, Week and Month. It is also the tab pattern: there are no underline tabs.',
 sec('View switching', None, '''
<div class="seg" data-seg role="radiogroup" aria-label="Range"><span class="thumb"></span>
 <button type="button" role="radio" aria-pressed="false">Day</button><button type="button" role="radio" aria-pressed="true">Week</button><button type="button" role="radio" aria-pressed="false">Month</button><button type="button" role="radio" aria-pressed="false">Year</button></div>'''),
 sec('With icons', 'A 14px icon 4px before each label, for page-level settings.', f'''
<div class="seg" data-seg role="radiogroup" aria-label="Theme preview"><span class="thumb"></span>
 <button type="button" role="radio" aria-pressed="true">{I('sun')}Light</button><button type="button" role="radio" aria-pressed="false">{I('moon')}Dark</button><button type="button" role="radio" aria-pressed="false">{I('grid')}System</button></div>'''),
 sec('As tabs', 'Each option shows a different panel below it.', '''
<div class="stack">
 <div class="seg" data-seg data-tabs="tabp" role="tablist" aria-label="Project"><span class="thumb"></span>
  <button type="button" role="tab" aria-pressed="true" data-tab="0">Overview</button><button type="button" role="tab" aria-pressed="false" data-tab="1">Claims</button><button type="button" role="tab" aria-pressed="false" data-tab="2">Members</button></div>
 <div id="tabp" class="card surface-raised"><div data-panel="0"><p class="card-title">Overview</p><p class="ink-11">Status, owner and recent activity for this project.</p></div><div data-panel="1" hidden><p class="card-title">Claims</p><p class="ink-11">12,480 processed in the last 7 days.</p></div><div data-panel="2" hidden><p class="card-title">Members</p><p class="ink-11">Rama, Dita and Bayu can edit.</p></div></div>
</div>'''),
 specs([
  ('Track', '36px, fully round, 4px inset, one step darker than its surface', '--ink-3'),
  ('Option', '28px, 11px sides, 13/20; inactive ink-11', '--control-h-pill'),
  ('Thumb', 'White + toggle shadow; slides with a gentle spring', '--shadow-toggle'),
  ('Phone', '42px track, 34px options, 44pt hit area', '–'),
 ]),
 usage(['Use 2 to 5 short options.', 'Let it hug its content, even inside a modal.'], ['Add underline tabs.', 'Use it for actions; it only switches what is shown.']),
 a11y(['As a filter: <code>role="radiogroup"</code>. As tabs: <code>role="tablist"</code> with <code>aria-controls</code>.', 'One tab stop; arrow keys move between options.']),
 code('''<div class="seg" role="radiogroup"><span class="thumb"></span>
  <button role="radio" aria-pressed="true">Week</button>
  <button role="radio" aria-pressed="false">Month</button>
</div>'''))

page('slider', 'Slider', 'Inputs',
 'Picks a value in a range where the exact number matters less than the feel. Always show the value as a number too.',
 sec('Default', None, '''
<div class="stack" style="gap:28px">
 <div class="slider"><div class="slider-top"><label for="sl1">Auto-approve limit</label><output for="sl1" id="sl1-o">Rp 2.500.000</output></div><input id="sl1" class="range" type="range" min="0" max="10000000" step="500000" value="2500000" data-out="sl1-o" data-fmt="idr"><div class="slider-ticks"><span>Rp 0</span><span>Rp 10.000.000</span></div></div>
 <div class="slider"><div class="slider-top"><label for="sl2">Fraud score threshold</label><output for="sl2" id="sl2-o">70</output></div><input id="sl2" class="range" type="range" min="0" max="100" value="70" data-out="sl2-o"></div>
 <div class="slider"><div class="slider-top"><label for="sl3">Retention</label><output for="sl3">30 days</output></div><input id="sl3" class="range" type="range" min="0" max="90" value="30" disabled></div>
</div>'''),
 specs([
  ('Track', '6px, fully round, ink-4', '--ink-4'),
  ('Fill', 'ink-12 up to the value', '--ink-12'),
  ('Thumb', '20px white knob, ring and drop like the switch', '–'),
  ('Value', 'ink-12, tabular figures, right of the label', '–'),
  ('Focus', '2px orange ring around the thumb', '--focus-ring'),
 ]),
 usage(['Show the current value as text.', 'Pair with a field when people need an exact number.'], ['Use for values that must be precise, like money to transfer.', 'Colour the fill by how risky the value is.']),
 a11y(['Use the native <code>input type="range"</code>; arrow keys step, Page Up/Down jump.', 'Give it a visible label and <code>aria-valuetext</code> when the number needs units.']),
 code('<input class="range" type="range" min="0" max="100" value="70">'))

page('date-picker', 'Date picker', 'Inputs',
 'A field that opens a calendar. People can also type the date. Today has a ring; the chosen day is filled.',
 sec('Field', 'Click the field to open the calendar.', f'''
<div class="field"><label for="dp1">Incident date</label>
 <div class="dp" id="dp1-wrap"><div class="input-wrap">{I('calendar','lead')}<input id="dp1" class="input has-lead" placeholder="DD/MM/YYYY" data-datepicker="dp1-cal" autocomplete="off" aria-haspopup="dialog"></div>
 <div class="cal surface-overlay" id="dp1-cal" role="dialog" aria-label="Choose a date"></div></div></div>'''),
 sec('Calendar', 'The popover on its own. Future dates are disabled here because an incident can\'t be in the future.', '''
<div class="cal static surface-overlay" id="dp-static" data-cal-static></div>'''),
 specs([
  ('Popover', '280px, 12px padding, radius 8', '--shadow-menu'),
  ('Day', '34px tall, radius 6, tabular figures', '--radius-control'),
  ('Today', '1px ink-7 inner ring', '–'),
  ('Selected', 'Primary fill and text', '--primary-bg'),
  ('Outside month', 'ink-9; disabled ink-8', '–'),
 ]),
 usage(['Accept typed dates as well as clicks.', 'Disable dates that can\'t be picked, and say why nearby.'], ['Show the time zone on phones.', 'Use a date picker for a birth year: a field is faster.']),
 a11y(['Arrow keys move by day, Page Up/Down by month, Enter picks, Escape closes.', 'Each day has a full label, like "24 November 2026".']),
 code('<input class="input has-lead" placeholder="DD/MM/YYYY" aria-haspopup="dialog">'))

page('file-upload', 'File upload', 'Inputs',
 'A drop area that is also a button. Each file shows as a row with its progress and a way to remove it.',
 sec('Drop area', 'Click or drop files. This demo fakes the upload.', f'''
<div style="max-width:520px">
 <div class="drop" tabindex="0" role="button" id="drop" aria-describedby="drop-h">{I('upload')}<p>Drop files here or click to browse</p><p id="drop-h">PDF, JPG or PNG, up to 10 MB each</p></div>
 <input type="file" id="drop-in" multiple hidden>
 <div class="files" id="files">
  <div class="file"><span class="fi">{I('file')}</span><div style="min-width:0"><p class="nm">medical-receipt-0412.pdf</p><p class="mt">1.2 MB · Uploaded</p></div><button class="btn btn-ghost btn-icon-sm" aria-label="Remove file" data-remove>{I('x')}</button></div>
  <div class="file err"><span class="fi">{I('file')}</span><div style="min-width:0"><p class="nm">xray-scan-full-resolution.tiff</p><p class="mt">This file type isn't supported. Use PDF, JPG or PNG.</p></div><button class="btn btn-ghost btn-icon-sm" aria-label="Remove file" data-remove>{I('x')}</button></div>
 </div>
</div>'''),
 specs([
  ('Drop area', 'ink-2, radius 8, dashed 1px edge, 28px padding', '--ink-2'),
  ('Drag over', 'Fill deepens to ink-3', '–'),
  ('File row', 'Raised like a button, 32px file icon', '--shadow-button'),
  ('Progress', '4px bar, ink-12 fill', '–'),
  ('Error', 'Message replaces the size in red-11', '--red-11'),
 ]),
 usage(['State accepted types and size before upload.', 'Keep failed files in the list with the reason.'], ['Remove a failed file silently.', 'Upload without showing progress for large files.']),
 a11y(['The drop area is a <code>role="button"</code> reachable by Tab; Enter opens the file dialog.', 'Announce finished and failed uploads in a live region.']),
 code('''<div class="drop" role="button" tabindex="0">Drop files here or click to browse</div>
<input type="file" multiple hidden>'''))

page('filter-pill', 'Filter pill', 'Inputs',
 'Shows a filter that is on, with a small × to clear it. The label is quiet; the value leads.',
 sec('Filter row', 'Click × to remove a filter.', f'''
<div class="row" id="fpills" style="gap:8px">
 <span class="fpill"><span class="k">Status</span><span class="v">Failed</span><button class="x" aria-label="Clear status filter">{I('x')}</button></span>
 <span class="fpill"><span class="k">Owner</span><span class="v">Rama</span><button class="x" aria-label="Clear owner filter">{I('x')}</button></span>
 <span class="fpill"><span class="k">Client</span><span class="v">PT Asuransi Jiwa Sejahtera Bersama Indonesia</span><button class="x" aria-label="Clear client filter">{I('x')}</button></span>
 <button class="fpill add" id="fpill-add">{I('plus')}Add filter</button>
</div>'''),
 specs([
  ('Height', '28px; 36px on phone', '--control-h-pill'),
  ('Fill', 'White + toggle shadow', '--shadow-toggle'),
  ('Label / value', 'ink-10 / ink-12', '–'),
  ('Value width', 'Truncates past 180px', '–'),
  ('Clear', '20px round ×; 28px on phone', '–'),
 ]),
 usage(['Keep pills in one row next to the view toggles.', 'Truncate long values and show them in a tooltip.'], ['Wrap pills to a second line on phones: scroll sideways instead.', 'Colour pills by filter type.']),
 a11y(['The × has a label naming the filter it clears.', 'Move focus to the next pill after one is removed.']),
 code('''<span class="fpill"><span class="k">Status</span><span class="v">Failed</span>
  <button class="x" aria-label="Clear status filter">…</button></span>'''))
