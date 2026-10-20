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

# In cPanel File Manager, when changing permissions:
# It calls: Fileman::fileop with op=chmod
# What are the exact parameters?
# Let's test combinations of parameters:
test_params = [
    {"op": "chmod", "sourcefiles": "public_html/wp-content/mu-plugins", "metadata": "0755"},
    {"op": "chmod", "sourcefiles": "public_html/wp-content/mu-plugins", "metadata": "755"},
    {"op": "chmod", "sourcefiles": "public_html/wp-content/mu-plugins", "permissions": "0755"},
    {"op": "chmod", "sourcefiles": "public_html/wp-content/mu-plugins", "permissions": "755"},
    {"op": "chmod", "sourcefiles": "public_html/wp-content/mu-plugins", "mode": "0755"},
    {"op": "chmod", "sourcefiles": "public_html/wp-content/mu-plugins", "mode": "755"},
    {"op": "chmod", "sourcefiles": "public_html/wp-content/mu-plugins", "perms": "0755"},
    {"op": "chmod", "sourcefiles": "public_html/wp-content/mu-plugins", "perms": "755"},
]

for p in test_params:
    params = {
        "cpanel_jsonapi_user": "katharinakisser",
        "cpanel_jsonapi_module": "Fileman",
        "cpanel_jsonapi_func": "fileop",
        "cpanel_jsonapi_apiversion": "2",
    }
    params.update(p)
    url = "https://" + host + ":" + port + "/json-api/cpanel?api.version=1&" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, context=ctx) as r:
        res = json.loads(r.read())
        print(f"Test {p}:", res.get("cpanelresult", {}).get("data"))
