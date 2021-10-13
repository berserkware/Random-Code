import discord
import json

with open("b:/random-code/discord-bots/billionbot/number.json", 'r') as f:
    number = json.load(f)

lastnumber = number["number"]

TOKEN = 'beans'

client = discord.Client()

@client.event
async def on_message(message):
    if message.channel.id == 891829061444304910:
        with open("b:/random-code/discord-bots/billionbot/number.json", 'w') as f:
            global lastnumber
            newnumber = lastnumber + 1

            data = {
                "number" : newnumber
            }
            f.write(json.dumps(data))
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
