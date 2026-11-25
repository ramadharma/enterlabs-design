import html as _h
from icons import I

PAGES = []  # (id, title, group, desc, html)
_uid = [0]

def esc(s):
    return _h.escape(s, quote=False)

def sec(title, desc, body, stage=True, extra=''):
    """A preview section."""
    d = f'<p class="sub-desc">{desc}</p>' if desc else ''
    if stage is True:
        b = f'<div class="sub-body stage surface-sunk {extra}">{body}</div>'
    elif stage == 'raw':
        b = f'<div class="sub-body {extra}">{body}</div>'
    else:
        b = f'<div class="sub-body {extra}">{body}</div>'
    return f'<div class="sub"><h2 class="sub-title">{title}</h2>{d}{b}</div>'

def specs(rows, head=('Property', 'Value', 'Token')):
    th = ''.join(f'<th{" class=\"wrap\"" if i == 1 else ""}>{h}</th>' for i, h in enumerate(head))
    trs = ''
    for r in rows:
        tds = ''
        for i, c in enumerate(r):
            if i == len(r) - 1 and len(head) == 3:
                c = f'<code>{c}</code>' if c and c != '–' else '<span class="dash">–</span>'
            tds += f'<td{" class=\"wrap\"" if i == 1 else ""}>{c}</td>'
        trs += f'<tr>{tds}</tr>'
    return f'<div class="sub"><h2 class="sub-title">Specs</h2><div class="sub-body table-wrap surface-raised"><table class="tbl doc-tbl"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div></div>'

def usage(do, dont):
    lis = lambda xs: ''.join(f'<li>{x}</li>' for x in xs)
    return f'''<div class="sub"><h2 class="sub-title">Usage</h2><div class="sub-body dodont">
<div class="do"><p class="h">{I('check')}Do</p><ul class="rules">{lis(do)}</ul></div>
<div class="dont"><p class="h">{I('x')}Don't</p><ul class="rules">{lis(dont)}</ul></div></div></div>'''

def a11y(items):
    lis = ''.join(f'<li>{x}</li>' for x in items)
    return f'<div class="sub"><h2 class="sub-title">Accessibility</h2><ul class="rules">{lis}</ul></div>'

def code(src):
    _uid[0] += 1
    cid = f'code-{_uid[0]}'
    return f'''<div class="sub"><h2 class="sub-title">Code</h2><div class="sub-body code sm">
<button class="btn btn-outline btn-sm rounded-full" data-copy-target="{cid}">{I('copy')}<span>Copy</span></button>
<pre id="{cid}">{esc(src.strip())}</pre></div></div>'''

def anatomy(items):
    lis = ''.join(f'<li><span>{x}</span></li>' for x in items)
    return f'<div class="sub"><h2 class="sub-title">Anatomy</h2><ol class="anatomy">{lis}</ol></div>'

def page(pid, title, group, desc, *parts):
    body = ''.join(parts)
    html = f'''<article class="page" data-page="{pid}" data-title="{title}" data-group="{group}" tabindex="-1">
<header class="page-head"><h1 class="section-title">{title}</h1><p class="desc">{desc}</p></header>
<div class="body">{body}</div>
</article>'''
    PAGES.append((pid, title, group, desc, html))
    return html
