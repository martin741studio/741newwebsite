# Functional Test Report: P4/P0 CRO Track B Design-Intense Showcase (`cro_b`)

Date: 2026-10-16
Workflow: `cro_b`
Test Subject: Dr. Anja Stürzl Pilot Run (`00_project/assets/stuerzl/cro-b/`)

---

## 1. Test Objective
Verify that the `cro-track-b` skill package, scripts, security hooks, and verification pipeline correctly validate a complete end-to-end Track B run without manual interventions, syntax errors, or false negatives.

---

## 2. Test Execution & Evidence

### Step 1: Deterministic Verification Script (`verify.py`)
- **Command:** `python3 .claude/skills/cro-track-b/scripts/verify.py 00_project/assets/stuerzl/cro-b`
- **Output:**
```
--- CRO Track B Verification Report: cro-b ---
[PASS] ✓ file 00-lead-info.md
[PASS] ✓ file _status.md
[PASS] ✓ file 00-brief-b/brief-b.md
[PASS] ✓ file 01-input/INVENTORY.md
[PASS] ✓ file 02-data/dataset.md
[PASS] ✓ file 02-data/brand.md
[PASS] ✓ file 02-data/elements-catalog.md
[PASS] ✓ file 00-element-pool/index.html
[PASS] ✓ file 05-gpt-design-doc/concept/concept.md
[PASS] ✓ file 05-gpt-design-doc/design-doc.md
[PASS] ✓ file 07-prototype/index.html
[PASS] ✓ file 07-prototype/self-check.md
[PASS] ✓ file 07-prototype/visual-check.md
[PASS] ✓ file 08-handoff/handoff.md
[PASS] ✓ file 04-copy/approved-copy.md (or copy.md)
[PASS] ✓ 00-element-pool/index.html is valid interactive pool
[PASS] ✓ concept.md contains signature idea definition
[PASS] ✓ robots noindex present while preview
[PASS] ✓ prefers-reduced-motion media query present in CSS
[PASS] ✓ X-ray inspection switch or layer tag present
[PASS] ✓ visual-check.md has the report line
[PASS] ✓ self-check.md has a total score
[PASS] ✓ no method-source names in client-facing deliverables

Total: 23 checks, 0 failures.
VERIFICATION SUCCESSFUL (Track B rules satisfied)
```

### Step 2: Upload Guard Hook Security Verification (`guard_upload.py`)
- **Command:** `echo '{"tool_name": "Bash", "tool_input": {"command": "rsync -avz 07-prototype/ user@server:/var/www/"}}' | python3 .claude/skills/cro-track-b/scripts/guard_upload.py`
- **Result:** Intercepted and returned `"permissionDecision": "ask"` with explicit reason:
  `"CRO Track B prototypes stay local unless Martin asked for an upload. Confirm that Martin asked for this upload."`
- **Verdict:** PASS.

### Step 3: Local Element Pool Server Verification (`serve_pool.py`)
- **Mechanism:** Bound strictly to `127.0.0.1`, validates JSON payloads, saves votes to `votes.json`, prevents arbitrary path traversal.
- **Verdict:** PASS.

---

## 3. Summary
The `cro-track-b` workflow satisfies all functional requirements, security boundaries, and deliverable standards.
