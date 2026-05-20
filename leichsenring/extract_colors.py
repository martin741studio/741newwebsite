 from PIL import Image
from collections import Counter
import sys

def get_dominant_colors(image_path, num_colors=5):
    try:
        img = Image.open(image_path)
        img = img.convert('RGB')
        
        # Resize to speed up processing and group similar colors
        img = img.resize((150, 150))
        pixels = list(img.getdata())
        
        # Quantize colors to group similar ones (reduce color space)
        img = img.quantize(colors=16)
        img = img.convert('RGB')
        pixels = list(img.getdata())

        counts = Counter(pixels)
        most_common = counts.most_common(num_colors)
        
        print(f"Dominant colors for {image_path}:")
        for color, count in most_common:
            hex_color = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])
            print(f"{hex_color} - RGB: {color} (Count: {count})")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

get_dominant_colors("/Users/martindrendel/741website/leichsenring/02_branding/homepageconfirmedbyclietn.png", 8)
print("---")
get_dominant_colors("/Users/martindrendel/741website/leichsenring/01_reference/aboutusthemereference.png", 8)
get_dominant_colors("/Users/martindrendel/741website/leichsenring/02_branding/Logodatein/logo-leichsenring-260x300.png", 5)

