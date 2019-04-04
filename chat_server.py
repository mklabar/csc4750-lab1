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

for i in range(0, MAX_CLIENTS):
    clients[i][0].send(b"Welcome to the chatroom!\nType 'quit' to exit")

sender = 0
msg = ""
while True:
    clients[sender][0].send(b"1")
    msg = clients[sender][0].recv(1024)
    
    if msg.decode("utf-8") == "quit":
        break

    for i in range(0, MAX_CLIENTS):
        if i != sender:
            clients[i][0].send(b"0")
            clients[i][0].send(msg)
    
    sender += 1
    if sender == MAX_CLIENTS:
        sender = 0

for i in range(0, MAX_CLIENTS):
    print("Stranger", i+1, "disconnected")
    clients[i][0].send(b"-1")
    clients[i][0].send(b"You have been disconnected from the chatroom")
    clients[i][0].close()

exit()


