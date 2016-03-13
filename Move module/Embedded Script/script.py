#!/usr/bin/python
# -*-coding:Latin-1 -*
#Script de communication entre le module EV3 et l'app
#Communication Bluetooth


import bluetooth
import time
from ev3dev.auto import *

print "starting programm"

server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port = 1
server_sock.bind(("",port))
server_sock.listen(1)

# Connect two large motors on output ports B and C:
ml = LargeMotor(OUTPUT_B)
mr = LargeMotor(OUTPUT_C)

assert ml.connected
assert mr.connected

ml.duty_cycle_sp=0
mr.duty_cycle_sp=0
ml.run_direct()
mr.run_direct()

print "Socket opened waiting for client"
client_sock,address = server_sock.accept()
print "Accepted connection from ",address



while 1:
    try :
    	data = client_sock.recv(1024)
    	print "received [%s]" % data
    	cmd=data.split(';')
    except :
    	#Le client a fermé son socket
    	print "Client disconnected, waiting for new one"
    	client_sock.close()
    	client_sock,address = server_sock.accept()
    	print "Accepted connection from ",address
    
    try :
    	if cmd[0]=='m':
    		ml.duty_cycle_sp=int(cmd[1])
    		mr.duty_cycle_sp=int(cmd[2])
    #Si erreur commande
    except:
    	print "erreur" 
    	#server_sock.send("Error : CMD_ERROR")    

#server_sock.send(u"Data Received"

server_sock.close()