// /api/comments
//   GET  ?page=<id>                 comments on one docs page, newest first
//   GET  ?status=open|resolved|all  every comment (the Feedback inbox); add &format=md for Markdown
//   GET  ?counts=1                  open comments per page: { counts: { button: 2 } }
//   POST { page, page_title, author, body, code }
import { json, error, accessEmail, PAGE_RE, clean, toMarkdown } from '../../../lib/feedback.js';

export async function onRequestGet({ request, env }) {
  if (!env.DB) return error(503, 'Feedback database is not connected.');
  const url = new URL(request.url);
  const page = url.searchParams.get('page');

  if (url.searchParams.get('counts')) {
    const { results } = await env.DB.prepare(
      "SELECT page, COUNT(*) AS n FROM comments WHERE status = 'open' GROUP BY page"
    ).all();
    return json({ counts: Object.fromEntries(results.map((r) => [r.page, r.n])) });
  }

  if (page) {
    if (!PAGE_RE.test(page)) return error(400, 'Unknown page.');
    const { results } = await env.DB.prepare(
      'SELECT id, page, page_title, author, body, status, created_at, resolved_at, resolved_by FROM comments WHERE page = ? ORDER BY id DESC LIMIT 200'
    ).bind(page).all();
    return json({ comments: results });
  }

  const status = url.searchParams.get('status') || 'open';
  if (!['open', 'resolved', 'all'].includes(status)) return error(400, 'Status is open, resolved or all.');
  const where = status === 'all' ? '' : 'WHERE status = ?';
  const stmt = env.DB.prepare(
    `SELECT id, page, page_title, author, body, status, created_at, resolved_at, resolved_by FROM comments ${where} ORDER BY id DESC LIMIT 500`
  );
  const { results } = await (status === 'all' ? stmt : stmt.bind(status)).all();
  if (url.searchParams.get('format') === 'md') {
    return new Response(toMarkdown(results, url.origin), {
      headers: { 'content-type': 'text/markdown; charset=utf-8', 'cache-control': 'no-store' },
    });
  }
  return json({ comments: results });
}

export async function onRequestPost({ request, env }) {
  if (!env.DB) return error(503, 'Feedback database is not connected.');
  let data;
  try { data = await request.json(); } catch { return error(400, 'Send JSON.'); }

  if (env.TEAM_CODE && clean(data.code, 100) !== env.TEAM_CODE) return error(401, 'Enter the team code to comment.');

  const page = clean(data.page, 60);
  const pageTitle = clean(data.page_title, 120);
  const body = clean(data.body, 2000);
  const author = accessEmail(request) || clean(data.author, 80);
  if (!PAGE_RE.test(page)) return error(400, 'Unknown page.');
  if (!author) return error(400, 'Add your name.');
  if (!body) return error(400, 'Write a comment first.');
  if (data.website) return json({ ok: true }); // honeypot: bots fill every field

  const row = await env.DB.prepare(
    'INSERT INTO comments (page, page_title, author, body) VALUES (?, ?, ?, ?) RETURNING id, page, page_title, author, body, status, created_at, resolved_at, resolved_by'
  ).bind(page, pageTitle, author, body).first();
  return json({ comment: row }, 201);
}
