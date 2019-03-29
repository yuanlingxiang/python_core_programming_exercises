# -*- coding:utf-8 -*-

"""
计算面积和体积：
(a) 正方形 和 立方体
(b) 圆 和 球
"""

import math

def square_area(width):
    return width * width

def circle_area(r):
    return math.pi * (r ** 2)

def cube_volume(long, width, high):
    return long * width * high

def ball_volume(r):
    return (4/3.0) * math.pi * pow(r, 3)

if __name__ == "__main__":
    print square_area(5)
    print circle_area(5)
    print cube_volume(5, 5, 5)
    print ball_volume(5)




