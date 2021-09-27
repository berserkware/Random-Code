import socket
import threading

class Server():
    def __init__(self, ADDR, PORT):
        self.addr = ADDR
        self.port = PORT
    
    def Start_Server(self):
        pass

    def Close_Server(self):
        pass

    def Handle_Client(self, conn, addr):
        pass

    def Send(self, msg):
        pass
        