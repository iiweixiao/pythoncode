import time
import sys
import requests


"""
2022/7/8
哔哩哔哩bilibili合集视频解析，并发送到指定邮箱
"""


def parse(url):
    # bvid在查询参数params中要用到
    bvid = url.split('video/')[1].split('/')[0]

    # 最难的一步，找到存储数据的api接口
    url_api = 'https://api.bilibili.com/x/web-interface/view/detail'
    # 对应的名称：https://api.bilibili.com/x/web-interface/view/detail?bvid=BV1qa411Q7Gt&aid=258378104&need_operation_card=1&web_rm_repeat=1&need_elec=1&out_referer=&page_no=1

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


# url = 'https://www.bilibili.com/video/BV1C94y1X75h/?spm_id_from=333.788'
# d = parse(url)
#
# print(d)
