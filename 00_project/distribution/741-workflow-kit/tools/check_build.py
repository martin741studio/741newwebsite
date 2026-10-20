#!/usr/bin/env python3
"""741 Workflow Build Checker.

Validates that a workflow build passes all required steps and quality gates before deployment.
Tracks progress via build-checklist.json in the build directory.

Usage:
  check_build.py init <id> "<Workflow Name>"           Create workflow checklist
  check_build.py check <id> --gate cp1|cp2|install     Exit 1 if gate requirements are not met
  check_build.py status <id>                           Display step-by-step progress
  check_build.py done <id> <step> <evidence_path>      Mark a step complete with evidence
  check_build.py skip <id> <step> "<reason>"           Skip an optional step
"""

import json
import os
import sys
import argparse
from pathlib import Path

# Resolve ROOT dynamically (no hardcoded user paths)
SCRIPT_PATH = Path(__file__).resolve()
ROOT = os.environ.get("REPO_ROOT")
if not ROOT:
    # Attempt to locate repo root by searching upward for .git or 00_project
    current = SCRIPT_PATH.parent
    while current != current.parent:
        if (current / ".git").exists() or (current / "00_project").exists():
            ROOT = str(current)
            break
        current = current.parent
    if not ROOT:
        ROOT = str(SCRIPT_PATH.parent.parent)

BUILDS = os.path.join(ROOT, "00_project", "workflow-builds")

STEPS = [
    ("0.0", "Inputs confirmed via interactive 4-parameter contract (Job, Surface, Cadence, Limits)"),
    ("1.1", "Building block chosen with justification (Skill, Subagent, Hook, Routine, MCP)"),
    ("1.2", "Pattern library searched for existing solutions"),
    ("1.3", "Source freshness verified (< 3 months old)"),
    ("1.4", "Existing workspace assets checked for reuse"),
    ("1.5", "Research note documented"),
    ("2.1", "2-3 concrete use cases defined (trigger, steps, tools, deliverable)"),
    ("2.2", "3 test scenarios written BEFORE body (direct, paraphrase, negative)"),
    ("2.3", "One real task solved manually step-by-step; edge cases noted"),
    ("2.4", "Execution pipeline map defined with clear checkpoints"),
    ("2.5", "Degrees of freedom applied (scripts for math/APIs, heuristics for copy)"),
    ("2.6", "Checkpoint 1 (CP1 Gate): Design approved"),
    ("3.1", "Folder structured per standard template (SKILL.md, scripts/, references/, assets/)"),
    ("3.2", "Frontmatter contract: WHAT + WHEN + negative trigger (NOT:)"),
    ("3.3", "Body formatted as sequential tickable checklist with critical rules on top"),
    ("3.4", "References linked one level deep; body under 500 lines"),
    ("3.5", "Automated verification step included at the end of the workflow body"),
    ("3.6", "House rules and no-hallucination standards applied"),
    ("3.7", "Unattended execution rules applied (if running scheduled)"),
    ("4.1", "Trigger tests verified (direct, paraphrase, negative rejection)"),
    ("4.2", "Functional end-to-end test passed in a clean session"),
    ("4.3", "Baseline comparison recorded (with vs without workflow)"),
    ("4.4", "Tool evaluation or prompt audit completed"),
    ("4.5", "Scorecard score >= 80 % with zero 0s in Fit or Verification"),
    ("5.1", "Checkpoint 2 (CP2 Gate): Final release approval"),
    ("5.2", "Files committed to Git repository"),
    ("5.3a", "Telemetry standard configured (emits _run.json)"),
    ("5.3b", "Brand guide applied to client-facing deliverables"),
    ("5.3c", "Documentation and memory index updated"),
    ("5.4", "Scheduled run tested manually if cron/routine"),
]

OPTIONAL = {"3.7", "4.4", "5.3b", "5.4"}

GATES = {
    "cp1": ["0.0", "1.1", "1.2", "1.3", "1.4", "1.5", "2.1", "2.2", "2.3", "2.4", "2.5"],
    "cp2": ["2.6", "3.1", "3.2", "3.3", "3.4", "3.5", "3.6", "3.7", "4.1", "4.2", "4.3", "4.4", "4.5"],
    "install": ["5.1", "5.2", "5.3a", "5.3b", "5.3c", "5.4"],
}

def get_checklist_path(workflow_id: str) -> str:
    return os.path.join(BUILDS, workflow_id, "build-checklist.json")

