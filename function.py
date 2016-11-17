#coding:utf-8

def helloFun(name,age):
    print "name:%s,age:%s"%(name,age)

helloFun(age=99,name="rick")

def funDefault(userAge='1',sex = 'male',userName = 'rick'):
    print '年龄：',userAge,\
        ' 性别:',sex\
        ,'名字：',userName

funDefault()
#helloFun()


def fun_arg(*arg,**arg1):
    print arg,'  ',type(arg)
    print arg1,' ',type(arg1)

fun_arg('1','trust','belivev',a=9,b='g',sure='yes')


print  '全局变量，局部变量'
a = 10
def fun5():
    a = 7
    print '全局危10，局部为7  .',a

fun5()
print a

def sum(startInt,endInt):
    s = 0
    for i in  range(startInt,endInt+1):
        s += i
    return s


print '\n\n1 - 100 和为：',sum(1,3)


