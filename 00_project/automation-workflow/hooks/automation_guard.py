#!/usr/bin/env python3
"""PreToolUse hook (DRAFT, not installed). Acts only in /automation-build sessions.

read / test_write -> no decision (normal permission flow), test_write is logged
G                 -> deny unless a granted go token matches this call (token is used once)
M                 -> deny always: Martin does money, prices, delete, bulk, permissions
secret / ledger   -> deny always
A crash in this script never blocks work (exit 0 without output).
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import automation_lib as L


def deny(reason):
    print(json.dumps({'hookSpecificOutput': {'hookEventName': 'PreToolUse', 'permissionDecision': 'deny',
                                             'permissionDecisionReason': reason}}))
    sys.exit(0)


def main():
    try:
        d = json.load(sys.stdin)
    except Exception:
        return
    sid = d.get('session_id') or ''
    s = L.session(sid)
    if not s:
        return  # not an automation session: the guard stays silent
    tool, ti = d.get('tool_name', ''), d.get('tool_input', {})
    cls, why = L.classify(tool, ti)
    if cls == 'read':
        return
    run_dir = s.get('run_dir')
    row = {'at': L.now(), 'tool': tool, 'class': cls, 'why': why, 'run_dir': run_dir}
    rs = os.path.join(L.SCRIPTS, 'run_state.py')

    if cls == 'ledger':
        L.append_jsonl(L.activity_path(sid), dict(row, decision='deny'))
        deny('Automation guard: the go ledger and hook state are written only by the hooks. Do not edit them.')
    if cls == 'secret':
        L.append_jsonl(L.activity_path(sid), dict(row, decision='deny'))
        deny(f'Automation guard: {why}. Secrets stay in .secrets/ or .env; use the variable name, never the value.')
    if cls == 'M':
        L.append_jsonl(L.activity_path(sid), dict(row, decision='deny'))
        deny(f'Automation guard, class M (Martin only): {why}. Do not do this yourself. Write the exact steps for Martin '
             f'into martin-steps.md in the run folder and ask him to do them.')
    if cls == 'test_write':
        if not run_dir and tool not in ('mcp__claude-in-chrome__form_input',):
            L.append_jsonl(L.activity_path(sid), dict(row, decision='deny'))
            deny(f'Automation guard: bind the run folder first (python3 "{rs}" init --session {sid} --client ... --slug ...).')
        L.append_jsonl(L.activity_path(sid), dict(row, decision='allow'))
        return

    # class G: needs a matching, unused go token
    blob = L.blob_of(ti)
    ledger = L.read_jsonl(L.ledger_path(sid))
    used = {}
    for e in ledger:
        if e.get('event') == 'used':
            used[e['id']] = used.get(e['id'], 0) + 1
    for e in ledger:
        if e.get('event') or not e.get('id'):
            continue
        left = int(e.get('uses', 1)) - used.get(e['id'], 0)
        if left <= 0:
            continue
        try:
            tool_ok = re.fullmatch(e.get('tool', ''), tool) is not None
        except re.error:
            tool_ok = False
        if tool_ok and e.get('contains') and all(c in blob for c in e['contains']):
            L.append_jsonl(L.ledger_path(sid), {'event': 'used', 'id': e['id'], 'at': L.now(), 'tool': tool})
            L.append_jsonl(L.activity_path(sid), dict(row, decision='allow', go=e['id']))
            if run_dir:
                st = L.run_state(run_dir)
                if st:
                    for a in st.get('actions', []):
                        if a.get('id') == e['id']:
                            a['used'] = a.get('used', 0) + 1
                            if a['used'] >= int(a.get('uses', 1)):
                                a['status'] = 'used'
                    L.save_run_state(run_dir, st)
            return
    L.append_jsonl(L.activity_path(sid), dict(row, decision='deny'))
    if not run_dir:
        deny(f'Automation guard, class G: {why}. Bind the run folder first, then request a go.')
    hint = re.sub(r'\s+', ' ', blob)[:160]
    deny(f'Automation guard, class G (needs Martin\'s go): {why}. Register the action: python3 "{rs}" request '
         f'--run "{run_dir}" --kind <send|publish|write> --tool "{re.escape(tool)}" --contains "<exact text from the call>" '
         f'--target "<what happens, for whom>". Show Martin the full action and wait for his "go A<n>". Call input was: {hint}')


try:
    main()
except SystemExit:
    raise
except Exception:
    sys.exit(0)
