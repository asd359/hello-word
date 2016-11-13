#coding=utf-8
fib = [0,1]
for i in range(38):
    fib.append(fib[-1] + fib[-2])

print fib

'''双层循环'''
'''s输出九九乘法表'''

for i in range(1,10):
    for j in range(1,10):
        if j > i :
            break
        print "%d * %d = %d "%(i,j,i*j),
    print ""


'''Dict'''
print '\nDict'
import random

print random.random()

d = {}
print d
d['rick'] = 99
d['sun'] = 89
d['菠萝'] = random.uniform(1,100)
d['cc'] = 56
d['cp'] = 56
d['euler'] = 73
print  d
# d.popitem()
# print d
# d.pop('sun')
# print set(0.987634)





money = int(raw_input('\n\n输入准备花多少钱￥：'))

print '预算是', money, '￥\n', '欢迎shopping！！'


# name = ['菠萝', '芒果', '栗子', '椰子', '奇果',
#         '芭乐', '榴莲', '香蕉', '甘蔗', '莲子',
#         '石榴', '核桃', '拐枣']
name = ['菠萝', '芒果', '栗子', '椰子']


# 所有字典均为字符类型
# shopList{商品序号，价格}
shopList = {}
# 我的清单{商品序号，数量}
mylist = {}
goexit = 0
count = 0

# 初始化商品单//////////////////////////////////////////////
for i in range(name.__len__()):
    shopList[str(i)] = str(int(random.uniform(money / 5, 2 * money))+1)

while not(goexit):

    # 计算总价
    count = 0
    for i in mylist:
        count += int(shopList[i]) * int(mylist[i])

    # 查看余额状态，删除商品
    if money - count < 0:
        print '我的清单：'

        for i in mylist:
            print name[int(i)], '  *', mylist[i], ' 序号', i
        print '总价：',count

        t = raw_input('————预算不足——————\n'
                      '不买了输入 -1,删除商品输入商品编号\n')

        if t == '-1':
            break

        if t in mylist:
            mylist.pop(t)
        else:
            print '购物篮无此商品'
        continue


    inNum = raw_input('-1 结账，-2 商品单,-3 查看预算使用'
                      '\n添加商品直接按序号\n')

    #  查看预算使用情况
    if inNum == '-3':
        print '预算还剩：',money-count
    # 打印商品清单
    if inNum == '-2':
        print '商品    价格    序号'
        for i in range(name.__len__()):
             # print name[i]
             print "%s    %s    %d"%(name[i],shopList[str(i)],i)
        continue

    # 退出
    if inNum == '-1':
        goexit = 1
        continue

    # 添加购物

    if inNum in shopList:
        if inNum in  mylist:
            mylist[inNum] = str(int(mylist[inNum])+1)
        else:
            mylist[inNum] = '1'




if goexit:
    print '购买清单'
    for i in mylist:
        print name[int(i)], '  *', mylist[i], '  单价', shopList[i]
    print '总价：', count
    print '预算余额：',money-count
else:
    print '欢迎下次光临'
