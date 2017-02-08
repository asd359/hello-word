#coding:utf-8
import socket,os,struct

path = "SFM.rar"
# path = "2.txt"
m = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
m.bind(("",8000))
m.listen(1)
conn,addr = m.accept()
print "Connected by",addr

# print os.path.basename(path),#文件名字
# print os.stat(path).st_size  #文件大小

file_head = struct.pack("256sl",os.path.basename(path),os.stat(path).st_size)
print file_head.__len__()
conn.send(file_head)
print conn.recv(128)

file = open(path,'r')
i = os.stat(path).st_size
while i > -1024:
    file_con = file.read(1024)#每次读取字节数
    conn.send(file_con)
    i = i-1024

    # print file_con,


conn.close()
m.close()