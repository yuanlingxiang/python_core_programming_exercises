# -*- coding:utf-8 -*-

"""
随意取一个商品金额，然后根据当地营业税额度计算应该交纳的营业税
"""

def func(sale, rate=0.03):
    return sale * rate

if __name__ == "__main__":
    print func(1000)

