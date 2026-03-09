import re

with open('/Users/martindrendel/Downloads/741-website-v2/index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

# Grab Global Styles
head_style_match = re.search(r'<!-- Brand Guidelines Color Overrides -->.*?</style>', idx, re.DOTALL)
global_styles = head_style_match.group(0) if head_style_match else ""

# Grab Responsive DOM block
responsive_dom_match = re.search(r'<div class="code_responsive-dom w-embed">.*?</div>', idx, re.DOTALL)
responsive_dom = responsive_dom_match.group(0) if responsive_dom_match else ""

# Grab Navbar
nav_start = idx.find('<div data-wf--navbar--variant="with-banner---black" class="navbar_main">')
if nav_start == -1: nav_start = idx.find('<div class="navbar_main"')

i = nav_start + 50
divs = 1
while divs > 0 and i < len(idx):
    if idx[i:i+4] == '<div': divs += 1; i += 4
    elif idx[i:i+6] == '</div>':
        divs -= 1; i += 6
        if divs == 0: break
    else: i += 1
navbar = idx[nav_start:i]

# Grab Footer
footer_match = re.search(r'<footer data-wf--footer--variant="base" class="footer">.*?</footer>', idx, re.DOTALL)
footer = footer_match.group(0) if footer_match else ""

# Grab Scripts at the bottom
script_start = idx.find('<script src="https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.5.1.min.dc5e7f18c8.js')
if script_start != -1:
    script_end = idx.find('</body>', script_start)
    scripts = idx[script_start:script_end]
else:
    scripts = ""

# Now process about.html
with open('/Users/martindrendel/Downloads/741-website-v2/about.html', 'r', encoding='utf-8') as f:
    abt = f.read()

# Replace <style> block in about.html with global styles from index
abt_style_match = re.search(r'<style>.*?</style>', abt, re.DOTALL)
if abt_style_match and global_styles:
    abt = abt.replace(abt_style_match.group(0), global_styles)

# Replace body styles to dark
abt = re.sub(r'html,\s*body\s*\{[^}]*\}', 'html, body { background-color: var(--brand--dark); color: white; }', abt)
abt = re.sub(r'body\s*\{[^}]*\}', 'body { background-color: var(--brand--dark); color: white; margin: 0; padding: 0; -webkit-font-smoothing: antialiased; }', abt)


# Insert responsive dom block right after <body> if not there
if responsive_dom and responsive_dom not in abt:
    abt = abt.replace('<body>', '<body>\n  ' + responsive_dom)

# Replace Navbar
abt_nav_start = abt.find('<div class="navbar_main">')
if abt_nav_start == -1: abt_nav_start = abt.find('<nav class="navbar_main"')

if abt_nav_start != -1:
    tag_name = ""
    if abt[abt_nav_start:abt_nav_start+4] == '<div': tag_name = 'div'
    elif abt[abt_nav_start:abt_nav_start+4] == '<nav': tag_name = 'nav'
    
    tags = 1
    i = abt_nav_start + 4
    
    # Simple state machine to find closing tag
    while tags > 0 and i < len(abt):
        if abt[i:i+len(tag_name)+1] == f'<{tag_name}':
            tags += 1
            i += len(tag_name) + 1
        elif abt[i:i+len(tag_name)+2] == f'</{tag_name}':
            tags -= 1
            if tags == 0:
                i += len(tag_name) + 3 # +3 for </ and >
                break
            i += len(tag_name) + 2
        else:
            i += 1
            
    # modify the navbar from index slightly to make "About" active instead of whatever was active
    mod_navbar = navbar.replace('aria-current="page"', '')
    mod_navbar = mod_navbar.replace('w--current', '')
    
    # Insert aria-current to About
    mod_navbar = re.sub(r'href="/about\.html"\s*class="nav_text-link[^"]*"', 'href="/about.html" class="nav_text-link w-variant-138f51c6-a923-3c01-fe1a-d27a5c95ed04 w--current" aria-current="page"', mod_navbar)

    abt = abt[:abt_nav_start] + mod_navbar + abt[i:]
else:
    print('Navbar not found in about.html')

# Replace Footer
abt_footer_match = re.search(r'<footer.*?</footer>', abt, re.DOTALL)
if abt_footer_match and footer:
    mod_footer = footer.replace('2025.', '2026.')
    abt = abt[:abt_footer_match.start()] + mod_footer + abt[abt_footer_match.end():]

# Replace Scripts
# remove existing <script> tags at the bottom to avoid duplicates
abt = re.sub(r'<script.*?</script>', '', abt, flags=re.DOTALL)
abt_body_end = abt.rfind('</body>')
if abt_body_end != -1 and scripts:
    abt = abt[:abt_body_end] + scripts + '\n</body>' + abt[abt_body_end+7:]

# Update specific sections to match homepage UI
# Add index.html hero background to about.html hero
new_hero_bg = 'background-image: linear-gradient(0deg, rgba(255, 255, 255, 0.3) 34%, rgba(250, 193, 24, 0.35) 71%), url("https://cdn.prod.website-files.com/681b040781d5b5e278a69989/681ccdbeb607e939f7db68fa_BG%20NET%20Hero.avif");'
abt = abt.replace('background-image: linear-gradient(0deg, var(--brand--dark) 0%, rgba(250, 193, 24, 0.05) 100%);', new_hero_bg)

# change wrapper to section-hero style
abt = abt.replace('<header class="section_hero-about">', '<header class="section-hero" style="padding: 12rem 2rem 8rem; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.05);">')

with open('/Users/martindrendel/Downloads/741-website-v2/about.html', 'w', encoding='utf-8') as f:
    f.write(abt)

print("Sync complete.")
