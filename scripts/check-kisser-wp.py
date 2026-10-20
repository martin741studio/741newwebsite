import json, subprocess

code = """
require_once ABSPATH . 'wp-admin/includes/update.php';
require_once ABSPATH . 'wp-admin/includes/plugin.php';

wp_version_check();
wp_update_plugins();

$core_updates = get_core_updates();
$plugin_updates = get_plugin_updates();

echo "=== WORDPRESS CORE ===\n";
echo "Current Version: " . get_bloginfo('version') . "\n";
if (!empty($core_updates)) {
    foreach ($core_updates as $cu) {
        echo "Available Core Update: " . $cu->version . " (Response: " . $cu->response . ")\n";
    }
} else {
    echo "Core is up to date.\n";
}

echo "\n=== PLUGINS NEEDING UPDATES (" . count($plugin_updates) . ") ===\n";
foreach ($plugin_updates as $file => $data) {
    echo "• " . $data->Name . " (Current: " . $data->Version . " -> New: " . $data->update->new_version . ")\n";
}

$all_plugins = get_plugins();
echo "\n=== TOTAL INSTALLED PLUGINS (" . count($all_plugins) . ") ===\n";
foreach ($all_plugins as $file => $p) {
    $active = is_plugin_active($file) ? '[ACTIVE]' : '[INACTIVE]';
    echo $active . " " . $p['Name'] . " v" . $p['Version'] . " (" . $file . ")\n";
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
