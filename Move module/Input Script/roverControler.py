from getch import getch 
import lightblue

bd_addr = "00:17:EC:03:19:C6"

port = 1

sock=lightblue.socket()
sock.connect((bd_addr, port))

sock.send("hello!")
print 'LETS GO !'

while 1:
	msg = 'empty'
	quit = False
	key = getch()
	if key == 'z':
		msg = 'f'
	elif key == 's':
		msg = 'b'
	elif key == 'q':
		msg = 'l'
	elif key == 'd':
		msg = 'r'
	elif key == 'x' :
		msg = 'x'
	elif key == 'p':
		msg = 'q'
		quit = True
		
	if msg != 'empty':
		sock.send(msg)
		print msg

	if quit:
		sock.close()
		break
