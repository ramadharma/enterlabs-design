from dsl import *
from icons import I

page('badge', 'Badge', 'Data display',
 'A short status or category. Fully round, tinted with its own hue, with an edge drawn from that same hue.',
 sec('Status', 'Hue means status only.', '''
<div class="row" style="gap:8px">
 <span class="badge green"><span class="dot"></span>Live</span><span class="badge red">Failed</span><span class="badge amber">Needs review</span><span class="badge blue">Beta</span><span class="badge neutral">Paused</span>
</div>'''),
 sec('Beside a title', 'Next to a 20px title the badge steps up to 24px, 8px from the title.', '''
<div class="row" style="gap:8px"><span class="section-title">Claims portal</span><span class="badge badge-lg green"><span class="dot"></span>Live</span></div>'''),
 sec('Brand', 'The one badge in brand orange, for brand moments only: something new or recommended. It never carries a status.', '''
<div class="row" style="gap:8px"><span class="badge brand">New</span><span class="badge brand">Recommended</span><span class="badge brand">First 50 claims free</span></div>'''),
 sec('Status dot', 'In tables and dense lists, a dot with its label replaces the badge. Ongoing states pulse.', '''
<div class="row" style="gap:20px">
 <span class="status-dot green ping"><span class="dot"></span>Processing</span><span class="status-dot green"><span class="dot"></span>Live</span><span class="status-dot amber"><span class="dot"></span>In review</span><span class="status-dot red"><span class="dot"></span>Failed</span><span class="status-dot neutral"><span class="dot"></span>Paused</span>
</div>'''),
 sec('Loading', 'A pulsing pill holds the badge\'s place, so nothing shifts.', '<span class="skel-badge" aria-label="Loading"></span>'),
 specs([
  ('Height', '20px; 24px beside a 20px title; 22px on phone', '--badge-h'),
  ('Padding', '8px; 6px on the icon side', '–'),
  ('Colour', 'hue-3 fill, hue-11 text; success teal, danger ruby, warning amber, info blue', '--green-3'),
  ('Edge', '1px ring 14% + drop 16% of its own text colour', '--shadow-badge'),
  ('Neutral', 'White with the button shadow, ink-11 text', '--shadow-button'),
  ('Brand', 'brand-3 fill, brand-11 text; New, Recommended', '--brand-3'),
  ('Dot', '6px in a badge, 8px on its own', '–'),
 ]),
 usage(['Keep labels to one or two words, max 24 characters.', 'Use one badge formula at every size.'], ['Use a badge as a button.', 'Pick a hue for looks; status wins every clash.']),
 a11y(['Never rely on colour alone: the word says the status.', 'A pulsing dot stops pulsing under reduced motion.']),
 code('''<span class="badge green"><span class="dot"></span>Live</span>
<span class="status-dot amber"><span class="dot"></span>In review</span>'''))

page('avatar', 'Avatar', 'Data display',
 'Shows a person or workspace. Initials on a quiet fill when there is no photo.',
 sec('Sizes', '20, 24, 32, 40 and 56px.', '''
<div class="row" style="gap:16px;align-items:flex-end">
 <span class="avatar-i av-20">RS</span><span class="avatar-i av-24">RS</span><span class="avatar-i av-32">RS</span><span class="avatar-i av-40">RS</span><span class="avatar-i av-56"><img src="[[img:avatar-black]]" alt="Enterlabs"></span>
</div>'''),
 sec('With details and status', None, '''
<div class="row" style="gap:32px">
 <div class="person"><span class="av-status"><span class="avatar-i av-32">DA</span><span class="dot"></span></span><div><p class="n">Dita Anggraini</p><p class="e">Claims reviewer · Online</p></div></div>
 <div class="person"><span class="av-stack"><span class="avatar-i av-24">RS</span><span class="avatar-i av-24">DA</span><span class="avatar-i av-24">BP</span><span class="avatar-i av-24">+4</span></span><span class="ink-11">7 members</span></div>
</div>'''),
 specs([
  ('Shape', 'Circle; workspaces may use the 6px radius', '–'),
  ('Fill', 'ink-3, ink-11 initials', '--ink-3'),
  ('Edge', '0.5px inner ring', '–'),
  ('Stack', '6px overlap, 2px ring in the surface colour', '–'),
  ('Status dot', '10px, success (teal), 2px surface ring', '--green-9'),
 ]),
 usage(['Use two initials from the person\'s name.', 'Cap a stack at 3 to 4 and show "+N".'], ['Colour avatars by person.', 'Use avatars where a name alone is clearer.']),
 a11y(['Images get the person\'s name as <code>alt</code>; decorative stacks are <code>aria-hidden</code> with the count in text.']),
 code('<span class="avatar-i av-32">RS</span>'))

