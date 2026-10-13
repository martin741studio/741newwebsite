# A02 — The Approval Queue Is the Product

- Author: Manish Lad
- URL: https://manishlad.substack.com/p/the-approval-queue-is-the-product
- Type: practitioner essay (design of background agents)
- Publish date: 2026-10-06 (shown on page)
- Fetch date: 2026-10-13

## Key points (paraphrased)

1. For background agents the real interface is not the chat. It is the **queue** where the human decides and the **log** where the human looks back at what happened while away.
2. Every approval request should be decidable in about a minute. If it is not, the request is badly built.
3. An **activity log** records actions the agent took while the person was away. It is the second half of the interface.
4. A routing policy puts every action in one of three paths: run automatically, run and notify, or wait for approval.
5. Route by reversibility and impact, not by how confident the agent sounds.
6. Use approval history to decide where autonomy can grow: actions that are always approved unchanged are candidates for "auto + notify".
7. Measure queue health: time to decision and queue age.
8. Approvals are not a patch for permissions that are too broad. Narrow the permissions first.
9. Waiting is a behaviour that someone must design (what happens while a decision is pending, and when it expires).
10. The queue should be visible to the team, not hidden in one person's chat.

## Use for 741

Defines the three routing classes for the grill and the evening log ("what agents did while you were away"). Gives two metrics to track: time-to-decision and oldest open card.

Short quote: "Waiting is a behavior, and someone has to design it."
