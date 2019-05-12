#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author    :AmosWu
# Date      :2019/1/26
# Features  : function

def func(x):
    return x*x
def main():
    num = int(input("Please input a number:"))
    result = func(num)
    print(result)
if __name__ == '__main__':
    main()
