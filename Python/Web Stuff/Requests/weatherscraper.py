import requests
from bs4 import BeautifulSoup

content = requests.get('https://www.weatherwatch.co.nz/forecasts/Auckland').text

soup = BeautifulSoup(content, 'lxml')

temperature = soup.find("div", class_ = "jsx-2553641016 temp").text

print(temperature)