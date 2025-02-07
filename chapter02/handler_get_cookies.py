import http.cookiejar
import urllib.request


def get_cookies():
    cookie = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('https://www.baidu.com')
    for item in cookie:
        print(item.name + '=' + item.value)


def get_cookies_file():
    file_path = 'cookies.txt'
    # MozillaCookieJar 用于读取和保存Cookies，会保存为 Mozilla 类型浏览器的 Cookies 格式
    cookie = http.cookiejar.MozillaCookieJar(file_path)
    # 另外 LWPCookieJar 也可以读取和保存Cookies，会保存为 libwww-perl(LWP) 格式
    # cookie = http.cookiejar.LWPCookieJar(file_path)

    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('https://www.baidu.com')
    cookie.save(ignore_discard=True, ignore_expires=True)

# get_cookies()
get_cookies_file()
