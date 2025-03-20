from urllib.parse import urlsplit

result = urlsplit('https://www.baidu.com/index.html;user?id=5#comment')
# SplitResult(scheme='https', netloc='www.baidu.com', path='/index.html;user', query='id=5', fragment='comment')
print(result)

# SplitResult是元组类型的，可以使用属性名或者索引来取值
print(result[0])
print(result.scheme)
