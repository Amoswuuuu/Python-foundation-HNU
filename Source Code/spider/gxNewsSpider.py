#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author    :AmosWu
# Date      :2019/1/27
# Features  : 工学部首页新闻列表自定义页数爬虫
from bs4 import BeautifulSoup #用于解析网页
import xlwt
import requests

url = 'http://222.30.226.10/xxgcxb/index.php?mods=cate&rootid=1&page=1&list='
title_list = []
date_list = []
link_list = []

def getNewsList(depth):
    try:
        for i in range(depth):
            x = i*10
            link = url + str(x)
            #生成爬取的链接队列
            response_i = requests.get(link)
            html_i = response_i.text
            print('爬取的链接' + str(i) + '为：' + link)
            soup_i = BeautifulSoup(html_i,'html.parser')                    #将网页所有代码以文档形式煲成汤
            title = soup_i.select('#realContentId > div.contentMain > ul > li > a')    #筛选所有与新闻标题相关的a标签
            date = soup_i.select('#realContentId > div.contentMain > ul > li > span')  #筛选所有与发布时间相关的span标签
        #获取新闻标题和链接
            for titles in title:
               t = titles.get_text()
               l = 'http://222.30.226.10/xxgcxb/' + titles.get('href')
               if t != []:
                   title_list.append(t)
               if l != []:
                  link_list.append(l)
            #获取发布时间
            for dates in date:
              d = '20' + dates.get_text()
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
        workbook.save('GX_Index_NewsList.xls')
        print('写入Excel成功！')
    except Exception:
        print('写入Excel失败！')

if __name__ == '__main__':
    depth = 1
    num = input('请输入你要爬取的深度，最大深度为48：')
    depth = int(num)
    getNewsList(depth)
    savaToExcle()
















