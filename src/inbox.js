/* ---------- Feedback inbox ---------- */
(function () {
  var API = '../api/comments';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var root = document.documentElement, rows = $('#ib-rows'), state = $('#ib-state'), wrap = $('#ib-table');
  var keyCard = $('#ib-key'), keyF = $('#ib-key-f'), keyErr = $('#ib-key-err'), count = $('#ib-count');
  var status = 'open', admin = false, key = '';
  try { key = sessionStorage.getItem('el-fb-admin') || ''; } catch (e) {}

  /* segmented controls: theme and filter */
  function placeThumb(seg) {
    var on = $('[aria-pressed="true"]', seg), th = $('.thumb', seg); if (!on || !th) return;
    th.style.width = on.offsetWidth + 'px'; th.style.transform = 'translateX(' + on.offsetLeft + 'px)';
  }
  function seg(el, cb) {
    $$('button', el).forEach(function (b) {
      b.addEventListener('click', function () {
        $$('button', el).forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
        placeThumb(el); cb(b);
      });
    });
    el.classList.add('no-anim'); placeThumb(el); el.offsetWidth; el.classList.remove('no-anim');
  }
  var themeSeg = $('#theme-seg');
  $$('button', themeSeg).forEach(function (b) { b.setAttribute('aria-pressed', b.dataset.v === root.getAttribute('data-theme') ? 'true' : 'false'); });
  seg(themeSeg, function (b) { root.setAttribute('data-theme', b.dataset.v); try { localStorage.setItem('el-theme', b.dataset.v); } catch (e) {} });
  seg($('#ib-filter'), function (b) { status = b.dataset.v; load(); });
  window.addEventListener('resize', function () { $$('.seg').forEach(placeThumb); });

  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }
  function when(s) {
    var d = new Date(String(s).replace(' ', 'T') + 'Z');
    return d.toLocaleString(undefined, { day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit' });
  }
  function headers(extra) { var h = extra || {}; if (key) h['x-admin-key'] = key; return h; }
  function showState(kind) {
    state.textContent = ''; state.hidden = !kind; wrap.hidden = !!kind;
    if (!kind) return;
    var t = { empty: ['Nothing here', status === 'open' ? 'No open feedback. The docs are up to date.' : 'No feedback with this status yet.'],
              fail: ['Couldn’t load feedback', 'The feedback server didn’t answer.'] }[kind];
    state.appendChild(el('p', null, t[0])); state.appendChild(el('p', null, t[1]));
    if (kind === 'fail') { var b = el('button', 'btn btn-outline', 'Try again'); b.onclick = load; state.appendChild(b); }
  }
  function render(list) {
    rows.textContent = '';
    count.textContent = list.length === 1 ? '1 comment' : list.length + ' comments';
    if (!list.length) return showState('empty');
    showState(null);
    list.forEach(function (c) {
      var tr = el('tr');
      var tdP = el('td'); var a = el('a', 'link', c.page_title || c.page); a.href = '../#' + c.page; tdP.appendChild(a); tr.appendChild(tdP);
      var tdB = el('td', 'wrap ib-body', c.body); tr.appendChild(tdB);
      tr.appendChild(el('td', null, c.author));
      var tdW = el('td', null, when(c.created_at)); tr.appendChild(tdW);
      var tdS = el('td');
      var s = el('span', 'status ' + (c.status === 'open' ? 'amber' : 'neutral')); s.appendChild(el('span', 'dot')); s.appendChild(document.createTextNode(c.status === 'open' ? 'Open' : 'Resolved'));
      tdS.appendChild(s); tr.appendChild(tdS);
      var tdA = el('td', 'act');
      var btn = el('button', 'btn btn-outline btn-xs', c.status === 'open' ? 'Resolve' : 'Reopen');
      btn.type = 'button';
      btn.addEventListener('click', function () { change(c, btn); });
      tdA.appendChild(btn); tr.appendChild(tdA);
      rows.appendChild(tr);
    });
  }
  function load() {
    rows.textContent = ''; showState(null);
    for (var i = 0; i < 4; i++) { var tr = el('tr'); for (var j = 0; j < 6; j++) { var td = el('td'); td.appendChild(el('span', 'skel-bar')).style.width = [96, 240, 80, 90, 60, 56][j] + 'px'; tr.appendChild(td); } rows.appendChild(tr); }
    fetch(API + '?status=' + status, { headers: headers() }).then(function (r) { return r.ok ? r.json() : Promise.reject(); })
      .then(function (d) { render(d.comments || []); })
      .catch(function () { count.textContent = ''; showState('fail'); });
  }
  function change(c, btn) {
    if (!admin) { keyCard.hidden = false; keyF.focus(); return; }
    var next = c.status === 'open' ? 'resolved' : 'open';
    btn.disabled = true; btn.innerHTML = '<span class="spinner"></span>' + (next === 'resolved' ? 'Resolving…' : 'Reopening…');
    fetch(API + '/' + c.id, { method: 'PATCH', headers: headers({ 'content-type': 'application/json' }), body: JSON.stringify({ status: next }) })
      .then(function (r) { if (!r.ok) throw r; load(); })
      .catch(function () { btn.disabled = false; btn.textContent = 'Try again'; });
  }
  function checkAdmin() {
    return fetch('../api/admin', { headers: headers() }).then(function (r) { return r.ok ? r.json() : { admin: false }; })
      .then(function (d) { admin = !!d.admin; keyCard.hidden = admin; return admin; }).catch(function () { return false; });
  }
  $('#ib-key-form').addEventListener('submit', function (e) {
    e.preventDefault(); key = keyF.value.trim(); keyErr.hidden = true; keyF.removeAttribute('aria-invalid');
    checkAdmin().then(function (ok) {
      if (ok) { try { sessionStorage.setItem('el-fb-admin', key); } catch (e) {} keyF.value = ''; }
      else { key = ''; keyErr.hidden = false; keyF.setAttribute('aria-invalid', 'true'); keyF.focus(); }
    });
  });
  $('#ib-copy').addEventListener('click', function () {
    var b = this, label = b.querySelector('span');
    fetch(API + '?status=' + status + '&format=md', { headers: headers() }).then(function (r) { return r.ok ? r.text() : Promise.reject(); })
      .then(function (t) { return navigator.clipboard.writeText('# Enterlabs docs feedback (' + status + ')\n\n' + t); })
      .then(function () { label.textContent = 'Copied'; setTimeout(function () { label.textContent = 'Copy as Markdown'; }, 1600); })
      .catch(function () { label.textContent = 'Copy failed'; setTimeout(function () { label.textContent = 'Copy as Markdown'; }, 1600); });
  });
  checkAdmin().then(function () { if (!admin) keyCard.hidden = true; });
  load();
})();
