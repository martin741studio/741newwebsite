#!/usr/bin/env python3
"""Deterministic Execution Core for Workflow Template.

Handles data intake, transformation, and output generation.
Rule R1.7 compliant: mathematical and file operations execute here,
keeping prompt context clean and token-efficient.
"""

import os
import sys
import json
import argparse
import datetime
from pathlib import Path

# Dynamic Path Resolution (Zero Hardcoded User Paths)
SCRIPT_DIR = Path(__file__).resolve().parent
WORKFLOW_ROOT = SCRIPT_DIR.parent

def run_workflow(client: str, mode: str, output_path: Path) -> dict:
    """Executes the deterministic business logic."""
    print(f"[INFO] Running workflow for client: '{client}' in mode: '{mode}'...")

    # Simulated deterministic data processing
    result_data = {
        "client": client,
        "mode": mode,
        "timestamp_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "status": "success",
        "metrics": {
            "processed_items": 12,
            "calculated_score": 94.0,
            "error_count": 0
        },
        "records": [
            {"id": "REC-01", "name": "Primary Record", "status": "verified"},
            {"id": "REC-02", "name": "Secondary Record", "status": "verified"}
        ]
    }

    # Ensure target output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result_data, f, indent=2, ensure_ascii=False)

    print(f"[OK] Deliverable generated at: {output_path}")
    return result_data

def emit_telemetry(client: str, mode: str, artifact_path: Path):
    """Emits standardized _run.json telemetry record."""
    today = datetime.date.today().isoformat()
    telemetry_dir = WORKFLOW_ROOT / "assets" / "runs" / client / today
    telemetry_dir.mkdir(parents=True, exist_ok=True)
    telemetry_file = telemetry_dir / "_run.json"

    telemetry = {
        "workflow_id": "template-workflow",
        "client": client,
        "date": today,
        "timestamp_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "status": "completed",
        "mode": mode,
        "approved": False,
        "artifact": str(artifact_path),
        "error": None
    }

    with open(telemetry_file, "w", encoding="utf-8") as f:
        json.dump(telemetry, f, indent=2, ensure_ascii=False)

    print(f"[OK] Telemetry recorded at: {telemetry_file}")

def main():
    parser = argparse.ArgumentParser(description="Deterministic Execution Core")
    parser.add_argument("--client", required=True, help="Target client name")
    parser.add_argument("--mode", default="audit", choices=["audit", "draft", "production"], help="Execution mode")
    parser.add_argument("--output", type=Path, default=None, help="Custom output path (optional)")

    args = parser.parse_args()

    default_output = WORKFLOW_ROOT / "assets" / "output" / f"{args.client}_deliverable.json"
    target_output = args.output if args.output else default_output

    try:
        run_workflow(client=args.client, mode=args.mode, output_path=target_output)
        emit_telemetry(client=args.client, mode=args.mode, artifact_path=target_output)
        sys.exit(0)
    except Exception as e:
        print(f"[ERROR] Execution failed: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
