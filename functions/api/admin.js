// /api/admin  GET: is this request an admin? The inbox uses it to check a key.
import { json, isAdmin } from '../../lib/feedback.js';
export const onRequestGet = ({ request, env }) => json({ admin: isAdmin(request, env) });
