import requests

# 注，该代码未测通
proxies = {
    # 如果代理需要使用HTTP Basic Auth ，可以使用下面的语法格式
    'http': 'http://user:password@10.10.1.10:3128',
    # requests 还支持 SOCKS 协议的代理，注意需要安装 pip3 install 'requests[socks]'
    'https': 'socks5://user:password@10.10.1.10:3128',
}

requests.get('https://www.taobao.com', proxies=proxies)
