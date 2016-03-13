#!/usr/bin/python
# -*-coding:Latin-1 -*
#Script de communication entre le module EV3 et l'app
#Communication Bluetooth


import bluetooth
import time
from ev3dev.auto import *
import ev3dev.ev3 as ev3

print "starting programm"

server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port = 1
server_sock.bind(("",port))
server_sock.listen(1)

# Connect two large motors on output ports B and C:
motor_left = LargeMotor(OUTPUT_B)
motor_right = LargeMotor(OUTPUT_C)

#Touche sensor
ts = TouchSensor();    assert ts.connected

assert motor_left.connected
assert motor_right.connected

motor_left.duty_cycle_sp=0
motor_right.duty_cycle_sp=0
motor_left.run_direct()
motor_right.run_direct()

print "Socket opened waiting for client"
client_sock,address = server_sock.accept()
print "Accepted connection from ",address
client_sock.sendto("Bienvenue sur EV3",address)
motor_right.position=0
motor_left.position=0


def Obs():
	#son
	
	#Red leds on
	for light in (Leds.LEFT, Leds.RIGHT):
		Leds.set_color(light, Leds.RED)
    #motors stop
	motor_left.stop(stop_command='brake')
	motor_right.stop(stop_command='brake')
	#Sound.tone([(1000, 500, 500)] * 3)
	ev3.Sound.speak('OOps I dit it again').wait()
    #Backward for 1.5 sec
	motor_left.run_timed(duty_cycle_sp=-50, time_sp=1500)
	motor_right.run_timed(duty_cycle_sp=-50, time_sp=1500)
	time.sleep(1.55)
    #Green led on
	for light in (Leds.LEFT, Leds.RIGHT):
		Leds.set_color(light, Leds.GREEN)
	motor_left.run_direct()
	motor_right.run_direct()
while 1:
	if ts.value():
		Obs()
		continue
	try :
		data = client_sock.recv(1024)
    	#print "received [%s]" % data
		
		cmd=data.split(';')
	except :
		#client closed socket
		print "Client disconnected, waiting for new one"
		client_sock.close()
		client_sock,address = server_sock.accept()
		print "Accepted connection from ",address
		client_sock.sendto("Welcome on EV3",address)
		motor_right.position=0
		motor_left.position=0

	client_sock.sendto(str(motor_left.position)+'\n',address)
	client_sock.sendto(str(motor_right.position)+'\n',address)
	motor_right.position=0
	motor_left.position=0	

	try :
		if cmd[0]=='m':
			motor_left.duty_cycle_sp=int(cmd[1])
			motor_right.duty_cycle_sp=int(cmd[2])
	#if cmd error
	except:
		print "erreur" 
    	    


server_sock.close()