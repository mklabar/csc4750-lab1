Chatty Master 

Chatty Master is a Client to Server chat program that allows users to send and receive messages directly.

Chatty Master can be used with an unlimited amount of clients in the same chat room! The server keeps an ordered list of all the clients connected. The server then cycles through the list in order to determine whose turn it is to send a message. Clients cannot send messages willy-nilly! They must wait. When it is a client's turn to send a message the server will notify the client behind the scenes, and the client will prompt the user to send a message.

Configuration:

To configure the server with the number of clients you would like in your chat room, change the value of MAX_CLIENTS in the chat_server.py file. Note: the server will not begin the chat room experience until the max clients has been reached. Once one client disconnects, the server disconnects everyone and shuts itself down.

Connecting via IP and Host:

To connect a client to the server via command line, you must specify the connection (IP or host name is acceptable) and the port number.

Example:

Connecting with IP:
	
	$python3 chat_client.py 127.0.0.1 43500

Connecting with host name:	

	$python3 chat_client.py localhost 43500

Command List:
	
	/help displays the command list and !bot list
	/quit disconnects client and all others from chat room

Bot List:

Type !bot to interact with our friendly Chatty Master bot!

	!bot quote to receive a random quote from a famous robot
	!bot spellcheck to receive a spelling lesson
	!bot time to find out the current time

