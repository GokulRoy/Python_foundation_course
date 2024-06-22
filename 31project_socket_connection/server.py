import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('socket created')
s.bind((socket.gethostname(), 9999))
s.listen(3) #no of clients at one point is x =3
print('waiting for the connection')
while True:
    c, addr = s.accept() # c for client s for server
    print("connected with",addr)
    name = c.recv(2056)
    print("connected with",name)
    c.send(bytes("welcome to gokul", 'utf-8'))
    # always close the server
    c.close()

