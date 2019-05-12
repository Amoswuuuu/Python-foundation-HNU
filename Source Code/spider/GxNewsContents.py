#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author    :AmosWu
# Date      :2019/2/4
# Features  : 新闻详情爬取

from bs4 import BeautifulSoup #用于解析网页
import requests
import re

url = 'http://222.30.226.10/xxgcxb/index.php?mods=showid&id=1332'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html,"html.parser")
title = soup.select('#realContentId > div.contentMain > h1')
date = soup.select('#realContentId > div.contentMain > h2')[0].text
datee = re.search(r"(\d{4}-\d{1,2}-\d{1,2})",date)
contents = soup.select('#column > p > span')
see = soup.select('#hits')
d = '发布时间：' + datee[0] + see[0].text
contents_list = []
for i in contents:
    s = i.get_text()
    contents_list.append(s)
    # print(i.get_text())
#生成TXT文件名
txtName = str(title[0].text) + '.txt'
print('生成 "' + txtName + '" 成功！')
#将以上数据写入TXT
f = open(txtName,'w')
f.write(title[0].text + '\n\n')
f.write(d + '\n\n\n')
for i in contents_list:
    f.write('   ' + i + '\n')
f.close()
print('写入' + txtName + '成功！\n')


