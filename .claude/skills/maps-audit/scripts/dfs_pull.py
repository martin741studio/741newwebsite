"""Phase 2 (after Go-A): DataForSEO backlinks summary (one target per call) and search volume. Logs cost_ledger.jsonl. Cap enforced (USD).
Usage: python3 dfs_pull.py <run_dir> backlinks <cap_usd> <domain,domain,...>
       python3 dfs_pull.py <run_dir> volume <cap_usd> <location_name> <kw|kw|kw>"""
import json, os, base64, urllib.request, datetime, sys
run, mode, cap = sys.argv[1], sys.argv[2], float(sys.argv[3])
env = {}
for l in open('/Users/martindrendel/741website/.secrets/dataforseo.env'):
    if '=' in l and not l.strip().startswith('#'):
        k, v = l.strip().split('=', 1); env[k.strip()] = v.strip().strip('"')
auth = 'Basic ' + base64.b64encode(f"{env['DATAFORSEO_LOGIN']}:{env['DATAFORSEO_PASSWORD']}".encode()).decode()
def post(path, body):
    req = urllib.request.Request('https://api.dataforseo.com/v3/' + path, json.dumps(body).encode(), {'Authorization': auth, 'Content-Type': 'application/json'})
    return json.loads(urllib.request.urlopen(req, timeout=120).read())
def ledger(**k): open(os.path.join(run, 'cost_ledger.jsonl'), 'a').write(json.dumps(dict(ts=datetime.datetime.now().astimezone().isoformat(timespec='seconds'), tool='dataforseo', **k)) + '\n')
spent = 0.0; now = datetime.datetime.now().astimezone().isoformat(timespec='seconds')
if mode == 'backlinks':
    out = {}
    for t in sys.argv[4].split(','):
        if spent >= cap: print('cap reached'); break
        r = post('backlinks/summary/live', [{'target': t, 'include_subdomains': True, 'backlinks_status_type': 'live'}])
        c = r.get('cost', 0) or 0; spent += c
        res = ((r.get('tasks') or [{}])[0].get('result') or [{}])[0] or {}
        out[t] = {k: res.get(k) for k in ('target', 'rank', 'backlinks', 'referring_domains', 'referring_main_domains', 'first_seen', 'backlinks_spam_score', 'broken_backlinks', 'broken_pages')}
        ledger(call='backlinks/summary/live', target=t, cost_usd=c); print(t, out[t]['rank'], out[t]['backlinks'], out[t]['referring_domains'], c)
    json.dump(dict(collected_at=now, spent_usd=spent, targets=out), open(os.path.join(run, 'evidence', 'backlinks-summary-2026-10-11.json'), 'w'), indent=1)
else:
    loc = sys.argv[4]; kws = sys.argv[5].split('|')
    r = post('keywords_data/google_ads/search_volume/live', [{'keywords': kws, 'location_name': loc, 'language_name': 'English'}])
    c = r.get('cost', 0) or 0; ledger(call='keywords_data/google_ads/search_volume/live', n_keywords=len(kws), cost_usd=c)
    res = (r.get('tasks') or [{}])[0].get('result') or []
    out = {x['keyword']: dict(volume=x.get('search_volume'), cpc=x.get('cpc'), competition=x.get('competition')) for x in res}
    json.dump(dict(collected_at=now, location=loc, cost_usd=c, keywords=out), open(os.path.join(run, 'evidence', 'search-volume-2026-10-11.json'), 'w'), indent=1)
    for k, v in sorted(out.items(), key=lambda kv: -(kv[1]['volume'] or 0)): print(k, v)
    print('cost', c)
