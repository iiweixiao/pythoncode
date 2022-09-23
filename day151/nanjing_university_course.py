import requests

url = 'https://www.icourse163.org/web/j/courseBean.getCourseListBySchoolId.rpc'
# param = {
#     'csrfKey': '27e640d2d90d4df588a99726fdf6c476'
# }
data = {
    'schoolId': '9002',
    'p': '1',
    'psize': '20',
    'type': '1',
    'courseStatus': '30',
}
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33',
    'referer': 'https://www.icourse163.org/university/NJU',
    'origin': 'https://www.icourse163.org',
}
resp = requests.post(url=url, data=data, headers=headers)
print(resp.json())
