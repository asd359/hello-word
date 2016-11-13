#coding:utf-8
names = ['mk','top','tree','while']
print names

for name in names :
    print name

fib = [0,1]
'''
for i in range(40):
    fib.append(fib[-1]+fib[-2])

print  '%d'%(fib[39])
'''


'''
sum = 0
for i in range(0,51,2):
    sum+=i

print '1 - 50 中偶数的和是',sum

last = 1
sum = 1
print '第 1  2  3 个斐波那契数分别是 : 0 1 1 '
for i in range(4,41):
    t = sum
    sum += last
    last = t

    print '第',i,'个斐波那契数 ',sum
'''