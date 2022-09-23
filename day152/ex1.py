import requests

url = 'https://www.icourse163.org/web/j/courseBean.getCourseListBySchoolId.rpc?csrfKey=20ccec6465b249c588159aecac2d2efc'
# url = 'https://www.icourse163.org/web/j/courseBean.getCourseListBySchoolId.rpc?csrfKey=0fc91ff1e45140349b4578af63f709e1'


school_name = 'TUT'
# school_name = 'ZJU'
headers = {
    'referer': f'https://www.icourse163.org/university/{school_name}',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33',
    'cookie': 'EDUWEBDEVICE=9cf6af5608244b94bc9f7174d0811fdd; WM_TID=sx9YVCawsAhFFAQUFRaQX0r0ygkL8xj7; __yadk_uid=Eq2gRAruk46gVN8c5T6desuqnHex9fR5; NTESSTUDYSI=20ccec6465b249c588159aecac2d2efc; utm="eyJjIjoiIiwiY3QiOiIiLCJpIjoiIiwibSI6IiIsInMiOiIiLCJ0IjoiIn0=|aHR0cHM6Ly9jbi5iaW5nLmNvbS8="; hb_MA-A976-948FFA05E931_source=cn.bing.com; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1663170657,1663254354; WM_NI=lDcm1%2F44mU6VxV%2FDZk4hlLpP7Jg8QXbAwsyOndjMyLm3r9qtXkzhO3Sp1qQS8wrFnSENmOWfjlOo0wxUs0KhjPddGtDODn7pEJIAgermsYTqksLFZnYaurUUQv49rYxnenM%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea9cf39f7ef878ece43a2968ba3d55f829a9eacd159af9e998bd33faae7afa8c62af0fea7c3b92ab09cad8eb425f8eca3b6b55ebc8ae1a5d961f8b8a4adf35cf596a9d9d454a29fb994fc45aebca6aefc48afedbedaf4809cb5b689ce3991b0ff92d459fca9bea7ed598792a3b0d66eaab48190b37dbc8bbdd1ca64aa90ac85c68088918c8fb67c879687a2e66fb2b3bdbad77ba9ad84a7d9669bbfbb93d85f93aafcdaf153bcb2ab8fd037e2a3; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1663254551',
}

data = {
    'schoolId': '9002',
    'p': '1',
    'psize': '20',
    'type': '1',
    'courseStatus': '30',
}

resp = requests.post(url=url, data=data, headers=headers)
course_dict = resp.json()

course_list = course_dict['result']['list']
for item in course_list:
    href = f'https://www.icourse163.org/course/{school_name}-{item["id"]}'
    print(item['name'], href)
