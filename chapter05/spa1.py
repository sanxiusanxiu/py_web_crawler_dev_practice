import requests
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# https://spa1.scrape.center/api/movie/?limit=10&offset=10
# index_url = 'https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'
limit = 10
total_page = 10

# 爬取页面
def scrape_api(url):
    logging.info(f'Scraping %s... {url}')
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # 解析响应内容并转换成JSON
            return response.json()
        logging.error(f'get invalid status code {response.status_code} while scraping {url}')
    except requests.exceptions.RequestException as e:
        # 设置 exc_info=True 可以打印 Traceback 错误堆栈信息
        logging.error(f'error occurred while scraping {url}', exc_info=True)

# 列表页的爬取
def scrape_index(page):
    url = f'https://spa1.scrape.center/api/movie/?limit={limit}&offset={limit * (page - 1)}'
    return scrape_api(url)

# 详情页的爬取
def scrape_detail(id):
    url = f'https://spa1.scrape.center/api/movie/{id}'
    return scrape_api(url)

# 保存数据
from pymongo import MongoClient

# 连接MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['crawler']
collection = db['movies_ajax']

def save_data(data):
    # 存在即更新，不存在就插入
    collection.update_one({'name': data.get('name')}, {'$set': data}, upsert=True)

def main():
    for page in range(1, total_page + 1):
        index_data = scrape_index(page)
        for item in index_data.get('results'):
            id = item.get('id')
            detail_data = scrape_detail(id)
            logging.info(f'detail_data: {detail_data}')
            save_data(detail_data)
            logging.info('data saved successfully')
            time.sleep(1)

if __name__ == '__main__':
    main()
