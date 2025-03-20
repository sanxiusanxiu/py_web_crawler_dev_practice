from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# 设置 ChromeDriver 的路径
chrome_driver_path = 'chromedriver.exe'
# 设置 Chrome 选项
chrome_options = Options()
# 无头模式
chrome_options.add_argument('--headless')
# 最大化浏览器窗口
# chrome_options.add_argument('--start-maximized')
# 创建 Service 对象，用于配置 ChromeDriver 服务的可执行路径
service = Service(executable_path=chrome_driver_path)
# 初始化 webdriver，指定使用的 ChromeDriver 服务以及配置的选项
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.set_window_size(1080, 720)
    driver.get('https://www.baidu.com/')
    # 输出页面截图
    driver.get_screenshot_as_file('selenium_headless_screenshot.png')
    driver.close()
finally:
    # 关闭浏览器
    driver.quit()
