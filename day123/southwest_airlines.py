import random

import requests

url = 'https://www.southwest.com/api/air-booking/v1/air-booking/page/air/booking/shopping'
data = {
    'adultPassengersCount': "1",
    'application': "air-booking",
    'departureDate': "2022-08-26",
    'departureTimeOfDay': "ALL_DAY",
    'destinationAirportCode': "BWI",
    'fareType': "USD",
    'int': "HOMEQBOMAIR",
    'originationAirportCode': "ORD",
    'passengerType': "ADULT",
    'reset': "true",
    'returnDate': "",
    'returnTimeOfDay': "ALL_DAY",
    'site': "southwest",
    'tripType': "oneway",
}
# UA池
my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]
headers = {
    # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54',
    'User-Agent': random.choice(my_headers),
    'Referer': 'https://www.southwest.com/air/booking/select.html?adultPassengersCount=1&departureDate=2022-08-26&departureTimeOfDay=ALL_DAY&destinationAirportCode=BWI&fareType=USD&int=HOMEQBOMAIR&originationAirportCode=ORD&passengerType=ADULT&reset=true&returnDate=&returnTimeOfDay=ALL_DAY&tripType=oneway',
    'Host': 'www.southwest.com',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
}

# ip代理池

resp = requests.post(url=url, data=data, headers=headers)
print(resp)
print(resp.status_code)

