#coding:utf-8
import os
myPath = "C://Users//rick//Desktop//"

def printTree(my_p,sNum = 0):
    list = os.listdir(my_p)  #获取当前目录列表
    for i in list:
        for j in range(0,sNum):
            print "- -",     #打印本次层数

        print str(i).decode('GBK')
        if (os.path.isdir(my_p+i)):
            printTree(my_p+i, sNum+1) #递归 进入目录
        else:
            continue
printTree(myPath)



