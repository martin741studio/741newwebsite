#!/usr/bin/env python3
"""sales-call-prep: the one hard gate before a brief is ever shown to Martin.

Usage: verify_brief.py <brief.md> --claims <booking/claims.json>

Runs two checks and prints RESULT: PASS only when both hold:
  1. German AI-slop check, scored with the real claims file so a number from
     the booking folder is not flagged as "invented proof":
       python3 00_project/content-writing-skill/scripts/deslop_de.py <file> --claims <claims.json>
     must print "score 5/5".
  2. No outside methodology source is named anywhere in the file (internal
     research may name them; the brief Martin reads before the call never
     does, per memory no-method-sources-in-deliverables.md).

On FAIL, prints exactly what failed and why, then exits 1. Fix the file and
run again — never ship on anything but RESULT: PASS.
"""
import argparse, re, subprocess, sys, os

ROOT = '/Users/martindrendel/741website'
DESLOP = os.path.join(ROOT, '00_project', 'content-writing-skill', 'scripts', 'deslop_de.py')

OUTSIDE_NAMES = re.compile(
    r'hormozi|ramoszi|closer framework|diagnostic sale|\$100m|100 million (leads|money models)',
    re.I,
)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('brief')
    ap.add_argument('--claims', required=True)
    a = ap.parse_args()

    ok = True
    print(f'Checking {a.brief}')

    # 1. slop / claims check
    res = subprocess.run(
        [sys.executable, DESLOP, a.brief, '--claims', a.claims],
        capture_output=True, text=True,
    )
    out = (res.stdout + res.stderr).strip()
    print('--- deslop_de.py ---')
    print(out)
    if 'score 5/5' not in out:
        ok = False
        print('FAIL: slop/claims check did not reach 5/5.')

    # 2. outside method names
    text = open(a.brief, encoding='utf-8').read()
    hits = sorted(set(m.group(0) for m in OUTSIDE_NAMES.finditer(text)))
    if hits:
        ok = False
        print(f'FAIL: outside method source named in the brief: {hits}')
    else:
        print('OK: no outside method source named.')

    print('RESULT:', 'PASS' if ok else 'FAIL')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
