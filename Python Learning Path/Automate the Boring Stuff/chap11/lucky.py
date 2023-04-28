#! python3
# lucky.py - Opens several Google search result

import requests, sys, webbrowser, bs4

print("Googlin....") # display text while downloading the Google page
res = requests.get("https://www.bing.com/search?q=" + "".join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "html.parser")

# Open a browser tab for each result
linkElems = soup.select("a[target]")
for link in linkElems:
    print("Link")
    print(link)

numOpen=min(5, len(linkElems))

print(numOpen)

for i in range(numOpen):
    webbrowser.get().open(linkElems[i].get("href"))

