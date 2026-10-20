import os, sys, ssl, urllib.request, urllib.parse, json

with open("/Users/martindrendel/741website/.whm_credentials.env") as f:
    cfg = dict(l.strip().split("=", 1) for l in f if "=" in l and not l.startswith("#"))

ctx = ssl._create_unverified_context()
host = cfg["WHM_HOST"]
port = cfg["WHM_PORT"]
token = cfg["WHM_TOKEN"]
headers = {"Authorization": f"whm root:{token}"}

params = {
    "cpanel_jsonapi_user": "katharinakisser",
    "cpanel_jsonapi_module": "Cron",
    "cpanel_jsonapi_func": "listcron",
    "cpanel_jsonapi_apiversion": "2"
}
url = f"https://{host}:{port}/json-api/cpanel?api.version=1&{urllib.parse.urlencode(params)}"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, context=ctx) as r:
    data = json.loads(r.read())
    print("listcron full:", json.dumps(data, indent=2))
