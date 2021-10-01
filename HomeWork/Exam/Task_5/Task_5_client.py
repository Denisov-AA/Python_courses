import socket
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.0.188'
port = 5555
s.gettimeout()
s.connect((host, port))
message = str(random.randint(1, 10))
print(f"Requested manufacturer ID - {message}")
s.send(message.encode())
data = s.recv(1024)
print('Received Data: {}'.format(data.decode()))
s.close()
