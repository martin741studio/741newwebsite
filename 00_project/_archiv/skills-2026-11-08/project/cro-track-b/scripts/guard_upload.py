#!/usr/bin/env python3
"""PreToolUse hook for Bash. Asks for confirmation before any command that uploads files from a CRO run
(prototype, 06-gpt-assets, /cro-b/, /cro/ folders) to a server.
Reason: prototypes stay local unless Martin asks.
It returns 'ask' so Martin can explicitly confirm."""
import sys, json, re
try: d = json.load(sys.stdin)
except Exception: sys.exit(0)
if d.get('tool_name') != 'Bash': sys.exit(0)
cmd = (d.get('tool_input') or {}).get('command','')
uploads = re.search(r'(\blftp\b|\bsftp\b|\bscp\b|\brsync\b[^|;]*@|curl[^|;]*(-T\b|--upload-file|ftp://|ftps://)|ftplib|\bncftp)', cmd)
cro = re.search(r'(/cro-b/|/cro/|07-prototype|assets/[a-z0-9_-]+/cro)', cmd)
if uploads and cro:
    print(json.dumps({"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"ask",
      "permissionDecisionReason":"CRO Track B prototypes stay local unless Martin asked for an upload. Confirm that Martin asked for this upload."}}))
sys.exit(0)
