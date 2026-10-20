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

def cpanel_uapi(user, module, func, **kwargs):
    url = f"https://{HOST}:{PORT}/json-api/cpanel?api.version=1&cpanel_jsonapi_user={user}&cpanel_jsonapi_module={module}&cpanel_jsonapi_func={func}&cpanel_jsonapi_apiversion=3"
    if kwargs:
        url += f"&{urllib.parse.urlencode(kwargs)}"
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, context=CTX) as res:
        return json.loads(res.read().decode())

def cpanel_api2(user, module, func, **kwargs):
    params = {
        "cpanel_jsonapi_user": user,
        "cpanel_jsonapi_module": module,
        "cpanel_jsonapi_func": func,
        "cpanel_jsonapi_apiversion": "2"
    }
    params.update(kwargs)
    url = f"https://{HOST}:{PORT}/json-api/cpanel?api.version=1&{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, context=CTX) as res:
        return json.loads(res.read().decode())

# Check mu-plugins
print("--- Checking mu-plugins ---")
res = cpanel_api2("katharinakisser", "Fileman", "listfiles", dir="public_html/wp-content/mu-plugins")
print(json.dumps(res, indent=2))

# Check uploads/.cache-dir
print("--- Checking uploads/.cache-dir ---")
res2 = cpanel_api2("katharinakisser", "Fileman", "listfiles", dir="public_html/wp-content/uploads/.cache-dir")
print(json.dumps(res2, indent=2))

# Check uploads/2026/10/.thumbnails
print("--- Checking uploads/2026/10/.thumbnails ---")
res3 = cpanel_api2("katharinakisser", "Fileman", "listfiles", dir="public_html/wp-content/uploads/2026/10/.thumbnails")
print(json.dumps(res3, indent=2))
