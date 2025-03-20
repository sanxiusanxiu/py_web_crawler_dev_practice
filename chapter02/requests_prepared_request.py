from requests import Request, Session

url = 'https://httpbin.org/post'
data = {'name': 'John'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
}

s = Session()
# 构造 Request 对象
request = Request('POST', url, data=data, headers=headers)
# 将 Request 对象转换成 Prepared Request 对象
prepped = s.prepare_request(request)

# 发送请求
response = s.send(prepped)
print(response.text)
