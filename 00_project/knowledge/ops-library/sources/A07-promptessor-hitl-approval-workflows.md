# A07 — Human-in-the-Loop AI Agents: Approval Workflows and Best Practices

- Author/org: PrompTessor Team
- URL: https://promptessor.com/blog/human-in-the-loop-ai-agents
- Type: practical guide
- Publish date: 2026-10-06 (from `article:published_time` metadata. No visible date on page)
- Fetch date: 2026-10-13

## Key points (paraphrased)

1. Do not gate every action. Classify by risk. Low-risk actions run automatically.
2. Four decision types for the human: **approve, modify, reject, escalate**. Approve/reject alone is too narrow.
3. Approval must pause the workflow and resume it later, not restart the conversation. State must survive long delays.
4. An approval can **expire**: if the world changed since the request, re-check state and ask again.
5. The reviewer needs a full context package at the moment of decision.
6. Escalation differs from approval: it says the decision is outside this agent's or reviewer's authority.
7. Define timeout and escalation behaviour in advance.
8. Approval fatigue makes oversight meaningless.
9. Keep an audit trail of who decided what, when, and on which evidence.

## Use for 741

Adds "modify" and "expiry" to the decision card design. A card answered yesterday may need re-validation today before an agent acts on it.

Short quote: "Approval fatigue can make oversight meaningless."
