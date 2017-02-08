#coding:utf-8
import os

class get_file_tree:
    path_list = []
    def find_treee(self,my_p,sNum = 0):
        list = os.listdir(my_p)
        for i in list:
            for j in range(0,sNum):
                pass
                # print "- -",
            try:
                if (os.path.isdir(my_p+"\\"+i)):#如果是目录就递归
                    # print "|",str(i).decode('GBK')
                    self.find_treee(my_p+"\\"+i, sNum+1)
                    # find_treee(my_p+"\\"+i, sNum+1)
                else:
                    self.path_list.append(my_p+"\\"+i)
                    continue
            except:
                pass

#-------主文件-------------------------------------
class get_tree_list():
    def __init__(self):
        pass
    def get_tree_ls(self,myPath = "C:\\Users\\rick\\Desktop"):
        gt = get_file_tree()
        gt.find_treee(myPath)
        return gt.path_list#返回目录下的所有文件绝对地址

# a = get_tree_list()
# print str(a.get_tree_ls("C:\\Users\\rick\\Desktop")).__len__()



    # print get_tree_list()
    # print "get_file_tree.py"