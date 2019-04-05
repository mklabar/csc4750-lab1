from socket import *

#setup socket to connect to server
serverName = 'localhost'
serverPort = int(input("Enter port number: "))
clientSocket = socket(AF_INET, SOCK_STREAM) #TCP socket
clientSocket.connect((serverName, serverPort))

#receive message from server, print it, close connection
message = clientSocket.recv(1024).decode('utf-8')
print(message)

while True:
    #server passes 1/True if client is sender
    #passes 0/False if client is receiver
    flag = int(clientSocket.recv(1))
    if flag == 2:
        break
    sender = flag == 1

    if(sender):
        message = input("Enter a message: ")
        clientSocket.send(message.encode('utf-8'))
    else:
       message = clientSocket.recv(1024).decode('utf-8')
       print("Stranger:", message)

print(clientSocket.recv(1024).decode("utf-8"))
clientSocket.close()
exit()
