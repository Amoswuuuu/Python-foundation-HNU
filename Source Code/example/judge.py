#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author    :AmosWu
# Date      :2019/1/26
# Features  : Judge

age = int(input("Please your age:"))
if age >= 18:
    print("adult")
elif age >= 6:
    print("teenager")
else:
    print("kid")
