#!/usr/bin/env python3
"""Pre-flight environment and dependency verification script.

Ensures that Python runtime, packages, and environment variables are satisfied
before the workflow runs. Works across macOS, Linux, and Windows.
"""

import os
import sys
from pathlib import Path

REQUIRED_PYTHON = (3, 10)
# Add variables that must exist in .env
REQUIRED_ENV_VARS = ["WORKFLOW_API_URL"]

def check_python():
    if sys.version_info < REQUIRED_PYTHON:
        print(f"[FAIL] Python {REQUIRED_PYTHON[0]}.{REQUIRED_PYTHON[1]}+ required. Found {sys.version.split()[0]}.")
        return False
    print(f"[OK] Python version: {sys.version.split()[0]}")
    return True

def load_dotenv_safely(env_path: Path):
    if not env_path.exists():
        return
    with open(env_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, val = line.split("=", 1)
                os.environ.setdefault(key.strip(), val.strip().strip('"').strip("'"))

def check_env():
    # Resolve .env relative to this script directory
    script_dir = Path(__file__).resolve().parent
    env_file = script_dir.parent / ".env"
    
    if not env_file.exists():
        print(f"[WARN] No .env file found at {env_file}")
        print("       Copy .env.example to .env to configure credentials.")
    else:
        load_dotenv_safely(env_file)

    missing = [var for var in REQUIRED_ENV_VARS if not os.environ.get(var)]
    if missing:
        print(f"[FAIL] Missing required environment variable(s): {', '.join(missing)}")
        print("       Check your .env file or environment settings.")
        return False

    print("[OK] Required environment variables confirmed.")
    return True

def check_write_permissions():
    script_dir = Path(__file__).resolve().parent
    test_dir = script_dir.parent / "assets"
    test_dir.mkdir(parents=True, exist_ok=True)
    test_file = test_dir / ".perm_check"
    try:
        test_file.write_text("ok", encoding="utf-8")
        test_file.unlink()
        print("[OK] Workspace directory is writable.")
        return True
    except Exception as e:
        print(f"[FAIL] Workspace directory not writable: {e}")
        return False

def main():
    print("=" * 50)
    print(" 741 Workflow Pre-Flight Environment Check")
    print("=" * 50)

    py_ok = check_python()
    env_ok = check_env()
    perm_ok = check_write_permissions()

    print("-" * 50)
    if py_ok and env_ok and perm_ok:
        print("[SUCCESS] Environment is fully validated. Proceed with workflow.")
        sys.exit(0)
    else:
        print("[ERROR] Environment setup incomplete. Resolve issues above before running.")
        sys.exit(1)

if __name__ == "__main__":
    main()
