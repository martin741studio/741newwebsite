#!/usr/bin/env python3
"""Write _run.json telemetry for a personal-posts run (workflow-creation-workflow.md
5.3a: every skill run writes status at each checkpoint and at completion).

Usage:
  run_log.py write <checkpoint> <status> ["note"]

checkpoint: draft | verified | martin_go | delivered
status: ok | blocked | rejected
"""
import json, os, sys, datetime

ROOT = '/Users/martindrendel/741website'


def path_for_today():
    day = datetime.date.today().isoformat()
    d = os.path.join(ROOT, '00_project', 'assets', '741studio', 'personal-posts', day)
    os.makedirs(d, exist_ok=True)
    return os.path.join(d, '_run.json')


def write(checkpoint, status, note):
    p = path_for_today()
    events = []
    if os.path.exists(p):
        with open(p) as f:
            events = json.load(f).get('events', [])
    events.append({
        'checkpoint': checkpoint, 'status': status, 'note': note or '',
        'at': datetime.datetime.now().isoformat(timespec='seconds'),
    })
    with open(p, 'w') as f:
        json.dump({'workflow': 'personal-posts', 'events': events}, f, indent=2)
        f.write('\n')
    print(f'logged {checkpoint}={status} -> {p}')


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) < 3 or args[0] != 'write':
        sys.exit(__doc__)
    checkpoint, status = args[1], args[2]
    note = args[3] if len(args) > 3 else ''
    write(checkpoint, status, note)
