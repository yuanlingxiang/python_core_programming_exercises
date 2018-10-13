#!usr/bin/env/python
# -*-coding:utf-8 -*-

"""python核心编程第五章习题"""

import math
import sys
import random

def func1():
    """整型和长整型的区别：
    现在没有明显的区别,显示显示为长整型只需要值后面加l
    """
    a = 1l
    b = 1
    return a, b


def func2():
    """返回两个数的剩积"""
    try:
        a = input('a=')
        b = input('b=')
        return a * b
    except ValueError, e:
        print '输入的值类型错误：', str(e)


def func3():
    """判断成绩的等级"""
    try:
        score = input('score=')
    except ValueError, e:
        print '输入的值类型错误：', str(e)
    else:
        print score
        if 100 >= score >= 90:
            return 'A'
        elif 90 > score >= 80:
            return 'B'
        elif 80 >= score >= 70:
            return 'C'
        elif 70 >= score >= 60:
            return 'D'
        else:
            return 'E'


def func4():
    """判断一个数是否是闰年"""
    try:
        year = input('year=')
        if (year % 4 == 0) and (year % 100 != 0):
            return u'是闰年！'
        elif (year % 4 == 0) and (year % 100 == 0):
            return u'是闰年！'
        else:
            return u'不是闰年'
    except ValueError, e:
        print u'输入值类型错误', str(e)


def func5():
    """计算小于1元的钱能换算成硬币数量"""
    money = int(input('money=') * 100)

    coin_25_nums = divmod(money, 25)
    coin_10_nums = divmod(coin_25_nums[1], 10)
    coin_5_nums = divmod(coin_10_nums[1], 5)
    return 'coin_25_nums',coin_25_nums[0],'coin_10_nums', coin_10_nums[0],\
                'coin_5_nums',coin_5_nums[0], 'coin_1_nums', coin_5_nums[1]


def func6():
    """二元计算"""
    expresion = raw_input(':')
    return eval(expresion)


def func7(rate=0.03):
    """营业税"""
    price = input('price=') * rate
    return price


class Shape(object):
    def area(self, lenth, width):
        return lenth * width

    def volume(self, lenth, width, height):
        return lenth * width * height

    def circle_area(self, r):
        return math.pi * pow(r, 2)

    def ball_volumne(self, r):
        return (4/3.0) * math.pi * pow(r, 3)


def func9():
    """数字格式问题
    数字前面加0表示该数字是八进制"""
    print 17 + 32
    print 017+ 32
    print 017 + 032
    print 56l + 78l


def func10():
    """转换"""
    F = input('F=')
    return (F - 32) * (5 / (9 *1.0))


def func11():
    """取余"""
    odd_list = []
    even_list = []
    for i in range(21):
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    print odd_list, even_list

    num1 = input('num1=')
    num2 = input('num2=')

    greater = num1 if num1>num2 else num2
    smaller = num1 if num1<num2 else num2

    if greater % smaller == 0:
        return True
    else:
        return False


def func12():
    """确定系统整数，浮点数范围"""
    return sys.maxint, sys.float_info


def func13():
    """将小时转换为分钟"""
    time1 = raw_input("小时和分钟用':'隔开， time=").split(':')
    return int(time1[0]) * 60 + int(time1[1])


def func14(rate=0.033):
    """银行利息"""
    deposit = input('deposet=')

    for i in range(365):
        deposit = deposit + (deposit * rate) / 365
    return deposit


def func15():
    """最大公约数，最小公倍数"""
    num1 = input('num1=')
    num2 = input('num2=')

    greater = num1 if num1 > num2 else num2
    smaller = num1 if num1 < num2 else num2

    for i in range(2, smaller + 1):
        if num1 % i == 0 and num2 % i == 0:
            common_divisor = i

    while True:
        if greater % num1 == 0 and greater % num2 == 0:
            common_multiple = greater
            break
        greater += 1

    return 'common_divisor: %d, common_multiple: %d' % (common_divisor, common_multiple)


def func16():
    """家庭财务"""
    balance = input('Enter opening balance:')
    payment = input('Enter opening payment:')

    print 'Amount Remaining'
    print '%-7s%-7s%-10s' % ('Pymt#', 'Paid', 'Balance')
    print '-'*5, '-'*6, '-'*9
    month = 0
    print '%-6s$%-7s$%-10s' % (month, payment, balance)
    while True:
        month += 1
        if (balance-payment) > 0:
            balance -= payment
            print '%-6s$%-7s$%-10s' % (month, payment, balance)
        else:
            payment = balance
            balance = 0
            print '%-6s$%-7s$%-10s' % (month, payment, balance)
            break


def func17():
    """随机数"""

    list1 = [j for i in range(random.randint(1, 101)) for j in range(random.randrange(231))]
    list2 = []
    for i in range(random.randint(1, 101)):
        list2.append(random.choice(list1))

    return sorted(list2)




























