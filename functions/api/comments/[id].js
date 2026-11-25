// /api/comments/:id  (admins only)
//   PATCH { status: 'resolved' | 'open' }
//   DELETE
import { json, error, isAdmin, accessEmail } from '../../../lib/feedback.js';

function id(params) {
  const n = Number(params.id);
  return Number.isInteger(n) && n > 0 ? n : null;
}

export async function onRequestPatch({ request, env, params }) {
  if (!env.DB) return error(503, 'Feedback database is not connected.');
  if (!isAdmin(request, env)) return error(403, 'Only admins can change a comment.');
  const n = id(params); if (!n) return error(400, 'Unknown comment.');
  let data;
  try { data = await request.json(); } catch { return error(400, 'Send JSON.'); }
  if (!['resolved', 'open'].includes(data.status)) return error(400, 'Status is resolved or open.');
  const by = accessEmail(request) || 'admin';
  const stmt = data.status === 'resolved'
    ? env.DB.prepare("UPDATE comments SET status = 'resolved', resolved_at = datetime('now'), resolved_by = ? WHERE id = ? RETURNING *").bind(by, n)
    : env.DB.prepare("UPDATE comments SET status = 'open', resolved_at = NULL, resolved_by = NULL WHERE id = ? RETURNING *").bind(n);
  const row = await stmt.first();
  if (!row) return error(404, 'Unknown comment.');
  return json({ comment: row });
}

export async function onRequestDelete({ request, env, params }) {
  if (!env.DB) return error(503, 'Feedback database is not connected.');
  if (!isAdmin(request, env)) return error(403, 'Only admins can delete a comment.');
  const n = id(params); if (!n) return error(400, 'Unknown comment.');
  const r = await env.DB.prepare('DELETE FROM comments WHERE id = ?').bind(n).run();
  if (!r.meta.changes) return error(404, 'Unknown comment.');
  return json({ ok: true });
}
