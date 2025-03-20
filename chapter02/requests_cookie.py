import requests


def requests_cookie_base():
    r = requests.get('https://www.baidu.com')
    print(r.cookies)
    # items() 将 RequestsCookieJar 类型的 Cookies 转换为由元组组成的列表
    for key, value in r.cookies.items():
        print(key + '=' + value)


def requests_cookie_direct():
    headers = {
        'Cookie': '',
        'Host': 'www.baidu.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    }
    r = requests.get('https://www.baidu.com', headers=headers)
    print(r.text)

# requests_cookie_base()
# requests_cookie_direct()
