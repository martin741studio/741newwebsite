import os, sys, ssl, urllib.request, urllib.parse, json

ENV_PATH = "/Users/martindrendel/741website/.whm_credentials.env"
CONFIG = {}
with open(ENV_PATH) as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            CONFIG[k.strip()] = v.strip()

HOST = CONFIG.get("WHM_HOST", "185.2.31.101")
PORT = CONFIG.get("WHM_PORT", "2087")
TOKEN = CONFIG.get("WHM_TOKEN", "")

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE
HEADERS = {"Authorization": f"whm root:{TOKEN}"}

def whm_api(endpoint, params=None):
    url = f"https://{HOST}:{PORT}/json-api/{endpoint}?api.version=1"
    if params:
        url += f"&{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, context=CTX) as res:
        return json.loads(res.read().decode())

res = whm_api("get_available_applications")
app_obj = res.get("data", {}).get("app", {})
print("Type of app:", type(app_obj))
if isinstance(app_obj, dict):
    print("Keys in app:", list(app_obj.keys()))
    for k, v in app_obj.items():
        if isinstance(v, list):
            for it in v:
                print(it.get("key"), it.get("url"))
elif isinstance(app_obj, list):
    for grp in app_obj:
        print("Grp:", grp.get("key"))
        for it in grp.get("items", []):
            print("  ", it.get("key"), it.get("url"))
