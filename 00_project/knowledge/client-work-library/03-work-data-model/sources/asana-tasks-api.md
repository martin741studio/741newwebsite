# Asana API Reference: Tasks
- URL: https://developers.asana.com/reference/tasks
- Type: Official API documentation (page metadata updatedAt 2026-10-07)
- Published: living page, fetched 2026-10-13
- Fetched: 2026-10-13

## Key points
- Asana keeps one Task object for several kinds of work. The resource_subtype field holds default_task, milestone, approval or custom.
- A milestone task cannot have a start date. It marks a point in time.
- An approval task has approval_status: pending, approved, changes_requested or rejected. Only pending counts as not completed.
- Completion has three fields: completed, completed_at and completed_by. The record keeps who closed the item and when.
- Dependencies and dependents are opt-in arrays of task ids. The relation exists in both directions.
- The external field holds an app-specific gid and data string. A tool can then address the task as external:<own id>. This gives a stable mapping to outside systems.
- The old assignee_status field is deprecated. Personal planning state does not belong on the shared task.
- Gaps / bias notes: The fetch did not reach the assignee and custom_fields parts of the page (the page is very large). Agent assignment in Asana is in early access and is not confirmed here.
