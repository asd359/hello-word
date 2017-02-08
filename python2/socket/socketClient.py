#coding=utf-8
import socket

_ADDR_ = ("127.0.0.1",6000)
socketC = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socketC.connect(_ADDR_)
while True :
    print "start"
    data = raw_input(">>>>:")
    socketC.send("client:"+str(data).replace(">>>>:",""))

    receive = str(socketC.recv(100))
    if  receive.find("end") >=0:#找到end 就退出
        break

    print receive

socketC.close()

