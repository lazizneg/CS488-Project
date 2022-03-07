from email.message import Message
import socket

host = '192.168.233.128'
port = 5566
size = 1024
Message = 'Ping'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send(Message)
data = s.recv(size)
s.close()

print("received: ", repr(data))