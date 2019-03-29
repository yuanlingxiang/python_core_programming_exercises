# -*- coding:utf-8 -*-

"""
写一个计算器程序 你的代码可以接受这样的表达式，两个操作数加一个运算符：
N1 运算符 N2. 其中 N1 和 N2 为整数或浮点数，运算符可以是+, -, *, /, %, ** 分别表示
加法，减法， 乘法， 整数除，取余和幂运算。计算这个表达式的结果，然后显示出来。提示：
可以使用字符串方法 split(),但不可以使用内建函数 eval().
"""
import operator

sysmbol = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div,
           "%": operator.mod, "**": operator.pow}
def func1(num1, sysm, num2):
    return sysmbol.get(sysm)(float(num1), float(num2))

if __name__ == '__main__':
    num1, sysm, num2 = raw_input(":").split()
    print func1(num1, sysm, num2)