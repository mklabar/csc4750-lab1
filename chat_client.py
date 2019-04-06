from socket import *
from struct import *
#setup socket to connect to server
serverName = 'localhost'
serverPort = int(input("Enter port number: "))
clientSocket = socket(AF_INET, SOCK_STREAM) #TCP socket
clientSocket.connect((serverName, serverPort))
recv_len = 0
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
		message_len = len(message)
		clientSocket.send(bytes([message_len & 0xFFFFFFFF])) 
		clientSocket.send(message.encode('utf-8'))
	else:
		recv_len = int.from_bytes(clientSocket.recv(4), 'big')
		message = clientSocket.recv(recv_len).decode('utf-8')
		print("Stranger:", message)

print(clientSocket.recv(1024).decode("utf-8"))
clientSocket.close()
exit()
