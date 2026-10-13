# GitHub REST API: Issue dependencies
- URL: https://docs.github.com/en/rest/issues/issue-dependencies
- Type: Official API documentation (API version 2026-03-10)
- Published: living page, fetched 2026-10-13
- Fetched: 2026-10-13

## Key points
- GitHub models dependencies as "blocked by" relations between two issues.
- One endpoint lists the issues that block an issue. A second endpoint lists the issues that this issue blocks.
- A POST adds a "blocked by" relation with the numeric issue_id of the blocker. A DELETE removes it.
- Each issue response carries an issue_dependencies_summary with the blocked_by count, the blocking count and totals.
- The relation is an edge between two items. It is not a text field on the item.
- Fast add and remove calls can hit secondary rate limits. Bulk sync must pace its writes.
- Gaps / bias notes: The page does not give rules for cycles or cross-repository limits. It is an API reference, not a modelling guide.
