import requests
from lxml import etree

url = 'https://www.colorhub.me/'

resp = requests.get(url)
print(resp.status_code)
html = etree.HTML(resp.text)
#
# divs = html.xpath('/html/body/div[1]/div/div[3]/div/div[3]/div/div')
# print(divs)
# # for div in divs:
# #     title = div.xpath('./div[1]/div/a/img/@title')
# #     print(title)


titles = html.xpath('/html/body/div[1]/div/div[3]/div/div[3]/div/div/div[1]/div/a/img')
for i in titles:
    title = i.xpath('./@alt')
    print(title)
