import requests
from PIL import Image
from io import BytesIO

raw = requests.get("https://cdn.discordapp.com/attachments/818467711436849182/875869014511984640/wallpaper.jpg").content
obj = BytesIO(raw)
img = Image.open(obj)

img.show()