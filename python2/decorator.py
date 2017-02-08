#coding:utf-8
def func1(func):

    def func2():
        print 'this is %s is running'%func.__name__
        return func

    return func2()


@func1
def foo():
    print 'this is func:foo'
    # print 'this is %s is .running' %foo.__name__
foo()
