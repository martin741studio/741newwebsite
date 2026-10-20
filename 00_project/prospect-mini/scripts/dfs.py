#!/usr/bin/env python3
"""Prospect mini workflow: one DataForSEO call with cost ledger and cap.

Usage: dfs.py <prospect_dir> <endpoint> <payload.json|inline-json> <out_name> [cap_usd=0.30]
Example: dfs.py prospects/x keywords_data/google_ads/search_volume/live '[{"keywords":["a"],"location_code":2276}]' volumes

Writes evidence/dfs-<out_name>.json and appends to cost_ledger.jsonl. Stops before the call if the ledger sum >= cap.
A task status other than 20000 prints "TASK FAILED ..." to stderr and goes into the ledger as task_status.
Credentials: .secrets/dataforseo.env (DATAFORSEO_LOGIN / DATAFORSEO_PASSWORD). Never printed.
"""
import base64, datetime, json, os, sys, urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))


def creds():
    env = {}
    for l in open(os.path.join(ROOT, '.secrets', 'dataforseo.env')):
        if '=' in l and not l.startswith('#'):
            k, v = l.strip().split('=', 1); env[k] = v.strip().strip('"')
    return env['DATAFORSEO_LOGIN'], env['DATAFORSEO_PASSWORD']


def spent(pdir):
    p = os.path.join(pdir, 'cost_ledger.jsonl')
    if not os.path.exists(p): return 0.0
    return sum(json.loads(l).get('usd', 0) for l in open(p) if l.strip())


def task_check(d):
    """Return the first task's status code; print a clear stderr line when it is not 20000."""
    t = (d.get('tasks') or [{}])[0]
    code = t.get('status_code')
    if code != 20000:
        print(f"TASK FAILED {code} {t.get('status_message')}: retry once, then skip and note it", file=sys.stderr)
    return code


def call(pdir, endpoint, payload, out_name, cap=0.30):
    if spent(pdir) >= cap:
        raise SystemExit(f'cap reached: {spent(pdir):.4f} >= {cap}')
    lg, pw = creds()
    req = urllib.request.Request('https://api.dataforseo.com/v3/' + endpoint.strip('/'), json.dumps(payload).encode(),
                                 {'Authorization': 'Basic ' + base64.b64encode(f'{lg}:{pw}'.encode()).decode(), 'Content-Type': 'application/json'})
    d = json.loads(urllib.request.urlopen(req, timeout=180).read())
    code = task_check(d)
    os.makedirs(os.path.join(pdir, 'evidence'), exist_ok=True)
    json.dump(d, open(os.path.join(pdir, 'evidence', f'dfs-{out_name}.json'), 'w'), ensure_ascii=False, indent=1)
    with open(os.path.join(pdir, 'cost_ledger.jsonl'), 'a') as f:
        f.write(json.dumps({'at': datetime.datetime.now().isoformat(timespec='seconds'), 'tool': 'dataforseo', 'endpoint': endpoint,
                            'out': out_name, 'usd': d.get('cost', 0), 'status': d.get('status_code'), 'task_status': code}) + '\n')
    return d


if __name__ == '__main__':
    pdir, ep, pl, out = sys.argv[1:5]
    cap = float(sys.argv[5]) if len(sys.argv) > 5 else 0.30
    payload = json.load(open(pl)) if os.path.exists(pl) else json.loads(pl)
    d = call(pdir, ep, payload, out, cap)
    t = (d.get('tasks') or [{}])[0]
    print(json.dumps({'status': d.get('status_code'), 'msg': d.get('status_message'), 'cost': d.get('cost'),
                      'task_status': t.get('status_code'), 'task_msg': t.get('status_message'), 'spent_total': round(spent(pdir), 4)}))
