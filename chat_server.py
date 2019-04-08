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

#on runtime server asks for the number of clients
MAX_CLIENTS = int(input("Please enter the number of expected clients: "))

#confirmation message on server side
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

#waits for max number of clients to connect
#prints confirmation on server side they have connected
for i in range(0, MAX_CLIENTS):
    connectionSocket, addr = serverSocket.accept()
    clients.append((connectionSocket, addr))
    if i < MAX_CLIENTS:
        print("Stranger", i+1, "connected")

#broadcasts a welcome message to all clients upon connection
for i in range(0, MAX_CLIENTS):
    clients[i][0].send(b"Welcome to the chatroom!\nType '/help' for a list of commands")

sender = 0
msg = ""
random.seed()
flag = "0"

while True:
	#sends 1 to client whose turn it is to send message
	clients[sender][0].send(b"1")
	
	#receives message from client
	msg = clients[sender][0].recv(1024)
	
	#saves decoded message string
	msg_dc = msg.decode("utf-8")
	
	#checks if message is a command or a bot call
	if msg_dc[0] == "/" or msg_dc[0] == "!":
		
		#sets flag to 3 for server message
		flag = "3"
		
		#breaks to disconnect users from server
		if msg_dc == "/quit":
			break
		
		#displays help message
		elif msg_dc == "/help":
			msg = "\n\tCommands:\
			\n\n\t/help\tdisplays the list of commands\
			\n\t/quit\tdisconnects all clients from the server\
			\n\n\tBot Commands:\
			\n\n\t!bot quote\tChatty Bot says a famous robot quote\
			\n\t!bot time\tChatty Bot tells the current time\
			\n\t!bot spellcheck\tChatty bot gives a list of spelling\
			\t\t\t\tcorrections for the first typed word\n"
		
		elif msg_dc[0:5] == "!bot ":
			
			#sets flag to 4 for bot message
			flag = "4"
			
			#if the message contains quote, set msg to a random quote from list
			if "quote" in msg_dc:
				msg = quotes[random.randint(0,11)]
			
			#if the message contains time, set msg to current time
			elif "time" in msg_dc:
				msg = "The current time is " + datetime.datetime.now().strftime("%I:%M %p")
			
			#if the message contains spellcheck then the msg gives spelling recommendations
			#only for the word following bot call (index 2)
			elif "spellcheck" in msg_dc:
				msg_array = msg_dc.split()
				misspelled = spell.unknown(msg_array)
				candidates = spell.candidates(msg_array[2])
				msg = "You may mean..."
				
				#lists all possible correct spellings
				for word in candidates:
					msg = msg + " " + word
			
			#if called !bot but did not list proper command, msg set to bot error
			else:
				msg = "I'm sorry, I don't know that command yet!\
				\n\t    Type '/help' for a list of commands"
		
		#if message starts with '/' or '!' but does not match a proper command, msg set to general error
		else:
			msg = "Command does not exist. Type '/help' for a list of commands"
		 
		for i in range(0, MAX_CLIENTS):
			#sends flag (either 3 or 4), sleeps to avoid jamming
			clients[i][0].send(flag.encode("utf-8"))
			time.sleep(.01)
			
			#sends message
			clients[i][0].send(msg.encode("utf-8"))
	
	#if message is not a bot call or command, sends message to everyone EXCEPT sender
	else:
		for i in range(0, MAX_CLIENTS):
			if i != sender:
				#sends flag 0 to indicate receiving, sleeps to avoid jamming
				clients[i][0].send(b"0")
				time.sleep(.01)
				
				#sends message
				clients[i][0].send(msg)
		
	#to rotate senders, sender iterates by 1
	sender += 1
	
	#if sender == max, wraps around back to 0
	if sender == MAX_CLIENTS:
		sender = 0

#client sent '/quit'
for i in range(0, MAX_CLIENTS):
	
	#displays confirmation on server side
	print("Stranger", i+1, "disconnected")
	
	#sends quitting flag, sleeps to avoid jamming
	clients[i][0].send(b"2")
	time.sleep(.01)
	
	#sends disconnection message
	clients[i][0].send(b"You have been disconnected from the chatroom")
	clients[i][0].close()

exit()


