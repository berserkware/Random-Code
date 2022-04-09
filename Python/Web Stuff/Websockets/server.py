#import librarys
import websockets
import asyncio

PORT = 7890

print(f"SERVER STARTED, PORT: {PORT}")

async def echo(websocket, path):
    print(f"A client has connected")

    try:
        async for message in websocket:
            print(f"Received message from client: {message}")
            await websocket.send(message)
    except websockets.exceptions.ConnectionClosed as e:
        print("a client disconnected")

startserver = websockets.serve(echo, "localhost", PORT)

asyncio.get_event_loop().run_until_complete(startserver)
asyncio.get_event_loop().run_forever()