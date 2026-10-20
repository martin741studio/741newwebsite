import os, sys, ssl, urllib.request, urllib.parse, json

cfg = {}
with open("/Users/martindrendel/741website/.whm_credentials.env") as f:
    for line in f:
        if "=" in line and not line.startswith("#"):
            k, v = line.strip().split("=", 1)
            cfg[k] = v

ctx = ssl._create_unverified_context()
def whm_api(endpoint, params=None):
    host = cfg["WHM_HOST"]
    port = cfg["WHM_PORT"]
    token = cfg["WHM_TOKEN"]
    url = f"https://{host}:{port}/json-api/{endpoint}?api.version=1"
    if params:
        url += f"&{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"Authorization": f"whm root:{token}"})
    with urllib.request.urlopen(req, context=ctx) as res:
        return json.loads(res.read().decode())

print("=== 1. API TOKENS ===")
tokens = whm_api("api_token_list")
print("Tokens response:", json.dumps(tokens.get("data", {}), indent=2))

print("\n=== 2. SYSTEM LOAD & SERVICES ===")
load = whm_api("systemloadavg")
print("Load:", load.get("data"))

print("\n=== 3. ACCOUNTS LIST ===")
accts = whm_api("listaccts")
acct_list = accts.get("data", {}).get("acct", [])
print("Total accounts:", len(acct_list))
for a in acct_list:
    print(f"- {a.get('user'):16} : {a.get('domain'):30} (Disk: {a.get('diskused')}, Suspended: {a.get('suspended')})")
