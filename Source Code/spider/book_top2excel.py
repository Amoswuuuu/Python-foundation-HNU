#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author    :AmosWu
# Date      :2019/2/11
# Features  : 汇华学院图书馆借阅排行榜TOP100 to Excel

from bs4 import BeautifulSoup
from urllib.request import urlopen
import xlwt

#__init__
url = 'http://222.30.226.2/top/top_lend.php'
html = urlopen(url)
h = html.read()
title_list = []
author_list = []
publish_list = []
callNum_list = []
collection_list = []
borrow_list = []
detailLink_list = []

soup = BeautifulSoup(h,'html.parser')

def get_book_top_list():

    try:
        for i in range(2,102):

            # 获取书名
            title_i = soup.select('#container > table > tr:nth-child(' + str(i) + ') > td')[1].text
            title_list.append(title_i)

            # 获取作者信息
            author_i = soup.select('#container > table > tr:nth-child(' + str(i) + ') > td')[2].text
            author_list.append(author_i)

            #获取书目详情链接
            detailLink_i ='http://222.30.226.2/' + soup.select('#container > table >  tr:nth-child(' + str(i) + ') > td > a')[0].get('href')[3:]
            detailLink_list.append(detailLink_i)

            # 获取出版信息
            publish_i = soup.select('#container > table > tr:nth-child(' + str(i) + ') > td')[3].text
            publish_list.append(publish_i)

            # 获取索书号
            callNum_i = soup.select('#container > table > tr:nth-child(' + str(i) + ') > td')[4].text
            callNum_list.append(callNum_i)

            # 获取馆藏
            collection_i = soup.select('#container > table > tr:nth-child(' + str(i) + ') > td')[5].text
            collection_list.append(collection_i)

            # 获取借阅册次
            borrow_i = soup.select('#container > table > tr:nth-child(' + str(i) + ') > td')[6].text
            borrow_list.append(borrow_i)
    except Exception:
        print('获取列表失败！')

def save2Excel():

    try:
        # 创建Excel表格并写入数据
        workbook = xlwt.Workbook()

        # 创建工作表worksheet,填入表名
        worksheet = workbook.add_sheet('list1')

        head = ['编号', '书名', '作者信息','出版信息','索书号','馆藏数','借阅册次','书目详情链接']  # 表头
        for h in range(len(head)):
            worksheet.write(0, h, head[h])

        i = 1
        # 在表中写入相应的数据
        for t in range(len(title_list)):
            worksheet.write(i, 0, i)
            worksheet.write(i, 1, title_list[i - 1])
            worksheet.write(i, 2, author_list[i - 1])
            worksheet.write(i, 3, publish_list[i - 1])
            worksheet.write(i, 4, callNum_list[i - 1])
            worksheet.write(i, 5, collection_list[i - 1])
            worksheet.write(i, 6, borrow_list[i - 1])
            worksheet.write(i, 7, detailLink_list[i - 1])
            i += 1

        # 保存表
        workbook.save('Hh_book_top_List.xls')
        print('写入Excel成功！')
    except Exception:
        print('保存失败！')

if __name__ == '__main__':
    get_book_top_list()
    save2Excel()






