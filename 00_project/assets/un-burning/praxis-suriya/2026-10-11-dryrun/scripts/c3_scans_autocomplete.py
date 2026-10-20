import sys, json, urllib.request, urllib.parse
sys.path.insert(0, __file__.rsplit('/',1)[0])
from ub_lib import save_evidence
env = {}
for l in open('/Users/martindrendel/741website/.secrets/standup.env'):
    l = l.strip()
    if l and not l.startswith('#') and '=' in l:
        k, v = l.split('=', 1); env[k.strip()] = v.strip()
BASE = env['SUPABASE_URL']; CID = '3f71ef33-8c74-4ea1-b2d3-0273c2e99649'
req = urllib.request.Request(BASE + '/auth/v1/token?grant_type=password', data=json.dumps({'email': env['STANDUP_EMAIL'], 'password': env['STANDUP_PASSWORD']}).encode(), headers={'apikey': env['SUPABASE_ANON'], 'Content-Type': 'application/json'}, method='POST')
tok = json.load(urllib.request.urlopen(req, timeout=30))['access_token']
def get(path):
    r = urllib.request.Request(BASE + '/rest/v1/' + path, headers={'apikey': env['SUPABASE_ANON'], 'Authorization': 'Bearer ' + tok}, method='GET')
    return urllib.request.urlopen(r, timeout=60).read()
try:
    b = get(f'scans?client_id=eq.{CID}&select=*&order=created_at.desc&limit=30')
    save_evidence('EV-C-scans-existing', b, 'json', 'supabase postgrest GET (read-only)', f'GET /rest/v1/scans?client_id=eq.{CID}&select=*&order=created_at.desc&limit=30 [existing Falcon scans, read only]', subdir='area_c')
    d = json.loads(b); print('scans', len(d)); 
    if d: print(list(d[0].keys()))
except Exception as e:
    print('scans ERR', e)
# Autocomplete (free, no API key)
out = {}
for q in ["praxis suriya ingelheim erfahrungen", "praxis suriya ingelheim abzocke", "praxis suriya ingelheim bewertung", "praxis suriya ingelheim", "suriya ingelheim"]:
    u = 'https://suggestqueries.google.com/complete/search?client=firefox&hl=de&gl=de&q=' + urllib.parse.quote(q)
    r = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
    try: out[q] = json.loads(urllib.request.urlopen(r, timeout=30).read().decode('utf8', 'replace'))
    except Exception as e: out[q] = {'error': str(e)}
save_evidence('EV-D-autocomplete', json.dumps(out, ensure_ascii=False, indent=1), 'json', 'google suggestqueries (free)', 'GET suggestqueries.google.com/complete/search?client=firefox&hl=de&gl=de&q=<5 brand queries>', subdir='area_d')
for k, v in out.items(): print(k, '->', v[1] if isinstance(v, list) else v)
