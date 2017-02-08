#coding=utf-8
from time import sleep,ctime #导入俩个模块
import thread

loops = [3,2] #定义休眠时间
def loop(nloop,nsec,lock):
    print "开始 ",nloop,ctime()
    sleep(nsec)
    print "loop ",nloop,"done:",ctime()
    lock.release() #释放锁
def loop2():
    print "loop2程序开始 ",ctime()
    locks = []
    nloops = range(len(loops))
    for i in nloops:  #用于批量创建锁对象
        lock = thread.allocate() #创建锁对象
        lock.acquire() #尝试获取锁对象
        locks.append(lock)
    for i in nloops:
        thread.start_new_thread(loop,(i,loops[i],locks[i]))
    sleep(4)
    print "---all done---"

loop2()
