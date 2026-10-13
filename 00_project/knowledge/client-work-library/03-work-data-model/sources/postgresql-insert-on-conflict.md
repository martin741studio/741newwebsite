# PostgreSQL 18 Documentation: INSERT (ON CONFLICT)
- URL: https://www.postgresql.org/docs/current/sql-insert.html
- Type: Official documentation (PostgreSQL 18.6)
- Published: living page, fetched 2026-10-13
- Fetched: 2026-10-13

## Key points
- ON CONFLICT DO NOTHING skips a row that violates a unique constraint or index.
- ON CONFLICT DO UPDATE updates the existing row. It needs a conflict target.
- DO UPDATE gives an atomic result: either an insert or an update, also under high concurrency.
- EXCLUDED refers to the proposed row. An alias on the target table refers to the existing row.
- RETURNING gives only rows that were inserted or updated. In version 18, RETURNING can read OLD and NEW values.
- An optional WHERE on DO UPDATE can skip stale updates, but the row is still locked.
- The docs prefer index inference over a named constraint, because inference survives an index rebuild.
- One command cannot change the same row twice. Duplicate keys in one batch raise an error.
- Gaps / bias notes: This is a reference page. It gives no guidance on key design for sync from many producers.
