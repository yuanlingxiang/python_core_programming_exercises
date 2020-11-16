#! usr/bin/env/python
# -*- coding:utf-8 -*-

import threading
from time import sleep, ctime

loops = [4, 2]


class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    # 实例可以像函数一样就行调用
    def __call__(self):
        # 调用函数
        self.func(*self.args)


def loop(nloop, nsec):
    print 'start loop %s at: %s' % (nloop, ctime())
    sleep(nsec)
    print 'loop %s done at: %s' % (nloop, ctime())

def main():
    print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))

    # 生成线程列表
    for i in nloops:
        # target中是类的实例
        # 创建线程，参数为类对象时，该类对象必须是可调用，所以类中要定义__call__
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        threads.append(t)

    for thread in threads:
        # 启动线程
        thread.start()

    for thread in threads:
        thread.join()

    print 'all done at:', ctime()


if __name__ == '__main__':
    main()