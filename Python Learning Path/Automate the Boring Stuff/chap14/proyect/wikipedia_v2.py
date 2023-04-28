#! python3
#! webtoon - # Iterate a dictionary. Keys are manga titles names and values are their URLs.
            # For each title download all images from lastest chapter 
            # Download only after one week from last time

import requests, bs4, re, time


microprocessor = {
    "title" : "Microprocessor",
    "url" : "https://en.wikipedia.org/wiki/Microprocessor",
    "last_download" : "place_holder"
}


def download_handling(): # Download  in one folder

    # Get main page url
    res = requests.get(microprocessor["url"])
    res.raise_for_status()
    main_page_html = bs4.BeautifulSoup(res.text, 'html.parser' )

    # Takes only main content
    getFiles(main_page_html)

    # Time handling
    last_time = time.time()

    print(last_time)


# Return title or content
def getFiles(main_page_html):
    
    # Gets only "p" and "h" tags
    html_content = main_page_html.find_all([re.compile("h\d"), "p"])

    # Iterate each tag
    regex_h_class = re.compile(r"h\d")
    for i in range(len(html_content)):

        # Looks for titles and text.
        regex_result = regex_h_class.findall(str(html_content[i]))
        if len(regex_result) != 0:
            title = getTitle(html_content[i])
            get_txt(str(title))
        else:
            text = getText(html_content[i])
            get_txt(str(text))


def getTitle(html_title):
    clean_html_title =  html_title.find_all(re.compile("span"), class_ = re.compile("mw-headline"))
    
    for bs4_Obj in clean_html_title:
        title = "\n" + bs4_Obj.get_text() + "\n\n"
        return title
    

def getText(html_text):

    text = html_text.getText()
    return text


def get_txt(plain_string):

    with open("wikipedia.txt", "a", encoding="utf-8") as f:
        f.write(plain_string)

    

download_handling()