import logging
from os.path import exists
from os import makedirs
import json
import asyncio
from pyppeteer import launch
from pyppeteer.errors import TimeoutError

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

# URL
index_url = 'https://spa2.scrape.center/page/{page}'
# 超时时间
time_out = 10
# 总页数
total_page = 10
# 指定数据保存路径，如果不存在则创建
results_dir = 'case_results'
exists(results_dir) or makedirs(results_dir)
# 设置窗口大小
window_width, window_height = 1366, 768

# 浏览器、选项卡，是否无头模式
browser, tab = None, None
headless = False

# 初始化 pyppeteer
async def init():
    global browser, tab
    browser = await launch(headless=headless, args=[f'--window-size={window_width},{window_height}'])
    tab = await browser.newPage()
    await tab.setViewport({'width': window_width, 'height': window_height})

# 通用爬虫
async def scrape_page(url, selector):
    logging.info('正在爬取：%s', url)
    try:
        await tab.goto(url)
        # 最多等待 10 秒钟，根据选择器匹配节点，否则报错
        await tab.waitForSelector(selector, options={
            'timeout': time_out * 1000
        })
    except TimeoutError:
        logging.error('error occurred while scraping %s', url, exc_info=True)

# 爬取列表页
async def scrape_index(page):
    url = index_url.format(page=page)
    await scrape_page(url, '.item .name')

# 解析列表页
async def parse_index():
    return await tab.querySelectorAllEval('.item .name', 'nodes => nodes.map(node => node.href)')

# 爬取详情页
async def scrape_detail(url):
    await scrape_page(url, 'h2')

# 解析详情页
async def parse_detail():
    url = tab.url
    name = await tab.querySelectorEval('h2', 'node => node.innerText')
    categories = await tab.querySelectorAllEval('.categories button span', 'nodes => nodes.map(node => node.innerText)')
    cover = await tab.querySelectorEval('.cover', 'node => node.src')
    score = await tab.querySelectorEval('.score', 'node => node.innerText')
    drama = await tab.querySelectorEval('.drama p', 'node => node.innerText')
    # 返回电影URL，电影名称，类别，封面，分数，简介
    return {
        'url': url,
        'name': name,
        'categories': categories,
        'cover': cover,
        'score': score,
        'drama': drama
    }

# 保存数据
async def save_data(data):
    # 为防止个别电影名称无法命名文件，将所有电影放到一个文件内
    # name = data.get('name')
    name = 'movies_pyppeteer'
    data_path = f'{results_dir}/{name}.json'
    json.dump(data, open(data_path, 'a', encoding='utf-8'), ensure_ascii=False, indent=2)

#
async def main():
    await init()
    try:
        for page in range(1, total_page + 1):
            await scrape_index(page)
            detail_urls = await parse_index()
            for detail_url in detail_urls:
                await scrape_detail(detail_url)
                detail_data = await parse_detail()
                logging.info('详情数据：%s', detail_data)
                await save_data(detail_data)
    finally:
        await browser.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
