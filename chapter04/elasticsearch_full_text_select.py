from elasticsearch import Elasticsearch

hosts = ["https://elastic:zvSxldH8H7ljHOqLuQU_@localhost:9200"]
es = Elasticsearch(hosts=hosts, verify_certs=False)

# 使用 DSL 语句进行查询，使用 match 指定全文检索
dsl = {
    'query': {
        'match': {
            'title': '创造 哪吒'
        }
    }
}

result = es.search(index='news', body=dsl)
# '_score' 表示分数，越高表示越符合
print(result)
"""
{
	'took': 2,
	'timed_out': False,
	'_shards': {
		'total': 1,
		'successful': 1,
		'skipped': 0,
		'failed': 0
	},
	'hits': {
		'total': {
			'value': 2,
			'relation': 'eq'
		},
		'max_score': 3.9792352,
		'hits': [{
			'_index': 'news',
			'_id': 'Xy-C9JQBlzqLic7BJPO1',
			'_score': 3.9792352,
			'_source': {
				'title': '创造历史！哪吒为何这样火？',
				'url': 'https://news.qq.com/rain/a/20250211A00GYJ00'
			}
		}, {
			'_index': 'news',
			'_id': 'Yy-C9JQBlzqLic7BJPPT',
			'_score': 1.61033,
			'_source': {
				'title': '多地争给哪吒上“户口”',
				'url': 'https://news.qq.com/rain/a/20250211A038XE00'
			}
		}]
	}
}
"""
