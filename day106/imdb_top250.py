import requests
from lxml import etree


url = 'https://www.iyingku.cn/imdb250/'

res = requests.get(url)
data = etree.HTML(res.text)

trs = data.xpath('//tbody/tr')
n = 1
for tr in trs:
    title = tr.xpath('./td[2]/a/@title')[0]
    href = 'https://iyingku.cn' + tr.xpath('./td[2]/a/@href')[0]
    print(n, title, href)
    n += 1