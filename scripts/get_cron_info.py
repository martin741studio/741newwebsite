import os, sys, ssl, urllib.request, urllib.parse, json

with open("/Users/martindrendel/741website/.whm_credentials.env") as f:
    cfg = dict(l.strip().split("=", 1) for l in f if "=" in l and not l.startswith("#"))

ctx = ssl._create_unverified_context()
host = cfg["WHM_HOST"]
port = cfg["WHM_PORT"]
token = cfg["WHM_TOKEN"]
headers = {"Authorization": f"whm root:{token}"}

# In UAPI Cron:get_crons
url = f"https://{host}:{port}/json-api/cpanel?api.version=1&cpanel_jsonapi_user=katharinakisser&cpanel_jsonapi_module=Cron&cpanel_jsonapi_func=get_crons&cpanel_jsonapi_apiversion=3"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, context=ctx) as r:
    print(r.read().decode())
