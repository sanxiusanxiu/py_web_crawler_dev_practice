import urllib.request
import ssl

# 全局取消证书验证，避免访问https网页报错
ssl._create_default_https_context = ssl._create_unverified_context

# 隧道域名:端口号
tunnel = "f766.kdltpspro.com:15818"

# 用户名密码方式
username = "t13961162503686"
password = "ppmrn3ul"
proxies = {
    "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel},
    "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel}
}

# 白名单方式（需提前设置白名单）
# proxies = {
#     "http": "http://%(proxy)s/" % {"proxy": tunnel},
#     "https": "http://%(proxy)s/" % {"proxy": tunnel}
# }

# 要访问的目标网页
target_url = 'https://httpbin.org/get'

# 使用隧道域名发送请求
proxy_support = urllib.request.ProxyHandler(proxies)
opener = urllib.request.build_opener(proxy_support)
# urllib.request.install_opener(opener)   注意此处是全局设置代理，如用这种写法进程内之后的所有urllib请求都会使用代理
# response = urllib.request.urlopen(target_url)
response = opener.open(target_url)

# 获取页面内容
if response.code == 200:
    print(response.read().decode('utf-8'))
