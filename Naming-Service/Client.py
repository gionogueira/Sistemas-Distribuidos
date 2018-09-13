import socket


IP = '127.0.0.1'
PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

ServerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ServerSock.connect((IP, PORT))
ServerSock.send(MESSAGE)
DataServer  = ServerSock.recv(BUFFER_SIZE)

print "Received data:", DataServer
 
ServerSock.close()


