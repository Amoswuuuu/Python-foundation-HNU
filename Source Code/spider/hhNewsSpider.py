#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author    :AmosWu
# Date      :2019/1/27
# Features  : 汇华学院新闻列表爬虫

from urllib.request import urlopen #用于抓取网页
from bs4 import BeautifulSoup #用于解析网页
import xlwt

url = 'http://222.30.226.10/news/index.php?mods-cate_id-2.html'
html = urlopen(url)
contents = html.read()
title_list = []
date_list = []
link_list = []

def getNewsList():
    soup = BeautifulSoup(contents,'html.parser')                    #将网页所有代码以文档形式煲成汤
    title = soup.select('#ileft > div.ggcontent3 > ul > li > a')    #筛选所有与新闻标题相关的a标签
    date = soup.select('#ileft > div.ggcontent3 > ul > li > span')  #筛选所有与发布时间相关的span标签

    try:
        #获取新闻标题和链接
        for titles in title:
           t = titles.get_text()
           l = 'http://222.30.226.10/news/' + titles.get('href')
           if t != []:
               title_list.append(t)
           if l != []:
              link_list.append(l)
        #获取发布时间
        for dates in date:
          d = dates.get_text()
          if d != []:
            date_list.append(d)
    except Exception:
        print('获取新闻列表失败！')
def savaToExcle():
    try:
        # 创建Excel表格并写入数据
        workbook = xlwt.Workbook()

        # 创建工作表worksheet,填入表名
        worksheet = workbook.add_sheet('list1')

        head = ['发布时间', '新闻标题', '详情链接']  # 表头
        for h in range(len(head)):
            worksheet.write(0, h, head[h])

        i = 1
        # 在表中写入相应的数据
        for t in range(len(date_list)):
            worksheet.write(i, 0, date_list[i - 1])
            worksheet.write(i, 1, title_list[i - 1])
            worksheet.write(i, 2, link_list[i - 1])
            i += 1

        # 保存表
        workbook.save('HH_Index_NewsList.xls')
        # workbook.save (r"C:\Users\WU\Desktop\HH_Index_NewsList.xls")
        print('写入Excel成功！')
    except Exception:
        print('写入Excel失败！')

if __name__ == '__main__':
    getNewsList()
    savaToExcle()

















