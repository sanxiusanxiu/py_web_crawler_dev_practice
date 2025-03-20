import http.cookiejar
import urllib.request

cookies = http.cookiejar.MozillaCookieJar()
# 调用 load() 读取本地的 Cookies 文件
cookies.load('./urllib_handler_cookies.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookies)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
print(response.read().decode('utf-8'))
