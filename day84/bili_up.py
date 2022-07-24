import sys
import time
import requests
import smtplib
from email.utils import formataddr
from email.mime.text import MIMEText


def send_email(r_addr, content_list, subject='python(默认主题)'):

    # 将数据列表加工成邮件格式
    content = f'<h1>{content_list[0][0]}</h1>'
    for index, item in enumerate(content_list):
        content += f"{index + 1} <a href='{item[2]}'>{item[1]}</a> <br>{item[3]} <br> <br>"
        print(item[1])
        # 邮件内容配置
    # 邮件文本
    msg = MIMEText(content, "html", "utf-8")
    # 邮件上显示的发件人:wx_python
    msg["From"] = formataddr(["bili_up", "iiweixiao@yeah.net"])
    # 邮件上显示的主题
    msg["Subject"] = subject

    # 发送邮件
    # server = smtplib.SMTP_SSL("smtp.yeah.net")
    # server.login("iiweixiao@yeah.net", "IHHLUMDULZIKQPQR")  # "发件人的邮箱", "这里填写授权码"
    # server.sendmail("iiweixiao@yeah.net", r_addr, msg.as_string())  # "发件人邮箱", "接受人邮箱"
    # server.quit()
    print('已发送邮件')
    # send_email(r_addr, content)

mid = '20165629'

if len(sys.argv) > 1:
    mid = sys.argv[1]

page = 1
data_list = []  # 用于存储此url所有视频信息：作者，标题，播放地址，创建时间

while True:
    url_api = f'https://api.bilibili.com/x/space/arc/search?mid={mid}&ps=30&tid=0&pn={page}&keyword=&order=pubdate&jsonp=jsonp'
    resp = requests.get(url_api).json()
    if not resp['data']:
        print('请求被拦截')
        break
    vlist = resp['data']['list']['vlist']
    if not vlist:
        break
    for dic in vlist:
        author = dic['author']
        title = dic['title']
        bvid = dic['bvid']
        href = f'https://www.bilibili.com/video/{bvid}'
        created_timestamp = dic['created']
        localtime = time.localtime(created_timestamp)
        created = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
        # print(author, title, href, created)

        data_list.append([author, title, href, created])
    print(f'第{page}页解析完毕')
    page += 1

if data_list:
    # print(data_list)
    send_email('weixiaot2021@icloud.com', data_list, data_list[0][0])
