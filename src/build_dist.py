"""Build public/dist/: the machine-readable spec that the enterlabs-design skill fetches.

Source: spec/enterlabs.md (the full spec) and tokens.css (the complete token file).
Run: python3 src/build_dist.py
"""
import json, os, re, datetime

W = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(W, '..', 'public', 'dist')
os.makedirs(OUT, exist_ok=True)

spec = open(os.path.join(W, 'spec', 'enterlabs.md')).read()
tokens = open(os.path.join(W, 'tokens.css')).read()
version = re.search(r'^# Enterlabs design system · v([\d.]+)', spec, re.M).group(1)
updated = os.environ.get('SPEC_UPDATED') or datetime.date.today().isoformat()

DESC = {
    'overview': 'What Enterlabs is, the logo kit and UI layer versions, and where the spec lives.',
    'workflow': 'How to work with the spec: pin the output, start from tokens and components, check, report.',
    'brand-and-logo': 'Logo compositions, kit files, clear space, minimum sizes, misuse, inline SVG artwork, favicon wiring.',
    'principles': 'The four principles, in priority order.',
    'tokens': 'How tokens work (roles, dark mode, surfaces), the base CSS, neutral steps by job, checked contrast.',
    'foundations': 'Type scale, spacing, radius, elevation, motion, layout, phone rules, icons.',
    'colour-roles': 'Brand orange (where it goes and never goes), status hues, links, charts, illustration and imagery.',
    'components': 'The spec of every component: actions, inputs, data display, feedback, overlays, navigation.',
    'component-css': 'Component CSS, markup recipes and the behaviour the CSS expects.',
    'copy': 'Copy rules: sentence case, verbs, ellipsis, locale formats.',
    'before-you-ship': 'The checklist that must pass before anything ships.',
    'review-mode': 'How to audit existing work against the spec.',
}

def slug(t):
    return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')

parts = re.split(r'^## (\d+)\. (.+)$', spec, flags=re.M)
pages = []
head = parts[0].strip()
body = head.split('\n', 1)[1].strip()
open(os.path.join(OUT, 'overview.md'), 'w').write(f'# Enterlabs · Overview (v{version})\n\n{body}\n')
pages.append({'path': 'overview.md', 'section': 0, 'title': 'Overview', 'description': DESC['overview']})
for i in range(1, len(parts), 3):
    n, title, text = int(parts[i]), parts[i + 1].strip(), parts[i + 2].strip()
    s = slug(title)
    open(os.path.join(OUT, f'{s}.md'), 'w').write(f'# Enterlabs · {n}. {title} (v{version})\n\n{text}\n')
    pages.append({'path': f'{s}.md', 'section': n, 'title': title, 'description': DESC.get(s, '')})

open(os.path.join(OUT, 'enterlabs.md'), 'w').write(spec)

css_blocks = re.findall(r'```css\n(.*?)```', spec, re.S)
open(os.path.join(OUT, 'tokens.css'), 'w').write(tokens)
open(os.path.join(OUT, 'base.css'), 'w').write(css_blocks[1])
open(os.path.join(OUT, 'components.css'), 'w').write(css_blocks[2])

# Every token the spec states must match the token file, or the two have drifted.
def props(t):
    d = {}
    for scope, block in re.findall(r'([^{}]+)\{([^{}]*)\}', t):
        sc = scope.strip().split('\n')[-1].strip()
        for k, v in re.findall(r'(--[\w-]+)\s*:\s*([^;]+);', block):
            d[(sc, k)] = ' '.join(v.split())
    return d
a, b = props(css_blocks[0]), props(tokens)
drift = [f'{k[0]} {k[1]}: spec {a[k]} / tokens.css {b.get(k)}' for k in a if b.get(k) != a[k]]
if drift:
    raise SystemExit('Token drift between spec/enterlabs.md and tokens.css:\n  ' + '\n  '.join(drift))

index = {
    'name': 'Enterlabs design system',
    'version': version,
    'updated': updated,
    'site': 'https://enterlabs-design-systems.pages.dev',
    'full': 'enterlabs.md',
    'pages': pages,
    'files': [
        {'path': 'tokens.css', 'description': 'Complete token file: light, dark, phone, surfaces.'},
        {'path': 'base.css', 'description': 'Base CSS to paste once, before the components.'},
        {'path': 'components.css', 'description': 'Core component CSS (buttons, fields, choices, switch, badge, table, menu, modal, toast...).'},
    ],
    'assets': '../assets/brand/',
}
open(os.path.join(OUT, 'index.json'), 'w').write(json.dumps(index, indent=2) + '\n')
print('dist', version, updated, len(pages), 'pages')
