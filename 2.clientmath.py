import socket
import signal
import sys

ClientSocket = socket.socket()
host = 'put your server ip'
port = 8895

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response.decode("utf-8"))
while True:
    Input = input('\n[*]Enter the operation( L | S | E ) and number: ')

    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print(Response.decode("utf-8"))

ClientSocket.close()
