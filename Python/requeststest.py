from PIL import Image
import requests
from io import BytesIO


try:
    x = requests.get(requests.get("http://reddit.com/r/memes/random/.json").json()[0]["data"]["children"][0]["data"]["url"])
except:
    x = requests.get(requests.get("http://reddit.com/r/memes/random/.json").json()[0]["data"]["children"][0]["data"]["thumbnail"])


img = Image.open(BytesIO(x.content))

img.show()