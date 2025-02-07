from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username = 'admin'
password = 'admin'
url = 'https://ssr3.scrape.center/'

p = HTTPPasswordMgrWithDefaultRealm()
# 添加用户名和密码
p.add_password(None, url, username, password)
# 实例化 HTTPBasicAuthHandler 对象
auth_handler = HTTPBasicAuthHandler(p)
# 构建 opener
opener = build_opener(auth_handler)

try:
    # 使用 opener 的 open() 打开链接
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)
