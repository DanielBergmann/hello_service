import socket
import json
sock = socket.socket()
sock.connect(('localhost', 10001))
sock.send(b'hello, world!')
data = sock.recv(1024)
sock.close()
print(json.loads(data))
