from PIL import Image, ImageDraw, ImageFont

import os

im = Image.new('RGBA', (200, 200), 'white')

draw = ImageDraw.Draw(im)

draw.text((20, 150), 'Hello', fill='purple')

fontsFolder = 'FONT_FOLDER' # e.g. ‘/Library/Fonts’

arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)

arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)

im.save('text.png')