#!/usr/bin/env python3
"""741 workflow build checker (2026-10-13).

Every new or reworked workflow keeps 00_project/workflow-builds/<id>/build-checklist.json.
This script blocks a checkpoint until every required step is done AND has a real evidence file.

Usage:
  check_build.py init <id> "<Workflow name>"          create the folder and the checklist
  check_build.py check <id> --gate cp1|cp2|install     exit 1 when the gate is not passed
  check_build.py status <id>                           show all steps
  check_build.py done <id> <step> <evidence-path> ["note"]   mark a step done with its evidence
  check_build.py skip <id> <step> "<reason>"           only for optional steps (4.4, 5.3b, 5.4, 3.7)
"""
import json, os, re, sys, subprocess, datetime

ROOT = '/Users/martindrendel/741website'
BUILDS = os.path.join(ROOT, '00_project', 'workflow-builds')
REG = os.path.join(ROOT, '00_project', 'workflow-registry', 'registry.json')
MEM = os.path.expanduser('~/.claude/projects/-Users-martindrendel-741website/memory')

STEPS = [
 ('0.0', 'Inputs Martin gives confirmed via interactive grill (inputs-grill.md: Job, Surface, Cadence, Limits)'),
 ('1.1', 'Building block chosen with reason (patterns.md section 3)'),
 ('1.2', 'Library searched for the topic (grep result or notes)'),
 ('1.3', 'Library freshness checked (INDEX.md date; refresh if older than 6 weeks)'),
 ('1.4', 'Existing 741 assets checked (coverage map)'),
 ('1.5', 'Research note written (10-20 lines)'),
 ('2.1', '2-3 use cases (trigger, steps, tools, result)'),
 ('2.2', '3 test scenarios with expected output, BEFORE the body (obvious, paraphrase, must-not-trigger)'),
 ('2.3', 'One real task solved by hand with Martin; context noted'),
 ('2.4', 'Pipeline with checkpoints'),
 ('2.5', 'Degrees of freedom per step (script vs heuristic)'),
 ('2.6', 'Checkpoint 1: Martin go on the design (decision record)'),
 ('3.1', 'Folder from the 741 template (patterns.md section 5)'),
 ('3.2', 'Frontmatter: WHAT + WHEN + negative trigger'),
 ('3.3', 'Body as checklist with gates; critical rules on top'),
 ('3.4', 'References one level deep; body under 500 lines'),
 ('3.5', 'Verification step with evidence at the end of the body'),
 ('3.6', '741 house rules applied'),
 ('3.7', 'Unattended rules (rules.md section 6), if it runs unattended'),
 ('4.1', 'Trigger tests in a fresh session (3 scenarios, results recorded)'),
 ('4.2', 'Functional test in a fresh session (real task)'),
 ('4.3', 'Baseline with vs without (corrections, tool calls, tokens)'),
 ('4.4', 'Plugin eval or /doctor prompt-audit, if it applies'),
 ('4.5', 'Scorecard >= 80 %, no zero in A or D'),
 ('5.1', 'Checkpoint 2: Martin go on scorecard + one real output (decision record)'),
 ('5.2', 'Committed (project files) or path noted in memory (personal skill)'),
 ('5.3a', 'Registry entry (add-workflow) and _run.json per run'),
 ('5.3b', 'Martin guide where a client or prospect sees output'),
 ('5.3', 'Memory file + MEMORY.md line'),
 ('5.4', 'Scheduled run done once by hand and read, if scheduled'),
]
OPTIONAL = {'3.7', '4.4', '5.3b', '5.4'}
GATES = {
 'cp1': ['0.0', '1.1', '1.2', '1.3', '1.4', '1.5', '2.1', '2.2', '2.3', '2.4', '2.5'],
 'cp2': ['2.6', '3.1', '3.2', '3.3', '3.4', '3.5', '3.6', '3.7', '4.1', '4.2', '4.3', '4.4', '4.5'],
 'install': ['5.1', '5.2', '5.3a', '5.3b', '5.3', '5.4'],
}
ORDER = ['cp1', 'cp2', 'install']

