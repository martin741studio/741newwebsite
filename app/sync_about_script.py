import re

with open('/Users/martindrendel/Downloads/741-website-v2/index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

with open('/Users/martindrendel/Downloads/741-website-v2/about.html', 'r', encoding='utf-8') as f:
    abt = f.read()

# 1. Grab Global Styles from index
head_style_match = re.search(r'<!-- Brand Guidelines Color Overrides -->.*?</style>', idx, re.DOTALL)
global_styles = head_style_match.group(0)

# Replace <style> in about.html entirely (assuming it has only one <style> block in <head>)
abt_style_match = re.search(r'<style>.*?</style>', abt, re.DOTALL)
abt = abt.replace(abt_style_match.group(0), global_styles)

# 2. Grab Navbar from index
nav_start = idx.find('<div data-wf--navbar--variant="with-banner---black" class="navbar_main">')
i = nav_start + 50
divs = 1
while divs > 0 and i < len(idx):
    if idx[i:i+4] == '<div': divs += 1; i += 4
    elif idx[i:i+6] == '</div>':
        divs -= 1; i += 6
        if divs == 0: break
    else: i += 1
navbar = idx[nav_start:i]
navbar = navbar.replace('aria-current="page"', '')
navbar = navbar.replace('w--current', '')
navbar = navbar.replace('="/about.html" class="nav_text-link"', '="/about.html" aria-current="page" class="nav_text-link w--current"')

# Replace old Navbar in about
# The old navbar is <nav class="navbar_main"> ... </nav>
abt_nav_match = re.search(r'<nav class="navbar_main">.*?</nav>', abt, re.DOTALL)
if abt_nav_match:
    abt = abt.replace(abt_nav_match.group(0), navbar)
else:
    print("Could not find old navbar to replace")

# 3. Fix Hero background to match index.html
# We want to replace section_hero-about background with index.html's section-hero background
abt = re.sub(
    r'(\.section_hero-about\s*{[^}]*background-image:\s*)([^;]+)',
    r'\1linear-gradient(0deg, rgba(255, 255, 255, 0.3) 34%, rgba(250, 193, 24, 0.35) 71%), url("https://cdn.prod.website-files.com/681b040781d5b5e278a69989/681ccdbeb607e939f7db68fa_BG%20NET%20Hero.avif")',
    abt
)
# Ensure global body background is set to the dark color and not overwritten
if 'html, body {\\n  background-color: var(--brand--dark);\\n  color: white;\\n}' not in abt:
    abt = re.sub(r'body\s*{[^}]*}', 'body { background-color: var(--brand--dark); color: white; font-family: Inter, sans-serif; margin: 0; padding: 0; -webkit-font-smoothing: antialiased; }', abt)

# 4. Values / Tools cards styles
# The user wants value cards to have similar styling to the homepage tools section.
# We will inject additional CSS for .value_card right after global styles
value_card_css = """
    .value_card {
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid rgba(255, 255, 255, 0.05);
      padding: 3rem;
      border-radius: 1.5rem;
      transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1);
      position: relative;
      overflow: hidden;
    }
    .value_card:hover {
      transform: translateY(-12px);
      background: rgba(255, 255, 255, 0.05);
      border-color: var(--brand--lemon);
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
    }
    .value_icon {
      font-size: 3rem; margin-bottom: 1.5rem;
    }
"""
abt = abt.replace('</style>', value_card_css + '\\n</style>')

# 5. Grab Footer from index
foot_match = re.search(r'<footer data-wf--footer--variant="base" class="footer">.*?</footer>', idx, re.DOTALL)
footer = foot_match.group(0)

# Replace old footer in about
abt_foot_match = re.search(r'<footer data-wf--footer--variant="base" class="footer">.*?</footer>', abt, re.DOTALL)
if abt_foot_match:
    abt = abt.replace(abt_foot_match.group(0), footer)

# 6. Add GSAP/Lenis/Modals scripts from index to bottom of about
scripts_match = re.search(r'    <!-- Lenis JS -->.*?</body>', idx, re.DOTALL)
if scripts_match:
    scripts = scripts_match.group(0).replace('</body>', '')
    
    # remove old akira script from about if any
    abt = re.sub(r'<script>\s*function toggleAkira.*?id=\'akira-bubble\'.*?</script>', '', abt, flags=re.DOTALL)
    
    # insert the new scripts right before </body>
    if '<!-- Contact Modal HTML -->' not in abt:
        abt = abt.replace('</body>', f"\\n{scripts}\\n</body>")

with open('/Users/martindrendel/Downloads/741-website-v2/about.html', 'w', encoding='utf-8') as f:
    f.write(abt)

print("Sync completed.")
