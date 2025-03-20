from elasticsearch import Elasticsearch
# 忽略警告
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Elasticsearch 服务器地址和端口
hosts = ["https://elastic:zvSxldH8H7ljHOqLuQU_@localhost:9200"]

# 创建 Elasticsearch 客户端实例
es = Elasticsearch(hosts=hosts, verify_certs=False)

result = es.indices.delete(index='news')
print(result)
