# -*- coding:utf-8 -*-

"""
取一个任意小于1 美元的金额，然后计算可以换成最少多少枚硬币。硬币有1
美分，5 美分，10 美分，25 美分四种。1 美元等于100 美分。举例来说，0.76 美元换算结果
应该是 3 枚25 美分，1 枚1 美分。类似76 枚1 美分，2 枚25 美分+2 枚10 美分+1 枚5 美分+1
枚1 美分这样的结果都是不符合要求的
"""

num_list = []
coin_list = ['coin25', 'coin10', 'coin5', 'coin1']

def func1(money):
    coin_25, money = divmod(money, 25)
    coin_10, money = divmod(money, 10)
    coin_5, money = divmod(money, 5)
    coin_1, money = divmod(money, 1)
    return {'coin_25': coin_25, 'coin_10': coin_10, 'coin_5': coin_5, 'coin_1': coin_1}

def func2(money):
    for i in [25, 10, 5, 1]:
        num, money = divmod(money, i)
        num_list.append(num)
    return dict(zip(coin_list, num_list))

if __name__ == '__main__':
    print func1(76)
    print func2(76)