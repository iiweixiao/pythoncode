import csv

import requests
import pymongo

# https://xueqiu.com/service/v5/stock/screener/quote/list?page=1&size=30&order=desc&order_by=amount&exchange=CN&market=CN&type=sha&_=1614500868073
# https://xueqiu.com/service/v5/stock/screener/quote/list?page=2&size=30&order=desc&order_by=amount&exchange=CN&market=CN&type=sha&_=1614501032124


# client = pymongo.MongoClient(host='localhost', port=27017)
# db = client.test


def get_index_page(page):
    url = "https://xueqiu.com/service/v5/stock/screener/quote/list?page={}&size=30&order=desc&order_by=amount&exchange=CN&market=CN&type=sha&_=1614500868073".format(
        str(page))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
        'X - Requested - With': 'XMLHttpRequest'
    }
    r = requests.get(url, headers=headers)
    r = r.json()
    return r


def parse_page(json):
    data_list = json['data']['list']

    for data in data_list:
        data_dict = {}
        股票代码 = data['symbol']
        股票名称 = data['name']
        当前价格 = data['current']
        涨跌额 = data['chg']
        涨跌幅度 = data['percent']
        年初至今 = data['current_year_percent']
        成交量 = data['volume']
        成交额 = data['amount']
        换手率 = data['turnover_rate']
        市盈率 = data['pe_ttm']
        股息率 = data['dividend_yield']
        if 股息率:
            股息率 = str(data['dividend_yield']) + '%'
        else:
            股息率 = None
        市值 = data['market_capital']
        data_dict = {"股票代码": 股票代码,
                     "股票名称": 股票名称,
                     "当前价格": 当前价格,
                     "涨跌额": 涨跌额,
                     "涨跌幅度": 涨跌幅度,
                     "年初至今": 年初至今,
                     "成交量": 成交量,
                     "成交额": 成交额,
                     "换手率": 换手率,
                     "市盈率": 市盈率,
                     "股息率": 股息率,
                     "市值": 市值
                     }
        save_csv(data_dict, 股票名称)
        # save_MongoDB(data_dict,股票名称)
    pass


# 保存到MongoDB
# def save_MongoDB(data, name):
#     if db['xuehua1'].insert(data):
#         print(name, '存到MongoDB成功')
#         return True
#     return False


# 保存到csv数据
file = open('./雪球股票数据.csv', mode='a')
csv_writer = csv.DictWriter(file, fieldnames=[
    '股票代码', '股票名称', '当前价格', '涨跌额', '涨跌幅度', '年初至今', '成交量', '成交额', '换手率', '市盈率', '股息率', '市值'
])
csv_writer.writeheader()


def save_csv(data, name):
    csv_writer.writerow(data)
    print("{}成功写入csv文件".format(name))


def main():
    for page in range(1, 3):
        print(f"++++++++++++正在打印第{page}股票数据++++++++++++")
        json = get_index_page(page)
        parse_page(json)


if __name__ == '__main__':
    main()
