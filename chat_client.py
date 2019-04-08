from socket import *
from struct import *
import sys

#if the command line argument is missing the IP/hostname or port number an error is printed
if len(sys.argv) !=3:
	print("\nInvalid syntax: please enter the IP address or hostname followed by the port number\n")
	exit()

#setup socket to connect to server, arg 1 is IP or hostname, arg 2 is port number
serverName = sys.argv[1]
serverPort = int(sys.argv[2])

clientSocket = socket(AF_INET, SOCK_STREAM) #TCP socket
clientSocket.connect((serverName, serverPort))

#broadcast a welcome message to all clients
message = clientSocket.recv(1024).decode('utf-8')
print("\n" + message + "\n", end = "", sep = "")

while True:
    #server passes 0 if client is receiver
    #server passes 1 if client is sender
    #server passes 2 if client is being disconnected
    #server passes 3 if a server message is incoming
    #server passes 4 if a bot message is incoming
	flag = int(clientSocket.recv(1))
	
	#prints message from other clients
	if(flag == 0):
		message = clientSocket.recv(1024).decode('utf-8')
		print("Stranger:", message)
	
	#accepts client input message and sends to server
	elif(flag == 1):
		message = input("Enter a message: ")
		clientSocket.send(message.encode('utf-8'))
	
	#client breaks to be disconnected
	elif flag == 2:
		break
	
    #prints message from server
	elif flag == 3:
		message = clientSocket.recv(1024).decode("utf-8")
		print("Server:", message)
	
    #prints message from bot
	elif flag == 4:
		message = clientSocket.recv(1024).decode("utf-8")
		print("Chatty Bot:", message)

#prints disconnection message and closes socket
print(clientSocket.recv(1024).decode("utf-8"))
clientSocket.close()
exit()
