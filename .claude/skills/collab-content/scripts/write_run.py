#!/usr/bin/env python3
"""
Standard 741 Telemetry Emitter for Co-Marketing & Backlink Collaboration Workflow (scripts/write_run.py).
Records run metadata, checkpoint transitions, and lint results in _run.json.
"""

import sys
import os
import json
from datetime import datetime, timezone

def emit_run(client, partner_slug, status, checkpoint, details=None):
    base_dir = f"00_project/assets/{client}/collab/{partner_slug}"
    os.makedirs(base_dir, exist_ok=True)
    run_file = os.path.join(base_dir, "_run.json")
    
    payload = {
        "workflow": "collab-content",
        "client": client,
        "partner": partner_slug,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "status": status,
        "checkpoint": checkpoint,
        "details": details or {}
    }
    
    with open(run_file, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
        
    print(f"Recorded telemetry in {run_file}")
    return run_file

def main():
    if len(sys.argv) < 5:
        print("Usage: python3 write_run.py <client> <partner-slug> <status> <checkpoint> [details_json]")
        sys.exit(1)
        
    client = sys.argv[1]
    partner_slug = sys.argv[2]
    status = sys.argv[3]
    checkpoint = sys.argv[4]
    
    details = {}
    if len(sys.argv) >= 6:
        try:
            details = json.loads(sys.argv[5])
        except Exception:
            details = {"raw": sys.argv[5]}
            
    emit_run(client, partner_slug, status, checkpoint, details)

if __name__ == "__main__":
    main()
