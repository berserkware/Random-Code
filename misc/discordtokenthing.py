import requests
import json

req = requests.get("https://discord.com/api/v9/users/@me/guilds", headers={"authorization": 'OTUyMzQ3MjMyNjM4NzUwNzYy.Yi0seg.BTkgBtTiZNT-TMJLEEoyXPm1LXk'})

print(req.json())