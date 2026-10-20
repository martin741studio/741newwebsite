import json, subprocess

code = """
global $wpdb;

// 1. PURGE SPAM POSTS
$whitelist_ids = [6217, 6336];
$posts = get_posts([
    'post_type' => 'post',
    'post_status' => 'any',
    'numberposts' => -1
]);

$deleted_posts = [];
foreach ($posts as $p) {
    if (!in_array($p->ID, $whitelist_ids)) {
        $title = $p->post_title;
        $id = $p->ID;
        wp_delete_post($id, true); // bypass trash
        $deleted_posts[] = "ID {$id}: {$title}";
    }
}

echo "=== DELETED SPAM POSTS (" . count($deleted_posts) . ") ===\n";
foreach ($deleted_posts as $dp) {
    echo "• " . $dp . "\n";
}

// 2. CLEAN HIDDEN PARASITE SEO LINK BLOCKS FROM ALL PAGES & POSTS
$pages = $wpdb->get_results("SELECT ID, post_title, post_type, post_content FROM {$wpdb->posts} WHERE post_content LIKE '%data-seo-links-block%' OR post_content LIKE '%como-evaluar-un-casino%'");

$cleaned_pages = [];
foreach ($pages as $p) {
    $orig = $p->post_content;
    // Remove the data-seo-links-block div and its contents
    $cleaned = preg_replace('/<div[^>]*data-seo-links-block[^>]*>.*?<\/div>/is', '', $orig);
    // Remove any leftover casino links block if div tag differed
    $cleaned = preg_replace('/<a[^>]*href=[\"\']https?:\/\/[^\"]*(casino|boomerang-bet|terrybet|wildsino|betspino|cazeus|fafabet|winplace)[^\"]*[\"\'][^>]*>.*?<\/a>/is', '', $cleaned);

    if ($cleaned !== $orig) {
        $wpdb->update(
            $wpdb->posts,
            ['post_content' => $cleaned],
            ['ID' => $p->ID]
        );
        clean_post_cache($p->ID);
        $cleaned_pages[] = "ID {$p->ID} ({$p->post_type}): {$p->post_title}";
    }
}

echo "\n=== CLEANED SUBPAGES (" . count($cleaned_pages) . ") ===\n";
foreach ($cleaned_pages as $cp) {
    echo "• " . $cp . "\n";
}

// 3. CLEAR WP ROCKET CACHE
if (function_exists('rocket_clean_domain')) {
    rocket_clean_domain();
    echo "\nWP Rocket cache cleared for domain.\n";
}

// 4. VERIFY REMAINING POSTS
$remaining = get_posts([
    'post_type' => 'post',
    'post_status' => 'any',
    'numberposts' => -1
]);
echo "\n=== REMAINING LEGITIMATE POSTS (" . count($remaining) . ") ===\n";
foreach ($remaining as $r) {
    echo "• ID {$r->ID} ({$r->post_date}): {$r->post_title}\n";
}
"""

payload = json.dumps({'code': code})
res = subprocess.run(['novamira', '--site', 'katharinakisser.at', '--yes', 'run', 'novamira/execute-php', '--input', payload, '--json'], capture_output=True, text=True)
try:
    data = json.loads(res.stdout)
    print(data.get('data', {}).get('output'))
    if data.get('data', {}).get('errors'):
        print('Errors:', data['data']['errors'])
except Exception as e:
    print('Failed to parse:', e)
    print('Raw stdout:', res.stdout)
    print('Raw stderr:', res.stderr)
