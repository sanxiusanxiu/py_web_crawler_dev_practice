import time
import logging
import json

from urllib.parse import urljoin

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

index_url = 'https://spa2.scrape.center/page/{page}'
time_out = 10
total_page = 10

chrome_driver_path = 'chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--start-maximized')
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, time_out)

def scrape_page(url, condition, locator):
    """
    通用爬虫

    :param url: 需要爬取的页面
    :param condition: 页面加载成功的判断条件
    :param locator: 定位器
    :return:
    """
    logging.info(f'Scraping {url}')
    try:
        driver.get(url)
        wait.until(condition(locator))
    except TimeoutException:
        logging.info(f'Timed out {url}', exc_info=True)

# 爬取列表页
def scrape_index(page):
    url = index_url.format(page=page)
    # visibility_of_all_elements_located 所有节点都加载出来后才算成功
    scrape_page(url, condition=EC.visibility_of_all_elements_located, locator=(By.CSS_SELECTOR, '#index .item'))

# 爬取详情页
def scrape_detail(url):
    # visibility_of_element_located 单个元素出现即可
    scrape_page(url, condition=EC.visibility_of_element_located, locator=(By.TAG_NAME, 'h2'))

# 解析列表页
def parse_index():
    # 获取列表页中的所有电影节点
    elements = driver.find_elements(By.CSS_SELECTOR, '#index .item .name')
    for element in elements:
        href = element.get_attribute('href')
        # 拼接出电影详情页
        yield urljoin(index_url, href)

# 解析详情页
def parse_detail():
    url = driver.current_url
    name = driver.find_element(By.TAG_NAME, 'h2').text
    categories = [element.text for element in driver.find_elements(By.CSS_SELECTOR, '.categories button span')]
    cover = driver.find_element(By.CSS_SELECTOR, '.cover').get_attribute('src')
    score = driver.find_element(By.CLASS_NAME, 'score').text
    drama = driver.find_element(By.CSS_SELECTOR, '.drama p').text

    return {
        'url': url,
        'name': name,
        'categories': categories,
        'cover': cover,
        'score': score,
        'drama': drama
    }

from os import makedirs
from os.path import exists

# 指定数据保存路径，如果不存在则创建
results_dir = 'results'
exists(results_dir) or makedirs(results_dir)

def save_data(data):
    # 存储电影信息
    name = 'movies'
    data_path = f'{results_dir}/{name}.json'
    json.dump(data, open(data_path, 'a', encoding='utf-8'), ensure_ascii=False, indent=4)

def main():
    try:
        for page in range(1, total_page + 1):
            scrape_index(page)
            detail_urls = parse_index()
            for detail_url in list(detail_urls):
                logging.info(f'get detail url {detail_url}')
                scrape_detail(detail_url)
                detail_data = parse_detail()
                logging.info(f'detail data {detail_data}')
                data = parse_detail()
                logging.info('saving data to json file')
                save_data(data)
                logging.info('data saved successfully')
    finally:
        driver.close()
    time.sleep(9)
    driver.quit()

if __name__ == '__main__':
    main()
