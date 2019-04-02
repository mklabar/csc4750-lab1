from socket import *

MAX_CLIENTS = 2

#setup socket to wait for connections
serverPort = 43500
serverSocket = socket(AF_INET, SOCK_STREAM) #TCP (reliable)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #make port reusable
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to accept clients')

clients = []
#accept up to two connections from clients, which
# must connect before we can move on
for i in range(0, MAX_CLIENTS):
    connectionSocket, addr = serverSocket.accept()
    clients.append((connectionSocket, addr))
    if i < MAX_CLIENTS:
        print("Stranger", i+1, "connected")

#omitting while loop means the server will run once!
sender = 0
for i in range(0, MAX_CLIENTS):
    clients[i][0].send(b"Welcome to the chatroom!\nType 'quit' to exit")

msg = clients[0][0].recv(1024)
sender = 0  

while msg.decode("utf-8") != "quit":
    for i in range(0, MAX_CLIENTS):
        if i is not sender:
            clients[i][0].send(msg)
            msg = clients[i][0].recv(1024)
            sender = i

for i in range(0, MAX_CLIENTS):
    print("Stranger", i+1, "disconnected")
    clients[i][0].send(b"You have disconnected from the chatroom")
    clients[i][0].close()
    exit()


