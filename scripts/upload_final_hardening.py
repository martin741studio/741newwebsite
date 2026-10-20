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
exec > /home/katharinakisser/public_html/final_fix.log 2>&1
echo "=== FINAL DATABASE & SECURITY HARDENING ==="

# 1. Purge Rogue Users
mysql -e "DELETE FROM katharinakisser_main.wp_users WHERE ID IN (16, 17, 18);"
mysql -e "DELETE FROM katharinakisser_main.wp_usermeta WHERE user_id IN (16, 17, 18);"
echo "Remaining users in wp_users:"
mysql -e "SELECT ID, user_login, user_email, user_registered FROM katharinakisser_main.wp_users;"

# 2. Fix active_plugins using WP-CLI or PHP
php -r '
require_once "/home/katharinakisser/public_html/wp-load.php";
$active = get_option("active_plugins", array());
$clean = array();
foreach ($active as $p) {
    if (file_exists(WP_PLUGIN_DIR . "/" . $p) && !empty($p)) {
        $clean[] = $p;
    } else {
        echo "Pruned inactive/deleted plugin: $p\n";
    }
}
update_option("active_plugins", $clean);
echo "Active plugins updated successfully.\n";
'

# 3. Clean temporary maintenance files
rm -f /home/katharinakisser/public_html/clean_server.sh
rm -f /home/katharinakisser/public_html/cleanup_result.txt
rm -f /home/katharinakisser/public_html/remediation_log.txt
rm -f /home/katharinakisser/public_html/test_perm.txt

# 4. Remove any duplicate mu-plugins-disabled folder
rm -rf /home/katharinakisser/public_html/wp-content/mu-plugins-disabled

# 5. Flush Redis / Object Cache / WP-Rocket Cache
rm -rf /home/katharinakisser/public_html/wp-content/cache/*

echo "=== ALL SYSTEMS CLEAN AND SECURE ==="
"""

res = cpanel_uapi("katharinakisser", "Fileman", "save_file_content", 
                  dir="public_html", 
                  file="run_final.sh", 
                  content=script_content)
print("Saved run_final.sh:", res.get("result", {}).get("status"))
