#coding:utf-8

def fun_max(m):
    print m
    if  m > 0:
        print fun_max(m-1)
    return m

print fun_max(4)


def  funSum(start,end):
    if start == end:
        return start
    return start + funSum(start-1,end)
print funSum(100,1)

print 'lambda---------'

var = lambda x,y:x+y
var1 = var(1,5)
print var1