import re, html as _h, sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build as B  # reuses logo(), app(), png(), contrast rows via its module-level code
from icons import sprite, I, ICONS
import dsl
from illo import imagery
import c_inputs, c_display, c_rest  # noqa: populate dsl.PAGES

W = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(W, '..', 'public', 'index.html')
v1 = open(f'{W}/template_v1.html').read()

# ---------- head + css ----------
head = v1[:v1.index('</style>')]
head = head.replace('<title>Enterlabs design system</title>', '<title>Enterlabs design system</title>')
comp_css = open(f'{W}/components.css').read()
comp_css += '''
.sheet-grab.grab { display: none; }
@media screen and (width < 48rem) { .modal .sheet-grab.grab, .side-panel .sheet-grab.grab { display: grid; } }
.page { padding: 0; }
'''
head += '\n' + comp_css + '\n</style>\n</head>\n'

# ---------- foundation sections from v1 ----------
def section(sid):
    m = re.search(r'<section id="%s"[^>]*>(.*?)\n</section>' % sid, v1, re.S)
    return m.group(1)

FOUND = [
 ('overview', 'Overview', 'Start'), ('principles', 'Principles', 'Start'),
 ('logo', 'Logo', 'Brand'), ('icons', 'App icons and favicon', 'Brand'), ('colour', 'Colour', 'Brand'), ('imagery', 'Illustration and imagery', 'Brand'),
 ('type', 'Typography', 'Foundations'), ('spacing', 'Spacing and sizes', 'Foundations'), ('shape', 'Shape and elevation', 'Foundations'),
 ('iconography', 'Iconography', 'Foundations'), ('motion', 'Motion', 'Foundations'), ('layout', 'Layout', 'Foundations'),
]
REF = [('tokens', 'Tokens', 'Reference'), ('checklist', 'Before you ship', 'Reference')]

def art(pid, title, group, inner):
    return f'<article class="page" data-page="{pid}" data-title="{title}" data-group="{group}" tabindex="-1">\n{inner}\n</article>'

def found_inner(pid):
    s = section(pid)
    s = s.replace('<h2 class="section-title">', '<h1 class="section-title">', 1).replace('</h2>', '</h1>', 1)
    if pid == 'overview':
        s = s.replace('Every specimen on this page is built from the tokens at the end, so what you see is what ships, in light and dark.',
                      'Every specimen here, from a button to a bottom sheet, is built from the same tokens, so what you see is what ships, in light and dark.')
        s = s.replace('<div><p class="figure-n">1</p><p class="figure-l">Typeface, one weight</p></div>',
                      '<div><p class="figure-n">[[ncomp]]</p><p class="figure-l">Components, each on its own page</p></div>')
        s += '''
  <div class="body"><div class="row"><a class="btn btn-default" href="#/components">Browse components</a><a class="btn btn-outline" href="#/logo">Logo guidelines</a><a class="btn btn-ghost" href="#/tokens">Get the tokens</a></div></div>'''
    if pid == 'motion':
        s = s.replace('<p class="desc">', '<p class="desc">', 1)
    return s

