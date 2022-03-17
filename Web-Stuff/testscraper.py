import requests
from bs4 import BeautifulSoup

page = requests.get(f"https://www.merriam-webster.com/thesaurus/hello,")
scraper = BeautifulSoup(page.text, "lxml")
lister = scraper.find("ul", class_="mw-list")
synonyms = lister.find_all("a")
print(synonyms[0].text)