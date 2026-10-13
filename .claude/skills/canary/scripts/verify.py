#!/usr/bin/env python3
"""Verification step for the canary skill. Run after any change to the skill or the registry.
Fix until this prints ALL CHECKS PASSED before reporting "done" to Martin.
"""
import subprocess, sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
ROOT = SKILL.parents[2]

checks = []


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    return r.returncode, r.stdout + r.stderr


def check(name, ok, detail=""):
    checks.append((name, ok, detail))
    print(("OK  " if ok else "FAIL"), name, (f"— {detail}" if detail and not ok else ""))


def main():
    # 1. registry validates
    rc, out = run(["python3", str(SKILL / "scripts" / "registry.py"), "validate"])
    check("registry validates", rc == 0, out.strip())

    # 2. allowlist.py parses references/allowlist.md and both branches work
    rc1, _ = run(["python3", str(SKILL / "scripts" / "allowlist.py"), "check", "recheck"])
    rc2, _ = run(["python3", str(SKILL / "scripts" / "allowlist.py"), "check", "zapier-replay"])
    rc3, _ = run(["python3", str(SKILL / "scripts" / "allowlist.py"), "check", "pause-ads-campaign"])
    check("allowlist: no-go action allowed", rc1 == 0)
    check("allowlist: go-needed action allowed", rc2 == 0)
    check("allowlist: unlisted action rejected", rc3 == 1)

    # 3. alert.py env file exists (token saved) — do not print its contents
    env_file = ROOT / ".secrets" / "canary-telegram.env"
    check("Telegram bot token file exists", env_file.exists(), str(env_file))
    if env_file.exists():
        mode = oct(env_file.stat().st_mode)[-3:]
        check("Telegram bot token file is mode 600", mode == "600", f"mode={mode}")

    # 4. SKILL.md body under 500 lines, references one level deep
    skill_md = SKILL / "SKILL.md"
    check("SKILL.md exists", skill_md.exists())
    if skill_md.exists():
        lines = len(skill_md.read_text().splitlines())
        check("SKILL.md under 500 lines", lines < 500, f"{lines} lines")

    # 5. required reference files present
    for ref in ["check-catalogue.md", "allowlist.md", "runbooks.md", "zapier-manager-setup.md"]:
        p = SKILL / "references" / ref
        check(f"references/{ref} present", p.exists())

    # 6. incident/decision templates present
    check("incident-log template present", (SKILL / "assets" / "incident-log.template.md").exists())

    # 7. canaries.json has at least one live check (Marcel)
    rc, out = run(["python3", str(SKILL / "scripts" / "registry.py"), "list", "--status", "live"])
    check("at least one check is live", "(no matching" not in out, out.strip().splitlines()[0] if out.strip() else "")

    passed = all(ok for _, ok, _ in checks)
    print()
    print(f"{sum(1 for _,ok,_ in checks if ok)}/{len(checks)} checks passed")
    print("ALL CHECKS PASSED" if passed else "SOME CHECKS FAILED — fix before reporting done")
    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
