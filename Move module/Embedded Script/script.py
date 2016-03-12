#!/usr/bin/python
#Script de communication entre le module EV3 et l'app
#Communication Bluetooth


import bluetooth
import time
from ev3dev.auto import *

print "starting programm"

server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

time.sleep(0.1)
port = 1
server_sock.bind(("",port))
server_sock.listen(1)

# Connect two large motors on output ports B and C:
ml = LargeMotor(OUTPUT_B)
mr = LargeMotor(OUTPUT_C)

assert ml.connected
assert mr.connected


def forward():
    """
    Start both motors. `run-direct` command will allow to vary motor
    performance on the fly by adjusting `duty_cycle_sp` attribute.
    """
    ml.duty_cycle_sp=100
    mr.duty_cycle_sp=100
    ml.run_direct()
    mr.run_direct()


def backward():

    ml.duty_cycle_sp=-100
    mr.duty_cycle_sp=-100
    ml.run_direct()
    mr.run_direct()

def stop():
	ml.stop()
	mr.stop()

def left():
	stop()
	#ml.duty_cycle_sp=-40
	#mr.duty_cycle_sp=40
	ml.run_timed(duty_cycle_sp=-40, time_sp=500)
	mr.run_timed(duty_cycle_sp=40, time_sp=500)
	time.sleep(0.500)

def right():
	stop()
	#ml.duty_cycle_sp=-40
	#mr.duty_cycle_sp=40
	ml.run_timed(duty_cycle_sp=40, time_sp=500)
	mr.run_timed(duty_cycle_sp=-40, time_sp=500)
	time.sleep(0.500)


print "Socket opened waiting for client"
client_sock,address = server_sock.accept()
print "Accepted connection from ",address



while 1:
    data = client_sock.recv(1024)
    print "received [%s]" % data
    if data == 'q':
    	stop()
    	break
    elif data=='f':
    	print "go forward"
    	forward()
    elif data=='b':
    	backward()
    elif data=='l':
    	left()
    elif data=='r' :
    	right()
    elif data=='x':
    	stop()

#server_sock.send(u"Data Received")

client_sock.close()
server_sock.close()