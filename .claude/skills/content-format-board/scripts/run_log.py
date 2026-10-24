#!/usr/bin/env python3
"""Write _run.json telemetry (registry schema, 00_project/workflow-registry/README.md).

Usage:
  run_log.py <out_dir> <checkpoint> <status> --client "<Name>" [--result <path>] [--mode Echt|Trockenlauf] ["note"]

checkpoint: intake | questions | draft | verified | martin_go | delivered
status:     ok | blocked | rejected
The registry status is derived: delivered+ok -> "fertig, Freigabe offen", else "in Arbeit"
(or "Trockenlauf" when --mode Trockenlauf). Events are appended under "events".
"""
import json, os, sys, datetime

WORKFLOW = 'content-format-board'


def main(argv):
    if len(argv) < 3:
        sys.exit(__doc__)
    out_dir, checkpoint, status = argv[0], argv[1], argv[2]
    rest = argv[3:]
    opts = {'--client': None, '--result': None, '--mode': 'Echt'}
    for k in list(opts):
        if k in rest:
            i = rest.index(k)
            opts[k] = rest[i + 1]
            del rest[i:i + 2]
    note = rest[0] if rest else ''
    if not opts['--client']:
        sys.exit('--client "<Name>" is required')
    os.makedirs(out_dir, exist_ok=True)
    p = os.path.join(out_dir, '_run.json')
    data = {}
    if os.path.exists(p):
        with open(p) as f:
            data = json.load(f)
    events = data.get('events', [])
    events.append({'checkpoint': checkpoint, 'status': status, 'note': note,
                   'at': datetime.datetime.now().isoformat(timespec='seconds')})
    if opts['--mode'] == 'Trockenlauf':
        reg_status = 'Trockenlauf'
    elif checkpoint == 'delivered' and status == 'ok':
        reg_status = 'fertig, Freigabe offen'
    else:
        reg_status = 'in Arbeit'
    data.update({
        'client': opts['--client'], 'workflow': WORKFLOW, 'status': reg_status,
        'mode': opts['--mode'], 'last_run': datetime.date.today().isoformat(),
        'result': opts['--result'] or data.get('result', ''),
        'drive': data.get('drive', ''), 'note': note or data.get('note', ''),
        'events': events,
    })
    with open(p, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write('\n')
    print(f'logged {checkpoint}={status} status="{reg_status}" -> {p}')


if __name__ == '__main__':
    main(sys.argv[1:])
