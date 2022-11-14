import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog

"""
INCOMPLETE

tkinter experiment/testing
Will use to create a gui for chatroom
"""

host = input("IP (Local 127.0.0.1): ")
port = int(input("Port: "))

class Client:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(host, port)

        msg = tkinter.Tk()
        msg.withdraw()

        self.nickname = simpledialog.askstring("Name", "Please choose a name", parent=msg)

        self.gui_done = False
        self.running = True

        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.receive)

        gui_thread.start()
        receive_thread.start()

    def gui_loop(self):
        pass

    def receive(self):
        pass


# class Server(threading.Thread):
#     def __init__(self, host, port):
#         super().__init__
#         self.connections = []
#         self.host = host
#         self.port = port

#     def run(self):
#         server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         server.bind(self.host, self.port)
#         server.listen()

#         while True:
#             # Accept Connection
#             sc, sockname = server.accept()
#             print("Connected from {} to {}".format(str(sc.getpeername(), sc.getsocketname())))

#             server_socket = ServerSocket(sc, sockname, self)

#             server_socket.start()
#             self.connections.append(server_socket)
#             print("Ready to receive messages")

