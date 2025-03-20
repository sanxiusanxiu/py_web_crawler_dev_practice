from urllib import request, parse

"""
class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)

data 参数，必须是字节流类型（bytes）的，如果是字典则需要使用 urllib.parse 模块中的 urlencode() 编码
headers 参数，是一个字典，就是请求头，请求头最常用的就是修改 User-Agent 来伪装浏览器，默认是 Python-urllib
origin_req_host 参数，请求方的 host 或者 IP
unverifiable 参数，表示这个请求是否无法验证（通常用于从本地缓存中读取数据）
method 参数，用来指示请求使用的方法，如 GET、POST、PUT
"""

url = 'https://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5l Windows NT)',
    'Host': 'httpbin.org'
}
dic = {
    'name': 'Germey'
}
data = bytes(parse.urlencode(dic), encoding='utf8')

req = request.Request(url=url, data=data, headers=headers, method='POST')
# 还可以使用 add_header() 添加 Headers 内容
# req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5l Windows NT)')

response = request.urlopen(req)

print(response.read().decode('utf-8'))
