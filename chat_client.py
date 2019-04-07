from socket import *
from struct import *
import sys

if len(sys.argv) !=3:
    print("\nInvalid syntax: please enter the IP address or hostname followed by the port number\n")
    exit()

#setup socket to connect to server
serverName = sys.argv[1]
serverPort = int(sys.argv[2])

clientSocket = socket(AF_INET, SOCK_STREAM) #TCP socket
clientSocket.connect((serverName, serverPort))

recv_len = 0

#receive message from server, print it, close connection
message = clientSocket.recv(1024).decode('utf-8')
print("\n" + message + "\n", end = "", sep = "")

while True:
    #server passes 1/True if client is sender
    #passes 0/False if client is receiver
	flag = int(clientSocket.recv(1))
	
	if(flag == 0):
			#recv_len = int.from_bytes(clientSocket.recv(4), 'big')
			#message = clientSocket.recv(recv_len).decode('utf-8')
			message = clientSocket.recv(1024).decode('utf-8')
			print("Stranger:", message)
	elif(flag == 1):
			message = input("Enter a message: ")
			message_len = len(message)
			#clientSocket.send(bytes([message_len & 0xFFFFFFFF])) 
			clientSocket.send(message.encode('utf-8'))
	elif flag == 2:
		break
	elif flag == 3:
		message = clientSocket.recv(1024).decode("utf-8")
		print("Server:", message)
	elif flag == 4:
		message = clientSocket.recv(1024).decode("utf-8")
		print("Chatty Bot:", message)
		
print(clientSocket.recv(1024).decode("utf-8"))
clientSocket.close()
exit()
