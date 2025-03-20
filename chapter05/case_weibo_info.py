import time
from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq

base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

# 构造参数字典，其中 type、value、containerid 是固定参数，page 是可变参数
def get_page(page):
    params = {
        'type': 'uid',
        'value': '',
        'containerid': '',
        'page': page
    }
    # 将参数转化成 类似于 type=uid&value=2145291155&containerid=1076032145291155&page=2 的形式
    url = base_url + urlencode(params)
    try:
        # 发送请求
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print('请求成功 --> ', url)
            # 如果请求成功，直接调用 json 方法将内容解析为 JSON
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)

# 定义一个解析方法，从结果中提取想要的信息，比如微博的 id、正文、点赞数、评论数和转发数
def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            # 创建字典
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comments_count')
            weibo['reposts'] = item.get('reposts_count')
            yield weibo

# 将结果保存到 MongoDB 数据库
def page_to_mongodb(results):
    import pymongo
    from pymongo import MongoClient
    # 连接 MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    # 指定数据库
    db = client['crawler']
    # 指定集合（表）
    collection = db['weibo_info']
    insert_info = collection.insert_many(results)
    print(insert_info)

if __name__ == '__main__':
    for page in range(1, 11):
        json = get_page(page)
        results = parse_page(json)
        print('存储中...')
        page_to_mongodb(results)
        time.sleep(13)
