#! usr/bin/env/python
# -*- coding:utf-8 -*-

import threading
from time import sleep, ctime

loops = [4, 2]


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.args = args
        self.func = func

    def run(self):
        self.func(*self.args)

def loop(nloop, nsec):
    print 'start loop %s at: %s' % (nloop, ctime())
    sleep(nsec)
    print 'loop %s done at: %s' % (nloop, ctime())

def main():
    print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print 'all done at:', ctime()


if __name__ == '__main__':
    main()
