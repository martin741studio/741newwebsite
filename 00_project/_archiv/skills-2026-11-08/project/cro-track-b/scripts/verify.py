#!/usr/bin/env python3
"""Verification script for CRO Track B (Design-Intense Showpiece).
Usage: verify.py <cro-b-dir> [--proto 07-prototype]
Checks: required files per Track B step (B0 to B9), element pool presence,
concept and signature idea, motion checks, reduced-motion fallback, X-ray switch,
self-check total, visual check report line, and no method-source mentions."""

import sys, os, re, glob

def main():
    if len(sys.argv) < 2:
        print("Usage: verify.py <cro-b-dir> [--proto 07-prototype]")
        sys.exit(1)

    cro = os.path.abspath(sys.argv[1])
    proto = '07-prototype'
    if '--proto' in sys.argv:
        proto = sys.argv[sys.argv.index('--proto') + 1]

    res = []
    def ok(cond, name, info=''):
        res.append(('PASS' if cond else 'FAIL', name, info))
    def note(name, info=''):
        res.append(('INFO', name, info))

    def rd(p):
        path = os.path.join(cro, p)
        return open(path, encoding='utf-8', errors='ignore').read() if os.path.exists(path) else ''

    # 1. Required files
    req_files = [
        '00-lead-info.md',
        '_status.md',
        '00-brief-b/brief-b.md',
        '01-input/INVENTORY.md',
        '02-data/dataset.md',
        '02-data/brand.md',
        '02-data/elements-catalog.md',
        '00-element-pool/index.html',
        '05-gpt-design-doc/concept/concept.md',
        '05-gpt-design-doc/design-doc.md',
        os.path.join(proto, 'index.html'),
        os.path.join(proto, 'self-check.md'),
        os.path.join(proto, 'visual-check.md'),
        '08-handoff/handoff.md'
    ]

    for f in req_files:
        ok(os.path.exists(os.path.join(cro, f)), f'file {f}')

    # Check copy file (approved-copy.md or copy.md)
    has_copy = os.path.exists(os.path.join(cro, '04-copy', 'approved-copy.md')) or os.path.exists(os.path.join(cro, '04-copy', 'copy.md'))
    ok(has_copy, 'file 04-copy/approved-copy.md (or copy.md)')

    # Check element pool index
    pool_idx = rd('00-element-pool/index.html')
    ok('Element-Pool' in pool_idx or 'element-pool' in pool_idx.lower(), '00-element-pool/index.html is valid interactive pool')

    # Concept check
    concept = rd('05-gpt-design-doc/concept/concept.md')
    ok(bool(re.search(r'signature|idee|konzept|briefbogen', concept, re.I)), 'concept.md contains signature idea definition')

    # Prototype checks
    idx_path = os.path.join(cro, proto, 'index.html')
    if os.path.exists(idx_path):
        h = open(idx_path, encoding='utf-8', errors='ignore').read()
        ok('noindex' in h, 'robots noindex present while preview')
        ok('prefers-reduced-motion' in h, 'prefers-reduced-motion media query present in CSS')
        ok('xray' in h.lower() or 'data-layer' in h.lower() or 'key === \'x\'' in h or 'toggle' in h.lower(), 'X-ray inspection switch or layer tag present')

    # Visual check report line
    vc = rd(os.path.join(proto, 'visual-check.md'))
    ok(bool(re.search(r'Visual check done in Chrome, \d+ items checked, \d+ fixed, \d+ open', vc)), 'visual-check.md has the report line')

    # Self-check score
    sc = rd(os.path.join(proto, 'self-check.md'))
    ok(bool(re.search(r'\d+\s*(?:von|/)\s*\d+', sc)), 'self-check.md has a total score')

    # Method sources forbidden
    bad_sources = ['hormozi', 'backlinko', 'gotch', 'diggity', 'brian dean']
    hits = []
    for f in ['08-handoff/handoff.md', os.path.join(proto, 'index.html')]:
        t = rd(f).lower()
        hits += [f'{f}:{w}' for w in bad_sources if w in t]
    ok(not hits, 'no method-source names in client-facing deliverables', ', '.join(hits))

    # Print results
    fails = 0
    print(f"\n--- CRO Track B Verification Report: {os.path.basename(cro)} ---")
    for status, name, info in res:
        symbol = '✓' if status == 'PASS' else ('ℹ' if status == 'INFO' else '✗')
        extra = f" ({info})" if info else ""
        print(f"[{status}] {symbol} {name}{extra}")
        if status == 'FAIL':
            fails += 1

    print(f"\nTotal: {len(res)} checks, {fails} failures.")
    if fails > 0:
        sys.exit(1)
    print("VERIFICATION SUCCESSFUL (Track B rules satisfied)")
    sys.exit(0)

if __name__ == '__main__':
    main()
