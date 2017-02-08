#coding=utf-8
import os,socket,thread,time

def get(duan):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect(("192.168.3.1",duan))
        data = sock.recv(5000)
        print str(data).__len__()," \a  ",duan,"   ",data
        sock.close()


for i in range(0,255*255):
    print i,
    try:
        thread.start_new_thread(get,i)
    except:
        pass
        print "  ",i," done"
    # time.sleep(2)