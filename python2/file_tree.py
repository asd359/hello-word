#coding:utf-8
import os
myPath = "C:\\Users\\rick\\Desktop\\pycode"

def printTree(my_p,sNum = 0):
    list = os.listdir(my_p)
    for i in list:
        for j in range(0,sNum):
            print "- -",

        try:
            if (os.path.isdir(my_p+"\\"+i)):#如果是目录就递归
                print "|",str(i).decode('GBK')
                printTree(my_p+"\\"+i, sNum+1)
            else:
                print str(i).decode('GBK')
                continue
        except:
            pass
printTree(myPath)



