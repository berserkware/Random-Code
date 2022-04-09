import requests
from bs4 import BeautifulSoup
import re

def replace(sentance):
    result = []
    newsentance = sentance.split()
    for i in newsentance:
        page = requests.get(f"https://www.merriam-webster.com/thesaurus/{i}")
        scraper = BeautifulSoup(page.text, "lxml")
        lister = scraper.find("ul", class_="mw-list")
        if lister != None:
            synonyms = lister.find_all("a")
            result.append(synonyms[0].text)
        else:
            result.append(i)
    return " ".join(result)

print(replace(""))
