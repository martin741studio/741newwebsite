#!/usr/bin/env python3
"""741 Client Roadmap - Universal Telemetry Emitter.

Writes standardized _run.json to 00_project/assets/<client>/roadmap/<date>/_run.json
"""
import sys
import os
import json
import datetime

ROOT = "/Users/martindrendel/741website"
ASSETS_DIR = os.path.join(ROOT, "00_project", "assets")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Emit roadmap telemetry _run.json")
    parser.add_argument("--client", required=True, help="Client folder name")
    parser.add_argument("--checkpoint", default="cp1", help="Checkpoint ID (e.g. cp1, M1, M2)")
    parser.add_argument("--status", default="passed", choices=["passed", "failed", "blocked"])
    parser.add_argument("--summary", default="Milestone updated", help="Brief result summary")
    args = parser.parse_args()
    
    today = datetime.date.today().isoformat()
    client_dir = os.path.join(ASSETS_DIR, args.client)
    if not os.path.isdir(client_dir):
        os.makedirs(client_dir, exist_ok=True)
        
    out_dir = os.path.join(client_dir, "roadmap", today)
    os.makedirs(out_dir, exist_ok=True)
    
    run_data = {
        "client_id": args.client,
        "workflow_id": "roadmap",
        "checkpoint": args.checkpoint,
        "status": args.status,
        "mode": "production",
        "result_summary": args.summary,
        "error_signal": None if args.status == "passed" else "Task blocked or failed",
        "updated_at": datetime.datetime.now(datetime.timezone.utc).isoformat()
    }
    
    run_file = os.path.join(out_dir, "_run.json")
    with open(run_file, "w", encoding="utf-8") as f:
        json.dump(run_data, f, indent=2, ensure_ascii=False)
        
    print(f"Emitted telemetry: {run_file}")

if __name__ == "__main__":
    main()
