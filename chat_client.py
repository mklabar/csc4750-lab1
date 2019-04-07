from socket import *
import sys

if len(sys.argv) !=3:
    print("\nInvalid syntax: please enter the IP address or hostname followed by the port number\n")
    exit()

#setup socket to connect to server
serverName = sys.argv[1]
serverPort = int(sys.argv[2])

clientSocket = socket(AF_INET, SOCK_STREAM) #TCP socket
clientSocket.connect((serverName, serverPort))

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
