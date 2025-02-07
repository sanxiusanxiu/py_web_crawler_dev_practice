import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
}


def requests_ssl_error():
    r = requests.get('https://ssr2.scrape.center/')
    print(r.status_code)


def requests_verify_ignore():
    import urllib3
    # 设置忽略警告
    urllib3.disable_warnings()
    # 不验证SSL证书
    r = requests.get('https://ssr2.scrape.center/', headers=headers, verify=False)
    print(r.status_code)


def requests_verify_catch():
    import logging
    # 捕获警告到日志
    logging.captureWarnings(True)
    # 不验证SSL证书
    r = requests.get('https://ssr2.scrape.center/', verify=False)
    print(r.status_code)


# requests_ssl_error()
# requests_verify_ignore()
# requests_verify_ignore()