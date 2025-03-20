from urllib.parse import urlparse

# 进行 URL 解析
result = urlparse('https://www.baidu.com/index.html;user?id=5#comment')

# <class 'urllib.parse.ParseResult'> ParseResult(
#    scheme='https',
#    netloc='www.baidu.com',
#    path='/index.html',
#    params='user',
#    query='id=5',
#    fragment='comment'
# )
print(type(result), result)

"""
介绍一下返回的结果
scheme='https' 代表协议
netloc='www.baidu.com' 代表域名
path='/index.html' 访问路径
params='user' 代表参数
query='id=5' 查询条件，一般用作GET请求的URL
fragment='comment' 代表锚点，用于定位页面的下拉位置
"""
