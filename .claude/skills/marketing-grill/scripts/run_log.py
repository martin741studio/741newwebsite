#!/usr/bin/env python3
"""Write _run.json telemetry (registry schema, 00_project/workflow-registry/README.md).

Usage:
  run_log.py <out_dir> <checkpoint> <status> [--result <path>] ["note"]

checkpoint: read_phase | round1 | round2 | round3 | round4 | playbook_written |
            checks_passed | delivered
status:     ok | blocked | rejected
The registry status is derived: delivered+ok -> "fertig", else "in Arbeit".
Events are appended under "events".
"""
import json
import os
import sys
import datetime

WORKFLOW = 'marketing-grill'


def main(argv):
    if len(argv) < 3:
        sys.exit(__doc__)
    out_dir, checkpoint, status = argv[0], argv[1], argv[2]
    rest = argv[3:]
    opts = {'--result': None}
    for k in list(opts):
        if k in rest:
            i = rest.index(k)
            opts[k] = rest[i + 1]
            del rest[i:i + 2]
    note = rest[0] if rest else ''
    os.makedirs(out_dir, exist_ok=True)
    p = os.path.join(out_dir, '_run.json')
    data = {}
    if os.path.exists(p):
        with open(p) as f:
            data = json.load(f)
    events = data.get('events', [])
    events.append({'checkpoint': checkpoint, 'status': status, 'note': note,
                    'at': datetime.datetime.now().isoformat(timespec='seconds')})
    reg_status = 'fertig' if checkpoint == 'delivered' and status == 'ok' else 'in Arbeit'
    data.update({
        'client': '741studio', 'workflow': WORKFLOW, 'status': reg_status,
        'last_run': datetime.date.today().isoformat(),
        'result': opts['--result'] or data.get('result', ''),
        'note': note or data.get('note', ''),
        'events': events,
    })
    with open(p, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write('\n')
    print(f'logged {checkpoint}={status} status="{reg_status}" -> {p}')


if __name__ == '__main__':
    main(sys.argv[1:])
