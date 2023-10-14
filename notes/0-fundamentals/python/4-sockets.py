#!/bin/python3

#5.15.35 		Sockets


#Used to connect two nodes together - connecting to ports and IP addresses

import socket

HOST = 127.0.0.1  #loopback address of home network
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #af_inet = ipv4, sock_stream is port
s.connect((HOST,PORT)) #connect certain port on an IP

#nc = netcat; connect or establish listener on open port; terminal cmd: nc -nvlp 7777




#5.23.20 	Building Port Scanner

# please go to Scanner.py
