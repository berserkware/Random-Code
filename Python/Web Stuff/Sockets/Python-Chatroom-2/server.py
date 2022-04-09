import socket
import threading

class Server():
    def __init__(self, SERVER, PORT):
        self.addr = (SERVER, PORT)

    def Handle_Client(self, conn, addr):
        username = conn.recv(1024).decode("utf-8")

        self.Send(f"[CONNECTION] {username} has joined the room")

        while True:
            try:
                msg = conn.recv(1024).decode("utf-8")
            except:
                conn.close()
                self.clients.remove(conn)

                self.Send(f"[CONNECTION] {username} has left the room")

                break

            if msg != "":
                self.Send(f"[{username}] {msg}")
        
    def Send(self, msg):
        for i in self.clients:
            i.send(str(msg).encode("utf-8"))
        print(msg)

    def Start_Server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   

        self.clients = []

        print("[SERVER] Server is starting")
        self.server.bind(self.addr)

        self.server.listen()
        print(f"[SERVER] Server is listning on {self.addr}")

        while True:
            conn, addr = self.server.accept()
            self.conn = conn
            self.clients.append(conn)
            thread = threading.Thread(target=self.Handle_Client, args=(conn, addr))
            thread.start()
            print(threading.activeCount() - 1)
        

server = Server(socket.gethostbyname(socket.gethostname()), 5050)
server.Start_Server()