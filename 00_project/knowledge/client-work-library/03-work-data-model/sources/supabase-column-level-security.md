# Supabase Docs: Column Level Security
- URL: https://supabase.com/docs/guides/database/postgres/column-level-security
- Type: Official documentation
- Published: living page, fetched 2026-10-13
- Fetched: 2026-10-13

## Key points
- RLS controls rows. It does not control which columns a role can see.
- Postgres column privileges can grant or revoke select and update per column.
- A restricted role cannot use "select *" on such a table. Every query must list the columns.
- A revoked column fails on insert, update, delete and "select *".
- Supabase calls this an advanced feature and does not recommend it for most users.
- Supabase recommends RLS plus dedicated tables instead.
- Gaps / bias notes: The page does not explain how to split sensitive columns into a second table. That step is an inference from the advice.
