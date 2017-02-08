#!/usr/bin/python
#coding:utf-8

import os
import json
import time
import threading
import SocketServer
from package.get_file_tree import get_tree_list
from  package.socket_file_info import socket_info

# data_info = socket_info()  # 用于将文件地址 转换成编辑好的字典信息y
# file_ls = get_tree_list().get_tree_ls("C:\\Users\\rick\\Desktop\\ss")
path = "t.bmp" #这个path是全局变量的Path
# 设置SocektServer的handler
class send_file(SocketServer.BaseRequestHandler):
    # list_num = 0
    def setup(self):#类似于构造函数   setup不可接受参数
        # pass
        self.file = open(path,'r')
        self.content = self.file.read()
        self.request.sendall(path)
        # pass
    def handle(self):
        print "%s:%s is connected"%self.client_address
        request_data = self.request.recv(512)
        #self.request:是在模板类当中封装好的接收和发送信息的对象，是一个socket对象
        print request_data

        self.request.sendall(self.content)

        # data_info  #用于将文件地址 转换成编辑好的字典信息
        # file_ls
        # print self.list_num
        # if self.list_num >= len(file_ls):
        #     self.request.sendall("-1")
        # else:
        #     self.request.sendall(str(file_ls[self.list_num]))
        #     self.list_num = self.list_num+1
            # self.request.sendall("ffffffffffffff9999999")
        # self.request.sendall(str(file_ls))
        # print self.request.recv(512)


    def finish(self):#类似于类当中的析构函数
        print "%s is done"%self.client_address[0]
        if self.file.closed == False:
            self.file.close()
#-----------------------------------------------------
# class send_info(SocketServer.BaseRequestHandler):
#     def setup(self):  # 类似于构造函数   setup不可接受参数
#         pass
#     def handle(self):
#         print "%s:%s is connected" % self.client_address
#         request_data = self.request.recv(512)
#         # self.request:是在模板类当中封装好的接收和发送信息的对象，是一个socket对象
#         print request_data
#
#         self.request.sendall(str(path))
#
#     def finish(self):  # 类似于类当中的析构函数
#         print "%s is done" % self.client_address[0]


#-------------------------------------





#通过多继承形成新的支持多线程的服务器
class MyServer(SocketServer.TCPServer,SocketServer.ThreadingMixIn,):
    pass


# data_info = socket_info()  # 用于将文件地址 转换成编辑好的字典信息
# file_ls = get_tree_list().get_tree_ls("C:\\Users\\rick\\Desktop\\ss")
# for i in file_ls:  # -----------向客户端发送文件列表
#     print data_info.get_info(i)

# m_info = MyServer(("",8000),send_info)
# th_info = threading.Thread(target = m_info.serve_forever(),args = ())
# th_info.start()
# m_info.shutdown()
# m_info.server_close()

#实例化服务器 将我们要绑定的地址和写好的Handler作为参数传入
m = MyServer(("",8001),send_file)
#启动多线程
th = threading.Thread(target = m.serve_forever(),args = ())
th.start()
m.shutdown()
m.server_close()

