# Build note — automation-completion = automation-build, installed (steps 3.1-3.6)

Mapping (explicit, so this is not confusing later): the checklist id `automation-completion`
tracks the FINISH-AND-INSTALL work. The deliverable itself is the `automation-build` skill
and its 3 hooks — same name, same files, same design as approved 2026-10-11. Nothing here
is a second/parallel skill.

**3.1 Folder from the 741 template** — installed at user level (Martin's go, 2026-10-15),
per patterns.md section 5's "personal, all projects" row: `~/.claude/skills/automation-build/SKILL.md`.
Scripts/templates/references stay at their existing absolute path inside the 741website repo
(`/Users/martindrendel/741website/00_project/automation-workflow/{scripts,templates,hooks}/`)
— not duplicated, so there is one copy to maintain, not two. Verified: `diff` between the
installed copy and the repo source is empty (identical).

**3.2 Frontmatter: WHAT + WHEN + negative trigger** — unchanged from the 2026-10-11 draft,
already correct: `description` states what it builds, the real trigger phrases
("/automation-build <client> <automation>", "Bau die Zapier-Strecke", "Automation für
<Kunde>"), and the negative trigger ("Do NOT use for website pages or content..., review
pages, one-off data pulls, or writing a message about an automation"). `disable-model-invocation: true`
is set.

**3.3 Body as checklist with gates; critical rules on top** — unchanged: the `## Critical`
section (4 rules, including the 2026-10-14 "never test on live" rule) sits above the P0-P7
checklist with checkpoints A and B.

**3.4 References one level deep; body under 500 lines** — `wc -l` on the installed file:
69 lines (after the path fixes below, well under the 500-line budget). All references
(`automation-workflow.md`, `automation-failure-map.md`, `hooks/`, templates, martin-guide
README) are one level deep, named by absolute path.

**3.5 Verification step with evidence at the end of the body** — step P5 "Verify": fresh
verifier subagent, then `check_report.py <dir>` until PASS, immediately before the go-live
checkpoint. The `## Critical` section additionally states the global rule: "Say done,
fertig, läuft or live only when check_report.py passes. The Stop hook blocks it otherwise" —
this is the hook-enforced version of the same verification step, so it cannot be skipped by
rewording.

**3.6 741 house rules applied** — per-change go (checkpoints A/B + per-action `go A<n>`),
STE/German in client-facing text (`runbook-de.md`, `testprotokoll-de.md`), no team or
method-source names in the client-safe test protocol, client message draft in Ich-Form/du
for Martin at P7. One known, already-acknowledged gap carried over from 2026-10-11 (not
new, not fixed here): handover uses a portal page, not a Drive link — matches the separate
house rule that client text drafts go to the portal node, not a Drive doc.

**Fix applied during this build (new, 2026-10-15):** the skill body used several paths
relative to the `741website` repo root (`00_project/automation-workflow/scripts/run_state.py`,
`templates/...`, etc.). Those break when the skill runs from a different project folder —
exactly the scenario Martin's Q2 go was meant to cover ("client work also runs in other
folders like ~/huewel-site"). Changed every reference to the absolute path
`/Users/martindrendel/741website/00_project/automation-workflow/...`. Proven correct by the
S1 trigger test (trigger-tests.md): invoked from a scratch folder outside any 741 project,
`run_state.py init` still wrote the run folder under the real repo's `00_project/assets/`,
not under the scratch folder or failing with "file not found".

Also added one explicit line to P3a (the 2026-10-14 Zapier-AI-draft step), from the light
Zapier Copilot/Agents research in research-note.md: Copilot/Agents prompts "Test" and then
"Publish" inside its own chat — the skill now says explicitly that accepting those prompts
is not 741's test gate, P4/P5 still apply regardless.

**3.7 Unattended rules** — not applicable: `/automation-build` is Martin-triggered
(`disable-model-invocation: true`, no schedule). Skipped with reason via `check_build.py skip`.
