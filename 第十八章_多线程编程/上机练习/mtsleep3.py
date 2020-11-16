#! usr/bin/env/python
# -*- coding:utf-8 -*-

import threading
from time import sleep, ctime

loops = [4, 2]


def loop(nloop, nsec):
    print 'start loop %s at: %s' % (nloop, ctime())
    sleep(nsec)
    print 'loop %s done at: %s' % (nloop, ctime())


def main():
    print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))

    # 第一步： 创建线程列表
    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    # 第二步： 启动所有的线程
    for thread in threads:
        thread.start()
        print '线程的名字：', thread.getName()

    # 第三步： 等待所有的线程执行完成，在执行主线程
    for thread in threads:
        thread.join()

    print 'all done at:', ctime()


if __name__ == '__main__':
    main()
