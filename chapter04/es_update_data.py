from elasticsearch import Elasticsearch

es = Elasticsearch(hosts='https://localhost:9200', verify_certs=False)

data = {
    'title': '乘风破浪不负韶华，奋斗青春圆梦高考',
    'url': 'https://view.inews.qq.com/a/EDU2021041600732200',
    'date': '2021-07-05'
}

result = es.update(index='news', id='1', body=data)
print(result)
