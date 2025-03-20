import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
}


def requests_ssl_error():
    r = requests.get('https://ssr2.scrape.center/')
    print(r.status_code)


def requests_ssl_ignore():
    import urllib3
    # 设置忽略警告
    urllib3.disable_warnings()
    # 不验证 SSL 证书
    r = requests.get('https://ssr2.scrape.center/', headers=headers, verify=False)
    print(r.status_code)


def requests_ssl_catch():
    import logging

    # 配置日志记录器
    logging.basicConfig(filename='requests_ssl_warnings.log', level=logging.INFO)
    # 捕获警告到日志
    logging.captureWarnings(True)
    # 不验证 SSL 证书
    r = requests.get('https://ssr2.scrape.center/', verify=False)
    print(r.status_code)


# requests_ssl_error()
# requests_ssl_ignore()
# requests_ssl_catch()
