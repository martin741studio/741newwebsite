<?php
header('Content-Type: text/plain');
ini_set('display_errors', 1);
error_reporting(E_ALL);

require 'wp-load.php';
global $wpdb;

echo "=== PHASE 1: REVOKING ROGUE TOKENS ===\n";

$users = get_users('role=administrator');
foreach($users as $user) {
    echo "Processing User: {$user->user_login} (ID: {$user->ID})\n";
    $app_passwords = get_user_meta($user->ID, '_application_passwords', true);
    
    if (!empty($app_passwords)) {
        echo "  - Identified " . count($app_passwords) . " active Application Passwords.\n";
        // Delete all application passwords for this user
        delete_user_meta($user->ID, '_application_passwords');
        echo "  [SUCCESS] All Application Passwords successfully revoked and deleted from the database.\n";
    } else {
        echo "  - No Application Passwords active.\n";
    }
}

echo "\n=== PHASE 2: GLOBAL LOCKDOWN ===\n";

$config_path = ABSPATH . 'wp-config.php';
$config_content = file_get_contents($config_path);

if (strpos($config_content, 'WP_APPLICATION_PASSWORDS') === false) {
    echo "Application Password killswitch not found. Injecting definition...\n";
    
    $insert_str = "\n/** Hardening: Disable REST API Application Passwords (Anti-Spam) */\ndefine( 'WP_APPLICATION_PASSWORDS', false );\n";
    $replacement = $insert_str . "/* That's all, stop editing! Happy publishing. */";
    
    if(strpos($config_content, "/* That's all, stop editing! Happy publishing. */") !== false) {
        $config_content = str_replace("/* That's all, stop editing! Happy publishing. */", $replacement, $config_content);
        file_put_contents($config_path, $config_content);
        echo "  [SUCCESS] Application Passwords globally disabled in wp-config.php.\n";
    } else {
        echo "  [ERROR] Failed to find injection point in wp-config.php.\n";
    }
} else {
    echo "  [INFO] WP_APPLICATION_PASSWORDS already defined in wp-config.php.\n";
}

echo "\n=== END REPORT ===\n";

// Self destruct
@unlink(__FILE__);
?>
