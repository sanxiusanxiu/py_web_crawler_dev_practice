from elasticsearch import Elasticsearch

es = Elasticsearch(hosts='https://localhost:9200', verify_certs=False)
# ignore=400 表示忽略因为索引已存在而创建失败的情况
result = es.indices.create(index='news', ignore=400)
print(result)

