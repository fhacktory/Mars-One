from sys import platform as _platform
import time, pygame, socket, errno
from pygame.locals import *

#import bluetooth for mac or linux
if _platform == 'darwin':
    import lightblue
elif _platform == 'linux2':
    import bluetooth

#bluetooth constantes
bd_addr = "00:17:EC:03:19:C6"
port = 1

isRunning = True

#init socket
if _platform == 'darwin':
    sock=lightblue.socket()
elif _platform == 'linux2':
    sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

#init pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pygame Caption')
pygame.mouse.set_visible(0)

#connect socket
try :
    sock.connect((bd_addr, port))
    sock.setblocking(0)
    isConnect = True
except :
    # Cannot connect the rover
    print "Impossible to connect the Rover. Restart script"
    isConnect = False

print 'LETS GO !'

while isRunning & isConnect:

    try:
        data = sock.recv(1024)
        print data
    except :
        print 'No data available'

    left = 0
    right = 0
    
    pygame.event.pump()
    keys = pygame.key.get_pressed()

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
    try :
        sock.send(msg)
    except :
        print "Connection lost"
        isConnect = False
    #print msg

    if not isRunning:
        try :
            sock.send('q')
        except :
            print "Connection lost"
            isConnect = False

    # Loop frequency
    time.sleep(0.1)

sock.close()