#!/bin/bash
# READ-ONLY audit of the Tacheles WordPress install. Changes nothing on the server.
# Prints no secrets (wp-config is filtered).
for R in /mnt/web716/b2/87/57923587/htdocs/WordPress_01 "$HOME/WordPress_01" /WordPress_01 ./WordPress_01; do
  [ -f "$R/wp-config.php" ] && break
done
echo "ROOT=$R"; date; id; uname -a
echo; echo "== WP core version"; grep "wp_version =" "$R/wp-includes/version.php"
echo; echo "== mu-plugins"; ls -la --time-style=long-iso "$R/wp-content/mu-plugins" 2>&1
echo; echo "== wp-safe-mode dir"; ls -la --time-style=long-iso "$R/wp-content/wp-safe-mode" 2>&1
echo; echo "== plugins by mtime (newest first)"; ls -lat --time-style=long-iso "$R/wp-content/plugins" 2>&1 | head -60
echo; echo "== themes by mtime"; ls -lat --time-style=long-iso "$R/wp-content/themes" 2>&1 | head -20
echo; echo "== wp-content top level"; ls -la --time-style=long-iso "$R/wp-content" 2>&1
echo; echo "== PHP files changed in last 45 days (no cache/uploads)"
find "$R" -type f -name '*.php' -mtime -45 -not -path '*/cache/*' -not -path '*/uploads/*' -exec ls -l --time-style=long-iso {} + 2>&1 | sort -k6,7 -r | head -150
echo; echo "== PHP/PHTML/PHAR inside uploads"
find "$R/wp-content/uploads" -type f \( -name '*.php' -o -name '*.phtml' -o -name '*.phar' -o -name '*.php5' \) -exec ls -l --time-style=long-iso {} + 2>&1 | head -40
echo; echo "== Malware code patterns"
grep -rIl --include='*.php' -E 'eval\s*\(\s*(base64_decode|gzinflate|str_rot13|gzuncompress)|assert\s*\(\s*\$_(POST|REQUEST|GET)|shell_exec\s*\(\s*\$_|FilesMan|c99shell|wso_version|\$\{"\\x' "$R" 2>/dev/null | head -50
echo; echo "== Files with the conditional-inject signature (has_cap edit_posts + echo script)"
grep -rIl --include='*.php' -E "has_cap\('edit_posts'\)" "$R" 2>/dev/null | head -30
echo; echo "== Files mentioning the fake captcha / yandex counter"
grep -rIl -E 'mc\.yandex|cjs-container|checkbox-window|99162160|tag_phono' "$R" 2>/dev/null | head -30
echo; echo "== Casino/pharma spam words in PHP or HTML (outside uploads)"
grep -rIli --include='*.php' --include='*.html' --include='*.htm' -E 'casino|slot gacor|viagra|cialis|togel' "$R" --exclude-dir=uploads --exclude-dir=cache 2>/dev/null | head -30
echo; echo "== .htaccess files"
find "$R" -name '.htaccess' -exec ls -l --time-style=long-iso {} + 2>&1 | head -20
echo "--- root .htaccess ---"; head -80 "$R/.htaccess" 2>&1
echo; echo "== odd core leftovers"; ls -la --time-style=long-iso "$R/wp-includes/load.php.orig" "$R/wp-includes/load.php" "$R/wp-admin/.pid" 2>&1
echo "--- .pid ---"; head -c 400 "$R/wp-admin/.pid" 2>&1; echo
echo "--- diff load.php.orig -> load.php ---"; diff "$R/wp-includes/load.php.orig" "$R/wp-includes/load.php" 2>&1 | head -60
echo; echo "== web root listing"; ls -la --time-style=long-iso "$R" 2>&1
echo; echo "== .user.ini / php.ini / auto_prepend"; find "$R" -maxdepth 3 \( -name '.user.ini' -o -name 'php.ini' \) -exec sh -c 'echo "-- $1"; head -20 "$1"' _ {} \; 2>&1
echo; echo "== wp-config (filtered, no secrets)"; grep -E "WP_DEBUG|DISALLOW_FILE|table_prefix|WP_HOME|WP_SITEURL|auto_prepend|ini_set" "$R/wp-config.php" 2>&1
echo; echo "DONE"
