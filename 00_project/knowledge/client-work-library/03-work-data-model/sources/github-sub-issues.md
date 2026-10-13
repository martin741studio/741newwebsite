# GitHub REST API: Sub-issues
- URL: https://docs.github.com/en/rest/issues/sub-issues
- Type: Official API documentation (API version 2026-03-10)
- Published: living page, fetched 2026-10-13
- Fetched: 2026-10-13

## Key points
- An issue can have one parent and many sub-issues. The API can get the parent, list, add and remove sub-issues.
- Adding a sub-issue takes a sub_issue_id. An optional replace_parent flag moves it from its old parent.
- A sub-issue must belong to the same owner as the parent.
- A reprioritize endpoint sets the order of sub-issues with after_id or before_id. Order is relative, not a number.
- Each issue carries parent_issue_url. It also carries a sub_issues_summary with child counts and a percent_completed value.
- Progress is computed from the children. Nobody types the percent by hand.
- Gaps / bias notes: The page states no limit for depth or count. It covers hierarchy only, not status or ownership.
