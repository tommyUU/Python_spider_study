# requests库【重点】

> * `requests`库也是一个网络请求库，基于`urllib`和`urllib3`封装的便捷使用的网络请求库。


## 安装环境

> * `pip install requests`


## 核心函数

> * `requests.request()`
>
>   * 所有请求方法的基本方法
>   * `method:str` 指定请求方法，GET,POST,PUT,DELETE
>   * `url:str`请求的资源接口(API),在`RESTful`规范中即是URI(统一资源标签识符）
>   * `params:dict` 用于GET请求的查询参数(Query String params);
>   * `data:dict` 用于POST/PUT/DELETE请求的表单参数(Form Data)
>   * `json:dict` 用于上传json数据的参数，封装到body（请求体）中。请求头的Content-Type默认设置为application/.json
>   * `files:dict`,结构{'name': file-like-object | tuple},如果是tuple,则有三种情况：
>
>     * ('filename', file-like-object)
>     * ('filename', file-like-object,content_type)
>     * ('filename', file-like-object,content_type,custom-headers)
>     * 指定files用于上传文件，一般使用post请求，默认请求头的`Content-Type`为`multipart/form-data`类型。
>   * `neaders/cookies :dict`
>   * `proxies:dict`  设置代理
>   * `auth:tuple`  用于授权的用户名和口令，形式('username','pwd')
> * `requests.get()`
>
>   * 发起GET请求，查询数据
>   * `url`
>   * `params`
>   * `json`
>   * `headers`/`cookies`/`auth`
> * `requests.post()`
>
>   * 发起POST请求，上传/添加数据
>   * `url`
>   * `data`/`files`
>   * `json`
>   * `headers`/`cookies`/`auth`
> * `requests.put()`
>
>   * 发起PUT请求，修改或更新数据
> * `requests.patch()`   HTTP幂等性的问题，可能会出现重复处理，一般不使用
>
>   * HTTP PATCH 方法用于对资源进行局部更新，即只更新资源的部分内容。与其他一些 HTTP 方法（如 PUT）不同，PATCH 方法是非幂等的，因为多次发送相同的 PATCH 请求可能会导致不同的结果。
>
>     由于 PATCH 方法的非幂等性，重复发送相同的 PATCH 请求可能会导致重复处理，从而引发意外结果或副作用。因此，在设计和开发中，对于具有幂等性要求的操作，一般不会使用 PATCH 方法。
>
>     对于需要幂等性保证的操作，通常会选择使用 PUT 方法。PUT 方法用于完全替换或创建资源，因此多次发送相同的 PUT 请求不会产生副作用或引发重复处理的问题。
>
>     当需要对资源进行局部更新时，可以考虑使用其他的解决方案，如使用 POST 方法并在请求中指定需要更新的字段或使用自定义的 API 端点来实现局部更新的功能。
>
>     总结起来，虽然 `requests.patch()` 方法可以用于发送 PATCH 请求，但在具有幂等性要求的操作中，一般会选择`其他方法`来确保操作的可靠性和一致性，避免重复处理和意外结果的出现。
> * `requests.delete()`
>
>   * 发起DELETE请求，删除数据

#python函数的引用规范#

```python
# 声明函数时,参数名后的":类型"表示参数值的类型
# 在函数的()后的`-〉类型`表示函数返回的数据(结果)类型
def download(url: str) -> str:
    return 'hi,disen!'


r = download('')
print(r.upper())
```

### requests.Respose

```python
page = requests.get(url, params={'from': 'navigation'}, headers=UA)
page.headers
Out[7]: {'Server': 'Tengine', 'Date': 'Sun, 14 May 2023 15:30:13 GMT', 'Content-Type': 'text/html; charset=utf-8', 'Wcloud': 'cluster=hbg_web_hbghousepc;env=Product;group=ajk_house_list;host_name=tjtx176-81-36.58os.org;image_four_version=4.5.25.0', 'Hostname': 'hbg-web-hbghousepc-4-110449-qnhf8', 'Wcloud_cluster_group': 'ajk_house_list', 'Wcloud_imagefourversion': '4.5.25.0', 'Wcloud_wmonitor_cluster': 'hbg_web_hbghousepc', 'Fe-Trace-Id': '37f7a640-f26c-11ed-9401-75e74509302c', 'Accept-Ranges': 'none', 'Vary': 'Accept-Encoding', 'Set-Cookie': 'aQQ_ajkguid=7DC309A0-CD7E-49BE-94C1-630CFF9220F2; Path=/; Domain=.anjuke.com; Max-Age=31536000; Expires=Mon, 13 May 2024 15:30:13 GMT, sessid=7C3CC782-43FA-4678-A4B4-070B7E7B86CB; Path=/; Domain=.anjuke.com; Max-Age=31536000; Expires=Mon, 13 May 2024 15:30:13 GMT, ajk-appVersion=; Path=/; Domain=.anjuke.com; Max-Age=31536000; Expires=Mon, 13 May 2024 15:30:13 GMT, ctid=426; Path=/; Domain=.anjuke.com; Max-Age=31536000; Expires=Mon, 13 May 2024 15:30:13 GMT, fzq_h=6ddc83c7e9c811c6ace8d1172e174cb0_1684078212768_213364b377794d0489cfec284734faef_1949315390; Path=/; Domain=anjuke.com; Max-Age=691200; Expires=Mon, 22 May 2023 15:30:13 GMT', 'X-Webkit-CSP': 'frame-ancestors *.anjuke.com http://*.anjuke.com *.aifang.com http://*.aifang.com *.58ganji.com http://*.58ganji.com *.58.com http://*.58.com *.jikejia.cn http://*.jikejia.cn http://jikejia.cn yfyk.youfangyouke.com http://yfyk.youfangyouke.com *.58corp.com http://*.58corp.com *.qiaofangyun.com', 'X-Content-Security-Policy': 'frame-ancestors *.anjuke.com http://*.anjuke.com *.aifang.com http://*.aifang.com *.58ganji.com http://*.58ganji.com *.58.com http://*.58.com *.jikejia.cn http://*.jikejia.cn http://jikejia.cn yfyk.youfangyouke.com http://yfyk.youfangyouke.com *.58corp.com http://*.58corp.com *.qiaofangyun.com', 'Content-Security-Policy': 'frame-ancestors *.anjuke.com http://*.anjuke.com *.aifang.com http://*.aifang.com *.58ganji.com http://*.58ganji.com *.58.com http://*.58.com *.jikejia.cn http://*.jikejia.cn http://jikejia.cn yfyk.youfangyouke.com http://yfyk.youfangyouke.com *.58corp.com http://*.58corp.com *.qiaofangyun.com', 'X-Cache-Lookup': 'Cache Miss, Cache Miss, Cache Miss, Cache Miss', 'Content-Encoding': 'gzip', 'Content-Length': '70111', 'X-NWS-LOG-UUID': '8229083051448810126', 'Connection': 'keep-alive'}
page.cookies
Out[8]: <RequestsCookieJar[Cookie(version=0, name='aQQ_ajkguid', value='7DC309A0-CD7E-49BE-94C1-630CFF9220F2', port=None, port_specified=False, domain='.anjuke.com', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=False, expires=1715614212, discard=False, comment=None, comment_url=None, rest={}, rfc2109=False), Cookie(version=0, name='ajk-appVersion', value='', port=None, port_specified=False, domain='.anjuke.com', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=False, expires=1715614212, discard=False, comment=None, comment_url=None, rest={}, rfc2109=False), Cookie(version=0, name='ctid', value='426', port=None, port_specified=False, domain='.anjuke.com', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=False, expires=1715614212, discard=False, comment=None, comment_url=None, rest={}, rfc2109=False), Cookie(version=0, name='fzq_h', value='6ddc83c7e9c811c6ace8d1172e174cb0_1684078212768_213364b377794d0489cfec284734faef_1949315390', port=None, port_specified=False, domain='.anjuke.com', domain_specified=True, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=1684769412, discard=False, comment=None, comment_url=None, rest={}, rfc2109=False), Cookie(version=0, name='sessid', value='7C3CC782-43FA-4678-A4B4-070B7E7B86CB', port=None, port_specified=False, domain='.anjuke.com', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=False, expires=1715614212, discard=False, comment=None, comment_url=None, rest={}, rfc2109=False)]>
for i in page.cookies:
    print(i.name, i.value)
  
aQQ_ajkguid 7DC309A0-CD7E-49BE-94C1-630CFF9220F2
ajk-appVersion 
ctid 426
fzq_h 6ddc83c7e9c811c6ace8d1172e174cb0_1684078212768_213364b377794d0489cfec284734faef_1949315390
sessid 7C3CC782-43FA-4678-A4B4-070B7E7B86CB
```

以上的请求方法返回的对象类型是`Response`,对象常用的属性如下：

> * `status_code`响应状态码
> * `url`   请求的url
> * `headers:dict`  响应的头,相对于`urllib`的响应对象的`getheaders()`,但不包含`cookie`
> * `cookies` :可迭代的对象，元素是Cookie类对象(name,value,path)
> * `text`: 响应的文本信息
> * `content`: 响应的字节数据
> * `encoding` :响应数据的编码字符集，如`utf-8`,`gbk`,`gb2312`
> * `json()` :如果响应数据类型为`application/json`,则将响应的数据进行反序化成python的`list`或`dict`对象
>
>   * 扩展-`javascript`的序列化和反序列化
>
>     * `JSON.stringify(obj)`序列化
>     * `JSON.parse(text)`反序列化


```python
import requests
from requests import Response

url = 'https://cixi.anjuke.com/sale/?from=navigation'
UA = {'User-Agent':
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}


# page: Response = requests.get(url, params={'from': 'navigation'})
# 变量名后跟：类型，好处是编程时会自动提醒（提示）对象中的属性及方法

def download(url: str) -> str:
    page: Response = requests.get(url, params={'from': 'navigation'}, headers=UA)
    if page.status_code == 200:
        print("响应完成")
        return page.text
    return '下载失败'


result = download(url)
print(result)

```