page('card', 'Card', 'Data display',
 'One unit of related data, raised off its surface. Section headings sit outside the card, so the card doesn\'t repeat them.',
 sec('Data card', 'One strong figure beats six small ones.', '''
<div class="grid-2">
 <div class="card surface-raised"><div class="card-head"><p class="card-title">Processed claims</p><span class="badge green"><span class="dot"></span>Live</span></div><p class="figure-n" style="margin-top:16px">12,480</p><p class="figure-l">Last 7 days</p></div>
 <div class="card surface-raised"><div class="card-strip"><span>Review time</span><button class="btn btn-outline btn-sm rounded-full">Details</button></div><p class="figure-n">4m 12s</p><p class="figure-l">Median, down from 6m 40s</p></div>
</div>'''),
 sec('Clickable card', 'Hover fills, press squeezes to 99%.', f'''
<div class="grid-3">
 <button class="card-click"><span class="t">Connect a data source</span><span class="d">Bring claims in from your core system.</span></button>
 <button class="card-click"><span class="t">Invite your team</span><span class="d">Reviewers, admins and auditors.</span></button>
 <button class="card-click"><span class="t">Set review rules</span><span class="d">Decide what gets checked by hand.</span></button>
</div>'''),
 specs([
  ('Surface', 'White in light; ink-2 with 0.5px ink-6 outline in dark', '--raised'),
  ('Shadow', 'Ring + 1px drop + one short drop', '--shadow-card'),
  ('Radius', '8px', '--radius-container'),
  ('Padding', '20 to 24px; 12 to 16px for clickable cards', '–'),
  ('Header strip', '46px, 0.5px rule under it, action at right', '–'),
 ]),
 usage(['Keep cards in a row the same height.', 'Put the card\'s action at the right of its header.'], ['Nest a card in a card.', 'Use a card for a list of links: use plain rows.']),
 a11y(['A clickable card is one <code>&lt;button&gt;</code> or <code>&lt;a&gt;</code>, not a div with a click handler.']),
 code('''<div class="card surface-raised">
  <p class="card-title">Processed claims</p>
  <p class="figure-n">12,480</p><p class="figure-l">Last 7 days</p>
</div>'''))

page('stat', 'Stat and meter', 'Data display',
 'A figure with its label, a meter for a quantity against a limit, and stat rows for several numbers on a phone.',
 sec('Figures', 'Label directly under the number.', '''
<div class="figures" style="margin-top:0"><div><p class="figure-n">12,480</p><p class="figure-l">Claims processed</p></div><div><p class="figure-n">98.2%</p><p class="figure-l">Auto-approved</p></div><div><p class="figure-n">1.2M</p><p class="figure-l">Rupiah saved, compact</p></div><div><p class="figure-n">–</p><p class="figure-l">Fraud flagged, no data</p></div></div>'''),
 sec('Meters', 'Every bar is 10px. It turns red only for something running out.', '''
<div class="stack" style="max-width:400px;gap:24px">
 <div class="meter"><div class="meter-top"><span class="l">Seats</span><span class="a">18 <span>/ 25</span></span></div><div class="meter-bar"><i style="width:72%"></i></div></div>
 <div class="meter"><div class="meter-top"><span class="l">API calls left this month</span><span class="a">4,120 <span>/ 50,000</span></span></div><div class="meter-bar low"><i style="width:8.2%"></i></div></div>
</div>'''),
 sec('Stat rows', 'On phones, many numbers become rows so they stay a glance.', '''
<div class="stat-rows surface-raised"><div><span class="l">Submitted</span><span class="v">1,204</span></div><div><span class="l">In review</span><span class="v">86</span></div><div><span class="l">Approved</span><span class="v">1,092</span></div><div><span class="l">Rejected</span><span class="v">26</span></div></div>'''),
 specs([
  ('Figure', '24/32 ink-12, tabular figures', '--text-figure'),
  ('Label', '13/20 ink-10 under it', '--ink-10'),
  ('Meter bar', '10px, ink-4 track, ink-12 fill', '–'),
  ('Low', 'red-9 at 10% remaining or less', '--red-9'),
  ('Large numbers', 'Over 6 digits go compact (1.2M)', '–'),
  ('Missing', 'An en dash in ink-9', '–'),
 ]),
 usage(['Lead with the one number that answers the question.', 'Show "/ total" in a quieter ink.'], ['Animate numbers as they change.', 'Show a grid of six equal small numbers.']),
 a11y(['Give a meter <code>role="meter"</code> with <code>aria-valuenow</code>, min and max.', 'Write compact numbers out in a tooltip and accessible name.']),
 code('''<p class="figure-n">12,480</p><p class="figure-l">Claims processed</p>'''))

