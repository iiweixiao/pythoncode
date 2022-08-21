import loguru, requests, random, time
from lxml import etree
from concurrent.futures import ThreadPoolExecutor


def get_url():  # 得到存放ip地址的网页
    print("正在获取ip池", "，不要着急！")
    for i in range(random.randint(10, 20)):  # 爬取随机页数
        time.sleep(1)
        if i == 0:
            url = "https://ip.ihuan.me/"
        else:
            url = url_list[-1]
        try:
            resp = requests.get(url=url, headers=headers_test, timeout=10)
        except Exception as e:
            print(e)
            break
        html = etree.HTML(resp.text)
        ul = html.xpath('//ul[@class="pagination"]')
        ul_num = html.xpath('//ul[@class="pagination"]/li')
        for j in range(len(ul_num)):
            if j != 0 and j != len(ul_num) - 1:
                a = ul[0].xpath(f"./li[{j}+1]/a/@href")[0]
                url_list.append("https://ip.ihuan.me/" + a)  # 得到许多的代理ip网址
        loguru.logger.info(f"over，{url}")


def get_ip():
    for i in url_list:
        time.sleep(1)
        resp = requests.get(url=i, headers=headers)
        html = etree.HTML(resp.text)
        td = html.xpath("//tbody/tr")
        for i in td:
            ip = i.xpath("./td[1]//text()")[0]  # 地址
            pt = i.xpath("./td[2]//text()")[0]  # 端口
            tp = "http" if i.xpath("./td[5]//text()")[0] == "不支持" else "https"  # 访问类型
            ip_list.append({"type": tp, "proxy": f"{ip}:{pt}"})
    loguru.logger.info("ip地址获取完成")


def set_ip(url) -> "动态构建ip池":  # 要传入需要爬取网页的url
    try:
        f = open('./app/ip.txt', "r")
        for j in eval(f.read()):
            temp_ip.append(j)
        f.close()
    except Exception as e:
        print("没有ip，正在构造ip池，请稍等")

    if not temp_ip:  # 判断是否有ip地址
        print("没有ip地址，正在获取")
        get_url()
    else:
        for i in temp_ip:
            ip_list.append(i)  # 将已有的ip添加到测试ip中
        temp_ip.clear()

    get_ip()  # 得到大量ip地址
    with open('./app/ip.txt', "w") as file:
        file.write(ip_list)
    ip_able = list(set(j["proxy"] for j in ip_list if j["type"] == url.split(":")[0]))  # 存放符合要求的ip字符串，同时利用集合去重
    url_test = "http://httpbin.org/ip" if url.split(":")[0] == "http" else ""  # 测试ip地址是否有用

    def test_ip(ip):
        proxy_test = {
            "http": f"{ip}",
            "https": f"{ip}"
            # 注意：如果请求的ip是https类型的，但代理的ip是只支持http的，那么还是使用本机的ip，如果请求的ip是http类型的，那么代理的ip一定要是http的，前面不能写成https，否则使用本机IP地址
        }
        resp = requests.get(url=url_test, headers=headers, proxies=proxy_test, timeout=6)
        if resp.json()["origin"] == ip.split(":")[0]:
            ip = {"type": url.strip(":")[0], "proxy": ip}  # 格式化ip，便于后期处理，是的其有http/https标识
            temp_ip.append(ip)  # 符合条件的添加，不符合条件的抛弃

    with ThreadPoolExecutor(50) as pool:  # 使用多线程测试
        pool.map(test_ip, ip_able)

    pool.join()

    print("测试完毕")

    if temp_ip:
        i = random.choice(temp_ip)
        proxy = {
            "http": f"{i['proxy']}",
            "https": f"{i['proxy']}"
        }
        return proxy
    else:
        set_ip(url=url)


# 参数

headers = {
    'User-Agent': "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 96.0.4664 .93 Safari / 537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}
headers_test = {
    'User-Agent': "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 96.0.4664 .93 Safari / 537.36",
    "accept-encoding": "gzip, deflate, br",
    "cookie": "Hm_lvt_8ccd0ef22095c2eebfe4cd6187dea829=1642389014,1642412091",
    "Referer": "https://ip.ihuan.me/"
}
url_list, ip_list, temp_ip = ["https://ip.ihuan.me/"], [], []  # 存放url， 存放ip地址， 有用的ip地址

if __name__ == '__main__':
    proxy = set_ip(url="https://www.baidu.com")  # 得到代理ip
    print(proxy)
