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
chrome_options.add_argument('--headless')
# 最大化窗口
chrome_options.add_argument("--start-maximized")
# 创建Service对象
service = Service(executable_path=chrome_driver_path)

# 保存路径，如果不存在则创建
results_dir = './VUL'
exists(results_dir) or makedirs(results_dir)

try:
    # 初始化webdriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    # 生成一个 12~29 之间的随机数
    # random_number = random.randint(12, 29)
    # print(f'{random_number}-- 123 --')
    # 打开0day首页
    driver.get('https://0day.today/')
    time.sleep(4)
    # 语言选择
    select_language_a = driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[12]/div[2]/a[12]')
    select_language_a.click()
    time.sleep(6)
    select_language_input = driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[14]/div[3]/form/input')
    select_language_input.click()
    time.sleep(5)
    # 内页的弹窗
    select_inner_close = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div/a')
    if select_inner_close is not None:
        select_inner_close.click()
    # 获取到首页的10~84个条目
    for index in [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84]:
        # 可以加一个判断
        # tail_url = driver.find_element(by=By.XPATH, value=f'/html/body/div[2]/div[{index}]/div[2]/h3/a//@href')
        # 假设index是已经定义好的变量
        tail_url = driver.find_element(by=By.XPATH, value=f'/html/body/div[2]/div[{index}]/div[2]/h3/a').get_attribute('href')
        exploit_id = tail_url.split('/')[-1]
        print(exploit_id)
        loop_click_a = driver.find_element(by=By.XPATH, value=f'/html/body/div[2]/div[{index}]/div[2]/h3/a')
        loop_click_a.click()
        exploit_source = driver.page_source
        # 将源代码写入HTML文件
        file_name = results_dir + '0Day-ID-' + str(exploit_id) + '.html'
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(exploit_source)
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

