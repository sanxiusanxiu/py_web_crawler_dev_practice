from urllib.parse import urlparse

# 进行URL解析
result = urlparse('https://www.baidu.com/index.html;user?id=5#comment')
# 输出返回结果
print(type(result), result)

'''
剖析一下返回的结果
scheme='https' 代表协议
netloc='www.baidu.com' 代表域名
path='/index.html' 访问路径
params='user' 代表参数
query='id=5' 查询条件，一般用作GET请求的URL
fragment='comment' 代表锚点，用于定位页面的下拉位置
'''
