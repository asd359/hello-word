#coding:utf-8
def func1(num1):
    def func2(num2):
        print 'num2 : ',num2
        return num2
    def func3(num3):
        print 'num3: ',num3
        return num3

    print num1
    b = [func2,func3]
    return b
res = func1(33)
print res[0](9)





