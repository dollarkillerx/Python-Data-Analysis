import requests

from easyutils import easyutil



targerUrl = "https://www.douban.com"
r = requests.get(targerUrl)
# print(r.content) # 二进制代码
# print(r.text) # 文本数据
# print(r.status_code) # http_code
# print(r.encoding) # 编码方式

print(easyutil.getRandUserAgent())
print(__file__)