#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author    :AmosWu
# Date      :2019/1/26
# Features  :利用递归函数调用方式，将所输入的字符，以相反顺序打印出来

def output(s,l):
    if l==0:
        return
    print (s[l-1])
    output(s,l-1)

s = input('Input a string:')
l = len(s)
output(s,l)