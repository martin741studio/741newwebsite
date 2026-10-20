"""READ-ONLY PostgREST GET against Supabase project galjmtozcgxcwtzkzbpi. Never writes. Never prints secrets."""
import sys, json, urllib.request, urllib.parse
sys.path.insert(0, __file__.rsplit('/',1)[0])
from ub_lib import save_evidence
env = {}
for l in open('/Users/martindrendel/741website/.secrets/standup.env'):
    l = l.strip()
    if l and not l.startswith('#') and '=' in l:
        k, v = l.split('=', 1); env[k.strip()] = v.strip()
BASE = env['SUPABASE_URL']
CID = '3f71ef33-8c74-4ea1-b2d3-0273c2e99649'
def post_login():
    req = urllib.request.Request(BASE + '/auth/v1/token?grant_type=password',
        data=json.dumps({'email': env['STANDUP_EMAIL'], 'password': env['STANDUP_PASSWORD']}).encode(),
        headers={'apikey': env['SUPABASE_ANON'], 'Content-Type': 'application/json'}, method='POST')
    return json.load(urllib.request.urlopen(req, timeout=30))['access_token']
tok = post_login()
def get(path):
    req = urllib.request.Request(BASE + '/rest/v1/' + path, headers={'apikey': env['SUPABASE_ANON'], 'Authorization': 'Bearer ' + tok}, method='GET')
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()
loc = get(f'client_locations?client_id=eq.{CID}&select=*')
save_evidence('EV-C-client-locations', loc, 'json', 'supabase postgrest GET (read-only)', f'GET /rest/v1/client_locations?client_id=eq.{CID}&select=*  [admin login from standup.env, not stored]', subdir='area_c')
cit = get(f'client_citations?client_id=eq.{CID}&select=*,directory:directories(*)&limit=500')
save_evidence('EV-C-client-citations', cit, 'json', 'supabase postgrest GET (read-only)', f'GET /rest/v1/client_citations?client_id=eq.{CID}&select=*,directory:directories(*)&limit=500  [admin login from standup.env, not stored]', subdir='area_c')
cl = get(f'clients?id=eq.{CID}&select=id,name')
save_evidence('EV-C-client-row', cl, 'json', 'supabase postgrest GET (read-only)', f'GET /rest/v1/clients?id=eq.{CID}&select=id,name', subdir='area_c')
print(len(json.loads(loc)), len(json.loads(cit)))
