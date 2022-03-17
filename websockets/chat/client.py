import websockets
import asyncio

async def listen():
    url = "ws://127.0.0.1:7890"

    async with websockets.connect(url) as ws:

        await ws.send("Hi")

        while True:
            msg = await ws.recv()
            print(msg)

asyncio.get_event_loop().run_until_complete(listen())