page('table', 'Table', 'Data display',
 'Many records with the same fields. Actions sit above the table; paging sits below it, outside the frame.',
 sec('Default', 'Tick rows to select them: the actions above switch to what you can do with the selection. Click Amount to sort.', f"""
<div class="stack">
 <div class="tbl-bar">
  <p class="card-title">Claims</p>
  <div class="row tbl-acts" data-when="none" style="gap:8px"><button class="btn btn-outline btn-sm">{I('down','ico ico-lead')}Export</button></div>
  <div class="row tbl-acts" data-when="some" hidden style="gap:8px"><span class="ink-11" id="tsel" aria-live="polite"></span><button class="btn btn-sm btn-ghost" id="tclear">Clear</button><button class="btn btn-outline btn-sm">Send to reviewer</button><button class="btn btn-outline btn-sm">Approve</button></div>
 </div>
 <div class="table-wrap surface-raised">
  <table class="tbl hoverable sel" id="tbl-sel" aria-label="Claims">
   <thead><tr>
    <th class="chk"><label class="row-check"><input type="checkbox" aria-label="Select all claims on this page"><span class="mark box"></span></label></th>
    <th>Claim</th><th>Client</th><th>Status</th>
    <th aria-sort="none"><button class="th-sort" data-sort="amount">Amount{I('chev','sort-ico')}</button></th>
    <th class="act"><span class="sr-only">Actions</span></th>
   </tr></thead>
   <tbody>
    <tr data-amount="4250000"><td class="chk"><label class="row-check"><input type="checkbox" aria-label="Select CLM-1042"><span class="mark box"></span></label></td><td>CLM-1042</td><td><div class="trunc" title="PT Asuransi Jiwa Sejahtera Bersama Indonesia">PT Asuransi Jiwa Sejahtera Bersama Indonesia</div></td><td><span class="status green"><span class="dot"></span>Approved</span></td><td>Rp 4.250.000</td><td class="act"><button class="btn btn-ghost btn-icon-sm" aria-label="More for CLM-1042">{I('more')}</button></td></tr>
    <tr data-amount="12900000"><td class="chk"><label class="row-check"><input type="checkbox" aria-label="Select CLM-1043"><span class="mark box"></span></label></td><td>CLM-1043</td><td>Mitra Sehat</td><td><span class="status amber"><span class="dot"></span>In review</span></td><td>Rp 12.900.000</td><td class="act"><button class="btn btn-ghost btn-icon-sm" aria-label="More for CLM-1043">{I('more')}</button></td></tr>
    <tr data-amount="87000000"><td class="chk"><label class="row-check"><input type="checkbox" aria-label="Select CLM-1044"><span class="mark box"></span></label></td><td>CLM-1044</td><td>Bumi Proteksi</td><td><span class="status red"><span class="dot"></span>Flagged</span></td><td>Rp 87.000.000</td><td class="act"><button class="btn btn-ghost btn-icon-sm" aria-label="More for CLM-1044">{I('more')}</button></td></tr>
    <tr data-amount="0" class="inactive"><td class="chk"></td><td>CLM-1031</td><td>Mitra Sehat</td><td><span class="status neutral"><span class="dot"></span>Withdrawn</span></td><td><span class="dash">–</span></td><td class="act"></td></tr>
   </tbody>
  </table>
 </div>
 <div class="pager"><span class="count">Showing 1 to 4 of 32</span><div class="btns"><button class="btn btn-outline btn-sm" disabled>Previous</button><button class="btn btn-outline btn-sm">Next</button></div></div>
</div>"""),
 sec('Without selection', 'Most tables have no checkbox column. The first column names the row and leads in ink-12.', """
<div class="table-wrap surface-raised"><table class="tbl hoverable" aria-label="Reviewers"><thead><tr><th>Reviewer</th><th>Role</th><th>Open claims</th><th>Median time</th></tr></thead><tbody>
 <tr><td><span class="person"><span class="avatar-i av-20">DA</span>Dita Anggraini</span></td><td>Reviewer</td><td>24</td><td>3m 48s</td></tr>
 <tr><td><span class="person"><span class="avatar-i av-20">BP</span>Bayu Pratama</span></td><td>Admin</td><td>9</td><td>5m 02s</td></tr>
 <tr><td><span class="person"><span class="avatar-i av-20">SR</span>Sari Rahma</span></td><td>Auditor</td><td><span class="dash">–</span></td><td><span class="dash">–</span></td></tr>
</tbody></table></div>"""),
 sec('Loading', 'Keep the frame and column widths; pulse bars where values will be.', """
<div class="table-wrap surface-raised"><table class="tbl" aria-busy="true" aria-label="Claims, loading"><thead><tr><th>Claim</th><th>Client</th><th>Status</th><th>Amount</th></tr></thead><tbody>
 <tr><td><span class="skel-bar" style="width:64px"></span></td><td><span class="skel-bar" style="width:120px"></span></td><td><span class="skel-bar" style="width:72px"></span></td><td><span class="skel-bar" style="width:88px"></span></td></tr>
 <tr><td><span class="skel-bar" style="width:64px"></span></td><td><span class="skel-bar" style="width:96px"></span></td><td><span class="skel-bar" style="width:72px"></span></td><td><span class="skel-bar" style="width:80px"></span></td></tr>
 <tr><td><span class="skel-bar" style="width:64px"></span></td><td><span class="skel-bar" style="width:132px"></span></td><td><span class="skel-bar" style="width:72px"></span></td><td><span class="skel-bar" style="width:92px"></span></td></tr>
</tbody></table></div>"""),
 anatomy(['Title and actions, above the frame', 'Optional selection column: checkbox in the leading padding, no divider', 'Header row: ink-12, 0.5px rule under it', 'Identifying column in ink-12; other cells ink-10', 'Actions column: hugs a ghost icon-sm button', 'Pager, 12px under the frame']),
 specs([
  ('Row', '38px; 44pt on phone', '--row-h'),
  ('Frame', '0.5px line, radius 8, table drop', '--shadow-table'),
  ('Cells', '14px padding, left-aligned, tabular figures', '–'),
  ('Selection column', '16px in, 18px mark, 12px to the next cell, no divider', '–'),
  ('Ink', 'Header and identifying column ink-12, others ink-10', '–'),
  ('Hover / selected', 'Ground + 1 / ground + 2', '--ink-3'),
  ('Sort', '14px ink-9 chevron; ink-12 on the sorted column', '–'),
  ('Inactive row', 'Whole row at 50%, nothing to select', '–'),
  ('Free text', 'Truncates past 30 to 32ch with a tooltip', '–'),
 ]),
 usage(['Keep one typeface in every cell.', 'Show status as a dot with its word.', 'Swap the actions above the table when rows are selected.', 'Stop overview tables at 5 or 6 rows, then "View all".'],
       ['Put the pager or actions inside the table frame.', 'Draw a divider after the checkbox column.', 'Offer a checkbox on a row that can\'t be acted on.', 'Zebra-stripe short tables.']),
 a11y(['Use real <code>&lt;table&gt;</code> and <code>&lt;th&gt;</code> with an accessible name.', 'Sortable headers are buttons; the header cell carries <code>aria-sort</code>.', 'Each row checkbox names its row: "Select CLM-1042". The selection count is announced.', 'Row actions name their row: "More for CLM-1042".']),
 code("""<div class="table-wrap surface-raised">
  <table class="tbl sel" aria-label="Claims">
    <thead><tr>
      <th class="chk"><label class="row-check"><input type="checkbox" aria-label="Select all"><span class="mark box"></span></label></th>
      <th>Claim</th><th aria-sort="none"><button class="th-sort">Amount</button></th>
    </tr></thead>
    <tbody><tr>
      <td class="chk">…</td><td>CLM-1042</td><td>Rp 4.250.000</td>
    </tr></tbody>
  </table>
</div>"""))

