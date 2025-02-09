from elasticsearch import Elasticsearch

es = Elasticsearch(hosts='https://localhost:9200', verify_certs=False)

result = es.delete(index='news', id='1')
print(result)
