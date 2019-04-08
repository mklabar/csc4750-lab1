# Chatty Master 

Chatty Master is a Client to Server chat program that allows users to send and receive messages directly.

Chatty Master can be used with an unlimited amount of clients in the same chat room! The server keeps an ordered list of all the clients connected. The server then cycles through the list in order to determine whose turn it is to send a message. Clients cannot send messages willy-nilly! They must wait. When it is a client's turn to send a message the server will notify the client behind the scenes, and the client will prompt the user to send a message.

## Installation Requirements:

Chatty Master uses the module `pyspellchecker`. To install this module follow these instructions:

\1. If you already have `pip` installed, skip this step. To install `pip` first update your Linux version to 18.04:
	
	$sudo apt update

To install `pip`:

	$sudo apt install python3-pip

To double check you have the correct version of `pip`:

	$pip3 --version

Output may look something like this:

	pip 9.01 from /usr/lib/python3/dist-packages (python 3.6)

\2. To install `pyspellchecker`:

	$pip3 install pyspellchecker

If you run into any issues, the github for `pyspellchecker` can be found [here.](https://github.com/barrust/pyspellchecker)

## Server Configuration:

### Specifiying number of clients:

Chatty Master can be used with any number of clients! When running the server, you will be prompted to specify the number of clients expected. Note: the chatroom will not initiate until the number of clients expected have connected. This is not just a maximum, it is also a minimum. Once one client disconnects, the server disconnects all other clients and shuts itself down.

### Connecting via IP and Host:

To connect a client to the server via command line, you must specify the connection (IP or host name is acceptable) and the port number.

Example:

#### Connecting with IP:
	
	$python3 chat_client.py 127.0.0.1 43500

#### Connecting with host name:	

	$python3 chat_client.py localhost 43500

## Command List:
	
	/help displays the command list and !bot list
	/quit disconnects all clients from chat room

## Bot List:

Type !bot to interact with our friendly Chatty bot!

	!bot quote to receive a random quote from a famous robot
	!bot spellcheck to receive a spelling lesson
	!bot time to find out the current time

