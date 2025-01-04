from selenium import webdriver
from selenium.webdriver.firefox.service import Service

# 指定GeckoDriver的路径
gecko_path = './geckodriver.exe'

# 创建Service对象
service = Service(gecko_path)

# 初始化火狐浏览器驱动
driver = webdriver.Firefox(service=service)

try:
    # 打开一个网页
    driver.get('https://www.mozilla.org')

    # 打印网页标题
    print(driver.title)
finally:
    # 关闭浏览器
    driver.quit()
