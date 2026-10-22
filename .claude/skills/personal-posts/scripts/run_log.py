#!/usr/bin/env python3
"""Write _run.json telemetry for a personal-posts run (workflow-creation-workflow.md
5.3a: every skill run writes status at each checkpoint and at completion). Covers
BOTH accounts in one daily file, each event tagged with its account so a business
run and a personal run on the same day stay distinguishable.

Usage:
  run_log.py write <checkpoint> <status> --account personal|business ["note"]

checkpoint: draft | angle_picked | verified | martin_go | delivered
status: ok | blocked | rejected
"""
import json, os, sys, datetime

ROOT = '/Users/martindrendel/741website'


def path_for_today():
    day = datetime.date.today().isoformat()
    d = os.path.join(ROOT, '00_project', 'assets', '741studio', 'personal-posts', day)
    os.makedirs(d, exist_ok=True)
    return os.path.join(d, '_run.json')


def write(checkpoint, status, account, note):
    p = path_for_today()
    events = []
    if os.path.exists(p):
        with open(p) as f:
            events = json.load(f).get('events', [])
    events.append({
        'checkpoint': checkpoint, 'status': status, 'account': account, 'note': note or '',
        'at': datetime.datetime.now().isoformat(timespec='seconds'),
    })
    with open(p, 'w') as f:
        json.dump({'workflow': 'personal-posts', 'events': events}, f, indent=2)
        f.write('\n')
    print(f'logged {checkpoint}={status} account={account} -> {p}')


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) < 3 or args[0] != 'write':
        sys.exit(__doc__)
    checkpoint, status, rest = args[1], args[2], args[3:]
    if '--account' not in rest:
        sys.exit('--account personal|business is required')
    i = rest.index('--account')
    account = rest[i + 1]
    if account not in ('personal', 'business'):
        sys.exit("--account must be 'personal' or 'business'")
    del rest[i:i + 2]
    note = rest[0] if rest else ''
    write(checkpoint, status, account, note)
