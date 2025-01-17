import random
import time
from os import makedirs
from os.path import exists

import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

# 设置ChromeDriver的路径
chrome_driver_path = './chromedriver.exe'
# 设置Chrome选项
chrome_options = Options()
# 无头模式
# chrome_options.add_argument('--headless')
# 最大化窗口
chrome_options.add_argument("--start-maximized")
# 创建Service对象
service = Service(executable_path=chrome_driver_path)

# 保存路径，如果不存在则创建
results_dir = './VUL/'
exists(results_dir) or makedirs(results_dir)
all_tag = 766

try:
    # 初始化webdriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    # https://www.gartner.com/reviews/markets
    driver.get('https://www.gartner.com/reviews/markets')
    time.sleep(6)
    # //*[@id="marketSelectPage"]/div[2]/div/div[2]/div/div/section/div/div/ul/li[766]/div/a
    # /reviews/market/zero-trust-network-access
    # 获取766个条目
    for index in range(1, all_tag + 1):
        tail_url = driver.find_element(by=By.XPATH, value=f'//*[@id="marketSelectPage"]/div[2]/div/div[2]/div/div/section/div/div/ul/li[{index}]/div/a').get_attribute('href')
        print('tail_url:', tail_url)
        product_name = tail_url.split('/')[-1]
        product_name_pure = product_name[:30]
        print('product_name_pure:', product_name_pure)
        time.sleep(1)
        #
        loop_click_a = driver.find_element(by=By.XPATH, value=f'//*[@id="marketSelectPage"]/div[2]/div/div[2]/div/div/section/div/div/ul/li[{index}]/div')
        # loop_click_a = driver.find_element(by=By.XPATH, value=f'//*[@id="marketSelectPage"]/div[2]/div/div[2]/div/div/section/div/div/ul/li[{index}]/div/a/div[2]/i/svg')
        print('loop_click_a:', loop_click_a)
        loop_click_a.click()

        product_source = driver.page_source
        # 将源代码写入HTML文件
        file_name = results_dir + 'GARTNER-NAME-' + str(product_name_pure) + '.html'
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(product_source)
        random_number = random.randint(3, 9)
        time.sleep(random_number)
        # 返回上一个页面
        driver.back()
        time.sleep(random_number)

    time.sleep(2)
    # 网页内容
    content = driver.page_source
    # print(content)
except WebDriverException as e:
    print(f"WebDriverException occurred: {e}")
finally:
    # 确保在脚本结束前关闭浏览器
    driver.quit()



