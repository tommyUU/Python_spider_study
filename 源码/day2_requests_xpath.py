"""
基于requests库作用现网络请求
基于xpath实现数据提取
"""
import requests
from lxml import etree


class RequestError(Exception):
    """
    请求异常
    """
    pass


class ParseError(Exception):
    """
    解析异常
    """
    pass


def get(url):
    resp = requests.get(url, verify=False)
    if resp.status_code == 200:
        parse(resp.text)
    else:
        raise Exception('请求失败')


def parse(html):
    """
    使用xpath解析
    """
    root = etree.HTML(html)  # xpath的元素对象
    divs = root.xpath('//div[@class="el-row"]')  # List中的可迭代的很多的元素
    for div in divs:
        cover_url = div.xpath('..//img[@class="cover"]')  # list['str']  extract从元素中提取内容（属性值）
        title = div.xpath('.//div/a/h2[@class="m-b-sm"]')

        print(cover_url, title)


if __name__ == '__main__':
    get('https://ssr1.scrape.center/')