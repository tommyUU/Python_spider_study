"""
复杂的get请求，多页面请求下载
"""
import time
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from utils import header
import ssl

# keyword = input()
# page = input()
# url = f'https://www.baidu.com/s?wd={keyword}&pn={page}'
url = 'https://www.baidu.com/s?'
params = {
    'wd': '',
    'pn': 0  # 0, 10 ,20... = (n-1) * 10
}


def pages_get(wd):
    params['wd'] = wd
    for page in range(40):
        params['pn'] = (page - 1) * 10

        page_url = url + urlencode(params)
        resp = urlopen(Request(page_url, headers={'User-Agent': header.get_ua()}))

        assert resp.code == 200
        file_name = 'urllib_baidu_pages/%s-%s.html' % (wd, page)
        with open(file_name, 'wb') as f:
            bytes_ = resp.read()
            f.write(bytes_)
        print(f'下载{file_name}成功！')
        time.sleep(0.5)


if __name__ == '__main__':
    pages_get('Python')