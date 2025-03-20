import time
from elasticsearch import Elasticsearch
# 忽略警告
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

hosts = ["https://elastic:zvSxldH8H7ljHOqLuQU_@localhost:9200"]
es = Elasticsearch(hosts=hosts, verify_certs=False)

# 设置映射信息
mapping = {
    'properties': {
        'title': {
            'type': 'text',  # 类型
            'analyzer': 'ik_max_word',  # 分词器
            'search_analyzer': 'ik_max_word'  # 搜索分词器
        }
    }
}

# 删除之前的索引
es.indices.delete(index='news', ignore=[400, 404])
es.indices.create(index='news', ignore=400)
result = es.indices.put_mapping(index='news', body=mapping)
print(result)

# 插入几条新数据
time.sleep(3)
datas = [
    {
        'title': '推动新时代东北全面振兴 总书记寄予厚望',
        'url': 'https://news.qq.com/rain/a/20250210A08UDO00'
    },
    {
        'title': '创造历史！哪吒为何这样火？',
        'url': 'https://news.qq.com/rain/a/20250211A00GYJ00'
    },
    {
        'title': '公司要求员工就董事长讲话写心得',
        'url': 'https://news.qq.com/rain/a/20250211A05RO000'
    },
    {
        'title': '重点领域消费品以旧换新销量显著增长',
        'url': 'https://news.qq.com/rain/a/20250210A05L1U00'
    },
    {
        'title': '中方移除了钓鱼岛周边的浮标？',
        'url': 'https://news.qq.com/rain/a/20250211A05G4S00'
    },
    {
        'title': '多地争给哪吒上“户口”',
        'url': 'https://news.qq.com/rain/a/20250211A038XE00'
    },
    {
        'title': '马云现身阿里杭州总部',
        'url': 'https://news.qq.com/rain/a/20250211A0417E00'
    },
    {
        'title': '东北虎咬死同伴在雪地上拖行？',
        'url': 'https://news.qq.com/rain/a/20250211A056MQ00'
    },
    {
        'title': 'A股震荡调整 超3400股飘绿',
        'url': 'https://news.qq.com/rain/a/20250211A05NUI00'
    },
    {
        'title': '百名乘客飞抵雅加达 行李被落在广州',
        'url': 'https://news.qq.com/rain/a/20250211A04FM300'
    }
]
for data in datas:
    es.index(index='news', body=data)
# 查询索引中的内容
time.sleep(3)
result = es.search(index='news')
print(result)
