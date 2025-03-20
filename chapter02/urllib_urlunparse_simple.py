from urllib.parse import urlunparse

# 也可以使用元组或其他的数据结构
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
# http://www.baidu.com/index.html;user?a=6#comment
print(urlunparse(data))
