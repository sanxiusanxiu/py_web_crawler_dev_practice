import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chromium.options import ChromiumOptions

# 设置ChromeDriver的路径
chrome_driver_path = 'chromedriver.exe'

# 设置Chrome选项
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# 创建Service对象，用于配置ChromeDriver服务的可执行路径
service = Service(executable_path=chrome_driver_path)

# 添加反爬虫策略
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_experimental_option('useAutomationExtension', False)

# 初始化webdriver，指定使用的ChromeDriver服务以及配置的选项
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # 使用CDP命令来规避某些网站的爬虫检测
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
    })

    # 访问目标网站
    driver.get('https://antispider1.scrape.center/')
    time.sleep(3)
finally:
    # 关闭浏览器
    driver.quit()
