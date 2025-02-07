from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

# proxy = '59.54.238.198:22067'
proxy = '127.0.0.1'

# 使用ProxyHandler设置代理
proxy_handler = ProxyHandler({
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
})

# 使用build_opener方法创建一个Opener
opener = build_opener(proxy_handler)

try:
    # 调用Opener对象的open方法访问链接
    response = opener.open('https://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
