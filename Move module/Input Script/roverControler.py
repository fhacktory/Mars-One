from sys import platform as _platform
import time, pygame
from pygame.locals import *


if _platform == 'darwin':
	import lightblue
elif _platform == 'linux2':
	import bluetooth


bd_addr = "00:17:EC:03:19:C6"
port = 1

isRunning = True

pygame.init()

if _platform == 'darwin':
	sock=lightblue.socket()
elif _platform == 'linux2':
	sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pygame Caption')
pygame.mouse.set_visible(0)

try :
	sock.connect((bd_addr, port))
	isConnect = True
except :
	# Cannot connect the rover
	print "Impossible to connect the Rover. Restart script"
	isConnect = False

print 'LETS GO !'

while isRunning & isConnect:
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
	try :
		sock.send(msg)
	except :
		print "Connection lost"
		isConnect = False
	print msg

	if not isRunning:
		try :
			sock.send('q')
		except :
			print "Connection lost"
			isConnect = False

	# Loop frequency
	time.sleep(0.1)

sock.close()
