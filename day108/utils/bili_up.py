import requests


def parse_mid(mid):
    url = f'https://api.bilibili.com/x/space/arc/search?mid={mid}&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp'
    resp = requests.get(url).json()
    name = resp['data']['list']['vlist'][0]['author']
    return name


mid = '50063223'
