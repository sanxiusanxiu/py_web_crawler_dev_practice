import urllib.request

request = urllib.request.Request('https://python.org')
# 虽然还是使用 urlopen() 来发送请求，但是这次的参数是一个 Request 类型的对象
# 这样做一方面可以将请求独立成一个对象，另一方面可以更加灵活地配置参数
response = urllib.request.urlopen(request)

print(response.read().decode('utf-8'))