# iconography page
icon_cells = ''.join(f'<button class="icon-cell" data-copy="#i-{k}" aria-label="Copy {k}">{I(k)}<span>{k}</span></button>' for k in ICONS)
iconography = f'''<h1 class="section-title">Iconography</h1>
  <p class="desc">One outline set: round caps and joins, about 1.5px rendered at 16px, drawn on a 24px grid. Icons support words; they rarely replace them.</p>
  <div class="body">
    <div class="sub"><h2 class="sub-title">Sizes</h2><p class="sub-desc">14px beside small text in pills and toggles, 16px in buttons and rows, 18px in empty states, 20px standalone.</p>
      <div class="sub-body stage surface-sunk"><div class="icon-sizes">
        <div class="s"><svg style="width:14px;height:14px"><use href="#i-folder"/></svg><span class="meta">14</span></div>
        <div class="s"><svg style="width:16px;height:16px"><use href="#i-folder"/></svg><span class="meta">16</span></div>
        <div class="s"><svg style="width:18px;height:18px"><use href="#i-folder"/></svg><span class="meta">18</span></div>
        <div class="s"><svg style="width:20px;height:20px"><use href="#i-folder"/></svg><span class="meta">20</span></div>
        <div class="s"><svg style="width:24px;height:24px"><use href="#i-folder"/></svg><span class="meta">24 phone</span></div>
      </div></div></div>
    <div class="sub"><h2 class="sub-title">Ink</h2>
      <div class="sub-body table-wrap surface-raised"><table class="tbl doc-tbl"><thead><tr><th>Where</th><th class="wrap">Ink</th></tr></thead><tbody>
        <tr><td>Leading icon in a white button</td><td class="wrap">ink-9; the label carries the meaning</td></tr>
        <tr><td>Row and icon buttons</td><td class="wrap">ink-10, ink-12 on hover</td></tr>
        <tr><td>Navigation rows</td><td class="wrap">ink-10; ink-12 on the current row</td></tr>
        <tr><td>Inside the primary or a tint</td><td class="wrap">The text colour of its container</td></tr>
        <tr><td>Status</td><td class="wrap">Never an icon alone: a dot in its hue plus a word</td></tr>
      </tbody></table></div></div>
    <div class="sub"><h2 class="sub-title">Set</h2><p class="sub-desc">Click an icon to copy its sprite reference.</p>
      <div class="sub-body icon-grid">{icon_cells}</div></div>
    <ul class="rules">
      <li>An icon beside text is centred on the text's line, not sat on its baseline.</li>
      <li>Checkmarks are slightly rounded everywhere. A filled glyph means "ready to run".</li>
      <li>The external-link arrow appears only when a link truly leaves the app.</li>
      <li>Don't put icons in boxes or circles to make them look important.</li>
      <li>Icons never turn orange, not even when active: the current row's icon goes ink-12.</li>
      <li>In code, use Lucide (it ships with shadcn). Spot illustrations follow <a class="link" href="#/imagery">Illustration and imagery</a>.</li>
    </ul>
  </div>'''

# components index
GROUP_ORDER = ['Actions', 'Inputs', 'Data display', 'Feedback', 'Overlays', 'Navigation']
by_group = {g: [p for p in dsl.PAGES if p[2] == g] for g in GROUP_ORDER}
def first_sentence(s):
    s = re.sub('<[^>]+>', '', s)
    m = re.match(r'(.+?[.!?])(\s|$)', s)
    return m.group(1) if m else s
cards = ''
for g in GROUP_ORDER:
    cs = ''.join(f'<a class="ccard" href="#/{p[0]}"><span class="t">{p[1]}</span><span class="d">{first_sentence(p[3])}</span></a>' for p in by_group[g])
    cards += f'<div><p class="cgroup-title">{g}</p><div class="cgrid">{cs}</div></div>'
ncomp = len(dsl.PAGES)
comp_index = f'''<h1 class="section-title">Components</h1>
  <p class="desc">{ncomp} components, each with its own page: live preview, specs, usage, accessibility notes and code. Every one borrows its fill, edge and drop from the surface it sits on.</p>
  <div class="body cindex">{cards}</div>'''

# ---------- order ----------
ORDER = []  # (id, title, group, inner_html)
for pid, t, g in FOUND:
    if pid == 'iconography': ORDER.append((pid, t, g, iconography))
    elif pid == 'imagery': ORDER.append((pid, t, g, imagery))
    else: ORDER.append((pid, t, g, found_inner(pid)))
ORDER.append(('components', 'All components', 'Components', comp_index))
for g in GROUP_ORDER:
    for p in by_group[g]:
        inner = re.sub(r'^<article[^>]*>\n|\n</article>$', '', p[4])
        ORDER.append((p[0], p[1], g, inner))
