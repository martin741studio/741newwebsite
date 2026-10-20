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

def cpanel_api2(user, module, func, **kwargs):
    params = {
        "cpanel_jsonapi_user": user,
        "cpanel_jsonapi_module": module,
        "cpanel_jsonapi_func": func,
        "cpanel_jsonapi_apiversion": "2"
    }
    params.update(kwargs)
    url = f"https://{host}:{port}/json-api/cpanel?api.version=1&{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, context=ctx) as res:
        return json.loads(res.read().decode())

def cpanel_uapi(user, module, func, **kwargs):
    params = {
        "cpanel_jsonapi_user": user,
        "cpanel_jsonapi_module": module,
        "cpanel_jsonapi_func": func,
        "cpanel_jsonapi_apiversion": "3"
    }
    params.update(kwargs)
    url = f"https://{host}:{port}/json-api/cpanel?api.version=1&{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, context=ctx) as res:
        return json.loads(res.read().decode())

user = "katharinakisser"

# 1. Create a test file in public_html
print("Creating test file...")
res = cpanel_uapi(user, "Fileman", "save_file_content", dir="public_html", file="test_perm.txt", content="hello")
print(res)

# 2. Check its mode
res = cpanel_api2(user, "Fileman", "listfiles", dir="public_html")
for it in res.get("cpanelresult", {}).get("data", []):
    if it.get("file") == "test_perm.txt":
        print("Initial mode:", it.get("nicemode"))

# 3. Chmod it
res = cpanel_api2(user, "Fileman", "fileop", op="chmod", sourcefiles="public_html/test_perm.txt", metadata="0444")
print("Chmod result:", res.get("cpanelresult", {}).get("data"))

# 4. Check mode again
res = cpanel_api2(user, "Fileman", "listfiles", dir="public_html")
for it in res.get("cpanelresult", {}).get("data", []):
    if it.get("file") == "test_perm.txt":
        print("Mode after chmod 0444:", it.get("nicemode"))

# 5. Delete it
res = cpanel_api2(user, "Fileman", "fileop", op="unlink", sourcefiles="public_html/test_perm.txt")
print("Delete result:", res.get("cpanelresult", {}).get("data"))
