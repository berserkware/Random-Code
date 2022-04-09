#import librarys
import websockets
import asyncio

PORT = 7890

print(f"SERVER STARTED, PORT: {PORT}")

connected = set()

async def echo(websocket, path):
    print(f"A client has connected")
    connected.add(websocket)

    try:
        async for message in websocket:
            print(f"Received message from client: {message}")
            for conn in connected:
                if conn != websocket:
                    await conn.send(f"{websocket}: {message}")
    except websockets.exceptions.ConnectionClosed as e:
        print("a client disconnected")
    finally:
        connected.remove(websocket)

startserver = websockets.serve(echo, "localhost", PORT)

asyncio.get_event_loop().run_until_complete(startserver)
asyncio.get_event_loop().run_forever()