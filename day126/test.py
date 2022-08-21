import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

web = Chrome()

web.get('https://www.lagou.com/')

# web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a')
el = web.find_element(by=By.XPATH, value='//*[@id="changeCityBox"]/p[1]/a')
el.click()

web.find_element(by=By.XPATH, value='//*[@id="search_input"]').send_keys('python', Keys.ENTER)
# web.find_element(by=By.XPATH, value='//*[@id="search_button"]').click()

div_list = web.find_elements(by=By.XPATH, value='//*[@id="jobList"]/div[1]/div')
with open('拉勾网.txt', 'a') as f:
    for div in div_list:
        title = div.find_element(by=By.XPATH, value='./div/div/div/a').text
        salary = div.find_element(by=By.XPATH, value='./div/div/div[2]/span').text
        company = div.find_element(by=By.XPATH, value='./div/div[2]/div/a').text
        div.find_element(by=By.XPATH, value='./div/div/div/a').click()
        web.switch_to.window(web.window_handles[-1])
        time.sleep(1)
        job_detail = web.find_element(by=By.XPATH, value='//*[@id="job_detail"]/dd[2]').text
        web.close()
        web.switch_to.window(web.window_handles[0])
        s = company + '  ' + title + '  ' + salary + '\n' + job_detail
        f.writelines(s)
        print(company, title, salary)
        print(job_detail)
        print('--------')

web.close()