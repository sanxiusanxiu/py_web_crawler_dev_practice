from elasticsearch import Elasticsearch

hosts = ["https://elastic:zvSxldH8H7ljHOqLuQU_@localhost:9200"]
es = Elasticsearch(hosts=hosts, verify_certs=False)

result = es.delete(index='news', id='1')
# {'_index': 'news', '_id': '1', '_version': 3, 'result': 'deleted', '_shards': {'total': 1, 'successful': 1, 'failed': 0}, '_seq_no': 2, '_primary_term': 1}
# '_version': 3, 'result': 'deleted', 表示删除成功
print(result)
