# Decision Record: Checkpoint 2 (Ship Approval)

Workflow ID: unburning
Name: Un-Burning Harm Remediation
Date: 2026-10-16
Owner: Martin

## Status: GO / APPROVED

Martin reviewed the complete validation package for `unburning` and gave his explicit Go / approval:
- Scorecard audited against `_derived/scorecard.md`: **Total Score 95.8 %** (0 blocking zeros).
- Real functional output verified on Praxis Suriya dry run (`00_project/assets/un-burning/praxis-suriya/2026-10-11-dryrun/`): 56 harm items validated with 0 schema errors via `scripts/validate_run.py`; Bedrock lights accurately calculated via `scripts/bedrock.py`.
- Baseline efficiency confirmed: -91.4 % token consumption, -90.0 % tool calls, 0 unintended live edits.
- Telemetry contract: Universal `_run.json` requirement enforced at `00_project/assets/<client>/unburning/<YYYY-MM-DD>/_run.json`.

Authorized to proceed to Gate Install, registry synchronization, and permanent memory logging.
