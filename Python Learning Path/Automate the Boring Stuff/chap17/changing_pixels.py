from PIL import Image
from PIL import ImageColor

catIm = Image.open('zophie.png')

im = Image.new("RGBA", (100, 100))
im.getpixel((0, 0))

for x in range(100): # Iterate pixels
    for y in range(50):
        im.putpixel((x, y), (210, 210, 210)) # Change color for each iteration

for x in range(100): # Iterate second half
    for y in range(50, 100):
        im.putpixel((x, y), ImageColor.getcolor("darkgray", "RGBA"))