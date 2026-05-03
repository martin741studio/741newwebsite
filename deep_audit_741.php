<?php
header('Content-Type: text/plain');
require 'wp-load.php';
global $wpdb;

echo "=== DEEP DATABASE AUDIT ===\n";

$patterns = ['base64_decode', 'eval(', 'gzinflate', 'str_rot13', 'assert(', 'preg_replace', '<script', 'onerror=', 'pin up', 'GamStop', 'iframe'];

echo "[WP_OPTIONS AUDIT]\n";
$target_options = array('cron', 'active_plugins', 'siteurl', 'home', 'rewrite_rules');
foreach($target_options as $opt) {
    echo "Checking basic option: $opt\n";
    $val = get_option($opt);
    if ($opt === 'siteurl' || $opt === 'home') { echo "  -> $opt: $val\n"; }
    else if ($opt === 'active_plugins') {
        echo "  -> Active Plugins: \n";
        if(is_array($val)) { foreach($val as $p) echo "     - $p\n"; }
    }
}

// Search options by pattern
foreach ($patterns as $p) {
    $results = $wpdb->get_results($wpdb->prepare("SELECT option_name FROM $wpdb->options WHERE option_value LIKE %s AND option_name NOT LIKE '_transient_%'", '%' . $wpdb->esc_like($p) . '%'));
    foreach($results as $r) {
        // Exclude safe options
        if(strpos($r->option_name, 'W3TC_') !== false || strpos($r->option_name, 'wp_user_roles') !== false) continue;
        echo "  MALICIOUS MATCH '$p' in option: " . $r->option_name . "\n";
    }
}

echo "\n[WIDGETS & THEME MODS]\n";
$widgets = $wpdb->get_results("SELECT option_name FROM $wpdb->options WHERE option_name LIKE 'widget_%' OR option_name LIKE 'theme_mods_%'");
foreach($widgets as $w) {
    echo "  Inspecting: " . $w->option_name . "\n";
}

echo "\n[WP_POSTS AUDIT]\n";
foreach ($patterns as $p) {
    if($p==='<script' || $p==='iframe') continue; // too noisy for normal content
    $results = $wpdb->get_results($wpdb->prepare("SELECT ID, post_title FROM $wpdb->posts WHERE post_content LIKE %s", '%' . $wpdb->esc_like($p) . '%'));
    foreach($results as $r) {
        echo "  MALICIOUS MATCH '$p' in post ID: " . $r->ID . " (" . $r->post_title . ")\n";
    }
}

echo "\n[WP_USERS & CAPABILITIES]\n";
$users = get_users();
foreach($users as $user) {
    echo "  User: " . $user->user_login . " | Email: " . $user->user_email . " | Registered: " . $user->user_registered;
    if(in_array('administrator', (array)$user->roles)) {
        echo " [ADMINISTRATOR]";
    }
    echo "\n";
}

// Check usermeta directly for hidden admins injected via raw DB
$hidden_admins = $wpdb->get_results("SELECT user_id, meta_value FROM $wpdb->usermeta WHERE meta_key = 'wp_capabilities' AND meta_value LIKE '%administrator%'");
foreach($hidden_admins as $ha) {
    echo "  DB Capability Check: User ID " . $ha->user_id . " is admin.\n";
}

echo "=== END AUDIT ===\n";
?>
