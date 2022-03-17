import discord
from discord.ext import commands
import requests
from io import BytesIO
import json

TOKEN = 'ODg5Mzk4Nzk4MDQyOTQzNTUw.YUgrLQ.ajEgNNao6m9irutUNUN5zei9WqA'

client = commands.Bot(command_prefix='>')

@client.command()
async def say(message, numberoftimes: int, *phrase):
    for i in range(numberoftimes):
        await message.send(" ".join(phrase))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)

client.run(TOKEN)