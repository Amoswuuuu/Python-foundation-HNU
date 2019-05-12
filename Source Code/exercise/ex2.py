#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author    :AmosWu
# Date      :2019/1/26
# Features  : Print all daffodils number on the screen

for i in range(100,1000):
    a = i%10
    b = int(i/100)
    c = (int(i/10))%10
    if i == a**3+b**3+c**3:
        print('%d'%i)