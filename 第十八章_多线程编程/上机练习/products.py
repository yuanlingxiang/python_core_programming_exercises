#! usr/bin/env/python
# -*- coding:utf_8 -*-

from random import randint
from time import sleep
from Queue import Queue
from myThread import MyThread


def writeQ(queue):
    print 'producting object for Q...'
    # 把对象'xxx'放到队列中
    queue.put('xxx', 1)
    print 'size now', queue.qsize()

def readQ(queue):
    # 从队列中获取一个对象
    queue.get(1)
    # queue.qsize()返回队列的大小
    print 'consumed object from Q... size now', queue.qsize()

def writer(queue, loops):
    for i in range(loops):
        # 把对象写入队列中
        writeQ(queue)
        sleep(randint(1, 3))

def reader(queue, loops):
    for i in range(loops):
        # 从队列中读取一个对象
        readQ(queue)
        sleep(randint(2, 5))

funcs= [writer, reader]
nfuncs = range(len(funcs))


def main():
    nloops = randint(2, 5)
    # 创建一个Queue对象，并指定大小为32
    q = Queue(32)

    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

    print 'all done'

if __name__ == '__main__':
    main()