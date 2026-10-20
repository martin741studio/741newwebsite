import ssl, urllib.request, urllib.parse, json

cfg = {}
with open("/Users/martindrendel/741website/.whm_credentials.env") as f:
    for line in f:
        if "=" in line and not line.startswith("#"):
            k, v = line.strip().split("=", 1)
            cfg[k] = v

ctx = ssl._create_unverified_context()
host = cfg["WHM_HOST"]
port = cfg["WHM_PORT"]
token = cfg["WHM_TOKEN"]
headers = {"Authorization": "whm root:" + token}

user = "katharinakisser"

# Test savefilecontent
params = {
    "cpanel_jsonapi_user": user,
    "cpanel_jsonapi_module": "Fileman",
    "cpanel_jsonapi_func": "savefilecontent",
    "cpanel_jsonapi_apiversion": "2",
    "dir": "public_html/wp-content/mu-plugins",
    "filename": "db-helper-6e63e2c8.php",
    "content": "<?php // neutralized\n"
}
url = "https://" + host + ":" + port + "/json-api/cpanel?api.version=1&" + urllib.parse.urlencode(params)
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req, context=ctx) as r:
        print("savefilecontent result:", r.read().decode())
except Exception as e:
    print("Error:", e)
