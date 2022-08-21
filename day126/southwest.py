import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
#
# opt = Options()
# # opt.add_argument('--headless')
# opt.add_argument('--disable-gpu')
# opt.add_experimental_option('excludeSwitches', ['enable-automation'])  # 去除自动化程序控制提示

# web = Chrome(options=opt)

from selenium import webdriver

# from auth_proxy import proxyauth_plugin_path

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.101 Safari/537.36'
# 反爬配置
options = webdriver.ChromeOptions()  # 设置谷歌浏览器的一些配置选项
options.add_argument('--incognito')  # 设置隐私（无痕）模式
# options.add_argument('--headless')  # 设置无头模式
# options.add_argument('--proxy-server=https://host:port')  # 无账号密码代理
# options.add_extension(proxyauth_plugin_path)  # 设置私密代理，需要将配置文件保存为auth_proxy.py保存后导入此文件
options.add_experimental_option(f'--user-agent={user_agent}')  # 模拟浏览器发送请求
options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 去除自动化程序控制提示

# 初始化浏览器对象
web = webdriver.Chrome(options=options)
# driver.get('https://www.baidu.com')

# 规避webdriver监测
# 括号中是官网给的，直接粘贴过来
web.execute_cdp_cmd(
    'Page.addScriptToEvaluateOnNewDocument',
    {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'}
)





# web = Chrome()

# web.get('https://hotels.ctrip.com/')
web.get('https://www.southwest.com/')

time.sleep(3)
# el = web.find_element(by=By.XPATH, value='//*[@id="hp_nfes_searchbar"]/div')
# el.click()
# el.send_keys('西安', Keys.ENTER)
web.find_element(by=By.XPATH, value='//*[@id="LandingAirBookingSearchForm_originationAirportCode"]').send_keys('LAX')
time.sleep(0.3)
web.find_element(by=By.XPATH, value='//*[@id="LandingAirBookingSearchForm_destinationAirportCode"]').send_keys('SFO')
time.sleep(0.3)
web.find_element(by=By.XPATH, value='//*[@id="LandingAirBookingSearchForm_departureDate"]').send_keys(Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE,'9/2')
time.sleep(0.3)
web.find_element(by=By.XPATH, value='//*[@id="LandingAirBookingSearchForm_returnDate"]').send_keys('9/9')
time.sleep(0.3)
el = web.find_element(by=By.XPATH, value='//*[@id="LandingAirBookingSearchForm_submit-button"]')
el.click()