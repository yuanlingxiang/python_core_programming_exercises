#!usr/bin/env/python
# -*-coding:utf-8 -*-

"""
键入2.15 节的文件显示的代码， 然后运行它， 看看能否在你的系统上正常工作，然后试
一下其它的输入文件。
"""

filename = raw_input('Enter file name: ')
fobj = open(filename, 'r')
for eachLine in fobj:
    print eachLine,

fobj.close()