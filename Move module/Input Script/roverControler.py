#from getch import getch 
import bluetooth, time, pygame
from pygame.locals import *

bd_addr = "00:17:EC:03:19:C6"
port = 1

pygame.init()

#sock=lightblue.socket()
#sock.connect((bd_addr, port))
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

print 'LETS GO !'

isRunning = True

while isRunning:
	left = 0
	right = 0
	
	pygame.event.pump()
	keys = pygame.key.get_pressed()

	if keys[K_p]:
		isRunning = False
	elif keys[K_z] | keys[K_s]:
	    left = 100
	    right = 100
	    if keys[K_q]:
	    	left -= 50
	    if keys[K_d]:
	    	right -= 50
	    if keys[K_s]:
	    	left *= -1
	    	right *= -1
	elif keys[K_q] & keys[K_d]:
		left = 0
		right = 0
	elif keys[K_q]:
		left = -100
		right = 100
	elif keys[K_d]:
		left = 100
		right = -100


	msg = 'm' +  ';' + str(left) + ';' + str(right)	
	sock.send(msg)
	print msg

	if not isRunning:
		sock.send('q')
		sock.close()

	time.sleep(0.1)
