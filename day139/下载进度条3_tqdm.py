import os.path
import time
import requests
from tqdm import tqdm

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def parse_link(url):
    opt = Options()
    opt.add_argument('--headless')
    opt.add_argument('--disable-gpu')

    web = Chrome(options=opt)

    web.implicitly_wait(1)

    web.get(url)

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
    return video_src, title


def download(url, name):
    resp = requests.get(url, stream=True)
    total = int(resp.headers.get('content-length', 0))
    with open(name, 'wb') as f, tqdm(
            desc=name,
            total=total,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
    ) as bar:
        for data in resp.iter_content(chunk_size=1024):
            size = f.write(data)
            bar.update(size)


if __name__ == '__main__':
    if os.path.exists('urls.txt'):
        with open('urls.txt', 'r') as f:
            urls = f.readlines()
        for url in urls:
            video_src, title = parse_link(url.strip())
            download(video_src, f'{title}.mp4')
    else:
        url = ''
        video_src, title = parse_link(url.strip())
        download(video_src, f'{title}.mp4')