from socket import *
from struct import *
import random
import time
import datetime
 

#setup socket to wait for connections
serverPort = 43500
serverSocket = socket(AF_INET, SOCK_STREAM) #TCP (reliable)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #make port reusable
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
MAX_CLIENTS = int(input("Please enter the number of expected clients: "))
print('The server is ready to accept', MAX_CLIENTS, 'clients on port', serverPort)


clients = []
quotes = ["Who's ready to fly on a zipline? I am!",
 "Shut up baby I know it!",
 "Bwee, hoo hoo, bwoo.",
 "I'm sorry Dave. I just can't do that.",
 "Error 404: Sarcasm module not found",
 "Don't you call me a mindless philosopher you overweight glob of grease!",
 "Would you like more butter?",
 "VOIP",
 "Be... Good...",
 "Autobots, roll out!",
 "DANGER WILL ROBINSON",
 "At least ~your~ keyboard is dry",]
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
random.seed()
while True:
	clients[sender][0].send(b"1")
	#msg_len = int.from_bytes(clients[sender][0].recv(4), 'big')
	#msg = clients[sender][0].recv(msg_len)
	msg = clients[sender][0].recv(1024)
	msg_dc = msg.decode("utf-8")
	
	if msg_dc == "quit":
		break
	
	for i in range(0, MAX_CLIENTS):
		if i != sender:
			clients[i][0].send(b"0")
			#clients[i][0].send(bytes([msg_len & 0xFFFFFFFF]))
			clients[i][0].send(msg)
			time.sleep(.01)
	
	if msg_dc[0:5] == "!bot ":
		if "quote" in msg_dc:
			msg = quotes[random.randint(0,11)]
		elif "time" in msg_dc:
			msg = str(datetime.datetime.now())
		for i in range(0, MAX_CLIENTS):
			clients[i][0].send(b"3")
			clients[i][0].sendall(msg.encode("utf-8"))
			time.sleep(.01)
		
			
			
	
	sender += 1
	if sender == MAX_CLIENTS:
		sender = 0

for i in range(0, MAX_CLIENTS):
	print("Stranger", i+1, "disconnected")
	clients[i][0].send(b"2")
	clients[i][0].send(b"You have been disconnected from the chatroom")
	clients[i][0].close()

exit()