page('list', 'List', 'Data display',
 'Plain rows for navigation and short lists: no box, fill on hover only. Settings on a phone group into one raised card of rows.',
 sec('Navigation rows', None, f'''
<div class="list">
 <a href="#/list" onclick="return false" aria-current="true">{I('home')}<span class="grow">Overview</span></a>
 <a href="#/list" onclick="return false">{I('folder')}<span class="grow">Projects</span><span class="m">12</span></a>
 <a href="#/list" onclick="return false">{I('users')}<span class="grow">Members</span><span class="m">7</span></a>
 <a href="#/list" onclick="return false">{I('sliders')}<span class="grow">Settings</span></a>
</div>'''),
 sec('Rows in a card', 'For a group of related records or settings.', f'''
<div class="rows-card surface-raised">
 <a href="#/list" onclick="return false"><span class="avatar-i av-32">DA</span><div class="grow"><p class="t">Dita Anggraini</p><p class="d">Reviewer · dita@enterlabs.id</p></div>{I('chev','chev')}</a>
 <a href="#/list" onclick="return false"><span class="avatar-i av-32">BP</span><div class="grow"><p class="t">Bayu Pratama</p><p class="d">Admin · bayu@enterlabs.id</p></div>{I('chev','chev')}</a>
 <a href="#/list" onclick="return false"><span class="avatar-i av-32">SR</span><div class="grow"><p class="t">Sari Rahma</p><p class="d">Auditor · sari@enterlabs.id</p></div>{I('chev','chev')}</a>
</div>'''),
 specs([
  ('Row', '36px plain; 52px in a card; 48pt in a phone sheet', '–'),
  ('Icon', '16px ink-10, 8px before the label', '–'),
  ('Hover / current', 'ink-2 / ink-3', '–'),
  ('Card rows', '0.5px rules between rows, none at the ends', '--line'),
  ('Meta', 'Counts in ink-10, tabular', '--ink-10'),
 ]),
 usage(['Use plain rows for link lists and navigation.', 'Lead with the identifying text, meta at the right.'], ['Draw lines between plain rows.', 'Slide one highlight between rows on hover.']),
 a11y(['Mark the current item with <code>aria-current</code>.', 'Each row is one link or button.']),
 code('''<div class="list">
  <a href="/projects" aria-current="true"><svg class="ico">…</svg>Projects</a>
</div>'''))

