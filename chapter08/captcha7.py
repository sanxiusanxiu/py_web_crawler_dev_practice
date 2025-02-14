import time
import re
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from PIL import Image
from io import BytesIO
import numpy as np
from retrying import retry

# 对验证码图片进行去噪操作
def preprocess(image):
    image = image.convert('L')
    array = np.array(image)
    # 经过调试使用 150 作为阈值比较合适
    array = np.where(array > 150, 255, 0)
    image = Image.fromarray(array.astype('uint8'))
    # image.show()
    return image

# 设置重试，确保某次识别出错也能反复测试
@retry(stop_max_attempt_number=5, retry_on_result=lambda x:x is False)
def login():
    # 打开网站
    browser.get('https://captcha7.scrape.center/')
    # 输入用户名和密码
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, '.username input[type="text"]').send_keys('admin')
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, '.password input[type="password"]').send_keys('admin')
    # 找到验证码图片
    time.sleep(1)
    captcha = browser.find_element(By.CSS_SELECTOR, '#captcha')
    # 转化成图片对象
    image = Image.open(BytesIO(captcha.screenshot_as_png))
    # 去噪
    image = preprocess(image)
    # 识别
    captcha = pytesseract.image_to_string(image)
    # 去除识别结果中的非字母、非数字字符
    captcha = re.sub('[^A-Za-z0-9]', '', captcha)
    # 输入验证码结果
    time.sleep(1)
    print('验证码：', captcha)
    browser.find_element(By.CSS_SELECTOR, '.captcha input[type="text"]').send_keys(captcha)
    # 登录
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, '.login').click()
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//h2[contains(., "登录成功")]')))
        time.sleep(10)
        browser.close()
        return True
    except TimeoutException:
        return False

if __name__ == '__main__':
    chrome_driver_path = '../chapter07/chromedriver.exe'
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service(executable_path=chrome_driver_path)
    browser = webdriver.Chrome(service=service, options=chrome_options)
    #
    login()
