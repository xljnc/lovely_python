#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time      :2018/5/3 22:27
# @Author    :WuTian
# @Contact   :jsj0804wt@126.com
# @Desc

import time


def is_leap_year(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print "%s is leap year!" % year
    else:
        print "%s is not leap year!" % year


year = time.localtime()[0]
is_leap_year(year)
