import requests
from bs4 import BeautifulSoup
import re

url = 'https://ssr1.scrape.center/'

a = requests.get(url, verify=False)
if a.status_code == 200:
    print("响应成功\n以下是电影信息\n")

soup = BeautifulSoup(a.content, "lxml")
all_p = soup.find_all("h2")
# for p in all_p:
#     print(p)

# 使用正则表达式匹配包含数字的 h2 标签
# 使用正则表达式匹配汉字
pattern = re.compile(r'[\u4e00-\u9fa5]+')

for h2 in all_p:
    chinese_only = ''.join(pattern.findall(h2.text))
    print(chinese_only)

'''
pattern.findall(h2.text) 这段代码使用正则表达式模式 pattern 匹配字符串 h2.text 中的所有符合条件的子字符串，并返回一个列表，列表中的每个元素都是一个符合条件的子字符串。

具体来说，正则表达式模式 pattern 匹配的是 Unicode 编码中所有汉字的范围，也就是 [\u4e00-\u9fa5]+。其中 \u4e00 表示汉字 Unicode 编码的开始位置，\u9fa5 表示汉字 Unicode 
编码的结束位置，[]+ 表示匹配一个或多个包含在 [] 中的字符。

在这个例子中，h2.text 是一个字符串，它包含了 h2 标签的文本内容。pattern.findall(h2.text) 会在 h2.text 中匹配所有符合 pattern 正则表达式模式的子字符串，
将它们保存在一个列表中并返回该列表。这个列表中的元素都是字符串，每个元素都包含了一个或多个汉字字符。

'''
