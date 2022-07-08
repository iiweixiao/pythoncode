import time
import sys
import requests
import smtplib
from email.utils import formataddr
from email.mime.text import MIMEText

"""
2022/7/8
哔哩哔哩bilibili合集视频解析，并发送到指定邮箱
"""


def parse(url):
    # bvid在查询参数params中要用到
    bvid = url.split('video/')[1].split('/')[0]

    # 最难的一步，找到存储数据的api接口
    url_api = 'https://api.bilibili.com/x/web-interface/view/detail'

    # 查询参数
    params = {
        "bvid": bvid,
        "aid": "",
        "need_operation_card": 1,
        "web_rm_repeat": 1,
        "need_elec": 1,
        "out_referer": "",
        "page_no": 1
    }

    # 将数据解析成json格式
    resp = requests.get(url=url_api, params=params)
    data_json = resp.json()

    # 找到存放每条内容的列表
    episodes = data_json['data']['View']['ugc_season']['sections'][0]['episodes']

    # 将每条内容存到content_list中返回
    content_list = []
    for index, item in enumerate(episodes):
        # 标题
        title = item['arc']['title']
        # 播放地址
        bvid = item['bvid']
        href = 'https://www.bilibili.com/video/' + bvid
        # 创建时间
        created_timestamp = item['arc']['ctime']
        localtime = time.localtime(created_timestamp)
        created = time.strftime("%Y-%m-%d %H:%M:%S", localtime)

        # 测试输出
        print(index + 1, title, href, created)

        content_list.append([title, href, created])

    return content_list


def send_email(r_addr, content_list, subject='python(默认主题)'):
    # 将数据列表加工成邮件格式
    content = ''
    for index, item in enumerate(content_list):
        content += f"{index + 1} <a href='{item[1]}'>{item[0]}</a> <br>{item[2]} <br> <br>"

    # 邮件内容配置
    # 邮件文本
    msg = MIMEText(content, "html", "utf-8")
    # 邮件上显示的发件人:wx_python
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


# 可以在这里填上有合集的任意一个视频地址
url = 'https://www.bilibili.com/video/BV1C94y1X75h/?spm_id_from=333.788'
subject = '零基础学剪映'

# 也可以在运行时将视频地址作为参数传入
if len(sys.argv) == 2:
    url = sys.argv[1]
elif len(sys.argv) == 3:
    url = sys.argv[1]
    subject = sys.argv[2]

content_list = parse(url)

# send_email('weixiaot2021@icloud.com', content_list, subject)
