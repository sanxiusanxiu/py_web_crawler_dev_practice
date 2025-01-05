import requests


def requests_session_fore():
    # 请求这个测试网站时，可以设置一个cookie，名称叫做number，内容是123456789
    requests.get('https://httpbin.org/cookies/set/number/123456789')
    # 紧随其后请求该网站获取当前的cookies
    r = requests.get('https://httpbin.org/cookies')
    print(r.text)  # {"cookies": {}}  # 显然这是不行的


def requests_session_base():
    s = requests.Session()
    s.get('https://httpbin.org/cookies/set/number/123456789')
    r = s.get('https://httpbin.org/cookies')
    print(r.text)  # {"cookies": {"number": "123456789"}}


# requests_session_fore()
# requests_session_base()