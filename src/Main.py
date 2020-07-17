from Morse import encrypt
import socket
import os

port = int(os.getenv("SOCKET_PORT"))
queue_length = int(os.getenv("SOCKET_QUEUE_LENGTH"))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", port))
s.listen(queue_length)

while True:
    clientsocket, address = s.accept()
    morse_ip = encrypt(address[0])
    clientsocket.send(bytes(f"your ip in morse code is {morse_ip}","utf-8"))
    clientsocket.close()
