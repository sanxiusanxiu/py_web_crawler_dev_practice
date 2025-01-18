import time

from cffi.cffi_opcode import CLASS_NAME
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

# 设置用户代理
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

# 设置ChromeDriver的路径
chrome_driver_path = 'chromedriver.exe'
# 设置Chrome选项
chrome_options = Options()
# 最大化浏览器窗口
chrome_options.add_argument("--start-maximized")
# 创建Service对象，用于配置ChromeDriver服务的可执行路径
service = Service(executable_path=chrome_driver_path)
# 初始化webdriver，指定使用的ChromeDriver服务以及配置的选项
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # 隐式等待
    driver.implicitly_wait(100)
    driver.get('https://spa2.scrape.center/')
    # 如果找不到节点，先等一段时间再查找DOM  logo-image
    input = driver.find_element(by=By.CLASS_NAME, value='result')
    print(input)

finally:
    # 关闭浏览器
    driver.quit()