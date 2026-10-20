#!/bin/bash
set -e

DIR="/home/physiotherapiekr/public_html"
THEME_FUNC="$DIR/wp-content/themes/hello-theme-child-master/functions.php"

echo "=== 1. CLEANING FUNCTIONS.PHP DROPPER ==="
if [ -f "$THEME_FUNC" ]; then
    cp -v "$THEME_FUNC" /root/kraft_functions.php.bak
    sed -i '/wphc/d' "$THEME_FUNC"
    sed -i '/eval(/d' "$THEME_FUNC"
    sed -i '/base64_decode/d' "$THEME_FUNC"
    sed -i '/auto-cache/d' "$THEME_FUNC"
fi

echo "=== 2. RESTORING AND LOCKING INDEX.PHP ==="
printf '%s\n' \
'<?php' \
'/**' \
' * Front to the WordPress application. This file does not do anything, but loads' \
' * wp-blog-header.php which tells WordPress to load the theme.' \
' *' \
' * @package WordPress' \
' */' \
'' \
'/**' \
' * Tells WordPress to load the WordPress theme and output it.' \
' *' \
' * @var bool' \
' */' \
"define( 'WP_USE_THEMES', true );" \
'' \
"/** Loads the WordPress Environment and Template */" \
"require __DIR__ . '/wp-blog-header.php';" > "$DIR/index.php"

chown physiotherapiekr:physiotherapiekr "$DIR/index.php"
chmod 444 "$DIR/index.php"

echo "=== 3. RESTORING AND LOCKING ROBOTS.TXT ==="
printf '%s\n' \
'User-agent: *' \
'Disallow: /wp-admin/' \
'Allow: /wp-admin/admin-ajax.php' > "$DIR/robots.txt"

chown physiotherapiekr:physiotherapiekr "$DIR/robots.txt"
chmod 444 "$DIR/robots.txt"

echo "=== 4. RESTORING AND LOCKING .HTACCESS ==="
printf '%s\n' \
'# BEGIN WordPress' \
'<IfModule mod_rewrite.c>' \
'RewriteEngine On' \
'RewriteRule .* - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]' \
'RewriteBase /' \
'RewriteRule ^index\.php$ - [L]' \
'RewriteCond %{REQUEST_FILENAME} !-f' \
'RewriteCond %{REQUEST_FILENAME} !-d' \
'RewriteRule . /index.php [L]' \
'</IfModule>' \
'# END WordPress' > "$DIR/.htaccess"

chown physiotherapiekr:physiotherapiekr "$DIR/.htaccess"
chmod 444 "$DIR/.htaccess"

echo "=== 5. PURGING AND LOCKING MU-PLUGINS ==="
rm -rf "$DIR/wp-content/mu-plugins"/* "$DIR/wp-content/mu-plugins"/.* 2>/dev/null || true
chmod 555 "$DIR/wp-content/mu-plugins"

echo "=== 6. BLOCKING PHP IN UPLOADS ==="
printf '%s\n' \
'<Files *.php>' \
'Order Deny,Allow' \
'Deny from all' \
'</Files>' > "$DIR/wp-content/uploads/.htaccess"
chmod 444 "$DIR/wp-content/uploads/.htaccess"

echo "=== 7. HARDENING WP-CONFIG ==="
WP_CFG="$DIR/wp-config.php"
if [ -f "$WP_CFG" ]; then
    if ! grep -q "DISALLOW_FILE_EDIT" "$WP_CFG"; then
        sed -i "2i define( 'DISALLOW_FILE_EDIT', true );" "$WP_CFG"
        sed -i "3i define( 'DISALLOW_FILE_MODS', true );" "$WP_CFG"
    fi
    chmod 400 "$WP_CFG"
fi

echo "=== 8. RESTARTING PHP-FPM AND APACHE ==="
/scripts/restartsrv_cpanel_php_fpm 2>/dev/null || systemctl restart ea-php*-php-fpm 2>/dev/null || systemctl restart httpd 2>/dev/null || true

echo "=== IMMUNIZATION COMPLETED SUCCESSFULLY ==="
