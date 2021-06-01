import os
import json
system = os.name

if system == 'nt':
	message = json.dumps({'msg': 'hello windows'})
else:
	message = json.dumps({'msg': 'hello linux and other'})

print(message)
