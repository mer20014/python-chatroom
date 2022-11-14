import socket
import threading 
# import tkinter as tk

nickname = input("Name: ")
host = input("IP (Local 127.0.0.1): ")
port = int(input("Port: "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')

            if message == "NAME":
                client.send(nickname.encode('utf-8'))
            
            # elif message == "CHANGENAME":
            #     input("Who would you like to change? ")
            else:
                print(message)
        except:
            print("Error, Press any key to exit...")
            client.close()
            break

def write():
    while True:
        message = f"{nickname}: {input('')}"
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

