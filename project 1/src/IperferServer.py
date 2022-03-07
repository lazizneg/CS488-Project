import socket

host = '192.168.233.128'
port = 5566
size = 20

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
print(host , port)
s.listen(1)
conn, addr = s.accept()

print('Connected by', addr)
while True:
    try:
        data = conn.recv(size)
    if not data: break
        print("received: ", repr(data))
        conn.send(data) 
    except socket.error:
        print("Error Occured") 
        break
conn.close()