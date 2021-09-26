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

def handle_client(conn, addr):
    print(f"[CONNECTION] New Connection: {addr}")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        conn.send(lastestmessage.encode(FORMAT))
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            

            if msg == DISCONECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")

    conn.close()

def start():
    server.listen()
    print(f"[SERVER] Server is listning on {SERVER}")
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(threading.activeCount() - 1)


print("[STARTING] Server is starting")
start()