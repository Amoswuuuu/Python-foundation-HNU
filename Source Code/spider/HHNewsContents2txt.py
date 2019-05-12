#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author    :AmosWu
# Date      :2019/2/10
# Features  : 汇华学院官网新闻详情存入txt文件 *100

from urllib.request import urlopen #用于抓取网页
from bs4 import BeautifulSoup #用于解析网页
import re

# __init__
url_list = ['http://222.30.226.10/news/index.php?mods-cnews_id-10178.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10177.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10172.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10171.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10170.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10169.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10168.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10167.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10166.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10159.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10158.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10156.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10153.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10152.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10151.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10150.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10149.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10146.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10145.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10144.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10143.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10141.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10140.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10139.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10138.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10137.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10136.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10135.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10134.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10133.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10132.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10131.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10130.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10129.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10127.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10126.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10124.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10123.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10119.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10118.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10116.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10115.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10110.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10109.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10108.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10106.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10105.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10104.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10103.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10102.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10101.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10100.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10098.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10094.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10093.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10092.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10091.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10090.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10089.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10088.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10087.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10086.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10085.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10084.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10083.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10082.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10081.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10080.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10079.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10078.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10077.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10076.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10073.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10072.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10070.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10068.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10067.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10066.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10065.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10064.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10063.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10062.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10061.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10060.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10059.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10058.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10057.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10056.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10053.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10052.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10051.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10050.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10047.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10046.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10045.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10043.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10042.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10037.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10036.html', 'http://222.30.226.10/news/index.php?mods-cnews_id-10035.html']


def NewsContentsList2Txt(length):
    try:
        for num in range(length):

            html = urlopen(url_list[num])
            contents = html.read()
            soup = BeautifulSoup(contents,'html.parser')
            title = soup.select('#ileft > div.title')
            see = soup.select('#ileft > div.time')
            content = soup.select('#ileft > div:nth-child(4) > p')

            # 获取新闻标题
            t_i = title[0].text

            #获取发布时间
            s_i = see[0].text
            result_i = re.findall(r'\d+', s_i)

            dateTime_i = result_i[0] + '-' + result_i[1] + '-' + result_i[2] + ' ' + result_i[3] + ':' + result_i[4] + ':' + result_i[5]
            # 获取阅读数
            sees_i = result_i[-1]

            # 获取正文
            cont_i = ''
            for i in content:
                c = i.text
                cont_i = cont_i + '    ' + c + '\n'

            # 生成TXT文件名
            txtName = '【' + str(num + 1) + '】' + str(t_i) + '.txt'
            # 将数据写入TXT
            f = open('f:\py\HHnews\ ' + txtName, 'w', encoding='utf-8')
            f.write(t_i + '\n\n')
            f.write('发布时间：' + dateTime_i + ' ' + '阅读数：' + sees_i + '\n')
            f.write('新闻链接：' + url_list[num] + '\n\n')
            f.write('    ' + str.format(cont_i) + '\n')     #格式化字符串写入txt
            print(url_list[num])
            print('写入' + txtName + '成功！\n')

    except Exception :
        print('获取新闻详情列表失败！')

if __name__ == '__main__':
    num = input('请输入要爬取的文章数：')
    length = int(num)
    NewsContentsList2Txt(length)


