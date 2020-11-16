#! usr/bin/env python
# -*- coding:utf-8 -8-

from operator import add, sub
from random import randint


ops = {'+': add, '-': sub}
maxtries = 2



def hello():
    """未指定return，返回None"""
    print 'hello world'


def foo():
    """通过return返回列表"""
    return ['xyz', 100000, -98.6]


def bar():
    """通过return返回三个对象，其实是一个元组"""
    return 'abc', [42, 'python'], 'Guido'


def bar1():
    print 'in foo()'

def foo1():
    print 'in bar()'
    bar1()

# @deco2
# @deco1
# def func(arg1, arg2):
#     pass
#
# def func1(arg1, arg2):
#     pass
#
# deco2(deco1(func1))

def tuple_varargs(arg1, arg2='defaultB', *the_rest):
    print 'arg1:', arg1
    print 'arg2:', arg2
    print 'the_rest:', the_rest
    for each_arg in the_rest:
        print each_arg




if __name__ == '__main__':
    tuple_varargs(1, 2, 3, 4)
    # atuple = bar()
    # x, y, z = bar()
    # (a, b, c) = bar()
    # print atuple
    # print x, y, z
    # print (a, b, c)
    # res = hello()
    # print res