import time
import requests

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


opt = Options()
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')

web = Chrome(options=opt)

web.implicitly_wait(1)

web.get('https://mp.weixin.qq.com/s/LMCHQXMk3nElzyTNGXNilw')

time.sleep(2)
title = web.find_element(by=By.XPATH, value='//*[@id="js_video_page_title"]').text
print(title)
el = web.find_element(by=By.XPATH, value='/html/body/div[2]/div[1]/div/div[1]/div[3]/div/div/div[3]/div/div/div/div[1]/div/div[5]/button')
el.click()

video_src = web.find_element(by=By.XPATH, value='/html/body/div[2]/div[1]/div/div[1]/div[3]/div/div/div[3]/div/div/div/div[1]/div/div[17]/div[1]/video').get_attribute('src')
print(video_src)


headers = {
    'Connection': 'keep-alive',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.101 Safari/537.36',
}

video = requests.get(url=video_src, headers=headers, stream=True)

with open(f'{title}.mp4', 'wb') as f:
    print('正在下载...')
    for chunk in video.iter_content(chunk_size=1024*1024):
        if chunk:
            f.write(chunk)
    print('下载完毕')
web.close()