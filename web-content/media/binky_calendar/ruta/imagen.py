from PIL import Image, ImageDraw, ImageOps
import sys

size = (200, 200)

img = Image.open(sys.argv[1])
img = img.resize((200,200), Image.ANTIALIAS)

mask = Image.new('L', size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0) + size, fill=255)

output = ImageOps.fit(img, mask.size,centering=(0.5, 0.5))
output.putalpha(mask)
output.save(sys.argv[2])
