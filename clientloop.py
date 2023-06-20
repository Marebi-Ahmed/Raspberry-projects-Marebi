import socket,json,random,time

#this IP is called "loop back IP add", if the connection is between the same device itself
loopback_IP="127.0.0.1"
server_IP="93.117.249.43"
server_port=11888
per=1
while(True):
    #1 create a socket of the server, to connect with
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #2 connect this socket to the server
    s.connect((loopback_IP,server_port))

    #3 send a request
    randata=random.randint(1,99)
    d={"identifier":"ABC321","val":randata,"type":"random"}
    encoded=json.dumps(d)  #this decode it into json
    message=bytes(encoded,encoding="utf8")  #encode it into bytes to be sent via internet
    s.sendall(message)

    #4 recieve a response
    data=s.recv(1024)

    #5 handle the response
    dataStr=data.decode()  #decode it from bytes
    print(dataStr)

    #6 close the socket
    s.close()
    
    time.sleep(per)
