import discord
import requests
import random

TOKEN = 'ODczMzQ0MDEwOTY0NTkwNjE1.YQ3C_g.j9mJbTYm8NLws5H9N6J5Yzu5JeE'

client = discord.Client()

@client.event
async def on_message(message):
    words = ["Why don't you ", "You could ", "If I was you I would "]

    if message.author == client.user:
        return

    for statement in ("im bored", "i'm bored", "i am bored", "Im bored", "I'm bored", "I am bored"):
        if statement in message.content:
             x = requests.get("http://www.boredapi.com/api/activity/")
             await message.channel.send(words[random.randrange(0, 2)] + x.json()["activity"].lower() + "?")
             if x.json()["link"] != "":
                 await message.channel.send("Link - " + x.json()["link"])

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)

client.run(TOKEN)