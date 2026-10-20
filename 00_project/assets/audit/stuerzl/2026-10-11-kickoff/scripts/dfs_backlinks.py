"""Phase 2 (after Go-A): DataForSEO backlinks summary, one target per call. Writes evidence + cost_ledger.jsonl. Cap enforced."""
import json, os, base64, urllib.request, datetime, sys
RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = {}
for l in open('/Users/martindrendel/741website/.secrets/dataforseo.env'):
    if '=' in l and not l.strip().startswith('#'):
        k, v = l.strip().split('=', 1); env[k.strip()] = v.strip().strip('"')
login = env.get('DATAFORSEO_LOGIN') or env.get('LOGIN') or list(env.values())[0]
pw = env.get('DATAFORSEO_PASSWORD') or env.get('PASSWORD') or list(env.values())[1]
auth = 'Basic ' + base64.b64encode(f'{login}:{pw}'.encode()).decode()
CAP_USD = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
targets = ['stuerzl-steuerstrafrecht.de', 'dreyenberg.com', 'anwalt-steuerrecht-frankfurt.de', 'die-anwalts-kanzlei.de', 'strafrecht-bundesweit.de', 'kanzlei-tikbas.de', 'pohl-legal.com']
spent = 0.0; out = {}
for t in targets:
    if spent >= CAP_USD: print('cap reached, stop'); break
    req = urllib.request.Request('https://api.dataforseo.com/v3/backlinks/summary/live', json.dumps([{'target': t, 'include_subdomains': True, 'backlinks_status_type': 'live'}]).encode(), {'Authorization': auth, 'Content-Type': 'application/json'})
    r = json.loads(urllib.request.urlopen(req, timeout=90).read())
    cost = r.get('cost', 0) or 0; spent += cost
    res = ((r.get('tasks') or [{}])[0].get('result') or [{}])[0]
    out[t] = {k: res.get(k) for k in ('target', 'rank', 'backlinks', 'referring_domains', 'referring_main_domains', 'referring_pages', 'first_seen', 'backlinks_spam_score', 'referring_domains_nofollow', 'broken_backlinks', 'broken_pages')}
    open(os.path.join(RUN, 'cost_ledger.jsonl'), 'a').write(json.dumps(dict(ts=datetime.datetime.now().astimezone().isoformat(timespec='seconds'), tool='dataforseo', call='backlinks/summary/live', target=t, cost_usd=cost)) + '\n')
    print(t, 'rank', out[t]['rank'], 'bl', out[t]['backlinks'], 'refdom', out[t]['referring_domains'], 'cost', cost)
json.dump(dict(collected_at=datetime.datetime.now().astimezone().isoformat(timespec='seconds'), spent_usd=spent, targets=out), open(os.path.join(RUN, 'evidence', 'backlinks-summary-2026-10-11.json'), 'w'), indent=1)
print('spent usd', round(spent, 4))
