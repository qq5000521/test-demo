from urllib.request import urlretrieve

import requests
from bs4 import BeautifulSoup


def get_mm(page):
    for i in range(1, page+1):
        # 想要什么类型，cid就替换成什么
        url = "https://www.buxiuse.com/?cid=2&page=%d" % i
        head = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0"
        }
        resp = requests.get(url, headers=head)
        # print(resp.text)
        page = BeautifulSoup(resp.text, "html.parser")
        # 拿到所有img标签
        img = page.find_all('img')
        # print(img)
        # 遍历img
        for i in img:
            # print(i)
            # 拿到src瞎子路径
            src = i.get("src")
            # print(src)
            # 拿到标题，方便命名
            name = i.get("title")
            # 设置好下载路径
            path = "img/{}.jpg".format(name)
            print("正在下载{}.jpg".format(name))
            # print(page)
            # 下载路径和保持路径
            urlretrieve(src, path)


# 设置下载页数 我设置为两页
get_mm(2)