page('accordion', 'Accordion', 'Data display',
 'Folds secondary detail, like FAQs or advanced settings, under its question. Not for primary content.',
 sec('Default', None, f'''
<div class="acc" data-acc>
 <div class="acc-item"><button class="acc-btn" aria-expanded="true">How long does a claim review take?{I('chev')}</button><div class="acc-panel"><div><p>Most claims are scored in under a minute. Claims flagged for review wait for a person, usually within one working day.</p></div></div></div>
 <div class="acc-item"><button class="acc-btn" aria-expanded="false">Who can approve high-value claims?{I('chev')}</button><div class="acc-panel"><div><p>Only admins and reviewers with the high-value role. You can change this in Settings, under Roles.</p></div></div></div>
 <div class="acc-item"><button class="acc-btn" aria-expanded="false">Can I export the audit log?{I('chev')}</button><div class="acc-panel"><div><p>Yes. Export as CSV from the Audit page. Exports cover up to 12 months at a time.</p></div></div></div>
</div>'''),
 specs([
  ('Row', '48px min, question in ink-12', '–'),
  ('Chevron', '16px ink-9, turns over when open', '–'),
  ('Divider', '0.5px between items, none at the ends', '--line'),
  ('Motion', 'Height and fade, 300ms', '--dur-move'),
 ]),
 usage(['Write each header as the question people ask.', 'Allow several items open at once.'], ['Hide something people need to finish their task.', 'Nest accordions.']),
 a11y(['Each header is a <code>&lt;button&gt;</code> with <code>aria-expanded</code> and <code>aria-controls</code>.']),
 code('''<button class="acc-btn" aria-expanded="false">Question<svg>…</svg></button>
<div class="acc-panel"><div><p>Answer</p></div></div>'''))

