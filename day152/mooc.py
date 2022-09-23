import re

import requests
from lxml import etree

# 获取所有学校链接及学校中文名
url = 'https://www.icourse163.org/university/view/all.htm#/'
resp = requests.get(url)
html = etree.HTML(resp.text)
# print(html)
href_list = html.xpath('//*[@id="g-body"]/div/div[2]/div[2]/a/@href')
c_school_name_list = html.xpath('//*[@id="g-body"]/div/div[2]/div[2]/a/img/@alt')
count = len(href_list)
# print(c_school_name_list)

def get_courses(href, school_id, c_school_name):
    url2 = 'https://www.icourse163.org/web/j/courseBean.getCourseListBySchoolId.rpc?csrfKey=20ccec6465b249c588159aecac2d2efc'

    school_name = href.replace('/university/', '')

    headers = {
        'referer': f'https://www.icourse163.org/university/{school_name}',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33',
        'cookie': 'EDUWEBDEVICE=9cf6af5608244b94bc9f7174d0811fdd; WM_TID=sx9YVCawsAhFFAQUFRaQX0r0ygkL8xj7; __yadk_uid=Eq2gRAruk46gVN8c5T6desuqnHex9fR5; NTESSTUDYSI=20ccec6465b249c588159aecac2d2efc; utm="eyJjIjoiIiwiY3QiOiIiLCJpIjoiIiwibSI6IiIsInMiOiIiLCJ0IjoiIn0=|aHR0cHM6Ly9jbi5iaW5nLmNvbS8="; hb_MA-A976-948FFA05E931_source=cn.bing.com; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1663170657,1663254354; WM_NI=lDcm1%2F44mU6VxV%2FDZk4hlLpP7Jg8QXbAwsyOndjMyLm3r9qtXkzhO3Sp1qQS8wrFnSENmOWfjlOo0wxUs0KhjPddGtDODn7pEJIAgermsYTqksLFZnYaurUUQv49rYxnenM%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea9cf39f7ef878ece43a2968ba3d55f829a9eacd159af9e998bd33faae7afa8c62af0fea7c3b92ab09cad8eb425f8eca3b6b55ebc8ae1a5d961f8b8a4adf35cf596a9d9d454a29fb994fc45aebca6aefc48afedbedaf4809cb5b689ce3991b0ff92d459fca9bea7ed598792a3b0d66eaab48190b37dbc8bbdd1ca64aa90ac85c68088918c8fb67c879687a2e66fb2b3bdbad77ba9ad84a7d9669bbfbb93d85f93aafcdaf153bcb2ab8fd037e2a3; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1663254551',
    }

    print(c_school_name)

    p = 1
    while True:
        data = {
            'schoolId': f'{school_id}',
            'p': p,
            'psize': '20',
            'type': '1',
            'courseStatus': '30',
        }

        resp = requests.post(url=url2, data=data, headers=headers)
        course_dict = resp.json()

        if course_dict['result']['list']:
            course_list = course_dict['result']['list']
            print(f'---第{p}页---')
            for item in course_list:
                href = f'https://www.icourse163.org/course/{school_name}-{item["id"]}'
                print(item['name'], href)
            p += 1
        else:
            break


for i in range(count):
    # 获取某个学校的schoolID
    url1 = f'https://www.icourse163.org{href_list[i]}'
    # print(href_list[i])
    # print(url1)
    resp1 = requests.get(url1)
    html1 = etree.HTML(resp1.text)
    script_text = html1.xpath('//*[@id="g-body"]/script[1]/text()')[0]
    pattern = re.compile('schoolId = "(.*?)";', re.S)
    school_id = re.findall(pattern, script_text)[0]
    # print(school_id)
    # print(c_school_name_list[i])
    get_courses(href_list[i], school_id, c_school_name_list[i])