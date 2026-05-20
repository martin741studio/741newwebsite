<?php
header('Content-Type: text/plain');
ini_set('display_errors', 1);
error_reporting(E_ALL);
@ini_set('memory_limit', '512M');
@set_time_limit(0);

require 'wp-load.php';
global $wpdb;

echo "=== PHASE 1: FORENSIC POST ANALYSIS ===\n";
// Grab a sample of the new spam
$recent_spam = $wpdb->get_results("SELECT ID, post_title, post_date, post_author, guid FROM $wpdb->posts WHERE post_content LIKE '%casino%' OR post_content LIKE '%GamStop%' ORDER BY post_date DESC LIMIT 5");

if(!empty($recent_spam)) {
    echo "Recent Spam Post Forensics:\n";
    foreach($recent_spam as $spam) {
        $author_info = get_userdata($spam->post_author);
        $author_name = $author_info ? $author_info->user_login : "UNKNOWN (Or Deleted)";
        echo " - Post ID: {$spam->ID}\n";
        echo "   Date: {$spam->post_date}\n";
        echo "   Author Used: {$author_name} (ID: {$spam->post_author})\n";
        echo "   Title: " . substr($spam->post_title, 0, 30) . "...\n\n";
    }
}

echo "=== PHASE 2: APPLICATION PASSWORD / TOKEN CHECK ===\n";
// Are they using application passwords for Dinakar?
$users = get_users('role=administrator');
foreach($users as $user) {
    echo "Checking user: {$user->user_login}...\n";
    $app_passwords = get_user_meta($user->ID, '_application_passwords', true);
    if (!empty($app_passwords)) {
        echo "  [🚨 CRITICAL] Application Passwords ENABLED for {$user->user_login}:\n";
        foreach($app_passwords as $ap) {
            echo "    - Name: {$ap['name']} | Created: " . date('Y-m-d H:i:s', $ap['created']) . " | Last IP: {$ap['last_used_ip']}\n";
        }
    } else {
        echo "  - No Application Passwords found.\n";
    }
}

echo "\n=== PHASE 3: DEEP FILESYSTEM HUNT ===\n";
echo "Scanning for disguised executables or backdoors...\n";

$dangerous_extensions = ['phtml', 'php5', 'php7', 'phar', 'inc'];
$upload_dir = wp_upload_dir()['basedir'];

$suspicious_files = [];

function check_dir_deep($dir) {
    global $suspicious_files, $dangerous_extensions;
    if(!is_dir($dir)) return;
    
    $iter = new RecursiveIteratorIterator(
        new RecursiveDirectoryIterator($dir, RecursiveDirectoryIterator::SKIP_DOTS),
        RecursiveIteratorIterator::SELF_FIRST,
        RecursiveIteratorIterator::CATCH_GET_CHILD
    );

    $cutoff = time() - (72 * 3600); // 72 hours ago

    foreach ($iter as $path => $dir_obj) {
        if ($dir_obj->isDir()) continue;
        
        $filename = $dir_obj->getFilename();
        $ext = strtolower(pathinfo($filename, PATHINFO_EXTENSION));
        
        // 1. Check for dangerous disguised extensions anywhere
        if (in_array($ext, $dangerous_extensions)) {
            $suspicious_files[] = "[DISGUISED SCRIPT] " . $path;
        }

        // 2. Check for recent plugin modifications (hunting for nulled Elementor traces)
        if (strpos($path, 'wp-content/plugins') !== false && $ext === 'php') {
            if ($dir_obj->getMTime() > $cutoff) {
                // Read top 500 bytes to check if it's a known generic dropper
                $content = file_get_contents($path, false, null, 0, 800);
                if (strpos($content, 'base64_decode') !== false || strpos($content, 'eval(') !== false || strpos($content, 'preg_replace("/.*/e"') !== false) {
                    $suspicious_files[] = "[INFECTED PLUGIN FILE] " . $path;
                }
            }
        }

        // 3. Check for any PHP in uploads (strict)
        if (strpos($path, 'wp-content/uploads') !== false && $ext === 'php') {
            $suspicious_files[] = "[PHP IN UPLOADS] " . $path;
        }
    }
}

// Start deep scan
check_dir_deep(ABSPATH);

if(empty($suspicious_files)) {
    echo " - No disguised shells or infected recent plugin files found in deep scan.\n";
} else {
    foreach($suspicious_files as $sf) {
        echo "  -> $sf\n";
    }
}

echo "\n=== PHASE 4: CLEANUP (Spam Purge) ===\n";
echo "Wiping new spam injections...\n";
$patterns = ['casino', 'cialis', 'pharma', 'viagra', 'pin up', 'GamStop'];
$post_ids_to_delete = [];

foreach ($patterns as $p) {
    $results = $wpdb->get_results($wpdb->prepare("SELECT ID FROM $wpdb->posts WHERE post_content LIKE %s", '%' . $wpdb->esc_like($p) . '%'));
    foreach($results as $r) {
        $post_ids_to_delete[] = $r->ID;
    }
}

$post_ids_to_delete = array_unique($post_ids_to_delete);
$count = 0;
foreach($post_ids_to_delete as $id) {
    wp_delete_post($id, true);
    $count++;
}
echo "Permanently shredded $count reinjected spam posts.\n";

echo "\n=== END REPORT ===\n";
@unlink(__FILE__);
?>
