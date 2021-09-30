import socket 
import threading

class Client():
    def __init__(self, SERVER, PORT):
        self.addr = (SERVER, PORT)

    def Receive(self):
        while True:
            print(self.client.recv(2048).decode("utf-8"))

    def Send(self, msg):
        self.client.send(msg.encode("utf-8"))


    def Start(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.addr)


        thread = threading.Thread(target=self.Receive, args=())
        thread.start()

        while True:
            name = input("What is your username - ")
            if name != "":
                self.Send(name)
                break

        while True:
            msg = input()
            self.Send(msg)

client = Client(socket.gethostbyname(socket.gethostname()), 5050)
client.Start()