for pid, t, g in REF:
    ORDER.append((pid, t, g, found_inner(pid)))

# pager nav
articles = []
for i, (pid, t, g, inner) in enumerate(ORDER):
    pv = ORDER[i - 1] if i > 0 else None
    nx = ORDER[i + 1] if i < len(ORDER) - 1 else None
    nav = '<nav class="pager-nav" aria-label="Pages">'
    if pv: nav += f'<a class="prev" href="#/{pv[0]}"><span class="k">Previous</span><span class="t">{pv[1]}</span></a>'
    if nx: nav += f'<a class="next" href="#/{nx[0]}"><span class="k">Next</span><span class="t">{nx[1]}</span></a>'
    nav += '</nav>'
    articles.append(art(pid, t, g, inner + '\n' + nav))

# rail + select
rail = ''; sel = ''; lastg = None
for pid, t, g, _ in ORDER:
    if g != lastg:
        rail += f'<p class="nav-group">{g}</p>'
        if lastg is not None: sel += '</optgroup>'
        sel += f'<optgroup label="{g}">'
        lastg = g
    rail += f'<a href="#/{pid}">{t}</a>'
    sel += f'<option value="{pid}">{t}</option>'
sel += '</optgroup>'

TERMS = '<h3>1. What we process</h3><p>Claim records, policy numbers, medical receipts and the names and contact details of claimants, as sent by your systems.</p><h3>2. Why we process it</h3><p>Only to score claims for fraud risk, route them for review and keep the audit log you can export.</p><h3>3. Where it is stored</h3><p>In data centres in Jakarta. Backups stay in Indonesia and are encrypted at rest and in transit.</p><h3>4. Who can see it</h3><p>People you invite, within the role you give them. Our staff see it only when you open a support request and grant access.</p><h3>5. How long we keep it</h3><p>For as long as your contract runs, then 90 days so you can export it. After that it is deleted, backups included.</p><h3>6. Subprocessors</h3><p>We use a small number of subprocessors for hosting and email. The current list is in Settings, under Legal.</p><h3>7. Your requests</h3><p>Claimants can ask to see or correct their data through you. We answer your requests within 14 days.</p><h3>8. Changes</h3><p>We tell admins at least 30 days before these terms change. Continuing to use the service after that means you accept them.</p>'
FB_BTN = '''<button type="button" class="btn btn-outline btn-sm fb-open" id="fb-open" data-open="fb-panel" aria-label="Feedback">[[edit]]<span class="fb-label">Feedback</span><span class="kpill fb-n" id="fb-n" hidden></span></button>'''.replace('[[edit]]', I('edit'))
THEME = '''<div class="seg seg-sm" id="theme-seg" role="radiogroup" aria-label="Theme"><span class="thumb" aria-hidden="true"></span>
<button type="button" data-v="light" role="radio" aria-pressed="false">[[sun]]Light</button><button type="button" data-v="dark" role="radio" aria-pressed="false">[[moon]]Dark</button></div>'''.replace('[[sun]]', I('sun')).replace('[[moon]]', I('moon'))

