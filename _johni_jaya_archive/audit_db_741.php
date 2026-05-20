<?php
// Load WordPress Environment
require 'wp-load.php';
global $wpdb;

echo "=== START AUDIT ===\n";

// 1. Check unknown admin users
$admins = get_users('role=administrator');
echo "[ADMIN USERS]\n";
foreach($admins as $a) {
    echo $a->ID . " | " . $a->user_login . " | " . $a->user_email . "\n";
}

// 2. Scan options for suspicious patterns
echo "\n[SUSPICIOUS OPTIONS]\n";
$patterns = ['base64_decode', 'eval(', "pin up", "GamStop", '<script'];
foreach ($patterns as $p) {
    $results = $wpdb->get_results($wpdb->prepare("SELECT option_name, option_value FROM $wpdb->options WHERE option_value LIKE %s LIMIT 10", '%' . $wpdb->esc_like($p) . '%'));
    foreach($results as $r) {
        echo "Match '$p' in option: " . $r->option_name . "\n";
    }
}

// 3. Scan posts
echo "\n[SUSPICIOUS POSTS]\n";
foreach ($patterns as $p) {
    $results = $wpdb->get_results($wpdb->prepare("SELECT ID, post_title FROM $wpdb->posts WHERE post_content LIKE %s LIMIT 10", '%' . $wpdb->esc_like($p) . '%'));
    foreach($results as $r) {
        echo "Match '$p' in post ID: " . $r->ID . " (" . $r->post_title . ")\n";
    }
}

// 4. Retrieve Cron Jobs
echo "\n[CRON JOBS]\n";
$cron = get_option('cron');
if (is_array($cron)) {
    foreach($cron as $timestamp => $cronhooks) {
        if (is_array($cronhooks)) {
            foreach($cronhooks as $hook => $keys) {
                echo "Hook: $hook\n";
            }
        }
    }
}

// 5. Active Plugins
echo "\n[ACTIVE PLUGINS]\n";
$plugins = get_option('active_plugins');
if (is_array($plugins)) {
    foreach($plugins as $plugin) {
        echo $plugin . "\n";
    }
}

echo "=== END AUDIT ===\n";
?>
