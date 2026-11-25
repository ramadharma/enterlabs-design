/* ---------- Feedback: comments per docs page (Cloudflare Pages Functions + D1) ---------- */
(function () {
  var API = 'api/comments';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var panel = $('#fb-panel'), btn = $('#fb-open'); if (!panel || !btn) return;
  var form = $('#fb-form'), list = $('#fb-list'), err = $('#fb-err'), send = $('#fb-send');
  var nameF = $('#fb-name'), bodyF = $('#fb-body'), codeF = $('#fb-code'), codeWrap = $('#fb-code-f');
  var pageName = $('#fb-page'), countPill = $('#fb-n'), offline = $('#fb-offline'), heading = $('#fb-list-t');
  var store = {
    get: function (k) { try { return localStorage.getItem(k) || ''; } catch (e) { return ''; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  };
  nameF.value = store.get('el-fb-name'); codeF.value = store.get('el-fb-code');
  if (codeF.value) codeWrap.hidden = false;
  var counts = {}, online = location.protocol.indexOf('http') === 0;

  function current() {
    var p = document.querySelector('.page.on');
    return p ? { id: p.dataset.page, title: p.dataset.title } : { id: 'overview', title: 'Overview' };
  }
  function ago(s) {
    var d = new Date(String(s).replace(' ', 'T') + 'Z'), m = Math.round((Date.now() - d) / 60000);
    if (m < 1) return 'Just now';
    if (m < 60) return m + ' min ago';
    if (m < 1440) return Math.round(m / 60) + ' h ago';
    return d.toLocaleDateString(undefined, { day: 'numeric', month: 'short', year: d.getFullYear() === new Date().getFullYear() ? undefined : 'numeric' });
  }
  function initials(n) { return n.replace(/@.*/, '').split(/[\s._-]+/).filter(Boolean).slice(0, 2).map(function (w) { return w[0].toUpperCase(); }).join('') || '?'; }
  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }

  function showCount() {
    var n = counts[current().id] || 0;
    countPill.hidden = !n; countPill.textContent = n;
    btn.setAttribute('aria-label', 'Feedback' + (n ? ', ' + n + ' open on this page' : ''));
  }
  function setOffline(on) {
    offline.hidden = !on;
    Array.prototype.forEach.call(form.elements, function (f) { f.disabled = on; });
  }
  function loadCounts() {
    if (!online) return;
    fetch(API + '?counts=1').then(function (r) { return r.ok ? r.json() : Promise.reject(); })
      .then(function (d) { counts = d.counts || {}; showCount(); }).catch(function () {});
  }
  function render(items) {
    list.textContent = '';
    heading.textContent = items.length ? 'On this page (' + items.length + ')' : 'On this page';
    if (!items.length) {
      var e = el('div', 'empty');
      e.appendChild(el('p', null, 'No feedback on this page yet'));
      e.appendChild(el('p', null, 'Say what should change, and the owner sees it in the inbox.'));
      list.appendChild(e); return;
    }
    items.forEach(function (c) {
      var a = el('article', 'fb-item' + (c.status === 'resolved' ? ' resolved' : ''));
      var meta = el('div', 'fb-meta');
      meta.appendChild(el('span', 'avatar-i av-24', initials(c.author)));
      meta.appendChild(el('span', 'fb-author', c.author));
      meta.appendChild(el('span', 'meta', ago(c.created_at)));
      if (c.status === 'resolved') { var b = el('span', 'badge neutral', 'Resolved'); meta.appendChild(b); }
      a.appendChild(meta);
      a.appendChild(el('p', 'fb-body', c.body));
      list.appendChild(a);
    });
  }
  function load() {
    var p = current(); pageName.textContent = p.title;
    if (!online) { setOffline(true); render([]); return; }
    list.setAttribute('aria-busy', 'true');
    fetch(API + '?page=' + encodeURIComponent(p.id)).then(function (r) { return r.ok ? r.json() : Promise.reject(); })
      .then(function (d) { setOffline(false); render(d.comments || []); })
      .catch(function () { setOffline(true); render([]); })
      .then(function () { list.removeAttribute('aria-busy'); });
  }
  function fail(msg) { err.textContent = msg; err.hidden = false; bodyF.setAttribute('aria-invalid', 'true'); }

  btn.addEventListener('click', function () {
    load();
    setTimeout(function () { (nameF.value ? bodyF : nameF).focus({ preventScroll: true }); }, 80);
  });
  window.addEventListener('hashchange', function () { showCount(); if (panel.classList.contains('open')) load(); });
  bodyF.addEventListener('input', function () { err.hidden = true; bodyF.removeAttribute('aria-invalid'); });

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var p = current(), name = nameF.value.trim(), body = bodyF.value.trim();
    if (!name) { nameF.focus(); return fail('Add your name so the team knows who wrote it.'); }
    if (!body) { bodyF.focus(); return fail('Write a comment first.'); }
    var label = send.textContent; send.disabled = true; send.setAttribute('aria-busy', 'true');
    send.innerHTML = '<span class="spinner"></span>Posting…';
    fetch(API, {
      method: 'POST', headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ page: p.id, page_title: p.title, author: name, body: body, code: codeF.value.trim(), website: $('#fb-hp').value })
    }).then(function (r) { return r.json().then(function (d) { return { ok: r.ok, status: r.status, d: d }; }); })
      .then(function (res) {
        if (res.status === 401) { codeWrap.hidden = false; codeF.focus(); return fail(res.d.error || 'Enter the team code.'); }
        if (!res.ok) return fail(res.d.error || 'Couldn’t post. Try again.');
        store.set('el-fb-name', name); if (codeF.value) store.set('el-fb-code', codeF.value.trim());
        bodyF.value = ''; counts[p.id] = (counts[p.id] || 0) + 1; showCount(); load();
        if (window.elToast) window.elToast('Comment posted', 'green');
      })
      .catch(function () { fail('Couldn’t reach the server. Check your connection and try again.'); })
      .then(function () { send.disabled = false; send.removeAttribute('aria-busy'); send.textContent = label; });
  });

  loadCounts(); showCount();
})();
