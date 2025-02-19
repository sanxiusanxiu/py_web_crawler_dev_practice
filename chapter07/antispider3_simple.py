import logging
import time

from selenium import webdriver
from pyquery import PyQuery as pq
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

chrome_driver_path = 'chromedriver.exe'
chrome_options = Options()
# chrome_options.add_argument('--start-maximized')
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'https://antispider3.scrape.center/'
time_out = 40

driver.get(url)
time.sleep(3)
WebDriverWait(driver, time_out).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.item')))
html = driver.page_source
doc = pq(html)
names = doc('.item .name')
for name in names.items():
    print(name.text())

driver.close()
