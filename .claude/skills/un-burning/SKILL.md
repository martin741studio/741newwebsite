---
name: un-burning
description: Runs the 741 Un-Burning clean-up for one client. Finds what harms the online presence (wrong NAP, spam listings, 404s, duplicates, thin or orphan pages, bad indexing, suspect reviews), builds a harm register and keep/fix/kill list, repairs approved items in waves with rollback. Trigger on "Un-Burning für KUNDE", "Altlasten aufräumen", "NAP-Bereinigung", "404 auf 301", "Index aufräumen", "/un-burning". Not for the Maps audit (maps-audit).
disable-model-invocation: true
allowed-tools: Read, Grep, Glob, Bash(python3:*), Bash(curl:*), Bash(dig:*), Bash(whois:*), Bash(ls:*), Bash(mkdir:*), Bash(shasum:*)
---

# Un-Burning

Spec: `/Users/martindrendel/741website/00_project/un-burning-workflow.md` (read the sections named below, not the whole file).
Data model: `/Users/martindrendel/741website/00_project/un-burning-workflow/data-model.md`. Schema: `harm-register.schema.json` next to it.
Interface with the audit: spec section 3. Un-Burning removes harm. It does not add gap items.

## Critical

- `scan` changes nothing on any client asset. A live change needs a go: GO-1 (kill list), GO-2 (each wave), GO-3 (client release). One go never covers the next change.
- Every item has evidence, source, date and confidence (`verified`, `derived`, `client_stated`). Never guess addresses or dates. Ownership and access are NOT part of Un-Burning: they are onboarding preconditions. A gap there marks actions `blocked`. It never becomes an item, a light or a bedrock criterion. An unreadable source is "unreadable", never "nothing found".
- Nothing is deleted without a snapshot and a rollback step. A page with clicks or backlinks is never deleted without a 301.
- Suspended or ineligible profiles: compliant route only (real business, real eligible address, proof, video verification). No address workarounds. Review removal: Google report and appeal routes and a legal route only.
- Client mail only through Airmailer, never without Martin's go. Drafts are full texts in "ich" form. German clients: "du". Health clients: HWG check.

## Inputs

- Client name and slug, domain, GBP name or place id, known history (what burned, since when).
- The locked NAP master record (`client_locations` row or `nap-master.json`). If missing, stop and ask once, in one line.
- Mode: `scan` (default), `scan --from-audit <run>`, `reverify`. Flags: `--with-backlinks`, `--areas C,D,E`.

## Workflow

Copy this checklist and tick it off:

- [ ] 0. Intake. Create `00_project/assets/un-burning/<client-slug>/<YYYY-MM-DD>-<mode>/`. Check the master record. Copy the baseline files once into `baseline/`. State the mode, areas and cost cap in one line.
- [ ] 1. Scan (read only). Check the preconditions (NAP master locked, access present) and write `preconditions.json`. Start the area C, D and E scan agents in parallel (prompts in `references/subagent-prompts.md`; maximum 4 agents; Haiku or Sonnet is enough). Each agent writes its own `part-<area>/` folder (harm-register.json + manifest.json; brief template in the Stürzl run: `scan-brief-common.md`). Validate each part, then merge: `python3 -I scripts/merge_parts.py <run-folder> --client-slug <slug> --domain <domain> --scanned A,C,D,E`. Close duplicate items between areas (mark `keep`, `rejected`, with a pointer). If `--from-audit`, read the audit `findings.json` first and map fields per spec section 3.
- [ ] 2. Validate. Run `python3 -I scripts/validate_run.py <run-folder>`. Fix until it prints `VALID`. Do not proceed on errors.
- [ ] 3. Review. Start a fresh reviewer subagent (prompt in `references/subagent-prompts.md`). It reports only correctness gaps. Fix the gaps.
- [ ] 4. Bedrock and report. Run `python3 -I scripts/bedrock.py <run-folder> --write`. Build the report: `python3 -I scripts/build_report.py <run-folder> --out report/internal.html`. Check it with a screenshot in rendered state.
- [ ] 5. **GO-1.** Show page 1 and the keep/fix/kill list. Wait. Record per item: keep, fix, kill, hold. A whole class may be approved only if it is reversible. Destructive items need a per-item go.
- [ ] 6. Execute per wave (order: 1 reversible, 2 redirects, 3 content, 4 deletes and reports). Write `changes.json`. Run `python3 -I scripts/validate_changes.py changes.json harm-register.json` and fix until `WAVE OK`. Take the snapshots. **GO-2:** show the exact change list and rollback steps. Wait. Apply. Append `change-log.jsonl`. Verify each item live and save `after`. Roll back an item that fails twice.
- [ ] 7. Re-scan with the same parameters. Compute the delta. Run `bedrock.py` again. Build the before/after tracker against `baseline/`.
- [ ] 8. Client tab (draft) and message. Build `python3 -I scripts/build_report.py <run-folder> --client --form sie|du --out report/client.html`. It shows only items with a reviewed `client_text`. Then grep it for tool and table names. Draft the client message as one full text. Send nothing.
- [ ] 9. **GO-3.** Show the client tab draft, the message draft and the Drive link. Wait. Release only on a clear yes.
- [ ] 10. Deliver: Drive link, screenshot as a file, list of open items. State what was verified and how.


## Rules in short

- Page with clicks or backlinks: keep, fix, or merge with a 301. Never delete. Duplicate: keep the stronger page, 301 the other. Wrong NAP on a listing: claim and fix first, delete only if the correction route fails (per-item go). Suspect review: report only if it fits a Google policy case; 741 does not answer reviews.
- **Suriya:** read `references/suriya-rules.md` before any change (page 1511 stays untouched, name, address, phone, forms, no live edit). Dinakar edits the same site: name the pages of each wave at GO-2.
- Browser reads of a Google profile only with Martin's go, read only, as 741studio18.

Details: `references/decision-rules.md` (all decision rules, browser reads), `references/suriya-rules.md`, `references/registry-and-guide.md` (registry sync, Martin guide), `references/subagent-prompts.md` (prompts for the C, D, E scan agents and the reviewer).

## Output template

Page 1 of `report/internal.html` always has: four area lights (B, C, D, E), damage tally (blocks revenue / leaks link power / cosmetic), top 5 leaks, next 3 actions, open approvals, before/after, data coverage. See `00_project/un-burning-workflow/report-wireframe.md`. ALWAYS use this layout. `scripts/build_report.py` builds both reports from `harm-register.json`.

## Checkpoints

- After step 4: GO-1. After each wave plan: GO-2. After step 8: GO-3.
- If a source is unreadable, say so on page 1 under "Datenlage".

## Verification

- `validate_run.py` must print `VALID`. `validate_changes.py` must print `WAVE OK` before any execution.
- The final report states: the commands run, their output, the screenshot path, the Drive link.

## Registry

The overview Excel updates itself (Stop hook `workflow_registry.py sync`). Keep `<run>/run.json` current: `client`, `mode` (`dryrun` or `live`), `finished_at`. Approval is manual: `python3 /Users/martindrendel/741website/00_project/workflow-registry/workflow_registry.py approve --client "<client>" --workflow unburning` in the same turn.
