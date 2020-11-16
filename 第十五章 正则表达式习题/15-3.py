#!usr/bin/env python
# -*- coding:utf-8 -*-

"""匹配用逗号和一个空格分割开的一个单词和一个字母"""

import re

# 变异正则表达式为字节码
patten = re.compile(',|\s+')

if __name__ == '__main__':
    name_list = ['zhang,     san', 'zhang   san']
    for name in name_list:
        name = re.split(patten, name)
        # 过滤掉元素为''的对象
        for element in name:
            if element == '':
                name.remove(element)
        print name




