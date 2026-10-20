#!/usr/bin/env python3
"""UserPromptSubmit hook. When Martin's message looks like an approval, remind Claude to record it in the workflow registry.
It adds one short context line. It never blocks and never changes the message."""
import sys, json, re
try: d = json.load(sys.stdin)
except Exception: sys.exit(0)
t = (d.get('prompt') or '').lower()
if re.search(r'(freigegeben|freigabe erteilt|abgesegnet|absegnen|genehmigt|\bapproved?\b|ist so freigegeben|confirmed and approved|go für den workflow)', t):
    msg = ("Registry reminder: if this message approves a workflow result or a workflow for a client, record it in the same turn: "
           "python3 /Users/martindrendel/741website/00_project/workflow-registry/workflow_registry.py approve --client \"<name>\" --workflow <id> "
           "(CRO page: approve --cro-id <id>). Workflow ids: cro, unburning, phone, audit, pool, citations, backlink, cro_b. "
           "If it is unclear what was approved, ask one short question. Then tell Martin the sheet was updated.")
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": msg}}))
sys.exit(0)
