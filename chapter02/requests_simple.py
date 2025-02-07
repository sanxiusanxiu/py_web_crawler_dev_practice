import requests

response = requests.get('https://www.baidu.com/')
# 输出响应的类型
print(type(response))
# 输出状态码
print(response.status_code)
# 输出响应体的类型
print(type(response.text))
# 输出响应体内容
print(response.text)
# 输出Cookies
print(response.cookies)

# # get() 的方便之处在于一行代码就可以完成其他类型的请求
# response = requests.post('http://httpbin.org/post')
# response = requests.put('http://httpbin.org/put')
# response = requests.delete('http://httpbin.org/delete')
# response = requests.head('http://httpbin.org/head')
# response = requests.options('http://httpbin.org/get')
