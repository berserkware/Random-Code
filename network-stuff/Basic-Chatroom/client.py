import socket
import threading

HEADER = 8
PORT = 5050
FORMAT = "utf-8"
DISCONECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def recieve():
    while True:
        print(client.recv(2048).decode(FORMAT))

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def start():
    thread = threading.Thread(target=recieve, args=())
    thread.start()
    while True:
        msg = input()
        send(msg)

start()