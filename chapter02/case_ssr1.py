import requests
import logging
import re
import json
from urllib.parse import urljoin
from os import makedirs
from os.path import exists

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

base_url = 'https://ssr1.scrape.center'
total_tag = 10

# 通用的爬取页面操作
def scrape_page(url):
    logging.info(f'正在爬取 %s... {url}')
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        logging.error(f'异常的响应码 {response.status_code} 在爬取 {url} 时')
    except requests.exceptions.RequestException as e:
        # 设置 exc_info=True 可以打印 Traceback 错误堆栈信息
        logging.error(f'在爬取 {url} 时发生错误', exc_info=True)

# 列表页的爬取
def scrape_index(page):
    index_url = f'{base_url}/page/{page}'
    return scrape_page(index_url)

# 详情页的爬取
def scrape_detail(url):
    return scrape_page(url)

# 解析列表页
def parse_index(html):
    # 提取超链接的正则
    pattern = re.compile(r'<a.*?href="(.*?)".*?class="name">')
    items = re.findall(pattern, html)
    if not items:
        return []
    for item in items:
        detail_url = urljoin(base_url, item)
        logging.info(f'获取详情页的链接 {detail_url}')
        yield detail_url

# 解析详情页
def parse_detail(html):
    # 封面
    cover_pattern = re.compile(r'class="item.*?<img.*?src="(.*?)".*?class="cover">', re.S)
    # 名称
    name_pattern = re.compile(r'<h2.*?>(.*?)</h2>', re.S)
    # 类别
    categories_pattern = re.compile(r'<button.*?category.*?<span>(.*?)</span>.*?</button>', re.S)
    # 上映时间
    published_at_pattern = re.compile(r'(\d{4}-\d{2}-\d{2})\s?上映', re.S)
    # 剧情简介
    drama_pattern = re.compile(r'<div.*?drama.*?>.*?<p.*?>(.*?)</p>', re.S)
    # 评分
    score_pattern = re.compile(r'<p.*?score.*?>(.*?)</p>', re.S)

    cover = re.search(cover_pattern, html).group(1).strip() if re.search(cover_pattern, html) else None
    name = re.search(name_pattern, html).group(1).strip() if re.search(name_pattern, html) else None
    categories = re.findall(categories_pattern, html) if re.findall(categories_pattern, html) else []
    published_at = re.search(published_at_pattern, html).group(1) if re.search(published_at_pattern, html) else None
    drama = re.search(drama_pattern, html).group(1).strip() if re.search(drama_pattern, html) else None
    score = re.search(score_pattern, html).group(1).strip() if re.search(score_pattern, html) else None
    print(cover, name, categories, published_at, drama, score)
    return {
        'cover': cover,
        'name': name,
        'categories': categories,
        'published_at': published_at,
        'drama': drama,
        'score': score
    }

# 指定数据保存路径，如果不存在则创建
results_dir = 'case_results'
exists(results_dir) or makedirs(results_dir)

def save_data(data):
    # 获取数据中的 电影名称，将其作为文件名
    # name = data.get('name')
    # 20250114 不再分开存放，会导致部分电影数据缺失
    name = 'movies'
    data_path = f'{results_dir}/{name}.json'
    json.dump(data, open(data_path, 'a', encoding='utf-8'), ensure_ascii=False, indent=4)

# 可使用多进程加速爬取，见下
def main():
    for page in range(1, total_tag + 1):
        index_html = scrape_index(page)
        detail_urls = parse_index(index_html)
        for detail_url in detail_urls:
            detail_html = scrape_detail(detail_url)
            data = parse_detail(detail_html)
            logging.info(f'获取到详情页信息 {data}')
            logging.info('保存数据中 ...')
            save_data(data)
            logging.info('数据保存成功')

if __name__ == '__main__':
    main()

'''
# 多进程加速
import multiprocessing

def main(page):
    index_html = scrape_index(page)
    detail_urls = parse_index(index_html)
    for detail_url in detail_urls:
        detail_html = scrape_detail(detail_url)
        data = parse_detail(detail_html)
        logging.info(f'get detail data {data}')
        logging.info('saving data to json file')
        save_data(data)
        logging.info('data saved successfully')

if __name__ == '__main__':
    # 声明一个进程池，进程池的大小根据 CPU 核数决定
    pool = multiprocessing.Pool()
    # 遍历所有的页码
    pages = range(1, total_tag + 1)
    pool.map(main, pages)
    pool.close()
    pool.join()
'''