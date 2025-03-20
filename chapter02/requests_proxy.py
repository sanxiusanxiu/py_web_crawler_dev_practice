import requests

proxies = {
    # 如果代理需要使用 HTTP Basic Auth 认证，可以使用下面的语法格式
    'http': 'http://user:password@127.0.0.1:7890',
    # requests 还支持 SOCKS 协议的代理，注意需要安装 pip3 install 'requests[socks]'
    'https': 'socks5://user:password@127.0.0.1:7890',
}

requests.get('https://www.taobao.com', proxies=proxies)
