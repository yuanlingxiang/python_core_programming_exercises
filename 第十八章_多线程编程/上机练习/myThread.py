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

    def getResult(self):
        return self.res

    def run(self):
        print 'starting %s at %s' % (self.name, ctime())
        self.res = self.func(*self.args)
        print '%s finished at:%s' % (self.name, ctime())