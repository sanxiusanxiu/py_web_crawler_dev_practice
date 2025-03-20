from elasticsearch import Elasticsearch
# 忽略警告
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

hosts = ["https://elastic:zvSxldH8H7ljHOqLuQU_@localhost:9200"]
es = Elasticsearch(hosts=hosts, verify_certs=False)

index_name = 'news'
data = {
    'title': '乘风破浪不负韶华，奋斗青春圆梦高考',
    'url': 'https://view.inews.qq.com/a/EDU2021041600732200'
}

result = es.create(index='news', id='1', body=data)
# 也可以使用 insert 方法，使用 insert 时不用指定 id
# result = es.index(index='news', body=data)

# {'_index': 'news', '_id': '1', '_version': 1, 'result': 'created', '_shards': {'total': 2, 'successful': 1, 'failed': 0}, '_seq_no': 0, '_primary_term': 1}
# 'result': 'created' 表示数据插入成功
print(result)