def load_checklist(workflow_id: str) -> dict:
    path = get_checklist_path(workflow_id)
    if not os.path.exists(path):
        print(f"[ERROR] Checklist not found for workflow '{workflow_id}' at {path}")
        sys.exit(1)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_checklist(workflow_id: str, data: dict):
    path = get_checklist_path(workflow_id)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    temp_path = path + ".tmp"
    with open(temp_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(temp_path, path)

def resolve_evidence(path_str: str) -> str:
    if path_str.startswith("/") or path_str.startswith("http"):
        return path_str
    return os.path.join(ROOT, path_str)

def check_step(data: dict, step_id: str) -> tuple:
    step = data.get("steps", {}).get(step_id, {})
    status = step.get("status", "todo")

    if status == "skipped":
        if step_id in OPTIONAL and step.get("reason"):
            return True, f"Skipped (Optional): {step.get('reason')}"
        return False, f"Invalid skip: step {step_id} is required"

    if status != "done":
        return False, "Not completed"

    evidence = step.get("evidence", "")
    if not evidence:
        return False, "Marked done, but missing evidence path"

    if step_id == "0.0":
        ev_path = resolve_evidence(evidence)
        if not evidence.startswith("http") and (not os.path.exists(ev_path) or os.path.getsize(ev_path) == 0):
            return False, f"Evidence file missing or empty: {evidence}"
        try:
            content = open(ev_path, "r", encoding="utf-8", errors="ignore").read().lower()
            params = {
                "Job": any(k in content for k in ["job", "task", "goal", "objective"]),
                "Surface": any(k in content for k in ["surface", "runtime", "environment"]),
                "Cadence": any(k in content for k in ["cadence", "frequency", "schedule"]),
                "Limits": any(k in content for k in ["limit", "boundary", "hard limit"]),
            }
            missing = [k for k, v in params.items() if not v]
            if missing:
                return False, f"Evidence missing parameters: {', '.join(missing)}"
            return True, "Validated 4 parameters (Job, Surface, Cadence, Hard Limits)"
        except Exception as e:
            return False, f"Could not read evidence: {e}"

    return True, f"Completed with evidence: {evidence}"

def cmd_init(workflow_id: str, name: str):
    path = get_checklist_path(workflow_id)
    if os.path.exists(path):
        print(f"[WARN] Checklist already exists for '{workflow_id}'")
        return

    data = {
        "workflow_id": workflow_id,
        "name": name,
        "steps": {step_id: {"status": "todo", "label": label, "evidence": "", "notes": ""} for step_id, label in STEPS}
    }
    save_checklist(workflow_id, data)
    print(f"[OK] Initialized workflow checklist at: {path}")

def cmd_check(workflow_id: str, gate: str):
    if gate not in GATES:
        print(f"[ERROR] Unknown gate '{gate}'. Choices: {', '.join(GATES.keys())}")
        sys.exit(1)

    data = load_checklist(workflow_id)
    required_steps = GATES[gate]
    failures = []

    print(f"\n--- Checking Gate '{gate.upper()}' for Workflow '{workflow_id}' ---")
    for sid in required_steps:
        passed, msg = check_step(data, sid)
        status_symbol = "✓" if passed else "✗"
        print(f"[{status_symbol}] Step {sid}: {msg}")
        if not passed:
            failures.append((sid, msg))

    print("-" * 50)
    if failures:
        print(f"[GATE FAILED] {len(failures)} step(s) not satisfied:")
        for sid, msg in failures:
            print(f"  • Step {sid}: {msg}")
        sys.exit(1)
    else:
        print(f"[GATE PASSED] Gate '{gate.upper()}' satisfied. Proceed.\n")
        sys.exit(0)

def cmd_status(workflow_id: str):
    data = load_checklist(workflow_id)
    print(f"\nStatus for Workflow '{data.get('name', workflow_id)}' ({workflow_id}):")
    for sid, label in STEPS:
        step = data.get("steps", {}).get(sid, {})
        st = step.get("status", "todo")
        print(f"  [{st.upper():^7}] {sid}: {label}")

def cmd_done(workflow_id: str, step_id: str, evidence: str, note: str = ""):
    data = load_checklist(workflow_id)
    if step_id not in data.get("steps", {}):
        print(f"[ERROR] Step '{step_id}' does not exist.")
        sys.exit(1)

    data["steps"][step_id]["status"] = "done"
    data["steps"][step_id]["evidence"] = evidence
    if note:
        data["steps"][step_id]["notes"] = note
    save_checklist(workflow_id, data)
    print(f"[OK] Step {step_id} marked as DONE with evidence '{evidence}'.")

def main():
    parser = argparse.ArgumentParser(description="741 Workflow Build Checker")
    subparsers = parser.add_subparsers(dest="command")

    init_p = subparsers.add_parser("init")
    init_p.add_argument("id", help="Workflow ID (kebab-case)")
    init_p.add_argument("name", help="Human-readable workflow name")

    check_p = subparsers.add_parser("check")
    check_p.add_argument("id", help="Workflow ID")
    check_p.add_argument("--gate", required=True, choices=["cp1", "cp2", "install"], help="Target gate")

    status_p = subparsers.add_parser("status")
    status_p.add_argument("id", help="Workflow ID")

    done_p = subparsers.add_parser("done")
    done_p.add_argument("id", help="Workflow ID")
    done_p.add_argument("step", help="Step ID (e.g. 0.0, 1.1)")
    done_p.add_argument("evidence", help="Path to evidence file or link")
    done_p.add_argument("note", nargs="?", default="", help="Optional note")

    args = parser.parse_args()
    if args.command == "init":
        cmd_init(args.id, args.name)
    elif args.command == "check":
        cmd_check(args.id, args.gate)
    elif args.command == "status":
        cmd_status(args.id)
    elif args.command == "done":
        cmd_done(args.id, args.step, args.evidence, args.note)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
