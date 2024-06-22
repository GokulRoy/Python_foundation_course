import socket
c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

c.connect((socket.gethostname(),9999))
name = input("Enter your name ")
c.send(bytes(name,'utf-8'))
# c.send(bytes('welcome to telusko', 'utf-8'))
msg = c.recv(2056).decode()
print("message received",msg)
