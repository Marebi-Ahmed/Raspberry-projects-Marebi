import socket

#1 create socket of the client, to connect with
#arguments: 1)communication way ex: internet. 2) internet communication type.
socket1=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #SOCK_STREAM MEANS TCP

# 2 blinds the socket to IP/port of the client
socket1.bind(("",11999))

#3 listen to the connection
socket1.listen(3)   #number of clients

#4 accept the connection
conn,addr=socket1.accept()
#this returns, the connection and the address of the client
#the address also consists of (IP/port)
print(addr)

#5 recieve the request
req=conn.recv(1024)
#number of bytes to recieve, if we don't know the length, prefer put multiple of 512 or 1024

#6 handle the request
reqStr=req.decode()
print(reqStr)

#send a response
message=b"I got your request!" #we make it in bytes (bits), since the connection is in bytes
conn.sendall(message)

#close the connection
socket1.close()