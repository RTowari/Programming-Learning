#! python3
#! webtoon - # Iterate a dictionary. Keys are manga titles names and values are their URLs.
            # For each title download all images from lastest chapter 
            # Download only after one week from last time
import requests, bs4, re, docx, os

class Article:
    def __init__(self, title, url, last_time):
        self.title = title
        self.url = url
        self.last_time = last_time

microprocessor = {
    "title" : "Microprocessor",
    "url" : "https://en.wikipedia.org/wiki/Microprocessor",
    "last_download" : "place_holder"
}

tyrannosaurus_rex = {
    "title" : "Tyrannosaurus rex",
    "url" : "https://es.wikipedia.org/wiki/Tyrannosaurus_rex",
    "last_download" : "place_holder"
}

page_data = [microprocessor, tyrannosaurus_rex]


def download_handling(): # Download  in one folder

    # Get main page url
    res = requests.get(microprocessor["url"])
    res.raise_for_status()
    main_page_html = bs4.BeautifulSoup(res.text, 'html.parser' )

    # Parse text
    getParapgh(main_page_html)
    getTitle(main_page_html)


def getParapgh(main_page_html):
    
    html_text = main_page_html.select("div p")
    end_text = ""

    for html_paragraph in html_text:
        html_paragraph = str(html_paragraph)

        regex = re.compile(r">[\s.,;/“”:'()$&%a-zA-Z0-9 -]*<*")
        clean_html_paragraph = regex.findall(html_paragraph)

        # Append list to single string with all the wikipedia text
        end_paragraph = ""
        for words in clean_html_paragraph:
            for  char in words:
                if char == "<" or char == ">":
                    continue
                else:
                    end_paragraph = end_paragraph + char

        end_text = end_text + end_paragraph

    makeDOC(end_text)


def getTitle(main_page_html):

    # Get code lines inside h class
    html_titles = main_page_html.find_all(re.compile("h\d"))

    # Get lines inside span
    for html_title in html_titles:
        clean_html_title =  html_title.find_all(re.compile("span"), class_ = re.compile("mw-headline"))

        # Get only titles
        for title in clean_html_title:
            print(title.get_text())



    
        

def makeDOC(end_text):

    # Get file name and path
    cwd = os.getcwd()
    file_name = microprocessor["title"] + ".docx"
    file_path = os.path.join(cwd, file_name)

    doc = docx.Document()
    doc.add_paragraph(end_text)
    doc.save(file_name)
    


    

download_handling()