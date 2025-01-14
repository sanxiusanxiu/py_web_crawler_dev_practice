from selenium import webdriver  # 导入selenium的webdriver模块
from selenium.webdriver.chrome.options import Options  # 导入用于配置Chrome浏览器选项的模块
from selenium.webdriver.chrome.service import Service  # 导入用于配置ChromeDriver服务的模块
from selenium.webdriver.common.by import By  # 导入用于定位元素的By类
from selenium.webdriver.common.keys import Keys  # 导入selenium的Keys模块，用于键盘操作
from selenium.webdriver.support.wait import WebDriverWait  # 导入用于显式等待的模块

# 设置用户代理
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

# 设置ChromeDriver的路径
chrome_driver_path = 'chromedriver.exe'
# 设置Chrome选项
chrome_options = Options()
# 最大化浏览器窗口
# chrome_options.add_argument("--start-maximized")
# 创建Service对象，用于配置ChromeDriver服务的可执行路径
service = Service(executable_path=chrome_driver_path)
# 初始化webdriver，指定使用的ChromeDriver服务以及配置的选项
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # 使用driver.get()方法打开百度首页
    driver.get('https://www.baidu.com')
    # 通过元素的ID定位到搜索框，并赋值给变量input
    input = driver.find_element(By.ID, 'kw')
    # 向搜索框中输入关键词 python
    input.send_keys('python')
    # 模拟键盘按Enter键，执行搜索
    input.send_keys(Keys.ENTER)

    # 创建WebDriverWait对象，设置最长等待时间为10秒
    wait = WebDriverWait(driver, 10)
    # 打印当前页面的URL
    print(driver.current_url)
    # 打印当前页面的cookies
    print(driver.get_cookies())
    # 打印当前页面的源代码
    print(driver.page_source)
finally:
    # 关闭浏览器
    driver.quit()