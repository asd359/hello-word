#coding:utf-8

# def fun_max(m):
#     print m
#     if  m > 0:
#         print fun_max(m-1)
#     return m
#
# print fun_max(4)


# def  funSum(start,end):
#     if start == end:
#         return start
#     return start + funSum(start-1,end)
# print funSum(100,1)
#
# print 'lambda---------'
#
# myfun1 = [lambda x:x**2,lambda x:x**3,lambda x:x**4]
# print myfun1[2](2)
# print myfun1[0](2)
#
# print "循环一遍匿名函数"
# for var in myfun1:
#     print var(2)
#
# print '--------------'
#
# def func():
#     return 'func'
#
# def func1():
#     return 'func1'
#
# def func2():
#     return 'func2'
#
# mylist_func = [func,func1,func2]
#
# print mylist_func[0]()
# print mylist_func[1]()
# print mylist_func[2]()
#
# print  '\n传递可变对象'
# a= [1,2,3]
#
# def funa1(obj):#定义一个函数，传递一个可变对象，相当于传递一个值
#     obj = ['a','b','c']
#     print  '内部obj=',obj
# funa1(a)
# print '外部a：' ,a
#
# b = 1
# print id(b)
# def funa2(obj):
#     obj += 2
#     print id(obj)
#     print '内部obj：',obj
# funa2(b)
# print '外部变量b：',b


print 'clac--------------\n'
str = '1+39+4+6'
a = 1
b = 39
cout = {'+': a + b, '-': a - b, '*': a * b, '/': a / b}


import re
lsNum = re.split('\+|\-|\*|\/|\(|\)',str)
lsCout = re.split('1|2|3|4|5|6|7|8|9|0',str)

def delLs(list,delData):
    newLs = []
    for i in range(len(list)):
        if list[i] != delData:
            newLs.append(list[i])
    return newLs

lsNum = delLs(lsNum,"")
lsCout = delLs(lsCout,"")


print lsNum
print lsCout


def calc(num):
    # if num == len(lsCout) - 1:
    #     return
    if num == len(lsCout) - 1:
        return lsNum[-1]
    a = lsNum[num]
    b = lsNum[num+1]
    print  a , b
    print cout[lsCout[num]]
    lsNum[num + 1] = cout[lsCout[num]]

    calc(num+1)



calc(0)


# calc()


