import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

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
    driver.get('https://www.baidu.com')
    # 开启一个新的选项卡
    driver.execute_script("window.open()")
    print(driver.window_handles)
    # 切换到新的选项卡
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://www.taobao.com')
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    driver.get('https://python.org')
    time.sleep(1)
finally:
    # 关闭浏览器
    driver.quit()
