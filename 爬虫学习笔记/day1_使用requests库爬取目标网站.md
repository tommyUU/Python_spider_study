```python
import requests
from bs4 import BeautifulSoup
import re
```

> 先导入`requests`和`BeautifulSoup`以及简单的数据清洗`re`正则表达式库


```python
spider = requests.get(url, verify=False)
if spider.status_code == 200:
    print("响应成功\n以下是电影信息\n")
else:
    print(spider.status_code)
```

> 这一步先实例化对象，使用变量`spider`来实例化
> 使用`if`条件分支来简单判断下响应的状态码。如果返回其他状态码，根据反馈进行'`debug


```python
soup = BeautifulSoup(spider.content, "lxml")
all_p = soup.find_all("h2")
```

> 这一步是创建一个对象，用来接受网页中`H2`标签的内容
> `BeautifulSoup`库能对`HTML`页面的属性进行抓取



```python
pattern = re.compile(r'[\u4e00-\u9fa5]+')

for h2 in all_p:
    chinese_only = ''.join(pattern.findall(h2.text))
    print(chinese_only)
```

> 使用正则表达式匹配包含汉字的 `h2` 标签
> `pattern.findall(h2.text)` 这段代码使用正则表达式模式 `pattern` 匹配字符串 `h2.text` 中的所有符合条件的子字符串，并返回一个列表，列表中的每个元素都是一个符合条件的子字符串。

> 具体来说，正则表达式模式 `pattern` 匹配的是 `Unicode` 编码中所有汉字的范围，也就是 `[\u4e00-\u9fa5]+`。其中 `\u4e00` 表示汉字 `Unicode` 编码的开始位置，`\u9fa5` 表示汉字 `Unicode` 编码的结束位置，`[]+` 表示匹配一个或多个包含在 `[] `中的字符。

> 在这段代码中，`h2.text` 是一个字符串，它包含了 `h2` 标签的文本内容。`pattern.findall(h2.text)` 会在 `h2.text` 中匹配所有符合 `pattern` 正则表达式模式的子字符串，
将它们保存在一个列表中并返回该列表。这个列表中的元素都是字符串，每个元素都包含了一个或多个汉字字符。
