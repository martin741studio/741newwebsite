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
exec > /home/katharinakisser/public_html/remediation_log.txt 2>&1
echo "=============================================="
echo "   COMPREHENSIVE ROOT REMEDIATION & LOCKDOWN  "
echo "   Date: $(date)                              "
echo "=============================================="
id

DIR="/home/katharinakisser/public_html"

echo "=== 1. UNLOCKING ALL ATTRIBUTES ==="
chattr -R -i "$DIR/wp-content" 2>/dev/null || true

echo "=== 2. REMOVING MALWARE PLUGINS ==="
rm -rf "$DIR/wp-content/plugins/plugin-editor-pro"
rm -rf "$DIR/wp-content/plugins/cache-helper-"*
rm -rf "$DIR/wp-content/plugins/media-cache-"*
rm -rf "$DIR/wp-content/plugins/wordfence-"*
rm -rf "$DIR/wp-content/plugins/filester"

echo "=== 3. PURGING & REBUILDING MU-PLUGINS ==="
rm -rf "$DIR/wp-content/mu-plugins"*
mkdir -p "$DIR/wp-content/mu-plugins"
cat << 'EOF' > "$DIR/wp-content/mu-plugins/index.php"
<?php
// Silence is golden.
EOF
chmod 755 "$DIR/wp-content/mu-plugins"
chown -R katharinakisser:katharinakisser "$DIR/wp-content/mu-plugins"

echo "=== 4. REMOVING UPLOADS BACKDOOR DIRECTORIES ==="
rm -rf "$DIR/wp-content/uploads/.cache-dir"
rm -rf "$DIR/wp-content/uploads/"*".thumbnails"
rm -rf "$DIR/wp-content/debug"

echo "=== 5. BLOCKING PHP EXECUTION IN UPLOADS ==="
cat << 'EOF' > "$DIR/wp-content/uploads/.htaccess"
<Files *.php>
Order Deny,Allow
Deny from all
</Files>
<Files *.php5>
Order Deny,Allow
Deny from all
</Files>
<Files *.phtml>
Order Deny,Allow
Deny from all
</Files>
EOF
chown katharinakisser:nobody "$DIR/wp-content/uploads/.htaccess"
chmod 444 "$DIR/wp-content/uploads/.htaccess"
chattr +i "$DIR/wp-content/uploads/.htaccess" 2>/dev/null || true

echo "=== 6. CHECKING DATABASE WP_USERS FOR ROGUE ADMINS ==="
mysql -e "SELECT ID, user_login, user_email, user_registered FROM katharinakisser_main.wp_users;"

echo "=== 7. CLEANING ACTIVE_PLUGINS OPTION IN DATABASE ==="
# Deactivate plugin-editor-pro and 6e63e2c8 plugins in DB
mysql -e "
UPDATE katharinakisser_main.wp_options 
SET option_value = REPLACE(option_value, 'plugin-editor-pro/plugin-editor-pro.php', '') 
WHERE option_name = 'active_plugins';
"
mysql -e "
SELECT option_value FROM katharinakisser_main.wp_options WHERE option_name = 'active_plugins';
"

echo "=== 8. REMOVING ANY CRON PERSISTENCE ==="
crontab -u katharinakisser -r 2>/dev/null || true
echo "Cleared katharinakisser crontab."

echo "=== 9. VERIFYING DISALLOW_FILE_EDIT IN WP-CONFIG ==="
WP_CFG="$DIR/wp-config.php"
if [ -f "$WP_CFG" ]; then
    chattr -i "$WP_CFG" 2>/dev/null || true
    if ! grep -q "DISALLOW_FILE_EDIT" "$WP_CFG"; then
        sed -i "2i define( 'DISALLOW_FILE_EDIT', true );" "$WP_CFG"
        sed -i "3i define( 'DISALLOW_FILE_MODS', true );" "$WP_CFG"
    fi
    chmod 400 "$WP_CFG"
fi

echo "=== 10. RESTARTING WEB SERVICES ==="
systemctl restart ea-php*-php-fpm 2>/dev/null || /scripts/restartsrv_cpanel_php_fpm 2>/dev/null || true
systemctl restart httpd 2>/dev/null || /scripts/restartsrv_httpd 2>/dev/null || true

echo "=== 11. FINAL SCAN FOR ANY LINGERING 6e63e2c8 FILES ==="
find /home -name "*6e63e2c8*" 2>/dev/null | while read f; do
    echo "LINGERING: $f"
    chattr -i "$f" 2>/dev/null || true
    rm -rf "$f"
done

chmod 644 /home/katharinakisser/public_html/remediation_log.txt
chown katharinakisser:katharinakisser /home/katharinakisser/public_html/remediation_log.txt
echo "=== COMPREHENSIVE REMEDIATION FINISHED: $(date) ==="
"""

res = cpanel_uapi("katharinakisser", "Fileman", "save_file_content", 
                  dir="public_html", 
                  file="clean_server.sh", 
                  content=script_content)
print("Updated clean_server.sh:", res.get("result", {}).get("status"))
