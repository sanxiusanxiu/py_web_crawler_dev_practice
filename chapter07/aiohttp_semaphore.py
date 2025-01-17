import aiohttp
import asyncio

# 最大并发量
concurrency = 3
url = 'https://www.baidu.com/'

# 创建一个信号量对象
semaphore = asyncio.Semaphore(concurrency)
session = None

async def scrape_api():
    async with semaphore:
        print(f'Scraping {url}')
        async with session.get(url) as response:
            await asyncio.sleep(1)
            return await response.text()

async def main():
    global session
    session = aiohttp.ClientSession()
    scrape_index_tasks = [asyncio.ensure_future(scrape_api()) for _ in range(10)]
    await asyncio.gather(*scrape_index_tasks)

if __name__ == '__main__':
    asyncio.run(main())
