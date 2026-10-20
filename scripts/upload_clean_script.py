import os, sys, ssl, urllib.request, urllib.parse, json

cfg = {}
with open("/Users/martindrendel/741website/.whm_credentials.env") as f:
    for line in f:
        if "=" in line and not line.startswith("#"):
            k, v = line.strip().split("=", 1)
            cfg[k] = v

ctx = ssl._create_unverified_context()
def cpanel_uapi(user, module, func, **kwargs):
    params = {
        "cpanel_jsonapi_user": user,
        "cpanel_jsonapi_module": module,
        "cpanel_jsonapi_func": func,
        "cpanel_jsonapi_apiversion": "3"
    }
    params.update(kwargs)
    url = "https://" + cfg["WHM_HOST"] + ":" + cfg["WHM_PORT"] + "/json-api/cpanel?api.version=1&" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"Authorization": "whm root:" + cfg["WHM_TOKEN"]})
    with urllib.request.urlopen(req, context=ctx) as r:
        return json.loads(r.read())

script_content = """#!/bin/bash
exec > /home/katharinakisser/public_html/cleanup_result.txt 2>&1
echo "=== ROOT CLEANUP START: $(date) ==="
id

echo "=== 1. UNLOCKING AND DELETING KATHARINAKISSER MALWARE ==="
chattr -R -i /home/katharinakisser/public_html/wp-content/mu-plugins* 2>/dev/null || true
rm -rf /home/katharinakisser/public_html/wp-content/mu-plugins*

chattr -R -i /home/katharinakisser/public_html/wp-content/uploads/.cache-dir 2>/dev/null || true
rm -rf /home/katharinakisser/public_html/wp-content/uploads/.cache-dir

chattr -R -i /home/katharinakisser/public_html/wp-content/uploads/*/.thumbnails 2>/dev/null || true
rm -rf /home/katharinakisser/public_html/wp-content/uploads/*/.thumbnails

chattr -R -i /home/katharinakisser/public_html/wp-content/plugins/*6e63e2c8* 2>/dev/null || true
rm -rf /home/katharinakisser/public_html/wp-content/plugins/*6e63e2c8*

# Recreate clean mu-plugins
mkdir -p /home/katharinakisser/public_html/wp-content/mu-plugins
chmod 755 /home/katharinakisser/public_html/wp-content/mu-plugins
chown -R katharinakisser:katharinakisser /home/katharinakisser/public_html/wp-content/mu-plugins

echo "=== 2. SEARCHING FOR ANY OTHER 6e63e2c8 FILES ACROSS ENTIRE SERVER ==="
find /home -name "*6e63e2c8*" 2>/dev/null | while read f; do
    echo "Found rogue file: $f"
    chattr -i "$f" 2>/dev/null || true
    rm -rf "$f"
    echo "Deleted: $f"
done

echo "=== 3. CHECKING ALL USER CRONS ==="
for c in /var/spool/cron/*; do
    echo "Crontab: $c"
    cat "$c"
done

echo "=== 4. CHECKING ACTIVE ROGUE PROCESSES ==="
ps aux | grep -E "6e63e2c8|cron-helper|theme-footer|db-helper" | grep -v grep || echo "No rogue processes running."

echo "=== 5. CHECKING RECENT KISSER PLUGINS ==="
ls -la /home/katharinakisser/public_html/wp-content/plugins
ls -la /home/katharinakisser/public_html/wp-content/mu-plugins

chmod 644 /home/katharinakisser/public_html/cleanup_result.txt
chown katharinakisser:katharinakisser /home/katharinakisser/public_html/cleanup_result.txt
echo "=== ROOT CLEANUP COMPLETED: $(date) ==="
"""

res = cpanel_uapi("katharinakisser", "Fileman", "save_file_content", 
                  dir="public_html", 
                  file="clean_server.sh", 
                  content=script_content)
print("Uploaded clean_server.sh:", res.get("result", {}).get("status"))
