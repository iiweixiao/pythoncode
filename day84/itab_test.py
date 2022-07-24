import requests



url = 'https://api.codelife.cc/api/top/list'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'signaturekey': 'U2FsdGVkX183Kuu0UDTrFCyzQT5+xTkJTGakvwWZnkw=',
}

data = {id: "KqndgxeLl9"}

resp = requests.post(url=url, data=data, headers=headers)
data_json = resp.json()
print(data_json)

# data_list = data_json['data']
# for data_dict in data_list:
#     print(data_dict['link'])