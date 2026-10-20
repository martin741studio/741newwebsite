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

# Check applist or available WHM API functions
try:
    res = whm_api("applist")
    print("applist keys:", list(res.keys()))
    if "data" in res:
        print("applist data sample:", res["data"][:5] if isinstance(res["data"], list) else res["data"])
except Exception as e:
    print("applist error:", e)

# Check if there is any terminal / shell / exec in WHM API
try:
    res = whm_api("get_available_applications")
    print("available apps:", res)
except Exception as e:
    print("get_available_applications error:", e)
