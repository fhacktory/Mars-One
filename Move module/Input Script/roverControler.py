from sys import platform as _platform
import time, pygame
from pygame.locals import *


if _platform == 'darwin':
	import lightblue
elif _platform == 'linux2':
	import bluetooth


bd_addr = "00:17:EC:03:19:C6"
port = 1

pygame.init()

if _platform == 'darwin':
	sock=lightblue.socket()
	sock.connect((bd_addr, port))
elif _platform == 'linux2':
	sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
	sock.connect((bd_addr, port))
	screen = pygame.display.set_mode((640, 480))
	pygame.display.set_caption('Pygame Caption')
	pygame.mouse.set_visible(0)

print 'LETS GO !'

isRunning = True

while isRunning:
	left = 0
	right = 0
	
	pygame.event.pump()
	keys = pygame.key.get_pressed()
	print keys

	if keys[K_p]:
		isRunning = False
	elif keys[K_z] | keys[K_s] | keys[K_UP] | keys[K_DOWN]:
	    left = 100
	    right = 100
	    if keys[K_q] | keys[K_LEFT]:
	    	left -= 50
	    if keys[K_d] | keys[K_RIGHT]:
	    	right -= 50
	    if keys[K_s] | keys[K_DOWN]:
	    	left *= -1
	    	right *= -1
	elif keys[K_q] & keys[K_d]:
		left = 0
		right = 0
	elif keys[K_q] | keys[K_LEFT]:
		left = -100
		right = 100
	elif keys[K_d] | keys[K_RIGHT]:
		left = 100
		right = -100


	msg = 'm' +  ';' + str(left) + ';' + str(right)	
	sock.send(msg)
	print msg

	if not isRunning:
		sock.send('q')
		sock.close()

	time.sleep(0.1)
