import os
import json
import socket

system = os.name

if system == 'nt':
	message = json.dumps({'msg': 'hello windows'})
else:
	message = json.dumps({'msg': 'hello linux and other'})

print(message)

sock = socket.socket()
sock.bind(('', 10001))
sock.listen(1)

try:
	while True:
		conn, addr = sock.accept()
		data = conn.recv(1024)
		conn.send(message.encode())
finally:
	sock.shutdown(0)
	sock.close()
