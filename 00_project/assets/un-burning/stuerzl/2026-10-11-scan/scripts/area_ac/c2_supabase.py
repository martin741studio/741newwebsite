"""READ-ONLY PostgREST GET. Never writes. Never prints secrets."""
import sys, json, urllib.request
sys.path.insert(0, __file__.rsplit('/',1)[0])
from ub_lib import save_evidence
env = {}
for l in open('/Users/martindrendel/741website/.secrets/standup.env'):
    l = l.strip()
    if l and not l.startswith('#') and '=' in l:
        k, v = l.split('=', 1); env[k.strip()] = v.strip()
BASE = env['SUPABASE_URL']; CID = 'b6f6e303-50e4-4afb-a343-337206cec316'
req = urllib.request.Request(BASE + '/auth/v1/token?grant_type=password',
    data=json.dumps({'email': env['STANDUP_EMAIL'], 'password': env['STANDUP_PASSWORD']}).encode(),
    headers={'apikey': env['SUPABASE_ANON'], 'Content-Type': 'application/json'}, method='POST')
tok = json.load(urllib.request.urlopen(req, timeout=30))['access_token']
def get(path):
    req = urllib.request.Request(BASE + '/rest/v1/' + path, headers={'apikey': env['SUPABASE_ANON'], 'Authorization': 'Bearer ' + tok}, method='GET')
    with urllib.request.urlopen(req, timeout=60) as r: return r.read()
for eid, path in [('EV-C-client-locations', f'client_locations?client_id=eq.{CID}&select=*'),
                  ('EV-C-client-citations', f'client_citations?client_id=eq.{CID}&select=*,directory:directories(*)&limit=500'),
                  ('EV-C-client-row', f'clients?id=eq.{CID}&select=id,name,status')]:
    b = get(path)
    save_evidence(eid, b, 'json', 'supabase postgrest GET (read-only)', f'GET /rest/v1/{path}  [admin login from standup.env, not stored]', 'area_c')
    print(eid, len(json.loads(b)))
