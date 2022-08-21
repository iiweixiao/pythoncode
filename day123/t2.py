import random

import requests

url = 'https://www.baidu.ocm'

prox_list = [
    'https://120.194.55.139:6969',
    'https://47.106.105.236:80',
    'https://47.106.105.236:80',
    'https://223.82.60.202:8060',
    'https://120.194.55.139:6969',
    'https://223.82.60.202:8060',
    'https://47.106.105.236:80',
    'https://223.82.60.202:8060',
    'https://223.96.90.216:8085',
    'https://47.113.90.161:83',
    'https://58.215.201.98:56566',
    'https://101.200.127.149:3129',
    'https://122.9.101.6:8888',
    'https://223.82.60.202:8060',
    'https://58.20.184.187:9091',
]

# prox = random.choice(prox_list)
# print(prox)
for prox in prox_list:
    try:
        resp = requests.get(url=url)
        print(resp.status_code)
    except:
        print('超时')

