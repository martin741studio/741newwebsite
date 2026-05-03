<?php
header('Content-Type: text/plain');
echo "=== STEP 1: CORE RECOVERY START ===\n";

$zip_url = 'https://wordpress.org/latest.zip';
$zip_file = 'latest.zip';

echo "Downloading fresh WordPress core...\n";
if (!file_put_contents($zip_file, file_get_contents($zip_url))) {
    die("Failed to download WordPress core.\n");
}

function deleteDir($dirPath) {
    if (!is_dir($dirPath)) { return; }
    $files = array_diff(scandir($dirPath), array('.','..'));
    foreach ($files as $file) {
        $path = $dirPath . '/' . $file;
        is_dir($path) ? deleteDir($path) : unlink($path);
    }
    rmdir($dirPath);
}

echo "Deleting wp-admin and wp-includes...\n";
deleteDir('wp-admin');
deleteDir('wp-includes');

echo "Extracting fresh core...\n";
$zip = new ZipArchive;
if ($zip->open($zip_file) === TRUE) {
    $zip->extractTo('./');
    $zip->close();
} else {
    die("Failed to extract WordPress zip.\n");
}

echo "Moving fresh files to root...\n";
$source = "wordpress/";
$files = scandir($source);
foreach ($files as $file) {
    if (in_array($file, array(".",".."))) continue;
    if ($file === 'wp-content' || $file === 'wp-config.php') continue;
    
    if (is_dir($source.$file)) {
        rename($source.$file, $file);
    } else {
        copy($source.$file, $file);
        unlink($source.$file);
    }
}
deleteDir('wordpress');
unlink($zip_file);

echo "=== CORE RECOVERY COMPLETE ===\n";
require 'wp-load.php';
echo "WordPress Bootstrap test: " . (function_exists('wp_footer') ? "SUCCESS" : "FAILED") . "\n";
?>
