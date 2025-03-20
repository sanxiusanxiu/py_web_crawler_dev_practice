import requests

def requests_response():
    r = requests.get('https://www.baidu.com')
    print(type(r.status_code), r.status_code)
    print(type(r.headers), r.headers)
    print(type(r.cookies), r.cookies)
    print(type(r.url), r.url)
    print(type(r.history), r.history)
    # 内置的状态码检查对象  # 例如 404 可以使用 requests.codes.not_found 来比对，更多种类的返回码见下
    exit() if not r.status_code == requests.codes.ok else print('请求成功')

requests_response()

"""
1xx - 信息性状态码
100 Continue: 服务器已经接收到请求头，客户端可以继续发送请求体
101 Switching Protocols: 服务器正在根据客户端的请求切换协议

2xx - 成功状态码
200 OK: 请求成功，服务器返回了请求的资源
201 Created: 请求已成功，并且服务器创建了新的资源
204 No Content: 请求成功，但服务器没有返回任何内容
206 Partial Content: 服务器成功处理了部分 GET 请求

3xx - 重定向状态码
301 Moved Permanently: 请求的资源已被永久移动到新位置
302 Found: 请求的资源临时移动到了另一个位置
303 See Other: 服务器发送这个状态码来指示客户端应该使用GET方法访问另一个 URL
304 Not Modified: 资源未修改，可以使用缓存的内容
307 Temporary Redirect: 请求的资源临时移动到了另一个位置，但客户端应该继续使用原始的请求方法

4xx - 客户端错误状态码
400 Bad Request: 服务器无法理解请求的格式
401 Unauthorized: 请求需要用户认证
403 Forbidden: 服务器理解请求，但拒绝执行
404 Not Found: 请求的资源在服务器上不存在
405 Method Not Allowed: 请求的方法不被允许

5xx - 服务器错误状态码
500 Internal Server Error: 服务器遇到了一个意外的情况，阻止它完成请求
501 Not Implemented: 服务器不支持请求的功能
502 Bad Gateway: 服务器作为网关或代理，从上游服务器收到了无效的响应
503 Service Unavailable: 服务器目前无法处理请求，通常是服务器过载或维护
504 Gateway Timeout: 服务器作为网关或代理，没有及时从上游服务器收到响应
"""