OVERLAYS = f'''
<div class="scrim" id="scrim"></div>
<div class="modal surface-overlay" id="md-form" role="dialog" aria-modal="true" aria-labelledby="md-form-t" aria-describedby="md-form-d" data-guard>
 <button class="sheet-grab grab" data-close aria-label="Close"><i></i></button>
 <div class="dialog-head"><p class="dialog-title" id="md-form-t">Create project</p><p class="ink-11" id="md-form-d" style="margin-top:4px">Projects group claims from one client.</p></div>
 <form class="dialog-body" id="md-form-f" novalidate onsubmit="return false">
  <div class="field"><label for="mf-name">Project name</label><input id="mf-name" class="input" placeholder="E.g. Claims portal" autocomplete="off" aria-describedby="mf-name-m"><p class="hint" id="mf-name-m">Everyone in the workspace sees this name.</p></div>
  <div class="field"><label for="mf-client">Client</label><div class="select-wrap"><select id="mf-client" class="input"><option>PT Asuransi Jiwa Sejahtera</option><option>Mitra Sehat</option><option>Bumi Proteksi</option></select>[[chev]]</div></div>
  <div class="field"><label for="mf-desc">Description <span class="opt">(optional)</span></label><textarea id="mf-desc" class="input" placeholder="What is this project for?"></textarea></div>
 </form>
 <div class="dialog-foot"><button class="btn btn-outline" data-close>Cancel</button><button class="btn btn-default" id="mf-submit" data-requires="mf-name" disabled><span class="label-swap"><span>Create project</span></span></button></div>
</div>
<div class="modal sm surface-overlay" id="md-confirm" role="dialog" aria-modal="true" aria-labelledby="md-confirm-t" aria-describedby="md-confirm-d">
 <button class="sheet-grab grab" data-close aria-label="Close"><i></i></button>
 <div class="dialog-head"><p class="dialog-title" id="md-confirm-t">Archive Claims portal?</p><p class="ink-11" id="md-confirm-d" style="margin-top:4px">It stops receiving new claims and moves to Archived. You can restore it any time.</p></div>
 <div class="dialog-foot"><button class="btn btn-outline" data-close>Cancel</button><button class="btn btn-default" data-close data-toast-after="Project archived">Archive project</button></div>
</div>
<div class="modal sm surface-overlay" id="md-downgrade" role="dialog" aria-modal="true" aria-labelledby="md-dg-t" aria-describedby="md-dg-d">
 <button class="sheet-grab grab" data-close aria-label="Close"><i></i></button>
 <div class="dialog-head"><p class="dialog-title" id="md-dg-t">Downgrade to Starter?</p><p class="ink-11" id="md-dg-d" style="margin-top:4px">On 30 December you lose SSO, the audit log and 45 of your 50 seats. Reviewers over the limit are signed out.</p></div>
 <div class="dialog-foot"><button class="btn btn-outline" data-close data-toast-after="Downgrade scheduled for 30 Dec" data-tone="amber">Downgrade</button><button class="btn btn-default" data-close>Keep Team plan</button></div>
</div>
<div class="modal info surface-overlay" id="md-info" role="dialog" aria-modal="true" aria-labelledby="md-info-t">
 <button class="sheet-grab grab" data-close aria-label="Close"><i></i></button>
 <div class="dialog-head"><p class="dialog-title" id="md-info-t">Keyboard shortcuts</p><p class="ink-11" style="margin-top:4px">Work through the review queue without the mouse.</p><button class="btn btn-ghost btn-icon-sm x-close" data-close aria-label="Close">[[x]]</button></div>
 <div class="dialog-body keylist">
  <div><span>Search</span><span class="keys"><span class="kchip">⌘</span><span class="kchip">K</span></span></div>
  <div><span>New project</span><span class="keys"><span class="kchip">N</span></span></div>
  <div><span>Approve claim</span><span class="keys"><span class="kchip">A</span></span></div>
  <div><span>Send to reviewer</span><span class="keys"><span class="kchip">R</span></span></div>
  <div><span>Next claim</span><span class="keys"><span class="kchip">J</span></span></div>
  <div><span>Previous claim</span><span class="keys"><span class="kchip">K</span></span></div>
 </div>
</div>
<div class="modal surface-overlay" id="md-steps" role="dialog" aria-modal="true" aria-labelledby="md-steps-t" aria-describedby="md-steps-d">
 <button class="sheet-grab grab" data-close aria-label="Close"><i></i></button>
 <div class="dialog-head"><p class="dialog-title" id="md-steps-t">Invite reviewers</p><p class="ink-11" id="md-steps-d" style="margin-top:4px">They get an email with a sign-in link that works for 7 days.</p></div>
 <div class="dialog-body mbody-hold">
  <div class="mstep" data-s="form">
   <div class="field"><label for="ms-emails">Email addresses</label><textarea id="ms-emails" class="input" placeholder="One per line" aria-describedby="ms-emails-m">dita@enterlabs.id
bayu@enterlabs.id
sari@enterlabs.id</textarea><p class="hint" id="ms-emails-m">Up to 20 at a time.</p></div>
   <div class="field"><label for="ms-role">Role</label><div class="select-wrap"><select id="ms-role" class="input"><option>Reviewer</option><option>Auditor</option><option>Admin</option></select>[[chev]]</div></div>
  </div>
  <div class="mstep mcenter" data-s="busy" hidden tabindex="-1"><span class="spinner s18" aria-hidden="true"></span><p class="ink-11">Sending invites…</p></div>
  <div class="mstep mcenter" data-s="done" hidden tabindex="-1"><span class="done-disc">[[check]]</span><p class="ink-12" id="ms-done-t">3 invites sent</p><p class="ink-11">They'll appear under Members once accepted.</p></div>
 </div>
 <div class="dialog-foot" data-f="form"><button class="btn btn-outline" data-close>Cancel</button><button class="btn btn-default" id="ms-send">Send invites</button></div>
 <div class="dialog-foot" data-f="done" hidden><span></span><button class="btn btn-outline" data-close>Close</button></div>
</div>
<div class="modal surface-overlay" id="md-scroll" role="dialog" aria-modal="true" aria-labelledby="md-scroll-t" aria-describedby="md-scroll-d">
 <button class="sheet-grab grab" data-close aria-label="Close"><i></i></button>
 <div class="dialog-head"><p class="dialog-title" id="md-scroll-t">Data processing terms</p><p class="ink-11" id="md-scroll-d" style="margin-top:4px">Version 3, effective 1 December 2026.</p></div>
 <div class="dialog-body prose" tabindex="0" aria-label="Terms text">[[terms]]</div>
 <div class="dialog-foot"><button class="btn btn-outline" data-close>Cancel</button><button class="btn btn-default" data-close data-toast-after="Terms accepted">I agree</button></div>
</div>
<div class="modal sm surface-overlay" id="dlg-del" role="alertdialog" aria-modal="true" aria-labelledby="dlg-del-t" aria-describedby="dlg-del-d">
 <button class="sheet-grab grab" data-close aria-label="Close"><i></i></button>
 <div class="dialog-head"><p class="dialog-title danger" id="dlg-del-t">Delete Claims portal?</p><p class="ink-11" id="dlg-del-d" style="margin-top:4px">Its 12,480 claims and their history go with it. This can't be undone.</p></div>
 <div class="dialog-foot"><button class="btn btn-outline" data-close>Cancel</button><button class="btn btn-destructive" data-close data-toast-after="Project deleted">Delete project</button></div>
</div>
<aside class="side-panel surface-overlay" id="panel1" role="dialog" aria-labelledby="panel1-t">
 <button class="sheet-grab grab" data-close aria-label="Close"><i></i></button>
 <div class="dialog-head"><div><div class="row" style="gap:8px"><p class="dialog-title" id="panel1-t">CLM-1044</p><span class="badge red">Flagged</span></div><p class="ink-11" style="margin-top:4px">Bumi Proteksi · submitted 21 Nov</p></div><button class="btn btn-ghost btn-icon-sm" data-close aria-label="Close panel">{I('x')}</button></div>
 <div class="dialog-body">
  <dl class="kv"><dt>Amount</dt><dd>Rp 87.000.000</dd><dt>Fraud score</dt><dd>86 / 100</dd><dt>Incident</dt><dd>12 Nov 2026</dd><dt>Hospital</dt><dd>RS Medika Jakarta</dd><dt>Owner</dt><dd><span class="person"><span class="avatar-i av-20">DA</span>Dita Anggraini</span></dd></dl>
  <div class="inline-alert hue-amber">{I('info')}<span>Same patient filed a claim at another hospital on the same day.</span></div>
  <div class="field"><label for="pn">Note</label><textarea id="pn" class="input" placeholder="Add a note for the reviewer"></textarea></div>
 </div>
 <div class="dialog-foot"><button class="btn btn-outline" data-close data-toast-after="Sent to reviewer">Send to reviewer</button><button class="btn btn-default" data-close data-toast-after="Claim approved">Approve</button></div>
</aside>
<aside class="side-panel surface-overlay" id="fb-panel" role="dialog" aria-labelledby="fb-t" aria-describedby="fb-d">
 <button class="sheet-grab grab" data-close aria-label="Close"><i></i></button>
 <div class="dialog-head"><div><p class="dialog-title" id="fb-t">Feedback</p><p class="ink-11" id="fb-d" style="margin-top:4px">On <span id="fb-page" class="ink-12">this page</span>. Everyone on the team can read it.</p></div><button class="btn btn-ghost btn-icon-sm" data-close aria-label="Close feedback">{I('x')}</button></div>
 <div class="dialog-body">
  <div class="inline-alert hue-blue" id="fb-offline" hidden>{I('info')}<span>Comments work on the published site. This copy can't reach the feedback server.</span></div>
  <form id="fb-form" class="fb-form" novalidate>
   <div class="field"><label for="fb-name">Your name</label><input id="fb-name" class="input" autocomplete="name" maxlength="80"></div>
   <div class="field"><label for="fb-body">Comment</label><textarea id="fb-body" class="input" maxlength="2000" placeholder="What should change on this page?" aria-describedby="fb-err"></textarea><p class="err" id="fb-err" hidden></p></div>
   <div class="field" id="fb-code-f" hidden><label for="fb-code">Team code</label><input id="fb-code" class="input" autocomplete="off"><p class="hint">Ask the design system owner. You only enter it once.</p></div>
   <input type="text" id="fb-hp" class="sr-only" tabindex="-1" autocomplete="off" aria-hidden="true">
   <div class="fb-actions"><button class="btn btn-default" type="submit" id="fb-send">Post comment</button></div>
  </form>
  <div class="fb-thread"><h2 class="sub-title" id="fb-list-t">On this page</h2><div id="fb-list" class="fb-list" aria-live="polite"></div></div>
 </div>
 <div class="dialog-foot"><span></span><a class="btn btn-outline" href="feedback/">All feedback</a></div>
</aside>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
'''

