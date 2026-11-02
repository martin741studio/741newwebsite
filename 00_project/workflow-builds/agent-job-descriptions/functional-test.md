# Functional test (Step 4.2) — fresh general-purpose subagent, 2026-11-03

Task: run the installed skill's write mode for the agent `morning-grill-brief` (scheduled task `morning-grill-0600`) in dry mode: no cards, no placing, one draft file, report stalls.

## Result
- Draft written and validated: `00_project/agent-jobs/morning-grill-brief.md` — `PASS · 0 finding(s)`; slop lint 5/5 after one rewrite (first pass 3/5). Status draft, not placed; a real second deliverable next to `webdev.md`.
- 27 tool calls, 2 of them blocked by the go-gate (read-only greps that named the hook and settings files).

## Where it stalled, guessed, or found the skill unclear (the signal this step exists for)
1. Go-gate blocked Bash greps naming `.claude/hooks/live_change_gate.py` / `settings.json`; hook-rung claims were marked [unverified]. → Fixed: SKILL.md step 2 now says use the Read tool and the rung-ladder/README for hook coverage.
2. Inbox path conflict: examples used `00_project/assets/_agents/<id>/inbox/`, SKILL.md and the task template used `00_project/agent-jobs/<id>/inbox/`. → Fixed: one path everywhere (`agent-jobs`).
3. Validator gaps found on a scratch copy: Go check was a substring test ("Google" passed); review-day check was a substring test; report check did not test "unreadable"; `--copies` passed trivially with an empty `placed_at`. → Fixed: word-boundary regex for Go, explicit no-self-grade phrase required, "unreadable" required, empty `placed_at` = FAIL.
4. No retry cap in the validate loop (R2.5 says 3). → Fixed: max 3 rounds, then BLOCKED.
5. Real contradictions in the described agent (not the skill): the live morning-grill prompt vs the morning-grill skill (bookmark move rule, "steps 0–6 only" vs required steps 7/9/10, `_run.json` status "in Arbeit" vs "fertig", step 3d Supabase read missing from the prompt, `allowed-tools` grants send_message/computer-use/AskUserQuestion so "never send" rests on prose, `references/scheduled-prompts.md` stale). These are proposals for the Morning Grill agent's first Friday review, not edits to make now. → SKILL.md review step 2 now says where such findings go.
6. Cards it would have asked (8) match the design: place Go, agent-specific rules (bookmark, step 3d, tool removal, status value, retry cap), re-enable task, language. The "language" card is no longer needed (decided 03.11., English STE); removed from the open-questions list.

## Verdict
The skill produced a valid, sourced description for an agent it had never seen, with the real gaps marked [unverified] instead of guessed. All six findings are patched in the skill or recorded as review proposals.
