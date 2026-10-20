#!/usr/bin/env python3
"""UserPromptExpansion + UserPromptSubmit hook. Installed at user level, 2026-10-15.

1. Registers a session as an automation session when Martin starts /automation-build
   (literal prefix), OR when the prompt paraphrases the same request: a build verb
   (bau/baue/bauen/verbinde/verbinden) next to an automation noun (Zapier/Zap/
   Automation-Strecke/Zapier-Strecke). Added 2026-10-15 after a real fresh-session test
   showed a paraphrase got neither the skill (disable-model-invocation stays as designed —
   this hook never loads the skill body, it only switches the guard/done-gate on) nor the
   hook, and the model attempted to build an automation ad hoc, ungated. This hook's job is
   only to arm the guard and the done gate; it never changes what loads the skill itself.
2. Records Martin's go tokens. Only a prompt that is exactly "go A3" (or "go A3 A4", "go spec")
   counts. Text from other sessions, scheduled turns or subagents is wrapped and never matches.
Never blocks a prompt. Never fails a turn.
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import automation_lib as L

GO_RE = re.compile(r'^\s*go\s+((?:A\d+|spec)(?:[\s,+&]+(?:A\d+|spec))*)\s*[.!]?\s*$', re.I)
# Paraphrase match (2026-10-15): a build verb near an automation noun, anywhere in the prompt.
# Biased towards catching too much rather than too little — this only arms the guard/gate,
# it does not load the skill body and does not block anything by itself.
PARA_VERB_RE = r'\b(bau(?:e|en|t)?|verbinde(?:n|t)?)\b'
PARA_NOUN_RE = r'\b(zapier(?:[- ]?strecke)?|zap|automation[s]?[- ]?strecke)\b'
PARAPHRASE_RE = re.compile(PARA_VERB_RE, re.I), re.compile(PARA_NOUN_RE, re.I)
# Wrapped-text guard (2026-10-15, after a real false registration): GO_RE is protected because
# it is anchored to the full prompt (^...$), so a wrapped block never matches it. PARAPHRASE_RE
# uses .search() instead and has no such anchor, so it used to fire on a build verb and an
# automation noun anywhere inside a task-notification, cross-session message or other
# harness-delivered block — text Martin never typed. A genuine prompt from Martin never starts
# with the harness's own markup, so refuse to arm on a prompt that does.
WRAPPED_RE = re.compile(r'^\s*<[\w-]+[\s>]')


def out(text):
    print(json.dumps({'hookSpecificOutput': {'hookEventName': EVENT, 'additionalContext': text}}))
    sys.exit(0)


try:
    d = json.load(sys.stdin)
except Exception:
    sys.exit(0)
EVENT = d.get('hook_event_name', 'UserPromptSubmit')
sid = d.get('session_id') or ''
prompt = (d.get('prompt') or '').strip()
if not sid:
    sys.exit(0)

literal = EVENT == 'UserPromptSubmit' and bool(re.match(r'^/automation-build(\s|$)', prompt))
paraphrase = EVENT == 'UserPromptSubmit' and not literal and not WRAPPED_RE.match(prompt) and \
             bool(PARAPHRASE_RE[0].search(prompt)) and bool(PARAPHRASE_RE[1].search(prompt))
starts = (EVENT == 'UserPromptExpansion' and d.get('command_name') == 'automation-build') or literal or paraphrase
if starts:
    s = L.session(sid) or {}
    first = not s
    s.setdefault('registered_at', L.now())
    s['trigger'] = 'paraphrase' if paraphrase else ('literal' if literal else 'expansion')
    s.setdefault('run_dir', None)
    s['last_start_prompt'] = prompt[:300]
    L.save_session(sid, s)
    rs = os.path.join(L.SCRIPTS, 'run_state.py')
    out(('Automation session registered. ' if first else 'Automation session already registered. ') +
        f'session_id={sid}. The automation guard and the done gate are active in this session. '
        f'Bind the run folder before any write: python3 "{rs}" init --session {sid} --client "<client>" --slug <slug> '
        f'(or: bind --session {sid} --run <run_dir> to resume).')

m = GO_RE.match(prompt)
if not m or EVENT != 'UserPromptSubmit':
    sys.exit(0)
s = L.session(sid)
if not s or not s.get('run_dir'):
    sys.exit(0)
run_dir = s['run_dir']
state = L.run_state(run_dir)
if not state:
    out(f'go not recorded: no state.json in {run_dir}.')

ids = re.findall(r'A\d+|spec', m.group(1), re.I)
done, bad = [], []
for raw in ids:
    if raw.lower() == 'spec':
        state['spec_approved_at'] = L.now()
        done.append('spec')
        continue
    aid = raw.upper()
    act = next((a for a in state.get('actions', []) if a.get('id') == aid), None)
    req = [r for r in L.read_jsonl(L.requests_path(sid)) if r.get('id') == aid and r.get('run_dir') == run_dir]
    if not act or not req:
        bad.append(f'{aid} unknown')
        continue
    if act.get('status') != 'requested' or any(e.get('id') == aid and not e.get('event') for e in L.read_jsonl(L.ledger_path(sid))):
        bad.append(f"{aid} is {act.get('status')}")
        continue
    rule = req[-1]  # hook-owned copy written by run_state.py request; state.json edits do not count
    act['status'] = 'granted'
    act['granted_at'] = L.now()
    L.append_jsonl(L.ledger_path(sid), {'id': aid, 'run_dir': run_dir, 'tool': rule['tool'], 'contains': rule['contains'],
                                        'uses': int(rule.get('uses', 1)), 'target': rule.get('target', ''),
                                        'granted_at': act['granted_at']})
    done.append(f"{aid} ({rule.get('target', '')})")
L.save_run_state(run_dir, state)
msg = ('Go recorded by the hook: ' + ', '.join(done) + '.') if done else 'No go recorded.'
if bad:
    msg += ' Not recorded: ' + ', '.join(bad) + '.'
out(msg)
