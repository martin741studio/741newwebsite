# Build evidence — section 3 (goals-data-architecture)

## 3.1 Folder from the 741 template
Not a new skill — extends the existing `morning-grill` skill, which already has the template shape (`SKILL.md`, `scripts/`, `references/`, `assets/`) at `00_project/morning-grill-skill/` (source) and `~/.claude/skills/morning-grill/` (installed copy, per its own "edit there, then re-copy" rule). New files added to both, in parallel, without touching the pre-existing drift between the two copies (live has WhatsApp/computer-use additions the repo source lacks — not my change, left alone):
- `scripts/generate_goals.py` (Phase A — generation)
- `scripts/reconcile_drive.py` (Phase C — reconciliation)
- `assets/reconcile-sheets.json` (per-client Drive sheet registry, starts with Stürzl)
- `references/goals-architecture.md` (operating reference)
- `00_project/morning-grill-goals-overlay.json` (repo root, next to `morning-grill-goals.json`, same convention as the goal sheet itself)
- `00_project/morning-grill-goals-archive-log.md` (created on first write by `generate_goals.py`)

## 3.2 Frontmatter: WHAT + WHEN + negative trigger
No change needed. The skill's trigger surface is unchanged — Martin still says "grill me" / "morning grill" etc., the same as before. This build only changes what happens *inside* an existing, already-triggered run (one new step before the scan, one new Monday/on-demand step), so the existing `description` (WHAT + WHEN + NOT) in `SKILL.md` still accurately describes when the skill loads. Reviewed, not rewritten.

## 3.3 / 3.4 Body as checklist with gates; references one level deep
`SKILL.md` (both copies) got: one Critical bullet ("goals.json is generated, never hand-edited"), one new checklist step `3c` (regenerate before scanning, read the warnings, refuses to write on an unexplained drop), one Monday/on-demand line (reconciliation), one `## References` line. Full detail lives one level deep in `references/goals-architecture.md` (under 100 lines, no TOC needed). Evidence: `00_project/morning-grill-skill/SKILL.md` and `~/.claude/skills/morning-grill/SKILL.md` (diffed identical except for the pre-existing, unrelated drift).

## 3.5 Verification step with evidence
`generate_goals.py` has its own feedback loop (R2.7): it diffs against the previous file, logs every status/phase transition, prints every warning (unmatched Supabase client, overlay status_override active), and **refuses to write** if the client count would drop without an explained removal. `reconcile_drive.py` never writes at all — it only emits flagged items for a human-answered card. The skill's existing `validate_brief.py` end-of-run check is unchanged and still the final gate for the whole grill run.

## 3.6 House rules applied
- No live site, no client message, no portal write in this build — everything is internal tooling (morning-grill's own data).
- The one write performed (`work_goals` backfill, 15 rows) was Martin's explicit go #2, a data write not a schema change, read-only from then on.
- STE: all replies to Martin in this build were in Simplified Technical English (reports, decisions.md, this evidence set).
- No tool/provider names leaked into any client-facing material — not applicable here (nothing client-facing was touched).

## 3.7 Unattended rules (the scan step runs inside the 06:00/17:00 scheduled task)
- R6.1/R6.2: `generate_goals.py` never silently reports "nothing new" — a dropped client or an unmatched Supabase row is always printed as a warning, never hidden.
- R6.5 read-only credentials: `generate_goals.py` only issues `GET` requests (enforced in code, not at the DB role level — the reused `standup-bot` credential has `profiles.role='admin'`, so this is a code-level discipline, not a DB-level guarantee; noted as a possible future hardening, not blocking).
- Writes that need judgment (goal-number capture, reconciliation resolution, the one-time backfill) are never run inside the unattended 06:00/17:00 task — they happen only in an attended chat with Martin's go, same rule the skill already applies to `publish_tasks.py`.
- R6.6 time zone: unchanged, WITA throughout, same as the rest of the skill.
- R6.3/R6.4 (confirm before ledger, re-check before posting): the archive log is append-only and only written after a successful file write; the reconciliation pass re-reads both sides fresh on every run, never caches a stale comparison.
