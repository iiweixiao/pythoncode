import requests

url = 'https://www.yaozh.com/login/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27',
}

form_data = {
    'username': 'hexiang1st',
    'pwd': 'Dafengche2nd',
    'formhash': '3103A5BD2F',
    'backurl': 'https%3A%2F%2Fwww.yaozh.com%2F',
}

# 实例化Session
session = requests.Session()

# 通过session，保存自己的cookie
resp = session.post(url, data=form_data, headers=headers)

member_url = 'https://www.yaozh.com/member'

# 通过session请求个人信息页面，就这个session带了cookie去请求的
data = session.get(member_url, headers=headers).text
print(data)