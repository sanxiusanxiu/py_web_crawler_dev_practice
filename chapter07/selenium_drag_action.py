import time
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
    # 打开拖拽操作的网址
    url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    driver.get(url)

    # 切换到 iframe
    driver.switch_to.frame('iframeResult')

    # 定位到可拖拽的元素和目标元素
    source = driver.find_element(By.CSS_SELECTOR, '#draggable')
    target = driver.find_element(By.CSS_SELECTOR, '#droppable')

    # 创建 ActionChains 对象
    actions = ActionChains(driver)

    # 执行拖拽操作
    actions.drag_and_drop(source, target).perform()

    # 等待几秒查看效果
    time.sleep(3)

finally:
    # 关闭浏览器
    driver.quit()
