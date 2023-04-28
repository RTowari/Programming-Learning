# Select rectangle and delete everything outside
from PIL import Image

catIm = Image.open('zophie.png')

croppedIm = catIm.crop((335, 345, 565, 560))

croppedIm.save("cropped.png")

# Copy image
catIm = Image.open("zophie.png")
catCopyIm = catIm.copy()

