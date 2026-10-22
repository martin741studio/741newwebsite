#!/usr/bin/env python3
"""Verification gate for one or more platform drafts: slop lint + length check,
combined. Run this on EVERY platform version separately (length changes can
reintroduce a tell a longer version did not have — hand-run.md finding, 2026-10-22).

Usage:
  verify_draft.py <file>...

Exit 0 only when every file is 5/5 clean AND within its hard length limit.
Below 5/5: run `.claude/skills/slopmonster/tools/cleanse.sh <file>`, then re-run this.
"""
import os, subprocess, sys

ROOT = '/Users/martindrendel/741website'
DESLOP = os.path.join(ROOT, '.claude', 'skills', 'slopmonster', 'tools', 'deslop.py')
HERE = os.path.dirname(__file__)
CHECK_LENGTHS = os.path.join(HERE, 'check_lengths.py')


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


if __name__ == '__main__':
    files = sys.argv[1:]
    if not files:
        sys.exit(__doc__)
    all_ok = True
    for f in files:
        print(f'=== {f} ===')
        lint = run(['python3', DESLOP, f])
        print(lint.stdout.strip())
        if lint.returncode != 0:
            print(f'SLOP GATE FAILED on {f} -> run cleanse.sh, then re-run verify_draft.py')
            all_ok = False
        length = run(['python3', CHECK_LENGTHS, f])
        print(length.stdout.strip())
        if length.returncode != 0:
            all_ok = False
        print()
    sys.exit(0 if all_ok else 1)
