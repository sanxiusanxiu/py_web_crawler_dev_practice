from elasticsearch import Elasticsearch

es = Elasticsearch(hosts='https://localhost:9200', verify_certs=False)

result = es.indices.delete(index='news', ignore=[400, 404])
print(result)
