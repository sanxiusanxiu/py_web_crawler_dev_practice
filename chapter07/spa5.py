import json
import aiohttp
import asyncio
import logging

from motor.motor_asyncio import AsyncIOMotorClient

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# https://spa5.scrape.center/api/book/?limit=18&offset=18
index_url = 'https://spa5.scrape.center/api/book/?limit=18&offset={offset}'
detail_url = 'https://spa5.scrape.center/api/book/{id}'

# 每页18本图书
page_book_number = 18
# 共100页
page_number = 100
# 并发量
concurrency = 3

# 数据库相关配置
from pymongo import MongoClient

client_string = 'mongodb://localhost:27017/'
client = AsyncIOMotorClient(client_string)
db = client['crawler']
collection = db['books_async']


semaphore = asyncio.Semaphore(concurrency)
session = None

# 列表页、详情页 通用爬取
async def scrape_api(url):
    # 引入信号量作为上下文
    async with semaphore:
        try:
            logging.info(f'Scraping {url}')
            # 请求网页，返回JSON数据
            async with session.get(url) as response:
                return await response.json()
        except aiohttp.ClientError:
            logging.error(f'Failed to scrape {url}', exc_info=True)

# 保存数据
async def save_data(data):
    logging.info(f'Saving data {data} to database')
    if data:
        return await collection.update_one({'id': data['id']}, {'$set': data}, upsert=True)

# 爬取列表页
async def scrape_index(page):
    url = index_url.format(offset=page_book_number * (page - 1))
    return await scrape_api(url)

# 爬取详情页
async def scrape_detail(id):
    url = detail_url.format(id=id)
    data = await scrape_api(url)
    await save_data(data)

async def main():
    global session
    session = aiohttp.ClientSession()
    scrape_index_tasks = [asyncio.ensure_future(scrape_index(page)) for page in range(1, page_number + 1)]
    results = await asyncio.gather(*scrape_index_tasks)
    logging.info('results: %s', json.dumps(results, ensure_ascii=False, indent=2))

    # 增加 results 解析
    id_list = []
    for index_data in results:
        if not index_data:
            continue
        for item in index_data.get('results'):
            id_list.append(item.get('id'))

    # 爬取详情页
    scrape_detail_tasks = [asyncio.ensure_future(scrape_detail(id)) for id in id_list]
    await asyncio.wait(scrape_detail_tasks)
    await session.close()

if __name__ == '__main__':
    asyncio.run(main())
