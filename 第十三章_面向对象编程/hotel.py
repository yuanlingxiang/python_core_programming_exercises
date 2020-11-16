#! usr/bin/env/python
# -*- coding:utf-8 -*-


class HotelRoomCalc(object):
    """Hotel room rate caoculator"""
    def __init__(self, rt, sales=0.085, rm=0.1):
        'HotelRoomCalc default arguments'
        self.sales_tax = sales
        self.room_tax = rm
        self.room_rate = rt

    def calc_total(self, days=1):
        'Calculate total; default to daily rate'
        daily = round((self.room_rate*(1+self.room_tax + self.sales_tax)), 2)
        return float(days) * daily


if __name__ == '__main__':
    sfo = HotelRoomCalc(299)
    for i in range(1, 3):
        print sfo.calc_total(days=i)
    sea = HotelRoomCalc(189, 0.086, 0.058)
    print sea.calc_total(4)
    waswkday = HotelRoomCalc(119, 0.045, 0.02)
    print waswkday.calc_total(6)