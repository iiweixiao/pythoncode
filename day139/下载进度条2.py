import time
import requests
from contextlib import closing

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import progressbar

opt = Options()
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')

web = Chrome(options=opt)

web.implicitly_wait(1)

web.get('https://mp.weixin.qq.com/s/LMCHQXMk3nElzyTNGXNilw')

time.sleep(2)
title = web.find_element(by=By.XPATH, value='//*[@id="js_video_page_title"]').text
print(title)
el = web.find_element(by=By.XPATH,
                      value='/html/body/div[2]/div[1]/div/div[1]/div[3]/div/div/div[3]/div/div/div/div[1]/div/div[5]/button')
el.click()

video_src = web.find_element(by=By.XPATH,
                             value='/html/body/div[2]/div[1]/div/div[1]/div[3]/div/div/div[3]/div/div/div/div[1]/div/div[17]/div[1]/video').get_attribute(
    'src')
print(video_src)

headers = {
    'Connection': 'keep-alive',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.101 Safari/537.36',
}

with closing(requests.get(video_src, headers=headers, stream=True)) as response:
    response = requests.request('GET', url=video_src, stream=True, data=None, headers=headers)
    total_length = int(response.headers["content-length"])
    chunk_size = 1024  # 单次请求最大值
    # response.headers['content-length']得到的数据类型是str而不是int
    content_size = int(response.headers['content-length'])  # 文件总大小
    data_count = 0  # 当前已传输的大小
    with open(f'{title}.mp4', 'wb') as f:
        widgets = ['Progress: ', progressbar.Percentage(), ' ',
                   progressbar.Bar(marker='#', left='[', right=']'),
                   ' ', progressbar.ETA(), ' ', progressbar.FileTransferSpeed()]
        pbar = progressbar.ProgressBar(widgets=widgets, maxval=total_length).start()
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
            pbar.update(len(chunk) + 1)
        pbar.finish()



web.close()
