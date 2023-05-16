import uuid
import requests
import pymysql
from lxml import etree
from utils import header


def save_to_mysql(item, connection):
    """
    保存数据到 MySQL
    :param item: 要保存的数据项（字典）
    :param connection: pymysql 连接对象
    """
    try:
        with connection.cursor() as cursor:
            # 确保所有字段都是字符串类型且不为空
            for field in ['name', 'author', 'content', 'tags']:
                if not item[field]:
                    item[field] = '\n'  # 替换为适当地默认值
                elif isinstance(item[field], list):  # 如果字段是列表，则将其转换为字符串
                    item[field] = ' '.join(item[field])

            # 执行插入语句
            sql = "INSERT INTO `gushi` (`id`, `name`, `author`, `content`, `tags`) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (item['id'], item['name'], item['author'], item['content'], item['tags']))

        # 提交事务以保存更改
        connection.commit()
    except Exception as e:
        print(e)


def parse(html, connection):
    """
    解析 HTML 页面
    :param html: 要解析的 HTML 内容
    :param connection: pymysql 连接对象
    """
    root = etree.HTML(html)  # 获取html的根元素
    divs = root.xpath('//div[@class="left"]/div[@class="sons"]')  # 获取列表元素
    item = {}
    for div in divs:
        item['id'] = uuid.uuid4().hex
        item['name'] = div.xpath('.//p[1]//text()')
        item['author'] = ''.join(div.xpath('.//p[2]/a/text()'))
        item['content'] = '<br>'.join(div.xpath('.//div[@class="contson"]/text()'))
        item['tags'] = '，'.join(div.xpath('./div[last()]/a/text()'))

        save_to_mysql(item, connection)


def get(url, connection):
    """
    发起 HTTP 请求获取数据
    :param url: 要请求的 URL
    :param connection: pymysql 连接对象
    """
    resp = requests.get(url, headers={'User-Agent': header.get_ua()})

    if resp.status_code == 200:
        parse(resp.text, connection)
    else:
        raise Exception('请求失败')


if __name__ == '__main__':
    # 创建数据库连接
    connection = pymysql.connect(host='',
                                 user='root',
                                 password='!',
                                 db='',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    get('https://www.gushiwen.cn/', connection)
    # 关闭数据库连接
    connection.close()
