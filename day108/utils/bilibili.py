import time
import requests


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
            ...
        #     # print(author, title, href, created)
        #     data_list.append([author, title, href, created])
        data_list.append([author, title, href, created])

    return data_list


def mid_data(mid):
    """ 获取某个up主视频信息 """
    api_url = f'https://api.bilibili.com/x/space/arc/search?mid={mid}&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp'

    # 1小时的时间戳3600
    timestamp = time.time() - 3600 * 24 * 7

    # 解析一页，返回data_list
    data_mid = parse_page(api_url, timestamp)

    return data_mid
