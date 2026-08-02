import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1 & 2. Replace CSS CDN
    content = re.sub(r'https://cdn\.prod\.website-files\.com/[^"]+\.css', '/assets/weavy.css', content)
    
    # 3. Remove fpr.js
    content = re.sub(r'<script src="https://cdn\.firstpromoter\.com/fpr\.js".*?</script>\n?', '', content)
    
    # 4. Remove model-viewer
    content = re.sub(r'<script src="https://unpkg\.com/@google/model-viewer[^"]+".*?</script>\n?', '', content)
    
    # 5. Remove webflow JS
    content = re.sub(r'<script src="https://cdn\.prod\.website-files\.com/[^"]*webflow[^"]*\.js"[^>]*></script>\n?', '', content)
    content = re.sub(r'<script src="https://cdn\.prod\.website-files\.com/[^"]*schunk[^"]*\.js"[^>]*></script>\n?', '', content)
    content = re.sub(r'<script src="https://cdn\.prod\.website-files\.com/[^"]*finsweet[^"]*\.js"[^>]*></script>\n?', '', content)

    # 6. Remove Weavy images/videos
    # For images, let's replace the src and srcset with empty strings so layout doesn't completely collapse but no external asset is loaded
    content = re.sub(r'src="https://cdn\.prod\.website-files\.com/[^"]+\.(avif|png|jpg|jpeg|svg)"', 'src=""', content)
    content = re.sub(r'srcset="https://cdn\.prod\.website-files\.com/[^"]+"', 'srcset=""', content)
    
    # For videos, remove the source tags
    content = re.sub(r'<source src="https://assets\.weavy\.ai/[^"]+"\s*type="video/mp4"\s*/?>\n?', '', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for root, _, files in os.walk('04_site'):
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))

print("Assets replaced.")
