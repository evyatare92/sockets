import socket
import sys

host = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

x = 1
msg = s.recv(1024)
print(msg.decode("utf-8"))