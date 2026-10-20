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
exec > /home/katharinakisser/public_html/csf_audit.txt 2>&1
echo "=== CSF CONFIG & HISTORY AUDIT ==="

echo "--- 1. Testing mode in csf.conf ---"
grep -E "^TESTING\s*=" /etc/csf/csf.conf 2>/dev/null

echo "--- 2. TCP_IN and TCP6_IN (Allowed incoming ports) ---"
grep -E "^TCP_IN\s*=" /etc/csf/csf.conf 2>/dev/null
grep -E "^TCP6_IN\s*=" /etc/csf/csf.conf 2>/dev/null

echo "--- 3. Port 8769 present in csf.conf? ---"
grep "8769" /etc/csf/csf.conf 2>/dev/null || echo "PORT 8769 NOT FOUND IN CSF.CONF!"

echo "--- 4. CSF Allow list (/etc/csf/csf.allow) ---"
head -n 25 /etc/csf/csf.allow 2>/dev/null

echo "--- 5. When and why was CSF disabled? (Searching bash_history) ---"
grep -E "csf\s+-[xefrd]|systemctl.*csf" /root/.bash_history 2>/dev/null | tail -n 20

echo "--- 6. Last LFD log entries before disable ---"
tail -n 25 /var/log/lfd.log 2>/dev/null

chmod 644 /home/katharinakisser/public_html/csf_audit.txt
chown katharinakisser:katharinakisser /home/katharinakisser/public_html/csf_audit.txt
"""

cpanel_uapi("katharinakisser", "Fileman", "save_file_content", 
            dir="public_html", 
            file="run_csf_audit.sh", 
            content=script_content)
print("Saved run_csf_audit.sh")
