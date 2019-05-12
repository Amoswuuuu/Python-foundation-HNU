#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author    :AmosWu
# Date      :2019/1/26
# Features  :利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

def main():
    s = int(input('Enter a number:'))
    if s >= 90:
        grade = 'A'
    elif s >= 60:
        grade = 'B'
    else:
        grade = 'C'
    print (grade)

if __name__ == '__main__':
    main()