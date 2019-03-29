#! usr/bin/env python
# -*- coding:utf-8 -*-

'''
最大公约数和最小公倍数。请计算两个整数的最大公约数和最小公倍数
'''

def func1(num1, num2):
    '''
    :param num1:
    :param num2:
    :return:返回两个数的最大公约数
    '''
    smaller = num1 if num1 < num2 else num2
    hcf = 1
    for i in range(1, smaller+1):
        if num1 % i == 0 and num2 % i == 0:
            hcf = i
    return hcf

def func2(num1, num2):
    '''
    :param num1:
    :param num2:
    :return:返回两个数的最小公倍数
    '''
    greater = num1 if num1 > num2 else num2

    while True:
        if greater % num1 == 0 and greater % num2 == 0:
            return greater
        greater += 1


if __name__ == '__main__':
    print func1(54, 24)
    print func2(54, 24)