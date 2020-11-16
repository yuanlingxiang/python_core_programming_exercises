#! usr/bin/env/python
# -*- coding:utf-8 -*-

import thread

from time import sleep, ctime

loops = [4, 2]


def loop(nloop, nsec, lock):
    print 'start loop %s at: %s' % (nloop, ctime())
    sleep(nsec)
    print 'loop %s done at %s' % (nloop, ctime())
    # 释放锁
    lock.release()


def main():
    print 'starting at :', ctime()
    locks = []
    nloops = range(len(loops))
    # 第一步：创建锁列表
    for i in nloops:
        # 分配锁
        lock = thread.allocate_lock()
        # 获取锁
        lock.acquire()
        # 生成锁列表
        locks.append(lock)

    # 第二步：创建并启动线程
    for i in nloops:
        # 创建线程并加上锁，然后运行
        thread.start_new_thread(loop, (i, loops[i], locks[i]))

    # 第三步：判定所有的线程是否都分配过锁
    for i in nloops:
        # 判断所有的线程是否都有锁
        while locks[i].locked():
            pass

    print 'all done at:', ctime()


if __name__ == '__main__':
    main()