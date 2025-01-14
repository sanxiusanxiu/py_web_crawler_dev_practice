import random
import time

import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

chrome_driver_path = './chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
service = Service(executable_path=chrome_driver_path)
try:
    driver = webdriver.Chrome(service=service, options=chrome_options)
    # 生成一个 2~9 之间的随机数
    random_number = random.randint(2, 9)
    # print(f'{random_number}-- 123 --')
    #
    ip_list = ['42.81.169.37', ]
    for ip in ip_list:
        # 打开  首页
        driver.get('https://www.shodan.io/')
        time.sleep(random_number)
        input = driver.find_element(by=By.XPATH, value='//*[@id="search-query"]')
        input.send_keys(ip)
        time.sleep(random_number)
        # 内页的弹窗
        # select_inner_close = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div/a')
        # if select_inner_close is not None:
        #     select_inner_close.click()

    # 网页内容
    content = driver.page_source
    print(content)
except WebDriverException as e:
    print(f"WebDriverException occurred: {e}")
finally:
    # 确保在脚本结束前关闭浏览器
    driver.quit()
#
# # 根据网页找链接
# html = etree.HTML(content)
# print(html)
# # https://cn.0day.today/exploit/description/39338
# base_url = 'https://cn.0day.today'
# url_tail_list = html.xpath('//h3/a/@href')
# for url_tail in url_tail_list:
#     # print(url_tail)
#     url = base_url + url_tail
#     file_name = '0Day-ID-' + url_tail.split('/')[-1] + '.html'
#     html = requests.get(url, headers=headers)
#     time.sleep(random_number)
#     with open(file_name, 'w', encoding='utf-8') as f:
#         f.write(content)
#     f.close()
#     print(f'{url}，获取漏洞详情成功')
#
# import json
# import time
# import random
# import requests
# from lxml import etree
#
# #
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
# }
#
# # ip_list = ['42.81.169.37', ]
# # base_url = 'https://www.shodan.io/host/'
# # for ip in ip_list:
# #     url = base_url + ip
# #     response = requests.get(url, headers=headers)
# #     if response.status_code == 200:
# #         print('正在请求 -->', url)
# #         print(response.text)
#
# # 直接读取文件进行解析
# html = etree.parse('./shodan_temp.html', etree.HTMLParser())
# hostname = html.xpath('//*[@id="host"]/div[2]/div[1]/div/table/tbody/tr[1]/td[2]//text()')
# print(hostname)

# # 解析请求返回的内容
# html = etree.HTML(text)
# movie_name = html.xpath('//h2//text()')
# movie_categories = html.xpath('//*[@id="index"]/div[1]/div[1]/div/div/div/div[2]/div//text()')
# movie_nation = html.xpath('//*[@id="index"]/div[1]/div[1]/div/div/div/div[2]/div[2]/span[1]//text()')
# movie_duration = html.xpath('//*[@id="index"]/div[1]/div[1]/div/div/div/div[2]/div[2]/span[3]//text()')
# movie_online = html.xpath('//*[@id="index"]/div[1]/div[1]/div/div/div/div[2]/div[3]/span//text()')
# movie_score = html.xpath('//*[@id="index"]/div[1]/div[1]/div/div/div/div[3]/p[1]//text()')
# # print(movie_name)
# # movie_categories 和 movie_score 需要简单清洗一下
# # 使用列表推导式和replace()方法去除\r、\n和空格
# movie_categories_pre = [item.replace('\r', '').replace('\n', '').strip() for item in movie_categories]
# score_clean = [item.replace('\r', '').replace('\n', '').strip() for item in movie_score]
# all_categories = ''
# for i in movie_categories_pre:
#     # 将替换后的、符合要求的内容拼接到一起
#     if (len(i) == 2) or (i == '/'):
#         i_sep = i + '、'
#         all_categories += i_sep
# # 得到电影分类
# categories_clean = all_categories.split('、/、')
# '''
# yield 的作用是使这个函数成为一个生成器（generator），而不是返回一个列表
# 每次循环迭代时，yield 会返回一个字典，其中包含当前迭代的电影的名称、类型、国家、时长、上映时间和评分
# 然后生成器会暂停执行，保存当前的执行状态
# 当外部代码再次请求生成器的下一个值时，生成器会从上次暂停的地方继续执行，直到再次遇到 yield
# '''
# for i in range(len(movie_name)):
#     print(i)
#     # yield {
#     #     '名称': movie_name[i],
#     #     '类型': categories_clean[i],
#     #     '国家': movie_nation[i],
#     #     '时长': movie_duration[i],
#     #     '上映时间': movie_online[i],
#     #     '电影评分': score_clean[i]
#     # }


