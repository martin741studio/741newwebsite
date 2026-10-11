#!/usr/bin/env python3
"""Run folder and go requests for the 741 Automation Build workflow (DRAFT).

  init    --session S --client C --slug X [--mode Echt|Trockenlauf] [--root DIR] [--client-dir NAME]
  bind    --session S --run DIR
  phase   --run DIR --set PHASE
  request --run DIR --kind send|publish|write --tool REGEX --contains TEXT [--contains TEXT2] --target TEXT [--uses N]
  log     --run DIR --msg TEXT
  runjson --run DIR [--status S] [--result R] [--note N] [--drive URL]
  status  --run DIR

There is no "grant" command on purpose: only Martin's prompt "go A<n>" grants, through the prompt hook.
"""
import argparse, datetime, json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'hooks'))
import automation_lib as L

REPO = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
DEFAULT_ROOT = os.path.join(REPO, '00_project', 'assets')
SUBDIRS = ['evidence', 'snapshots']
FILES = {'changelog.md': '# Change log\n\nOne line per change: time, system, object, before → after, evidence file.\n\n'}


def slugify(s):
    s = s.lower()
    for a, b in (('ä', 'ae'), ('ö', 'oe'), ('ü', 'ue'), ('ß', 'ss')):
        s = s.replace(a, b)
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')


def today():
    return datetime.date.today().isoformat()


def write_runjson(run_dir, **kw):
    p = os.path.join(run_dir, '_run.json')
    d = L.jload(p, {})
    d.update({k: v for k, v in kw.items() if v is not None})
    d['last_run'] = today()
    L.jsave(p, d)


def bind(session_id, run_dir):
    s = L.session(session_id) or {'registered_at': L.now()}
    s['run_dir'] = os.path.abspath(run_dir)
    L.save_session(session_id, s)


def latest_unbound_session(max_minutes=30):
    best = None
    for sid, s in L.sessions().items():
        if s.get('run_dir'):
            continue
        try:
            t = datetime.datetime.fromisoformat(s['registered_at'])
        except Exception:
            continue
        age = (datetime.datetime.now(datetime.timezone.utc) - t).total_seconds() / 60
        if age <= max_minutes and (best is None or t > best[1]):
            best = (sid, t)
    return best[0] if best else None


def cmd_init(a):
    sid = a.session or latest_unbound_session()
    if not sid:
        sys.exit('No session id given and no fresh unbound automation session found. Start with /automation-build.')
    client_slug = slugify(a.client_dir or a.client)
    run_dir = os.path.join(a.root or DEFAULT_ROOT, client_slug, 'automation', slugify(a.slug))
    if os.path.exists(os.path.join(run_dir, 'state.json')):
        bind(sid, run_dir)
        print(f'Run exists, session bound: {run_dir}')
        return
    for sd in SUBDIRS:
        os.makedirs(os.path.join(run_dir, sd), exist_ok=True)
    for f, body in FILES.items():
        p = os.path.join(run_dir, f)
        if not os.path.exists(p):
            open(p, 'w', encoding='utf-8').write(body)
    L.save_run_state(run_dir, {'client': a.client, 'slug': slugify(a.slug), 'created_at': L.now(), 'phase': 'intake',
                               'mode': a.mode, 'spec_approved_at': None, 'actions': [], 'phase_log': []})
    write_runjson(run_dir, client=a.client, workflow='automation', status='Trockenlauf' if a.mode == 'Trockenlauf' else 'in Arbeit',
                  mode=a.mode, result=os.path.relpath(run_dir, REPO), note=f'Automation Build: {a.slug}')
    bind(sid, run_dir)
    print(run_dir)


def cmd_bind(a):
    if not os.path.exists(os.path.join(a.run, 'state.json')):
        sys.exit('No state.json in that folder.')
    bind(a.session, a.run)
    print(f'bound {a.session} -> {os.path.abspath(a.run)}')


