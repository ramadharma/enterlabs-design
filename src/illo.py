from icons import I

SW = [('Base', '--illo-base', 'White ground'), ('Line', '--illo-line', 'Every stroke'), ('Strong line', '--illo-line-strong', 'The shape in focus'),
      ('Soft fill', '--illo-fill', 'Groups'), ('Grid', '--illo-grid', 'Dot grid, rings'), ('Orange', '--illo-accent', 'The point, once')]
swatches = ''.join(
    f'<div class="st"><button class="c" style="background:var({v})" data-copy="var({v})" aria-label="Copy {v}"></button>'
    f'<span class="n">{n}</span><span class="h">{v}</span></div>' for n, v, _ in SW)


def doc(x, y):
    return f'<path class="ln" d="M{x} {y} h9 l5 5 v15 h-14 z M{x+9} {y} v5 h5"/>'


HERO = f'''<svg viewBox="0 0 640 280" role="img" aria-labelledby="illo-t illo-d">
  <title id="illo-t">Documents flow into review</title>
  <desc id="illo-d">A claim, an invoice and a policy flow into a review step. One path ends approved, the other is flagged.</desc>
  <defs><pattern id="illo-dots" width="16" height="16" patternUnits="userSpaceOnUse"><circle class="grid" cx="2" cy="2" r="1"/></pattern></defs>
  <rect width="640" height="280" fill="url(#illo-dots)"/>
  <circle class="ring" cx="320" cy="140" r="84"/>
  <path class="ln dash" d="M160 68 C 216 68, 216 140, 272 140"/>
  <path class="ln dash" d="M160 140 L 272 140"/>
  <path class="ln dash" d="M160 212 C 216 212, 216 140, 272 140"/>
  <circle class="acc-dot" cx="222" cy="140" r="3"/>
  <path class="ln" d="M368 140 C 420 140, 420 82, 472 82"/>
  <path class="ln dash" d="M368 140 C 420 140, 420 198, 472 198"/>
  <rect class="node" x="40" y="46" width="120" height="44" rx="8"/>{doc(56, 58)}<text class="lbl" x="82" y="73">Claim</text>
  <rect class="node" x="40" y="118" width="120" height="44" rx="8"/>{doc(56, 130)}<text class="lbl" x="82" y="145">Invoice</text>
  <rect class="node" x="40" y="190" width="120" height="44" rx="8"/>{doc(56, 202)}<text class="lbl" x="82" y="217">Policy</text>
  <rect class="acc-node" x="272" y="92" width="96" height="96" rx="16"/>
  <path class="acc" d="M300 114 h24 l10 10 v34 h-34 z M324 114 v10 h10 M308 132 h18 M308 140 h18 M308 148 h10"/>
  <circle class="acc-node" cx="334" cy="160" r="9"/><path class="acc" d="M340.5 166.5 L 348 174"/>
  <text class="lbl hi" x="320" y="212" text-anchor="middle">Review</text>
  <rect class="node" x="472" y="60" width="128" height="44" rx="8"/>
  <path class="strong" d="M490 82 l5 5 l9 -10"/><text class="lbl hi" x="514" y="87">Approved</text>
  <rect class="node dash" x="472" y="176" width="128" height="44" rx="8"/>
  <path class="ln" d="M491 192 l11 11 M502 192 l-11 11"/><text class="lbl" x="514" y="203">Flagged</text>
</svg>'''

