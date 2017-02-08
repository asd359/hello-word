#coding:utf-8
import socket,os,struct

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",8000))
data = s.recv(2048)
data_unpack = struct.unpack("256sl",data)
print data_unpack[0],"  ",data_unpack[1]
s.send("ok")

with open("new.rar",'w') as f:
    i = data_unpack[1]
    while i>-1024:
        data = s.recv(1024)
        f.write(data)
        i = i-1024

    f.flush()
    f.close()


s.close()