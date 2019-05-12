#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author    :AmosWu
# Date      :2019/1/26
# Features  : while-Calculate the sum of all odd numbers within 100

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
