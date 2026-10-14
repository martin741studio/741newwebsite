# N10 — Node.js Release Working Group README (official release schedule)

- Org/author: Node.js project (Release Working Group)
- Type: official project documentation, living
- Publish date: living/evergreen README; dates it states (EOL dates, LTS transition dates) were cross-checked against N09's independent third-party summary and matched. Counted as current on fetch date.
- URL: https://cdn.jsdelivr.net/gh/nodejs/release@main/README.md
- Fetch date: 2026-10-15

## Extract (own words)

- Node 22: Maintenance LTS, end-of-life **2027-04-30**.
- Node 24: Active LTS; maintenance phase begins **2026-10-20**; end-of-life **2028-04-30**.
- Node 26: Current; Active LTS begins **2026-10-28**; end-of-life **2029-04-30**.
- Starting with Node 27, the release model itself changes: one major release lands each April, with LTS promotion following in October. Node 26 is the last release line under the current (more frequent) model.
- Stated reason for the model change: maintainer capacity — "managing security releases across four or five active release lines has become difficult to sustain."
- The project does not build security patches for end-of-life lines, full stop — there is no "we'll still patch critical CVEs" exception stated.

## IF/THEN rules for 741

1. IF 741-agents-01 stays on Node 22.x past April 2027, THEN it is running an end-of-life, unpatched runtime — plan the migration to 24.x (or whatever is Active LTS by then) with real lead time, not reactively.
2. IF 741 wants to minimise future migration churn, THEN note the release model itself is changing after Node 26 (one release per year instead of ~2/year) — the cadence of "how often do I need to repeat this whole exercise" is about to slow down, which is useful context for not over-building automation around the current faster cycle.
3. IF Martin ever asks "can we just stay on an old Node version since it works," THEN the direct answer from this source is no safety net exists past EOL — no patches ship for an end-of-life line regardless of severity.

## Caveats

- All dates in this README are explicitly marked by the project itself as "subject to change" — re-check before relying on an exact date for a migration deadline.
