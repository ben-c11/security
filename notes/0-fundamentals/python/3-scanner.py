#!/bin/python3

#5.23.20 	Building Port Scanner

import sys
import socket
from datetime import datetime

#Define target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translate hostname to ipv4
else:
	print('Invalid amount of arguments')
	print('Syntax: python3 scanner.py <IP>')
	
#add in more errors: must be valid IP, 4 octets, can only be 0-255

# Add banner

print("-"*50)
print("Scanning target: " + target)
print("Time started: " + str(datetime.now()) #no work :(	
print("-"*50)


try:
	for port in range(50-85): #catch DNS and HTTP
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex(target,port)
		if result == 0:
			print(f"Port {port} is open")
		s.close()
		#if port open, connect_ex returns 0 and tells us that the port is open; this s.connect_ex is an error indicator. If  closed we close out of this port loop and move to the next one
		
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
except socket.gaierror:
	print("Hostname could not resolve")
	sys.exit()
except socket.error: #if we try to talk to IP but received nothing
	print("Could not connect to server")
	sys.exit()
	
#5.38.30
#ON VM make sure you can connect to your gateway on host OS.
#Works!! 5.40.00

#Accepting user input 5.41.50 --> New file input.py 
