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

audit_script = """#!/bin/bash
exec > /home/katharinakisser/public_html/deep_audit_report.txt 2>&1
echo "=========================================================="
echo "      DEEP WHM & SERVER SECURITY AUDIT - 185.2.31.101     "
echo "      Generated at: $(date)                               "
echo "=========================================================="
id
uname -a
uptime

echo ""
echo "=== 1. TOP PROCESSES BY CPU & MEMORY ==="
ps aux --sort=-%cpu | head -n 25

echo ""
echo "=== 2. SUSPICIOUS BACKGROUND PROCESSES (php, perl, python, bash, sh, curl, wget, socat, nc, miner) ==="
ps aux | grep -iE 'miner|xmrig|kdevtmpfsi|kinsing|xmr|stratum|\.pl|\.py|\.sh|curl.*\||wget.*\|' | grep -v grep || echo "None found."

echo ""
echo "=== 3. NETWORK LISTENING PORTS & ESTABLISHED CONNECTIONS ==="
echo "--- Listening Ports (ss -tulpn) ---"
ss -tulpn 2>/dev/null || netstat -tulpn 2>/dev/null

echo "--- Outgoing / Established Connections (ss -tunp) ---"
ss -tunp state established 2>/dev/null | head -n 30

echo ""
echo "=== 4. CRON JOBS ACROSS ENTIRE SERVER ==="
echo "--- /var/spool/cron (User Crontabs) ---"
for c in /var/spool/cron/*; do
    if [ -f "$c" ] && [ -s "$c" ]; then
        echo ">>> Crontab for $(basename $c):"
        cat "$c"
        echo ""
    fi
done

echo "--- /etc/crontab & /etc/cron.* ---"
cat /etc/crontab 2>/dev/null
ls -la /etc/cron.d/ /etc/cron.daily/ /etc/cron.hourly/ 2>/dev/null

echo ""
echo "=== 5. SSH & WHM AUTHENTICATION LOGS (Recent Logins & Failures) ==="
echo "--- Successful SSH logins (last 50) ---"
grep "Accepted " /var/log/secure* 2>/dev/null | tail -n 30 || grep "Accepted " /var/log/auth.log* 2>/dev/null | tail -n 30 || echo "No accepted logins found in logs."

echo "--- Recent Root Logins (lastlog / last) ---"
last -n 20 2>/dev/null

echo "--- WHM Login Log (/usr/local/cpanel/logs/login_log) ---"
tail -n 30 /usr/local/cpanel/logs/login_log 2>/dev/null || echo "login_log not found."

echo ""
echo "=== 6. ROOT AUTHORIZED_KEYS & SSH CONFIG ==="
echo "--- /root/.ssh/authorized_keys ---"
cat /root/.ssh/authorized_keys 2>/dev/null || echo "None."

echo ""
echo "=== 7. SUSPICIOUS FILES IN /tmp, /var/tmp, /dev/shm ==="
ls -la /tmp 2>/dev/null | head -n 30
ls -la /var/tmp 2>/dev/null | head -n 30
ls -la /dev/shm 2>/dev/null | head -n 30

echo ""
echo "=== 8. SCANNING ALL 21 CPANEL ACCOUNTS FOR MALWARE ARTIFACTS ==="
echo "--- Checking for any rogue PHP in uploads across all accounts ---"
find /home/*/public_html/wp-content/uploads/ -type f \( -name "*.php*" -o -name "*.phtml" -o -name "*.ico" \) 2>/dev/null | grep -v "/cache/" | head -n 50 || echo "None."

echo "--- Checking for any mu-plugins across all accounts ---"
for d in /home/*/public_html/wp-content/mu-plugins; do
    if [ -d "$d" ]; then
        echo ">>> $d:"
        ls -la "$d"
    fi
done

echo "--- Checking for known malware campaign signatures (*6e63e2c8*, *ayyplim*, *wphc*, *auto-cache*) ---"
find /home/ -name "*6e63e2c8*" -o -name "*ayyplim*" -o -name "*wphc*" -o -name "*auto-cache*" 2>/dev/null || echo "None."

echo ""
echo "=== 9. SECURITY TOOLS & FIREWALL STATUS ==="
which csf 2>/dev/null && csf -l | head -n 20 || echo "CSF status checked."
which iptables 2>/dev/null && iptables -L -n -v | head -n 30 || echo "iptables checked."

chmod 644 /home/katharinakisser/public_html/deep_audit_report.txt
chown katharinakisser:katharinakisser /home/katharinakisser/public_html/deep_audit_report.txt
echo "=========================================================="
echo "            AUDIT COMPLETED: $(date)                      "
echo "=========================================================="
"""

res = cpanel_uapi("katharinakisser", "Fileman", "save_file_content", 
                  dir="public_html", 
                  file="run_deep_audit.sh", 
                  content=audit_script)
print("Uploaded run_deep_audit.sh:", res.get("result", {}).get("status"))
