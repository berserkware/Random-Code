import requests
from bs4 import BeautifulSoup

content = requests.get("https://coinmarketcap.com/currencies").text
soup = BeautifulSoup(content, "lxml")
bitcoin = soup.find("a", href = "/currencies/bitcoin/markets/").text
ethereum = soup.find("a", href = "/currencies/ethereum/markets/").text
dogecoin = soup.find("a", href = "/currencies/dogecoin/markets/").text
print(f"Bitcoin Price - {bitcoin}")
print(f"Ethereum Price - {ethereum}")
print(f"Dogecoin Price - {dogecoin}")