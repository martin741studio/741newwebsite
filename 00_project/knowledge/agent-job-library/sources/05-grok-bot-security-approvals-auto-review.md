# 05 — Grok Bot docs: Security (Approvals and Auto Review)

Type: vendor documentation (follow-up to source 04). Fetched 2026-11-03.
URL: https://cursor.com/docs/grok-bot/security

## Key content
- "The strongest boundary is the one in the request itself, so have members state what a Bot may change and where it must stop." Example: "Reconcile the campaign data and draft a recommended budget change. Don't change the campaign or message the agency. Ask for approval after showing the current value, proposed value, and expected impact."
- Approval card shows the proposed operation and its inputs; Allow once / Always allow (saves a rule) / Deny. "An approval controls the proposed action, not work already completed, and nobody should approve an action whose target or effect they can't identify."
- Auto Review = an independent review model that evaluates risky actions before they run (shell, app calls, computer use, automation writes, delegation). It can proceed, require approval, or deny.
- Rules: "Ask first" rules always stop; "Allow automatically" rules only loosen when the reviewer finds no other reason. Personal rules only make behaviour stricter. "Keep rules narrow and tied to a known action, like 'ask first before sending any external email'. Avoid broad rules like 'allow everything in the browser'."
- "It doesn't review every side effect. Memory writes and most settings changes are examples. Treat it as a complement to explicit boundaries and least privilege, working alongside controls that don't depend on a model's judgment: per-action approvals, the network policy, and per-user isolation."
- Bots act as the signed-in member; no identity of their own; credentials never reach the model.
- Prompt injection: outside content is untrusted; "keep consequential actions behind approval."

## Assessment for 741
New vs. video: the layering — request boundary (prose) < model reviewer (judgement) < deterministic controls (approvals, allowlists, isolation). Tyler has only the first layer.
Marketing: Enterprise-only feature list.
Usable for 741: 741's stack already has the deterministic layer (go-gate PreToolUse hook, settings deny lists). The job description is the prose layer and must say which of its "never" lines are enforced by a hook and which are advisory only. "Nobody should approve an action whose target or effect they can't identify" = the approval card must show the exact change (already Martin's rule: show the exact change, then a card with "Go" in the label).
