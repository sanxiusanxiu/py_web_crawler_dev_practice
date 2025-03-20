from elasticsearch import Elasticsearch

hosts = ["https://elastic:zvSxldH8H7ljHOqLuQU_@localhost:9200"]
es = Elasticsearch(hosts=hosts, verify_certs=False)

data = {
    'title': '乘风破浪不负韶华，奋斗青春圆梦高考',
    'url': 'https://view.inews.qq.com/a/EDU2021041600732200',
    'date': '2021-07-05'
}

# 更新文档  # 文档更新成功：{'_index': 'news', '_id': '1', '_version': 2, 'result': 'updated', '_shards': {'total': 1, 'successful': 1, 'failed': 0}, '_seq_no': 1, '_primary_term': 1}
# '_version': 2, 'result': 'updated', 表示更新成功
if es.exists(index='news', id='1'):
    result = es.update(index='news', id='1', body={'doc': data})
    # 更新也可以使用 index 方法，这里不再介绍了
    print(f"文档更新成功：{result}")
else:
    print(f"文档 ID 不存在，无法更新。")
