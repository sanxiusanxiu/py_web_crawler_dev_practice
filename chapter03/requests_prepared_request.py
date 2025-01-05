from requests import Request, Session

url = 'https://httpbin.org/post'

data = {
    'name': 'germey',
}

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHML, like Gecko) '
                      'Chrome/52.0.2743.116 Safari/537.36',
}

s = Session()
# 构造Request对象
request = Request('POST', url, data=data, headers=headers)
# 将Request对象转换成Prepared Request对象
prepped = s.prepare_request(request)

# 发送
r = s.send(prepped)
print(r.text)
