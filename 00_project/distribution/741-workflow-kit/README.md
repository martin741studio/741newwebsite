# 741 Workflow Starter Kit
**The Definitive Architecture, Rules, and Boilerplate for Building Cybernetic Workflows**

---

## What Is This?
This kit contains the complete specifications, rules, quality gates, and code boilerplate for designing, implementing, and running autonomous, reliable AI workflows inside modern agent environments (Claude Code, Antigravity IDE, Cursor, CLI).

Every workflow is designed as a **cybernetic regulation loop**:
- **Strict Boundaries:** Fails fast before running if inputs, environments, or parameters are invalid.
- **Rule R1.7 Separation:** Fragile logic (maths, APIs, file transforms) lives in isolated Python scripts. Qualitative guidance (strategy, writing, critique) lives in Markdown prompts (`SKILL.md`).
- **Portability First:** Zero hardcoded usernames (`/Users/...`), zero secret leaks, and platform-independent execution.

---

## Quick Start: Building a Workflow in 5 Minutes

### 1. Copy the Template
Copy the `template/` folder into your repository's skills directory:
```bash
cp -r template/ .claude/skills/my-new-workflow/
cd .claude/skills/my-new-workflow/
```

### 2. Configure Environment
Copy `.env.example` to `.env` and set your variables:
```bash
cp .env.example .env
```

### 3. Verify Environment
Run the smoke test to ensure Python version, packages, and environment variables are satisfied:
```bash
python3 scripts/verify_env.py
```

### 4. Customize Logic
- Modify `SKILL.md` with your specific trigger keywords, sequential checklist, and output structure.
- Implement data manipulation, API calls, or parsing in `scripts/run.py`.
- Define output validation criteria in `scripts/validate.py`.

---

## Kit Contents

```text
741-workflow-kit/
├── README.md               # This master onboarding guide
├── docs/
│   ├── 01_architecture.md  # The 5-layer cybernetic meta-architecture & gates
│   ├── 02_rules.md         # The complete 741 workflow rules (R0–R9)
│   ├── 03_patterns.md      # Pattern catalog (primitives, shapes, loops)
│   └── 04_scorecard.md     # Pre-ship quality scorecard (≥ 80 % pass mark)
├── tools/
│   └── check_build.py      # Automated CP1 / CP2 gate checking script
└── template/               # Production-ready starter workflow
    ├── SKILL.md            # Workflow instructions & execution checklist
    ├── requirements.txt    # Pinned Python dependencies
    ├── .env.example        # Clean environment variable template
    ├── scripts/
    │   ├── verify_env.py   # Pre-flight environment & credential validator
    │   ├── run.py          # Main execution script (deterministic core)
    │   └── validate.py     # Automated output validator
    ├── references/
    │   └── schema.md       # Data schema documentation
    └── assets/
        └── sample_output.json # Sample validated deliverable
```

---

## The 7 Portability Rules (Multi-Laptop / Multi-Account Standard)

To ensure this workflow runs seamlessly on **any other laptop, cloud instance, or colleague's account**:

1. **Zero Hardcoded Paths:** Never use absolute paths like `/Users/<name>/` or `C:\Users\<name>\`. Always resolve paths dynamically using `Path(__file__).resolve()` or relative to repo root.
2. **Repository-Bound:** Always commit workflows into the repository (`.claude/skills/<id>/` or `.agents/skills/<id>/`). Never store shared workflows only in personal local folders (`~/.claude/`).
3. **No Secrets in Code:** Never embed API keys, database credentials, or tokens in scripts or prompts. Use `.env` and provide a clean `.env.example`.
4. **Cross-Platform OS:** Avoid OS-specific shell commands like `pbcopy` or `open`. Use cross-platform Python libraries.
5. **Deterministic Dependencies:** List all third-party dependencies in `requirements.txt`. Prefer Python standard library modules where possible.
6. **Explicit Tool & MCP Requirements:** If an MCP server is needed, declare it in `SKILL.md` with a ready-to-paste `.mcp.json` snippet.
7. **Smoke-Test Included:** Always provide `scripts/verify_env.py` so a new user can verify their local setup in 5 seconds.
