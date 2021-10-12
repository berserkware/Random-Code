import discord
import requests
import random

lastnumber = 7920

TOKEN = 'beans'

client = discord.Client()

@client.event
async def on_message(message):
    if message.channel.id == 891829061444304910:
        global lastnumber
        newnumber = lastnumber + 1
        try:
            number = int(message.content)
        except:
            await message.delete()
            return

        if number != newnumber:
            await message.delete()
            return

        lastnumber = newnumber

        

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)

client.run(TOKEN)
