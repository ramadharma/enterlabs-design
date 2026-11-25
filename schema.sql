-- Feedback comments on the docs. Run once:
--   npx wrangler d1 execute enterlabs-feedback --remote --file=schema.sql
CREATE TABLE IF NOT EXISTS comments (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  page        TEXT NOT NULL,              -- docs page id, e.g. "button"
  page_title  TEXT,
  author      TEXT NOT NULL,              -- name typed in, or the Cloudflare Access email
  body        TEXT NOT NULL,
  status      TEXT NOT NULL DEFAULT 'open' CHECK (status IN ('open', 'resolved')),
  created_at  TEXT NOT NULL DEFAULT (datetime('now')),
  resolved_at TEXT,
  resolved_by TEXT
);
CREATE INDEX IF NOT EXISTS idx_comments_page ON comments (page, status);
CREATE INDEX IF NOT EXISTS idx_comments_status ON comments (status, id);
