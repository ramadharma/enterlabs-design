# Enterlabs design system

The Enterlabs design system: browsable docs, a machine-readable spec that the `enterlabs-design` Claude skill reads on every run, and team feedback on every docs page.

| Path | What it is |
|---|---|
| `/` | The docs: 54 pages, light and dark. Every page has a **Feedback** button. |
| `/feedback/` | The feedback inbox: every comment, filter by status, resolve, copy as Markdown. |
| `/dist/index.json` | The spec's version, date and page list. The skill reads this first. |
| `/dist/enterlabs.md` | The whole spec in one file. Single sections sit beside it (`tokens.md`, `components.md`, …). |
| `/dist/tokens.css`, `base.css`, `components.css` | The code. |
| `/assets/brand/` | Logo SVG masters from the kit. |
| `/api/comments` | The feedback API (Cloudflare Pages Functions + D1). |

## Repo layout

```
public/            what Cloudflare Pages serves (built, committed)
  index.html       docs, built from src/
  feedback/        inbox, built from src/
  dist/            spec, built from src/spec/enterlabs.md + src/tokens.css
  assets/brand/    logo files
functions/api/     feedback API routes
lib/feedback.js    shared API helpers
schema.sql         D1 table for comments
src/               sources: page builders, CSS, JS, the spec
brand-kit/         the kit files the builder embeds (logo kit v1.0)
```

## Deploy the first time

You need a Cloudflare account, Node 18+, and Python 3 with Pillow (`pip install pillow`).

1. **Push to GitHub.** Create a repo named `enterlabs-design-systems` and push this folder.
2. **Install and sign in.** `npm install`, then `npx wrangler login`.
3. **Create the database.** `npx wrangler d1 create enterlabs-feedback`. Copy the `database_id` it prints into `wrangler.toml`.
4. **Create the table.** `npx wrangler d1 execute enterlabs-feedback --remote --file=schema.sql`
5. **Create the Pages project.** Cloudflare dashboard → Workers & Pages → Create → Pages → Connect to Git → pick the repo. Framework preset: None. Build command: leave empty. Build output directory: `public`. Cloudflare reads `wrangler.toml`, so the D1 binding comes with it. Name the project `enterlabs-design-systems` so the site lands on `enterlabs-design-systems.pages.dev`, the URL the skill expects.
6. **Set the admin key.** `npx wrangler pages secret put ADMIN_KEY --project-name enterlabs-design-systems`. Resolving and deleting comments need it.
7. **Check.** Open the site, `/dist/index.json` and `/feedback/`. Post a test comment, resolve it in the inbox with the admin key.

Deploying from your machine instead of Git: `npx wrangler pages project create enterlabs-design-systems`, then `npm run deploy`.

### Optional settings

| Setting | Type | Effect |
|---|---|---|
| `ADMIN_KEY` | secret | Unlocks resolve, reopen and delete in the inbox. |
| `TEAM_CODE` | secret | Commenting asks for this code once per browser. Use it while the site is public. |
| `ADMIN_EMAILS` | variable | Comma-separated emails that are admins without a key. Needs Cloudflare Access. |

**Keep feedback private with Cloudflare Access** (free up to 50 users). Zero Trust → Access → Applications → Self-hosted, for the Pages domain, with an Allow policy for your team's emails. Add a second application on `/dist/*` and `/assets/*` with a **Bypass** policy for everyone, so the skill can still read the spec. With Access on, comments are signed with each person's verified email and `ADMIN_EMAILS` works.

## Update the design system

1. Change the docs in `src/` and the spec in `src/spec/enterlabs.md`. Tokens live in `src/tokens.css`; the build stops if the spec's token block and `tokens.css` disagree.
2. On a release, bump the version in the spec's first line (`# Enterlabs design system · v0.4`).
3. `npm run build`, then commit and push. Pages redeploys in about a minute, and every skill run after that uses the new spec. Nobody needs to update their skill.

`npm run dev` runs the site with the API on `http://localhost:8788` (copy `.dev.vars.example` to `.dev.vars`; run `npm run db:local` once).

## Feedback API

| Request | Returns |
|---|---|
| `GET /api/comments?page=button` | Comments on one page, newest first |
| `GET /api/comments?status=open` (`resolved`, `all`) | Every comment with that status. Add `&format=md` for Markdown |
| `GET /api/comments?counts=1` | Open comments per page |
| `POST /api/comments` `{ page, page_title, author, body, code? }` | The new comment |
| `PATCH /api/comments/:id` `{ status: "resolved" \| "open" }` | Admin only (`X-Admin-Key` header or an admin email) |
| `DELETE /api/comments/:id` | Admin only |

To act on feedback with Claude: in the inbox, **Copy as Markdown** and paste it into the chat, or ask Claude to read `/api/comments?status=open&format=md`.
