#!/usr/bin/python
#Python version is 2.7.9
#Author: Martin Schmidt aka qw2100m

import socket
import time
import select

HOST = ""
PORT = 2269

socket.listen(max_players)

class Server():
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port       
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((HOST, PORT))        
        
    def wait_for_connections(self):
        """Just wait for everybody to connect."""
        self.max_players = input("Max number of players:")
        
        # Sockets from which we expect to read
        inputs = [ server ]  
        
        
    