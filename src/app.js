(function () {
  var root = document.documentElement;
  var reduce = matchMedia('(prefers-reduced-motion: reduce)');
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ---------- Segmented controls ---------- */
  function placeThumb(seg, instant) {
    var on = seg.querySelector('button[aria-pressed="true"]'), th = seg.querySelector('.thumb');
    if (!on || !th || !seg.offsetWidth) return;
    if (instant) seg.classList.add('no-anim');
    th.style.width = on.offsetWidth + 'px';
    th.style.transform = 'translateX(' + on.offsetLeft + 'px)';
    if (instant) { th.offsetWidth; seg.classList.remove('no-anim'); }
  }
  function initSeg(seg, onChange) {
    var btns = $$('button', seg);
    seg.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b) return;
      btns.forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); x.setAttribute('aria-checked', x === b ? 'true' : 'false'); x.tabIndex = x === b ? 0 : -1; });
      placeThumb(seg);
      if (seg.dataset.tabs) $$('[data-panel]', document.getElementById(seg.dataset.tabs)).forEach(function (p) { p.hidden = p.dataset.panel !== b.dataset.tab; });
      if (onChange) onChange(b);
    });
    seg.addEventListener('keydown', function (e) {
      if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
      var i = btns.indexOf(document.activeElement); if (i < 0) return;
      e.preventDefault();
      var n = btns[(i + (e.key === 'ArrowRight' ? 1 : btns.length - 1)) % btns.length];
      n.focus(); n.click();
    });
    btns.forEach(function (x) { x.tabIndex = x.getAttribute('aria-pressed') === 'true' ? 0 : -1; });
    placeThumb(seg, true);
  }
  function placeAll(scope) { $$('.seg', scope).forEach(function (s) { placeThumb(s, true); }); }

  var themeSeg = $('#theme-seg');
  $$('button', themeSeg).forEach(function (b) { b.setAttribute('aria-pressed', b.dataset.v === root.getAttribute('data-theme') ? 'true' : 'false'); });
  initSeg(themeSeg, function (b) { root.setAttribute('data-theme', b.dataset.v); try { localStorage.setItem('el-theme', b.dataset.v); } catch (e) {} });
  $$('[data-seg]').forEach(function (s) { initSeg(s); });
  window.addEventListener('resize', function () { placeAll(); });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { placeAll(); });

  /* ---------- Router: one page at a time ---------- */
  var pages = $$('.page'), byId = {};
  pages.forEach(function (p) { byId[p.dataset.page] = p; });
  var navLinks = $$('#nav a'), jump = $('#jump'), crumbs = $('#crumbs');
  var groupOf = { Start: null, Brand: 'Brand', Foundations: 'Foundations', Reference: 'Reference' };
  function crumbHTML(p) {
    var g = p.dataset.group, t = p.dataset.title, parts = [];
    var chev = '<svg aria-hidden="true"><use href="#i-chev-r"/></svg>';
    if (g === 'Start') parts.push('<span aria-current="page">' + t + '</span>');
    else if (groupOf.hasOwnProperty(g)) parts.push('<span>' + g + '</span>', chev, '<span aria-current="page">' + t + '</span>');
    else if (g === 'Components') parts.push('<span aria-current="page">Components</span>');
    else parts.push('<a href="#components">Components</a>', chev, '<span>' + g + '</span>', chev, '<span aria-current="page">' + t + '</span>');
    return parts.join('');
  }
  function route() {
    var id = (location.hash.match(/^#\/?([\w-]+)/) || [])[1] || 'overview';
    if (id === 'dialog') id = 'modal'; if (id === 'sidebar') id = 'sidebar-nav';
    var p = byId[id] || byId.overview;
    closeAll(true);
    pages.forEach(function (x) { x.classList.toggle('on', x === p); });
    navLinks.forEach(function (a) { a.setAttribute('aria-current', a.getAttribute('href') === '#' + p.dataset.page ? 'page' : 'false'); });
    var cur = $('#nav a[aria-current="page"]');
    if (cur) { var r = $('.rail'), top = cur.offsetTop, h = r.clientHeight; if (top < r.scrollTop + 80 || top > r.scrollTop + h - 80) r.scrollTop = top - h / 2; }
    crumbs.innerHTML = crumbHTML(p);
    if (jump.value !== p.dataset.page) jump.value = p.dataset.page;
    document.title = p.dataset.title + ' · Enterlabs design system';
    window.scrollTo(0, 0);
    placeAll(p);
    if (window._routed) p.focus({ preventScroll: true });
    window._routed = true;
  }
  jump.addEventListener('change', function () { location.hash = '#' + jump.value; });
  window.addEventListener('hashchange', route);
  document.addEventListener('keydown', function (e) {
    if (e.target.closest('input, textarea, select, [contenteditable]') || e.metaKey || e.ctrlKey || e.altKey) return;
    if (e.key !== '[' && e.key !== ']') return;
    var p = $('.page.on'), a = $(e.key === '[' ? '.pager-nav .prev' : '.pager-nav .next', p);
    if (a) location.hash = a.getAttribute('href');
  });

  /* ---------- Copy: tick on the click ---------- */
  function copyText(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) return navigator.clipboard.writeText(text);
    return new Promise(function (res, rej) {
      var ta = document.createElement('textarea'); ta.value = text; ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta); ta.select();
      try { document.execCommand('copy') ? res() : rej(); } catch (e) { rej(e); } finally { ta.remove(); }
    });
  }
  function flash(el, text) {
    var use = el.querySelector('use'), label = el.querySelector(':scope > span:not(.dot):not(.kbd)');
    var oldIcon = use ? use.getAttribute('href') : null, oldLabel = label ? label.textContent : null;
    if (el._busy) { clearTimeout(el._t); } else { el._oi = oldIcon; el._ol = oldLabel; }
    el._busy = true;
    if (use) use.setAttribute('href', '#i-check');
    el.classList.add('done');
    copyText(text).catch(function () { if (use) use.setAttribute('href', el._oi); if (label) label.textContent = 'Copy failed'; });
    el._t = setTimeout(function () {
      if (use) use.setAttribute('href', el._oi);
      if (label && el._ol !== null) label.textContent = el._ol;
      el.classList.remove('done'); el._busy = false;
    }, el.classList.contains('rounded-full') ? 1500 : 1000);
  }
  document.addEventListener('click', function (e) {
    var el = e.target.closest('[data-copy], [data-copy-target]'); if (!el) return;
    flash(el, el.dataset.copy || document.getElementById(el.dataset.copyTarget).textContent);
  });

  /* ---------- Foundations fillers ---------- */
  var L = ['#FBFBFA','#F5F5F4','#EDEDEC','#E5E5E4','#DEDEDD','#D6D6D5','#CACAC9','#B5B5B4','#8A8A89','#737372','#5C5C5B','#111111'];
  var D = ['#111111','#191919','#232323','#2B2B2B','#333333','#3D3D3D','#4A4A4A','#626262','#737373','#868686','#B4B4B4','#EEEEEE'];
  function fillScale(id, list) {
    var host = document.getElementById(id); if (!host) return;
    list.forEach(function (hex, i) {
      var d = document.createElement('div'); d.className = 'st';
      d.innerHTML = '<button class="c" style="background:' + hex + '" data-copy="' + hex + '" aria-label="Copy ink-' + (i + 1) + ', ' + hex + '"></button><span class="n">' + (i + 1) + '</span><span class="h">' + hex.slice(1) + '</span>';
      host.appendChild(d);
    });
  }
  fillScale('scale-light', L); fillScale('scale-dark', D);
  var ladder = $('#ladder');
  if (ladder) [2, 4, 6, 8, 12, 16, 20, 24, 32, 48, 64].forEach(function (v) {
    var s = document.createElement('div'); s.className = 's';
    s.innerHTML = '<div class="sq" style="width:' + v + 'px;height:' + v + 'px"></div><span class="meta">' + v + '</span>'; ladder.appendChild(s);
  });
  var heights = $('#heights');
  if (heights) [[44, 'phone field'], [40, 'lg'], [36, 'default'], [32, 'sm'], [28, 'toggle'], [24, 'xs'], [20, 'badge'], [18, 'key']].forEach(function (h) {
    var s = document.createElement('div'); s.className = 'h';
    s.innerHTML = '<div class="bx" style="height:' + h[0] + 'px"></div><span class="meta">' + h[0] + ' ' + h[1] + '</span>'; heights.appendChild(s);
  });
  var track = $('#track');
  if (track) $('#play-btn').addEventListener('click', function () {
    track.style.setProperty('--travel', (track.clientWidth - 40) + 'px');
    if (reduce.matches) { var p = $('.puck', track); p.style.opacity = 0; setTimeout(function () { track.classList.toggle('go'); p.style.opacity = 1; }, 160); }
    else track.classList.toggle('go');
  });
  var dl = $('#dl-btn');
  if (dl) dl.addEventListener('click', function () {
    var blob = new Blob([$('#tokens-code').textContent], { type: 'text/css' });
    var a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = 'enterlabs-ui-tokens.css';
    document.body.appendChild(a); a.click(); setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 0);
  });

  /* ---------- Buttons: spinner + disabled while busy ---------- */
  $$('[data-busy-label]').forEach(function (b) {
    var html = b.innerHTML;
    b.addEventListener('click', function () {
      var w = b.offsetWidth; b.style.minWidth = w + 'px';
      b.disabled = true; b.setAttribute('aria-busy', 'true');
      b.innerHTML = '<span class="spinner" aria-hidden="true"></span>' + b.dataset.busyLabel;
      setTimeout(function () { b.innerHTML = html; b.disabled = false; b.removeAttribute('aria-busy'); b.style.minWidth = ''; b.focus(); }, 1600);
    });
  });

  /* ---------- Switches ---------- */
  document.addEventListener('click', function (e) {
    var s = e.target.closest('.switch'); if (!s || s.disabled) return;
    s.setAttribute('aria-checked', s.getAttribute('aria-checked') === 'true' ? 'false' : 'true');
  });

  /* ---------- Menus ---------- */
  var openMenu = null;
  function closeMenu(focus) {
    if (!openMenu) return;
    openMenu.m.classList.remove('open'); openMenu.t.setAttribute('aria-expanded', 'false');
    if (focus) openMenu.t.focus({ preventScroll: true });
    openMenu = null;
  }
  $$('[data-menu]').forEach(function (t) {
    var m = document.getElementById(t.dataset.menu);
    t.addEventListener('click', function (e) {
      e.stopPropagation();
      if (openMenu && openMenu.m === m) return closeMenu();
      closeMenu(); closePop();
      m.classList.add('open'); t.setAttribute('aria-expanded', 'true'); openMenu = { m: m, t: t };
      var c = m.querySelector('[aria-checked="true"]') || m.querySelector('button');
      if (c) c.focus({ preventScroll: true });
    });
    m.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b) return;
      if (b.hasAttribute('aria-checked')) {
        $$('[aria-checked]', m).forEach(function (x) { x.setAttribute('aria-checked', x === b ? 'true' : 'false'); });
        var lab = t.querySelector('[data-label]'); if (lab) { lab.textContent = b.textContent; lab.classList.remove('ph'); }
        t.removeAttribute('aria-invalid');
        var err = t.closest('.field') && t.closest('.field').querySelector('.err'); if (err) err.remove();
      }
      closeMenu(true);
    });
    m.addEventListener('keydown', function (e) {
      var items = $$('button', m), i = items.indexOf(document.activeElement);
      if (e.key === 'ArrowDown') { e.preventDefault(); items[(i + 1) % items.length].focus(); }
      if (e.key === 'ArrowUp') { e.preventDefault(); items[(i - 1 + items.length) % items.length].focus(); }
      if (e.key === 'Tab') closeMenu();
    });
  });

  /* ---------- Popovers ---------- */
  var openPop = null;
  function closePop(focus) { if (!openPop) return; openPop.p.classList.remove('open'); openPop.t.setAttribute('aria-expanded', 'false'); if (focus) openPop.t.focus(); openPop = null; }
  $$('[data-pop]').forEach(function (t) {
    var p = document.getElementById(t.dataset.pop);
    t.addEventListener('click', function (e) {
      e.stopPropagation();
      if (openPop && openPop.p === p) return closePop();
      closePop(); closeMenu();
      p.classList.add('open'); t.setAttribute('aria-expanded', 'true'); openPop = { p: p, t: t };
      var f = p.querySelector('input'); if (f) setTimeout(function () { f.focus(); }, 30);
    });
    p.addEventListener('click', function (e) { e.stopPropagation(); });
  });
  document.addEventListener('click', function (e) {
    if (openMenu && !openMenu.m.contains(e.target)) closeMenu();
    if (openPop && !openPop.p.contains(e.target)) closePop();
  });

  /* ---------- Modals and side panels ---------- */
  var scrim = $('#scrim'), openOv = null;
  function openOverlay(id, trigger) {
    var el = document.getElementById(id); if (!el) return;
    closeMenu(); closePop();
    var isPanel = el.classList.contains('side-panel');
    var phone = matchMedia('(width < 48rem)').matches;
    if (el._reset) el._reset();
    $$('input, textarea, select', el).forEach(function (f) { f._init = f.value; });
    el.classList.add('open'); if (!isPanel || phone) scrim.classList.add('open');
    if (!isPanel || phone) document.body.style.overflow = 'hidden';
    openOv = { el: el, t: trigger };
    setTimeout(function () {
      if (el.getAttribute('role') === 'alertdialog') { el.setAttribute('tabindex', '-1'); el.focus({ preventScroll: true }); return; }
      var f = el.querySelector('.dialog-body input, .dialog-body textarea') || el.querySelector('.dialog-foot:not([hidden]) .btn:last-child') || el.querySelector('.x-close');
      if (f) f.focus({ preventScroll: true });
    }, 60);
  }
  function closeOverlay() {
    if (!openOv) return;
    openOv.el.classList.remove('open'); scrim.classList.remove('open'); document.body.style.overflow = '';
    if (openOv.t) openOv.t.focus({ preventScroll: true });
    openOv = null;
  }
  $$('[data-open]').forEach(function (t) { t.addEventListener('click', function () { openOverlay(t.dataset.open, t); }); });
  document.addEventListener('click', function (e) {
    var c = e.target.closest('[data-close]'); if (!c) return;
    var msg = c.dataset.toastAfter, tone = c.dataset.tone || 'green'; closeOverlay(); if (msg) setTimeout(function () { toast(msg, tone); }, 220);
  });
  function isDirty(el) { return $$('input, textarea, select', el).some(function (f) { return f.value !== f._init; }); }
  scrim.addEventListener('click', function () {
    if (openOv && openOv.el.hasAttribute('data-guard') && isDirty(openOv.el)) return;
    closeOverlay();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      if (openMenu) return closeMenu(true);
      if (openPop) return closePop(true);
      if (openOv) return closeOverlay();
      $$('.cal.open').forEach(function (c) { c.classList.remove('open'); });
    }
    if (e.key === 'Tab' && openOv && !openOv.el.classList.contains('side-panel')) {
      var f = $$('button:not([disabled]), input, textarea, select, a[href]', openOv.el).filter(function (x) { return x.offsetParent !== null; });
      if (!f.length) return;
      if (e.shiftKey && document.activeElement === f[0]) { e.preventDefault(); f[f.length - 1].focus(); }
      else if (!e.shiftKey && document.activeElement === f[f.length - 1]) { e.preventDefault(); f[0].focus(); }
    }
  });
  function closeAll(keepFeedback) { closeMenu(); closePop(); if (!(keepFeedback && openOv && openOv.el.id === 'fb-panel')) closeOverlay(); closeSheet(); }

  /* ---------- Modal demos ---------- */
  $$('[data-requires]').forEach(function (b) {
    var f = document.getElementById(b.dataset.requires);
    var sync = function () { if (!b.getAttribute('aria-busy')) b.disabled = !f.value.trim(); };
    f.addEventListener('input', sync); b._sync = sync;
  });
  var mForm = $('#md-form');
  if (mForm) {
    var mfName = $('#mf-name'), mfMsg = $('#mf-name-m'), mfBtn = $('#mf-submit'), mfBase = mfMsg.textContent;
    var taken = ['claims portal', 'fraud model v3', 'brand site'];
    mForm._reset = function () {
      $$('input, textarea', mForm).forEach(function (f) { f.value = ''; });
      mfName.removeAttribute('aria-invalid'); mfMsg.className = 'hint'; mfMsg.textContent = mfBase; mfMsg.removeAttribute('role');
      mfBtn.disabled = true; mfBtn.removeAttribute('aria-busy');
      $('.label-swap', mfBtn).innerHTML = '<span>Create project</span>';
    };
    var submit = function () {
      if (mfBtn.disabled) return;
      if (taken.indexOf(mfName.value.trim().toLowerCase()) > -1) {
        mfName.setAttribute('aria-invalid', 'true'); mfMsg.className = 'err'; mfMsg.setAttribute('role', 'alert');
        mfMsg.textContent = 'That name already exists. Pick another name.'; mfName.focus(); return;
      }
      mfName.removeAttribute('aria-invalid'); mfMsg.className = 'hint'; mfMsg.textContent = mfBase;
      var box = $('.label-swap', mfBtn), old = box.firstElementChild, nw = document.createElement('span');
      nw.className = 'in-wait'; nw.innerHTML = '<span class="spinner" aria-hidden="true"></span>Creating…';
      box.appendChild(nw); mfBtn.setAttribute('aria-busy', 'true');
      requestAnimationFrame(function () { old.classList.add('out'); nw.classList.remove('in-wait'); });
      setTimeout(function () { closeOverlay(); setTimeout(function () { toast('Project created', 'green', 'View'); }, 220); }, 1200);
    };
    mfBtn.addEventListener('click', submit);
    mfName.addEventListener('keydown', function (e) { if (e.key === 'Enter') { e.preventDefault(); submit(); } });
    mfName.addEventListener('input', function () { if (mfName.getAttribute('aria-invalid')) { mfName.removeAttribute('aria-invalid'); mfMsg.className = 'hint'; mfMsg.textContent = mfBase; } });
  }
  var mSteps = $('#md-steps');
  if (mSteps) {
    var show = function (k) {
      $$('.mstep', mSteps).forEach(function (x) {
        var on = x.dataset.s === k, was = !x.hidden; x.hidden = !on;
        if (on && !was) { x.classList.add('pre'); x.offsetWidth; requestAnimationFrame(function () { x.classList.remove('pre'); }); }
      });
      $$('.dialog-foot', mSteps).forEach(function (x) { x.hidden = x.dataset.f !== (k === 'busy' ? 'form' : k); });
    };
    mSteps._reset = function () { var bd = $('.mbody-hold', mSteps); bd.style.minHeight = ''; show('form'); $('#ms-send').disabled = false; bd.style.minHeight = bd.offsetHeight + 'px'; };
    $('#ms-send').addEventListener('click', function () {
      var list = $('#ms-emails').value.split(/\n+/).map(function (x) { return x.trim(); }).filter(Boolean);
      var msg = $('#ms-emails-m');
      if (!list.length || list.some(function (x) { return !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(x); })) {
        $('#ms-emails').setAttribute('aria-invalid', 'true'); msg.className = 'err'; msg.textContent = 'Check the addresses: one valid email per line.'; $('#ms-emails').focus(); return;
      }
      $('#ms-emails').removeAttribute('aria-invalid'); msg.className = 'hint'; msg.textContent = 'Up to 20 at a time.';
      $('#ms-send').disabled = true; show('busy'); $('[data-s="busy"]', mSteps).focus();
      setTimeout(function () {
        $('#ms-done-t').textContent = list.length + (list.length === 1 ? ' invite sent' : ' invites sent');
        show('done'); $('[data-s="done"]', mSteps).focus();
      }, 1400);
    });
  }

  /* ---------- Toasts ---------- */
  var toastEl = $('#toast'), tt;
  function toast(text, tone, action) {
    clearTimeout(tt);
    var show = function () {
      toastEl.className = 'toast hue-' + (tone || 'green') + (action ? ' has-action' : '');
      toastEl.setAttribute('role', tone === 'red' ? 'alert' : 'status');
      toastEl.innerHTML = '<span class="tt"></span>' + (action ? '<button class="act"></button>' : '');
      toastEl.querySelector('.tt').textContent = text;
      if (action) { var a = toastEl.querySelector('.act'); a.textContent = action; a.onclick = function () { toastEl.classList.remove('show'); }; }
      requestAnimationFrame(function () { toastEl.classList.add('show'); });
      tt = setTimeout(function () { toastEl.classList.remove('show'); }, 6000);
    };
    if (toastEl.classList.contains('show')) { toastEl.classList.remove('show'); setTimeout(show, 160); } else show();
  }
  window.elToast = toast;
  toastEl.addEventListener('mouseenter', function () { clearTimeout(tt); });
  toastEl.addEventListener('mouseleave', function () { tt = setTimeout(function () { toastEl.classList.remove('show'); }, 2000); });
  $$('[data-toast]').forEach(function (b) { b.addEventListener('click', function () { toast(b.dataset.toast, b.dataset.tone, b.dataset.action); }); });

  /* ---------- Accordion ---------- */
  $$('.acc-btn').forEach(function (b) { b.addEventListener('click', function () { b.setAttribute('aria-expanded', b.getAttribute('aria-expanded') === 'true' ? 'false' : 'true'); }); });

  /* ---------- Fields ---------- */
  $$('[data-validate="email"]').forEach(function (f) {
    var msg = document.getElementById(f.getAttribute('aria-describedby')), base = msg.textContent;
    f.addEventListener('blur', function () {
      var bad = f.value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(f.value);
      f.setAttribute('aria-invalid', bad ? 'true' : 'false');
      msg.className = bad ? 'err' : 'hint'; msg.setAttribute('role', bad ? 'alert' : '');
      msg.textContent = bad ? 'Enter a full address, like name@enterlabs.id' : base;
    });
  });
  $$('[data-counter]').forEach(function (t) {
    var c = document.getElementById(t.dataset.counter), max = t.getAttribute('maxlength');
    t.addEventListener('input', function () { c.textContent = t.value.length + ' / ' + max; });
  });
  var all = $('#cb-all');
  if (all) {
    var items = $$('.cb-item');
    var sync = function () { var n = items.filter(function (i) { return i.checked; }).length; all.checked = n === items.length; all.indeterminate = n > 0 && n < items.length; };
    all.addEventListener('change', function () { items.forEach(function (i) { i.checked = all.checked; }); sync(); });
    items.forEach(function (i) { i.addEventListener('change', sync); }); sync();
  }

  /* ---------- Search ---------- */
  var sIn = $('#srch'), sOut = $('#srch-r');
  if (sIn) {
    var data = [['Claims portal', 'EL-00481'], ['Fraud model v3', 'EL-00477'], ['Brand site', 'EL-00462'], ['Partner API', 'EL-00455'], ['Claims audit 2026', 'EL-00431'], ['Hospital network sync', 'EL-00420']];
    var hi = 0, res = [];
    var esc = function (s) { return s.replace(/[&<>]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]; }); };
    var render = function () {
      var q = sIn.value.trim().toLowerCase();
      if (!q) { sOut.classList.remove('open'); sIn.setAttribute('aria-expanded', 'false'); return; }
      res = data.filter(function (d) { return d[0].toLowerCase().indexOf(q) > -1 || d[1].toLowerCase().indexOf(q) > -1; });
      hi = Math.min(hi, Math.max(res.length - 1, 0));
      sOut.innerHTML = res.length ? res.map(function (d, i) {
        var n = d[0], k = n.toLowerCase().indexOf(q);
        var lab = k > -1 ? esc(n.slice(0, k)) + '<mark>' + esc(n.slice(k, k + q.length)) + '</mark>' + esc(n.slice(k + q.length)) : esc(n);
        return '<div class="r' + (i === hi ? ' hi' : '') + '" role="option" id="sr-' + i + '" aria-selected="' + (i === hi) + '"><span>' + lab + '</span><span class="m mono">' + d[1] + '</span></div>';
      }).join('') : '<p class="none">No projects match "' + esc(sIn.value.trim()) + '"</p>';
      sOut.classList.add('open'); sIn.setAttribute('aria-expanded', 'true');
      if (res.length) sIn.setAttribute('aria-activedescendant', 'sr-' + hi);
    };
    sIn.addEventListener('input', function () { hi = 0; render(); });
    sIn.addEventListener('keydown', function (e) {
      if (!res.length) return;
      if (e.key === 'ArrowDown') { e.preventDefault(); hi = (hi + 1) % res.length; render(); }
      if (e.key === 'ArrowUp') { e.preventDefault(); hi = (hi - 1 + res.length) % res.length; render(); }
      if (e.key === 'Enter') { sIn.value = res[hi][0]; sOut.classList.remove('open'); }
      if (e.key === 'Escape') { sOut.classList.remove('open'); }
    });
    sOut.addEventListener('mousedown', function (e) { var r = e.target.closest('.r'); if (r) { e.preventDefault(); sIn.value = res[+r.id.slice(3)][0]; sOut.classList.remove('open'); } });
    sIn.addEventListener('blur', function () { setTimeout(function () { sOut.classList.remove('open'); }, 100); });
  }
  document.addEventListener('keydown', function (e) {
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
      var p = $('.page.on'), f = p && p.querySelector('#srch'); if (f) { e.preventDefault(); f.focus(); }
    }
  });

  /* ---------- Slider ---------- */
  var idr = new Intl.NumberFormat('id-ID');
  $$('.range').forEach(function (r) {
    var set = function () {
      var p = (r.value - r.min) / (r.max - r.min) * 100; r.style.setProperty('--p', p + '%');
      if (r.dataset.out) { var o = document.getElementById(r.dataset.out); o.textContent = r.dataset.fmt === 'idr' ? 'Rp ' + idr.format(+r.value) : r.value; r.setAttribute('aria-valuetext', o.textContent); }
    };
    r.addEventListener('input', set); set();
  });

  /* ---------- Date picker ---------- */
  var MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
  function buildCal(host, opts) {
    var today = new Date(); today.setHours(0, 0, 0, 0);
    var view = new Date((opts.selected || today).getFullYear(), (opts.selected || today).getMonth(), 1);
    var sel = opts.selected || null;
    function draw() {
      var y = view.getFullYear(), m = view.getMonth();
      var start = new Date(y, m, 1 - ((new Date(y, m, 1).getDay() + 6) % 7));
      var h = '<div class="cal-head"><button class="btn btn-ghost btn-icon-sm" data-nav="-1" aria-label="Previous month"><svg><use href="#i-chev-l"/></svg></button><span class="m">' + MONTHS[m] + ' ' + y + '</span><button class="btn btn-ghost btn-icon-sm" data-nav="1" aria-label="Next month"><svg><use href="#i-chev-r"/></svg></button></div><div class="cal-grid" role="grid">';
      ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su'].forEach(function (d) { h += '<span class="wd">' + d + '</span>'; });
      for (var i = 0; i < 42; i++) {
        var d = new Date(start); d.setDate(start.getDate() + i);
        var cls = (d.getMonth() !== m ? 'out ' : '') + (+d === +today ? 'today' : '');
        var dis = opts.noFuture && d > today;
        h += '<button class="' + cls + '" data-d="' + d.getTime() + '" aria-label="' + d.getDate() + ' ' + MONTHS[d.getMonth()] + ' ' + d.getFullYear() + '"' + (sel && +d === +sel ? ' aria-selected="true"' : '') + (dis ? ' disabled' : '') + ' tabindex="-1">' + d.getDate() + '</button>';
      }
      host.innerHTML = h + '</div>';
      var focusBtn = host.querySelector('[aria-selected="true"]') || host.querySelector('.today') || host.querySelector('.cal-grid button:not(.out)');
      if (focusBtn) focusBtn.tabIndex = 0;
    }
    host.addEventListener('click', function (e) {
      e.stopPropagation();
      var n = e.target.closest('[data-nav]'); if (n) { view.setMonth(view.getMonth() + +n.dataset.nav); draw(); return; }
      var b = e.target.closest('[data-d]'); if (!b || b.disabled) return;
      sel = new Date(+b.dataset.d); draw(); if (opts.onPick) opts.onPick(sel);
    });
    host.addEventListener('keydown', function (e) {
      var b = e.target.closest('[data-d]'); if (!b) return;
      var step = { ArrowLeft: -1, ArrowRight: 1, ArrowUp: -7, ArrowDown: 7 }[e.key];
      if (!step) return; e.preventDefault();
      var nd = new Date(+b.dataset.d); nd.setDate(nd.getDate() + step);
      if (nd.getMonth() !== view.getMonth()) { view = new Date(nd.getFullYear(), nd.getMonth(), 1); draw(); }
      var t = host.querySelector('[data-d="' + nd.getTime() + '"]'); if (t) t.focus();
    });
    draw();
    return { draw: draw };
  }
  var calStatic = $('[data-cal-static]');
  if (calStatic) { var t0 = new Date(); t0.setHours(0, 0, 0, 0); t0.setDate(t0.getDate() - 5); buildCal(calStatic, { selected: t0, noFuture: true }); }
  $$('[data-datepicker]').forEach(function (inp) {
    var cal = document.getElementById(inp.dataset.datepicker);
    buildCal(cal, { noFuture: true, onPick: function (d) {
      inp.value = String(d.getDate()).padStart(2, '0') + '/' + String(d.getMonth() + 1).padStart(2, '0') + '/' + d.getFullYear();
      cal.classList.remove('open'); inp.focus();
    } });
    inp.addEventListener('click', function (e) { e.stopPropagation(); cal.classList.add('open'); });
    inp.addEventListener('keydown', function (e) { if (e.key === 'ArrowDown') { e.preventDefault(); cal.classList.add('open'); var f = cal.querySelector('.cal-grid button[tabindex="0"]'); if (f) f.focus(); } });
    document.addEventListener('click', function (e) { if (!cal.contains(e.target) && e.target !== inp) cal.classList.remove('open'); });
  });

  /* ---------- File upload ---------- */
  var drop = $('#drop'), dIn = $('#drop-in'), files = $('#files');
  if (drop) {
    var fileIcon = '<span class="fi"><svg><use href="#i-file"/></svg></span>';
    var addFile = function (name, size) {
      var row = document.createElement('div'); row.className = 'file';
      row.innerHTML = fileIcon + '<div style="min-width:0"><p class="nm"></p><p class="mt">0%</p><div class="bar"><i style="width:0%"></i></div></div><button class="btn btn-ghost btn-icon-sm" aria-label="Remove file" data-remove><svg><use href="#i-x"/></svg></button>';
      row.querySelector('.nm').textContent = name; files.prepend(row);
      var p = 0, bar = row.querySelector('.bar i'), mt = row.querySelector('.mt');
      var iv = setInterval(function () {
        p = Math.min(100, p + 8 + Math.random() * 18); bar.style.width = p + '%'; mt.textContent = Math.round(p) + '%';
        if (p >= 100) { clearInterval(iv); mt.textContent = size + ' · Uploaded'; row.querySelector('.bar').remove(); }
      }, 160);
    };
    var fmt = function (b) { return b > 1048576 ? (b / 1048576).toFixed(1) + ' MB' : Math.max(1, Math.round(b / 1024)) + ' KB'; };
    var take = function (list) { Array.prototype.forEach.call(list, function (f) { addFile(f.name, fmt(f.size)); }); };
    drop.addEventListener('click', function () { dIn.click(); });
    drop.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); dIn.click(); } });
    dIn.addEventListener('change', function () { take(dIn.files); dIn.value = ''; });
    ['dragenter', 'dragover'].forEach(function (ev) { drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.add('over'); }); });
    ['dragleave', 'drop'].forEach(function (ev) { drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.remove('over'); }); });
    drop.addEventListener('drop', function (e) { if (e.dataTransfer && e.dataTransfer.files.length) take(e.dataTransfer.files); else addFile('claim-form-scan.pdf', '840 KB'); });
    files.addEventListener('click', function (e) { var r = e.target.closest('[data-remove]'); if (r) r.closest('.file').remove(); });
  }

  /* ---------- Filter pills ---------- */
  var fp = $('#fpills');
  if (fp) {
    fp.addEventListener('click', function (e) {
      var x = e.target.closest('.x'); if (!x) return;
      var pill = x.closest('.fpill'), next = pill.nextElementSibling; pill.remove();
      if (next) (next.querySelector('.x') || next).focus();
    });
    $('#fpill-add').addEventListener('click', function () {
      var s = document.createElement('span'); s.className = 'fpill';
      s.innerHTML = '<span class="k">Amount</span><span class="v">Over Rp 10 jt</span><button class="x" aria-label="Clear amount filter"><svg><use href="#i-x"/></svg></button>';
      fp.insertBefore(s, $('#fpill-add'));
    });
  }

  /* ---------- Table selection and sort ---------- */
  var ts = $('#tbl-sel');
  if (ts) {
    var head = $('thead input', ts), out = $('#tsel');
    var rowsC = function () { return $$('tbody input:not(:disabled)', ts); };
    var upd = function () {
      var rows = rowsC(), n = 0;
      rows.forEach(function (c) { c.closest('tr').setAttribute('aria-selected', c.checked ? 'true' : 'false'); if (c.checked) n++; });
      head.checked = n > 0 && n === rows.length; head.indeterminate = n > 0 && n < rows.length;
      out.textContent = n + ' selected';
      $$('.tbl-acts').forEach(function (g) { g.hidden = (g.dataset.when === 'some') !== (n > 0); });
    };
    head.addEventListener('change', function () { rowsC().forEach(function (c) { c.checked = head.checked; }); upd(); });
    ts.addEventListener('change', function (e) { if (e.target !== head) upd(); });
    $('#tclear').addEventListener('click', function () { rowsC().forEach(function (c) { c.checked = false; }); upd(); head.focus(); });
    var sortBtn = $('.th-sort', ts);
    sortBtn.addEventListener('click', function () {
      var th = sortBtn.closest('th'), dir = th.getAttribute('aria-sort') === 'descending' ? 'ascending' : 'descending';
      th.setAttribute('aria-sort', dir);
      var tb = $('tbody', ts), trs = $$('tr', tb);
      trs.sort(function (a, b) {
        if (a.classList.contains('inactive') !== b.classList.contains('inactive')) return a.classList.contains('inactive') ? 1 : -1;
        return (dir === 'ascending' ? 1 : -1) * (+a.dataset.amount - +b.dataset.amount);
      }).forEach(function (tr) { tb.appendChild(tr); });
    });
  }

  /* ---------- Pagination ---------- */
  var pg = $('#pgr');
  if (pg) {
    var page = 0, total = 48, per = 10, last = Math.ceil(total / per) - 1;
    pg.addEventListener('click', function (e) {
      var b = e.target.closest('[data-pg]'); if (!b) return;
      page = Math.max(0, Math.min(last, page + +b.dataset.pg));
      $('.count', pg).textContent = 'Showing ' + (page * per + 1) + ' to ' + Math.min(total, (page + 1) * per) + ' of ' + total;
      $('[data-pg="-1"]', pg).disabled = page === 0; $('[data-pg="1"]', pg).disabled = page === last;
    });
  }

  /* ---------- Progress ---------- */
  var plb = $('#pl-btn');
  if (plb) plb.addEventListener('click', function () {
    var v = 0, bar = $('#pl'), lab = $('#pl-v'); plb.disabled = true;
    var iv = setInterval(function () { v = Math.min(100, v + 10); bar.style.width = v + '%'; lab.textContent = v + '%'; bar.parentNode.setAttribute('aria-valuenow', v); if (v >= 100) { clearInterval(iv); plb.disabled = false; } }, 250);
  });

  /* ---------- Navigation demos ---------- */
  $$('.mini-rail a').forEach(function (a) {
    a.addEventListener('click', function () {
      $$('.mini-rail a').forEach(function (x) { x.setAttribute('aria-current', x === a ? 'true' : 'false'); });
      var name = a.childNodes[1] ? a.childNodes[1].textContent : a.textContent;
      var t = $('#mini-title'); if (t) t.textContent = name;
      var c = $('.mini-strip [aria-current]'); if (c) c.textContent = name;
    });
  });
  var burger = $('#burger');
  if (burger) burger.addEventListener('click', function () { burger.setAttribute('aria-expanded', burger.getAttribute('aria-expanded') === 'true' ? 'false' : 'true'); });
  var stp = $('#stp');
  if (stp) stp.addEventListener('click', function (e) {
    var b = e.target.closest('[data-step-next]'); if (!b) return;
    var steps = $$('.step', stp), cur = b.closest('.step'), i = steps.indexOf(cur);
    cur.classList.add('done'); $('.marker', cur).innerHTML = '<svg><use href="#i-check"/></svg>'; b.remove();
    var nx = steps[i + 1];
    if (nx) { nx.classList.remove('wait'); var btn = document.createElement('button'); btn.className = 'btn btn-default btn-sm'; btn.dataset.stepNext = ''; btn.textContent = i + 1 === steps.length - 1 ? 'Finish' : 'Continue'; $('.txt', nx).appendChild(btn); btn.focus(); }
  });

  /* ---------- Bottom sheet demo ---------- */
  var sheet = $('#pf-sheet'), pfScrim = $('#pf-scrim');
  function openSheet() { if (!sheet) return; sheet.classList.add('open'); pfScrim.classList.add('open'); setTimeout(function () { $('#pf-grab').focus({ preventScroll: true }); }, 50); }
  function closeSheet() { if (!sheet || !sheet.classList.contains('open')) return; sheet.style.transform = ''; sheet.classList.remove('open'); pfScrim.classList.remove('open'); }
  if (sheet) {
    $('#pf-open').addEventListener('click', openSheet);
    $('#pf-grab').addEventListener('click', closeSheet);
    pfScrim.addEventListener('click', closeSheet);
    var y0 = null, dy = 0, t0 = 0, drag = false;
    sheet.addEventListener('pointerdown', function (e) { if (e.target.closest('.btn')) return; y0 = e.clientY; t0 = e.timeStamp; dy = 0; drag = false; });
    window.addEventListener('pointermove', function (e) {
      if (y0 === null) return; dy = e.clientY - y0;
      if (!drag && Math.abs(dy) > 4) { drag = true; sheet.classList.add('dragging'); }
      if (drag) sheet.style.transform = 'translateY(' + Math.max(0, dy) + 'px)';
    });
    window.addEventListener('pointerup', function (e) {
      if (y0 === null) return;
      var v = dy / Math.max(1, e.timeStamp - t0); y0 = null;
      sheet.classList.remove('dragging'); sheet.style.transform = '';
      if (drag && (dy > Math.min(64, sheet.offsetHeight * .15) || v > .11)) closeSheet();
      drag = false;
    });
  }

  route();
})();
