import json
import time
import random
import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

def get_one_page(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None

def parse_one_page(html):
    pattern = re.compile(r'<dd>.*?<i class="board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>', re.S)
    # 查找所有匹配项
    items = pattern.findall(html)
    # 打印提取的信息
    for item in items:
        rank, image_src, movie_name, stars, release_time, score_integer, score_fraction = item
        # 对于不太干净的数据清洗一下
        stars = stars.split('：')[-1]
        stars_2 = stars.split('\n')[0]
        release_time = release_time.split('：')[-1]
        print(f"电影排名：{rank}")
        print(f"图片链接：{image_src}")
        print(f"电影名称：{movie_name}")
        print(f"主要演员：{stars_2}")
        print(f"上映时间：{release_time}")
        print(f"猫眼评分：{score_integer}{score_fraction}")
        print('-' * 40)
        # 电影信息
        """
        yield 的作用是使这个函数成为一个生成器（generator），而不是返回一个列表
        每次循环迭代时，yield 会返回一个字典，其中包含当前迭代的电影的名称、类型、国家、时长、上映时间和评分
        然后生成器会暂停执行，保存当前的执行状态
        当外部代码再次请求生成器的下一个值时，生成器会从上次暂停的地方继续执行，直到再次遇到 yield
        """
        yield {
            'rank': rank,
            'image_src': image_src,
            'movie_name': movie_name,
            'stars': stars_2,
            'release_time': release_time,
            'score_integer': score_integer + score_fraction
        }

def write_to_file(content):
    with open('maoyan_movie_info.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

def main(offset):
    url = 'https://www.maoyan.com/board/4?offset=' + str(offset)
    # print('--->' + url)
    html = get_one_page(url)
    for item in parse_one_page(html):
        # print(item)
        write_to_file(item)

if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        # 生成一个 12~99 之间的随机数
        random_number = random.randint(12, 99)
        time.sleep(random_number)
