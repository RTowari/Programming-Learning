#! python3
# comic.py - Downloads images from imgur based on user tag. Only first page

import requests, os, bs4, sys, webbrowser

url = "https://imgur.com/"
proyect_path = os.getcwd()
image_folder_path = os.path.join(proyect_path, "images")
os.makedirs(image_folder_path)

# Ask user for tag and open imgur on that page
tag = sys.argv[1]                          # Tag
tag_url = url + "search?q=" + tag          # Url with the tag for easy handle
res = requests.get(tag_url)
res.raise_for_status()
webbrowser.open(tag_url)

# Take html as string and print html with images
soup = bs4.BeautifulSoup(res.text, "html.parser")
images_html = soup.select("a > img")           # List of strings with images's url

image_count = 0
for image in images_html:
    image_url = "https:" + image["src"]
    
    print("Downloading imagenes...")   
    data = requests.get(image_url).content    # Getting image

    image_name = str(image_count) + ".jpg"
    image_path = os.path.join(image_folder_path, image_name)

    f = open(image_path,'wb')                  # New file with no data
    f.write(data)                             # Writing data into file
    f.close()

    image_count = image_count + 1



