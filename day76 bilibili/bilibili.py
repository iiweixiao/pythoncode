import os
import time
import requests

import smtplib
from email.utils import formataddr
from email.mime.text import MIMEText


def parse_page(url, timestamp):
    data_list = []  # 用于存储此url所有视频信息：作者，标题，播放地址，创建时间

    resp = requests.get(url).json()
    vlist = resp['data']['list']['vlist']

    for dic in vlist:
        author = dic['author']
        title = dic['title']
        bvid = dic['bvid']
        href = f'https://www.bilibili.com/video/{bvid}'
        created_timestamp = dic['created']
        localtime = time.localtime(created_timestamp)
        created = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
        if created_timestamp > timestamp:
            # print(author, title, href, created)
            data_list.append([author, title, href, created])

    return data_list


def mid_data(mid):
    """ 获取某个up主视频信息 """
    api_url = f'https://api.bilibili.com/x/space/arc/search?mid={mid}&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp'

    # 1小时的时间戳3600
    timestamp = time.time() - 3600 * 24 * 1.2

    # 解析一页，返回data_list
    data_list = parse_page(api_url, timestamp)
    # print(data_list)

    # 发送邮件
    content = ''
    if data_list:
        content = f'<h1>{data_list[0][0]}</h1><br>'
        for index, item in enumerate(data_list):
            content += f"{index + 1} <a href='{item[2]}'>{item[1]}</a> <br>{item[3]} <br> <br>"
    return content


def send_email(r_addr, content, subject='python'):
    # 邮件内容配置
    # 邮件文本
    msg = MIMEText(content, "html", "utf-8")
    # 邮件上显示的发件人
    msg["From"] = formataddr(["wx_python", "iiweixiao@yeah.net"])
    # 邮件上显示的主题
    msg["Subject"] = subject

    # 发送邮件
    server = smtplib.SMTP_SSL("smtp.yeah.net")
    server.login("iiweixiao@yeah.net", "IHHLUMDULZIKQPQR")  # "发件人的邮箱", "这里填写授权码"
    server.sendmail("iiweixiao@yeah.net", r_addr, msg.as_string())  # "发件人邮箱", "接受人邮箱"
    server.quit()
    print('已发送邮件')
    # send_email(r_addr, content)


def parse_ids():
    path = os.path.dirname(os.path.abspath(__file__))
    txt = os.path.join(path, 'up_ids.txt')
    if not os.path.exists(txt):
        with open(txt, 'w') as f:
            up_id = '20165629:共青团中央'
            f.write(up_id)

    up_ids = []
    with open(txt, 'r') as f:
        s = f.read()

    lst = s.splitlines()

    for item in lst:
        if '：' in item:
            item = item.replace('：', ':')
        up_ids.append(item.split(':')[0])

    print('成功获取up主的id')
    return up_ids


def main():
    # up_ids = ['927587', '520324999', '542507083', '17171565', '167531912']

    # 获取up主的id，返回列表
    up_ids = parse_ids()

    # 循环解析每个up主视频
    contents = ''
    for mid in up_ids:
        content = mid_data(mid)
        print(f'解析{mid}成功')
        contents += content

    send_email('weixiaot2021@icloud.com', contents, 'bilibili')
    # print(contents)
    print('over')


if __name__ == '__main__':
    main()
