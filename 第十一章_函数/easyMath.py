#! usr/bin/env python
# -*- coding:utf-8 -*-

from operator import add, sub
from random import randint, choice

max_tries = 2
ops = {'+': add, '-': sub}


def droprob():
    op = choice('-+')
    nums = [randint(1, 10) for i in range(2)]
    nums.sort(reverse=True)
    ans = ops[op](*nums)
    pr = '%s %s %s = ' % (nums[0], op, nums[1])
    opps = 0
    while True:
        try:
            if int(raw_input(pr)) == ans:
                print '对了，对了'
                break
            if opps == max_tries:
                print '正确的答案\n%s %s' % (pr, ans)
            else:
                print '不对， 不对， 再回答一次：'
                opps += 1
        except (KeyboardInterrupt, EOFError, ValueError), e:
            print '输入错误， 再次输入'


def main():
    while True:
        droprob()
        try:
            opt = raw_3input('再来一次[y]').lower()
            if opt[0] == 'n':
                print '程序正确退出'
                break
        except (KeyboardInterrupt, EOFError):
            print '异常情况，退出程序'
            break


if __name__ == '__main__':
    main()