import logging
import re
import time

from selenium import webdriver
from pyquery import PyQuery as pq
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 解析源码得到标题
def parse_name(name_html):
    has_whole = name_html('.whole')
    if has_whole:
        return name_html.text()
    else:
        chars = name_html('.char')
        items = []
        for char in chars.items():
            items.append({
                'text': char.text().strip(),
                'left': int(re.search(r'(\d+)px', char.attr('style')).group(1))
            })
        items = sorted(items, key=lambda x: x['left'], reverse=False)
        return ''.join([item.get('text') for item in items])

chrome_driver_path = 'chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument('--start-maximized')
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'https://antispider3.scrape.center/'
time_out = 40

driver.get(url)
# time.sleep(3)
WebDriverWait(driver, time_out).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.item')))
html = driver.page_source
doc = pq(html)
names = doc('.item .name')
for name_html in names.items():
    name = parse_name(name_html)
    print(name)

driver.close()
