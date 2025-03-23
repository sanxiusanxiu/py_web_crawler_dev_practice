
def proxy_simple():
    from urllib.error import URLError
    from urllib.request import ProxyHandler, build_opener

    # proxy = '20.219.137.240:3000'
    # 增加代理认证
    proxy = 'username:password@127.0.0.1:7890'

    # 使用ProxyHandler设置代理
    proxy_handler = ProxyHandler({
        'http': 'http://' + proxy,
        'https': 'https://' + proxy
    })

    # 使用build_opener方法创建一个Opener
    opener = build_opener(proxy_handler)

    try:
        # 调用Opener对象的open方法访问链接
        response = opener.open('https://httpbin.org/get')
        print(response.read().decode('utf-8'))
    except URLError as e:
        print(e.reason)


def proxy_socks():
    import socks
    import socket
    from urllib import request
    from urllib.error import URLError

    socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 7891)
    socket.socket = socks.socksocket

    try:
        response = request.urlopen('https://httpbin.org/get')
        print(response.read().decode('utf-8'))
    except URLError as e:
        print(e.reason)
