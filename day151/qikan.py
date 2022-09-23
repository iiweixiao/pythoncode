import requests
from lxml import etree
import pandas as pd


def get_index(url):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    response = r.text
    return response


def parse_index(html):
    qiKan = etree.HTML(html)

    name = qiKan.xpath('//div[@class="goods-name"]/a/text()')
    level = qiKan.xpath('//div[@class="goods-name"]/a/em/text()')
    for i, j in zip(name, level):
        i = i.replace('\r\n\t\t  ', '')
        dict = {
            '期刊名称': [i],
            "期刊级别": [j]
        }
        save_csv(dict)


# 保存期刊
def save_csv(data):
    df = pd.DataFrame(data)
    df.to_csv('经济期刊爬取.csv', encoding='utf-8', mode='a', index=False, header=False)


def main():
    type = int(input("请输入你要查找的期刊类型代码 [1-工业期刊 2-经济期刊 3-教育期刊 4-社科期刊 5-医学期刊 6-政法期刊 7-科技期刊 8-其他期刊]："))
    base_url = ''
    if type == 1:
        base_url = '/gy/'
    elif type == 2:
        base_url = '/jjqk/'
    elif type == 3:
        base_url = '/qkqk/jiaoyuqikan/'
    elif type == 4:
        base_url = '/qkqk/skqk/'
    elif type == 5:
        base_url = "/qkqk/yxqk/"
    elif type == 6:
        base_url = '/qkqk/zfqk/'
    elif type == 7:
        base_url = "/qkqk/kj/"
    else:
        base_url = "/qkqk/qtqk/"

    for page in range(1, 10):
        url = "http://qikan.suhuwl.cn" + base_url + "list_1{}.html".format(page)
        html = get_index(url)
        parse_index(html)
        print(f'第{page}页保存完成')


if __name__ == '__main__':
    main()
