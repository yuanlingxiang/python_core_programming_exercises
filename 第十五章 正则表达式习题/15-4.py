#!usr/bin/env python
# -*- coding:utf-8 -*-

"""匹配所有合法的python标识符"""

import re

# 变异正则表达式为字节码
patten1 = re.compile(r'[_a-zA-Z]\w+')
patten2 = re.compile(r'[_a-zA-Z]')

if __name__ == '__main__':
    var_list = ['abc', '_abc', '1ab', '1', 'a', '_', 'a b', '!', 'a!', u'哈哈', u'a哈哈']
    for var in var_list:
        if len(var) > 1:
            if re.match(patten1, var):
                print var
        else:
            if re.match(patten2, var):
                print var
