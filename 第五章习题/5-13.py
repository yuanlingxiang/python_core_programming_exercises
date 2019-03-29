#!usr/bin/env/python
# -*- coding:utf-8 -*-

"""写一个函数把由小时和分钟表示的时间转换为只用分钟表示的时间"""

import re

def func1(time):
    pattern = re.compile('[:\s+]')
    time = re.split(pattern, time)
    return int(time[0])*60 + int(time[1])


if __name__ == "__main__":
    time = raw_input('time=')
    print func1(time)

