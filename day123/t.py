import random
import time

import requests
from lxml import etree


def check_ip(proxies_list):
    time.sleep(1)
    can_use = []
    for ip in proxies_list:
        try:
            response = requests.get(url='https://www.baidu.com', proxies=ip, timeout=0.1)
            if response.status_code == 200:
                can_use.append(ip)
        except:
            print('当前的代理：', ip, '请求超时，检测不合格')
        else:
            print('当前的代理：', ip, '检测合格')
    return can_use


proxies_list = []
# for page in range(1, 6):
for page in range(1, 6):
    time.sleep(1)

    print(f'=============正在爬取第{page}页数据=============')
    url = f'https://www.kuaidaili.com/free/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54',
    }
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding

    tree = etree.HTML(response.text)
    trs = tree.xpath('//*[@id="list"]/table/tbody/tr')

    for tr in trs:
        ip_num = tr.xpath('./td[1]/text()')[0]
        ip_port = tr.xpath('./td[2]/text()')[0]
        ip_proxy = ip_num + ':' + ip_port
        print(ip_proxy)

        if tr.xpath('./td[4]/text()')[0] == 'HTTP':
            proxy_dict = {
                'http': 'http://' + ip_proxy,
            }

        if tr.xpath('./td[4]/text()')[0] == 'HTTPS':
            proxy_dict = {
                'https': 'https://' + ip_proxy,
            }

        proxies_list.append(proxy_dict)
        print("保存成功：", proxy_dict)

print('\n============正在检测===================')
check_ip(proxies_list)
# print(proxies_list)
proxy = random.choice(proxies_list)

print(proxy)

url = 'https://www.southwest.com/api/air-booking/v1/air-booking/page/air/booking/shopping'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54',
    # 'User-Agent': random.choice(my_headers),
    'Referer': 'https://www.southwest.com/air/booking/select.html?adultPassengersCount=1&departureDate=2022-08-26&departureTimeOfDay=ALL_DAY&destinationAirportCode=BWI&fareType=USD&int=HOMEQBOMAIR&originationAirportCode=ORD&passengerType=ADULT&reset=true&returnDate=&returnTimeOfDay=ALL_DAY&tripType=oneway',
    'Host': 'www.southwest.com',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
}

data = {
    "adultPassengersCount": "1",
    "application": "air-booking",
    "departureDate": "2022-08-25",
    "departureTimeOfDay": "ALL_DAY",
    "destinationAirportCode": "SFO",
    "fareType": "USD",
    "int": "HOMEQBOMAIR",
    "originationAirportCode": "LAX",
    "passengerType": "ADULT",
    "reset": "true",
    "returnDate": "2022-08-30",
    "returnTimeOfDay": "ALL_DAY",
    "site": "southwest",
    "tripType": "roundtrip",
}
resp = requests.get(url=url, data=data, headers=headers, proxies=proxy)
print(resp)
