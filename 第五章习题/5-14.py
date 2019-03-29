#! usr/bin/env python
# -*- coding:utf-8 -*-

'''
写一个函数，以定期存款利率为参数， 假定该账户每日计算复利，请计
算并返回年回报率。
'''

def func1(money, rate=0.058):
    for i in range(365*5):
        money = money + (money * rate)/365
    return money

if __name__ == '__main__':
    print func1(400000)