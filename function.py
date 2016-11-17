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




