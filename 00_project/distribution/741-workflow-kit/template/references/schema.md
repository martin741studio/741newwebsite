# Data Schema Reference

## Ingest Payload Schema
When invoking `scripts/run.py`, the expected input schema is:

```json
{
  "client": "string (required)",
  "mode": "string: 'audit' | 'draft' | 'production'",
  "parameters": {
    "target_url": "string (optional)",
    "audit_depth": "integer (1-5)"
  }
}
```

## Telemetry `_run.json` Schema
Standardized telemetry record emitted by all 741 workflows:

```json
{
  "workflow_id": "template-workflow",
  "client": "ClientName",
  "date": "YYYY-MM-DD",
  "timestamp_utc": "ISO-8601 string",
  "status": "completed | failed | in_progress",
  "mode": "audit | production",
  "approved": false,
  "artifacts": {
    "output_json": "path/to/output.json",
    "report_md": "path/to/report.md"
  },
  "metrics": {
    "items_analyzed": 10,
    "validation_score": 100.0
  },
  "error": null
}
```
