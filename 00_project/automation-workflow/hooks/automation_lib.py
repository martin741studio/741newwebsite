#!/usr/bin/env python3
"""Shared code for the 741 Automation Build hooks (DRAFT, not installed).

Classes of a tool call:
  read        no change anywhere                              -> free
  test_write  change on TEST data, a draft, or 741 test inbox -> free, logged
  G           message to real people / switch on / publish /
              write on live data without TEST marker          -> needs Martin's "go A<n>"
  M           money, prices, delete, bulk, permissions        -> Martin only, always blocked
  secret      would print or store a secret                   -> blocked
  ledger      touches the go ledger or hook state             -> blocked

State lives in AUTOMATION_HOME (default ~/.claude/automation-runs):
  sessions.json            session_id -> {registered_at, run_dir}
  ledger/<session>.jsonl   go tokens (written only by the prompt hook and consumed by the guard)
  activity/<session>.jsonl every non-read call the guard saw
The hooks stop mistakes, not attacks. See ../automation-workflow.md section "Limits".
"""
import base64, datetime, json, os, re

HOME = os.environ.get('AUTOMATION_HOME') or os.path.expanduser('~/.claude/automation-runs')
HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.normpath(os.path.join(HERE, '..', 'scripts'))

TEST_MARKER = 'TEST-741'
# Recipients that count as test inboxes. Martin's own business inbox is the default test inbox.
TEST_RECIPIENT_RE = re.compile(r'^(martin@741\.studio|test[\w.+-]*@741\.studio|[\w.+-]+@[\w.-]+\.test)$', re.I)
EMAIL_RE = re.compile(r'[\w.+-]+@[\w-]+(?:\.[\w-]+)+')

PHASES = ['intake', 'spec', 'environment', 'build', 'test', 'verify', 'golive', 'monitor', 'done']


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')


def _p(*parts):
    return os.path.join(HOME, *parts)


def jload(path, default):
    try:
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return default


def jsave(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    os.replace(tmp, path)


def append_jsonl(path, row):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'a', encoding='utf-8') as f:
        f.write(json.dumps(row, ensure_ascii=False) + '\n')


