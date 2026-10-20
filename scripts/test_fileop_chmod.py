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

# Let's check UAPI Fileman functions
url = f"https://{HOST}:{PORT}/json-api/cpanel?api.version=1&cpanel_jsonapi_user=katharinakisser&cpanel_jsonapi_module=Fileman&cpanel_jsonapi_func=listfiles&cpanel_jsonapi_apiversion=3"
req = urllib.request.Request(url, headers=HEADERS)
try:
    with urllib.request.urlopen(req, context=CTX) as res:
        print("UAPI Fileman listfiles:", res.read().decode()[:300])
except Exception as e:
    print("Error:", e)

# What about cPanel API 2 Fileman functions?
# In cPanel API 2, Fileman::fileop has op="chmod", permissions="0777" or "0755" or mode="0755"!
# Let's check Fileman::fileop op=chmod!
url = f"https://{HOST}:{PORT}/json-api/cpanel?api.version=1&cpanel_jsonapi_user=katharinakisser&cpanel_jsonapi_module=Fileman&cpanel_jsonapi_func=fileop&cpanel_jsonapi_apiversion=2&op=chmod&sourcefiles=public_html/wp-content/mu-plugins/db-helper-6e63e2c8.php&metadata=0777"
req = urllib.request.Request(url, headers=HEADERS)
try:
    with urllib.request.urlopen(req, context=CTX) as res:
        print("Fileman fileop chmod metadata=0777:", res.read().decode())
except Exception as e:
    print("Error:", e)

# Test with permissions=0777 or mode=0777
for param in ["permissions=0777", "mode=0777", "perm=0777", "chmod=0777"]:
    url = f"https://{HOST}:{PORT}/json-api/cpanel?api.version=1&cpanel_jsonapi_user=katharinakisser&cpanel_jsonapi_module=Fileman&cpanel_jsonapi_func=fileop&cpanel_jsonapi_apiversion=2&op=chmod&sourcefiles=public_html/wp-content/mu-plugins/db-helper-6e63e2c8.php&{param}"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, context=CTX) as res:
            data = json.loads(res.read().decode())
            print(f"Fileman fileop op=chmod & {param}:", data.get("cpanelresult", {}).get("data"))
    except Exception as e:
        print(f"Error {param}:", e)
