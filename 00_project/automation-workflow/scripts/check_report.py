#!/usr/bin/env python3
"""Test gate for the 741 Automation Build workflow (DRAFT).

Usage: check_report.py <run_dir> [--json]
Exit 0 = the test report passes. Exit 1 = it does not (the failures are listed).

Rules (from Martin's answers, 2026-10-11):
- test-report.json exists and parses.
- At least one end-to-end case passed with a TEST record, a record ID and the fields read back.
- flow_class "messages" or "crm": error, idempotency and alert cases are mandatory and must pass.
- No case failed. A skipped case needs a reason, and mandatory types cannot be skipped.
- Every case has evidence files, and every file exists.
- A fresh verifier subagent gave "pass" after the last test case ran.
"""
import datetime, json, os, sys

MANDATORY_EXTRA = ('error', 'idempotency', 'alert')
TYPES = ('e2e', 'error', 'idempotency', 'alert', 'role', 'other')


def ts(x):
    try:
        t = datetime.datetime.fromisoformat(str(x).replace('Z', '+00:00'))
        return t if t.tzinfo else t.replace(tzinfo=datetime.timezone.utc)
    except Exception:
        return None


def check(run_dir):
    f = []
    p = os.path.join(run_dir, 'test-report.json')
    if not os.path.exists(p):
        return ['test-report.json is missing']
    try:
        r = json.load(open(p, encoding='utf-8'))
    except Exception as e:
        return [f'test-report.json does not parse: {e}']
    cases = r.get('cases') or []
    if not cases:
        return ['no test cases in the report']
    flow = r.get('flow_class')
    if flow not in ('messages', 'crm', 'internal'):
        f.append('flow_class must be messages, crm or internal')
    by_type = {}
    last_run = None
    for c in cases:
        cid = c.get('id', '?')
        t = c.get('type')
        if t not in TYPES:
            f.append(f'{cid}: unknown type {t}')
        st = c.get('status')
        if st not in ('pass', 'fail', 'skip'):
            f.append(f'{cid}: status must be pass, fail or skip')
        if st == 'fail':
            f.append(f'{cid}: failed')
        if st == 'skip':
            if not (c.get('skip_reason') or '').strip():
                f.append(f'{cid}: skipped without a reason')
            if t == 'e2e' or (flow in ('messages', 'crm') and t in MANDATORY_EXTRA):
                f.append(f'{cid}: mandatory type {t} cannot be skipped')
        if st == 'pass':
            by_type.setdefault(t, []).append(c)
            ev = c.get('evidence') or []
            if not ev:
                f.append(f'{cid}: no evidence files')
            for e in ev:
                if not os.path.exists(os.path.join(run_dir, e)):
                    f.append(f'{cid}: evidence file missing: {e}')
            ran = ts(c.get('ran_at'))
            if not ran:
                f.append(f'{cid}: ran_at missing or not ISO time')
            elif last_run is None or ran > last_run:
                last_run = ran
    e2e = [c for c in by_type.get('e2e', []) if (c.get('readback') or {}).get('record_ids')
           and (c.get('readback') or {}).get('fields_checked') and (c.get('test_marker') or '').strip()]
    if not e2e:
        f.append('no passed e2e case with test_marker, readback.record_ids and readback.fields_checked')
    if flow in ('messages', 'crm'):
        for t in MANDATORY_EXTRA:
            if not by_type.get(t):
                f.append(f'flow_class {flow} needs a passed {t} case')
    v = r.get('verifier') or {}
    if v.get('verdict') != 'pass':
        f.append('verifier verdict is not "pass"')
    if 'subagent' not in (v.get('by') or ''):
        f.append('verifier.by must name the fresh verifier subagent')
    vt = ts(v.get('at'))
    if not vt:
        f.append('verifier.at missing')
    elif last_run and vt < last_run:
        f.append('verifier ran before the last test case; run the verifier again')
    return f


def main():
    if len(sys.argv) < 2:
        sys.exit('usage: check_report.py <run_dir> [--json]')
    fails = check(sys.argv[1])
    if '--json' in sys.argv:
        print(json.dumps({'ok': not fails, 'failures': fails}, ensure_ascii=False))
    else:
        print('PASS' if not fails else 'FAIL\n- ' + '\n- '.join(fails))
    sys.exit(0 if not fails else 1)


if __name__ == '__main__':
    main()
