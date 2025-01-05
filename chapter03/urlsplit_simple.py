from urllib.parse import urlsplit

result = urlsplit('https://www.baidu.com/index.html;user?id=5#comment')
# SplitResult(scheme='https', netloc='www.baidu.com', path='/index.html;user', query='id=5', fragment='comment')
print(result)
# SplitResult是元组类型的
print(result[0])
print(result.scheme)
