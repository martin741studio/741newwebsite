import os
import re

ref_path = '/Users/martindrendel/741website/Skills/weavireference.html'
dest_path = '/Users/martindrendel/Downloads/741-website-v2/about.html'

with open(ref_path, 'r', encoding='utf-8') as f:
    ref = f.read()

with open(dest_path, 'r', encoding='utf-8') as f:
    abt = f.read()

# 1. Grab <head> content from ref (up to </head>)
ref_head_match = re.search(r'<head>(.*?)</head>', ref, re.DOTALL)
ref_head = ref_head_match.group(1) if ref_head_match else ""

# Also replace the 'Weavy' title and specific open graph stuff with generic About page details if we want? 
# The user said "take elements and change it if necessary from our reference html". Let's put the reference head, then modify title back to 'About | 741.Studio'
ref_head = re.sub(r'<title>.*?</title>', '<title>About | 741.Studio - Architecting Digital Growth</title>', ref_head, flags=re.DOTALL)

# Replace <head> in about
abt = re.sub(r'<head>.*?</head>', f'<head>{ref_head}</head>', abt, flags=re.DOTALL)

# 2. Get Responsive DOM
ref_responsive_dom_match = re.search(r'<div class="code_responsive-dom w-embed">.*?</div>', ref, re.DOTALL)
ref_responsive_dom = ref_responsive_dom_match.group(0) if ref_responsive_dom_match else ""

# Remove any existing responsive dom in about
abt = re.sub(r'<div class="code_responsive-dom w-embed">.*?</div>', '', abt, flags=re.DOTALL)
# Insert after <body>
abt_body_start = abt.find('<body>')
if abt_body_start != -1:
    abt = abt[:abt_body_start+6] + '\n  ' + ref_responsive_dom + abt[abt_body_start+6:]

# 3. Grab Navbar
ref_nav_start = ref.find('<div data-wf--navbar--variant="with-banner---black"')
if ref_nav_start == -1:
    ref_nav_start = ref.find('<div class="navbar')

if ref_nav_start != -1:
    i = ref_nav_start + 4
    tags = 1
    while tags > 0 and i < len(ref):
        if ref[i:i+4] == '<div':
            tags += 1
            i += 4
        elif ref[i:i+5] == '</div':
            tags -= 1
            i += 6
        else:
            i += 1
    ref_navbar = ref[ref_nav_start:i]
else:
    ref_navbar = ""

# Make About link active in navbar, remove from others
ref_navbar = ref_navbar.replace('aria-current="page"', '')
ref_navbar = ref_navbar.replace('w--current', '')
ref_navbar = re.sub(r'href="/about\.html"\s*class="([^"]*)"', r'href="/about.html" class="\1 w--current" aria-current="page"', ref_navbar)


# Replace existing navbar in about
abt_nav_start = abt.find('<div data-wf--navbar--variant="with-banner---black"')
if abt_nav_start == -1:
    abt_nav_start = abt.find('<nav class="navbar')
if abt_nav_start == -1:
    abt_nav_start = abt.find('<div class="navbar_main"')

if abt_nav_start != -1:
    tag_name = 'div' if abt[abt_nav_start:abt_nav_start+4] == '<div' else 'nav'
    i = abt_nav_start + len(tag_name) + 1
    tags = 1
    while tags > 0 and i < len(abt):
        if abt[i:i+len(tag_name)+1] == f'<{tag_name}':
            tags += 1
            i += len(tag_name) + 1
        elif abt[i:i+len(tag_name)+2] == f'</{tag_name}':
            tags -= 1
            i += len(tag_name) + 3
        else:
            i += 1
    abt = abt[:abt_nav_start] + ref_navbar + abt[i:]

# 4. Grab Footer
ref_footer_match = re.search(r'<footer.*?</footer>', ref, re.DOTALL)
ref_footer = ref_footer_match.group(0) if ref_footer_match else ""

# Replace Footer in about
abt_footer_match = re.search(r'<footer.*?</footer>', abt, re.DOTALL)
if abt_footer_match and ref_footer:
    ref_footer = ref_footer.replace('2025.', '2026.')
    abt = abt[:abt_footer_match.start()] + ref_footer + abt[abt_footer_match.end():]

# 5. Grab Scripts at bottom
ref_script_start = ref.find('<script src="https://d3e54v103j8qbb.cloudfront.net/js')
if ref_script_start != -1:
    ref_script_end = ref.find('</body>', ref_script_start)
    ref_scripts = ref[ref_script_start:ref_script_end]
else:
    ref_scripts = ""

# Remove old scripts in about
abt = re.sub(r'<script.*?</script>', '', abt, flags=re.DOTALL)
abt_body_end = abt.rfind('</body>')
if abt_body_end != -1 and ref_scripts:
    abt = abt[:abt_body_end] + ref_scripts + '\n</body>' + abt[abt_body_end+7:]

# Clean up any residual incorrect global css
abt = re.sub(r'body\s*{[^}]*background-color:\s*var\(--brand--dark\)[^}]*}', 'body { margin: 0; padding: 0; -webkit-font-smoothing: antialiased; }', abt)

with open(dest_path, 'w', encoding='utf-8') as f:
    f.write(abt)

print("Sync from weavireference completed successfully.")
