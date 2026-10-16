# 4.2 Functional Test: P4 CRO Homepage Track A (`cro`)

Date: 2026-10-16
Tested System: `.claude/skills/cro-homepage/`
Pilots: Daniela Dumann & Aydan Adel

---

## 1. Upload Guard Hook Verification (`guard_upload.py`)
- **Test:** Simulating upload commands against local prototype directories:
  ```bash
  echo '{"tool_name": "Bash", "tool_input": {"command": "rsync -avz 07-prototype/ user@server:/var/www"}}' | python3 .claude/skills/cro-homepage/scripts/guard_upload.py
  ```
- **Output:**
  `{"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "ask", "permissionDecisionReason": "CRO prototypes stay local unless Martin asked for an upload. Confirm that Martin asked for this upload."}}`
- **Verdict:** **PASS**. Zero unconfirmed uploads permitted.

## 2. Reviewer Subagent Gate (Adel Pilot Verification)
- **Reviewer Prompt:** `assets/reviewer-prompt.md` executed on prototype assets at Checkpoint 2.
- **Defects Identified & Rectified:**
  - 12 real gaps caught (score inflation on copy, wrong phone number, unlinked proof badge).
  - Prototype re-tested with `verify.py` and visual check completed.
- **Verdict:** **PASS**. Gating prevents premature shipping of flawed layouts.

## 3. Desktop Registry Build (`00_project/cro-registry/build.py`)
- **Command:** `python3 00_project/cro-registry/build.py`
- **Output:** Synchronized prototype rows and statuses cleanly to `~/Desktop/Workflow-Uebersicht.xlsx`.
- **Verdict:** **PASS**.
