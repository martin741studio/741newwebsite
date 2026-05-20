import os
import shutil

src = '/Users/martindrendel/.gemini/antigravity/brain/76fe7485-a5e6-47c3-b166-cd1d5a75354a/media__1777271896346.jpg'
dest_dir = '/Users/martindrendel/741website/WABA/assets'
dest = os.path.join(dest_dir, 'hero-people.jpg')

os.makedirs(dest_dir, exist_ok=True)
try:
    shutil.copy(src, dest)
    print("Copied successfully.")
except Exception as e:
    print(f"Error copying: {e}")
