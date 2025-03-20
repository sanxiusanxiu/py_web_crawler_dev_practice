from elasticsearch import Elasticsearch
import urllib3

# 忽略警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Elasticsearch 服务器地址和端口
hosts = ["https://elastic:zvSxldH8H7ljHOqLuQU_@localhost:9200"]

# 创建 Elasticsearch 客户端实例
es = Elasticsearch(hosts=hosts, verify_certs=False)

# 索引名称
index_name = 'news'
# 索引配置
settings = {
    "settings": {
        "number_of_shards": 1,  # 设置主分片数量
        "number_of_replicas": 0  # 设置副本数量
    },
    "mappings": {
        "properties": {
            "title": {
                "type": "text"
            },
            "url": {
                "type": "keyword"
            },  # 网址通常作为关键词
            "date": {
                "type": "date"
            }
        }
    }
}

# 创建索引
if not es.indices.exists(index=index_name):
    response = es.indices.create(index=index_name, body=settings)
    print(f"索引创建成功，响应: {response}")
else:
    print(f"索引 {index_name} 已经存在。")
