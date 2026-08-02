import re

with open('04_site/sections/services.html', 'r') as f:
    content = f.read()

with open('tmp/services_bg.html', 'r') as f:
    bg_content = f.read()

# Extract from <div class="models_bg-image-layer"> up to <div class="overlay-section-top">
bg_content = bg_content.split('<div class="overlay-section-top">')[0]

# Now we want to replace everything in services.html from <div class="models_bg-image-layer"> up to <!-- Hardcoded black opacity layer...
target_start = '<div class="models_bg-image-layer">'
target_end = '<!-- Hardcoded black opacity layer sitting perfectly on top of all videos/images but below text -->'

start_idx = content.find(target_start)
end_idx = content.find(target_end)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + bg_content + '      ' + content[end_idx:]
    with open('04_site/sections/services.html', 'w') as f:
        f.write(new_content)
    print("Success")
else:
    print("Could not find boundaries")
