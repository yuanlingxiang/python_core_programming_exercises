#! usr/bin/env python
# -*- coding:utf-8 -*-


my_seq = [123, 45.23, -6.2e8, 9999999L]


def convert(func, seq):
    return [func(each_num) for each_num in seq]


if __name__ == '__main__':
    for func in [int, long, float]:
        print convert(func, my_seq)