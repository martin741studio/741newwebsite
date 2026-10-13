# Supabase Docs: Row Level Security
- URL: https://supabase.com/docs/guides/auth/row-level-security (redirects to /docs/guides/database/postgres/row-level-security)
- Type: Official documentation
- Published: living page, fetched 2026-10-13
- Fetched: 2026-10-13

## Key points
- Enable RLS on every table in an exposed schema. Without RLS, any role with a grant can read and write the table.
- Revoke default grants and grant back only what each role needs. Policies do not remove grants.
- Write one policy for each operation (select, insert, update, delete). Do not use one "for all" policy. An update also needs a select policy.
- Name the role in each policy with the "to" clause.
- Wrap auth.uid() in a select so Postgres caches it per statement. Check that it is not null.
- Index every column that a policy filters on, for example client_id.
- Views bypass RLS by default. On Postgres 15 and later, set security_invoker = true on each exposed view.
- Keep authorization data in app_metadata, not in user_metadata, because users can edit user_metadata.
- The secret (service) key bypasses RLS. Use it only on the server. Test policies with pgTAP for both allowed and denied cases.
- Gaps / bias notes: The page gives no date. It does not give a full multi-tenant agency pattern (admin, team, client in one model).
