from selenium import webdriver
from selenium.webdriver.common.by import By

# 初始化浏览器对象
browser = webdriver.Chrome()
# 访问页面
browser.get('https://www.dushu.com/')
# print(browser.page_source)

# 查找单个节点
input_first = browser.find_element(by=By.NAME, value='qd')
input_second = browser.find_element(by=By.CLASS_NAME, value='wd')
input_third = browser.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[2]/form/div/input')
print(input_first, input_second, input_third)
# 查找多个节点，这个需要具体看一下网页内容
# li_s = browser.find_element(by=By.CSS_SELECTOR, value='.service-bd--LdDnWwA9 li')
# print(li_s)

browser.close()

