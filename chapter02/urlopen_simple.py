import urllib.request

# 向Python官网发送请求
response = urllib.request.urlopen('https://www.python.org')

# 响应的类型： <class 'http.client.HTTPResponse'>
print('响应的类型：', type(response))
