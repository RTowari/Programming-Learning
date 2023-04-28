from PIL import Image

catIm = Image.open('zophie.png')

catIm.rotate(90).save("rotated90.png")