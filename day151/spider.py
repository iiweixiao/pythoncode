import requests
from lxml import etree
from selenium import webdriver
import time
import pandas as pd

start = time.time()
url = 'https://www.icourse163.org/university/view/all.htm#/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
}
r = requests.get(url).text
tree = etree.HTML(r)
# 获取大学链接
href = tree.xpath('//a[@class="u-usity f-fl"]/@href')
# 获取大学名称
name = tree.xpath('//a[@class="u-usity f-fl"]/img/@alt')

driver = webdriver.Chrome()
driver.maximize_window()


def get_school_all_course():
    while (True):
        html = driver.page_source
        tree = etree.HTML(html)

        # 获取课程的链接
        hrefList = tree.xpath('//div[@class="um-spoc-course-list_wrap"]/div/a/@href')
        # 获取课程名称
        nameList = tree.xpath(
            '//div[@class="um-spoc-course-list_wrap"]/div/a/div[@class="u-courseCardWithTime-teacher"]/span/text()')
        # print(len(nameList))
        for x, y in zip(hrefList, nameList):
            x = 'https:' + x
            course_name.append(y)
            course_url.append(x)

        flag = (int(len(nameList)) != 20)

        if flag:
            break
        else:
            try:
                a = driver.find_element_by_link_text('下一页')
                a.click()
                time.sleep(3)
            except:
                return None
            get_school_all_course()


def save(data, school):
    df = pd.DataFrame(data)
    df.to_csv('./{}.csv'.format(school), mode='a', encoding='ANSI', index=False, header=False)


# 课程的链接
course_url = []
# 课程的名称
course_name = []
detail_school = input("请输入大学的名称:")
for x, y in zip(href, name):
    大学链接 = 'https://www.icourse163.org' + x
    dict = {
        "大学名称": y,
        "大学课程链接": 大学链接
    }
    if dict["大学名称"] == detail_school:
        new_url = dict["大学课程链接"]
        driver.get(new_url)
        get_school_all_course()

        for i, j in zip(course_name, course_url):
            new_dict = {
                "课程名称": [i],
                "课程链接": [j]
            }
            save(new_dict, detail_school)
        driver.close()
        end = time.time()
        print(detail_school, '慕课的所有课程保存完成')
        deltatime = end - start
        print("项目所用时间为:", deltatime)
