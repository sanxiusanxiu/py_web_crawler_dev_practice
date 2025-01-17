import json
import time
import random
import requests
from lxml import etree


# https://ssr1.scrape.center/page/2
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
    # html = etree.parse('./ssr1_temp.html', etree.HTMLParser())
    # 解析请求返回的内容
    html = etree.HTML(text)
    # 每个页面有10部电影
    movies = {}
    for i in range(1, 11):
        movie_name = html.xpath(f'//*[@id="index"]/div[1]/div[1]/div[{i}]/div/div/div[2]/a/h2//text()')
        movie_categories = html.xpath(f'//*[@id="index"]/div[1]/div[1]/div[{i}]/div/div/div[2]/div[1]/button/span//text()')
        movie_nation = html.xpath(f'//*[@id="index"]/div[1]/div[1]/div[{i}]/div/div/div[2]/div[2]/span[1]//text()')
        movie_duration = html.xpath(f'//*[@id="index"]/div[1]/div[1]/div[{i}]/div/div/div[2]/div[2]/span[3]//text()')
        movie_online = html.xpath(f'//*[@id="index"]/div[1]/div[1]/div[{i}]/div/div/div[2]/div[3]/span//text()')
        movie_score = html.xpath(f'//*[@id="index"]/div[1]/div[1]/div[{i}]/div/div/div[3]/p[1]//text()')
        # movie_score需要简单清洗一下  # 使用列表推导式和replace()方法去除\r、\n和空格
        score_clean = [item.replace('\r', '').replace('\n', '').strip() for item in movie_score]
        # 得到每部电影的信息
        movie_info = {
            '名称': movie_name,
            '分类': movie_categories,
            '国家': movie_nation,
            '时长': movie_duration,
            '上映': movie_online,
            '评分': score_clean
        }
        # 将10部电影信息分别添加到字典中
        movies[i] = movie_info
    return movies

def write_to_json(content):
    with open('ssr1_data.txt', 'a', encoding='utf-8') as file:
        file.write(json.dumps(content, ensure_ascii=False) + '\n')

def main(index):
    # https://ssr1.scrape.center/page/2
    url = 'https://ssr1.scrape.center/page/' + str(index)
    text = get_one_page(url)
    items = parse_one_page(text)
    # 逐个保存电影信息
    for item in items.values():
        print(item)
        write_to_json(item)

if __name__ == '__main__':
    # 每页10部，共100部电影
    for i in range(1, 11):
        main(i)
        # 生成一个 2~12 之间的随机数
        random_number = random.randint(2, 12)
        time.sleep(random_number)
