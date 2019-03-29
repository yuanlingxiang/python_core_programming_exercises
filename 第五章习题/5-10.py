#!usr/bin/env/python
# -*- coding:utf-8 -*-

"""写一对函数来进行华氏度到摄氏度的转换。转换公式为C = (F - 32) * (5 / 9)
应该在这个练习中使用真正的除法， 否则你会得到不正确的结果"""


def func1(F):
    C = (F -32) * 5 / 9
    return C


if __name__ == "__main__":
    F = float(raw_input('F='))
    print func1(F)