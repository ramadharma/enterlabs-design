import re, base64, io, html, urllib.parse, sys
from PIL import Image
import os
W=os.path.dirname(os.path.abspath(__file__))
K=os.environ.get('ENTERLABS_KIT', os.path.join(W, '..', 'brand-kit'))
tpl=open(f'{W}/template.html').read()
tokens=open(f'{W}/tokens.css').read()

def clean(svg, keepids=False):
    svg=re.sub(r'<title>.*?</title>','',svg); svg=re.sub(r'<desc>.*?</desc>','',svg)
    svg=re.sub(r'\s(role|aria-label)="[^"]*"','',svg)
    svg=svg.replace('<svg ','<svg role="img" aria-label="Enterlabs" focusable="false" ',1)
    svg=re.sub(r'\sxmlns:xlink="[^"]*"','',svg)
    if not keepids: svg=re.sub(r'\sid="[^"]*"','',svg)
    return svg.strip()
def logo(name, variant=None):
    raw=open(f'{K}/01_VECTOR_MASTER/SVG/enterlabs-{name}-black.svg').read().replace('#000000','currentColor')
    if variant=='tight':
        vb={'horizontal':'1 1 1337.2 269','symbol':'1 1 340 269'}[name]
        raw=re.sub(r'viewBox="[^"]*"',f"viewBox=\"{vb}\"",raw,count=1)
    if variant=='split':
        raw=raw.replace('<g id="word-labs"','<g id="word-labs" transform="translate(150 70) scale(0.72)"')
        raw=raw.replace('<g id="word-enter"','<g id="word-enter" transform="translate(0 -30)"')
    return clean(raw)
def app(c):
    return clean(open(f'{K}/04_ICONS/App/enterlabs-app-{c}.svg').read())
def png(path, size):
    im=Image.open(path).convert('RGB').resize((size,size),Image.LANCZOS); b=io.BytesIO(); im.save(b,'PNG',optimize=True)
    return 'data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()

def repl(m):
    parts=m.group(1).split(':')
    if parts[0]=='svg':
        n=parts[1]
        if n.startswith('app-'): return app(n[4:])
        return logo(n, parts[2] if len(parts)>2 else None)
    if parts[0]=='img':
        c=parts[1].split('-')[1]
        return png(f'{K}/04_ICONS/Social/enterlabs-avatar-{c}-1024.png',176)
    raise SystemExit('unknown '+m.group(1))

# contrast
def lum(h):
    h=h.lstrip('#'); c=[int(h[i:i+2],16)/255 for i in (0,2,4)]
    c=[x/12.92 if x<=0.03928 else ((x+0.055)/1.055)**2.4 for x in c]
    return 0.2126*c[0]+0.7152*c[1]+0.0722*c[2]
def cr(a,b):
    la,lb=sorted([lum(a),lum(b)],reverse=True); return (la+.05)/(lb+.05)
L=dict(zip(range(1,13),"#FBFBFA #F5F5F4 #EDEDEC #E5E5E4 #DEDEDD #D6D6D5 #CACAC9 #B5B5B4 #8A8A89 #737372 #5C5C5B #111111".split()))
D=dict(zip(range(1,13),"#111111 #191919 #232323 #2B2B2B #333333 #3D3D3D #4A4A4A #626262 #737373 #868686 #B4B4B4 #EEEEEE".split()))
WH='#FFFFFF'
rows=[
 ('ink-12 on ink-3', cr(L[12],L[3]), cr(D[12],D[3]), 'Titles, values, labels'),
 ('ink-11 on panel', cr(L[11],WH), cr(D[11],D[1]), 'Descriptions, body copy'),
 ('ink-11 on ink-3', cr(L[11],L[3]), cr(D[11],D[3]), 'Text inside wells and chips'),
 ('ink-10 on panel', cr(L[10],WH), cr(D[10],D[1]), 'Meta, table cells, figure labels'),
 ('ink-10 on ink-3', cr(L[10],L[3]), cr(D[10],D[3]), 'Placeholders and chevrons'),
 ('ink-9 on panel', cr(L[9],WH), cr(D[9],D[1]), 'Icons and decoration only'),
 ('Hairline on panel', cr(L[6],WH), cr(D[5],D[1]), '0.5px lines (needs 1.35:1)'),
 ('Primary label', cr(L[1],L[12]), cr(D[1],D[12]), 'Primary button text'),
 ('Danger: red-11 on red-3', cr('#CA244D','#FEEAED'), cr('#FF949D','#3A141E'), 'Danger badges, red text'),
 ('Success: green-11 on green-3', cr('#00796A','#E0F8F3'), cr('#0BD8B6','#0D2D2A'), 'Success badges'),
 ('Warning: amber-11 on amber-3', cr('#9A5800','#FFF7C2'), cr('#FFCA16','#302008'), 'Warning badges'),
 ('Info: blue-11 on blue-3', cr('#0B68BA','#E6F4FE'), cr('#70B8FF','#0D2847'), 'Info badges'),
 ('White on destructive', cr(WH,'#CA244D'), cr(WH,'#903144'), 'Destructive button'),
 ('Brand: brand-11 on brand-3', cr('#B83300','#FFEFE9'), cr('#FF8A5C','#391A0F'), 'Brand badges'),
 ('Brand text on panel', cr('#D63C01',WH), cr('#FF7038',D[1]), 'Orange words and figures'),
 ('Black on brand orange', cr('#050505','#FF5E1F'), cr('#050505','#FF5E1F'), 'Type and buttons on an orange field'),
 ('Focus ring on panel', cr('#E8500E',WH), cr('#FF7038',D[1]), 'Focus ring (needs 3:1)'),
 ('Focus ring on ground', cr('#E8500E',L[2]), cr('#FF7038','#000000'), 'Focus ring (needs 3:1)'),
 ('Focus ring on a well', cr('#E8500E',L[3]), cr('#FF7038',D[3]), 'Focus ring (needs 3:1)'),
 ('White on brand orange', cr(WH,'#FF5E1F'), cr(WH,'#FF5E1F'), 'Not for text: why buttons stay black'),
]
def fmt(v): return f'{v:.2f}:1'
tr=''.join(f'<tr><td>{a}</td><td>{fmt(b)}</td><td>{fmt(c)}</td><td class="wrap">{d}</td></tr>' for a,b,c,d in rows)
# for a,b,c,d in rows: print(f'{a:22} {b:6.2f} {c:6.2f}')

fav=open(f'{K}/01_VECTOR_MASTER/SVG/enterlabs-micro-black.svg').read()
fav=re.sub(r'<title>.*?</title>|<desc>.*?</desc>','',fav)
favuri='data:image/svg+xml,'+urllib.parse.quote(fav)

out=tpl.replace('[[tokens]]',tokens).replace('[[tokens-escaped]]',html.escape(tokens,quote=False)).replace('[[contrast-rows]]',tr).replace('[[favicon]]',favuri)
out=re.sub(r'\[\[([a-z0-9:-]+)\]\]',repl,out)
assert not re.search(r'\[\[(svg|img|tokens|contrast|favicon)', out)

