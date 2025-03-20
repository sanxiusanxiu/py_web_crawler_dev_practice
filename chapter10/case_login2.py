import time
import requests

from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def login2_selenium():
    base_url = 'https://login2.scrape.center/'
    login_url = urljoin(base_url, '/login')
    index_url = urljoin(base_url, '/page/1')
    username = 'admin'
    password = 'admin'
    chrome_driver_path = '../chapter07/chromedriver.exe'
    chrome_options = Options()
    # 忽略浏览器证书验证
    chrome_options.add_argument('--ignore-certificate-errors')
    service = Service(executable_path=chrome_driver_path)
    browser = webdriver.Chrome(service=service, options=chrome_options)
    browser.get(base_url)
    time.sleep(3)
    browser.find_element(by=By.CSS_SELECTOR, value='input[name="username"]').send_keys(username)
    browser.find_element(by=By.CSS_SELECTOR, value='input[name="password"]').send_keys(password)
    browser.find_element(by=By.CSS_SELECTOR, value='input[type="submit"]').click()
    time.sleep(9)
    # 获取 Cookie
    cookies = browser.get_cookies()
    print('Cookies: ', cookies)
    browser.close()
    # 使用 Cookie
    session = requests.Session()
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])
    response_index = session.get(index_url)
    print('状态码：', response_index.status_code)
    print('URL: ', response_index.url)

login2_selenium()
