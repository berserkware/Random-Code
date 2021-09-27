import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR =  (SERVER, PORT)
FORMAT = "utf-8"
DISCONECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

messages = []
conns = []

def send_messages(message):
    for i in conns:
        i.send(message.encode(FORMAT))
    


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] New Connection: {addr}")

    connected = True

    for i in messages:
        conn.send(i.encode(FORMAT))

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONECT_MESSAGE:
                connected = False

            messages.append(f"[{addr}] {msg}")
            print(f"[{addr}] {msg}")
            send_messages(f"[{addr}] {msg}")

    conn.close()

def start():
    server.listen()
    print(f"[SERVER] Server is listning on {SERVER}")
    
    while True:
        conn, addr = server.accept()
        conns.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(threading.activeCount() - 1)


print("[STARTING] Server is starting")
start()