def read_jsonl(path):
    rows = []
    try:
        with open(path, encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        rows.append(json.loads(line))
                    except Exception:
                        pass
    except FileNotFoundError:
        pass
    return rows


# ------------------------------------------------------------------ sessions and runs
def sessions():
    return jload(_p('sessions.json'), {})


def session(session_id):
    return sessions().get(session_id or '')


def save_session(session_id, data):
    s = sessions()
    s[session_id] = data
    jsave(_p('sessions.json'), s)


def ledger_path(session_id):
    return _p('ledger', f'{session_id}.jsonl')


def requests_path(session_id):
    return _p('requests', f'{session_id}.jsonl')


def activity_path(session_id):
    return _p('activity', f'{session_id}.jsonl')


def run_state(run_dir):
    return jload(os.path.join(run_dir, 'state.json'), None) if run_dir else None


def save_run_state(run_dir, state):
    jsave(os.path.join(run_dir, 'state.json'), state)


# ------------------------------------------------------------------ classification
RE = lambda s: re.compile(s, re.I | re.S)

READ_TOOLS = {'Read', 'Glob', 'Grep', 'WebFetch', 'WebSearch', 'ToolSearch', 'TodoWrite', 'AskUserQuestion',
              'ReadNotifications', 'ListAgents', 'Skill', 'Agent', 'TaskStop', 'ScheduleWakeup'}
READ_VERB = RE(r'(^|_|-)(get|list|search|read|fetch|query|discover|inspect|describe|find|check|whoami|ping|screenshot|'
               r'tabs_context|tabs_context_mcp|page_text|read_page|read_console|read_network|navigate|tabs_create|'
               r'tabs_create_mcp|tabs_close|tabs_close_mcp|select_browser|switch_browser|list_connected|resize|zoom|'
               r'download|export|render|show|preview|resolve|suggest|generate_typescript|advisors|logs|cost|'
               r'project_url|publishable_keys|organization|whoami|schema|guidance|info|details|metadata|context)'
               r'($|_|-)')

M_WORDS = RE(r'\b(delet\w*|lösch\w*|remov\w*|entfern\w*|trash\w*|pay\b|pays|paying|payment\w*|bezahl\w*|kauf\w*|kaufen|'
             r'purchas\w*|buy\w*|checkout|refund\w*|erstatt\w*|invit\w*|einlad\w*|permission\w*|berechtigung\w*|'
             r'api[ -]?key\w*|access token|grant\w*|freigeb\w* für|price\w*|preis\w*|pricing|upgrad\w*|downgrad\w*|'
             r'subscription\w*|abonnement\w*|kündig\w*|cancel (?:the )?(?:plan|subscription|membership)|bulk|massen\w*|'
             r'merge contacts|zusammenführ\w*|transfer\w*|übertrag\w*)\b')
G_WORDS = RE(r'\b(send|sends|sending|senden|sende|versend\w*|abschick\w*|submit|submits|submitting|absend\w*|'
             r'publish\w*|veröffentlich\w*|go(?:es)? live|activat\w*|aktivier\w*|turns? on|switch(?:es)? on|'
             r'einschalt\w*|enabl\w*|live schalt\w*|scharf schalt\w*|launch\w*|deploy\w*|schedul\w*|'
             r'start(?:s)? (?:the )?(?:zap|campaign|kampagne|sequence|serie|workflow|automation|scenario|flow)|'
             r'kampagne starten|reply|replies|antwort\w* senden|post(?:s)? (?:the|a|to)\b|tweet\w*|dial\w*|call(?:s)? (?:the )?(?:number|lead|client))\b')
DRAFTISH = RE(r'\b(draft|entwurf|TEST-741|test record|testdatensatz|placeholder|platzhalter|lorem)\b')

SECRET_RES = [RE(p) for p in [
    r'sk_live_[0-9a-z]{10,}', r'rk_live_[0-9a-z]{10,}', r'sk-ant-[\w-]{20,}', r'sk-[a-z0-9]{32,}', r'shpat_[0-9a-f]{20,}',
    r'shpss_[0-9a-f]{20,}', r'\bre_[a-z0-9]{6,}_[a-z0-9]{10,}', r'xox[bap]-[\w-]{10,}', r'ghp_[a-z0-9]{30,}',
    r'github_pat_[\w]{30,}', r'AKIA[0-9A-Z]{16}', r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
    r'whsec_[\w+/=]{10,}', r'EAA[a-z0-9]{60,}', r'AIza[0-9a-z_-]{35}',
    r'\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}_[0-9a-z]{6,}\b',
    r'(?:api[_-]?key|secret|passwor[dt]|client[_-]?secret|auth[_-]?token)["\']?\s*[:=]\s*["\'][^"\'\s]{16,}["\']',
]]
JWT_RE = re.compile(r'eyJ[\w-]{10,}\.(eyJ[\w-]{10,})\.[\w-]{10,}')
SECRET_FILE_RE = RE(r'(^|/)(\.env(\.[\w-]+)?|\.secrets/[^\s"\']+|[\w.-]*\.env)$')
SECRET_PATH_IN_CMD = RE(r'(?:^|[\s"\'=/])(\.env(?:\.[\w-]+)?|\.secrets/[\w./-]+|[\w./-]+\.env)\b')


def has_secret(text):
    for r in SECRET_RES:
        if r.search(text or ''):
            return True
    for m in JWT_RE.finditer(text or ''):
        try:
            seg = m.group(1)
            payload = json.loads(base64.urlsafe_b64decode(seg + '=' * (-len(seg) % 4)))
            if payload.get('role') == 'service_role':
                return True
        except Exception:
            continue
    return False


def blob_of(tool_input):
    try:
        return json.dumps(tool_input, ensure_ascii=False)
    except Exception:
        return str(tool_input)


def recipients_all_test(text):
    found = [e for e in EMAIL_RE.findall(text or '') if not e.lower().endswith(('@example.com',))]
    # ignore sender addresses written as "Name <x@y>" in a from field: we only judge to/cc/bcc when present
    m = re.search(r'"(?:to|cc|bcc)"\s*:\s*(\[[^\]]*\]|"[^"]*")', text or '', re.I)
    if m:
        found = EMAIL_RE.findall(' '.join(re.findall(r'"(?:to|cc|bcc)"\s*:\s*(\[[^\]]*\]|"[^"]*")', text, re.I)))
    return bool(found) and all(TEST_RECIPIENT_RE.match(e) for e in found)


def has_test_marker(text):
    return TEST_MARKER.lower() in (text or '').lower()


def touches_hook_state(text):
    t = (text or '')
    home = HOME.replace(os.path.expanduser('~'), '~')
    return ('automation-runs/ledger' in t or 'automation-runs/activity' in t or 'automation-runs/requests' in t
            or 'automation-runs/sessions.json' in t
            or (HOME in t and 'run_state.py' not in t) or (home in t and 'run_state.py' not in t))


def _expand_data_files(cmd):
    """curl --data-binary @file / -d @file: read the payload so recipients can be checked."""
    extra = []
    for f in re.findall(r'@([\w./~-]+\.(?:json|txt|html))', cmd):
        try:
            with open(os.path.expanduser(f), encoding='utf-8', errors='ignore') as fh:
                extra.append(fh.read()[:200000])
        except Exception:
            pass
    return cmd + '\n' + '\n'.join(extra)


RUN_SCRIPT_RE = re.compile(r'^\s*(?:\S*/)?python3?\s+"?[^"\s;&|]*/(?:run_state|check_report)\.py"?\s[^;&|`$<>]*$')


def classify_bash(cmd):
    c = cmd or ''
    if RUN_SCRIPT_RE.match(c) and '\n' not in c.strip():
        return 'read', ''  # the workflow's own scripts: one call, no chaining
    if touches_hook_state(c):
        return 'ledger', 'command touches the hook state (ledger, activity or sessions)'
    # secrets: never print them
    if re.search(r'\b(cat|less|more|head|tail|bat|nl|strings|xxd|od)\b[^|;&]*' + SECRET_PATH_IN_CMD.pattern, c, re.I) \
            or re.search(r'\becho\s+["\']?\$\{?\w*(KEY|TOKEN|SECRET|PASSWORD|PASS)\w*', c, re.I) \
            or re.search(r'(^|[;&|]\s*)(printenv|env)\s*($|[;&|])', c):
        return 'secret', 'command would print a secret (use the variable, never show its value)'
    if has_secret(c):
        return 'secret', 'command contains a literal secret (load it from .secrets or .env instead)'
    full = _expand_data_files(c)
    # Martin-only
    if re.search(r'\bstripe\b|api\.stripe\.com|paypal\.com/v\d|/refunds?\b|/charges\b', c, re.I):
        return 'M', 'payment or refund API'
    if re.search(r'\b(drop\s+(table|schema|database|function)|truncate\s+)', c, re.I):
        return 'M', 'drop or truncate'
    if re.search(r'(-X\s*|--request\s+)DELETE\b|\bdelete\s+from\b', c, re.I) and not has_test_marker(full):
        return 'M', 'delete on live data (TEST-741 records may be deleted by the agent)'
    if re.search(r'\b(grant|revoke)\s+\w+|alter\s+role|create\s+(role|user)\b|/users/invite|/invitations?\b', c, re.I):
        return 'M', 'permissions or invites'
    # switch on / publish
    switch = [
        (r'\blaunchctl\s+(load|bootstrap|enable|kickstart)\b', 'loads a LaunchAgent'),
        (r'\bcrontab\s+(?!-l\b)\S', 'changes crontab'),
        (r'\bcron\.(schedule|alter_job)\b', 'schedules a pg_cron job'),
        (r'\bgit\s+push\b', 'git push (deploys on GitHub Pages and CI)'),
        (r'\b(lftp|ncftp|sftp|ftp)\b|\bscp\s+\S+\s+\S+:|\brsync\b[^|;&]*\S+@\S+:|curl[^|;&]*(-T\b|--upload-file|ftps?://)|ftplib', 'uploads files to a server'),
        (r'\bsupabase\s+(functions\s+deploy|db\s+push)\b|\bnetlify\s+deploy\b|\bvercel\b[^|;&]*--prod|\bwrangler\s+(deploy|publish)\b', 'deploys'),
        (r'/workflows/[\w-]+/activate|/api/v1/workflows/[\w-]+/activate', 'activates an n8n workflow'),
        (r'\b(live_send_enabled|\w*_enabled|is_live|live)\s*=\s*true\b', 'sets a live switch to true'),
    ]
    for pat, why in switch:
        if re.search(pat, c, re.I):
            return 'G', why
    # messages to people
    sends = [
        r'api\.resend\.com/emails', r'api\.telegram\.org/bot[^\s/]*/send', r'api\.twilio\.com/[^\s]*/(Messages|Calls)',
        r'graph\.facebook\.com/[^\s]*/(messages|media_publish)', r'api\.sendgrid\.com/v3/mail', r'api\.brevo\.com/v3/smtp',
        r'smartlead\.ai/api/v1/campaigns/[^\s]*/(status|start)', r'hooks\.slack\.com/', r'api\.whatsapp\.com|/whatsapp/',
        r'osascript[^|;&]*(Mail|Airmailer|Messages)', r'\bsendmail\b|\bmail\s+-s\b',
    ]
    for pat in sends:
        if re.search(pat, c, re.I):
            if recipients_all_test(full) or has_test_marker(full):
                return 'test_write', 'message to a 741 test inbox only'
            return 'G', 'sends a message to real people'
    # generic writes over HTTP to external hosts
    if re.search(r'\bcurl\b', c) and re.search(r'(-X\s*|--request\s+)(POST|PUT|PATCH)\b|\s(-d|--data|--data-binary|--data-raw|-F|--form)\s', c, re.I):
        if re.search(r'https?://(localhost|127\.0\.0\.1|\[::1\])', c):
            return 'test_write', 'local write'
        if has_test_marker(full) or recipients_all_test(full):
            return 'test_write', 'write on TEST-741 data'
        return 'G', 'write over HTTP on live data without the TEST-741 marker'
    return 'read', ''


def classify_sql(sql):
    s = sql or ''
    if re.search(r'\b(drop\s+(table|schema|function|policy|trigger)|truncate)\b', s, re.I):
        return 'M', 'drop or truncate'
    if re.search(r'\b(grant|revoke)\b|\balter\s+role\b|\bcreate\s+(role|user)\b|\b(create|alter|drop)\s+policy\b|disable\s+row\s+level\s+security|\bauth\.users\b', s, re.I):
        return 'M', 'permissions, policies or auth users'
    if re.search(r'\bdelete\s+from\b', s, re.I):
        return ('test_write', 'delete of TEST-741 rows') if has_test_marker(s) else ('M', 'delete on live rows')
    if re.search(r'\bcron\.(schedule|alter_job)\b|\bnet\.http_post\b', s, re.I):
        return 'G', 'schedules a job or sends an HTTP request from the database'
    if re.search(r'\b\w*(enabled|is_live|live)\s*=\s*true\b|\bstatus\s*=\s*\'(active|live|running|published|sent|sending)\'', s, re.I):
        return 'G', 'switches something live'
    if re.search(r'^\s*(with\b[\s\S]*?\)\s*)?(select|explain|show)\b', s, re.I) and not re.search(r'\b(insert|update|delete|create|alter)\b', s, re.I):
        return 'read', ''
    if re.search(r'\b(insert|update|upsert|create|alter|comment\s+on)\b', s, re.I):
        return ('test_write', 'write on TEST-741 rows') if has_test_marker(s) else ('G', 'write on live database rows')
    return 'read', ''


JS_WRITE = RE(r'\.click\s*\(|\bsubmit\s*\(|\bfetch\s*\(|XMLHttpRequest|\$\.(ajax|post)|\.setData\s*\(|dispatchEvent|'
              r'\.value\s*=|\bsetContent\s*\(|\.save\s*\(|requestSubmit')


def classify(tool_name, tool_input):
    """Return (class, reason)."""
    name = tool_name or ''
    ti = tool_input if isinstance(tool_input, dict) else {}
    blob = blob_of(tool_input)
    if name in READ_TOOLS:
        return 'read', ''
    if name in ('Write', 'Edit', 'NotebookEdit', 'MultiEdit'):
        path = (ti.get('file_path') or ti.get('notebook_path') or '').replace('\\', '/')
        if touches_hook_state(path):
            return 'ledger', 'file is hook state'
        content = ' '.join(str(ti.get(k, '')) for k in ('content', 'new_string', 'new_source'))
        if not SECRET_FILE_RE.search(path) and has_secret(content):
            return 'secret', f'secret in a normal file ({os.path.basename(path)}); keep secrets in .secrets/ or .env only'
        return 'read', ''
    if name == 'Bash':
        return classify_bash(ti.get('command', ''))

    short = name.split('__')[-1] if name.startswith('mcp__') else name
    server = name.split('__')[1] if name.startswith('mcp__') and name.count('__') >= 2 else ''

    # Browser clicks: judge by the action summary Claude must write
    if short in ('computer',) or (short == 'browser_batch'):
        actions = ti.get('actions') if short == 'browser_batch' else [{'name': 'computer', 'input': ti}]
        worst = ('read', '')
        for a in actions or []:
            sub = classify(('mcp__' + server + '__' + a.get('name', '')) if server else a.get('name', ''), a.get('input', {})) \
                if a.get('name') != 'computer' else _classify_click(a.get('input', {}))
            worst = _worse(worst, sub)
        return worst
    if short in ('javascript_tool', 'execute_javascript'):
        code = ti.get('text') or ti.get('code') or ti.get('script') or blob
        return ('G', 'page script that clicks, posts or changes values') if JS_WRITE.search(code) else ('read', '')
    if short in ('form_input', 'file_upload', 'upload_image', 'gif_creator'):
        return 'test_write', 'form value in the browser (saved only by a later click)'
    if short in ('shortcuts_execute',):
        return 'G', 'runs a browser shortcut with unknown effect'

    # Native apps (computer use): messaging apps are class G
    if server == 'computer-use' and re.search(r'click|key|type|batch|drag|write_clipboard', short):
        if re.search(r'Airmailer|"Mail"|Messages|WhatsApp|Telegram|Slack|Signal|Outlook', blob, re.I):
            return 'G', 'acts in a messaging app'
        return 'test_write', 'native app input'

    # SQL and Supabase
    if short in ('execute_sql',):
        return classify_sql(ti.get('query', ''))
    if short in ('apply_migration',):
        return 'G', 'database migration on a live project'
    if short in ('deploy_edge_function',):
        return 'G', 'deploys an edge function'
    if short in ('create_project', 'pause_project', 'create_branch', 'merge_branch', 'reset_branch', 'delete_branch',
                 'rebase_branch', 'confirm_cost'):
        return 'M', 'project, branch or cost change'
    if short in ('restore_project',):
        return 'G', 'restores a paused project'

    # Generic MCP rules
    if re.search(r'"method"\s*:\s*"DELETE"|\bDELETE\s+/|"(action|operation)"\s*:\s*"(delete|remove|trash)\w*"', blob, re.I):
        return ('test_write', 'delete of TEST-741 data') if has_test_marker(blob) else ('M', f'{short}: delete through the API')
    if re.search(r'(^|_)(delete|trash|remove|unpublish)', short, re.I):
        return ('test_write', 'delete of TEST-741 data') if has_test_marker(blob) else ('M', f'{short}: delete')
    if re.search(r'(^|_)(register_domain|renew_domain|transfer_domain|create_hosting|update_nameservers|share|role_update|'
                 r'move_to_team|update_auto_renew|sandbox_topup)', short, re.I):
        return 'M', f'{short}: money, ownership or permissions'
    if re.search(r'(^|_)(create_event|update_event|respond_to_event)$', short, re.I):
        return 'G', f'{short}: calendar invites reach real people'
    if re.search(r'(deploy|publish|StartDeploy|ManageWixSite|execute-ability|execute_ability|ExecuteWixAPI|CallWixSiteAPI|'
                 r'create_dns|update_dns|create_url_forward|create_webhook|update_webhook|manage_marketing_email|'
                 r'manage_website_page|manage_landing_page|manage_blog_post)', short, re.I):
        if re.search(r'"method"\s*:\s*"GET"', blob) and not re.search(r'publish|send', blob, re.I):
            return 'read', ''
        if re.search(r'"(action|operation)"\s*:\s*"(get|list|read|search)', blob, re.I):
            return 'read', ''
        return 'G', f'{short}: changes a live site, DNS or sends'
    if READ_VERB.search(short):
        return 'read', ''
    # any other MCP write
    if re.search(r'send|email|message|notify|sms|whatsapp', blob, re.I) and not (recipients_all_test(blob) or has_test_marker(blob)):
        if re.search(r'"(to|recipient|recipients|email|phone|chat_id)"', blob, re.I):
            return 'G', f'{short}: message to real people'
    if has_test_marker(blob) or recipients_all_test(blob):
        return 'test_write', f'{short}: write on TEST-741 data'
    if name.startswith('mcp__'):
        return 'G', f'{short}: write on live data without the TEST-741 marker'
    return 'read', ''


def _classify_click(ci):
    action = (ci or {}).get('action', '')
    if action in ('screenshot', 'scroll', 'scroll_to', 'zoom', 'hover', 'wait'):
        return 'read', ''
    summary = (ci or {}).get('action_summary', '') or ''
    text = summary + ' ' + str((ci or {}).get('text', '') if action == 'key' else '')
    if M_WORDS.search(summary):
        if DRAFTISH.search(summary):
            return 'test_write', 'click on draft or TEST data'
        return 'M', f'click: "{summary[:80]}" (delete, money, prices, invites or permissions)'
    if G_WORDS.search(summary) or re.search(r'\b(cmd|ctrl)\+(enter|return)\b', text, re.I):
        if DRAFTISH.search(summary) and not re.search(r'publish|veröffentlich|live|activat|aktivier|turn on|einschalt|send|senden', summary, re.I):
            return 'test_write', 'click on draft or TEST data'
        return 'G', f'click: "{summary[:80]}" (send, publish or switch on)'
    if action in ('left_click', 'double_click', 'triple_click', 'right_click', 'left_click_drag', 'key', 'type'):
        if not summary.strip():
            return 'G', 'click without action_summary (write one so the guard can judge it)'
        return 'test_write', 'UI input (read the state back after it)'
    return 'read', ''


ORDER = {'read': 0, 'test_write': 1, 'G': 2, 'secret': 3, 'ledger': 3, 'M': 4}


def _worse(a, b):
    return a if ORDER.get(a[0], 0) >= ORDER.get(b[0], 0) else b