HERO_V = f'''<svg viewBox="0 0 340 420" role="img" aria-labelledby="illo-tv illo-dv">
  <title id="illo-tv">Documents flow into review</title>
  <desc id="illo-dv">A claim, an invoice and a policy flow into a review step. One path ends approved, the other is flagged.</desc>
  <defs><pattern id="illo-dots-v" width="16" height="16" patternUnits="userSpaceOnUse"><circle class="grid" cx="2" cy="2" r="1"/></pattern></defs>
  <rect width="340" height="420" fill="url(#illo-dots-v)"/>
  <circle class="ring" cx="170" cy="200" r="84"/>
  <path class="ln dash" d="M60 64 C 60 112, 170 104, 170 152"/>
  <path class="ln dash" d="M170 64 L 170 152"/>
  <path class="ln dash" d="M280 64 C 280 112, 170 104, 170 152"/>
  <circle class="acc-dot" cx="170" cy="110" r="3"/>
  <path class="ln" d="M170 248 C 170 290, 89 290, 89 330"/>
  <path class="ln dash" d="M170 248 C 170 290, 251 290, 251 330"/>
  <rect class="node" x="14" y="20" width="92" height="44" rx="8"/><text class="lbl" x="60" y="47" text-anchor="middle">Claim</text>
  <rect class="node" x="124" y="20" width="92" height="44" rx="8"/><text class="lbl" x="170" y="47" text-anchor="middle">Invoice</text>
  <rect class="node" x="234" y="20" width="92" height="44" rx="8"/><text class="lbl" x="280" y="47" text-anchor="middle">Policy</text>
  <rect class="acc-node" x="122" y="152" width="96" height="96" rx="16"/>
  <path class="acc" d="M150 174 h24 l10 10 v34 h-34 z M174 174 v10 h10 M158 192 h18 M158 200 h18 M158 208 h10"/>
  <circle class="acc-node" cx="184" cy="220" r="9"/><path class="acc" d="M190.5 226.5 L 198 234"/>
  <text class="lbl hi" x="232" y="204">Review</text>
  <rect class="node" x="14" y="330" width="150" height="44" rx="8"/>
  <path class="strong" d="M32 352 l5 5 l9 -10"/><text class="lbl hi" x="56" y="357">Approved</text>
  <rect class="node dash" x="176" y="330" width="150" height="44" rx="8"/>
  <path class="ln" d="M195 346 l11 11 M206 346 l-11 11"/><text class="lbl" x="218" y="357">Flagged</text>
</svg>'''

SPOTS = [
    ('Upload documents', '''<svg viewBox="0 0 160 100" aria-hidden="true">
  <rect class="node" x="46" y="14" width="46" height="60" rx="6"/>
  <rect class="node" x="58" y="24" width="46" height="60" rx="6"/>
  <path class="ln" d="M68 40 h26 M68 48 h26 M68 56 h16"/>
  <circle class="acc-node" cx="108" cy="78" r="14"/><path class="acc" d="M108 85 v-14 M102 77 l6 -6 l6 6"/>
</svg>'''),
    ('Review in minutes', '''<svg viewBox="0 0 160 100" aria-hidden="true">
  <rect class="node" x="50" y="14" width="52" height="68" rx="6"/>
  <path class="ln" d="M60 30 h32 M60 38 h32 M60 46 h20"/>
  <circle class="acc-node" cx="98" cy="66" r="15"/><path class="acc" d="M108.5 76.5 L 118 86"/>
</svg>'''),
    ('Kept private', '''<svg viewBox="0 0 160 100" aria-hidden="true">
  <path class="node" d="M80 12 l30 10 v24 c0 20 -14 32 -30 40 c-16 -8 -30 -20 -30 -40 v-24 z"/>
  <rect class="acc-node" x="70" y="46" width="20" height="16" rx="3"/><path class="acc" d="M74 46 v-5 a6 6 0 0 1 12 0 v5"/>
</svg>'''),
]
spots = ''.join(f'<div class="spot illo">{svg}<p>{t}</p></div>' for t, svg in SPOTS)

