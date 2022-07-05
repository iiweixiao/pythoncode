import os
import time
import requests


def parse_page(url, timestamp):
    data_list = []  # 用于存储此url所有视频信息：作者，标题，播放地址，创建时间
    print(data_list)
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
    timestamp = time.time() - 3600 * 24 * 1.1

    # 解析一页，返回data_list
    data_list = parse_page(api_url, timestamp)

    return data_list


def data_all():
    up_ids = ['927587', '520324999', '542507083', '167531912', '1578434087', '1488338933', '40430723', '1061932792',
              '8096990', '1435524207', '1067142290', '213845897', '54079756', '17171565', '314022607', '159085018',
              '287051252']
    # 循环解析每个up主视频
    data = []
    for mid in up_ids:
        data_list = mid_data(mid)
        print(f'解析{mid}成功')
        data.append(data_list)

    return data
