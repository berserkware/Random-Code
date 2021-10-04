import requests
import json

data = {'page' : 5}
r = requests.get("https://httpbin.org/get", params=data)
 
print(r.json()["url"])