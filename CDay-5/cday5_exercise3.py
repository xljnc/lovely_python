#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time      :2018/5/5 20:23
# @Author    :WuTian
# @Contact   :jsj0804wt@126.com
# @Desc judeg is the number is prime

def is_primes(num):
    if num < 2:
        print("%d is not prime." % num)
        return
    i = 2
    while i * i <= num:
        if (num % i == 0):
            print("%d is not prime." % num)
            return
        i += 1
    print("%d is prime." % num)


for x in range(101):
    is_primes(x)
