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

# 设置 ChromeDriver 的路径
chrome_driver_path = 'chromedriver.exe'
# 设置 Chrome 选项
chrome_options = Options()
# 最大化浏览器窗口
chrome_options.add_argument("--start-maximized")
# 创建 Service 对象，用于配置 ChromeDriver 服务的可执行路径
service = Service(executable_path=chrome_driver_path)
# 初始化 webdriver，指定使用的 ChromeDriver 服务以及配置的选项
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # 显式等待
    # driver.get('https://spa2.scrape.center/')
    driver.get('https://www.taobao.com/')
    wait = WebDriverWait(driver, 10)
    # presence_of_element_located 代表节点出现
    q = wait.until(EC.presence_of_element_located((By.ID, 'q')))
    # element_to_be_clickable 代表可点击
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
    print(q, button)
finally:
    # 关闭浏览器
    driver.quit()

"""
上面使用了节点出现、节点可点击两个等待条件，其实等待条件还有很多，如有需要自行百度

title_is，标题是某内容
title_contains，标题包含某内容
presence_of_element_located，节点出现，参数为节点的定位元组，如(By.ID, 'p')
visibility_of_element_located，节点可见，参数为节点的定位元组
visibility_of，可见，参数为节点对象
presence_of_all_elements_located，所有节点都出现
text_to_be_present_in_element，某个节点的文本值中包含某文字
text_to_be_present_in_element_value，某个节点值中包含某文字
frame_to_be_available_and_switch_to_it_frame，加载并切换
invisibility_of_element_located，节点不可见
element_to_be_clickable，按钮可点击
staleness_of，判断一个节点是否仍在 DOM 树中，可知页面是否已经刷新
element_to_be_selected，节点可选择，参数为节点对象
element_located_to_be_selected，节点可选择，参数为节点的定位元组
element_selection_state_to_be，参数为节点对象以及状态，相等返回 True，否则返回 False 
element_located_selection_state_to_be，参数为定位元组以及状态，相等返回 True，否则返回 False
alert_is_present，是否出现警告提示框
"""
