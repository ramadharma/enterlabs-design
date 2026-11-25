// Shared helpers for the feedback API (Cloudflare Pages Functions + D1).
export const json = (data, status = 200, extra = {}) =>
  new Response(JSON.stringify(data), {
    status,
    headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store', ...extra },
  });

export const error = (status, message) => json({ error: message }, status);

// Who is writing. With Cloudflare Access in front of the site, the verified email wins.
export function accessEmail(request) {
  return (request.headers.get('cf-access-authenticated-user-email') || '').trim().toLowerCase();
}

// Admins resolve, reopen and delete. Either an email in ADMIN_EMAILS (needs Access)
// or the ADMIN_KEY secret sent as the X-Admin-Key header.
export function isAdmin(request, env) {
  const email = accessEmail(request);
  const admins = (env.ADMIN_EMAILS || '').split(',').map((s) => s.trim().toLowerCase()).filter(Boolean);
  if (email && admins.includes(email)) return true;
  const key = request.headers.get('x-admin-key') || '';
  return Boolean(env.ADMIN_KEY) && key.length > 0 && timingSafeEqual(key, env.ADMIN_KEY);
}

function timingSafeEqual(a, b) {
  if (a.length !== b.length) return false;
  let r = 0;
  for (let i = 0; i < a.length; i++) r |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return r === 0;
}

export const PAGE_RE = /^[a-z0-9-]{1,60}$/;
export const clean = (s, max) => String(s ?? '').replace(/\r\n?/g, '\n').trim().slice(0, max);

export function toMarkdown(rows, site) {
  if (!rows.length) return 'No feedback.\n';
  const byPage = {};
  for (const r of rows) (byPage[r.page] ||= []).push(r);
  let out = '';
  for (const [page, list] of Object.entries(byPage)) {
    out += `## ${list[0].page_title || page} (${site}/#${page})\n\n`;
    for (const r of list) {
      const body = r.body.replace(/\n/g, '\n  ');
      out += `- [${r.status}] #${r.id} ${r.author}, ${r.created_at} UTC: ${body}\n`;
    }
    out += '\n';
  }
  return out;
}
