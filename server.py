import socket
import threading

host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)

print(host_name)
print(ip)

host = input("IP (127.0.0.1 for local): ")
port = int(input("Port: "))

#set up the server and binding given host and port
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try: #works while client is in server
            message = client.recv(1024)
            # if message == "CHANGENAME":
            #     client.send
            broadcast(message)
        
        except: #runs when client is gone - removes client & nickname from lists
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat".encode('utf-8'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('NAME'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print("Nickname is {}".format(nickname))
        broadcast("{} joined".format(nickname).encode('utf-8'))
        client.send('Connected to server!'.encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is started and listening")
receive()
        

