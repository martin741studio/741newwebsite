<?php
header('Content-Type: text/plain');
ini_set('display_errors', 1);
error_reporting(E_ALL);

require 'wp-load.php';
global $wpdb;

echo "=== DEEP POST FORENSICS AUDIT ===\n\n";

// 1. Total counts
$total_posts = $wpdb->get_var("SELECT COUNT(*) FROM $wpdb->posts WHERE post_type = 'post' AND post_status = 'publish'");
$total_pages = $wpdb->get_var("SELECT COUNT(*) FROM $wpdb->posts WHERE post_type = 'page' AND post_status = 'publish'");
echo "Total Published Blog Posts: $total_posts\n";
echo "Total Published Pages: $total_pages\n\n";

// 2. Posts by Author
echo "--- Posts grouped by Author ---\n";
$author_counts = $wpdb->get_results("SELECT post_author, COUNT(*) as count FROM $wpdb->posts WHERE post_type = 'post' GROUP BY post_author");
foreach($author_counts as $ac) {
    $author_info = get_userdata($ac->post_author);
    $author_name = $author_info ? $author_info->user_login : "UNKNOWN DELETED USER";
    echo "Author: $author_name (ID: {$ac->post_author}) -> Created {$ac->count} posts.\n";
}

// 3. Let's look at the 25 most recent posts regardless of content
echo "\n--- 25 Most Recent Posts ---\n";
$recent_posts = $wpdb->get_results("SELECT ID, post_title, post_date, post_author, post_status FROM $wpdb->posts WHERE post_type = 'post' ORDER BY post_date DESC LIMIT 25");

if(empty($recent_posts)) {
    echo "No posts exist in the database at all.\n";
} else {
    foreach($recent_posts as $rp) {
        $author_info = get_userdata($rp->post_author);
        $author_name = $author_info ? $author_info->user_login : "UNKNOWN";
        echo "ID: {$rp->ID} | Status: {$rp->post_status} | Date: {$rp->post_date} | Author: {$author_name}\n";
        echo "Title: " . mb_substr($rp->post_title, 0, 80) . "\n---\n";
    }
}

// 4. Quick scan for non-standard characters (Cyrillic/Japanese) often used in spam that our English nets missed
$weird_posts = $wpdb->get_results("SELECT ID, post_title FROM $wpdb->posts WHERE post_type = 'post' AND (post_title REGEXP '[А-Яа-яぁ-んァ-ヶｦ-ﾟ一-龥]') LIMIT 5");
if(!empty($weird_posts)) {
    echo "\n--- WARNING: Found posts containing Cyrillic or Asian characters! ---\n";
    foreach($weird_posts as $wp) {
        echo "ID: {$wp->ID} | Title: {$wp->post_title}\n";
    }
}

echo "\n=== END REPORT ===\n";
@unlink(__FILE__);
?>