body = f'''<body>
{sprite()}
<a class="sr-only" href="#main">Skip to content</a>
<div class="shell">
  <aside class="rail surface-rail" aria-label="Contents">
    <div class="rail-brand logo">[[svg:horizontal]]</div>
    <p class="rail-version meta">Design system v0.3</p>
    <nav class="nav" id="nav" aria-label="Pages">{rail}</nav>
  </aside>
  <main class="panel surface-panel" id="main">
    <header class="strip">
      <div class="strip-start">
        <span class="rail-mark logo">[[svg:symbol]]</span>
        <div class="jump-wrap select-wrap"><label class="sr-only" for="jump">Go to page</label>
          <select id="jump" class="btn btn-outline" style="padding-right:32px;appearance:none;-webkit-appearance:none">{sel}</select>{I('chev')}</div>
        <nav class="crumbs crumbs-wrap" id="crumbs" aria-label="Breadcrumb"></nav>
      </div>
      <div class="strip-end row" style="gap:8px">{FB_BTN}{THEME}</div>
    </header>
    <div class="col">
{chr(10).join(articles)}
    </div>
  </main>
</div>
{OVERLAYS}
<script>
{open(f'{W}/app.js').read()}
</script>
<script>
{open(f'{W}/fb.js').read()}
</script>
</body>
</html>
'''
body = body.replace('[[chev]]', I('chev')).replace('[[x]]', I('x')).replace('[[check]]', I('check')).replace('[[terms]]', TERMS)
tpl = head + body
tpl = tpl.replace('[[ncomp]]', str(ncomp))

