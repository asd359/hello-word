#coding:utf-8
# file_name = "foo1.txt"
# with open(file_name,'w') as file:
#     file.write('124845896')

class A(object):
    num = 1
class B(A):
    pass
class C(A):
    num = 2
class D(B,C):
    pass

d =D()
print d.num