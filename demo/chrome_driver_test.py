import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 指定下载的chromedriver的路径
chromedriver_path = './chromedriver.exe'
# 设置Chrome选项
chrome_options = Options()
# 创建Service对象
service = Service(executable_path=chromedriver_path)
# 初始化webdriver
browser = webdriver.Chrome(service=service, options=chrome_options)

browser.get('https://0day.today/')
time.sleep(2)
