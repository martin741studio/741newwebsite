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

user = "katharinakisser"

# List wp-content to see mu-plugins mode
res = cpanel_api2(user, "Fileman", "listfiles", dir="public_html/wp-content")
for item in res.get("cpanelresult", {}).get("data", []):
    if item.get("file") == "mu-plugins":
        print("mu-plugins dir info:", item)

# Let's try chmod on mu-plugins directory
print("Chmodding mu-plugins directory to 0755...")
cpanel_api2(user, "Fileman", "fileop", op="chmod", sourcefiles="public_html/wp-content/mu-plugins", metadata="0755")

# Check again
res2 = cpanel_api2(user, "Fileman", "listfiles", dir="public_html/wp-content")
for item in res2.get("cpanelresult", {}).get("data", []):
    if item.get("file") == "mu-plugins":
        print("mu-plugins dir info after chmod:", item.get("nicemode"))