def path_of(i): return os.path.join(BUILDS, i, 'build-checklist.json')
def load(i): return json.load(open(path_of(i), encoding='utf-8'))
def save(i, d):
    p = path_of(i); tmp = p + '.tmp'
    json.dump(d, open(tmp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1); os.replace(tmp, p)
def abs_ev(e): return e if e.startswith('/') else os.path.join(ROOT, e)
def text(e):
    try: return open(abs_ev(e), encoding='utf-8', errors='ignore').read()
    except Exception: return ''

def check_step(d, sid):
    if sid not in d.get('steps', {}):
        return True, 'legacy build (step not in checklist)'
    s = d['steps'].get(sid, {})
    st = s.get('status', 'todo')
    if st == 'skipped':
        return (sid in OPTIONAL and bool(s.get('reason'))), 'skipped: ' + s.get('reason', 'NO REASON') + ('' if sid in OPTIONAL else ' (NOT ALLOWED, step is required)')
    if st != 'done': return False, 'not done'
    ev = s.get('evidence', '')
    if not ev: return False, 'done but no evidence path'
    if sid == '0.0':
        if not ev.startswith('http') and (not os.path.exists(abs_ev(ev)) or os.path.getsize(abs_ev(ev)) == 0):
            return False, 'evidence file missing or empty: ' + ev
        t_low = text(ev).lower()
        has_job = any(k in t_low for k in ['job', 'was eingeht', 'task', 'ziel'])
        has_surface = any(k in t_low for k in ['surface', 'laufzeit', 'runtime'])
        has_cadence = any(k in t_low for k in ['cadence', 'frequenz', 'frequency', 'turnus'])
        has_limits = any(k in t_low for k in ['limit', 'grenz', 'hard limit'])
        if not (has_job and has_surface and has_cadence and has_limits):
            missing = []
            if not has_job: missing.append('Job')
            if not has_surface: missing.append('Surface')
            if not has_cadence: missing.append('Cadence')
            if not has_limits: missing.append('Hard Limits')
            return False, f'inputs-grill missing parameter(s): {", ".join(missing)} in {ev}'
        return True, 'verified 4 parameters (Job, Surface, Cadence, Hard Limits)'
    if sid == '5.3a':
        ids = [w['id'] for w in json.load(open(REG, encoding='utf-8'))['workflows']]
        return (d['workflow_id'] in ids), ('registry entry found' if d['workflow_id'] in ids else 'workflow id not in registry.json')
    if sid == '5.3':
        mp = abs_ev(ev)
        ok = os.path.exists(mp) and os.path.basename(mp) in open(os.path.join(MEM, 'MEMORY.md'), encoding='utf-8').read()
        return ok, ('memory file + index line found' if ok else 'memory file missing or not in MEMORY.md')
    if not ev.startswith('http') and (not os.path.exists(abs_ev(ev)) or os.path.getsize(abs_ev(ev)) == 0):
        return False, 'evidence file missing or empty: ' + ev
    t = text(ev)
    if sid == '2.2':
        n = len(re.findall(r'must.?not|NOT trigger|nicht ausl|should not trigger|darf nicht', t, re.I))
        if n < 1: return False, 'no must-not-trigger scenario found in ' + ev
    if sid == '4.5':
        m = re.search(r'(\d+(?:[.,]\d+)?)\s*%', t[t.find('Total'):] if 'Total' in t else t)
        z = re.search(r'Blocking zeros:\s*(\d+)', t)
        if not m: return False, 'no percent found in scorecard ' + ev
        pct = float(m.group(1).replace(',', '.'))
        if pct < 80: return False, f'scorecard {pct} % < 80 %'
        if z and int(z.group(1)) > 0: return False, f'blocking zeros: {z.group(1)}'
        return True, f'scorecard {pct} %'
    if sid in ('2.6', '5.1') and not re.search(r'\bgo\b|freigegeben|approved|abgesegnet|passt', t, re.I):
        return False, 'decision record has no go/approval wording: ' + ev
    return True, ev

def cmd_check(i, gate):
    d = load(i); upto = ORDER[:ORDER.index(gate) + 1]; bad = 0
    print(f"{d['name']} ({i}) · gate {gate}")
    for g in upto:
        for sid in GATES[g]:
            ok, why = check_step(d, sid)
            bad += 0 if ok else 1
            print(f"  {'OK ' if ok else 'MISSING'} {sid:5} {dict(STEPS)[sid][:60]:60} {why}")
    print(('GATE PASSED' if not bad else f'GATE BLOCKED: {bad} step(s) missing') + f' · {gate}')
    d.setdefault('gate_log', []).append({'gate': gate, 'passed': not bad, 'missing': bad, 'at': datetime.datetime.now().isoformat(timespec='minutes')})
    save(i, d); sys.exit(0 if not bad else 1)

if __name__ == '__main__':
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    if a[0] == 'init':
        i, name = a[1], a[2]; os.makedirs(os.path.join(BUILDS, i), exist_ok=True)
        if os.path.exists(path_of(i)): sys.exit('exists: ' + path_of(i))
        save(i, {'workflow_id': i, 'name': name, 'created': datetime.date.today().isoformat(),
                 'process': '00_project/workflow-creation-workflow.md',
                 'steps': {sid: {'status': 'todo', 'title': t, 'evidence': '', 'date': '', 'note': ''} for sid, t in STEPS}})
        print('created', path_of(i))
    elif a[0] == 'done':
        i, sid, ev = a[1], a[2], a[3]; d = load(i)
        d['steps'][sid].update({'status': 'done', 'evidence': ev, 'date': datetime.date.today().isoformat(), 'note': a[4] if len(a) > 4 else ''})
        save(i, d); ok, why = check_step(d, sid); print(('OK ' if ok else 'CHECK FAILS ') + sid + ' · ' + why)
    elif a[0] == 'skip':
        i, sid, reason = a[1], a[2], a[3]; d = load(i)
        if sid not in OPTIONAL: sys.exit(f'step {sid} is required and cannot be skipped')
        d['steps'][sid].update({'status': 'skipped', 'reason': reason, 'date': datetime.date.today().isoformat()}); save(i, d); print('skipped', sid)
    elif a[0] == 'status':
        d = load(a[1])
        for sid, t in STEPS:
            s = d['steps'][sid]; print(f"{s['status']:8} {sid:5} {t[:62]:62} {s.get('evidence') or s.get('reason', '')}")
    elif a[0] == 'check':
        cmd_check(a[1], a[a.index('--gate') + 1] if '--gate' in a else 'cp1')
    else: sys.exit(__doc__)
