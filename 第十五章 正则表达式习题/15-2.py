#!usr/bin/env python
# -*- coding:utf-8 -*-

"""匹配用空格分割任意一对单词"""

import re

# 变异正则表达式为字节码
patten = re.compile(r'\s+')

if __name__ == '__main__':
    name = 'zhang san'
    print re.split(patten, name)