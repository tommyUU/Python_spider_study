# 五、爬虫库`urllib`【重要】

> * python提供操作`url`的模块

## 版本

> * python2
>
>   * urllib
>   * urllib2
> * python3
>
>   * urllib
>   * urllib3
>
>     * requets模块依赖

## urllib.request

> * `urllib.request.urlopen(url)`
> * `response:http.client.HTTPResponse` ![img.png](..%2Fimg%2Fimg.png)
> * `urllib.request.urlretrieve(url=,filename=)`

## urllib.parse

> * `urllib.parse.urlencode（）`
> * `urllib.parse.quote（）`
> * `urllib.parse.unquote（）`url解码

## URLError\HTTPError 	

> * 捕获异常
> * HTTP状态码

## 扩展

> * 解决SSL问题
>
>   * 导入SSL包-->`import ssl`
>   * 请求前设置https上下文

## 简单的请求

```python
from urllib.request import urlopen
# 发起网络请求
resp = urllopen('http://www.hao123.com')
assert resp.code == 200
print('请求成功')
# 保存请求的网页
with open('a.html', 'wb') as f:
	f.write(resp.read())
```