from PIL import Image

catIm = Image.open('zophie.png')

catCopyIm = catIm.copy()

# Select rectangle
faceIm = catIm.crop((335, 345, 556, 560))


catCopyIm.paste(faceIm, (0, 0))
catCopyIm.paste(faceIm, (400, 500))
catCopyIm.save("pasted.png")
