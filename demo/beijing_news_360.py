import json
import time
import random
import requests
from lxml import etree
from urllib.parse import quote
from datetime import datetime

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

def get_one_page(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print('正在请求 -->', url)
        return response.text
    return None

def parse_one_page(text):
    # 直接读取文件进行解析
    # html = etree.parse('./beijing_news_360_temp.html', etree.HTMLParser())
    # 解析请求返回的内容
    html = etree.HTML(text)
    news_all = {}
    for i in range(1, 11):
        # 得到新闻的链接、标题和发布时间
        new_href = html.xpath(f'//*[@id="news"]/li[{i}]/a/@href')
        new_title = html.xpath(f'//*[@id="news"]/li[{i}]/a/@title')
        # 因为有的新闻时间是 3小时前 这种格式，需要换成当前的日期
        new_time = html.xpath(f'//*[@id="news"]/li[{i}]/a/div/div/p[2]/span//text()')
        # 获取当前时间
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 判断页面上有无发布时间，如果没有填为当前时间
        if new_time and new_time[0] is not None:
            new_time_join = current_time + '的' + new_time[0]
        else:
            new_time_join = current_time
        new_time_join_list = [new_time_join]
        # print(new_href, new_title, new_time_join_list)
        # 得到每条新闻的信息
        news_info = {
            '新闻链接': new_href[0],
            '新闻标题': new_title[0],
            '发布时间': new_time_join_list[0]
        }
        # 分别添加到字典中
        news_all[i] = news_info
    return news_all

def write_to_json(content):
    with open('./beijing_news_360.txt', 'a', encoding='utf-8') as file:
        file.write(json.dumps(content, ensure_ascii=False) + '\n')

def main(index):
    # https://news.so.com/ns?q=%E5%8C%97%E4%BA%AC
    # https://news.so.com/ns?q=%E5%8C%97%E4%BA%AC&pn=3&rank=rank&j=0&nso=10&tp=55&nc=0&src=page
    keyword = '北京'
    # 将搜索内容转化为URL编码格式
    base_url = 'https://news.so.com/ns?q=' + quote(keyword)
    url = base_url + f'&pn={index}&rank=rank&j=0&nso=10&tp=55&nc=0&src=page'
    text = get_one_page(url)
    items = parse_one_page(text)
    # 逐个保存新闻信息
    for item in items.values():
        print(item)
        write_to_json(item)

if __name__ == '__main__':
    # 每页10条，只取100条
    for i in range(1, 11):
        main(i)
        # 生成一个 2~12 之间的随机数
        random_number = random.randint(2, 12)
        time.sleep(random_number)
