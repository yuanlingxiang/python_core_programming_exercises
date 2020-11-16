#!usr/bin/env python
# -*- coding:utf-8 -*-

"""识别下列字符串： bat, bit, but, hat, hit, hut"""

import re

# 变异正则表达式为字节码
patten = re.compile(r'[bh][aiu]t')

if __name__ == '__main__':
    for strs in ['bat', 'bit', 'but', 'hat', 'hit', 'hut']:
        # group()输出匹配的对象
        print re.match(patten, strs).group()