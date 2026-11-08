# content-pool: telemetry record

After steps 8 and 12, run `python3 scripts/validate_pool.py --run-dir 00_project/assets/<client>/content-pool/` (0 errors) and write `00_project/assets/<client>/content-pool/<YYYY-MM-DD>/_run.json`. The Stop hook runs `workflow_registry.py sync` and updates `~/Desktop/Workflow-Uebersicht.xlsx`.

```json
{
  "client_id": "<client>",
  "workflow_id": "pool",
  "checkpoint": "cp2",
  "status": "passed",
  "mode": "production",
  "metrics": {
    "candidates_scored": 42,
    "pillars_populated": 4,
    "validation_errors": 0
  },
  "evidence_file": "00_project/assets/<client>/content-pool/summary.json",
  "result_summary": "Content pool and sitetree generated with 0 validation errors.",
  "error_signal": null,
  "updated_at": "ISO-TIMESTAMP"
}
```
