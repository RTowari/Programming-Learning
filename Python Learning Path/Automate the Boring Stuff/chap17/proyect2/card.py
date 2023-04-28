#! python3
# card.py - This program takes names from guests.txt and adds each one individually in seating cards.
# Cards must include some flowers and the table number the guest will be sitting on

from PIL import Image, ImageDraw, ImageFont
import os

# Takes list from guests and asign guests and tables as key value pairs
def main():
    names = []
    with open("guests.txt", "r") as f:
        for name in f:
            names.append(name.rstrip("\n"))
    
    names_tables_d = {}
    for name in names:
      print("%s's table: " % (name))
      table = input()
      names_tables_d[name] = table

    blank_images_l = get_blank_images(names)

    finished_images_l = get_list_finished_images(names_tables_d, blank_images_l)

    

# In a loop, make four images as big as 200x200 and append all of them in a single list
def get_blank_images(names):
    blank_images_l = []
    for i in range(len(names)):
        im = Image.new("RGBA", (300, 200), "white")
        blank_images_l.append(im)
    
    return blank_images_l



# Iterate images and call functions for flowers and names. Append all of them in one list while looping
def get_list_finished_images(names_tables_d, blank_images_l):
    
    for image in blank_images_l:
        image = add_flowers(image)

        image = add_name_and_table(image, names_tables_d)

        image.save("text.png")
        
    

   
# Another function will put flowers on corners
def add_flowers(image):
    flowerIm = Image.open("flower.png")
    image.paste(flowerIm, (0, 0), flowerIm)
    
    return image






 # Call function to add name and table to image
def add_name_and_table(image, names_tables_d):
    for name in names_tables_d:

        draw = ImageDraw.Draw(image)
        arialFont = ImageFont.truetype("arial.ttf", 32)
        draw.text((100, 100), name, fill = "purple", font = arialFont)
        return image

    # Last one will put a rectangle around image
def add_rectangle_around():
    pass



# With images finished iterate list and put all of them in a single 800x800 image

main()