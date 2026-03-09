import sys
import os

try:
    from PIL import Image
    import pillow_avif
except ImportError:
    print("Generating fallback placeholder script")
    sys.exit(1)

def create_composite():
    original_path = "/Users/martindrendel/Downloads/741-website-v2/app/assets/images/hcard-color_reference.avif"
    new_bg_path = "/Users/martindrendel/Downloads/741-website-v2/app/assets/images/sunburst_flare_hero.png"
    output_path = "/Users/martindrendel/Downloads/741-website-v2/app/assets/images/sunburst_flare_composite.webp"

    # Open the original AVIF that has the exact text and border
    orig = Image.open(original_path).convert("RGBA")
    
    # Open the new background
    bg = Image.open(new_bg_path).convert("RGBA")
    
    # Resize the new background to exactly match the original dimensions so spacing is perfect
    bg = bg.resize(orig.size, Image.Resampling.LANCZOS)
    
    # The original image has a dark top bar with the text. We extract it.
    # Looking at the original proportions, the top 45 pixels or so contain the rounded corner and text label.
    # We will crop the top 60 pixels from the original.
    width, height = orig.size
    top_label_crop = orig.crop((0, 0, width, 60))
    
    # We also want the border to match. Let's just create a mask that keeps the outer 2 pixels and the top label.
    # A simpler approach: create a new image, paste the background, then paste the top label over it.
    composite = Image.new("RGBA", orig.size)
    composite.paste(bg, (0,0))
    
    # Paste the original top label over the new background
    composite.paste(top_label_crop, (0, 0), top_label_crop)
    
    # Save as webp for high quality and small size
    composite.save(output_path, "WEBP", quality=90)
    print(output_path)

if __name__ == "__main__":
    create_composite()
