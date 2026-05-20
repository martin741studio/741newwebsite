import re

with open('/Users/martindrendel/741website/WABA/index.html', 'r') as f:
    content = f.read()

# Inject Tailwind CSS so classes work locally
if '<script src="https://cdn.tailwindcss.com"></script>' not in content:
    content = content.replace('</head>', '    <script src="https://cdn.tailwindcss.com"></script>\n</head>')

# Remove the full-screen black loader that is blocking the page
content = re.sub(r'<div class="loader fixed left-0 right-0 top-0 h-dvh z-22 bg-black text-white flex justify-center items-center">.*?</div>\s*</div>', '', content, flags=re.DOTALL)

# Ensure the body doesn't have overflow hidden from lenis
content = content.replace('overflow:clip', 'overflow:auto')

with open('/Users/martindrendel/741website/WABA/index.html', 'w') as f:
    f.write(content)

print("index.html patched with Tailwind and loader removed.")