page('tooltip', 'Tooltip', 'Data display',
 'Names an icon-only action, or shows the full value of something truncated. It appears at once, with no delay.',
 sec('Default', 'Hover or tab to each button.', f'''
<div class="row" style="gap:24px;padding-top:28px">
 <span class="tip-wrap"><button class="btn btn-outline btn-icon" aria-label="Download">{I('down')}</button><span class="tip" role="tooltip">Download</span></span>
 <span class="tip-wrap"><button class="btn btn-outline btn-icon" aria-label="Search">{I('search')}</button><span class="tip" role="tooltip">Search<span class="kpill">⌘K</span></span></span>
 <span class="tip-wrap"><button class="btn btn-outline btn-icon" aria-label="Share link">{I('link')}</button><span class="tip quiet" role="tooltip">Share link</span></span>
 <span class="tip-wrap"><span class="chip" tabindex="0" style="cursor:default"><span>el_live_8f2c…91ab</span></span><span class="tip" role="tooltip">el_live_8f2c4e7d0b3a91ab</span></span>
</div>'''),
 specs([
  ('Fill', 'ink-12 with ink-1 text; or ink-3 with a hairline', '--ink-12'),
  ('Text', '12/16, one line', '--text-meta'),
  ('Padding', '4px × 8px, radius 6', '–'),
  ('Offset', '6px from the trigger', '–'),
  ('Delay', 'None, in or out', '–'),
 ]),
 usage(['Name the action in a word or two.', 'Show a shortcut key inside it.'], ['Put information people need only in a tooltip.', 'Use tooltips on touch: they never show.']),
 a11y(['Show on focus as well as hover; link with <code>aria-describedby</code> or use it as the label.', 'Escape hides an open tooltip.']),
 code('''<span class="tip-wrap">
  <button class="btn btn-ghost btn-icon-sm" aria-label="Download">…</button>
  <span class="tip" role="tooltip">Download</span>
</span>'''))

page('key-chip', 'Key chip', 'Data display',
 'Shows a keyboard shortcut. Hidden on phones and touch screens, where there are no keys to press.',
 sec('Variants', None, f'''
<div class="stack" style="gap:16px">
 <div class="row"><button class="btn btn-default">Create project<span class="kbd">N</span></button><span class="ink-11">Button key chip, on the page primary only</span></div>
 <div class="row"><button class="search-trigger" style="width:240px">{I('search')}<span class="grow">Search…</span><span class="kpill">⌘K</span></button><span class="ink-11">Search key pill</span></div>
 <div class="row"><span class="keys"><span class="kchip">⌘</span><span class="kchip">⇧</span><span class="kchip">P</span></span><span class="ink-11">Combination in text</span></div>
</div>'''),
 specs([
  ('Button chip', '18px, 11px mono, 8px after the label', '--key-chip'),
  ('Search pill', '20px, 12/16 sans, 6px sides', '--badge-h'),
  ('Fill', '14% of its own text colour', '–'),
  ('Radius', 'Half the control radius, 3px', '--radius-xs'),
 ]),
 usage(['Use platform symbols: ⌘ on Mac, Ctrl elsewhere.'], ['Put key chips on secondary or navigation buttons.']),
 a11y(['Expose shortcuts with <code>aria-keyshortcuts</code> on the control.']),
 code('<button class="btn btn-default" aria-keyshortcuts="N">Create project<span class="kbd">N</span></button>'))
