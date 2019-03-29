#!usr/bin/env/python
# -*- coding:utf-8 -*-

"""
(a) 使用循环和算术运算，求出 0－20 之间的所有偶数
(b) 同上，不过这次输出所有的奇数
(c) 综合 (a) 和 (b)， 请问辨别奇数和偶数的最简单的方法是什么？
(d) 使用(c)的成果，写一个函数，检测一个整数能否被另一个整数整除。 先要求用户输
入两个数，然后你的函数判断两者是否有整除关系，根据判断结果分别返回 True 和 False
"""
odd = []
oushu = []

for i in range(0, 21):
    if i % 2 == 0:
        oushu.append(i)
    else:
        odd.append(i)

print odd
print oushu

def func1(num1, num2):
    if num1>=num2:
        greater = num1
        smaller = num2
    else:
        greater = num1
        smaller = num2

    if greater % smaller == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    num1 = int(raw_input('num1='))
    num2 = int(raw_input('num2='))
    print func1(num1, num2)