# LangChain: human-in-the-loop middleware

- URL: https://docs.langchain.com/oss/python/langchain/human-in-the-loop
- Type: official doc
- Published: living page, fetched 2026-10-13
- Fetched: 2026-10-13

## Key points
- The middleware checks each proposed tool call against a policy. If the call needs review, the agent pauses and saves its state.
- The team sets a rule for each tool: always pause or never pause.
- A third option pauses only when a condition is true, for example a write outside a folder.
- The human has four decisions: approve, edit, reject, and respond.
- Edit changes the arguments before the action runs. The doc advises small edits, because large edits make the agent re-plan.
- Reject skips the action and sends feedback. For side effects, the feedback should say: drop it, ask, or try a safer way.
- Do not use "respond" to deny an action. The agent then treats the action as done.
- The pause message shows the tool name, the arguments, and the allowed decisions.
- A durable store (checkpointer) and a thread ID keep the paused run. The run can wait for a long time and then resume.
- The older "Agent Inbox" UI used accept, edit, respond, and ignore. Names differ between versions.

## Gaps / bias notes
- Developer framework doc. It shows no dashboard for non-developers.
- The page does not cover timeouts for pending decisions.
