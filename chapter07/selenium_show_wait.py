import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    # 显式等待
    # driver.get('https://spa2.scrape.center/')
    driver.get('https://www.taobao.com/')
    wait = WebDriverWait(driver, 10)
    input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-tao')))
    print(input, button)

finally:
    # 关闭浏览器
    driver.quit()