def cmd_phase(a):
    st = L.run_state(a.run) or sys.exit('No state.json.')
    new = a.set
    if new not in L.PHASES:
        sys.exit(f'Unknown phase. Use one of: {", ".join(L.PHASES)}')
    old = st.get('phase', 'intake')
    if L.PHASES.index(new) < L.PHASES.index(old):
        sys.exit(f'Phase goes forward only ({old} -> {new} refused). Log a rework in changelog.md instead.')
    if L.PHASES.index(new) >= L.PHASES.index('environment') and not st.get('spec_approved_at'):
        sys.exit('Spec is not approved. Show Martin spec.md and wait for his prompt "go spec".')
    if L.PHASES.index(new) >= L.PHASES.index('golive'):
        r = subprocess.run([sys.executable, os.path.join(HERE, 'check_report.py'), a.run, '--json'], capture_output=True, text=True)
        res = json.loads(r.stdout or '{}')
        if not res.get('ok'):
            sys.exit('Test report does not pass: ' + '; '.join(res.get('failures', [])))
    st['phase'] = new
    st.setdefault('phase_log', []).append({'phase': new, 'at': L.now()})
    L.save_run_state(a.run, st)
    status = {'golive': 'in Arbeit', 'monitor': 'fertig, Freigabe offen', 'done': 'fertig, Freigabe offen'}.get(new)
    if status and st.get('mode') != 'Trockenlauf':
        write_runjson(a.run, status=status)
    print(f'phase: {old} -> {new}')


def cmd_request(a):
    st = L.run_state(a.run) or sys.exit('No state.json.')
    if not a.contains or not all(c.strip() for c in a.contains):
        sys.exit('--contains is required: exact text that will appear in the tool call (for example the Zap ID).')
    try:
        re.compile(a.tool)
    except re.error as e:
        sys.exit(f'--tool is not a valid regex: {e}')
    n = 1 + max([int(x['id'][1:]) for x in st.get('actions', [])] or [0])
    act = {'id': f'A{n}', 'kind': a.kind, 'tool': a.tool, 'contains': a.contains, 'target': a.target,
           'uses': a.uses, 'status': 'requested', 'requested_at': L.now()}
    st.setdefault('actions', []).append(act)
    L.save_run_state(a.run, st)
    # hook-owned copy: the go hook grants from this copy, so a later edit of state.json cannot change the rule
    run_abs = os.path.abspath(a.run)
    for sid, s in L.sessions().items():
        if s.get('run_dir') == run_abs:
            L.append_jsonl(L.requests_path(sid), dict(act, run_dir=run_abs))
    print(f'A{n} requested. Show Martin this action in full and wait for his prompt "go A{n}":\n'
          f'  A{n} [{a.kind}] {a.target}\n  tool: {a.tool}\n  must contain: {a.contains}\n  uses: {a.uses}')


def cmd_log(a):
    with open(os.path.join(a.run, 'changelog.md'), 'a', encoding='utf-8') as f:
        f.write(f'- {L.now()} {a.msg}\n')
    print('logged')


def cmd_runjson(a):
    write_runjson(a.run, status=a.status, result=a.result, note=a.note, drive=a.drive)
    print('ok')


def cmd_status(a):
    st = L.run_state(a.run) or sys.exit('No state.json.')
    print(json.dumps({k: st.get(k) for k in ('client', 'slug', 'phase', 'mode', 'spec_approved_at')}, ensure_ascii=False))
    for x in st.get('actions', []):
        print(f"  {x['id']} {x['status']:<9} [{x['kind']}] {x['target']}")


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest='cmd', required=True)
    i = sub.add_parser('init'); i.add_argument('--session'); i.add_argument('--client', required=True)
    i.add_argument('--slug', required=True); i.add_argument('--mode', default='Echt', choices=['Echt', 'Trockenlauf'])
    i.add_argument('--root'); i.add_argument('--client-dir', help='existing folder name under assets/, e.g. marcel')
    b = sub.add_parser('bind'); b.add_argument('--session', required=True); b.add_argument('--run', required=True)
    ph = sub.add_parser('phase'); ph.add_argument('--run', required=True); ph.add_argument('--set', required=True)
    r = sub.add_parser('request'); r.add_argument('--run', required=True)
    r.add_argument('--kind', required=True, choices=['send', 'publish', 'write'])
    r.add_argument('--tool', required=True); r.add_argument('--contains', action='append')
    r.add_argument('--target', required=True); r.add_argument('--uses', type=int, default=1)
    lg = sub.add_parser('log'); lg.add_argument('--run', required=True); lg.add_argument('--msg', required=True)
    rj = sub.add_parser('runjson'); rj.add_argument('--run', required=True)
    for k in ('status', 'result', 'note', 'drive'):
        rj.add_argument('--' + k)
    s = sub.add_parser('status'); s.add_argument('--run', required=True)
    a = p.parse_args()
    {'init': cmd_init, 'bind': cmd_bind, 'phase': cmd_phase, 'request': cmd_request, 'log': cmd_log,
     'runjson': cmd_runjson, 'status': cmd_status}[a.cmd](a)


if __name__ == '__main__':
    main()
