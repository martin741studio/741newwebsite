# [Agency workflow] Build one accountable daily operator queue across client delivery (GitHub issue #461)
- URL: https://github.com/camster91/ashbi-platform/issues/461
- Type: practitioner product spec (open-source agency platform issue)
- Published: 2026-09-25 (comment 2026-10-01: first version shipped)
- Fetched: 2026-10-13
## Key points
- The spec asks for one daily queue across all client delivery work.
- The queue has four views with a count each: Needs action, Awaiting approval, Waiting on client or external party, At risk or overdue.
- Every row names one accountable owner. Every row has a next action or a clear waiting reason.
- Each row shows its due date and its age.
- Each row links to one source record. Changes happen in that source record, not in the queue.
- Approval actions stay pending until an authorized person records the decision.
- Each row has a "last verified activity" field.
- Stale or missing data gets a label. The queue must not show it as healthy or done. Quote: "Do not invent urgency from missing or stale data."
- Non-admins see only their own tasks. Finance and approval sources are admin-only.
- Gaps / bias notes: One small project, not a study. No ranking rule. No usage data yet.
