# Pipeline — marketing-grill (Step 2.4)

```
[ Trigger: "marketing grill" / /marketing-grill / a channel-strategy question ]
                      │
                      ▼
[ 0. Read phase (read-only, no cards yet) ]
  - Grep the knowledge base: _derived/visibility-leads-master-reference.md,
    playbook-notes-channel-selection.md, hormozi-library/ (via grep on demand)
  - Read 741's real current state: marketing-quarter-campaign, revenue-model-100k,
    741-youtube-channel-avatar, coldemail-sending-infra + smartlead-cold-email
    (live state, not assumed), hubspot-leads-segmentation, leadgen-funnel-infra,
    stipendium-giveaway-page
  - If a prior playbook exists (00_project/assets/741studio/marketing-grill/),
    read it too (use case 2: re-run)
                      │
                      ▼
[ 1. Round 1 card: What marketing to do ]
  AskUserQuestion, grounded in Core Four + intent/interruption traffic +
  offer readiness. Recommended option first. Max 4 cards.
  <<< CHECKPOINT: Martin's answer recorded >>>
                      │
                      ▼
[ 2. Round 2 card: Where to reach people ]
  AskUserQuestion, grounded in 741's real avatar (agency owners, per
  741-youtube-channel-avatar) + Lead Getters (referrals/affiliates/agencies/employees)
  <<< CHECKPOINT >>>
                      │
                      ▼
[ 3. Round 3 card: How to focus and double down ]
  AskUserQuestion, grounded in More/Better/New, depth-before-width, Rule of 100,
  "what to STOP doing"
  <<< CHECKPOINT >>>
                      │
                      ▼
[ 4. Round 4 card: How the activity is structured ]
  AskUserQuestion, grounded in owner/volume/cadence/speed-to-lead rules;
  explicitly routes into the existing Morning Grill / Outreach board, not a
  parallel system
  <<< CHECKPOINT >>>
                      │
                      ▼
[ 5. Write the playbook ]
  00_project/assets/741studio/marketing-grill/<date>/playbook.md
  Every claim cites its source file. No invented numbers.
                      │
                      ▼
[ 6. Slop check + STE check on the delivered playbook text ]
                      │
                      ▼
[ 7. Report to Martin: the playbook + what changed vs. prior run (if any) ]
  Hard limit: the grill NEVER launches ads, sends outreach, spends money,
  or changes a live site. It only produces the document.
```

Checkpoints: after each of the 4 card rounds, Martin's answer is the gate — no round proceeds without his card response (AskUserQuestion blocks by design). No separate "go/no-go" checkpoint is needed beyond the card rounds themselves, since nothing in this pipeline has a side effect until Martin reads the final playbook and decides what to act on outside the workflow.
