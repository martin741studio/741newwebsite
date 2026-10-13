# A09 — Your AI Agent Needs a Queue, Not a Chat Box

- Author: Shilpa Mitra (Web After AI)
- URL: https://webafterai.substack.com/p/your-ai-agent-needs-a-queue-not-a
- Type: technical article
- Publish date: 2026-08-27 (shown on page)
- Fetch date: 2026-10-13

## Key points (paraphrased)

1. Most agents are built like one chat request. Real work needs a durable workflow that survives failures and long waits, including approvals.
2. Record each task as explicit steps with a status.
3. Retry failed steps. Never repeat steps that already completed.
4. Put clear boundaries around side effects (API calls, database writes).
5. Human approval is a step inside the workflow, with its own state.
6. Use idempotency keys so a retried step cannot send or write twice.
7. Treat notifications as separate, trackable steps.

## Use for 741

The decision queue and the evening log should be files or table rows with status fields (open / decided / parked / done), not chat history. A re-run of the morning routine must not create duplicate cards or send duplicate messages.

Short quote: "Make steps safe to retry."
