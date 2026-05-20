<?php
header('Content-Type: text/plain');
ini_set('display_errors', 1);
error_reporting(E_ALL);

require 'wp-load.php';
global $wpdb;

echo "=== LATEST POST-PATCH MALWARE AUDIT ===\n";
echo "Mode: READ-ONLY (No database modifications)\n\n";

$reinfection_indicators = 0;

echo "[1] FILESYSTEM CHECK: Hidden Markers\n";
$lock_files = ['.db2_convert', '.dbx_convert', '.lock', '.mb_convert', '.partition', '.ibase_pconnection', '.include', '.oauthexceptions', '.ob_iconv_handle'];
foreach ($lock_files as $lf) {
    if (file_exists(ABSPATH . $lf)) {
        echo "  [ALERT] Hidden lock file detected: $lf\n";
        $reinfection_indicators++;
    }
}
if ($reinfection_indicators === 0) echo "  - Clean: No hidden FilesMan markers found.\n";

echo "\n[2] FILESYSTEM CHECK: Core Modifications\n";
// Check if core files were modified recently (past 5 hours since patch)
$audit_cutoff = time() - (5 * 3600);
$core_files = ['wp-settings.php', 'wp-load.php', 'wp-config.php', 'index.php'];
$core_tampered = false;
foreach ($core_files as $cf) {
    $path = ABSPATH . $cf;
    if (file_exists($path)) {
        $mtime = filemtime($path);
        if ($mtime > $audit_cutoff) {
            echo "  [WARNING] Core file modified recently: $cf (" . date('Y-m-d H:i:s', $mtime) . ")\n";
            $core_tampered = true;
        }
    }
}
if (!$core_tampered) echo "  - Clean: No recent core modifications detected since patch.\n";

echo "\n[3] THEME CHECK: Target File Integrity\n";
$theme = wp_get_theme();
$functions_path = $theme->get_stylesheet_directory() . '/functions.php';
if (file_exists($functions_path)) {
    $func_code = file_get_contents($functions_path);
    if (strpos($func_code, 'base64_decode') !== false || strpos($func_code, 'crehcg') !== false || strpos($func_code, 'GambStop') !== false) {
        echo "  [ALERT] Malware detected inside active theme $theme functions.php!\n";
        $reinfection_indicators++;
    } else {
        echo "  - Clean: Active theme functions.php contains no known payloads.\n";
    }
}

echo "\n[4] DATABASE CHECK: Application Passwords\n";
$users = get_users('role=administrator');
$app_passes_found = false;
foreach($users as $user) {
    $app_passwords = get_user_meta($user->ID, '_application_passwords', true);
    if (!empty($app_passwords)) {
        echo "  [ALERT] Active Application Passwords found for {$user->user_login}!\n";
        $app_passes_found = true;
        $reinfection_indicators++;
    }
}
if (!$app_passes_found) echo "  - Clean: No rogue Application Passwords active.\n";

echo "\n[5] DATABASE CHECK: Rogue Administrators\n";
$users = get_users('role=administrator');
$rogue_admin_found = false;
foreach($users as $user) {
    if(strtolower($user->user_login) === 'adm1n' || strpos(strtolower($user->user_email), 'wordpress.com') !== false) {
        echo "  [ALERT] Rogue administrator found: {$user->user_login}\n";
        $rogue_admin_found = true;
        $reinfection_indicators++;
    }
}
if (!$rogue_admin_found) echo "  - Clean: No rogue administrators detected.\n";

echo "\n[6] DATABASE CHECK: SEO Spam Reinjection\n";
$spam_count = $wpdb->get_var("SELECT COUNT(*) FROM $wpdb->posts WHERE post_content LIKE '%casino%' OR post_content LIKE '%GamStop%' OR post_content LIKE '%pharma%' OR post_content LIKE '%cialis%'");
if ((int)$spam_count > 0) {
    echo "  [ALERT] Found $spam_count injected spam post(s)!\n";
    $reinfection_indicators++;
} else {
    echo "  - Clean: No SEO spam posts detected in the database.\n";
}

echo "\n=== AUDIT COMPLETE ===\n";
if ($reinfection_indicators === 0 && !$rogue_admin_found) {
    echo "VERDICT: PERFECTLY CLEAN. The killswitch held.\n";
} else {
    echo "VERDICT: RE-INFECTION DETECTED.\n";
}

// Self destruct
@unlink(__FILE__);
?>
