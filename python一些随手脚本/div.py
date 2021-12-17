
import requests
import re
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

if __name__ == '__main__':
    list_url = []
    url = 'https://alicert.taobao.com/exam/test?sid=_79387115011559&tenantName=ecpc_tenant_dingding&sst=a6BSHFOXbcpI4xQzxgK1el7yaQyGhyIrFhS5t3KWZWiH1vKhKO%2FRnbUnHmPxtpEt'
    # 设置请求头信息
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    req = requests.get(url=url, headers=headers)
    req.encoding = 'utf-8'
    html = req.text
    print(html)
    bf = BeautifulSoup(html, 'html.parser')
    targets_url_1 = bf.find_all(class_='_1rKgDfhM2eglNNPWZBFiMy')
    print(targets_url_1)
    bf = BeautifulSoup(str(targets_url_1), 'html.parser')
    targets_url_2 = bf.find_all(class_='name')

    # 保存名字链接
    for each in targets_url_2:
        list_url.append(
            re.sub('[\t\n]', "", re.sub(r'<[^>]+>', "", str(each))))

    f = open('保存题目.txt', 'w')  # 首先先创建一个文件对象，打开方式为w
    for each in list_url:
        f.writelines(each)  # 用readlines()方法写入文件
        f.writelines('\n')

    print(list_url)

    print('下载完成！')
