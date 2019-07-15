import re

a = 'C|C++|Java|C#|Python|Golang'

result = re.findall('(Python)',a) # 规则,数据
print(result)

a = "C0C++7Java8Cs848PSD778ASD"

# 目标: 提取a中所有数字
result = re.findall("(\d)",a)
print(result)

data = "abc, acc, adc, aec, afc, ahsc"
# 目标: 获取中间的
result = re.findall('a([\w])c',data)
print(result)

data = 'python 1111java445php24848golang'
# 目标: 获取语言名称
result = re.findall('[a-z]{3,6}',data)
print(result)

data = 'python 1111java445php24848golang'
# 目标: 获取python
result = re.findall('p[\w\W]+?n',data)
print(result)

''' 
# 数量词
    * 匹配0次或者无限次
    + 匹配1次或者无限次
    ? 匹配0次或者1次 
'''

import requests

# requests 学习
baseUrl = 'https://www.douban.com/search'

# 构建get 请求
dict = {'q':'golang'}
r = requests.get(baseUrl,params= dict)
print(r.url)
print(r.status_code)

# 构建post 请求
data = {'user':'dollarkiller','password':'xxxxxxx'}
r = requests.post(baseUrl,data = data)
print(r.status_code)