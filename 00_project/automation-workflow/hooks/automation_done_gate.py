#!/usr/bin/env python3
"""Stop hook (DRAFT, not installed). Acts only in /automation-build sessions.

Blocks the end of a turn when the last message claims the automation is done, works or is live,
the run is past the spec phase (or the session already wrote something), and scripts/check_report.py fails.
Uses stop_hook_active so it never loops. A crash never blocks.
"""
import json, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import automation_lib as L

CLAIM = re.compile(r'\b(done|finished|complete[d]?|works|working|is live|went live|goes live|ready for go-?live|'
                   r'fertig|erledigt|abgeschlossen|funktioniert|läuft|live geschaltet|ist live|steht|einsatzbereit)\b', re.I)
NEG = re.compile(r'\b(not|noch nicht|nicht|never|nie|no longer)\s+(?:\w+\s+){0,2}?(done|finished|complete[d]?|works|working|'
                 r'live|fertig|erledigt|abgeschlossen|funktioniert|läuft)\b', re.I)


def main():
    try:
        d = json.load(sys.stdin)
    except Exception:
        return
    if d.get('stop_hook_active'):
        return
    sid = d.get('session_id') or ''
    s = L.session(sid)
    if not s:
        return
    msg = d.get('last_assistant_message') or ''
    if not CLAIM.search(NEG.sub(' ', msg)):
        return
    run_dir = s.get('run_dir')
    wrote = any(r.get('class') in ('test_write', 'G') and r.get('decision') == 'allow'
                for r in L.read_jsonl(L.activity_path(sid)))
    if not run_dir:
        if wrote:
            block('This session changed systems but has no run folder. Bind it with run_state.py, write the test '
                  'report, then report. Until then say what was changed and that tests are pending.')
        return
    st = L.run_state(run_dir) or {}
    phase = st.get('phase', 'intake')
    if phase in ('intake', 'spec') and not wrote:
        return
    chk = os.path.join(L.SCRIPTS, 'check_report.py')
    try:
        r = subprocess.run([sys.executable, chk, run_dir, '--json'], capture_output=True, text=True, timeout=30)
        res = json.loads(r.stdout or '{}')
    except Exception as e:
        res = {'ok': False, 'failures': [f'check_report.py did not run: {e}']}
    if res.get('ok'):
        return
    fails = '; '.join(res.get('failures', [])[:8])
    block(f'Done gate: the message claims the automation is done or works, but the test report does not pass '
          f'({fails}). Finish the tests and the verifier run, or state plainly what is built and what is not yet '
          f'tested. Run: python3 "{chk}" "{run_dir}"')


def block(reason):
    print(json.dumps({'decision': 'block', 'reason': reason}))
    sys.exit(0)


try:
    main()
except SystemExit:
    raise
except Exception:
    sys.exit(0)
