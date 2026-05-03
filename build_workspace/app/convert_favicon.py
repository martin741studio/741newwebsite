import sys
from PIL import Image

in_path = "assets/images/favicon_7.png"
out_path = "assets/images/favicon_7_yellow.png"

try:
    img = Image.open(in_path).convert("RGBA")
    data = img.getdata()
    
    # Yellow: #fac118 -> rgb(250, 193, 24)
    # The user says "make the white background ... in the yellow"
    # This might mean all white pixels, or all transparent pixels if the background is transparent.
    # Let's replace both white AND transparent pixels with the brand yellow, or maybe just white?
    
    new_data = []
    for r, g, b, a in data:
        if a == 0:
            # fill transparent with yellow
            new_data.append((250, 193, 24, 255))
        elif r > 240 and g > 240 and b > 240:
            # replace white with yellow
            new_data.append((250, 193, 24, a))
        else:
            new_data.append((r, g, b, a))

    img.putdata(new_data)
    img.save(out_path, "PNG")
    print("Success")
except Exception as e:
    print(e)
