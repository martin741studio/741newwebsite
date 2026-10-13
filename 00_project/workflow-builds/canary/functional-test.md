# 4.2 Functional test — canary (fresh session "Claude B", 2026-10-14)

Real task: test scenario T5, Mode B on the incident "CANARY marcel-gewinnspiel-recon: 6 Tally submissions, 0 Pipedrive deals in 60 min" — the exact case the design anticipated (hand-run.md gap G-a: Tally/Pipedrive reads need API keys).

First run (before the disable-model-invocation fix): Skill tool refused outright at step 1. Zero steps reachable. Reported and fixed (see trigger-tests.md).

Re-run after the fix:
1. Skill tool invocation succeeded, loaded SKILL.md.
2. `registry.py list --client "Marcel Rosenbach"` found `marcel-gewinnspiel-reconciliation` (type R, SEV2, status planned, runner hand) — note already states the exact blocker.
3. `references/runbooks.md` "Reconciliation gap (type R)" section matched and was followed: confirm the read isn't the problem → identify the broken hop → usually SEV2 unless the live lead path is broken now.
4. No self-heal action-id applies to a reconciliation gap (diagnosis-only, correctly) — Claude B sanity-checked `allowlist.py` on 3 ids (recheck=allowed, zapier-replay=needs go, a made-up write=not allowed) and confirmed none fit.
5. Stalled exactly where the registry predicted: no live Tally/Pipedrive reads. This is the real external blocker (Marcel hasn't sent the keys yet), not a skill gap.
6. Minor ambiguity noted: type-R runbook has no named self-heal id, so "no fix applies" needed a one-line inference rather than a lookup; and the SEV1-vs-SEV2 call in runbook step 3 needs the real counts (used the registry's pre-set SEV2 as the test default).
7. Verdict (Claude B, verbatim): "The skill carried this to a correct, deliberate stop... but only because the registry had already pre-diagnosed the exact blocker; for a genuinely new type-R incident the runbook alone doesn't name a self-heal action, so it would still need Martin regardless of credentials."
`verify.py` → 14/14 ALL CHECKS PASSED (Claude B ran it independently).

No real alert was sent for this fictional incident, as instructed.
