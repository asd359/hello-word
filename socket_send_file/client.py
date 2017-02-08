#coding:utf-8
#Using GPL v2
import socket

# from __future__ import division
import math
import sys,time,os,json


# def progressbar(cur, total):
# 	percent = '{:.2%}'.format(cur / total)
# 	sys.stdout.write('\r')
# 	sys.stdout.write('[%-50s] %s' % ('=' * int(math.floor(cur * 50 / total)), percent))
# 	sys.stdout.flush()
# 	if cur == total:
#
# 		sys.stdout.write('\n')


# if __name__ == '__main__':
# 	file_size = 100
# 	size = 10
# 	while file_size > 0:
# 		progressbar(size * 10 / file_size, 10)
# 		file_size -= 10
# 		time.sleep(0.1)


	# ip_port = (('123.207.170.247',8000))
# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.connect(ip_port)
# while True:
# 	data = sock.recv(1024)
# 	print 'receive',data
# 	inp = raw_input('please input:')
# 	sock.sendall(inp)
# 	if inp == 'exit':
# 		break
# sock.close()
#

# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.connect(('127.1.1.1',8000))
# sock.send('hello I am your user')
# print "想下载文件么 ",sock.recv(512)


sock_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_.connect(('127.1.1.1', 8001))
sock_.send('I am coming')
file_name = sock_.recv(512)
print "你想下载这个文件么？y/n",file_name
user_in_put = raw_input()
# user_in_put = "y"
if user_in_put == "y":
	with open(file_name,'w') as f:
		loop = 0
		mb = 1
		while True:
			data = sock_.recv(512)
			f.write(data)
			if len(data) == 0 :
				break

else:
	pass

sock_.close()
# sock.close()


# num = -1
# while True:
# 	print  "请输入要下载的文件，例如：get 0。退出输入：q or e"
# 	user_in_put = raw_input()
# 	if	user_in_put == "e" or "q":
# 		break
# 	else:
# 		if int(user_in_put.replace("get ","")) >= 0:
# 			num = int(user_in_put.replace("get ",""))
# 			break
# if	num >= 0:
# 	sock.send(num)
#
#
# else:
# 	pass
#





