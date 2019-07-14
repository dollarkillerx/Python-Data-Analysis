# -*- coding: UTF-8 -*-
import sys
import urllib
import urllib.request
# from bs4 import BeautifulSoup
if (len(sys.argv) < 2):
    print("\n",'请输入正确的URL地址!')
    exit(0)

# 命令行url获取
url = sys.argv[1]
print(url)

baidu = "Mozilla/5.0 (compatible; Baiduspider/2.0;+http://www.baidu.com/search/spider.html）"

# url请求
req = urllib.request.Request(url,headers={'User-Agent':baidu})
html = urllib.request.urlopen(req)

# 解析获取html
soup = BeautifulSoup(html,"html.parser")
print(soup.html)