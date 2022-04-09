import requests
import json

headers = {'page' : 5}
r = requests.get("https://httpbin.org/get", headers=headers)
 
print(r.json()["url"])