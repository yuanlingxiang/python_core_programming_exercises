# -*- coding:utf-8 -*-

"""
判断给定年份是否是闰年
1992，1996 和2000 年是闰年，但1967 和1900 则不是闰年
"""

def is_yeap_year(year):
    if year%4==0 and year%100==0:
        return 'yeap year'
    elif year%4 == 0 and year%100!=0:
        return 'yeap year'
    else:
        return 'not yeap year'


if __name__ == '__main__':
    year = int(raw_input('year:'))
    print is_yeap_year(year)