imagery = f'''<h1 class="section-title">Illustration and imagery</h1>
  <p class="desc">Show the product working first. Live diagrams, demo widgets and real screens explain more than any picture. When an idea can't be shown that way, draw it as clean line art: grey strokes on white, with one orange element for the point of the picture.</p>
  <div class="body">
    <div class="sub"><h2 class="sub-title">Diagrams</h2>
      <p class="sub-desc">Flat and technical, like a system drawing. Abstract ideas get a metaphor: a flow, a network, a gate. One idea per picture.</p>
      <div class="sub-body stack">
        <div class="illo"><div class="illo-wide">{HERO}</div><div class="illo-tall">{HERO_V}</div></div>
        <div class="dodont">
          <div class="do"><p class="h">{I('check')}Do</p><ul class="rules"><li>Lines only: 1.5px, round caps and joins, like the icons</li><li>Grey, white and orange, nothing else</li><li>Orange once per picture, on the thing it's about</li><li>White nodes with a grey edge, radius 8; soft grey for groups</li><li>A faint dot grid behind diagrams, if it helps</li><li>Real text labels; state shown with an icon and a word</li><li>Alt text on every illustration that carries meaning</li></ul></div>
          <div class="dont"><p class="h">{I('x')}Don't</p><ul class="rules"><li>Gradients, glows, shadows or 3D rendering</li><li>Any colour other than grey, white and orange, status hues included</li><li>Filled scenes, mascots, clip art or stock people</li><li>Orange on more than one element</li><li>The logo, or shapes cut from it, used as decoration</li></ul></div>
        </div>
      </div></div>

    <div class="sub"><h2 class="sub-title">Spot illustrations</h2>
      <p class="sub-desc">96 to 160px wide, beside a feature or an empty state on marketing pages. Same stroke, same rules. In product UI, use an 18px icon instead.</p>
      <div class="sub-body spots">{spots}</div></div>

    <div class="sub"><h2 class="sub-title">Colours</h2>
      <p class="sub-desc">Six roles from the neutral and the brand orange. They follow the theme on their own, so dark mode needs no second drawing. Click one to copy its token.</p>
      <div class="sub-body swatch-row illo-swatches">{swatches}</div></div>

    <div class="sub"><h2 class="sub-title">How to draw meaning</h2>
      <p class="sub-desc">With only grey and orange, meaning comes from shape, line style and words.</p>
      <div class="sub-body table-wrap surface-raised"><table class="tbl doc-tbl"><thead><tr><th>Meaning</th><th class="wrap">Draw it with</th></tr></thead><tbody>
        <tr><td>The point of the picture</td><td class="wrap">Orange stroke, or one small orange dot for data on the move</td></tr>
        <tr><td>Flow and structure</td><td class="wrap">Grey lines at 1.5px. Solid for the main path, dashed for optional, waiting or async</td></tr>
        <tr><td>Things and steps</td><td class="wrap">White nodes with a grey edge; groups as soft grey areas with no edge</td></tr>
        <tr><td>Success, approved</td><td class="wrap">Solid node, a tick and a word in strong ink</td></tr>
        <tr><td>Blocked, failed</td><td class="wrap">Dashed node and path, a cross and a word in grey. Never red, never orange</td></tr>
        <tr><td>Labels</td><td class="wrap">Inter 500, 12px, label ink; the focus in strong ink</td></tr>
      </tbody></table></div>
      <ul class="rules" style="margin-top:12px">
        <li>Isometric line drawings only when depth explains the idea, such as layers or a stack. Same stroke, no shading.</li>
        <li>On a phone, redraw a wide diagram as a vertical one so labels stay about 12px. Never scale text below that.</li>
      </ul></div>

    <div class="sub"><h2 class="sub-title">Photography and video</h2>
      <div class="sub-body grid-2" style="align-items:start">
        <div class="media-frame" role="img" aria-label="16 by 9 video frame">{I('play')}</div>
        <ul class="rules">
          <li>Prefer real product footage: screens, flows, a demo running.</li>
          <li>Hero video: full-bleed with an AVIF poster. It stays still for reduced motion or low data.</li>
          <li>People: real customer headshots only, cropped in circles, in testimonials. No stock photos.</li>
          <li>AVIF or WebP with 1x and 2x sources. The hero loads first; everything below the fold loads lazily.</li>
          <li>Set the aspect ratio before the image arrives, so nothing jumps.</li>
        </ul>
      </div></div>

    <div class="sub"><h2 class="sub-title">Customer logos</h2>
      <p class="sub-desc">Monochrome SVG in <code>currentColor</code> (ink-10), at the same optical height, 24 to 32px, with 48 to 64px between them.</p>
      <div class="sub-body stage surface-sunk"><div class="logo-row" aria-label="Placeholder customer logos">
        <span class="cl">{I('grid')}Customer</span><span class="cl">{I('shield')}Customer</span><span class="cl">{I('chart')}Customer</span><span class="cl">{I('key')}Customer</span>
      </div></div></div>

    <div class="sub"><h2 class="sub-title">Brand colour in layouts</h2>
      <ul class="rules">
        <li>On marketing pages, orange appears in every layout: a small accent or a flat full-bleed field with black type. In product UI it stays rare (see <a class="link" href="#/colour">Colour</a>).</li>
        <li>No gradients anywhere: not in art, backgrounds, buttons or text.</li>
        <li>The Enterlabs mark appears only as the logo, under the <a class="link" href="#/logo">logo rules</a>. It is never cropped, tiled or layered into a decorative shape.</li>
        <li>Cream (<code>--cream</code>) is for warm bands on marketing pages, never product UI.</li>
      </ul></div>
  </div>'''
