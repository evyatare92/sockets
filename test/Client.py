import socket
import sys

host = sys.argv[1]
port = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

msg = s.recv(1024)
print(msg.decode("utf-8"))