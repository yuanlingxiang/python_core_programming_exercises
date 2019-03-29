# -*- coding:utf-8 -*-

"""
\标准类型运算符. 写一段脚本，输入一个测验成绩，根据下面的标准，输出他的评分
成绩（A-F）。
A: 90–100
B: 80–89
C: 70–79
D: 60–69
F: <60
"""

import random

def func1(score):
    if 90<=score<=100:
        print 'A'
    elif 80<=score<=89:
        print 'B'
    elif 70<=score<=79:
        print 'C'
    elif 60<=score<=69:
        print 'D'
    elif score<60:
        print 'F'
    else:
        print u'input error'

def func2(score):
    if score in range(90, 101):
        return 'A'
    elif score in range(80, 90):
        return 'B'
    elif score in range(70, 80):
        return 'C'
    elif score in range(60, 70):
        return 'D'
    else:
        raise ValueError(u'输入错误')


if __name__ == '__main__':
    score = int(raw_input('score='))
    func1(score)
    print func2(score)