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

# 1. Test chmod on a file in mu-plugins
print("Attempting chmod 0777 on mu-plugins/db-helper-6e63e2c8.php...")
res_chmod = cpanel_api2(user, "Fileman", "chmodfile", 
                        dir="public_html/wp-content/mu-plugins", 
                        file="db-helper-6e63e2c8.php", 
                        mode="0777")
print(res_chmod)

# 2. Attempt unlink
print("Attempting unlink on mu-plugins/db-helper-6e63e2c8.php...")
res_unlink = cpanel_api2(user, "Fileman", "fileop", 
                         op="unlink", 
                         sourcefiles="public_html/wp-content/mu-plugins/db-helper-6e63e2c8.php")
print(res_unlink)
