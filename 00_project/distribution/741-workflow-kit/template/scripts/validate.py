#!/usr/bin/env python3
"""Automated Output Validation Script.

Verifies generated outputs against required schema fields, data types,
and quality thresholds before human presentation or deployment.
"""

import sys
import json
import argparse
from pathlib import Path

REQUIRED_ROOT_KEYS = ["client", "mode", "timestamp_utc", "status", "metrics"]
REQUIRED_METRIC_KEYS = ["processed_items", "calculated_score", "error_count"]

def validate_deliverable(target_file: Path) -> bool:
    if not target_file.exists():
        print(f"[FAIL] Output file does not exist: {target_file}")
        return False

    try:
        with open(target_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"[FAIL] Invalid JSON syntax: {e}")
        return False

    # Check root keys
    missing_root = [k for k in REQUIRED_ROOT_KEYS if k not in data]
    if missing_root:
        print(f"[FAIL] Missing required root keys: {', '.join(missing_root)}")
        return False

    # Check metrics
    metrics = data.get("metrics", {})
    missing_metrics = [k for k in REQUIRED_METRIC_KEYS if k not in metrics]
    if missing_metrics:
        print(f"[FAIL] Missing required metric keys: {', '.join(missing_metrics)}")
        return False

    # Quality threshold check
    score = metrics.get("calculated_score", 0)
    if score < 80.0:
        print(f"[FAIL] Calculated score {score}% is below the 80% quality threshold.")
        return False

    errors = metrics.get("error_count", 0)
    if errors > 0:
        print(f"[FAIL] Deliverable reports {errors} error(s). Must be zero.")
        return False

    print(f"[OK] Deliverable validation passed for: {target_file.name}")
    print(f"     Quality Score: {score}% | Status: {data.get('status')}")
    return True

def main():
    parser = argparse.ArgumentParser(description="Output Quality Validator")
    parser.add_argument("--file", type=Path, required=True, help="Path to JSON deliverable to validate")

    args = parser.parse_args()

    if validate_deliverable(args.file):
        print("[SUCCESS] Validation PASSED. Deliverable ready for review.")
        sys.exit(0)
    else:
        print("[ERROR] Validation FAILED. Correct issues before proceeding.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
