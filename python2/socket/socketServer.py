#coding=utf-8
import socket

_SERVER_ADDR_ = ("",6000)
socketS = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socketS.bind(_SERVER_ADDR_)
socketS.listen(5)
clientSock,addr = socketS.accept()
while True:
    print "start"


    receive = str(clientSock.recv(100))
    print addr,":",receive
    if  receive.find("end") >=0:
        clientSock.send("goodbye end")
        break
    else:
        clientSock.send("im server ")
socketS.close()



