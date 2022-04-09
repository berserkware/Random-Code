import requests
import json

x = requests.get("http://reddit.com/r/memes/random/.json")
print(x.json()[0]["data"]["children"][0]["data"]["url_overridden_by_dest"])