from socket import *
from struct import *
import random
import time
import datetime
from spellchecker import SpellChecker

#setup socket to wait for connections
serverPort = 43500
serverSocket = socket(AF_INET, SOCK_STREAM) #TCP (reliable)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #make port reusable
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
MAX_CLIENTS = int(input("Please enter the number of expected clients: "))
print('The server is ready to accept', MAX_CLIENTS, 'clients on port', serverPort)

spell = SpellChecker()
clients = []
quotes = ["Who's ready to fly on a zipline? I am!",
 "Shut up baby I know it!",
 "Bwee, hoo hoo, bwoo.",
 "I'm sorry Dave. I just can't do that.",
 "Error 404: Sarcasm module not found",
 "Don't you call me a mindless philosopher you overweight glob of grease!",
 "Would you like more butter?",
 "VOIP!",
 "Be... Good...",
 "Autobots, roll out!",
 "DANGER, WILL ROBINSON!",
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
    clients[i][0].send(b"Welcome to the chatroom!\nType '/help' for a list of commands")

sender = 0
msg = ""
random.seed()
while True:
	clients[sender][0].send(b"1")
	#msg_len = int.from_bytes(clients[sender][0].recv(4), 'big')
	#msg = clients[sender][0].recv(msg_len)
	msg = clients[sender][0].recv(1024)
	msg_dc = msg.decode("utf-8")
	
	if msg_dc[0] == "/" or msg_dc[0] == "!":
		flag = "3"
		if msg_dc == "/quit":
			break
		elif msg_dc == "/help":
			msg = "\n\tCommands:\n\n\t\t/help\tdisplays the list of commands\
			\n\t\t/quit\tdisconnects all clients from the server\
			\n\n\tBot Commands:\n\n\t\t!bot quote\tChatty Bot says a famous robot quote\
			\n\t\t!bot time\tChatty Bot tells the current time\n\
			!bot spellcheck\tChatty bot accepts one word and gives you corrected word recommendations\n"
		elif msg_dc[0:5] == "!bot ":
			flag = "4"
			if "quote" in msg_dc:
				msg = quotes[random.randint(0,11)]
			elif "time" in msg_dc:
				msg = "The current time is " + datetime.datetime.now().strftime("%I:%M %p")
			elif "spellcheck" in msg_dc:
				msg_array = msg_dc.split()
				misspelled = spell.unknown(msg_array)
				candidates = spell.candidates(msg_array[2])
				msg = "You may mean"
				for word in candidates:
					msg = msg + " " + word
			else:
				msg = "I'm sorry, I don't know that command yet!\
				Type '/help' for a list of commands"
		else:
			msg = "Command does not exist. Type '/help' for a list of commmands"
		
		for i in range(0, MAX_CLIENTS):
			clients[i][0].send(flag.encode("utf-8"))
			clients[i][0].sendall(msg.encode("utf-8"))
			time.sleep(.01)
	else:
		for i in range(0, MAX_CLIENTS):
			if i != sender:
				clients[i][0].send(b"0")
			#clients[i][0].send(bytes([msg_len & 0xFFFFFFFF]))
				clients[i][0].send(msg)
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


