import requests

r = requests.get('https://www.baidu.com')
print(r.cookies)
# items() 将 RequestsCookieJar 类型的 Cookies 转换为由元组组成的列表
for key, value in r.cookies.items():
    print(key + '=' + value)
