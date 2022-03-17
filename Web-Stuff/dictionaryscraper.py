from bs4 import *
import requests

class scraper():   
    def __init__(self, word):
        self.word = word
        try:
            self.page = BeautifulSoup(requests.get(f"http://dictionary.com/browse/{self.word}").text, "xml")
        except:
            raise Exception("Could not find that word")

    def getall(self):
        self.defintion = self.page.find("span", class_="one-click-content css-nnyc96 e1q3nk1v1").text
        self.pronounciations = self.page.find("span", class_="pron-spell-content css-7iphl0 evh0tcl1").text
        return [self.word, self.pronounciations, self.defintion]

    def getdefiniton(self):
        self.defintion = self.page.find("span", class_="one-click-content css-nnyc96 e1q3nk1v1")
        return self.defintion.text

    def getprounoucniations(self):
        self.pronounciations = self.page.find("span", class_="pron-spell-content css-7iphl0 evh0tcl1").text
        return self.pronounciations


if __name__ == "__main__":
    while True:
        word = input("word ->")
        s = scraper(word)
        data = s.getall()
        print(f"{data[0]} {data[1]}:")
        print(data[2])