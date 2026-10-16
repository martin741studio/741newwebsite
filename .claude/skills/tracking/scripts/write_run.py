#!/usr/bin/env python3
"""741 Standardized Telemetry Writer (STE).

Writes standard _run.json telemetry records for the tracking workflow.

Usage:
  python3 write_run.py --client <client> --checkpoint <cp1|cp2|install|weekly|quarter> --status <passed|failed> [--metrics <json>]
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone

ROOT = "/Users/martindrendel/741website"

def write_telemetry(client, checkpoint, status, metrics=None, evidence_file=None, summary=""):
    today = datetime.now().strftime("%Y-%m-%d")
    out_dir = os.path.join(ROOT, "00_project", "assets", client, "tracking", today)
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "_run.json")

    record = {
        "client_id": client,
        "workflow_id": "tracking",
        "checkpoint": checkpoint,
        "status": status,
        "mode": "production",
        "metrics": metrics or {},
        "evidence_file": evidence_file or f"00_project/assets/{client}/tracking/{today}/weekly-card.md",
        "result_summary": summary or f"Tracking checkpoint {checkpoint} evaluated with status {status}.",
        "error_signal": None if status == "passed" else "Alert flags detected",
        "updated_at": datetime.now(timezone.utc).isoformat()
    }

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(record, f, indent=2, ensure_ascii=False)

    print(f"Telemetry written to {out_file}")
    return out_file

def main():
    parser = argparse.ArgumentParser(description="741 Telemetry Writer")
    parser.add_argument("--client", required=True, help="Client identifier")
    parser.add_argument("--checkpoint", required=True, help="Checkpoint name")
    parser.add_argument("--status", default="passed", help="Execution status")
    parser.add_argument("--evidence", help="Evidence file path")
    parser.add_argument("--summary", help="Short summary note")
    args = parser.parse_args()

    write_telemetry(args.client, args.checkpoint, args.status, evidence_file=args.evidence, summary=args.summary)

if __name__ == "__main__":
    main()
