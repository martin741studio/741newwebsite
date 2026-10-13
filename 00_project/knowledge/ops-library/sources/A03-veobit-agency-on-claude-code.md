# A03 — Veobit: a digital agency run day to day on Claude Code

- Author/org: Veobit (New Jersey agency for local service businesses. Web, search, ads, analytics)
- URL: https://github.com/Veobit/agency-on-claude-code (README write-up. Source code private)
- Type: practitioner case write-up (GitHub README)
- Publish date: repo created 2026-09-29, last push 2026-09-30 (GitHub API)
- Fetch date: 2026-10-13
- Closest public match to 741's model: a small agency for local service businesses running on Claude Code.

## Key points (paraphrased)

1. **Owner gate**: the owner approves anything external (outreach), anything that moves money, and every launch. Everything else runs inside gates.
2. **Sessions with roles**: one coordinating session reviews, keeps the record and pushes back. Operator sessions each own one mandate and report to it.
3. **One business record**: a single YAML file holds every lead, account, project, product and opportunity. Every entry has a source and a date. Unknowns are written as "unknown". Changes are proposed and approved before they are written. A validator rejects a bad batch whole. A money figure without a source event or "estimate" label blocks publishing.
4. **Guard hook before every shell command** blocks: pushing a design change to a client site without a recorded critique for that commit. Taking a site out of prelaunch before sign-off. Deploying by direct upload instead of the checked build.
5. **Hours logged** per client and project, billable or not. A daily job flags gaps.
6. **Autonomy ladder** for 19 automations: L0 propose only (5), L1 act and report (8), L2 act within a scope (6), L3 tune itself (none yet).
7. **Pulse log**: each scheduled job writes one line per run, so a silent job shows as stale, never as healthy. Jobs run via launchd on the Mac plus cloud routines.
8. A nightly backup is blocked if a secrets scan finds anything. One unattended job stops itself until its permission rules are settled.
9. A routing contract makes every deliverable name the skill that produced it, so faults are fixed in the skill, not only in the output.
10. Client lifecycle: audit, pitch (owner sends it), onboard, studio (hard gate), launch (hard gate), report. Follow-up and local run alongside.
11. Lessons from one site go into the shared site kit first (14 deploy checks, most added after real failures).
12. Ads: the daily search-term check only proposes changes, by design.

## Use for 741

Strong model for: owner-only decision classes, autonomy ladder per automation, one source-of-truth record with provenance, pulse log for unattended jobs, hours per client.

Short quote: "a silent job shows up as stale, never as healthy"
