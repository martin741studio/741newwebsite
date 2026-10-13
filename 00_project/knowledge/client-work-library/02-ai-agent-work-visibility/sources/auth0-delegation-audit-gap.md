# Closing the audit gap in human-to-agent delegation

- URL: https://dev.to/auth0/closing-the-audit-gap-in-human-to-agent-delegation-48il
- Type: vendor blog (practitioner article, Vivek Maskara for Auth0)
- Published: 2026-10-09 (page metadata datePublished)
- Fetched: 2026-10-13

## Key points
- Agents often act with tokens in the name of a user. Normal logs then show that the user did the action.
- A good record shows who authorized the action and which agent ran it.
- It also shows how the agent got access, and if a human approved.
- Log the approval request, the pending state, and the result (approved, denied, or expired) as one audit item.
- Use one stable ID per run (run ID, job ID, or workflow ID). Carry it through all logs and API calls.
- A reader comment adds: give each important tool call its own ID. One run can do several actions.
- Ask for human approval only for high-impact actions: data export, payments, permission changes, deletes, and publishing.
- Watch for repeated token refreshes at odd times. They can show a loop or a broken workflow.
- Join identity logs with app traces and provider logs in one place.

## Gaps / bias notes
- Vendor article about its own identity product.
- Technical focus. It does not cover how a task list shows this to non-developers.