tokens = open(f'{W}/tokens.css').read()
out = tpl.replace('[[tokens]]', tokens).replace('[[tokens-escaped]]', _h.escape(tokens, quote=False)).replace('[[contrast-rows]]', B.tr).replace('[[favicon]]', B.favuri)
out = re.sub(r'\[\[((?:svg|img):[a-z0-9:-]+)\]\]', B.repl, out)
assert not re.search(r'\[\[(svg|img|tokens|contrast|favicon|ncomp)', out)
out = out.replace('href="#/', 'href="#')
open(OUT, 'w').write(out)
print('pages', len(ORDER), 'components', ncomp, 'bytes', len(out))


# ---------- feedback inbox: public/feedback/index.html ----------
INBOX = head + f'''<body>
{sprite()}
<main class="panel surface-panel inbox" id="main">
  <header class="strip">
    <div class="strip-start">
      <a class="logo inbox-mark" href="../" aria-label="Enterlabs design system">[[svg:symbol]]</a>
      <nav class="crumbs" aria-label="Breadcrumb"><a href="../">Design system</a>{I('chev-r')}<span aria-current="page">Feedback</span></nav>
    </div>
    <div class="strip-end">{THEME}</div>
  </header>
  <div class="col ib-col">
    <div class="ib-head">
      <div><h1 class="section-title">Feedback</h1><p class="desc">Comments from the team on every docs page. Resolve one once the docs are updated.</p></div>
      <button type="button" class="btn btn-outline" id="ib-copy">{I('copy')}<span>Copy as Markdown</span></button>
    </div>
    <div class="ib-bar">
      <div class="seg" id="ib-filter" role="radiogroup" aria-label="Status"><span class="thumb" aria-hidden="true"></span><button type="button" role="radio" data-v="open" aria-pressed="true">Open</button><button type="button" role="radio" data-v="resolved" aria-pressed="false">Resolved</button><button type="button" role="radio" data-v="all" aria-pressed="false">All</button></div>
      <span class="meta" id="ib-count" aria-live="polite"></span>
    </div>
    <form class="card surface-raised ib-key" id="ib-key-form" novalidate><div id="ib-key" hidden>
      <div class="field"><label for="ib-key-f">Admin key</label>
        <div class="row" style="gap:8px;flex-wrap:nowrap"><input id="ib-key-f" class="input" type="password" autocomplete="off" aria-describedby="ib-key-h ib-key-err"><button class="btn btn-default" type="submit">Unlock</button></div>
        <p class="hint" id="ib-key-h">Anyone can read feedback. Resolving needs the admin key.</p><p class="err" id="ib-key-err" hidden>That key isn't right.</p></div>
    </div></form>
    <div class="table-wrap surface-raised" id="ib-table"><table class="tbl" aria-label="Feedback">
      <thead><tr><th>Page</th><th class="wrap">Comment</th><th>From</th><th>When</th><th>Status</th><th class="act"><span class="sr-only">Action</span></th></tr></thead>
      <tbody id="ib-rows"></tbody></table></div>
    <div class="empty" id="ib-state" hidden></div>
  </div>
</main>
<script>
{open(f'{W}/inbox.js').read()}
</script>
</body>
</html>
'''
INBOX = re.sub(r'\[\[((?:svg|img):[a-z0-9:-]+)\]\]', B.repl, INBOX).replace('[[favicon]]', B.favuri).replace('[[tokens]]', tokens).replace('href="#/', 'href="#')
assert '[[' not in INBOX
INBOX = INBOX.replace('<title>Enterlabs design system</title>', '<title>Feedback · Enterlabs design system</title>')
os.makedirs(os.path.join(W, '..', 'public', 'feedback'), exist_ok=True)
open(os.path.join(W, '..', 'public', 'feedback', 'index.html'), 'w').write(INBOX)
print('inbox', len(INBOX))
