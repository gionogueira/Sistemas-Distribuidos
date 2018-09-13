import socket


IP = '127.0.0.1'
PORT = 5005
BUFFER_SIZE = 1024  

ServerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ServerSock.bind((IP, PORT))
ServerSock.listen(1)

Conn, Addr = ServerSock.accept()

while 1:
    DataClient = Conn.recv(BUFFER_SIZE)
    if not DataClient: break
    Host = socket.gethostbyname(DataClient)
    print DataClient + " : " + Host 
    Conn.send(Host)  # echo

    Conn.close()