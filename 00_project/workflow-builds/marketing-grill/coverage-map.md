# Coverage map — marketing-grill (Step 1.4, existing 741 asset check)

Checked `ls .claude/skills/` and the relevant memory files before building anything new. No existing skill does a Martin-facing "what marketing to do" grill. The closest skills are adjacent legs to route INTO, not duplicate:

| Skill | What it already does | How marketing-grill relates |
|---|---|---|
| `content-format-board` | Builds a short-video idea board per client/prospect, grounded partly in the same Content Marketing Playbook notebook. | Organic-content EXECUTION leg. The grill decides whether/how much to invest in organic content; if yes, it routes Martin to this skill, never rebuilds its format logic. |
| `personal-posts` | Drafts 741's own text/image social posts, also grounded in the Content Marketing Playbook notebook. | Same organic-content leg, text format. Same routing rule — the grill picks the channel, this skill executes it. |
| `sales-pitch`, `sales-call-prep`, `booking-sequence` | The sales leg once a lead is engaged (pitch architecture, call prep, post-booking WhatsApp sequence). | Downstream of lead generation — the grill's job ends where a lead becomes "engaged" (per the Lead vs. Engaged Lead distinction in `_derived/visibility-leads-master-reference.md`); these skills take over from there. |
| `morning-grill` | The card-based decision-interview pattern (AskUserQuestion rounds, max-cards-per-round rule, decision ledger). | Not a marketing-content skill — reused here only for its MECHANICS (how a grill-me round works), not its content. |
| `canary` | Monitors existing client systems/automations for outages. | Unrelated; mentioned only because the brief's "coldemail-sending-infra" state-check (EXPIRED since 14.08.) is the kind of real-infrastructure-state check the grill must do before recommending cold outreach as a channel — it must not assume dead infrastructure still works. |

No existing workflow build (`00_project/workflow-builds/*`) covers channel selection, Lead Getters, or the More/Better/New focus framework for 741's own marketing. This build is net-new, not a rework.

## Adjacent infrastructure state (read, not re-verified live in this step — to be checked live during the grill itself, per `claims-need-real-data`)
- `coldemail-sending-infra.md`: 12 domains + Zapmail infra exists.
- `smartlead-cold-email.md`: EXPIRED since 2026-08-14 — cold outreach is not currently a working channel without fixing this first.
- `hubspot-leads-segmentation.md`: exists, state to be read live when the grill reaches the cold-outreach question.
- `leadgen-funnel-infra.md`, `stipendium-giveaway-page.md` (NOT deployed): lead-magnet assets that exist or half-exist — the grill must present these as "half-built," not "ready."
- `marketing-quarter-campaign.md`: existing 12-week plan (4 streams) — the grill must be able to re-evaluate this plan, not contradict it blindly or ignore it.
