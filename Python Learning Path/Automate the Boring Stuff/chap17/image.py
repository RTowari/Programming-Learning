from PIL import Image

catIm = Image.open('zophie.png')

print(catIm.size)

width, height = catIm.size

print(width, height)

print(catIm.filename)

print(catIm.format)

print(catIm.format_description)

catIm.save("zophie.jpg")